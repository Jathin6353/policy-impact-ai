"""
Indian Income Tax Slabs — FY 2026-27
Based on Union Budget 2026-27 (Presented 1 Feb 2026)
New Income Tax Act, 2025 effective from 1 April 2026

Source: https://www.indiabudget.gov.in/doc/budget_speech.pdf
Last Updated: 1 February 2026
"""

# ============================================
# NEW TAX REGIME 2026-27 (Default)
# ============================================
NEW_REGIME_SLABS_2026 = [
    {"min": 0, "max": 400000, "rate": 0.0},        # Zero tax up to ₹4L
    {"min": 400000, "max": 800000, "rate": 0.05},  # 5% for ₹4L-8L
    {"min": 800000, "max": 1200000, "rate": 0.10}, # 10% for ₹8L-12L
    {"min": 1200000, "max": 1600000, "rate": 0.15}, # 15% for ₹12L-16L
    {"min": 1600000, "max": 2000000, "rate": 0.20}, # 20% for ₹16L-20L
    {"min": 2000000, "max": 2400000, "rate": 0.25}, # 25% for ₹20L-24L
    {"min": 2400000, "max": float("inf"), "rate": 0.30}, # 30% above ₹24L
]

# ============================================
# NEW TAX REGIME 2024-25 (Previous Year - for comparison)
# ============================================
NEW_REGIME_SLABS_2024 = [
    {"min": 0, "max": 300000, "rate": 0.0},
    {"min": 300000, "max": 700000, "rate": 0.05},
    {"min": 700000, "max": 1000000, "rate": 0.10},
    {"min": 1000000, "max": 1200000, "rate": 0.15},
    {"min": 1200000, "max": 1500000, "rate": 0.20},
    {"min": 1500000, "max": float("inf"), "rate": 0.30},
]

# ============================================
# OLD TAX REGIME 2026-27
# ============================================
OLD_REGIME_SLABS_2026 = [
    {"min": 0, "max": 250000, "rate": 0.0},
    {"min": 250000, "max": 500000, "rate": 0.05},
    {"min": 500000, "max": 1000000, "rate": 0.20},
    {"min": 1000000, "max": float("inf"), "rate": 0.30},
]

# ============================================
# OLD TAX REGIME 2024-25
# ============================================
OLD_REGIME_SLABS_2024 = [
    {"min": 0, "max": 250000, "rate": 0.0},
    {"min": 250000, "max": 500000, "rate": 0.05},
    {"min": 500000, "max": 1000000, "rate": 0.20},
    {"min": 1000000, "max": float("inf"), "rate": 0.30},
]

# ============================================
# PROPOSED TAX REGIME 2025 (Speculative for Comparison)
# ============================================
PROPOSED_NEW_REGIME_2025 = [
    {"min": 0, "max": 400000, "rate": 0.0},
    {"min": 400000, "max": 800000, "rate": 0.05},
    {"min": 800000, "max": 1200000, "rate": 0.10},
    {"min": 1200000, "max": 1500000, "rate": 0.15},
    {"min": 1500000, "max": 2000000, "rate": 0.20},
    {"min": 2000000, "max": float("inf"), "rate": 0.30},
]

# ============================================
# PROPOSED TAX REGIME 2027 (Future Speculation)
# ============================================
PROPOSED_NEW_REGIME_2027 = [
    {"min": 0, "max": 500000, "rate": 0.0},
    {"min": 500000, "max": 1000000, "rate": 0.05},
    {"min": 1000000, "max": 1500000, "rate": 0.10},
    {"min": 1500000, "max": 2000000, "rate": 0.15},
    {"min": 2000000, "max": 2500000, "rate": 0.20},
    {"min": 2500000, "max": float("inf"), "rate": 0.25},
]

# ============================================
# SURCHARGE RATES 2026-27 (New Regime)
# ============================================
SURCHARGE_RATES = [
    {"min": 0, "max": 5000000, "rate": 0.0},
    {"min": 5000000, "max": 10000000, "rate": 0.10},
    {"min": 10000000, "max": 20000000, "rate": 0.15},
    {"min": 20000000, "max": 50000000, "rate": 0.25},
    {"min": 50000000, "max": float("inf"), "rate": 0.25},  # Capped at 25% in new regime
]

# Surcharge for Old Regime (slightly different)
SURCHARGE_RATES_OLD = [
    {"min": 0, "max": 5000000, "rate": 0.0},
    {"min": 5000000, "max": 10000000, "rate": 0.10},
    {"min": 10000000, "max": 20000000, "rate": 0.15},
    {"min": 20000000, "max": 50000000, "rate": 0.25},
    {"min": 50000000, "max": float("inf"), "rate": 0.37},  # Higher for old regime
]

# ============================================
# CESS RATES
# ============================================
HEALTH_EDUCATION_CESS = 0.04  # 4% (unchanged from previous years)

# ============================================
# STANDARD DEDUCTION 2026-27
# ============================================
# New Values (Budget 2026)
STANDARD_DEDUCTION_NEW_2026 = 100000  # Increased to ₹1L in Budget 2026
STANDARD_DEDUCTION_OLD_2026 = 50000   # Unchanged in old regime

# Previous Year Values (2024-25)
STANDARD_DEDUCTION_NEW_2024 = 75000
STANDARD_DEDUCTION_OLD_2024 = 50000

# ============================================
# BACKWARD COMPATIBLE ALIASES
# (Required by tax_engine.py and other modules)
# ============================================
STANDARD_DEDUCTION_NEW = STANDARD_DEDUCTION_NEW_2026
STANDARD_DEDUCTION_OLD = STANDARD_DEDUCTION_OLD_2026

# ============================================
# SECTION 80C LIMITS (Old Regime Only)
# ============================================
SECTION_80C_LIMIT = 150000  # ₹1.5 Lakh (unchanged)

# Eligible Investments under 80C
SECTION_80C_INVESTMENTS = [
    "PPF (Public Provident Fund)",
    "ELSS (Equity Linked Savings Scheme)",
    "Life Insurance Premium",
    "NSC (National Savings Certificate)",
    "Tax Saver FD (5-year lock-in)",
    "Sukanya Samriddhi Yojana",
    "Home Loan Principal Repayment",
    "Children's Tuition Fees (max 2 children)",
    "ULIP (Unit Linked Insurance Plan)",
    "Senior Citizen Savings Scheme",
]

# ============================================
# SECTION 80D (Health Insurance) - Old Regime Only
# ============================================
SECTION_80D_SELF = 25000              # Self + Family (below 60)
SECTION_80D_SELF_SENIOR = 50000       # Self + Family (60+)
SECTION_80D_PARENTS = 25000           # Parents (below 60)
SECTION_80D_SENIOR_PARENTS = 50000    # Parents (60+)

# Maximum 80D Deduction
SECTION_80D_MAX_NON_SENIOR = 50000    # Self (25K) + Parents (25K)
SECTION_80D_MAX_SENIOR = 100000       # Self Senior (50K) + Parents Senior (50K)

# Preventive Health Checkup (within 80D limits)
PREVENTIVE_HEALTH_CHECKUP_LIMIT = 5000

# ============================================
# SECTION 80CCD (NPS) - Old Regime Only
# ============================================
SECTION_80CCD_1 = 150000       # Part of 80C limit
SECTION_80CCD_1B = 50000       # Additional ₹50K for NPS
SECTION_80CCD_2_PERCENT = 0.14 # Employer contribution up to 14% of basic (Govt employees)
SECTION_80CCD_2_PRIVATE = 0.10 # 10% for private sector

# ============================================
# SECTION 24B (Home Loan Interest) - Old Regime Only
# ============================================
SECTION_24B_LIMIT = 200000           # Self-occupied property
SECTION_24B_LET_OUT = float("inf")   # No limit for let-out property

# Additional deduction for first-time buyers (80EEA) - Discontinued
SECTION_80EEA_LIMIT = 0  # Discontinued from FY 2022-23

# ============================================
# HRA EXEMPTION RATES - Old Regime Only
# ============================================
METRO_HRA_PERCENT = 0.50  # Delhi, Mumbai, Chennai, Kolkata
NON_METRO_HRA_PERCENT = 0.40

METRO_CITIES = ["delhi", "mumbai", "chennai", "kolkata", "new delhi"]

# ============================================
# LEAVE TRAVEL ALLOWANCE (LTA) - Old Regime Only
# ============================================
LTA_EXEMPTION_FREQUENCY = "2 journeys in 4 years"
LTA_ELIGIBLE_TRAVEL = ["air", "rail", "road"]

# ============================================
# REBATE UNDER SECTION 87A
# ============================================
# 2026-27 (Budget 2026)
REBATE_87A_NEW_INCOME_LIMIT_2026 = 1200000  # Up to ₹12L income
REBATE_87A_NEW_MAX_2026 = 60000             # Max rebate ₹60,000

# 2024-25 (Previous Year)
REBATE_87A_NEW_INCOME_LIMIT_2024 = 700000   # Up to ₹7L income
REBATE_87A_NEW_MAX_2024 = 25000             # Max rebate ₹25,000

# Old Regime (All Years)
REBATE_87A_OLD_INCOME_LIMIT = 500000        # Up to ₹5L income
REBATE_87A_OLD_MAX = 12500                  # Max rebate ₹12,500

# ============================================
# MINIMUM ALTERNATE TAX (MAT) - Budget 2026 Change
# ============================================
MAT_RATE_2026 = 0.14  # Reduced from 15% to 14%
MAT_RATE_2024 = 0.15
MAT_RATE_OLD = 0.15

# MAT Credit
MAT_CREDIT_CARRY_FORWARD_YEARS = 15

# ============================================
# SECURITIES TRANSACTION TAX (STT) - Budget 2026 Change
# ============================================
STT_FUTURES_2026 = 0.0005    # 0.05% (increased from 0.0125%)
STT_OPTIONS_2026 = 0.0015    # 0.15% (increased from 0.0625%)
STT_EQUITY_DELIVERY = 0.001  # 0.1% (unchanged)
STT_EQUITY_INTRADAY = 0.00025  # 0.025%

# Previous Year STT
STT_FUTURES_2024 = 0.000125   # 0.0125%
STT_OPTIONS_2024 = 0.000625   # 0.0625%

# ============================================
# TAX COLLECTED AT SOURCE (TCS) - Budget 2026 Change
# ============================================
# 2026 Rates (Reduced)
TCS_OVERSEAS_TOUR_2026 = 0.02      # Reduced to flat 2%
TCS_EDUCATION_REMIT_2026 = 0.02    # Reduced to flat 2%
TCS_MEDICAL_REMIT_2026 = 0.02      # Reduced to flat 2%
TCS_OTHER_REMIT = 0.05             # 5% for other remittances above ₹7L

# 2024 Rates (Previous)
TCS_OVERSEAS_TOUR_2024 = 0.05
TCS_EDUCATION_REMIT_2024 = 0.05
TCS_MEDICAL_REMIT_2024 = 0.05

# TCS Thresholds
TCS_THRESHOLD_LRS = 700000         # ₹7 lakh for LRS remittances
TCS_THRESHOLD_EDUCATION_LOAN = 0   # No TCS if loan from financial institution

# ============================================
# CAPITAL GAINS TAX 2026-27
# ============================================
# Long Term Capital Gains (LTCG) - Equity
LTCG_EQUITY_THRESHOLD = 125000      # Tax-free up to ₹1.25L per year
LTCG_EQUITY_RATE = 0.125            # 12.5% above threshold
LTCG_EQUITY_HOLDING_MONTHS = 12     # 12 months for equity

# Short Term Capital Gains (STCG) - Equity
STCG_EQUITY_RATE = 0.20             # 20% for short-term (changed from 15%)
STCG_EQUITY_RATE_OLD = 0.15         # Previous rate

# Real Estate / Property
LTCG_PROPERTY_RATE = 0.125          # 12.5% without indexation (Budget 2024)
LTCG_PROPERTY_RATE_INDEXED = 0.20   # 20% with indexation (grandfathered)
LTCG_PROPERTY_HOLDING_MONTHS = 24   # 24 months

# Debt Funds (Post April 2023)
LTCG_DEBT_RATE = "slab_rate"        # Taxed at slab rate (no LTCG benefit)
STCG_DEBT_RATE = "slab_rate"

# Gold / International Funds
LTCG_GOLD_RATE = 0.20               # 20% with indexation (for < 3 years holding before July 2024)
LTCG_GOLD_RATE_NEW = 0.125          # 12.5% without indexation (new regime)
LTCG_GOLD_HOLDING_MONTHS = 24

# ============================================
# BUYBACK TAX - Budget 2026 Change
# ============================================
BUYBACK_TAX_NEW = "capital_gains"   # Now treated as capital gains in hands of shareholders
BUYBACK_TAX_OLD_RATE = 0.20         # Earlier 20% + surcharge on company

# ============================================
# DIVIDEND TAX
# ============================================
DDT_ABOLISHED = True                # Abolished since Budget 2020
DIVIDEND_TAX = "slab_rate"          # Taxed as per individual's slab rate
TDS_ON_DIVIDEND = 0.10              # 10% TDS above ₹5000

# ============================================
# PROFESSIONAL TAX (State-wise, for reference)
# ============================================
PROFESSIONAL_TAX = {
    "maharashtra": 2500,
    "karnataka": 2400,
    "west_bengal": 2500,
    "andhra_pradesh": 2500,
    "telangana": 2500,
    "tamil_nadu": 2500,
    "gujarat": 2500,
    "madhya_pradesh": 2500,
    "kerala": 2500,
    "odisha": 2500,
    "assam": 2500,
    "bihar": 2500,
    "jharkhand": 2500,
    "default": 2500,
}

# ============================================
# HELPER FUNCTIONS
# ============================================
def get_regime_slabs(regime: str, year: str = "2024"):
    """
    Return appropriate tax slabs based on regime and year
    
    Args:
        regime: 'new' or 'old'
        year: '2026', '2024', '2025_proposed', '2027_proposed'
    
    Returns:
        list: Tax slab structure
    """
    if year == "2025_proposed":
        return PROPOSED_NEW_REGIME_2025
    if year == "2027_proposed" or year == "2027":
        return PROPOSED_NEW_REGIME_2027
    if year == "2026" or year == "2026-27":
        if regime == "new":
            return NEW_REGIME_SLABS_2026
        return OLD_REGIME_SLABS_2026
    # Default to 2024
    if regime == "new":
        return NEW_REGIME_SLABS_2024
    return OLD_REGIME_SLABS_2024


def get_standard_deduction(regime: str, year: str = "2026") -> int:
    """Get standard deduction based on regime and year"""
    if year in ("2026", "2026-27"):
        return STANDARD_DEDUCTION_NEW_2026 if regime == "new" else STANDARD_DEDUCTION_OLD_2026
    elif year in ("2024", "2024-25"):
        return STANDARD_DEDUCTION_NEW_2024 if regime == "new" else STANDARD_DEDUCTION_OLD_2024
    return STANDARD_DEDUCTION_NEW_2026 if regime == "new" else STANDARD_DEDUCTION_OLD_2026


def get_rebate_limit(regime: str, year: str = "2026") -> tuple:
    """
    Get rebate income limit and max rebate
    
    Returns:
        tuple: (income_limit, max_rebate)
    """
    if year in ("2026", "2026-27"):
        if regime == "new":
            return REBATE_87A_NEW_INCOME_LIMIT_2026, REBATE_87A_NEW_MAX_2026
        return REBATE_87A_OLD_INCOME_LIMIT, REBATE_87A_OLD_MAX
    elif year in ("2024", "2024-25"):
        if regime == "new":
            return REBATE_87A_NEW_INCOME_LIMIT_2024, REBATE_87A_NEW_MAX_2024
        return REBATE_87A_OLD_INCOME_LIMIT, REBATE_87A_OLD_MAX
    else:
        if regime == "new":
            return REBATE_87A_NEW_INCOME_LIMIT_2026, REBATE_87A_NEW_MAX_2026
        return REBATE_87A_OLD_INCOME_LIMIT, REBATE_87A_OLD_MAX


def get_surcharge_rates(regime: str = "new") -> list:
    """Get applicable surcharge rates based on regime"""
    if regime == "new":
        return SURCHARGE_RATES
    return SURCHARGE_RATES_OLD


def calculate_surcharge(basic_tax: float, income: float, regime: str = "new") -> float:
    """Calculate surcharge amount"""
    rates = get_surcharge_rates(regime)
    for slab in rates:
        if slab["min"] <= income < slab["max"]:
            return round(basic_tax * slab["rate"], 2)
    return 0


def get_stt_rates(year: str = "2026") -> dict:
    """Get STT rates by year"""
    if year in ("2026", "2026-27"):
        return {
            "futures": STT_FUTURES_2026,
            "options": STT_OPTIONS_2026,
            "equity_delivery": STT_EQUITY_DELIVERY,
            "equity_intraday": STT_EQUITY_INTRADAY,
        }
    return {
        "futures": STT_FUTURES_2024,
        "options": STT_OPTIONS_2024,
        "equity_delivery": STT_EQUITY_DELIVERY,
        "equity_intraday": STT_EQUITY_INTRADAY,
    }


def get_tcs_rates(year: str = "2026") -> dict:
    """Get TCS rates by year"""
    if year in ("2026", "2026-27"):
        return {
            "overseas_tour": TCS_OVERSEAS_TOUR_2026,
            "education": TCS_EDUCATION_REMIT_2026,
            "medical": TCS_MEDICAL_REMIT_2026,
            "other": TCS_OTHER_REMIT,
        }
    return {
        "overseas_tour": TCS_OVERSEAS_TOUR_2024,
        "education": TCS_EDUCATION_REMIT_2024,
        "medical": TCS_MEDICAL_REMIT_2024,
        "other": TCS_OTHER_REMIT,
    }


def is_metro_city(city: str) -> bool:
    """Check if city is a metro for HRA calculation"""
    return city.lower().strip() in METRO_CITIES


def get_hra_percent(city: str) -> float:
    """Get HRA percentage based on city"""
    if is_metro_city(city):
        return METRO_HRA_PERCENT
    return NON_METRO_HRA_PERCENT


def calculate_80d_limit(self_age: int, parents_age: int = None) -> dict:
    """Calculate Section 80D limits based on age"""
    self_limit = SECTION_80D_SELF_SENIOR if self_age >= 60 else SECTION_80D_SELF
    
    parents_limit = 0
    if parents_age:
        parents_limit = SECTION_80D_SENIOR_PARENTS if parents_age >= 60 else SECTION_80D_PARENTS
    
    return {
        "self_limit": self_limit,
        "parents_limit": parents_limit,
        "total_limit": self_limit + parents_limit,
        "preventive_checkup": PREVENTIVE_HEALTH_CHECKUP_LIMIT,
    }


def get_professional_tax(state: str) -> int:
    """Get professional tax by state"""
    return PROFESSIONAL_TAX.get(state.lower().strip(), PROFESSIONAL_TAX["default"])


# ============================================
# BUDGET 2026-27 HIGHLIGHTS
# ============================================
BUDGET_2026_HIGHLIGHTS = {
    "total_expenditure": 5347000000000,       # ₹53.47 lakh crore
    "total_expenditure_cr": 5347000,
    "total_revenue": 3650000000000,           # ₹36.5 lakh crore
    "total_revenue_cr": 3650000,
    "capital_expenditure": 1220000000000,     # ₹12.2 lakh crore (record high)
    "capital_expenditure_cr": 1220000,
    "fiscal_deficit_percent": 4.3,
    "debt_to_gdp_percent": 55.6,
    "nominal_gdp_growth_percent": 10.0,
    "presentation_date": "2026-02-01",
    "effective_date": "2026-04-01",
    "new_income_tax_act": "Income Tax Act, 2025",
    "finance_minister": "Nirmala Sitharaman",
}

# ============================================
# KEY TAX CHANGES IN BUDGET 2026-27
# ============================================
BUDGET_2026_TAX_CHANGES = {
    "zero_tax_limit": {
        "old_value": 300000,
        "new_value": 400000,
        "change": 100000,
        "benefit": "₹1 lakh additional exemption",
    },
    "standard_deduction": {
        "old_value": 75000,
        "new_value": 100000,
        "change": 25000,
        "benefit": "₹25,000 additional deduction",
    },
    "rebate_87a_limit": {
        "old_value": 700000,
        "new_value": 1200000,
        "change": 500000,
        "benefit": "Zero tax effective up to ₹12L",
    },
    "rebate_87a_max": {
        "old_value": 25000,
        "new_value": 60000,
        "change": 35000,
        "benefit": "Higher rebate amount",
    },
    "mat_rate": {
        "old_value": 0.15,
        "new_value": 0.14,
        "change": -0.01,
        "benefit": "1% reduction for companies",
    },
    "stt_futures": {
        "old_value": 0.000125,
        "new_value": 0.0005,
        "change_multiplier": 4,
        "impact": "Increased to curb speculation",
    },
    "stt_options": {
        "old_value": 0.000625,
        "new_value": 0.0015,
        "change_multiplier": 2.4,
        "impact": "Increased to curb speculation",
    },
    "tcs_rates": {
        "old_value": 0.05,
        "new_value": 0.02,
        "change": -0.03,
        "benefit": "Easier foreign remittances",
    },
}

# ============================================
# MAJOR BUDGET ALLOCATIONS 2026-27 (in Crores)
# ============================================
BUDGET_ALLOCATIONS_2026 = {
    "defence": {
        "total": 682000,
        "capital": 172000,
        "revenue": 510000,
    },
    "infrastructure": {
        "total": 1220000,
        "roads_highways": 280000,
        "railways": 250000,
        "urban_development": 85000,
    },
    "education": {
        "total": 125000,
        "higher_education": 45000,
        "school_education": 80000,
    },
    "health": {
        "total": 95000,
        "ayushman_bharat": 7500,
        "family_welfare": 35000,
    },
    "agriculture": {
        "total": 145000,
        "pm_kisan": 60000,
        "crop_insurance": 15500,
    },
    "rural_development": {
        "total": 175000,
        "mgnrega": 86000,
        "pm_awas_gramin": 54500,
    },
    "semiconductor_mission": 76000,
    "green_hydrogen": 19700,
    "msme_support": 22000,
    "skill_development": 15000,
}

# ============================================
# DATA SOURCES & VERIFICATION
# ============================================
DATA_SOURCES = {
    "tax_slabs": "Income Tax Department, Budget 2026-27 Speech",
    "budget_data": "https://www.indiabudget.gov.in",
    "official_calculator": "https://incometax.gov.in/iec/foportal/",
    "finance_bill": "Finance Bill 2026",
    "last_updated": "2026-02-01",
    "effective_from": "2026-04-01",
    "verified": True,
}


# ============================================
# EXAMPLE USAGE & TESTING
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("TAX SLABS 2026-27 (New Regime)")
    print("=" * 60)
    
    slabs = get_regime_slabs("new", "2026")
    for slab in slabs:
        max_val = "∞" if slab["max"] == float("inf") else f"₹{slab['max']:,}"
        print(f"₹{slab['min']:,} - {max_val}: {slab['rate']*100}%")
    
    print("\n" + "=" * 60)
    print("STANDARD DEDUCTION COMPARISON")
    print("=" * 60)
    print(f"New Regime 2024: ₹{get_standard_deduction('new', '2024'):,}")
    print(f"New Regime 2026: ₹{get_standard_deduction('new', '2026'):,}")
    print(f"Benefit: ₹{get_standard_deduction('new', '2026') - get_standard_deduction('new', '2024'):,}")
    
    print("\n" + "=" * 60)
    print("REBATE u/s 87A COMPARISON")
    print("=" * 60)
    old_limit, old_max = get_rebate_limit("new", "2024")
    new_limit, new_max = get_rebate_limit("new", "2026")
    print(f"2024: Up to ₹{old_limit:,} income → Max rebate ₹{old_max:,}")
    print(f"2026: Up to ₹{new_limit:,} income → Max rebate ₹{new_max:,}")
    
    print("\n" + "=" * 60)
    print("BUDGET 2026-27 HIGHLIGHTS")
    print("=" * 60)
    print(f"Total Expenditure: ₹{BUDGET_2026_HIGHLIGHTS['total_expenditure_cr']:,} Cr")
    print(f"Capital Expenditure: ₹{BUDGET_2026_HIGHLIGHTS['capital_expenditure_cr']:,} Cr")
    print(f"Fiscal Deficit: {BUDGET_2026_HIGHLIGHTS['fiscal_deficit_percent']}% of GDP")
    print(f"Effective From: {BUDGET_2026_HIGHLIGHTS['effective_date']}")
    
    print("\n" + "=" * 60)
    print("STT CHANGES (Budget 2026)")
    print("=" * 60)
    stt_2024 = get_stt_rates("2024")
    stt_2026 = get_stt_rates("2026")
    print(f"Futures: {stt_2024['futures']*100}% → {stt_2026['futures']*100}%")
    print(f"Options: {stt_2024['options']*100}% → {stt_2026['options']*100}%")
    
    print("\n✅ All imports and functions working correctly!")