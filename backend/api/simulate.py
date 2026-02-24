"""
Simulation API Routes
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from models.tax_engine import TaxEngine, compare_tax_regimes
from models.inflation_engine import InflationEngine
from models.monte_carlo import MonteCarloEngine
from models.stress_scorer import StressScorer
from models.policy_comparator import PolicyComparator
from data.subsidy_rules import check_subsidy_eligibility
from data.fuel_data import simulate_fuel_hike_impact
from data.inflation_data import get_income_bracket
from data.policy_scenarios import get_all_scenarios

router = APIRouter()


class UserProfile(BaseModel):
    annual_income: float = Field(..., gt=0, description="Annual income in INR")
    state: str = Field(default="default", description="State of residence")
    family_size: int = Field(default=4, ge=1, le=20)
    occupation: str = Field(default="salaried")
    monthly_emi: float = Field(default=0, ge=0)
    investments_80c: float = Field(default=0, ge=0)
    health_insurance: float = Field(default=0, ge=0)
    fuel_usage: str = Field(default="moderate")
    education_expenses: float = Field(default=0, ge=0)
    has_land: bool = Field(default=False)
    education_level: str = Field(default="none")
    tax_regime: str = Field(default="new")


class SimulationRequest(BaseModel):
    profile: UserProfile
    scenario_id: str = Field(default="status_quo")


class ComparisonRequest(BaseModel):
    profile: UserProfile
    scenario_a: str = Field(default="status_quo")
    scenario_b: str


@router.get("/scenarios")
async def list_scenarios():
    """List all available policy scenarios"""
    return {"scenarios": get_all_scenarios()}


@router.post("/full-simulation")
async def run_full_simulation(request: SimulationRequest):
    """Run complete impact simulation for a user profile"""
    profile = request.profile
    bracket = get_income_bracket(profile.annual_income)

    comparator = PolicyComparator({
        "annual_income": profile.annual_income,
        "family_size": profile.family_size,
        "occupation": profile.occupation,
        "state": profile.state,
        "monthly_emi": profile.monthly_emi,
    })

    # Run simulation
    simulation = comparator.simulate_scenario(request.scenario_id)

    # Monte Carlo projection
    mc = MonteCarloEngine(num_simulations=500)
    expense_ratio = 1 - (
        simulation["net_disposable_annual"] / profile.annual_income
        if profile.annual_income > 0
        else 0.8
    )
    expense_ratio = max(0.3, min(0.95, expense_ratio))

    projection = mc.simulate_income_trajectory(
        current_income=profile.annual_income,
        years=3,
        expense_ratio=expense_ratio,
    )

    # Stress score
    scorer = StressScorer()
    stress = scorer.calculate_stress_index(
        profile.annual_income,
        simulation["tax"]["total_tax"],
        profile.monthly_emi,
        profile.family_size,
        max(
            0,
            simulation["net_disposable_annual"]
            / profile.annual_income
            * 100
            if profile.annual_income > 0
            else 0,
        ),
        profile.occupation,
        simulation["inflation"]["total_annual_increase"],
        simulation["total_subsidy_benefit"],
    )

    # Tax regime comparison
    tax_comparison = compare_tax_regimes(
        profile.annual_income,
        investments_80c=profile.investments_80c,
        health_insurance=profile.health_insurance,
    )

    # Inflation projection
    infl_engine = InflationEngine(profile.annual_income, profile.family_size)
    expense_projection = infl_engine.project_expenses(years=3)

    # Generate human-readable insights
    insights = _generate_insights(
        simulation, stress, profile, request.scenario_id
    )

    return {
        "profile": {
            "annual_income": profile.annual_income,
            "income_bracket": bracket,
            "family_size": profile.family_size,
            "occupation": profile.occupation,
            "state": profile.state,
        },
        "simulation": simulation,
        "stress_index": stress,
        "monte_carlo": projection,
        "tax_comparison": tax_comparison,
        "expense_projection": expense_projection,
        "insights": insights,
    }


@router.post("/compare")
async def compare_policies(request: ComparisonRequest):
    """Compare two policy scenarios"""
    comparator = PolicyComparator({
        "annual_income": request.profile.annual_income,
        "family_size": request.profile.family_size,
        "occupation": request.profile.occupation,
        "state": request.profile.state,
        "monthly_emi": request.profile.monthly_emi,
    })

    result = comparator.compare(request.scenario_a, request.scenario_b)

    # Generate comparison insights
    insights = _generate_comparison_insights(result)
    result["insights"] = insights

    return result


@router.post("/quick-tax")
async def quick_tax_calculation(profile: UserProfile):
    """Quick tax calculation only"""
    engine = TaxEngine(profile.tax_regime, "2024")
    result = engine.compute_full_tax(
        profile.annual_income,
        investments_80c=profile.investments_80c,
        health_insurance=profile.health_insurance,
    )
    comparison = compare_tax_regimes(
        profile.annual_income,
        investments_80c=profile.investments_80c,
        health_insurance=profile.health_insurance,
    )
    return {"tax": result, "regime_comparison": comparison}


@router.post("/subsidies")
async def check_subsidies(profile: UserProfile):
    """Check subsidy eligibility"""
    subsidies = check_subsidy_eligibility(
        profile.annual_income,
        profile.occupation,
        profile.family_size,
        profile.state,
        profile.has_land,
        profile.education_level,
    )
    total = sum(s["annual_benefit"] for s in subsidies)
    return {
        "subsidies": subsidies,
        "total_annual_benefit": total,
        "monthly_benefit": round(total / 12, 2),
    }


def _generate_insights(
    simulation: dict,
    stress: dict,
    profile,
    scenario_id: str,
) -> list:
    """Generate human-readable insights"""
    insights = []
    monthly_income = profile.annual_income / 12

    # Tax insight
    tax_pct = simulation["tax"]["effective_rate"]
    insights.append({
        "category": "tax",
        "icon": "💰",
        "text": (
            f"Your effective tax rate is {tax_pct}%. "
            f"You pay ₹{simulation['tax']['monthly_tax']:,.0f}/month in taxes."
        ),
        "severity": (
            "low" if tax_pct < 10 else "medium" if tax_pct < 20 else "high"
        ),
    })

    # Inflation insight
    infl_monthly = simulation["inflation"]["total_monthly_increase"]
    infl_pct = simulation["inflation"]["purchasing_power_loss_percent"]
    insights.append({
        "category": "inflation",
        "icon": "📈",
        "text": (
            f"Inflation will erode ₹{infl_monthly:,.0f}/month "
            f"from your purchasing power ({infl_pct}% annual loss)."
        ),
        "severity": (
            "low" if infl_pct < 3 else "medium" if infl_pct < 6 else "high"
        ),
    })

    # Fuel insight
    if simulation["fuel_impact"]["annual_impact"] > 0:
        fuel_annual = simulation["fuel_impact"]["annual_impact"]
        insights.append({
            "category": "fuel",
            "icon": "⛽",
            "text": (
                f"Fuel price changes will cost you an additional "
                f"₹{fuel_annual:,.0f}/year "
                f"(₹{fuel_annual / 12:,.0f}/month)."
            ),
            "severity": (
                "low"
                if fuel_annual < 5000
                else "medium"
                if fuel_annual < 15000
                else "high"
            ),
        })

    # Subsidy insight
    total_subsidy = simulation["total_subsidy_benefit"]
    if total_subsidy > 0:
        insights.append({
            "category": "subsidy",
            "icon": "🏛️",
            "text": (
                f"You are eligible for ₹{total_subsidy:,.0f}/year "
                f"in government subsidies."
            ),
            "severity": "positive",
        })

    # Stress insight
    insights.append({
        "category": "stress",
        "icon": "🎯",
        "text": (
            f"Your Financial Stress Index is {stress['composite_score']}/100 "
            f"({stress['risk_level']}). {stress['risk_description']}"
        ),
        "severity": (
            "low"
            if stress["composite_score"] < 40
            else "medium"
            if stress["composite_score"] < 70
            else "high"
        ),
    })

    # Disposable income insight
    disposable = simulation["net_disposable_monthly"]
    insights.append({
        "category": "disposable",
        "icon": "💵",
        "text": (
            f"After all impacts, your effective monthly disposable income "
            f"is ₹{disposable:,.0f}."
        ),
        "severity": (
            "low"
            if disposable > monthly_income * 0.3
            else "medium"
            if disposable > monthly_income * 0.15
            else "high"
        ),
    })

    return insights


def _generate_comparison_insights(comparison: dict) -> list:
    """Generate insights for policy comparison"""
    insights = []
    diff = comparison["comparison"]

    direction = "better" if diff["impact_direction"] == "positive" else "worse"
    scenario_b_name = comparison["scenario_b"]["scenario"]["name"]

    insights.append({
        "icon": "⚖️",
        "text": (
            f"Under '{scenario_b_name}', "
            f"you are ₹{abs(diff['disposable_income_diff_monthly']):,.0f}/month "
            f"{direction} off."
        ),
    })

    if diff["tax_difference"] != 0:
        tax_dir = "more" if diff["tax_difference"] > 0 else "less"
        insights.append({
            "icon": "💰",
            "text": (
                f"You pay ₹{abs(diff['tax_difference']):,.0f}/year "
                f"{tax_dir} in taxes."
            ),
        })

    stress_change = comparison["stress_change"]
    if abs(stress_change) > 2:
        stress_dir = "increases" if stress_change > 0 else "decreases"
        insights.append({
            "icon": "🎯",
            "text": (
                f"Your financial stress {stress_dir} by "
                f"{abs(stress_change)} points."
            ),
        })

    return insights