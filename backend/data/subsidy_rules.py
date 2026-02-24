"""
Government Subsidy Eligibility Rules
Based on publicly available scheme guidelines
"""

SUBSIDIES = {
    "pm_kisan": {
        "name": "PM-KISAN Samman Nidhi",
        "amount_annual": 6000,
        "frequency": "3 installments of ₹2000",
        "eligibility": {
            "occupation": ["farmer", "agriculture"],
            "max_income": None,  # No income limit but institutional landholders excluded
            "land_required": True,
        },
        "description": "Direct income support to farmer families"
    },
    "lpg_subsidy": {
        "name": "LPG Subsidy (PMUY)",
        "amount_per_cylinder": 200,
        "max_cylinders_year": 12,
        "amount_annual": 2400,
        "eligibility": {
            "max_income": 1000000,
            "bpl_priority": True,
        },
        "description": "Subsidized LPG cylinders for eligible households"
    },
    "food_subsidy": {
        "name": "National Food Security Act (NFSA)",
        "amount_monthly": 700,  # Approximate value of subsidized ration
        "amount_annual": 8400,
        "eligibility": {
            "max_income": 300000,
            "priority_household": True,
        },
        "description": "Subsidized food grains at ₹1-3/kg"
    },
    "education_scholarship": {
        "name": "Central Sector Scholarship",
        "amount_annual": 20000,
        "eligibility": {
            "max_income": 800000,
            "education_level": ["undergraduate", "postgraduate"],
        },
        "description": "Merit-based scholarship for higher education"
    },
    "ayushman_bharat": {
        "name": "Ayushman Bharat (PMJAY)",
        "coverage": 500000,
        "premium_equivalent": 5000,
        "amount_annual": 5000,  # Insurance value per year
        "eligibility": {
            "max_income": 500000,
            "deprivation_criteria": True,
        },
        "description": "Health insurance cover of ₹5 lakh per family"
    },
    "pm_awas_yojana": {
        "name": "PM Awas Yojana",
        "subsidy_amount": 267000,  # Interest subsidy over loan period
        "amount_annual": 26700,  # Amortized over ~10 years
        "eligibility": {
            "max_income": 1800000,  # MIG-II limit
            "income_tiers": {
                "ews": {"max": 300000, "subsidy_rate": 0.065},
                "lig": {"max": 600000, "subsidy_rate": 0.065},
                "mig1": {"max": 1200000, "subsidy_rate": 0.04},
                "mig2": {"max": 1800000, "subsidy_rate": 0.03},
            }
        },
        "description": "Interest subsidy on home loans"
    },
    "mudra_loan": {
        "name": "PM MUDRA Yojana",
        "max_loan": 1000000,
        "interest_subsidy_rate": 0.02,
        "amount_annual": 10000,
        "eligibility": {
            "occupation": ["self_employed", "small_business", "entrepreneur"],
            "max_income": 1500000,
        },
        "description": "Collateral-free loans for small businesses"
    },
}


def check_subsidy_eligibility(
    annual_income: float,
    occupation: str,
    family_size: int,
    state: str,
    has_land: bool = False,
    education_level: str = "none"
) -> list:
    """Check which subsidies a citizen is eligible for"""
    eligible = []

    for key, subsidy in SUBSIDIES.items():
        rules = subsidy["eligibility"]
        is_eligible = True
        reasons = []

        # Income check
        if "max_income" in rules and rules["max_income"]:
            if annual_income > rules["max_income"]:
                is_eligible = False
                reasons.append(
                    f"Income exceeds ₹{rules['max_income']:,.0f} limit"
                )

        # Occupation check
        if "occupation" in rules:
            if occupation.lower() not in [
                o.lower() for o in rules["occupation"]
            ]:
                is_eligible = False
                reasons.append(
                    f"Occupation must be: {', '.join(rules['occupation'])}"
                )

        # Land check
        if "land_required" in rules and rules["land_required"]:
            if not has_land:
                is_eligible = False
                reasons.append("Agricultural land ownership required")

        # Education check
        if "education_level" in rules:
            if education_level.lower() not in [
                e.lower() for e in rules["education_level"]
            ]:
                is_eligible = False
                reasons.append(
                    f"Education level must be: "
                    f"{', '.join(rules['education_level'])}"
                )

        eligible.append({
            "scheme": key,
            "name": subsidy["name"],
            "eligible": is_eligible,
            "annual_benefit": subsidy.get("amount_annual", 0) if is_eligible else 0,
            "description": subsidy["description"],
            "reasons": reasons if not is_eligible else ["All criteria met"],
        })

    return eligible