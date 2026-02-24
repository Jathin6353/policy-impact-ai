import { SUBSIDIES } from './policyData';

export function checkSubsidies(income, occupation, familySize) {
  const results = [];
  let totalBenefit = 0;

  for (const [key, sub] of Object.entries(SUBSIDIES)) {
    let eligible = true;
    const reasons = [];

    if (sub.maxIncome && income > sub.maxIncome) {
      eligible = false;
      reasons.push(`Income exceeds ₹${(sub.maxIncome / 100000).toFixed(0)}L limit`);
    }

    if (sub.occupations && !sub.occupations.includes(occupation.toLowerCase())) {
      eligible = false;
      reasons.push(`Requires: ${sub.occupations.join(', ')}`);
    }

    if (eligible) totalBenefit += sub.annual;

    results.push({
      scheme: key,
      name: sub.name,
      eligible,
      annualBenefit: eligible ? sub.annual : 0,
      reasons: eligible ? ['All criteria met'] : reasons,
    });
  }

  return { subsidies: results, totalAnnual: totalBenefit, totalMonthly: Math.round(totalBenefit / 12) };
}