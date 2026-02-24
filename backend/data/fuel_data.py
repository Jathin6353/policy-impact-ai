"""
Fuel Price Data and Impact Model
Fuel prices affect everything — transport, food logistics, manufacturing
"""

# Current average fuel prices (₹/litre) — approximate national average
CURRENT_FUEL_PRICES = {
    "petrol": 104.50,
    "diesel": 91.30,
    "lpg_cylinder": 903.00,  # 14.2 kg domestic
    "cng": 76.50,
    "png": 52.00,  # per SCM
}

# Average monthly household fuel consumption
HOUSEHOLD_FUEL_CONSUMPTION = {
    "low_income": {
        "petrol_litres": 15,
        "diesel_litres": 0,
        "lpg_cylinders": 0.8,
        "cng_kg": 0,
    },
    "lower_middle": {
        "petrol_litres": 30,
        "diesel_litres": 0,
        "lpg_cylinders": 1.0,
        "cng_kg": 5,
    },
    "middle": {
        "petrol_litres": 50,
        "diesel_litres": 10,
        "lpg_cylinders": 1.0,
        "cng_kg": 10,
    },
    "upper_middle": {
        "petrol_litres": 70,
        "diesel_litres": 20,
        "lpg_cylinders": 1.0,
        "cng_kg": 15,
    },
    "high": {
        "petrol_litres": 100,
        "diesel_litres": 30,
        "lpg_cylinders": 1.0,
        "cng_kg": 20,
    },
}

# Fuel price cascade effect on other prices
# When fuel goes up 10%, these categories see price increases:
FUEL_CASCADE_MULTIPLIERS = {
    "food": 0.04,       # 10% fuel hike → 4% food price increase
    "transport": 0.07,  # 10% fuel hike → 7% transport cost increase
    "manufacturing": 0.03,
    "logistics": 0.06,
    "electricity": 0.02,
}

# State-wise fuel tax variation (VAT + surcharge as % of base)
STATE_FUEL_TAX = {
    "maharashtra": {"petrol": 0.39, "diesel": 0.25},
    "karnataka": {"petrol": 0.35, "diesel": 0.24},
    "tamil_nadu": {"petrol": 0.34, "diesel": 0.22},
    "delhi": {"petrol": 0.30, "diesel": 0.17},
    "uttar_pradesh": {"petrol": 0.36, "diesel": 0.23},
    "west_bengal": {"petrol": 0.35, "diesel": 0.27},
    "rajasthan": {"petrol": 0.38, "diesel": 0.26},
    "kerala": {"petrol": 0.37, "diesel": 0.25},
    "gujarat": {"petrol": 0.29, "diesel": 0.21},
    "madhya_pradesh": {"petrol": 0.40, "diesel": 0.27},
    "andhra_pradesh": {"petrol": 0.38, "diesel": 0.26},
    "telangana": {"petrol": 0.36, "diesel": 0.24},
    "bihar": {"petrol": 0.35, "diesel": 0.24},
    "punjab": {"petrol": 0.33, "diesel": 0.20},
    "haryana": {"petrol": 0.32, "diesel": 0.18},
    "default": {"petrol": 0.35, "diesel": 0.24},
}


def calculate_monthly_fuel_cost(income_bracket: str, state: str = "default") -> float:
    """Calculate monthly fuel expenditure"""
    consumption = HOUSEHOLD_FUEL_CONSUMPTION.get(
        income_bracket,
        HOUSEHOLD_FUEL_CONSUMPTION["middle"]
    )

    cost = 0
    cost += consumption["petrol_litres"] * CURRENT_FUEL_PRICES["petrol"]
    cost += consumption["diesel_litres"] * CURRENT_FUEL_PRICES["diesel"]
    cost += consumption["lpg_cylinders"] * CURRENT_FUEL_PRICES["lpg_cylinder"]
    cost += consumption["cng_kg"] * CURRENT_FUEL_PRICES["cng"]

    return round(cost, 2)


def simulate_fuel_hike_impact(
    hike_percent: float,
    income_bracket: str,
    annual_income: float
) -> dict:
    """Simulate cascading impact of fuel price hike"""
    monthly_fuel = calculate_monthly_fuel_cost(income_bracket)
    direct_increase = monthly_fuel * (hike_percent / 100)

    # Cascade effects
    monthly_income = annual_income / 12
    cascade_increase = 0
    for category, multiplier in FUEL_CASCADE_MULTIPLIERS.items():
        cascade_increase += monthly_income * 0.05 * multiplier * (hike_percent / 10)

    return {
        "direct_monthly_increase": round(direct_increase, 2),
        "cascade_monthly_increase": round(cascade_increase, 2),
        "total_monthly_increase": round(direct_increase + cascade_increase, 2),
        "annual_impact": round((direct_increase + cascade_increase) * 12, 2),
    }