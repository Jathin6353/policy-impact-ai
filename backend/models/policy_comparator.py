"""
Policy Comparison Engine
Compare two policy scenarios side by side
"""
from models.tax_engine import TaxEngine
from models.inflation_engine import InflationEngine
from models.stress_scorer import StressScorer
from data.fuel_data import simulate_fuel_hike_impact, calculate_monthly_fuel_cost
from data.subsidy_rules import check_subsidy_eligibility
from data.inflation_data import get_income_bracket
from data.policy_scenarios import get_scenario


class PolicyComparator:
    """Compare impact of two different policy scenarios"""

    def __init__(self, user_profile: dict):
        self.profile = user_profile
        self.income = user_profile["annual_income"]
        self.family_size = user_profile.get("family_size", 4)
        self.occupation = user_profile.get("occupation", "salaried")
        self.state = user_profile.get("state", "default")
        self.monthly_emi = user_profile.get("monthly_emi", 0)
        self.bracket = get_income_bracket(self.income)

    def simulate_scenario(self, scenario_id: str) -> dict:
        """Run full simulation for a single scenario"""
        scenario = get_scenario(scenario_id)
        changes = scenario.get("changes", {})

        # --- Tax Calculation ---
        tax_year = "2024"
        custom_cess = None
        custom_std_ded = None

        if "tax_regime" in changes and changes["tax_regime"] == "proposed_2025":
            tax_year = "2025_proposed"
        if "cess_rate" in changes:
            custom_cess = changes["cess_rate"]
        if "standard_deduction" in changes:
            custom_std_ded = changes["standard_deduction"]

        tax_engine = TaxEngine("new", tax_year)
        tax_result = tax_engine.compute_full_tax(
            self.income,
            custom_cess_rate=custom_cess,
            custom_standard_deduction=custom_std_ded,
        )

        # --- Inflation Impact ---
        inflation_override = changes.get("inflation_override", None)
        infl_engine = InflationEngine(self.income, self.family_size)
        inflation_result = infl_engine.calculate_category_inflation(
            inflation_override
        )

        # --- Fuel Impact ---
        fuel_impact = {"total_monthly_increase": 0, "annual_impact": 0}
        if "fuel_hike_percent" in changes:
            fuel_impact = simulate_fuel_hike_impact(
                changes["fuel_hike_percent"],
                self.bracket,
                self.income,
            )

        # --- Food GST ---
        food_gst_impact = {"annual_gst_burden": 0}
        if "food_gst_rate" in changes:
            food_gst_impact = infl_engine.calculate_food_gst_impact(
                changes["food_gst_rate"],
                changes.get("affected_food_share", 0.6),
            )

        # --- Subsidies ---
        subsidies = check_subsidy_eligibility(
            self.income,
            self.occupation,
            self.family_size,
            self.state,
        )
        total_subsidy = sum(s["annual_benefit"] for s in subsidies)

        # Remove subsidies if scenario dictates
        if "remove_subsidy" in changes:
            for scheme in changes["remove_subsidy"]:
                for s in subsidies:
                    if s["scheme"] == scheme and s["eligible"]:
                        total_subsidy -= s["annual_benefit"]
                        s["eligible"] = False
                        s["annual_benefit"] = 0
                        s["reasons"] = [
                            "Removed under this policy scenario"
                        ]

        # --- UBI ---
        ubi_benefit = 0
        if "ubi_monthly" in changes:
            if self.income <= changes.get("ubi_income_limit", float("inf")):
                ubi_benefit = changes["ubi_monthly"] * 12

        # --- Internet Subsidy ---
        internet_benefit = 0
        if "internet_subsidy_monthly" in changes:
            limit = changes.get("internet_subsidy_income_limit", float("inf"))
            if self.income <= limit:
                internet_benefit = changes["internet_subsidy_monthly"] * 12

        # --- EMI Impact ---
        emi_change = 0
        if "interest_rate_change" in changes:
            # Rough estimate: each 1% rate increase → ~7% EMI increase
            emi_change = (
                self.monthly_emi
                * changes["interest_rate_change"]
                * 0.07
            )

        # --- Net Impact Calculation ---
        total_negative_impact = (
            tax_result["total_tax"]
            + inflation_result["total_annual_increase"]
            + fuel_impact["annual_impact"]
            + food_gst_impact["annual_gst_burden"]
            + (emi_change * 12)
        )

        total_positive_impact = total_subsidy + ubi_benefit + internet_benefit

        net_disposable = (
            self.income
            - total_negative_impact
            + total_positive_impact
        )

        monthly_disposable = net_disposable / 12

        return {
            "scenario": scenario,
            "tax": tax_result,
            "inflation": inflation_result,
            "fuel_impact": fuel_impact,
            "food_gst_impact": food_gst_impact,
            "subsidies": subsidies,
            "total_subsidy_benefit": total_subsidy,
            "ubi_benefit": ubi_benefit,
            "internet_benefit": internet_benefit,
            "emi_monthly_change": round(emi_change, 2),
            "total_negative_annual": round(total_negative_impact, 2),
            "total_positive_annual": round(total_positive_impact, 2),
            "net_disposable_annual": round(net_disposable, 2),
            "net_disposable_monthly": round(monthly_disposable, 2),
        }

    def compare(self, scenario_a_id: str, scenario_b_id: str) -> dict:
        """Compare two scenarios"""
        result_a = self.simulate_scenario(scenario_a_id)
        result_b = self.simulate_scenario(scenario_b_id)

        diff_annual = (
            result_b["net_disposable_annual"]
            - result_a["net_disposable_annual"]
        )
        diff_monthly = (
            result_b["net_disposable_monthly"]
            - result_a["net_disposable_monthly"]
        )
        diff_tax = result_b["tax"]["total_tax"] - result_a["tax"]["total_tax"]

        # Stress scoring
        scorer = StressScorer()

        stress_a = scorer.calculate_stress_index(
            self.income,
            result_a["tax"]["total_tax"],
            self.monthly_emi,
            self.family_size,
            (
                result_a["net_disposable_annual"]
                / self.income
                * 100
                if self.income > 0
                else 0
            ),
            self.occupation,
            result_a["inflation"]["total_annual_increase"],
            result_a["total_subsidy_benefit"],
        )

        stress_b = scorer.calculate_stress_index(
            self.income,
            result_b["tax"]["total_tax"],
            self.monthly_emi + result_b.get("emi_monthly_change", 0),
            self.family_size,
            (
                result_b["net_disposable_annual"]
                / self.income
                * 100
                if self.income > 0
                else 0
            ),
            self.occupation,
            result_b["inflation"]["total_annual_increase"],
            result_b["total_subsidy_benefit"],
        )

        return {
            "user_profile": self.profile,
            "scenario_a": result_a,
            "scenario_b": result_b,
            "comparison": {
                "disposable_income_diff_annual": round(diff_annual, 2),
                "disposable_income_diff_monthly": round(diff_monthly, 2),
                "tax_difference": round(diff_tax, 2),
                "better_scenario": (
                    scenario_b_id if diff_annual > 0 else scenario_a_id
                ),
                "impact_direction": (
                    "positive" if diff_annual > 0 else "negative"
                ),
                "percent_change": round(
                    abs(diff_annual)
                    / max(result_a["net_disposable_annual"], 1)
                    * 100,
                    2,
                ),
            },
            "stress_a": stress_a,
            "stress_b": stress_b,
            "stress_change": round(
                stress_b["composite_score"]
                - stress_a["composite_score"],
                1,
            ),
        }