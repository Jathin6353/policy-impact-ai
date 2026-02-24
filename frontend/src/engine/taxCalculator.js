import { TAX_SLABS } from './policyData';

export function calculateTax(income, regime = 'new_2024', options = {}) {
  const slabs = TAX_SLABS[regime] || TAX_SLABS.new_2024;
  const standardDeduction = options.standardDeduction ?? (regime.includes('new') || regime.includes('proposed') ? 75000 : 50000);
  const cessRate = options.cessRate ?? 0.04;

  const taxableIncome = Math.max(0, income - standardDeduction - (options.deductions80c || 0) * (regime.includes('old') ? 1 : 0));

  let tax = 0;
  let remaining = taxableIncome;

  for (const slab of slabs) {
    if (remaining <= 0) break;
    const slabWidth = slab.max === Infinity ? remaining : slab.max - slab.min;
    const taxableInSlab = Math.min(remaining, slabWidth);
    tax += taxableInSlab * slab.rate;
    remaining -= taxableInSlab;
  }

  // Rebate u/s 87A
  let rebate = 0;
  if ((regime.includes('new') || regime.includes('proposed')) && taxableIncome <= 700000) {
    rebate = Math.min(tax, 25000);
  } else if (regime.includes('old') && taxableIncome <= 500000) {
    rebate = Math.min(tax, 12500);
  }

  const taxAfterRebate = Math.max(0, tax - rebate);

  // Surcharge
  let surcharge = 0;
  if (income > 5000000) surcharge = taxAfterRebate * 0.10;
  if (income > 10000000) surcharge = taxAfterRebate * 0.15;
  if (income > 20000000) surcharge = taxAfterRebate * 0.25;

  const cess = (taxAfterRebate + surcharge) * cessRate;
  const totalTax = taxAfterRebate + surcharge + cess;

  return {
    grossIncome: income,
    standardDeduction,
    taxableIncome,
    basicTax: Math.round(tax),
    rebate: Math.round(rebate),
    taxAfterRebate: Math.round(taxAfterRebate),
    surcharge: Math.round(surcharge),
    cess: Math.round(cess),
    totalTax: Math.round(totalTax),
    effectiveRate: income > 0 ? +(totalTax / income * 100).toFixed(2) : 0,
    monthlyTax: Math.round(totalTax / 12),
    postTaxIncome: Math.round(income - totalTax),
    monthlyPostTax: Math.round((income - totalTax) / 12),
  };
}

export function compareTaxRegimes(income, options = {}) {
  const oldTax = calculateTax(income, 'old_2024', options);
  const newTax = calculateTax(income, 'new_2024', options);
  const savings = oldTax.totalTax - newTax.totalTax;
  return { old: oldTax, new: newTax, savingsWithNew: savings, recommended: savings > 0 ? 'new' : 'old' };
}