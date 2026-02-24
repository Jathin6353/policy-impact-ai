"""
Indian Income Tax Slabs — FY 2024-25
Both Old and New Regime
All data from official Income Tax Department publications
"""

# New Tax Regime (Default from FY 2023-24)
NEW_REGIME_SLABS_2024 = [
    {"min": 0, "max": 300000, "rate": 0.0},
    {"min": 300000, "max": 700000, "rate": 0.05},
    {"min": 700000, "max": 1000000, "rate": 0.10},
    {"min": 1000000, "max": 1200000, "rate": 0.15},
    {"min": 1200000, "max": 1500000, "rate": 0.20},
    {"min": 1500000, "max": float("inf"), "rate": 0.30},
]

# Old Tax Regime
OLD_REGIME_SLABS_2024 = [
    {"min": 0, "max": 250000, "rate": 0.0},
    {"min": 250000, "max": 500000, "rate": 0.05},
    {"min": 500000, "max": 1000000, "rate": 0.20},
    {"min": 1000000, "max": float("inf"), "rate": 0.30},
]

# Proposed Scenario: Budget 2025 hypothetical changes
PROPOSED_NEW_REGIME_2025 = [
    {"min": 0, "max": 400000, "rate": 0.0},
    {"min": 400000, "max": 800000, "rate": 0.05},
    {"min": 800000, "max": 1200000, "rate": 0.10},
    {"min": 1200000, "max": 1500000, "rate": 0.15},
    {"min": 1500000, "max": 2000000, "rate": 0.20},
    {"min": 2000000, "max": float("inf"), "rate": 0.30},
]

# Surcharge rates
SURCHARGE_RATES = [
    {"min": 0, "max": 5000000, "rate": 0.0},
    {"min": 5000000, "max": 10000000, "rate": 0.10},
    {"min": 10000000, "max": 20000000, "rate": 0.15},
    {"min": 20000000, "max": 50000000, "rate": 0.25},
    {"min": 50000000, "max": float("inf"), "rate": 0.37},
]

HEALTH_EDUCATION_CESS = 0.04

# Standard deduction
STANDARD_DEDUCTION_NEW = 75000  # Updated in Budget 2024
STANDARD_DEDUCTION_OLD = 50000

# Section 80C limit
SECTION_80C_LIMIT = 150000

# Section 80D (Health Insurance)
SECTION_80D_SELF = 25000
SECTION_80D_PARENTS = 25000
SECTION_80D_SENIOR_PARENTS = 50000

# HRA exemption rules by city tier
METRO_HRA_PERCENT = 0.50  # Delhi, Mumbai, Chennai, Kolkata
NON_METRO_HRA_PERCENT = 0.40


def get_regime_slabs(regime: str, year: str = "2024"):
    """Return appropriate tax slabs"""
    if year == "2025_proposed":
        return PROPOSED_NEW_REGIME_2025
    if regime == "new":
        return NEW_REGIME_SLABS_2024
    return OLD_REGIME_SLABS_2024