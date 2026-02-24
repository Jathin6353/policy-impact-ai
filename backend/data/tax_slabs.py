"""
Indian Income Tax Slabs — FY 2026-27
Based on Union Budget 2026-27 (Presented 1 Feb 2026)
New Income Tax Act, 2025 effective from 1 April 2026

Source: https://www.indiabudget.gov.in/doc/budget_speech.pdf
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
# SURCHARGE RATES 2026-27
# ============================================
SURCHARGE_RATES_2026 = [
    {"min": 0, "max": 5000000, "rate": 0.0},
    {"min": 5000000, "max": 10000000, "rate": 0.10},
    {"min": 10000000, "max": 20000000, "rate": 0.15},
    {"min": 20000000, "max": 50000000, "rate": 0.25},
    {"min": 50000000, "max": float("inf"), "rate": 0.25},  # Capped at 25% in new regime
]

# ============================================
# CESS RATES
# ============================================
HEALTH_EDUCATION_CESS = 0.04  # 4% unchanged

# ============================================
# STANDARD DEDUCTION 2026-27
# ============================================
STANDARD_DEDUCTION_NEW_2026 = 100000  # Increased to ₹1L in Budget 2026
STANDARD_DEDUCTION_OLD_2026 = 50000   # Unchanged in old regime

# Previous year for comparison
STANDARD_DEDUCTION_NEW_2024 = 75000
STANDARD_DEDUCTION_OLD_2024 = 50000

# ============================================
# SECTION 80C LIMITS
# ============================================
SECTION_80C_LIMIT = 150000  # Unchanged

# ============================================
# SECTION 80D (Health Insurance)
# ============================================
SECTION_80D_SELF = 25000
SECTION_80D_PARENTS = 25000
SECTION_80D_SENIOR_PARENTS = 50000
SECTION_80D_SENIOR_SELF = 50000

# ============================================
# NPS DEDUCTIONS
# ============================================
SECTION_80CCD_1B = 50000   # Additional NPS deduction
SECTION_80CCD_2_LIMIT = 0.14  # Employer contribution up to 14% of basic

# ============================================
# HOME LOAN DEDUCTIONS
# ============================================
SECTION_24B_LIMIT = 200000  # Interest on housing loan

# ============================================
# REBATE UNDER SECTION 87A (2026-27)
# ============================================
REBATE_87A_NEW_INCOME_LIMIT = 1200000  # Up to ₹12L income
REBATE_87A_NEW_MAX = 60000             # Max rebate ₹60,000
REBATE_87A_OLD_INCOME_LIMIT = 500000   # Up to ₹5L income
REBATE_87A_OLD_MAX = 12500             # Max rebate ₹12,500

# Previous year for comparison
REBATE_87A_NEW_INCOME_LIMIT_2024 = 700000
REBATE_87A_NEW_MAX_2024 = 25000

# ============================================
# MINIMUM ALTERNATE TAX (MAT) - Budget 2026 Change
# ============================================
MAT_RATE_2026 = 0.14  # Reduced from 15% to 14%
MAT_RATE_OLD = 0.15

# ============================================
# SECURITIES TRANSACTION TAX (STT) - Budget 2026 Change
# ============================================
STT_FUTURES_2026 = 0.0005   # 0.05% (increased from 0.0125%)
STT_OPTIONS_2026 = 0.0015   # 0.15% (increased from 0.0625%)
STT_EQUITY_DELIVERY = 0.001  # 0.1% unchanged

# ============================================
# TAX COLLECTED AT SOURCE (TCS) - Budget 2026 Change
# ============================================
TCS_OVERSEAS_TOUR = 0.02      # Reduced to flat 2%
TCS_EDUCATION_REMIT = 0.02    # Reduced to flat 2%
TCS_MEDICAL_REMIT = 0.02      # Reduced to flat 2%
TCS_OTHER_REMIT = 0.05        # 5% for other remittances above ₹7L

# ============================================
# HRA EXEMPTION RATES
# ============================================
METRO_HRA_PERCENT = 0.50  # Delhi, Mumbai, Chennai, Kolkata
NON_METRO_HRA_PERCENT = 0.40

# ============================================
# CAPITAL GAINS TAX 2026-27
# ============================================
LTCG_EQUITY_THRESHOLD = 125000  # Tax-free up to ₹1.25L
LTCG_EQUITY_RATE = 0.125        # 12.5% above threshold
STCG_EQUITY_RATE = 0.20         # 20% for short-term

# Real Estate
LTCG_PROPERTY_RATE = 0.125      # 12.5% without indexation
LTCG_PROPERTY_RATE_INDEXED = 0.20  # 20% with indexation (old properties)


def get_regime_slabs(regime: str, year: str = "2026"):
    """Return appropriate tax slabs based on regime and year"""
    if year == "2026" or year == "2026-27":
        if regime == "new":
            return NEW_REGIME_SLABS_2026
        return OLD_REGIME_SLABS_2026
    elif year == "2024" or year == "2024-25":
        if regime == "new":
            return NEW_REGIME_SLABS_2024
        return OLD_REGIME_SLABS_2026
    else:
        return NEW_REGIME_SLABS_2026


def get_standard_deduction(regime: str, year: str = "2026") -> int:
    """Get standard deduction based on regime and year"""
    if year == "2026" or year == "2026-27":
        return STANDARD_DEDUCTION_NEW_2026 if regime == "new" else STANDARD_DEDUCTION_OLD_2026
    return STANDARD_DEDUCTION_NEW_2024 if regime == "new" else STANDARD_DEDUCTION_OLD_2024


def get_rebate_limit(regime: str, year: str = "2026") -> tuple:
    """Get rebate income limit and max rebate"""
    if year == "2026" or year == "2026-27":
        if regime == "new":
            return REBATE_87A_NEW_INCOME_LIMIT, REBATE_87A_NEW_MAX
        return REBATE_87A_OLD_INCOME_LIMIT, REBATE_87A_OLD_MAX
    else:
        if regime == "new":
            return REBATE_87A_NEW_INCOME_LIMIT_2024, REBATE_87A_NEW_MAX_2024
        return REBATE_87A_OLD_INCOME_LIMIT, REBATE_87A_OLD_MAX


# ============================================
# BUDGET 2026-27 HIGHLIGHTS
# ============================================
BUDGET_2026_HIGHLIGHTS = {
    "total_expenditure": 5347000000000,  # ₹53.47 lakh crore
    "total_revenue": 3650000000000,      # ₹36.5 lakh crore
    "capital_expenditure": 1220000000000, # ₹12.2 lakh crore (record high)
    "fiscal_deficit_percent": 4.3,
    "debt_to_gdp_percent": 55.6,
    "nominal_gdp_growth_percent": 10.0,
    "presentation_date": "2026-02-01",
    "effective_date": "2026-04-01",
    "new_income_tax_act": "Income Tax Act, 2025",
}