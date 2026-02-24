import React from 'react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend, BarChart, Bar } from 'recharts';
import { formatFullCurrency } from '../utils/formatters';

export function ExpenseProjectionChart({ data }) {
  return (
    <div className="card animate-in">
      <div className="card-title"><span className="icon">📈</span> 3-Year Financial Projection</div>
      <div className="chart-container">
        <ResponsiveContainer width="100%" height={300}>
          <AreaChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#2a2a4a" />
            <XAxis dataKey="year" stroke="#6868a0" tickFormatter={v => `Year ${v}`} />
            <YAxis stroke="#6868a0" tickFormatter={v => `₹${(v/1000).toFixed(0)}K`} />
            <Tooltip
              contentStyle={{ background: '#1a1a2e', border: '1px solid #2a2a4a', borderRadius: '8px' }}
              formatter={(v) => [formatFullCurrency(v)]}
            />
            <Legend />
            <Area type="monotone" dataKey="monthlyIncome" name="Income" stroke="#22c55e" fill="rgba(34,197,94,0.2)" strokeWidth={2} />
            <Area type="monotone" dataKey="monthlyExpenses" name="Expenses" stroke="#ef4444" fill="rgba(239,68,68,0.2)" strokeWidth={2} />
            <Area type="monotone" dataKey="monthlySavings" name="Savings" stroke="#6366f1" fill="rgba(99,102,241,0.2)" strokeWidth={2} />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export function InflationBreakdownChart({ categories }) {
  const data = Object.entries(categories).map(([key, val]) => ({
    category: key.charAt(0).toUpperCase() + key.slice(1),
    monthlyIncrease: val.monthlyIncrease,
    currentSpend: val.monthlySpend,
    effectiveRate: val.effectiveInflation,
  }));

  return (
    <div className="card animate-in">
      <div className="card-title"><span className="icon">📊</span> Inflation Impact by Category</div>
      <div className="chart-container">
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#2a2a4a" />
            <XAxis dataKey="category" stroke="#6868a0" angle={-20} textAnchor="end" height={60} fontSize={12} />
            <YAxis stroke="#6868a0" tickFormatter={v => `₹${v}`} />
            <Tooltip
              contentStyle={{ background: '#1a1a2e', border: '1px solid #2a2a4a', borderRadius: '8px' }}
              formatter={(v, name) => [formatFullCurrency(v), name]}
            />
            <Legend />
            <Bar dataKey="currentSpend" name="Current Spend" fill="rgba(99,102,241,0.6)" radius={[4, 4, 0, 0]} />
            <Bar dataKey="monthlyIncrease" name="Monthly Increase" fill="rgba(239,68,68,0.8)" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export function MonteCarloChart({ mcData }) {
  if (!mcData || !mcData.yearly) return null;

  const data = mcData.yearly.map(y => ({
    year: `Year ${y.year}`,
    expected: y.savings.mean,
    optimistic: y.savings.p90,
    pessimistic: y.savings.p10,
    negProb: y.savings.negativeProb,
  }));

  return (
    <div className="card animate-in">
      <div className="card-title"><span className="icon">🎲</span> Monte Carlo Projection ({mcData.summary?.simulations || 500} Simulations)</div>
      <div className="chart-container">
        <ResponsiveContainer width="100%" height={300}>
          <AreaChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#2a2a4a" />
            <XAxis dataKey="year" stroke="#6868a0" />
            <YAxis stroke="#6868a0" tickFormatter={v => `₹${(v/1000).toFixed(0)}K`} />
            <Tooltip
              contentStyle={{ background: '#1a1a2e', border: '1px solid #2a2a4a', borderRadius: '8px' }}
              formatter={(v) => [formatFullCurrency(v)]}
            />
            <Legend />
            <Area type="monotone" dataKey="optimistic" name="Best Case (P90)" stroke="#22c55e" fill="rgba(34,197,94,0.1)" strokeWidth={1} strokeDasharray="5 5" />
            <Area type="monotone" dataKey="expected" name="Expected" stroke="#6366f1" fill="rgba(99,102,241,0.2)" strokeWidth={2} />
            <Area type="monotone" dataKey="pessimistic" name="Worst Case (P10)" stroke="#ef4444" fill="rgba(239,68,68,0.1)" strokeWidth={1} strokeDasharray="5 5" />
          </AreaChart>
        </ResponsiveContainer>
      </div>
      {mcData.summary && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '12px', marginTop: '16px' }}>
          <div className="metric-card" style={{ padding: '12px' }}>
            <div className="metric-label">Negative Savings Risk</div>
            <div className="metric-value" style={{ fontSize: '1.4rem', color: mcData.summary.probabilityNegative > 30 ? 'var(--red)' : 'var(--green)' }}>
              {mcData.summary.probabilityNegative}%
            </div>
          </div>
          <div className="metric-card" style={{ padding: '12px' }}>
            <div className="metric-label">Expected Savings</div>
            <div className="metric-value neutral" style={{ fontSize: '1.4rem' }}>
              {formatFullCurrency(mcData.summary.expected)}
            </div>
          </div>
          <div className="metric-card" style={{ padding: '12px' }}>
            <div className="metric-label">Worst Case (P5)</div>
            <div className="metric-value negative" style={{ fontSize: '1.4rem' }}>
              {formatFullCurrency(mcData.summary.worstCase)}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}