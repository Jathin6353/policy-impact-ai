import { EXPENDITURE_PATTERNS, INFLATION_MULTIPLIERS, getIncomeBracket } from './policyData';

export function simulateInflation(income, familySize = 4, inflationRate = 5.5) {
  const bracket = getIncomeBracket(income);
  const pattern = EXPENDITURE_PATTERNS[bracket];
  const monthlyIncome = income / 12;
  const categories = {};
  let totalMonthlyIncrease = 0;

  for (const [cat, ratio] of Object.entries(pattern)) {
    if (cat === 'savings') continue;
    const multiplier = INFLATION_MULTIPLIERS[cat] || 1.0;
    const effectiveRate = inflationRate * multiplier;
    const monthlySpend = monthlyIncome * ratio;
    let increase = monthlySpend * (effectiveRate / 100);

    // Family size adjustment for essential categories
    if (['food', 'healthcare', 'education'].includes(cat)) {
      increase *= (1 + (familySize - 1) * 0.15);
    }

    categories[cat] = {
      monthlySpend: Math.round(monthlySpend),
      effectiveInflation: +(effectiveRate).toFixed(2),
      monthlyIncrease: Math.round(increase),
      annualIncrease: Math.round(increase * 12),
    };
    totalMonthlyIncrease += increase;
  }

  return {
    baseRate: inflationRate,
    bracket,
    categories,
    totalMonthlyIncrease: Math.round(totalMonthlyIncrease),
    totalAnnualIncrease: Math.round(totalMonthlyIncrease * 12),
    purchasingPowerLoss: +(totalMonthlyIncrease * 12 / income * 100).toFixed(2),
  };
}

export function projectExpenses(income, familySize, years = 3, inflationRate = 5.5) {
  const bracket = getIncomeBracket(income);
  const savingsRate = EXPENDITURE_PATTERNS[bracket].savings;
  const monthlyIncome = income / 12;
  const monthlyExpenses = monthlyIncome * (1 - savingsRate);
  const projections = [];

  for (let y = 0; y <= years; y++) {
    const inflated = monthlyExpenses * Math.pow(1 + inflationRate / 100, y);
    const growthRate = Math.max(inflationRate - 1.5, 2.0);
    const projectedIncome = monthlyIncome * Math.pow(1 + growthRate / 100, y);
    const gap = projectedIncome - inflated;

    projections.push({
      year: y,
      monthlyIncome: Math.round(projectedIncome),
      monthlyExpenses: Math.round(inflated),
      monthlySavings: Math.round(gap),
      savingsRate: projectedIncome > 0 ? +(gap / projectedIncome * 100).toFixed(1) : 0,
    });
  }
  return projections;
}