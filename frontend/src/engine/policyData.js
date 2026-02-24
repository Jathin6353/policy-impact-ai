// Complete client-side policy data — zero server dependency

export const TAX_SLABS = {
  new_2024: [
    { min: 0, max: 300000, rate: 0 },
    { min: 300000, max: 700000, rate: 0.05 },
    { min: 700000, max: 1000000, rate: 0.10 },
    { min: 1000000, max: 1200000, rate: 0.15 },
    { min: 1200000, max: 1500000, rate: 0.20 },
    { min: 1500000, max: Infinity, rate: 0.30 },
  ],
  old_2024: [
    { min: 0, max: 250000, rate: 0 },
    { min: 250000, max: 500000, rate: 0.05 },
    { min: 500000, max: 1000000, rate: 0.20 },
    { min: 1000000, max: Infinity, rate: 0.30 },
  ],
  proposed_2025: [
    { min: 0, max: 400000, rate: 0 },
    { min: 400000, max: 800000, rate: 0.05 },
    { min: 800000, max: 1200000, rate: 0.10 },
    { min: 1200000, max: 1500000, rate: 0.15 },
    { min: 1500000, max: 2000000, rate: 0.20 },
    { min: 2000000, max: Infinity, rate: 0.30 },
  ]
};

export const EXPENDITURE_PATTERNS = {
  low_income: { food: 0.45, fuel: 0.10, housing: 0.15, education: 0.05, healthcare: 0.08, transport: 0.07, savings: 0.05 },
  lower_middle: { food: 0.35, fuel: 0.08, housing: 0.18, education: 0.10, healthcare: 0.07, transport: 0.08, savings: 0.10 },
  middle: { food: 0.28, fuel: 0.07, housing: 0.20, education: 0.12, healthcare: 0.06, transport: 0.08, savings: 0.15 },
  upper_middle: { food: 0.20, fuel: 0.05, housing: 0.22, education: 0.14, healthcare: 0.05, transport: 0.07, savings: 0.20 },
  high: { food: 0.15, fuel: 0.04, housing: 0.20, education: 0.12, healthcare: 0.05, transport: 0.06, savings: 0.28 },
};

export const INFLATION_MULTIPLIERS = {
  food: 1.35, fuel: 1.50, housing: 0.85, education: 1.80,
  healthcare: 1.60, transport: 1.20, savings: 0
};

export const SCENARIOS = {
  status_quo: {
    id: 'status_quo', name: 'Current Policy (Status Quo)',
    description: 'No changes — baseline scenario', changes: {}, category: 'baseline'
  },
  tax_slab_reform_2025: {
    id: 'tax_slab_reform_2025', name: 'Proposed Tax Slab Reform 2025',
    description: 'Wider tax slabs with higher exemption. Zero tax up to ₹4L.',
    changes: { tax_regime: 'proposed_2025', standard_deduction: 100000 }, category: 'taxation'
  },
  fuel_hike_10: {
    id: 'fuel_hike_10', name: 'Fuel Price +10%',
    description: 'Petrol & diesel prices increase 10% due to crude oil surge.',
    changes: { fuel_hike: 10 }, category: 'fuel'
  },
  fuel_hike_20: {
    id: 'fuel_hike_20', name: 'Fuel Price +20%',
    description: 'Major fuel price surge scenario.',
    changes: { fuel_hike: 20 }, category: 'fuel'
  },
  subsidy_removal_lpg: {
    id: 'subsidy_removal_lpg', name: 'LPG Subsidy Removal',
    description: 'Government removes LPG subsidy for all.',
    changes: { remove_subsidy: 'lpg' }, category: 'subsidy'
  },
  education_cess_6: {
    id: 'education_cess_6', name: 'Education Cess → 6%',
    description: 'Health & Education Cess increased from 4% to 6%.',
    changes: { cess_rate: 0.06 }, category: 'taxation'
  },
  gst_food_5: {
    id: 'gst_food_5', name: '5% GST on Food',
    description: 'Previously exempt food items attract 5% GST.',
    changes: { food_gst: 0.05 }, category: 'taxation'
  },
  inflation_8: {
    id: 'inflation_8', name: 'Inflation Spikes to 8%',
    description: 'CPI rises to 8% annually.',
    changes: { inflation_override: 8.0 }, category: 'inflation'
  },
  interest_rate_hike: {
    id: 'interest_rate_hike', name: 'RBI Rate Hike +1.5%',
    description: 'Repo rate up 150bps. EMIs increase.',
    changes: { rate_hike: 1.5 }, category: 'monetary'
  },
  ubi_1000: {
    id: 'ubi_1000', name: 'UBI ₹1000/month',
    description: 'Universal Basic Income for adults below ₹5L.',
    changes: { ubi: 1000, ubi_limit: 500000 }, category: 'welfare'
  },
};

export const SUBSIDIES = {
  pm_kisan: { name: 'PM-KISAN', annual: 6000, occupations: ['farmer', 'agriculture'], maxIncome: null },
  lpg_subsidy: { name: 'LPG Subsidy', annual: 2400, occupations: null, maxIncome: 1000000 },
  food_subsidy: { name: 'NFSA Food', annual: 8400, occupations: null, maxIncome: 300000 },
  education_scholarship: { name: 'Central Scholarship', annual: 20000, occupations: null, maxIncome: 800000 },
  ayushman_bharat: { name: 'Ayushman Bharat', annual: 5000, occupations: null, maxIncome: 500000 },
  mudra_loan: { name: 'MUDRA Yojana', annual: 10000, occupations: ['self_employed', 'small_business', 'entrepreneur'], maxIncome: 1500000 },
};

export function getIncomeBracket(income) {
  if (income < 300000) return 'low_income';
  if (income < 700000) return 'lower_middle';
  if (income < 1500000) return 'middle';
  if (income < 3000000) return 'upper_middle';
  return 'high';
}