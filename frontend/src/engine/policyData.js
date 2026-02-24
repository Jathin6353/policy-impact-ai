/**
 * Policy Data — FY 2026-27
 * Based on Union Budget 2026-27 (Presented 1 Feb 2026)
 * 
 * Source: https://www.indiabudget.gov.in
 */

// ============================================
// TAX SLABS 2026-27
// ============================================
export const TAX_SLABS = {
  // New Tax Regime 2026-27 (Default)
  new_2026: [
    { min: 0, max: 400000, rate: 0 },        // Zero tax up to ₹4L
    { min: 400000, max: 800000, rate: 0.05 }, // 5% for ₹4L-8L
    { min: 800000, max: 1200000, rate: 0.10 }, // 10% for ₹8L-12L
    { min: 1200000, max: 1600000, rate: 0.15 }, // 15% for ₹12L-16L
    { min: 1600000, max: 2000000, rate: 0.20 }, // 20% for ₹16L-20L
    { min: 2000000, max: 2400000, rate: 0.25 }, // 25% for ₹20L-24L
    { min: 2400000, max: Infinity, rate: 0.30 }, // 30% above ₹24L
  ],
  
  // New Tax Regime 2024-25 (Previous - for comparison)
  new_2024: [
    { min: 0, max: 300000, rate: 0 },
    { min: 300000, max: 700000, rate: 0.05 },
    { min: 700000, max: 1000000, rate: 0.10 },
    { min: 1000000, max: 1200000, rate: 0.15 },
    { min: 1200000, max: 1500000, rate: 0.20 },
    { min: 1500000, max: Infinity, rate: 0.30 },
  ],
  
  // Old Tax Regime 2026-27
  old_2026: [
    { min: 0, max: 250000, rate: 0 },
    { min: 250000, max: 500000, rate: 0.05 },
    { min: 500000, max: 1000000, rate: 0.20 },
    { min: 1000000, max: Infinity, rate: 0.30 },
  ],
  
  // Speculative Future Reform
  proposed_2027: [
    { min: 0, max: 500000, rate: 0 },
    { min: 500000, max: 1000000, rate: 0.05 },
    { min: 1000000, max: 1500000, rate: 0.10 },
    { min: 1500000, max: 2000000, rate: 0.15 },
    { min: 2000000, max: 2500000, rate: 0.20 },
    { min: 2500000, max: Infinity, rate: 0.25 },
  ],
};

// ============================================
// TAX CONFIGURATION 2026-27
// ============================================
export const TAX_CONFIG = {
  // Standard Deduction
  standardDeduction: {
    new_2026: 100000,  // Increased to ₹1L
    new_2024: 75000,
    old_2026: 50000,
  },
  
  // Rebate u/s 87A
  rebate87A: {
    new_2026: { incomeLimit: 1200000, maxRebate: 60000 },
    new_2024: { incomeLimit: 700000, maxRebate: 25000 },
    old_2026: { incomeLimit: 500000, maxRebate: 12500 },
  },
  
  // Cess
  cessRate: 0.04,  // 4% Health & Education Cess
  
  // Surcharge (New Regime)
  surcharge: [
    { min: 0, max: 5000000, rate: 0 },
    { min: 5000000, max: 10000000, rate: 0.10 },
    { min: 10000000, max: 20000000, rate: 0.15 },
    { min: 20000000, max: 50000000, rate: 0.25 },
    { min: 50000000, max: Infinity, rate: 0.25 }, // Capped at 25%
  ],
  
  // Deduction Limits (Old Regime)
  deductions: {
    section80C: 150000,
    section80D_self: 25000,
    section80D_parents: 25000,
    section80D_senior_parents: 50000,
    section80CCD_1B: 50000,
    section24B: 200000,
  },
  
  // MAT Rate (Budget 2026)
  matRate: 0.14,  // Reduced from 15% to 14%
  
  // STT Rates (Budget 2026)
  stt: {
    futures: 0.0005,   // 0.05%
    options: 0.0015,   // 0.15%
    equityDelivery: 0.001,
  },
  
  // Capital Gains
  capitalGains: {
    ltcgEquityThreshold: 125000,
    ltcgEquityRate: 0.125,  // 12.5%
    stcgEquityRate: 0.20,   // 20%
  },
};

// ============================================
// BUDGET 2026-27 HIGHLIGHTS
// ============================================
export const BUDGET_2026_HIGHLIGHTS = {
  totalExpenditure: 5347000,    // ₹53.47 lakh crore
  totalRevenue: 3650000,        // ₹36.5 lakh crore
  capitalExpenditure: 1220000,  // ₹12.2 lakh crore (record)
  fiscalDeficitPercent: 4.3,
  debtToGDPPercent: 55.6,
  nominalGDPGrowthPercent: 10.0,
  presentationDate: '2026-02-01',
  effectiveDate: '2026-04-01',
  newIncomeTaxAct: 'Income Tax Act, 2025',
};

// ============================================
// MAJOR BUDGET ALLOCATIONS 2026-27
// ============================================
export const BUDGET_ALLOCATIONS = {
  infrastructure: { amount: 1220000, name: 'Infrastructure Capex', icon: '🏗️' },
  defence: { amount: 682000, name: 'Defence', icon: '🛡️' },
  education: { amount: 125000, name: 'Education', icon: '📚' },
  health: { amount: 95000, name: 'Health & Family Welfare', icon: '🏥' },
  agriculture: { amount: 145000, name: 'Agriculture & Allied', icon: '🌾' },
  ruralDevelopment: { amount: 175000, name: 'Rural Development', icon: '🏘️' },
  socialWelfare: { amount: 52000, name: 'Social Welfare', icon: '🤝' },
  semiconductors: { amount: 76000, name: 'Semiconductor Mission 2.0', icon: '💻' },
  greenHydrogen: { amount: 19700, name: 'Green Hydrogen Mission', icon: '⚡' },
  msme: { amount: 22000, name: 'MSME Support', icon: '🏭' },
};

// ============================================
// EXPENDITURE PATTERNS BY INCOME
// ============================================
export const EXPENDITURE_PATTERNS = {
  low_income: { 
    food: 0.48, fuel: 0.10, housing: 0.12, education: 0.04, 
    healthcare: 0.08, clothing: 0.05, transport: 0.06, savings: 0.02 
  },
  lower_middle: { 
    food: 0.38, fuel: 0.08, housing: 0.16, education: 0.08, 
    healthcare: 0.07, clothing: 0.05, transport: 0.08, savings: 0.08 
  },
  middle: { 
    food: 0.30, fuel: 0.07, housing: 0.18, education: 0.10, 
    healthcare: 0.06, clothing: 0.05, transport: 0.08, savings: 0.12 
  },
  upper_middle: { 
    food: 0.22, fuel: 0.05, housing: 0.20, education: 0.12, 
    healthcare: 0.05, clothing: 0.04, transport: 0.07, savings: 0.18 
  },
  high: { 
    food: 0.15, fuel: 0.04, housing: 0.18, education: 0.10, 
    healthcare: 0.05, clothing: 0.04, transport: 0.06, savings: 0.28 
  },
};

// ============================================
// INFLATION MULTIPLIERS
// ============================================
export const INFLATION_MULTIPLIERS = {
  food: 1.40,
  fuel: 1.35,
  housing: 0.80,
  education: 1.85,
  healthcare: 1.65,
  clothing: 0.85,
  transport: 1.25,
  savings: 0,
};

// Current inflation rate (FY 2026-27 projection)
export const CURRENT_INFLATION = 4.5;

// ============================================
// POLICY SCENARIOS 2026-27
// ============================================
export const SCENARIOS = {
  status_quo: {
    id: 'status_quo',
    name: 'Budget 2026-27 (Current)',
    description: 'Current policy as per Union Budget 2026-27',
    changes: { budget_year: '2026-27', tax_regime: 'new_2026' },
    category: 'baseline',
    icon: '📊',
  },
  pre_budget_2024: {
    id: 'pre_budget_2024',
    name: 'Pre-Budget 2024 (Old Policy)',
    description: 'Compare with policies before Budget 2024',
    changes: { tax_regime: 'new_2024', standard_deduction: 75000 },
    category: 'comparison',
    icon: '📅',
  },
  tax_regime_old: {
    id: 'tax_regime_old',
    name: 'Old Tax Regime',
    description: 'With deductions (80C, 80D, HRA)',
    changes: { tax_regime: 'old_2026' },
    category: 'taxation',
    icon: '💰',
  },
  fuel_hike_10: {
    id: 'fuel_hike_10',
    name: 'Fuel Price +10%',
    description: 'Petrol & diesel increase 10%',
    changes: { fuel_hike: 10 },
    category: 'fuel',
    icon: '⛽',
  },
  fuel_hike_20: {
    id: 'fuel_hike_20',
    name: 'Fuel Price +20%',
    description: 'Major fuel price surge',
    changes: { fuel_hike: 20 },
    category: 'fuel',
    icon: '⛽',
  },
  subsidy_removal_lpg: {
    id: 'subsidy_removal_lpg',
    name: 'LPG Subsidy Removal',
    description: 'No more LPG subsidy',
    changes: { remove_subsidy: 'lpg' },
    category: 'subsidy',
    icon: '🏛️',
  },
  cess_increase_6: {
    id: 'cess_increase_6',
    name: 'Education Cess → 6%',
    description: 'Cess increased from 4% to 6%',
    changes: { cess_rate: 0.06 },
    category: 'taxation',
    icon: '💰',
  },
  gst_food_5: {
    id: 'gst_food_5',
    name: '5% GST on Food',
    description: 'Food items attract 5% GST',
    changes: { food_gst: 0.05 },
    category: 'taxation',
    icon: '🍽️',
  },
  inflation_7: {
    id: 'inflation_7',
    name: 'Inflation → 7%',
    description: 'CPI rises to 7%',
    changes: { inflation_override: 7.0 },
    category: 'inflation',
    icon: '📈',
  },
  inflation_10: {
    id: 'inflation_10',
    name: 'Inflation → 10%',
    description: 'Severe inflation (crisis)',
    changes: { inflation_override: 10.0 },
    category: 'inflation',
    icon: '📈',
  },
  rbi_rate_hike: {
    id: 'rbi_rate_hike',
    name: 'RBI Rate +1%',
    description: 'Repo rate up 100bps',
    changes: { rate_hike: 1.0 },
    category: 'monetary',
    icon: '🏦',
  },
  rbi_rate_cut: {
    id: 'rbi_rate_cut',
    name: 'RBI Rate -1%',
    description: 'Repo rate cut 100bps',
    changes: { rate_hike: -1.0 },
    category: 'monetary',
    icon: '🏦',
  },
  ubi_1000: {
    id: 'ubi_1000',
    name: 'UBI ₹1000/month',
    description: 'For income below ₹5L',
    changes: { ubi: 1000, ubi_limit: 500000 },
    category: 'welfare',
    icon: '🤝',
  },
  ubi_2000: {
    id: 'ubi_2000',
    name: 'UBI ₹2000/month',
    description: 'For income below ₹8L',
    changes: { ubi: 2000, ubi_limit: 800000 },
    category: 'welfare',
    icon: '🤝',
  },
  pm_kisan_increase: {
    id: 'pm_kisan_increase',
    name: 'PM-KISAN → ₹8000',
    description: 'Increased from ₹6000/year',
    changes: { pm_kisan: 8000 },
    category: 'welfare',
    icon: '🌾',
  },
  ayushman_expansion: {
    id: 'ayushman_expansion',
    name: 'Ayushman → ₹10L',
    description: 'Coverage increased to ₹10L',
    changes: { ayushman_coverage: 1000000 },
    category: 'welfare',
    icon: '🏥',
  },
  semiconductor_boost: {
    id: 'semiconductor_boost',
    name: 'Semiconductor Mission 2.0',
    description: '₹76,000 Cr investment',
    changes: { sector_boost: 'semiconductor' },
    category: 'manufacturing',
    icon: '💻',
  },
  green_hydrogen: {
    id: 'green_hydrogen',
    name: 'Green Hydrogen Push',
    description: '₹19,700 Cr for green energy',
    changes: { sector_boost: 'green_hydrogen' },
    category: 'energy',
    icon: '⚡',
  },
  stt_impact: {
    id: 'stt_impact',
    name: 'New STT Rates',
    description: 'Budget 2026 STT changes',
    changes: { stt_futures: 0.0005, stt_options: 0.0015 },
    category: 'taxation',
    icon: '📊',
  },
};

// ============================================
// SUBSIDIES 2026-27
// ============================================
export const SUBSIDIES = {
  pm_kisan: { 
    name: 'PM-KISAN', 
    annual: 6000, 
    occupations: ['farmer', 'agriculture'], 
    maxIncome: null,
    website: 'pmkisan.gov.in',
    budget2026: 60000,
  },
  lpg_subsidy: { 
    name: 'PM Ujjwala (LPG)', 
    annual: 2400, 
    occupations: null, 
    maxIncome: 1000000,
    website: 'pmuy.gov.in',
    budget2026: 12000,
  },
  food_subsidy: { 
    name: 'NFSA Food', 
    annual: 8400, 
    occupations: null, 
    maxIncome: 300000,
    website: 'nfsa.gov.in',
    budget2026: 205000,
  },
  ayushman_bharat: { 
    name: 'Ayushman Bharat', 
    annual: 6000, 
    occupations: null, 
    maxIncome: 500000,
    coverage: 700000,  // Increased to ₹7L in Budget 2026
    website: 'pmjay.gov.in',
    budget2026: 7500,
  },
  pm_awas: { 
    name: 'PM Awas Yojana', 
    annual: 26700, 
    occupations: null, 
    maxIncome: 1800000,
    website: 'pmaymis.gov.in',
    budget2026: 80000,
  },
  education_scholarship: { 
    name: 'Central Scholarship', 
    annual: 20000, 
    occupations: null, 
    maxIncome: 800000,
    budget2026: 3000,
  },
  mudra_loan: { 
    name: 'PM MUDRA', 
    annual: 10000, 
    occupations: ['self_employed', 'small_business', 'entrepreneur'], 
    maxIncome: 1500000,
    website: 'mudra.org.in',
    budget2026: 10000,
  },
  pm_surya_ghar: { 
    name: 'PM Surya Ghar (Solar)', 
    annual: 18000, 
    occupations: null, 
    maxIncome: 1800000,
    website: 'pmsuryaghar.gov.in',
    budget2026: 75000,
  },
  skill_loan: { 
    name: 'Skill Loan 2026', 
    annual: 22500, 
    occupations: null, 
    maxIncome: null,
    maxLoan: 750000,  // Increased to ₹7.5L
    budget2026: 5000,
  },
};

// ============================================
// HELPER FUNCTIONS
// ============================================
export function getIncomeBracket(income) {
  if (income < 300000) return 'low_income';
  if (income < 700000) return 'lower_middle';
  if (income < 1500000) return 'middle';
  if (income < 3000000) return 'upper_middle';
  return 'high';
}

export function getScenariosByCategory(category) {
  return Object.values(SCENARIOS).filter(s => s.category === category);
}

export function getTaxSlabs(regime = 'new_2026') {
  return TAX_SLABS[regime] || TAX_SLABS.new_2026;
}

export function getStandardDeduction(regime = 'new_2026') {
  return TAX_CONFIG.standardDeduction[regime] || 100000;
}

export function getRebateLimit(regime = 'new_2026') {
  return TAX_CONFIG.rebate87A[regime] || TAX_CONFIG.rebate87A.new_2026;
}