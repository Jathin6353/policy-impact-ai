/**
 * Tax Calculator — FY 2026-27
 * Based on Union Budget 2026-27 and Income Tax Act, 2025
 */

import { TAX_SLABS, TAX_CONFIG, getStandardDeduction, getRebateLimit } from './policyData';

/**
 * Calculate income tax for FY 2026-27
 */
export function calculateTax(income, regime = 'new_2026', options = {}) {
  const slabs = TAX_SLABS[regime] || TAX_SLABS.new_2026;
  const standardDeduction = options.standardDeduction ?? getStandardDeduction(regime);
  const cessRate = options.cessRate ?? TAX_CONFIG.cessRate;
  
  // Calculate deductions
  let totalDeductions = standardDeduction;
  
  // Old regime allows additional deductions
  if (regime.includes('old')) {
    totalDeductions += Math.min(options.deductions80c || 0, TAX_CONFIG.deductions.section80C);
    totalDeductions += Math.min(options.deductions80d || 0, TAX_CONFIG.deductions.section80D_self);
    totalDeductions += Math.min(options.homeLoanInterest || 0, TAX_CONFIG.deductions.section24B);
    totalDeductions += Math.min(options.nps80ccd || 0, TAX_CONFIG.deductions.section80CCD_1B);
  }
  
  const taxableIncome = Math.max(0, income - totalDeductions);
  
  // Calculate basic tax using slabs
  let tax = 0;
  let remaining = taxableIncome;
  
  for (const slab of slabs) {
    if (remaining <= 0) break;
    const slabWidth = slab.max === Infinity ? remaining : slab.max - slab.min;
    const taxableInSlab = Math.min(remaining, slabWidth);
    tax += taxableInSlab * slab.rate;
    remaining -= taxableInSlab;
  }
  
  // Apply Rebate u/s 87A
  const rebateConfig = getRebateLimit(regime);
  let rebate = 0;
  if (taxableIncome <= rebateConfig.incomeLimit) {
    rebate = Math.min(tax, rebateConfig.maxRebate);
  }
  
  const taxAfterRebate = Math.max(0, tax - rebate);
  
  // Calculate Surcharge
  let surcharge = 0;
  for (const slab of TAX_CONFIG.surcharge) {
    if (income >= slab.min && income < slab.max) {
      surcharge = taxAfterRebate * slab.rate;
      break;
    }
  }
  
  // Calculate Cess
  const cess = (taxAfterRebate + surcharge) * cessRate;
  
  // Total Tax
  const totalTax = taxAfterRebate + surcharge + cess;
  
  return {
    grossIncome: income,
    standardDeduction,
    totalDeductions,
    taxableIncome,
    basicTax: Math.round(tax),
    rebate: Math.round(rebate),
    taxAfterRebate: Math.round(taxAfterRebate),
    surcharge: Math.round(surcharge),
    cess: Math.round(cess),
    totalTax: Math.round(totalTax),
    effectiveRate: income > 0 ? +((totalTax / income) * 100).toFixed(2) : 0,
    monthlyTax: Math.round(totalTax / 12),
    postTaxIncome: Math.round(income - totalTax),
    monthlyPostTax: Math.round((income - totalTax) / 12),
    regime,
    budgetYear: regime.includes('2026') ? '2026-27' : '2024-25',
  };
}

/**
 * Compare Old vs New Regime
 */
export function compareTaxRegimes(income, options = {}) {
  const oldTax = calculateTax(income, 'old_2026', options);
  const newTax = calculateTax(income, 'new_2026', options);
  
  const savings = oldTax.totalTax - newTax.totalTax;
  
  return {
    old: oldTax,
    new: newTax,
    savingsWithNew: savings,
    recommended: savings > 0 ? 'new' : 'old',
    monthlyDifference: Math.round(savings / 12),
    reason: savings > 0 
      ? `New regime saves ₹${Math.abs(savings).toLocaleString('en-IN')}/year`
      : `Old regime saves ₹${Math.abs(savings).toLocaleString('en-IN')}/year with your deductions`,
  };
}

/**
 * Compare Budget 2026 vs Budget 2024 Tax
 */
export function compareBudgetYears(income) {
  const tax2024 = calculateTax(income, 'new_2024');
  const tax2026 = calculateTax(income, 'new_2026');
  
  const benefit = tax2024.totalTax - tax2026.totalTax;
  
  return {
    budget2024: tax2024,
    budget2026: tax2026,
    annualBenefit: benefit,
    monthlyBenefit: Math.round(benefit / 12),
    benefitPercent: income > 0 ? +((benefit / income) * 100).toFixed(2) : 0,
    summary: benefit > 0 
      ? `Budget 2026 saves you ₹${benefit.toLocaleString('en-IN')}/year`
      : 'No additional benefit from Budget 2026',
  };
}

/**
 * Calculate Marginal Tax Rate
 */
export function getMarginalRate(income, regime = 'new_2026') {
  const slabs = TAX_SLABS[regime];
  const standardDeduction = getStandardDeduction(regime);
  const taxableIncome = Math.max(0, income - standardDeduction);
  
  for (let i = slabs.length - 1; i >= 0; i--) {
    if (taxableIncome > slabs[i].min) {
      const baseRate = slabs[i].rate * 100;
      const withCess = baseRate * 1.04;  // 4% cess
      return {
        marginalRate: baseRate,
        effectiveMarginaRate: +withCess.toFixed(2),
        slab: `₹${(slabs[i].min / 100000).toFixed(0)}L - ₹${slabs[i].max === Infinity ? '∞' : (slabs[i].max / 100000).toFixed(0) + 'L'}`,
      };
    }
  }
  
  return { marginalRate: 0, effectiveMarginalRate: 0, slab: 'Below taxable limit' };
}