import { calculateTax } from './taxCalculator';
import { simulateInflation } from './inflationSimulator';
import { checkSubsidies } from './subsidyChecker';
import { calculateStress } from './stressScorer';
import { SCENARIOS, getIncomeBracket } from './policyData';

export function runFullSimulation(profile, scenarioId = 'status_quo') {
  const scenario = SCENARIOS[scenarioId] || SCENARIOS.status_quo;
  const changes = scenario.changes;
  const bracket = getIncomeBracket(profile.annualIncome);

  // Tax
  let taxRegime = 'new_2024';
  let taxOptions = {};
  if (changes.tax_regime === 'proposed_2025') taxRegime = 'proposed_2025';
  if (changes.cess_rate) taxOptions.cessRate = changes.cess_rate;
  if (changes.standard_deduction) taxOptions.standardDeduction = changes.standard_deduction;

  const tax = calculateTax(profile.annualIncome, taxRegime, taxOptions);

  // Inflation
  const inflRate = changes.inflation_override || 5.5;
  const inflation = simulateInflation(profile.annualIncome, profile.familySize, inflRate);

  // Fuel
  let fuelImpact = { monthlyIncrease: 0, annualIncrease: 0 };
  if (changes.fuel_hike) {
    const baseFuelMonthly = profile.annualIncome / 12 * (bracket === 'low_income' ? 0.10 : bracket === 'lower_middle' ? 0.08 : 0.07);
    const directInc = baseFuelMonthly * (changes.fuel_hike / 100);
    const cascadeInc = profile.annualIncome / 12 * 0.03 * (changes.fuel_hike / 10);
    fuelImpact = {
      monthlyIncrease: Math.round(directInc + cascadeInc),
      annualIncrease: Math.round((directInc + cascadeInc) * 12),
    };
  }

  // Food GST
  let foodGstImpact = { annualBurden: 0 };
  if (changes.food_gst) {
    const foodSpend = profile.annualIncome / 12 * (bracket === 'low_income' ? 0.45 : 0.28);
    const familyAdj = foodSpend * (1 + (profile.familySize - 1) * 0.15);
    const gst = familyAdj * 0.6 * changes.food_gst;
    foodGstImpact = { monthlyBurden: Math.round(gst), annualBurden: Math.round(gst * 12) };
  }

  // Subsidies
  const subsidyResult = checkSubsidies(profile.annualIncome, profile.occupation, profile.familySize);
  let totalSubsidy = subsidyResult.totalAnnual;
  if (changes.remove_subsidy) {
    const removed = subsidyResult.subsidies.find(s => s.scheme === changes.remove_subsidy + '_subsidy' || s.scheme === changes.remove_subsidy);
    if (removed && removed.eligible) {
      totalSubsidy -= removed.annualBenefit;
      removed.eligible = false;
      removed.annualBenefit = 0;
    }
  }

  // UBI
  let ubiBenefit = 0;
  if (changes.ubi && profile.annualIncome <= (changes.ubi_limit || Infinity)) {
    ubiBenefit = changes.ubi * 12;
  }

  // EMI impact
  let emiChange = 0;
  if (changes.rate_hike) {
    emiChange = Math.round(profile.monthlyEmi * changes.rate_hike * 0.07);
  }

  // Net calculation
  const totalNegative = tax.totalTax + inflation.totalAnnualIncrease + fuelImpact.annualIncrease + (foodGstImpact.annualBurden || 0) + (emiChange * 12);
  const totalPositive = totalSubsidy + ubiBenefit;
  const netDisposable = profile.annualIncome - totalNegative + totalPositive;

  // Stress
  const savingsRate = profile.annualIncome > 0 ? (netDisposable / profile.annualIncome * 100) : 0;
  const stress = calculateStress({
    income: profile.annualIncome,
    totalTax: tax.totalTax,
    monthlyEmi: profile.monthlyEmi + emiChange,
    familySize: profile.familySize,
    savingsRate: Math.max(0, savingsRate),
    occupation: profile.occupation,
    inflationImpact: inflation.totalAnnualIncrease,
    subsidyBenefit: totalSubsidy,
  });

  return {
    scenario,
    tax,
    inflation,
    fuelImpact,
    foodGstImpact,
    subsidies: subsidyResult,
    totalSubsidy,
    ubiBenefit,
    emiChange,
    totalNegative: Math.round(totalNegative),
    totalPositive: Math.round(totalPositive),
    netDisposableAnnual: Math.round(netDisposable),
    netDisposableMonthly: Math.round(netDisposable / 12),
    stress,
    bracket,
  };
}