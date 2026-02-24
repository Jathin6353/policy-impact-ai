export function calculateStress(params) {
  const { income, totalTax, monthlyEmi, familySize, savingsRate, occupation, inflationImpact, subsidyBenefit } = params;
  const scores = {};

  // Tax burden
  const taxRate = income > 0 ? (totalTax / income * 100) : 0;
  scores.tax_burden = Math.min(100, taxRate * 3.5);

  // Inflation vulnerability
  const inflPct = income > 0 ? (inflationImpact / income * 100) : 0;
  scores.inflation_vulnerability = Math.min(100, inflPct * 8);

  // Savings adequacy
  if (savingsRate > 25) scores.savings_adequacy = 10;
  else if (savingsRate > 15) scores.savings_adequacy = 30;
  else if (savingsRate > 10) scores.savings_adequacy = 50;
  else if (savingsRate > 5) scores.savings_adequacy = 70;
  else if (savingsRate > 0) scores.savings_adequacy = 85;
  else scores.savings_adequacy = 100;

  // Debt exposure
  const monthlyIncome = income / 12;
  const emiRatio = monthlyIncome > 0 ? (monthlyEmi / monthlyIncome * 100) : 0;
  if (emiRatio > 50) scores.debt_exposure = 100;
  else if (emiRatio > 40) scores.debt_exposure = 85;
  else if (emiRatio > 30) scores.debt_exposure = 65;
  else if (emiRatio > 20) scores.debt_exposure = 45;
  else if (emiRatio > 10) scores.debt_exposure = 25;
  else scores.debt_exposure = 10;

  // Subsidy dependency
  const subPct = income > 0 ? (subsidyBenefit / income * 100) : 0;
  scores.subsidy_dependency = Math.min(100, subPct * 5);

  // Income volatility
  const volMap = {
    salaried: 15, government: 10, self_employed: 55, small_business: 60,
    farmer: 75, agriculture: 75, daily_wage: 90, freelance: 70, retired: 30, student: 40,
  };
  scores.income_volatility = volMap[occupation.toLowerCase()] ?? 50;

  // Family burden
  const perCapita = income / Math.max(familySize, 1);
  if (perCapita > 500000) scores.family_burden = 10;
  else if (perCapita > 300000) scores.family_burden = 25;
  else if (perCapita > 150000) scores.family_burden = 45;
  else if (perCapita > 80000) scores.family_burden = 70;
  else if (perCapita > 40000) scores.family_burden = 85;
  else scores.family_burden = 100;

  const weights = {
    tax_burden: 0.15, inflation_vulnerability: 0.20, savings_adequacy: 0.20,
    debt_exposure: 0.15, subsidy_dependency: 0.10, income_volatility: 0.10, family_burden: 0.10
  };

  let composite = 0;
  for (const [k, w] of Object.entries(weights)) {
    composite += (scores[k] || 0) * w;
  }
  composite = Math.min(100, Math.max(0, +composite.toFixed(1)));

  let riskLevel, riskColor, riskDesc;
  if (composite < 20) { riskLevel = 'Low Risk'; riskColor = '#22c55e'; riskDesc = 'Stable financial position.'; }
  else if (composite < 40) { riskLevel = 'Moderate'; riskColor = '#84cc16'; riskDesc = 'Manageable exposure to policy changes.'; }
  else if (composite < 60) { riskLevel = 'Elevated'; riskColor = '#eab308'; riskDesc = 'Noticeable vulnerability. Budget adjustments may be needed.'; }
  else if (composite < 80) { riskLevel = 'High Risk'; riskColor = '#f97316'; riskDesc = 'Significant stress. Policy changes could severely impact savings.'; }
  else { riskLevel = 'Critical'; riskColor = '#ef4444'; riskDesc = 'Extreme vulnerability. Urgent financial planning needed.'; }

  return { composite, riskLevel, riskColor, riskDesc, scores, weights };
}