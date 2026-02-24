"""
Monte Carlo Simulation Engine
For probabilistic financial impact projections
"""
import numpy as np
from typing import Dict, List


class MonteCarloEngine:
    """
    Run Monte Carlo simulations for financial projections
    Accounts for uncertainty in inflation, income growth, policy changes
    """

    def __init__(self, num_simulations: int = 1000, seed: int = 42):
        self.num_simulations = num_simulations
        np.random.seed(seed)

    def simulate_income_trajectory(
        self,
        current_income: float,
        years: int = 3,
        mean_growth: float = 5.0,
        growth_std: float = 3.0,
        inflation_mean: float = 5.5,
        inflation_std: float = 2.0,
        expense_ratio: float = 0.80,
        policy_shock: float = 0.0,
    ) -> Dict:
        """
        Simulate thousands of possible financial futures

        Args:
            current_income: Annual income
            years: Projection period
            mean_growth: Expected annual income growth %
            growth_std: Standard deviation of growth
            inflation_mean: Expected inflation %
            inflation_std: Inflation volatility
            expense_ratio: Current expense/income ratio
            policy_shock: One-time policy impact as % of income
        """
        results = []

        for _ in range(self.num_simulations):
            trajectory = []
            income = current_income
            expenses = income * expense_ratio

            # Apply policy shock in year 1
            income_after_shock = income * (1 - policy_shock / 100)

            for year in range(1, years + 1):
                # Random income growth
                growth = np.random.normal(mean_growth, growth_std) / 100
                growth = max(growth, -0.10)  # Cap decline at 10%
                income = (
                    income_after_shock if year == 1 else income
                ) * (1 + growth)

                # Random inflation
                inflation = np.random.normal(
                    inflation_mean, inflation_std
                ) / 100
                inflation = max(inflation, 0.01)
                expenses = expenses * (1 + inflation)

                savings = income - expenses
                savings_rate = (savings / income * 100) if income > 0 else 0

                trajectory.append({
                    "year": year,
                    "income": income,
                    "expenses": expenses,
                    "savings": savings,
                    "savings_rate": savings_rate,
                })

            results.append(trajectory)

        return self._analyze_results(results, years)

    def _analyze_results(
        self,
        results: List,
        years: int
    ) -> Dict:
        """Analyze Monte Carlo results for statistics"""
        analysis = {"yearly": [], "summary": {}}

        for year in range(years):
            incomes = [r[year]["income"] for r in results]
            expenses = [r[year]["expenses"] for r in results]
            savings = [r[year]["savings"] for r in results]
            savings_rates = [r[year]["savings_rate"] for r in results]

            year_stats = {
                "year": year + 1,
                "income": {
                    "mean": round(np.mean(incomes), 2),
                    "median": round(np.median(incomes), 2),
                    "p10": round(np.percentile(incomes, 10), 2),
                    "p25": round(np.percentile(incomes, 25), 2),
                    "p75": round(np.percentile(incomes, 75), 2),
                    "p90": round(np.percentile(incomes, 90), 2),
                },
                "expenses": {
                    "mean": round(np.mean(expenses), 2),
                    "median": round(np.median(expenses), 2),
                    "p10": round(np.percentile(expenses, 10), 2),
                    "p90": round(np.percentile(expenses, 90), 2),
                },
                "savings": {
                    "mean": round(np.mean(savings), 2),
                    "median": round(np.median(savings), 2),
                    "p10": round(np.percentile(savings, 10), 2),
                    "p90": round(np.percentile(savings, 90), 2),
                    "negative_probability": round(
                        sum(1 for s in savings if s < 0)
                        / len(savings)
                        * 100,
                        2,
                    ),
                },
                "savings_rate": {
                    "mean": round(np.mean(savings_rates), 2),
                    "median": round(np.median(savings_rates), 2),
                },
            }
            analysis["yearly"].append(year_stats)

        # Final year summary
        final_savings = [r[-1]["savings"] for r in results]
        analysis["summary"] = {
            "total_simulations": self.num_simulations,
            "years_projected": years,
            "probability_negative_savings": round(
                sum(1 for s in final_savings if s < 0)
                / len(final_savings)
                * 100,
                2,
            ),
            "probability_savings_above_10pct": round(
                sum(
                    1
                    for r in results
                    if r[-1]["savings_rate"] > 10
                )
                / len(results)
                * 100,
                2,
            ),
            "worst_case_savings": round(np.percentile(final_savings, 5), 2),
            "best_case_savings": round(np.percentile(final_savings, 95), 2),
            "expected_savings": round(np.mean(final_savings), 2),
        }

        # Distribution data for histogram
        analysis["distribution"] = {
            "savings_final_year": [round(s, 2) for s in sorted(final_savings)],
            "histogram_bins": self._create_histogram(final_savings),
        }

        return analysis

    def _create_histogram(
        self,
        data: List[float],
        num_bins: int = 20
    ) -> List[Dict]:
        """Create histogram data for frontend charting"""
        counts, bin_edges = np.histogram(data, bins=num_bins)
        histogram = []
        for i in range(len(counts)):
            histogram.append({
                "bin_start": round(bin_edges[i], 2),
                "bin_end": round(bin_edges[i + 1], 2),
                "count": int(counts[i]),
                "percentage": round(
                    counts[i] / len(data) * 100, 2
                ),
            })
        return histogram