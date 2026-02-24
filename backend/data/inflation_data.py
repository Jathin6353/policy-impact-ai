"""
CPI Inflation Data — India
Source: RBI, Ministry of Statistics
Historical CPI (Combined) year-over-year
"""

# Historical CPI inflation rates (annual average %)
CPI_INFLATION_HISTORY = {
    2015: 4.91,
    2016: 4.95,
    2017: 3.33,
    2018: 3.94,
    2019: 4.77,
    2020: 6.62,
    2021: 5.13,
    2022: 6.70,
    2023: 5.66,
    2024: 4.85,  # Estimated
}

# Category-wise inflation multipliers (relative to headline CPI)
CATEGORY_INFLATION_MULTIPLIERS = {
    "food": 1.35,           # Food inflation typically higher
    "fuel": 1.50,           # Fuel is volatile
    "housing": 0.85,        # Housing inflation lower
    "education": 1.80,      # Education inflation significantly higher
    "healthcare": 1.60,     # Healthcare rising fast
    "clothing": 0.90,
    "transport": 1.20,
    "recreation": 0.75,
    "miscellaneous": 1.00,
}

# Average household expenditure breakdown (% of income)
# Based on NSSO Household Consumer Expenditure Survey patterns
HOUSEHOLD_EXPENDITURE_PATTERN = {
    "low_income": {  # < 3 LPA
        "food": 0.45,
        "fuel": 0.10,
        "housing": 0.15,
        "education": 0.05,
        "healthcare": 0.08,
        "clothing": 0.05,
        "transport": 0.07,
        "recreation": 0.02,
        "miscellaneous": 0.03,
        "savings_rate": 0.05,
    },
    "lower_middle": {  # 3-7 LPA
        "food": 0.35,
        "fuel": 0.08,
        "housing": 0.18,
        "education": 0.10,
        "healthcare": 0.07,
        "clothing": 0.05,
        "transport": 0.08,
        "recreation": 0.03,
        "miscellaneous": 0.04,
        "savings_rate": 0.10,
    },
    "middle": {  # 7-15 LPA
        "food": 0.28,
        "fuel": 0.07,
        "housing": 0.20,
        "education": 0.12,
        "healthcare": 0.06,
        "clothing": 0.04,
        "transport": 0.08,
        "recreation": 0.04,
        "miscellaneous": 0.05,
        "savings_rate": 0.15,
    },
    "upper_middle": {  # 15-30 LPA
        "food": 0.20,
        "fuel": 0.05,
        "housing": 0.22,
        "education": 0.14,
        "healthcare": 0.05,
        "clothing": 0.04,
        "transport": 0.07,
        "recreation": 0.05,
        "miscellaneous": 0.05,
        "savings_rate": 0.20,
    },
    "high": {  # > 30 LPA
        "food": 0.15,
        "fuel": 0.04,
        "housing": 0.20,
        "education": 0.12,
        "healthcare": 0.05,
        "clothing": 0.04,
        "transport": 0.06,
        "recreation": 0.06,
        "miscellaneous": 0.06,
        "savings_rate": 0.28,
    },
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