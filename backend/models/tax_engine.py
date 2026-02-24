"""
Tax Calculation Engine
Handles both old and new regime with all edge cases
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.tax_slabs import (
    get_regime_slabs,
    SURCHARGE_RATES,
    HEALTH_EDUCATION_CESS,
    STANDARD_DEDUCTION_NEW,
    STANDARD_DEDUCTION_OLD,
    SECTION_80C_LIMIT,
)


class TaxEngine:
    """Complete Indian Income Tax Calculator"""

    def __init__(self, regime: str = "new", year: str = "2024"):
        self.regime = regime
        self.year = year
        self.slabs = get_regime_slabs(regime, year)

    def calculate_basic_tax(self, taxable_income: float) -> float:
        """Calculate tax based on slab rates"""
        tax = 0
        remaining = taxable_income

        for slab in self.slabs:
            if remaining <= 0:
                break

            slab_width = slab["max"] - slab["min"]
            taxable_in_slab = min(remaining, slab_width)
            tax += taxable_in_slab * slab["rate"]
            remaining -= taxable_in_slab

        return round(tax, 2)

    def calculate_surcharge(self, basic_tax: float, income: float) -> float:
        """Calculate surcharge based on income level"""
        for slab in SURCHARGE_RATES:
            if slab["min"] <= income < slab["max"]:
                return round(basic_tax * slab["rate"], 2)
        return 0

    def calculate_cess(
        self,
        basic_tax: float,
        surcharge: float,
        cess_rate: float = None
    ) -> float:
        """Calculate Health and Education Cess"""
        rate = cess_rate if cess_rate else HEALTH_EDUCATION_CESS
        return round((basic_tax + surcharge) * rate, 2)

    def get_deductions(
        self,
        gross_income: float,
        investments_80c: float = 0,
        health_insurance_80d: float = 0,
        hra_claimed: float = 0,
        home_loan_interest: float = 0,
        nps_80ccd: float = 0,
    ) -> dict:
        """Calculate total deductions based on regime"""
        deductions = {}

        if self.regime == "new" or self.year == "2025_proposed":
            # New regime: only standard deduction
            std_ded = (
                STANDARD_DEDUCTION_NEW
                if self.year == "2024" or self.year == "2025_proposed"
                else 50000
            )
            deductions["standard_deduction"] = std_ded
            deductions["total"] = std_ded
        else:
            # Old regime: all deductions available
            deductions["standard_deduction"] = STANDARD_DEDUCTION_OLD
            deductions["section_80c"] = min(investments_80c, SECTION_80C_LIMIT)
            deductions["section_80d"] = min(health_insurance_80d, 75000)
            deductions["hra"] = hra_claimed
            deductions["home_loan_24b"] = min(home_loan_interest, 200000)
            deductions["nps_80ccd"] = min(nps_80ccd, 50000)
            deductions["total"] = sum(deductions.values())

        return deductions

    def compute_full_tax(
        self,
        gross_income: float,
        investments_80c: float = 0,
        health_insurance: float = 0,
        hra: float = 0,
        home_loan_interest: float = 0,
        nps: float = 0,
        custom_cess_rate: float = None,
        custom_standard_deduction: float = None,
    ) -> dict:
        """Complete tax computation"""
        # Deductions
        deductions = self.get_deductions(
            gross_income,
            investments_80c,
            health_insurance,
            hra,
            home_loan_interest,
            nps,
        )

        if custom_standard_deduction is not None:
            deductions["standard_deduction"] = custom_standard_deduction
            deductions["total"] = sum(
                v for k, v in deductions.items() if k != "total"
            )

        taxable_income = max(0, gross_income - deductions["total"])

        # Rebate u/s 87A
        rebate = 0
        if self.regime == "new" and taxable_income <= 700000:
            basic_tax = self.calculate_basic_tax(taxable_income)
            rebate = min(basic_tax, 25000)
        elif self.regime == "old" and taxable_income <= 500000:
            basic_tax = self.calculate_basic_tax(taxable_income)
            rebate = min(basic_tax, 12500)

        basic_tax = self.calculate_basic_tax(taxable_income)
        basic_tax_after_rebate = max(0, basic_tax - rebate)

        surcharge = self.calculate_surcharge(basic_tax_after_rebate, gross_income)
        cess = self.calculate_cess(
            basic_tax_after_rebate,
            surcharge,
            custom_cess_rate
        )

        total_tax = basic_tax_after_rebate + surcharge + cess

        effective_rate = (total_tax / gross_income * 100) if gross_income > 0 else 0

        monthly_tax = total_tax / 12

        return {
            "gross_income": gross_income,
            "deductions": deductions,
            "taxable_income": taxable_income,
            "basic_tax": basic_tax,
            "rebate_87a": rebate,
            "tax_after_rebate": basic_tax_after_rebate,
            "surcharge": surcharge,
            "cess": cess,
            "total_tax": round(total_tax, 2),
            "effective_rate": round(effective_rate, 2),
            "monthly_tax": round(monthly_tax, 2),
            "post_tax_income": round(gross_income - total_tax, 2),
            "monthly_post_tax": round((gross_income - total_tax) / 12, 2),
            "regime": self.regime,
            "year": self.year,
        }


def compare_tax_regimes(gross_income: float, **kwargs) -> dict:
    """Compare tax under old vs new regime"""
    old_engine = TaxEngine("old", "2024")
    new_engine = TaxEngine("new", "2024")

    old_tax = old_engine.compute_full_tax(gross_income, **kwargs)
    new_tax = new_engine.compute_full_tax(gross_income, **kwargs)

    savings = old_tax["total_tax"] - new_tax["total_tax"]

    return {
        "old_regime": old_tax,
        "new_regime": new_tax,
        "savings_with_new": round(savings, 2),
        "recommended": "new" if savings > 0 else "old",
        "monthly_difference": round(savings / 12, 2),
    }