"""
Policy Scenarios for Simulation — FY 2026-27
Based on Union Budget 2026-27 and potential policy changes

Source: https://www.indiabudget.gov.in
"""

POLICY_SCENARIOS = {
    # ====== BASELINE ======
    "status_quo": {
        "id": "status_quo",
        "name": "Budget 2026-27 (Current)",
        "name_hi": "बजट 2026-27 (वर्तमान)",
        "description": "Current policy as per Union Budget 2026-27 presented on 1 Feb 2026",
        "changes": {
            "budget_year": "2026-27",
            "tax_regime": "new_2026",
        },
        "category": "baseline",
        "impact_summary": "Baseline scenario with Budget 2026-27 tax slabs and policies",
        "source": "Union Budget 2026-27",
    },
    
    "pre_budget_2024": {
        "id": "pre_budget_2024",
        "name": "Pre-Budget 2024 (Old Policy)",
        "name_hi": "बजट 2024 से पहले (पुरानी नीति)",
        "description": "Compare with policies before Budget 2024",
        "changes": {
            "budget_year": "2024-25",
            "tax_regime": "new_2024",
            "standard_deduction": 50000,
            "rebate_limit": 700000,
        },
        "category": "comparison",
        "impact_summary": "Shows improvement from Budget 2026 vs earlier policies",
        "source": "Budget 2024-25",
    },
    
    # ====== TAX SCENARIOS ======
    "tax_regime_old": {
        "id": "tax_regime_old",
        "name": "Switch to Old Tax Regime",
        "name_hi": "पुरानी कर व्यवस्था में बदलें",
        "description": "Calculate taxes under old regime with deductions (80C, 80D, HRA)",
        "changes": {
            "tax_regime": "old_2026",
            "deductions_available": True,
        },
        "category": "taxation",
        "impact_summary": "May benefit those with high investments and HRA claims",
    },
    
    "future_tax_reform": {
        "id": "future_tax_reform",
        "name": "Proposed Tax Reform 2027",
        "name_hi": "प्रस्तावित कर सुधार 2027",
        "description": "Speculated further simplification: Zero tax up to ₹5L, wider slabs",
        "changes": {
            "tax_regime": "proposed_2027",
            "zero_tax_limit": 500000,
            "standard_deduction": 125000,
            "rebate_limit": 1500000,
        },
        "category": "taxation",
        "impact_summary": "Hypothetical future reform scenario",
        "disclaimer": "This is a speculative scenario, not official policy",
    },
    
    "cess_increase_6": {
        "id": "cess_increase_6",
        "name": "Education Cess → 6%",
        "name_hi": "शिक्षा उपकर → 6%",
        "description": "Health & Education Cess increased from 4% to 6%",
        "changes": {
            "cess_rate": 0.06,
        },
        "category": "taxation",
        "impact_summary": "2% additional tax burden on all taxpayers",
    },
    
    # ====== FUEL SCENARIOS ======
    "fuel_hike_10": {
        "id": "fuel_hike_10",
        "name": "Fuel Price +10%",
        "name_hi": "ईंधन मूल्य +10%",
        "description": "Petrol & diesel prices increase 10% due to global crude surge",
        "changes": {
            "fuel_hike": 10,
            "petrol_increase": 10.5,  # ₹10.5/litre
            "diesel_increase": 9.1,   # ₹9.1/litre
            "lpg_increase": 90,       # ₹90/cylinder
        },
        "category": "fuel",
        "impact_summary": "Cascade effect on transport, food, and manufacturing costs",
    },
    
    "fuel_hike_20": {
        "id": "fuel_hike_20",
        "name": "Fuel Price +20%",
        "name_hi": "ईंधन मूल्य +20%",
        "description": "Major fuel price surge scenario (crisis level)",
        "changes": {
            "fuel_hike": 20,
            "petrol_increase": 21,
            "diesel_increase": 18.3,
            "lpg_increase": 180,
        },
        "category": "fuel",
        "impact_summary": "Severe impact on lower and middle income households",
    },
    
    "fuel_cut_10": {
        "id": "fuel_cut_10",
        "name": "Fuel Price -10% (Subsidy)",
        "name_hi": "ईंधन मूल्य -10% (सब्सिडी)",
        "description": "Government introduces fuel subsidy to reduce prices",
        "changes": {
            "fuel_hike": -10,
            "petrol_decrease": 10.5,
            "diesel_decrease": 9.1,
        },
        "category": "fuel",
        "impact_summary": "Relief for all households, especially transport sector",
    },
    
    # ====== SUBSIDY SCENARIOS ======
    "subsidy_removal_lpg": {
        "id": "subsidy_removal_lpg",
        "name": "LPG Subsidy Removal",
        "name_hi": "LPG सब्सिडी हटाना",
        "description": "Government removes LPG subsidy for all income groups",
        "changes": {
            "remove_subsidy": ["lpg_subsidy"],
            "lpg_market_price": True,
        },
        "category": "subsidy",
        "impact_summary": "₹2400/year additional burden per household",
    },
    
    "food_subsidy_reduction": {
        "id": "food_subsidy_reduction",
        "name": "NFSA Coverage Reduction",
        "name_hi": "NFSA कवरेज में कटौती",
        "description": "Food subsidy eligibility reduced to only AAY households",
        "changes": {
            "food_subsidy_eligibility": "AAY_only",
            "beneficiary_reduction_percent": 50,
        },
        "category": "subsidy",
        "impact_summary": "40 crore people lose subsidized ration access",
    },
    
    "ayushman_expansion": {
        "id": "ayushman_expansion",
        "name": "Ayushman Bharat → ₹10L",
        "name_hi": "आयुष्मान भारत → ₹10L",
        "description": "Health coverage increased from ₹7L to ₹10L per family",
        "changes": {
            "ayushman_coverage": 1000000,
            "income_limit_increase": 800000,
        },
        "category": "subsidy",
        "impact_summary": "Better health security for 60 crore+ Indians",
    },
    
    # ====== INFLATION SCENARIOS ======
    "inflation_7": {
        "id": "inflation_7",
        "name": "Inflation Rises to 7%",
        "name_hi": "मुद्रास्फीति 7% तक बढ़ी",
        "description": "CPI inflation increases to 7% annually",
        "changes": {
            "inflation_override": 7.0,
        },
        "category": "inflation",
        "impact_summary": "Moderate erosion of purchasing power",
    },
    
    "inflation_10": {
        "id": "inflation_10",
        "name": "Inflation Spikes to 10%",
        "name_hi": "मुद्रास्फीति 10% तक बढ़ी",
        "description": "Severe inflation scenario (2022 levels)",
        "changes": {
            "inflation_override": 10.0,
        },
        "category": "inflation",
        "impact_summary": "Severe purchasing power erosion, especially food & fuel",
    },
    
    "deflation_2": {
        "id": "deflation_2",
        "name": "Low Inflation (3%)",
        "name_hi": "कम मुद्रास्फीति (3%)",
        "description": "Inflation falls to RBI's ideal target",
        "changes": {
            "inflation_override": 3.0,
        },
        "category": "inflation",
        "impact_summary": "Improved purchasing power, stable prices",
    },
    
    # ====== MONETARY POLICY SCENARIOS ======
    "rbi_rate_hike_1": {
        "id": "rbi_rate_hike_1",
        "name": "RBI Rate Hike +1%",
        "name_hi": "RBI दर वृद्धि +1%",
        "description": "RBI increases repo rate by 100 basis points",
        "changes": {
            "interest_rate_change": 1.0,
            "emi_increase_percent": 7,
        },
        "category": "monetary",
        "impact_summary": "EMI increases ~7%, home loans become expensive",
    },
    
    "rbi_rate_cut_1": {
        "id": "rbi_rate_cut_1",
        "name": "RBI Rate Cut -1%",
        "name_hi": "RBI दर कटौती -1%",
        "description": "RBI reduces repo rate by 100 basis points",
        "changes": {
            "interest_rate_change": -1.0,
            "emi_decrease_percent": 7,
        },
        "category": "monetary",
        "impact_summary": "EMI decreases ~7%, cheaper loans",
    },
    
    # ====== GST SCENARIOS ======
    "gst_food_5": {
        "id": "gst_food_5",
        "name": "5% GST on Food Items",
        "name_hi": "खाद्य पदार्थों पर 5% GST",
        "description": "Previously exempt packaged food items attract 5% GST",
        "changes": {
            "food_gst": 0.05,
            "affected_food_share": 0.60,
        },
        "category": "taxation",
        "impact_summary": "Disproportionately affects low-income households",
    },
    
    "gst_simplification": {
        "id": "gst_simplification",
        "name": "GST Simplified (3 Slabs)",
        "name_hi": "GST सरलीकरण (3 स्लैब)",
        "description": "GST reduced to 3 slabs: 5%, 12%, 18%",
        "changes": {
            "gst_slabs": [5, 12, 18],
            "average_gst_reduction": 2,
        },
        "category": "taxation",
        "impact_summary": "Simplification with marginal price reduction",
    },
    
    # ====== WELFARE SCENARIOS ======
    "ubi_1000": {
        "id": "ubi_1000",
        "name": "UBI ₹1000/month",
        "name_hi": "UBI ₹1000/माह",
        "description": "Universal Basic Income of ₹1000/month for adults below ₹5L",
        "changes": {
            "ubi_monthly": 1000,
            "ubi_income_limit": 500000,
        },
        "category": "welfare",
        "impact_summary": "₹12,000/year direct benefit for low-income",
    },
    
    "ubi_2000": {
        "id": "ubi_2000",
        "name": "UBI ₹2000/month",
        "name_hi": "UBI ₹2000/माह",
        "description": "Enhanced UBI of ₹2000/month (election year scenario)",
        "changes": {
            "ubi_monthly": 2000,
            "ubi_income_limit": 800000,
        },
        "category": "welfare",
        "impact_summary": "₹24,000/year direct benefit",
    },
    
    "pm_kisan_increase": {
        "id": "pm_kisan_increase",
        "name": "PM-KISAN → ₹8000/year",
        "name_hi": "PM-KISAN → ₹8000/वर्ष",
        "description": "PM-KISAN increased from ₹6000 to ₹8000 per year",
        "changes": {
            "pm_kisan_amount": 8000,
        },
        "category": "welfare",
        "impact_summary": "₹2000 additional for 11 crore farmers",
    },
    
    # ====== INFRASTRUCTURE IMPACT ======
    "capex_boost": {
        "id": "capex_boost",
        "name": "Infrastructure Capex +20%",
        "name_hi": "इंफ्रास्ट्रक्चर कैपेक्स +20%",
        "description": "Government capex increased to ₹14.6 lakh crore",
        "changes": {
            "capex_increase_percent": 20,
            "job_creation_lakh": 50,
        },
        "category": "infrastructure",
        "impact_summary": "Job creation in construction, manufacturing",
    },
    
    # ====== EMPLOYMENT SCENARIOS ======
    "employment_incentive": {
        "id": "employment_incentive",
        "name": "Employment-Linked Incentive",
        "name_hi": "रोजगार-लिंक्ड प्रोत्साहन",
        "description": "₹15,000 incentive for first-time employees (Budget 2026)",
        "changes": {
            "employment_incentive": 15000,
            "epfo_subsidy_months": 24,
        },
        "category": "employment",
        "impact_summary": "50 lakh jobs targeted through incentives",
        "source": "Budget 2026-27",
    },
    
    # ====== SECTORAL POLICIES ======
    "semiconductor_impact": {
        "id": "semiconductor_impact",
        "name": "Semiconductor Mission 2.0",
        "name_hi": "सेमीकंडक्टर मिशन 2.0",
        "description": "₹76,000 Cr investment in semiconductor ecosystem",
        "changes": {
            "sector_boost": "semiconductor",
            "investment_cr": 76000,
            "jobs_created_lakh": 10,
        },
        "category": "manufacturing",
        "impact_summary": "High-skill job creation in electronics sector",
        "source": "Budget 2026-27",
    },
    
    "green_hydrogen_push": {
        "id": "green_hydrogen_push",
        "name": "Green Hydrogen Mission",
        "name_hi": "ग्रीन हाइड्रोजन मिशन",
        "description": "₹19,700 Cr for green hydrogen production",
        "changes": {
            "sector_boost": "green_energy",
            "investment_cr": 19700,
            "emission_reduction_mt": 50,
        },
        "category": "energy",
        "impact_summary": "5 MT green hydrogen production by 2030",
        "source": "Budget 2026-27",
    },
    
    # ====== MARKET SCENARIOS ======
    "stt_impact": {
        "id": "stt_impact",
        "name": "New STT Rates (Budget 2026)",
        "name_hi": "नई STT दरें (बजट 2026)",
        "description": "STT increased: 0.05% Futures, 0.15% Options",
        "changes": {
            "stt_futures": 0.0005,
            "stt_options": 0.0015,
        },
        "category": "taxation",
        "impact_summary": "Higher trading costs to curb speculation",
        "source": "Budget 2026-27",
    },
}

# ============================================
# SCENARIO CATEGORIES
# ============================================
SCENARIO_CATEGORIES = {
    "baseline": {
        "name": "Baseline",
        "name_hi": "आधार रेखा",
        "icon": "📊",
        "color": "#6366f1",
    },
    "comparison": {
        "name": "Historical Comparison",
        "name_hi": "ऐतिहासिक तुलना",
        "icon": "📅",
        "color": "#8b5cf6",
    },
    "taxation": {
        "name": "Tax Policy",
        "name_hi": "कर नीति",
        "icon": "💰",
        "color": "#f59e0b",
    },
    "fuel": {
        "name": "Fuel Price",
        "name_hi": "ईंधन मूल्य",
        "icon": "⛽",
        "color": "#ef4444",
    },
    "subsidy": {
        "name": "Subsidies",
        "name_hi": "सब्सिडी",
        "icon": "🏛️",
        "color": "#22c55e",
    },
    "inflation": {
        "name": "Inflation",
        "name_hi": "मुद्रास्फीति",
        "icon": "📈",
        "color": "#f97316",
    },
    "monetary": {
        "name": "Monetary Policy",
        "name_hi": "मौद्रिक नीति",
        "icon": "🏦",
        "color": "#3b82f6",
    },
    "welfare": {
        "name": "Welfare",
        "name_hi": "कल्याण",
        "icon": "🤝",
        "color": "#10b981",
    },
    "employment": {
        "name": "Employment",
        "name_hi": "रोजगार",
        "icon": "👷",
        "color": "#06b6d4",
    },
    "infrastructure": {
        "name": "Infrastructure",
        "name_hi": "बुनियादी ढांचा",
        "icon": "🏗️",
        "color": "#64748b",
    },
    "manufacturing": {
        "name": "Manufacturing",
        "name_hi": "विनिर्माण",
        "icon": "🏭",
        "color": "#475569",
    },
    "energy": {
        "name": "Energy",
        "name_hi": "ऊर्जा",
        "icon": "⚡",
        "color": "#84cc16",
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


def get_category_info(category: str) -> dict:
    """Get category display information"""
    return SCENARIO_CATEGORIES.get(category, {})


def get_budget_2026_scenarios() -> list:
    """Get scenarios directly from Budget 2026-27"""
    return [
        s for s in POLICY_SCENARIOS.values()
        if s.get("source") == "Budget 2026-27"
    ]