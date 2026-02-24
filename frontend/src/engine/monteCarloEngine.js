// Client-side Monte Carlo — runs entirely in browser

function normalRandom(mean, std) {
  // Box-Muller transform
  const u1 = Math.random();
  const u2 = Math.random();
  const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
  return mean + z * std;
}

export function runMonteCarlo(income, expenseRatio = 0.8, years = 3, simulations = 500) {
  const results = [];

  for (let s = 0; s < simulations; s++) {
    const trajectory = [];
    let currentIncome = income;
    let currentExpenses = income * expenseRatio;

    for (let y = 1; y <= years; y++) {
      const growth = Math.max(normalRandom(5, 3) / 100, -0.10);
      const inflation = Math.max(normalRandom(5.5, 2) / 100, 0.01);

      currentIncome *= (1 + growth);
      currentExpenses *= (1 + inflation);

      trajectory.push({
        year: y,
        income: currentIncome,
        expenses: currentExpenses,
        savings: currentIncome - currentExpenses,
        savingsRate: currentIncome > 0 ? ((currentIncome - currentExpenses) / currentIncome * 100) : 0,
      });
    }
    results.push(trajectory);
  }

  // Analyze
  const analysis = { yearly: [] };
  for (let y = 0; y < years; y++) {
    const savings = results.map(r => r[y].savings).sort((a, b) => a - b);
    const incomes = results.map(r => r[y].income);
    const expenses = results.map(r => r[y].expenses);

    analysis.yearly.push({
      year: y + 1,
      savings: {
        mean: Math.round(avg(savings)),
        median: Math.round(percentile(savings, 50)),
        p10: Math.round(percentile(savings, 10)),
        p90: Math.round(percentile(savings, 90)),
        negativeProb: +(savings.filter(s => s < 0).length / savings.length * 100).toFixed(1),
      },
      income: { mean: Math.round(avg(incomes)), median: Math.round(percentile(incomes, 50)) },
      expenses: { mean: Math.round(avg(expenses)), median: Math.round(percentile(expenses, 50)) },
    });
  }

  const finalSavings = results.map(r => r[years - 1].savings);
  analysis.summary = {
    simulations,
    probabilityNegative: +(finalSavings.filter(s => s < 0).length / finalSavings.length * 100).toFixed(1),
    worstCase: Math.round(percentile(finalSavings.sort((a,b)=>a-b), 5)),
    bestCase: Math.round(percentile(finalSavings, 95)),
    expected: Math.round(avg(finalSavings)),
  };

  return analysis;
}

function avg(arr) { return arr.reduce((a, b) => a + b, 0) / arr.length; }
function percentile(sorted, p) {
  const idx = Math.ceil(p / 100 * sorted.length) - 1;
  return sorted[Math.max(0, idx)];
}