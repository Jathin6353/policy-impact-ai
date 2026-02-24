"""
Policy Scenarios for Simulation
Each scenario represents a potential/actual policy change
"""

POLICY_SCENARIOS = {
    "status_quo": {
        "id": "status_quo",
        "name": "Current Policy (Status Quo)",
        "description": "No changes — baseline scenario",
        "changes": {},
        "category": "baseline",
    },
    "tax_slab_reform_2025": {
        "id": "tax_slab_reform_2025",
        "name": "Proposed Tax Slab Reform 2025",
        "description": (
            "Wider tax slabs with higher exemption limit. "
            "Zero tax up to ₹4L, lower rates for middle class."
        ),
        "changes": {
            "tax_regime": "proposed_2025",
            "standard_deduction": 100000,
        },
        "category": "taxation",
        "impact_summary": "Benefits middle and lower-middle income groups",
    },
    "fuel_hike_10_percent": {
        "id": "fuel_hike_10_percent",
        "name": "Fuel Price Increase: 10%",
        "description": (
            "Petrol and diesel prices increase by 10% "
            "due to global crude oil surge."
        ),
        "changes": {
            "fuel_hike_percent": 10,
        },
        "category": "fuel",
        "impact_summary": "Increases transportation and food costs across all groups",
    },
    "fuel_hike_20_percent": {
        "id": "fuel_hike_20_percent",
        "name": "Fuel Price Increase: 20%",
        "description": "Major fuel price surge scenario.",
        "changes": {
            "fuel_hike_percent": 20,
        },
        "category": "fuel",
        "impact_summary": "Severe impact on lower and middle income households",
    },
    "subsidy_removal_lpg": {
        "id": "subsidy_removal_lpg",
        "name": "LPG Subsidy Removal",
        "description": (
            "Government removes LPG subsidy for all income groups."
        ),
        "changes": {
            "remove_subsidy": ["lpg_subsidy"],
        },
        "category": "subsidy",
        "impact_summary": "Directly impacts cooking fuel costs for all households",
    },
    "education_cess_increase": {
        "id": "education_cess_increase",
        "name": "Education Cess Increased to 6%",
        "description": (
            "Health and Education Cess on income tax increased "
            "from 4% to 6%."
        ),
        "changes": {
            "cess_rate": 0.06,
        },
        "category": "taxation",
        "impact_summary": "Small increase in effective tax rate for all taxpayers",
    },
    "gst_food_5_percent": {
        "id": "gst_food_5_percent",
        "name": "5% GST on Essential Food Items",
        "description": (
            "Previously exempt food items now attract 5% GST."
        ),
        "changes": {
            "food_gst_rate": 0.05,
            "affected_food_share": 0.60,  # 60% of food basket affected
        },
        "category": "taxation",
        "impact_summary": (
            "Disproportionately affects low-income households "
            "who spend more on food"
        ),
    },
    "inflation_spike_8_percent": {
        "id": "inflation_spike_8_percent",
        "name": "CPI Inflation Spikes to 8%",
        "description": (
            "Consumer price inflation rises to 8% annually."
        ),
        "changes": {
            "inflation_override": 8.0,
        },
        "category": "inflation",
        "impact_summary": "Erodes purchasing power, hits fixed-income groups hardest",
    },
    "interest_rate_hike": {
        "id": "interest_rate_hike",
        "name": "RBI Rate Hike: +1.5%",
        "description": (
            "RBI increases repo rate by 150 basis points. "
            "EMIs increase across all floating rate loans."
        ),
        "changes": {
            "interest_rate_change": 1.5,
        },
        "category": "monetary",
        "impact_summary": (
            "Increases EMI burden for home loans, "
            "auto loans, personal loans"
        ),
    },
    "universal_basic_income": {
        "id": "universal_basic_income",
        "name": "Universal Basic Income: ₹1000/month",
        "description": (
            "Government introduces UBI of ₹1000/month "
            "for all adults below ₹5L income."
        ),
        "changes": {
            "ubi_monthly": 1000,
            "ubi_income_limit": 500000,
        },
        "category": "welfare",
        "impact_summary": "Direct cash benefit for low-income groups",
    },
    "digital_india_subsidy": {
        "id": "digital_india_subsidy",
        "name": "Digital India: Internet Subsidy",
        "description": (
            "₹200/month internet subsidy for households "
            "earning below ₹8L."
        ),
        "changes": {
            "internet_subsidy_monthly": 200,
            "internet_subsidy_income_limit": 800000,
        },
        "category": "welfare",
        "impact_summary": "Reduces digital divide, helps students and WFH workers",
    },
}


def get_scenario(scenario_id: str) -> dict:
    """Retrieve a specific policy scenario"""
    return POLICY_SCENARIOS.get(scenario_id, POLICY_SCENARIOS["status_quo"])


def get_all_scenarios() -> dict:
    """Return all available scenarios"""
    return POLICY_SCENARIOS


def get_scenarios_by_category(category: str) -> list:
    """Filter scenarios by category"""
    return [
        s for s in POLICY_SCENARIOS.values()
        if s.get("category") == category
    ]