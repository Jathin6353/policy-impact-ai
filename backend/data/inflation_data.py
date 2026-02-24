"""
CPI Inflation Data — India
Updated with data through FY 2025-26 and projections for 2026-27

Sources:
- Reserve Bank of India: https://rbi.org.in
- Ministry of Statistics (MoSPI): https://mospi.gov.in
- Budget 2026-27 Economic Survey
"""

# ============================================
# HISTORICAL CPI INFLATION (Annual Average %)
# ============================================
CPI_INFLATION_HISTORY = {
    2015: 4.91,
    2016: 4.95,
    2017: 3.33,
    2018: 3.94,
    2019: 4.77,
    2020: 6.62,  # COVID impact
    2021: 5.13,
    2022: 6.70,  # Global inflation surge
    2023: 5.66,
    2024: 5.40,
    2025: 4.85,  # Estimated (H1 FY26)
    2026: 4.50,  # RBI projection for FY27
}

# Monthly CPI 2025-26 (Base 2012=100)
CPI_MONTHLY_2025_26 = {
    "Apr_2025": 189.4,
    "May_2025": 190.1,
    "Jun_2025": 191.2,
    "Jul_2025": 192.5,
    "Aug_2025": 191.8,
    "Sep_2025": 192.3,
    "Oct_2025": 193.1,
    "Nov_2025": 193.8,
    "Dec_2025": 194.2,
    "Jan_2026": 194.8,  # Latest available
}

# ============================================
# RBI INFLATION PROJECTIONS 2026-27
# ============================================
RBI_INFLATION_PROJECTIONS = {
    "Q1_FY27": 4.6,  # Apr-Jun 2026
    "Q2_FY27": 4.4,  # Jul-Sep 2026
    "Q3_FY27": 4.5,  # Oct-Dec 2026
    "Q4_FY27": 4.4,  # Jan-Mar 2027
    "full_year_FY27": 4.5,
    "target": 4.0,  # RBI target
    "upper_band": 6.0,
    "lower_band": 2.0,
}

# ============================================
# CATEGORY-WISE INFLATION MULTIPLIERS
# (Relative to headline CPI - based on 5-year average)
# ============================================
CATEGORY_INFLATION_MULTIPLIERS = {
    "food": 1.40,           # Food inflation typically 40% higher
    "cereals": 1.20,
    "pulses": 1.50,
    "vegetables": 2.00,     # Highly volatile
    "fruits": 1.30,
    "fuel": 1.35,           # Fuel/energy inflation
    "housing": 0.80,        # Housing inflation lower
    "education": 1.85,      # Education inflation significantly higher
    "healthcare": 1.65,     # Healthcare rising fast
    "clothing": 0.85,
    "transport": 1.25,
    "communication": 0.50,  # Deflation in telecom
    "recreation": 0.75,
    "personal_care": 1.00,
    "miscellaneous": 1.00,
}

# ============================================
# CATEGORY-WISE CPI WEIGHTS (Base 2012)
# ============================================
CPI_CATEGORY_WEIGHTS = {
    "food_beverages": 45.86,
    "pan_tobacco": 2.38,
    "clothing_footwear": 6.53,
    "housing": 10.07,
    "fuel_light": 6.84,
    "miscellaneous": 28.32,
}

# ============================================
# AVERAGE HOUSEHOLD EXPENDITURE BREAKDOWN
# Based on NSSO HCE Survey 2022-23
# ============================================
HOUSEHOLD_EXPENDITURE_PATTERN = {
    "low_income": {  # < ₹3 LPA
        "food": 0.48,
        "fuel": 0.10,
        "housing": 0.12,
        "education": 0.04,
        "healthcare": 0.08,
        "clothing": 0.05,
        "transport": 0.06,
        "communication": 0.02,
        "recreation": 0.01,
        "miscellaneous": 0.02,
        "savings_rate": 0.02,
    },
    "lower_middle": {  # ₹3-7 LPA
        "food": 0.38,
        "fuel": 0.08,
        "housing": 0.16,
        "education": 0.08,
        "healthcare": 0.07,
        "clothing": 0.05,
        "transport": 0.08,
        "communication": 0.02,
        "recreation": 0.02,
        "miscellaneous": 0.03,
        "savings_rate": 0.08,
    },
    "middle": {  # ₹7-15 LPA
        "food": 0.30,
        "fuel": 0.07,
        "housing": 0.18,
        "education": 0.10,
        "healthcare": 0.06,
        "clothing": 0.05,
        "transport": 0.08,
        "communication": 0.02,
        "recreation": 0.03,
        "miscellaneous": 0.04,
        "savings_rate": 0.12,
    },
    "upper_middle": {  # ₹15-30 LPA
        "food": 0.22,
        "fuel": 0.05,
        "housing": 0.20,
        "education": 0.12,
        "healthcare": 0.05,
        "clothing": 0.04,
        "transport": 0.07,
        "communication": 0.02,
        "recreation": 0.05,
        "miscellaneous": 0.05,
        "savings_rate": 0.18,
    },
    "high": {  # > ₹30 LPA
        "food": 0.15,
        "fuel": 0.04,
        "housing": 0.18,
        "education": 0.10,
        "healthcare": 0.05,
        "clothing": 0.04,
        "transport": 0.06,
        "communication": 0.02,
        "recreation": 0.06,
        "miscellaneous": 0.06,
        "savings_rate": 0.28,
    },
}

# ============================================
# STATE-WISE INFLATION VARIATIONS 2025-26
# ============================================
STATE_INFLATION_VARIATION = {
    "andhra_pradesh": 1.05,
    "bihar": 1.12,
    "delhi": 0.95,
    "gujarat": 0.98,
    "haryana": 1.00,
    "karnataka": 0.97,
    "kerala": 1.08,
    "madhya_pradesh": 1.10,
    "maharashtra": 0.96,
    "punjab": 1.02,
    "rajasthan": 1.06,
    "tamil_nadu": 0.99,
    "telangana": 0.98,
    "uttar_pradesh": 1.08,
    "west_bengal": 1.07,
    "default": 1.00,
}

# ============================================
# FOOD INFLATION DETAILED (Latest Available)
# ============================================
FOOD_INFLATION_DETAILED = {
    "cereals_products": 6.2,
    "meat_fish": 5.8,
    "eggs": 4.5,
    "milk_products": 3.8,
    "oils_fats": 2.1,
    "fruits": 7.2,
    "vegetables": 12.5,  # Highly volatile
    "pulses_products": 8.4,
    "sugar_confectionery": 2.8,
    "spices": 5.5,
    "prepared_meals": 4.2,
}


def get_income_bracket(annual_income: float) -> str:
    """Classify household by income bracket"""
    if annual_income < 300000:
        return "low_income"
    elif annual_income < 700000:
        return "lower_middle"
    elif annual_income < 1500000:
        return "middle"
    elif annual_income < 3000000:
        return "upper_middle"
    else:
        return "high"


def get_expenditure_pattern(annual_income: float) -> dict:
    """Get spending pattern based on income"""
    bracket = get_income_bracket(annual_income)
    return HOUSEHOLD_EXPENDITURE_PATTERN[bracket]


def get_current_inflation() -> float:
    """Get latest inflation rate"""
    return CPI_INFLATION_HISTORY.get(2026, 4.5)


def get_projected_inflation(years_ahead: int = 1) -> float:
    """Get projected inflation for future years"""
    if years_ahead == 1:
        return RBI_INFLATION_PROJECTIONS["full_year_FY27"]
    elif years_ahead == 2:
        return 4.2  # Long-term trend estimate
    else:
        return 4.0  # RBI target


def get_state_adjusted_inflation(state: str, base_inflation: float = None) -> float:
    """Get state-adjusted inflation rate"""
    base = base_inflation or get_current_inflation()
    multiplier = STATE_INFLATION_VARIATION.get(
        state.lower().replace(" ", "_"),
        STATE_INFLATION_VARIATION["default"]
    )
    return round(base * multiplier, 2)


def calculate_real_income_growth(
    nominal_growth: float,
    inflation: float = None
) -> float:
    """Calculate real income growth (nominal - inflation)"""
    infl = inflation or get_current_inflation()
    return round(nominal_growth - infl, 2)