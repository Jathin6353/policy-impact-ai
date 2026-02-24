import React from 'react';
import { formatFullCurrency, formatPercent } from '../utils/formatters';

export default function ImpactDashboard({ simulation }) {
  const { tax, inflation, fuelImpact, totalSubsidy, ubiBenefit, netDisposableAnnual, netDisposableMonthly, totalNegative, totalPositive, bracket, scenario } = simulation;

  const metrics = [
    {
      label: 'Annual Tax',
      value: formatFullCurrency(tax.totalTax),
      sub: `Effective Rate: ${tax.effectiveRate}%`,
      color: 'negative',
      icon: '💰',
    },
    {
      label: 'Inflation Erosion / Year',
      value: formatFullCurrency(inflation.totalAnnualIncrease),
      sub: `Purchasing power loss: ${inflation.purchasingPowerLoss}%`,
      color: 'negative',
      icon: '📈',
    },
    {
      label: 'Monthly Post-Tax Income',
      value: formatFullCurrency(tax.monthlyPostTax),
      sub: `From ₹${(tax.grossIncome / 12).toLocaleString('en-IN', { maximumFractionDigits: 0 })} gross`,
      color: 'neutral',
      icon: '💼',
    },
    {
      label: 'Subsidy Benefits / Year',
      value: formatFullCurrency(totalSubsidy + ubiBenefit),
      sub: `${totalSubsidy > 0 ? 'Eligible subsidies found' : 'No subsidies matched'}`,
      color: totalSubsidy > 0 ? 'positive' : 'warning',
      icon: '🏛️',
    },
    {
      label: 'Net Disposable / Month',
      value: formatFullCurrency(netDisposableMonthly),
      sub: `Annual: ${formatFullCurrency(netDisposableAnnual)}`,
      color: netDisposableMonthly > 0 ? 'positive' : 'negative',
      icon: '💵',
    },
    {
      label: 'Total Annual Drain',
      value: formatFullCurrency(totalNegative),
      sub: `Tax + Inflation + Fuel + GST + EMI`,
      color: 'negative',
      icon: '🔻',
    },
  ];

  if (fuelImpact.annualIncrease > 0) {
    metrics.splice(2, 0, {
      label: 'Fuel Impact / Year',
      value: formatFullCurrency(fuelImpact.annualIncrease),
      sub: `₹${fuelImpact.monthlyIncrease}/month extra`,
      color: 'warning',
      icon: '⛽',
    });
  }

  return (
    <div className="animate-in">
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <span style={{ padding: '6px 16px', background: 'rgba(99,102,241,0.15)', borderRadius: '20px', fontSize: '0.85rem', color: 'var(--accent)' }}>
          Scenario: {scenario.name} | Income Bracket: {bracket.replace(/_/g, ' ').toUpperCase()}
        </span>
      </div>
      <div className="dashboard-grid">
        {metrics.map((m, i) => (
          <div key={i} className="metric-card">
            <div className="metric-label">{m.icon} {m.label}</div>
            <div className={`metric-value ${m.color}`}>{m.value}</div>
            <div className="metric-sublabel">{m.sub}</div>
          </div>
        ))}
      </div>
    </div>
  );
}