"""
Government Subsidy Eligibility Rules — FY 2026-27
Based on Union Budget 2026-27 and active government schemes

Sources:
- https://www.indiabudget.gov.in
- https://pmkisan.gov.in
- https://pmjay.gov.in
- https://pmaymis.gov.in
- https://pmuy.gov.in
"""

# ============================================
# ACTIVE GOVERNMENT SCHEMES 2026-27
# ============================================
SUBSIDIES = {
    # ====== AGRICULTURE SUBSIDIES ======
    "pm_kisan": {
        "name": "PM-KISAN Samman Nidhi",
        "amount_annual": 6000,
        "frequency": "3 installments of ₹2000",
        "installment_amount": 2000,
        "eligibility": {
            "occupation": ["farmer", "agriculture"],
            "max_income": None,  # No income limit
            "land_required": True,
            "exclusions": [
                "Institutional landholders",
                "Former/current MPs/MLAs",
                "Government employees",
                "Income tax payers (Old Regime)"
            ],
        },
        "beneficiaries_cr": 11,  # 11 crore farmers
        "total_disbursed_cr": 330000,  # ₹3.3 lakh crore since inception
        "description": "Direct income support to farmer families",
        "website": "https://pmkisan.gov.in",
        "budget_2026_allocation_cr": 60000,
    },
    
    "pm_fasal_bima": {
        "name": "PM Fasal Bima Yojana (PMFBY)",
        "premium_percent": {
            "kharif": 2.0,
            "rabi": 1.5,
            "horticulture": 5.0,
        },
        "coverage_percent": 100,  # Of sum insured
        "eligibility": {
            "occupation": ["farmer", "agriculture"],
            "loan_mandatory": False,
        },
        "amount_annual": 15000,  # Average claim value
        "description": "Crop insurance scheme with subsidized premium",
        "website": "https://pmfby.gov.in",
        "budget_2026_allocation_cr": 15500,
    },
    
    "kisan_credit_card": {
        "name": "Kisan Credit Card (KCC)",
        "interest_rate": 4.0,  # Effective interest after subsidy
        "interest_subsidy": 3.0,  # 3% interest subvention
        "max_limit": 300000,  # ₹3 lakh
        "eligibility": {
            "occupation": ["farmer", "agriculture", "fisherman", "animal_husbandry"],
            "land_required": False,  # Now available for allied activities
        },
        "amount_annual": 9000,  # Interest saving on ₹3L
        "description": "Subsidized credit for farmers",
        "budget_2026_allocation_cr": 20000,
    },
    
    # ====== FUEL & ENERGY SUBSIDIES ======
    "lpg_subsidy": {
        "name": "PM Ujjwala Yojana (PMUY)",
        "amount_per_cylinder": 200,
        "max_cylinders_year": 12,
        "amount_annual": 2400,
        "free_connection": True,
        "free_connection_value": 1600,
        "eligibility": {
            "max_income": 1000000,
            "bpl_priority": True,
            "woman_head": True,  # Connection in woman's name
        },
        "beneficiaries_cr": 10.35,
        "description": "Subsidized LPG cylinders for eligible households",
        "website": "https://pmuy.gov.in",
        "budget_2026_allocation_cr": 12000,
    },
    
    "pm_surya_ghar": {
        "name": "PM Surya Ghar Muft Bijli Yojana",
        "subsidy_percent": 40,
        "max_subsidy": 78000,  # For 3kW system
        "free_electricity_units": 300,  # Per month
        "amount_annual": 18000,  # Value of free electricity
        "eligibility": {
            "max_income": 1800000,
            "own_house": True,
            "roof_area_sqft": 100,  # Minimum
        },
        "description": "Rooftop solar with 40% subsidy",
        "website": "https://pmsuryaghar.gov.in",
        "budget_2026_allocation_cr": 75000,
    },
    
    # ====== FOOD & NUTRITION SUBSIDIES ======
    "food_subsidy": {
        "name": "National Food Security Act (NFSA)",
        "rice_per_kg": 3,
        "wheat_per_kg": 2,
        "coarse_grains_per_kg": 1,
        "quantity_per_person_kg": 5,
        "amount_monthly": 700,  # Approximate value of subsidized ration
        "amount_annual": 8400,
        "eligibility": {
            "max_income": 300000,
            "priority_household": True,
            "categories": ["AAY", "PHH", "BPL"],
        },
        "beneficiaries_cr": 81,  # 81 crore people
        "description": "Subsidized food grains at ₹1-3/kg",
        "website": "https://nfsa.gov.in",
        "budget_2026_allocation_cr": 205000,
    },
    
    "pm_poshan": {
        "name": "PM POSHAN (Mid-Day Meal)",
        "amount_per_child_daily": 12.71,  # Primary
        "amount_per_child_daily_upper": 19.03,  # Upper Primary
        "amount_annual": 3048,  # Per child (240 days)
        "eligibility": {
            "school_type": ["government", "government_aided"],
            "class_range": [1, 8],
        },
        "beneficiaries_cr": 11.8,
        "description": "Free mid-day meals in schools",
        "budget_2026_allocation_cr": 12000,
    },
    
    # ====== HEALTH SUBSIDIES ======
    "ayushman_bharat": {
        "name": "Ayushman Bharat (PM-JAY)",
        "coverage": 700000,  # Increased to ₹7 lakh in Budget 2026
        "premium_equivalent": 6000,
        "amount_annual": 6000,  # Insurance value per year
        "cashless_treatment": True,
        "eligibility": {
            "max_income": 500000,
            "secc_criteria": True,  # SECC 2011 deprivation criteria
            "categories": ["D1", "D2", "D3", "D4", "D5", "D7"],
        },
        "beneficiaries_cr": 55,  # 55 crore eligible
        "empanelled_hospitals": 30000,
        "description": "Health insurance cover of ₹7 lakh per family",
        "website": "https://pmjay.gov.in",
        "budget_2026_allocation_cr": 7500,
    },
    
    "janaushadhi": {
        "name": "PM Bhartiya Janaushadhi Pariyojana",
        "discount_percent": 50,  # Average discount on medicines
        "amount_annual": 5000,  # Average savings
        "eligibility": {
            "max_income": None,  # Open to all
        },
        "stores_count": 12000,
        "medicines_available": 1965,
        "description": "Generic medicines at 50-90% discount",
        "website": "https://janaushadhi.gov.in",
        "budget_2026_allocation_cr": 500,
    },
    
    # ====== HOUSING SUBSIDIES ======
    "pm_awas_yojana_urban": {
        "name": "PM Awas Yojana - Urban",
        "interest_subsidy_rate": {
            "ews": 0.065,  # 6.5% for EWS
            "lig": 0.065,  # 6.5% for LIG
            "mig1": 0.04,  # 4% for MIG-I
            "mig2": 0.03,  # 3% for MIG-II
        },
        "max_loan_amount": {
            "ews": 600000,
            "lig": 600000,
            "mig1": 900000,
            "mig2": 1200000,
        },
        "subsidy_amount": {
            "ews": 267000,
            "lig": 267000,
            "mig1": 235000,
            "mig2": 230000,
        },
        "amount_annual": 26700,  # Amortized over 10 years (EWS)
        "eligibility": {
            "income_limits": {
                "ews": 300000,
                "lig": 600000,
                "mig1": 1200000,
                "mig2": 1800000,
            },
            "no_pucca_house": True,
            "first_time_buyer": True,
        },
        "description": "Interest subsidy on home loans",
        "website": "https://pmaymis.gov.in",
        "budget_2026_allocation_cr": 80000,
    },
    
    "pm_awas_yojana_rural": {
        "name": "PM Awas Yojana - Gramin",
        "central_assistance": 120000,  # Plain areas
        "central_assistance_hilly": 130000,  # Hilly/difficult areas
        "amount_annual": 120000,  # One-time
        "eligibility": {
            "max_income": 300000,
            "no_pucca_house": True,
            "secc_list": True,
        },
        "description": "Direct assistance for rural housing",
        "website": "https://pmayg.nic.in",
        "budget_2026_allocation_cr": 54500,
    },
    
    # ====== EDUCATION SUBSIDIES ======
    "education_scholarship": {
        "name": "Central Sector Scholarship",
        "amount_annual": {
            "undergraduate": 20000,
            "postgraduate": 20000,
        },
        "eligibility": {
            "max_income": 800000,
            "education_level": ["undergraduate", "postgraduate"],
            "merit_based": True,
            "min_marks_percent": 80,
        },
        "description": "Merit-based scholarship for higher education",
        "budget_2026_allocation_cr": 3000,
    },
    
    "pm_vidyalaxmi": {
        "name": "PM Vidyalaxmi (Education Loan)",
        "interest_subsidy_percent": 3,
        "max_loan": 1000000,  # ₹10 lakh
        "moratorium_years": 1,  # After course completion
        "amount_annual": 30000,  # Interest subsidy value
        "eligibility": {
            "max_income": 800000,
            "course_type": ["professional", "technical"],
            "institution": ["government", "recognized"],
        },
        "description": "Subsidized education loans",
        "budget_2026_allocation_cr": 2000,
    },
    
    # ====== EMPLOYMENT & SKILL SUBSIDIES ======
    "skill_loan_scheme": {
        "name": "Revised Skill Loan Scheme 2026",
        "max_loan": 750000,  # Increased to ₹7.5 lakh
        "interest_subsidy_percent": 3,
        "amount_annual": 22500,  # 3% of max loan
        "eligibility": {
            "age_range": [18, 45],
            "course_duration_months": [3, 36],
            "recognized_institution": True,
        },
        "description": "Loans for skill development courses",
        "budget_2026_allocation_cr": 5000,
    },
    
    # ====== MSME SUBSIDIES ======
    "mudra_loan": {
        "name": "PM MUDRA Yojana",
        "categories": {
            "shishu": {"max": 50000, "interest_subsidy": 2},
            "kishore": {"max": 500000, "interest_subsidy": 1.5},
            "tarun": {"max": 1000000, "interest_subsidy": 1},
        },
        "amount_annual": 10000,  # Average interest subsidy
        "eligibility": {
            "occupation": ["self_employed", "small_business", "entrepreneur"],
            "max_income": 1500000,
            "collateral_required": False,
        },
        "description": "Collateral-free loans for small businesses",
        "website": "https://mudra.org.in",
        "budget_2026_allocation_cr": 10000,
    },
    
    "credit_guarantee_msme": {
        "name": "Credit Guarantee Scheme (CGTMSE)",
        "guarantee_percent": 85,  # Of loan amount
        "max_loan": 500000000,  # ₹5 crore
        "fee_subsidy_percent": 50,
        "amount_annual": 25000,  # Guarantee fee saving
        "eligibility": {
            "enterprise_type": ["micro", "small"],
            "manufacturing": True,
            "services": True,
        },
        "description": "Credit guarantee for MSME loans",
        "budget_2026_allocation_cr": 9000,
    },
    
    # ====== SENIOR CITIZEN SUBSIDIES ======
    "senior_citizen_savings": {
        "name": "Senior Citizen Savings Scheme",
        "interest_rate": 8.2,
        "tax_benefit_80c": True,
        "max_deposit": 3000000,  # ₹30 lakh
        "amount_annual": 24600,  # Extra interest vs FD
        "eligibility": {
            "age_min": 60,
            "age_vrs": 55,  # For VRS retirees
        },
        "description": "Higher interest savings for seniors",
    },
    
    "varishtha_pension_bima": {
        "name": "Varishtha Pension Bima Yojana",
        "guaranteed_return_percent": 9.0,
        "max_pension_monthly": 10000,
        "amount_annual": 120000,
        "eligibility": {
            "age_min": 60,
        },
        "description": "Guaranteed pension for senior citizens",
    },
    
    # ====== WOMEN-SPECIFIC SUBSIDIES ======
    "lakhpati_didi": {
        "name": "Lakhpati Didi Yojana",
        "target_income": 100000,  # Annual income target
        "training_support": True,
        "credit_linkage": True,
        "amount_annual": 50000,  # Support value
        "eligibility": {
            "gender": "female",
            "shg_member": True,
        },
        "target_beneficiaries_cr": 3,  # 3 crore women
        "description": "SHG women income enhancement",
        "budget_2026_allocation_cr": 5000,
    },
    
    "sukanya_samriddhi": {
        "name": "Sukanya Samriddhi Yojana",
        "interest_rate": 8.2,
        "tax_benefit_80c": True,
        "max_deposit_annual": 150000,
        "amount_annual": 12300,  # Extra interest vs FD
        "eligibility": {
            "girl_child_age_max": 10,
        },
        "description": "High-interest savings for girl child",
    },
}


def check_subsidy_eligibility(
    annual_income: float,
    occupation: str,
    family_size: int,
    state: str,
    age: int = 35,
    gender: str = "male",
    has_land: bool = False,
    education_level: str = "none",
    has_house: bool = True,
) -> list:
    """
    Check which subsidies a citizen is eligible for
    Returns list of eligible schemes with benefit amounts
    """
    eligible = []
    occupation_lower = occupation.lower()

    for key, subsidy in SUBSIDIES.items():
        rules = subsidy.get("eligibility", {})
        is_eligible = True
        reasons = []
        
        # Income check
        max_income = rules.get("max_income")
        if max_income and annual_income > max_income:
            is_eligible = False
            reasons.append(f"Income exceeds ₹{max_income:,.0f} limit")
        
        # Occupation check
        required_occupations = rules.get("occupation")
        if required_occupations:
            if occupation_lower not in [o.lower() for o in required_occupations]:
                is_eligible = False
                reasons.append(f"Requires occupation: {', '.join(required_occupations)}")
        
        # Land ownership check
        if rules.get("land_required") and not has_land:
            is_eligible = False
            reasons.append("Agricultural land ownership required")
        
        # Age check for senior citizens
        age_min = rules.get("age_min")
        if age_min and age < age_min:
            is_eligible = False
            reasons.append(f"Minimum age: {age_min} years")
        
        # Gender check
        required_gender = rules.get("gender")
        if required_gender and gender.lower() != required_gender.lower():
            is_eligible = False
            reasons.append(f"Only for {required_gender}")
        
        # House ownership check
        if rules.get("no_pucca_house") and has_house:
            is_eligible = False
            reasons.append("Must not own a pucca house")
        
        # Education level check
        education_levels = rules.get("education_level")
        if education_levels:
            if education_level.lower() not in [e.lower() for e in education_levels]:
                is_eligible = False
                reasons.append(f"Education level must be: {', '.join(education_levels)}")
        
        # Get annual benefit
        annual_benefit = 0
        if is_eligible:
            if "amount_annual" in subsidy:
                annual_benefit = subsidy["amount_annual"]
            elif "subsidy_amount" in subsidy:
                # For PMAY, get based on income bracket
                if annual_income <= 300000:
                    annual_benefit = subsidy.get("subsidy_amount", {}).get("ews", 0) / 10
                elif annual_income <= 600000:
                    annual_benefit = subsidy.get("subsidy_amount", {}).get("lig", 0) / 10
                elif annual_income <= 1200000:
                    annual_benefit = subsidy.get("subsidy_amount", {}).get("mig1", 0) / 10
                elif annual_income <= 1800000:
                    annual_benefit = subsidy.get("subsidy_amount", {}).get("mig2", 0) / 10
        
        eligible.append({
            "scheme": key,
            "name": subsidy["name"],
            "eligible": is_eligible,
            "annual_benefit": annual_benefit if is_eligible else 0,
            "description": subsidy["description"],
            "reasons": reasons if not is_eligible else ["All criteria met"],
            "website": subsidy.get("website", ""),
            "budget_allocation_cr": subsidy.get("budget_2026_allocation_cr", 0),
        })

    return eligible


def get_total_eligible_benefit(
    annual_income: float,
    occupation: str,
    family_size: int,
    **kwargs
) -> dict:
    """Calculate total annual benefit from all eligible schemes"""
    eligibility = check_subsidy_eligibility(
        annual_income, occupation, family_size, **kwargs
    )
    
    eligible_schemes = [s for s in eligibility if s["eligible"]]
    total_benefit = sum(s["annual_benefit"] for s in eligible_schemes)
    
    return {
        "total_annual_benefit": total_benefit,
        "monthly_benefit": round(total_benefit / 12, 2),
        "eligible_scheme_count": len(eligible_schemes),
        "schemes": eligibility,
    }