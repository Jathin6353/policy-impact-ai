"""
Financial Stress Scoring Engine
Creates a composite risk index for a household
"""


class StressScorer:
    """
    Calculate a composite Financial Stress Index (0-100)
    Higher = more stressed
    """

    WEIGHTS = {
        "tax_burden": 0.15,
        "inflation_vulnerability": 0.20,
        "savings_adequacy": 0.20,
        "debt_exposure": 0.15,
        "subsidy_dependency": 0.10,
        "income_volatility": 0.10,
        "family_burden": 0.10,
    }

    def calculate_stress_index(
        self,
        annual_income: float,
        total_tax: float,
        monthly_emi: float,
        family_size: int,
        savings_rate: float,
        occupation: str,
        inflation_impact: float,
        subsidy_benefit: float,
    ) -> dict:
        """Calculate comprehensive financial stress index"""
        scores = {}

        # 1. Tax burden score (0-100)
        tax_rate = (total_tax / annual_income * 100) if annual_income > 0 else 0
        scores["tax_burden"] = min(100, tax_rate * 3.5)

        # 2. Inflation vulnerability (0-100)
        inflation_pct = (
            (inflation_impact / annual_income * 100)
            if annual_income > 0
            else 0
        )
        scores["inflation_vulnerability"] = min(100, inflation_pct * 8)

        # 3. Savings adequacy (0-100, higher = worse)
        if savings_rate > 25:
            scores["savings_adequacy"] = 10
        elif savings_rate > 15:
            scores["savings_adequacy"] = 30
        elif savings_rate > 10:
            scores["savings_adequacy"] = 50
        elif savings_rate > 5:
            scores["savings_adequacy"] = 70
        elif savings_rate > 0:
            scores["savings_adequacy"] = 85
        else:
            scores["savings_adequacy"] = 100

        # 4. Debt exposure (0-100)
        monthly_income = annual_income / 12
        if monthly_income > 0:
            emi_ratio = (monthly_emi / monthly_income) * 100
        else:
            emi_ratio = 0

        if emi_ratio > 50:
            scores["debt_exposure"] = 100
        elif emi_ratio > 40:
            scores["debt_exposure"] = 85
        elif emi_ratio > 30:
            scores["debt_exposure"] = 65
        elif emi_ratio > 20:
            scores["debt_exposure"] = 45
        elif emi_ratio > 10:
            scores["debt_exposure"] = 25
        else:
            scores["debt_exposure"] = 10

        # 5. Subsidy dependency (0-100)
        if annual_income > 0:
            subsidy_pct = (subsidy_benefit / annual_income) * 100
        else:
            subsidy_pct = 0
        scores["subsidy_dependency"] = min(100, subsidy_pct * 5)

        # 6. Income volatility based on occupation (0-100)
        volatility_map = {
            "salaried": 15,
            "government": 10,
            "self_employed": 55,
            "small_business": 60,
            "entrepreneur": 65,
            "farmer": 75,
            "agriculture": 75,
            "daily_wage": 90,
            "freelance": 70,
            "gig_worker": 75,
            "retired": 30,
            "student": 40,
        }
        scores["income_volatility"] = volatility_map.get(
            occupation.lower(), 50
        )

        # 7. Family burden (0-100)
        per_capita_income = annual_income / max(family_size, 1)
        if per_capita_income > 500000:
            scores["family_burden"] = 10
        elif per_capita_income > 300000:
            scores["family_burden"] = 25
        elif per_capita_income > 150000:
            scores["family_burden"] = 45
        elif per_capita_income > 80000:
            scores["family_burden"] = 70
        elif per_capita_income > 40000:
            scores["family_burden"] = 85
        else:
            scores["family_burden"] = 100

        # Weighted composite
        composite = sum(
            scores[key] * weight
            for key, weight in self.WEIGHTS.items()
        )
        composite = round(min(100, max(0, composite)), 1)

        # Risk category
        if composite < 20:
            risk_level = "Low Risk"
            risk_color = "#22c55e"
            risk_description = (
                "Your financial position is stable. "
                "Policy changes have minimal impact."
            )
        elif composite < 40:
            risk_level = "Moderate"
            risk_color = "#84cc16"
            risk_description = (
                "Manageable financial exposure. "
                "Some policy changes may affect monthly budgets."
            )
        elif composite < 60:
            risk_level = "Elevated"
            risk_color = "#eab308"
            risk_description = (
                "Noticeable vulnerability to policy shifts. "
                "Budget adjustments may be needed."
            )
        elif composite < 80:
            risk_level = "High Risk"
            risk_color = "#f97316"
            risk_description = (
                "Significant financial stress. "
                "Policy changes could severely impact savings."
            )
        else:
            risk_level = "Critical"
            risk_color = "#ef4444"
            risk_description = (
                "Extreme financial vulnerability. "
                "Urgent need for financial planning."
            )

        return {
            "composite_score": composite,
            "risk_level": risk_level,
            "risk_color": risk_color,
            "risk_description": risk_description,
            "component_scores": scores,
            "weights": self.WEIGHTS,
            "weighted_scores": {
                key: round(scores[key] * self.WEIGHTS[key], 2)
                for key in scores
            },
        }