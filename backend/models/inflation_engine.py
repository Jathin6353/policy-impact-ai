"""
Inflation Impact Simulation Engine
Projects real purchasing power erosion
"""
import numpy as np
from data.inflation_data import (
    CPI_INFLATION_HISTORY,
    CATEGORY_INFLATION_MULTIPLIERS,
    get_income_bracket,
    get_expenditure_pattern,
)


class InflationEngine:
    """Simulate inflation impact on household finances"""

    def __init__(self, annual_income: float, family_size: int = 4):
        self.annual_income = annual_income
        self.family_size = family_size
        self.bracket = get_income_bracket(annual_income)
        self.expenditure_pattern = get_expenditure_pattern(annual_income)
        self.base_inflation = self._get_projected_inflation()

    def _get_projected_inflation(self) -> float:
        """Get baseline inflation projection using trend"""
        recent_rates = list(CPI_INFLATION_HISTORY.values())[-5:]
        return np.mean(recent_rates)

    def calculate_category_inflation(
        self,
        inflation_override: float = None
    ) -> dict:
        """Calculate inflation impact per spending category"""
        base_rate = (
            inflation_override
            if inflation_override
            else self.base_inflation
        )

        monthly_income = self.annual_income / 12
        category_impact = {}

        for category, spend_ratio in self.expenditure_pattern.items():
            if category == "savings_rate":
                continue

            multiplier = CATEGORY_INFLATION_MULTIPLIERS.get(category, 1.0)
            effective_inflation = base_rate * multiplier / 100

            monthly_spend = monthly_income * spend_ratio
            monthly_increase = monthly_spend * effective_inflation

            # Family size adjustment
            family_multiplier = 1 + (self.family_size - 1) * 0.15
            if category in ["food", "healthcare", "education"]:
                monthly_increase *= family_multiplier

            category_impact[category] = {
                "current_monthly_spend": round(monthly_spend, 2),
                "effective_inflation_rate": round(
                    base_rate * multiplier, 2
                ),
                "monthly_increase": round(monthly_increase, 2),
                "annual_increase": round(monthly_increase * 12, 2),
            }

        total_monthly_increase = sum(
            v["monthly_increase"] for v in category_impact.values()
        )

        return {
            "base_inflation_rate": round(base_rate, 2),
            "income_bracket": self.bracket,
            "category_breakdown": category_impact,
            "total_monthly_increase": round(total_monthly_increase, 2),
            "total_annual_increase": round(total_monthly_increase * 12, 2),
            "purchasing_power_loss_percent": round(
                (total_monthly_increase * 12) / self.annual_income * 100, 2
            ),
        }

    def project_expenses(
        self,
        years: int = 3,
        inflation_override: float = None
    ) -> list:
        """Project expenses over multiple years"""
        base_rate = (
            inflation_override
            if inflation_override
            else self.base_inflation
        )

        monthly_income = self.annual_income / 12
        monthly_expenses = monthly_income * (
            1 - self.expenditure_pattern.get("savings_rate", 0.10)
        )

        projections = []
        for year in range(years + 1):
            # Compound inflation
            inflated_expenses = monthly_expenses * (
                (1 + base_rate / 100) ** year
            )
            income_growth_rate = max(base_rate - 1.5, 2.0)
            projected_income = monthly_income * (
                (1 + income_growth_rate / 100) ** year
            )

            gap = projected_income - inflated_expenses
            savings_rate = (gap / projected_income * 100) if projected_income > 0 else 0

            projections.append({
                "year": year,
                "monthly_income": round(projected_income, 2),
                "monthly_expenses": round(inflated_expenses, 2),
                "monthly_savings": round(gap, 2),
                "savings_rate_percent": round(savings_rate, 2),
                "annual_income": round(projected_income * 12, 2),
                "annual_expenses": round(inflated_expenses * 12, 2),
                "cumulative_erosion": round(
                    (inflated_expenses - monthly_expenses) * 12 * year, 2
                ),
            })

        return projections

    def calculate_food_gst_impact(
        self,
        gst_rate: float,
        affected_share: float = 0.6
    ) -> dict:
        """Calculate impact of GST on food items"""
        monthly_income = self.annual_income / 12
        food_spend_ratio = self.expenditure_pattern.get("food", 0.30)
        monthly_food = monthly_income * food_spend_ratio

        family_multiplier = 1 + (self.family_size - 1) * 0.15
        adjusted_food = monthly_food * family_multiplier

        affected_amount = adjusted_food * affected_share
        gst_burden = affected_amount * gst_rate

        return {
            "monthly_food_spend": round(adjusted_food, 2),
            "affected_amount": round(affected_amount, 2),
            "monthly_gst_burden": round(gst_burden, 2),
            "annual_gst_burden": round(gst_burden * 12, 2),
            "percent_of_income": round(
                gst_burden * 12 / self.annual_income * 100, 2
            ),
        }