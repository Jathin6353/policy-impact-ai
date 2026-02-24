import React from 'react';
import { formatFullCurrency } from '../utils/formatters';

export default function PolicyComparator({ simA, simB }) {
  if (!simA || !simB) return null;

  const diffMonthly = simB.netDisposableMonthly - simA.netDisposableMonthly;
  const diffAnnual = simB.netDisposableAnnual - simA.netDisposableAnnual;
  const diffTax = simB.tax.totalTax - simA.tax.totalTax;
  const stressChange = simB.stress.composite - simA.stress.composite;

  return (
    <div className="card animate-in">
      <div className="card-title"><span className="icon">⚖️</span> Policy Comparison Result</div>

      <div className="comparison-container">
        {/* Scenario A */}
        <div>
          <h3 style={{ color: 'var(--accent)', marginBottom: '12px', textAlign: 'center' }}>📘 {simA.scenario.name}</h3>
          <div className="metric-card" style={{ marginBottom: '8px' }}>
            <div className="metric-label">Net Monthly</div>
            <div className="metric-value neutral" style={{ fontSize: '1.5rem' }}>{formatFullCurrency(simA.netDisposableMonthly)}</div>
          </div>
          <div className="metric-card" style={{ marginBottom: '8px' }}>
            <div className="metric-label">Annual Tax</div>
            <div className="metric-value negative" style={{ fontSize: '1.3rem' }}>{formatFullCurrency(simA.tax.totalTax)}</div>
          </div>
          <div className="metric-card">
            <div className="metric-label">Stress Index</div>
            <div className="metric-value" style={{ fontSize: '1.3rem', color: simA.stress.riskColor }}>{simA.stress.composite}</div>
            <div className="metric-sublabel">{simA.stress.riskLevel}</div>
          </div>
        </div>

        {/* VS */}
        <div className="vs-badge">VS</div>

        {/* Scenario B */}
        <div>
          <h3 style={{ color: 'var(--green)', marginBottom: '12px', textAlign: 'center' }}>📗 {simB.scenario.name}</h3>
          <div className="metric-card" style={{ marginBottom: '8px' }}>
            <div className="metric-label">Net Monthly</div>
            <div className="metric-value neutral" style={{ fontSize: '1.5rem' }}>{formatFullCurrency(simB.netDisposableMonthly)}</div>
          </div>
          <div className="metric-card" style={{ marginBottom: '8px' }}>
            <div className="metric-label">Annual Tax</div>
            <div className="metric-value negative" style={{ fontSize: '1.3rem' }}>{formatFullCurrency(simB.tax.totalTax)}</div>
          </div>
          <div className="metric-card">
            <div className="metric-label">Stress Index</div>
            <div className="metric-value" style={{ fontSize: '1.3rem', color: simB.stress.riskColor }}>{simB.stress.composite}</div>
            <div className="metric-sublabel">{simB.stress.riskLevel}</div>
          </div>
        </div>
      </div>

      {/* Summary */}
      <div style={{ marginTop: '24px', padding: '20px', background: 'rgba(99,102,241,0.05)', borderRadius: '12px', textAlign: 'center' }}>
        <div style={{ fontSize: '1.1rem', marginBottom: '12px', color: 'var(--text-secondary)' }}>
          Under <strong style={{ color: 'var(--green)' }}>{simB.scenario.name}</strong> compared to <strong style={{ color: 'var(--accent)' }}>{simA.scenario.name}</strong>:
        </div>
        <div style={{ display: 'flex', justifyContent: 'center', gap: '30px', flexWrap: 'wrap' }}>
          <div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Monthly Difference</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: diffMonthly >= 0 ? 'var(--green)' : 'var(--red)' }}>
              {diffMonthly >= 0 ? '+' : ''}{formatFullCurrency(diffMonthly)}
            </div>
          </div>
          <div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Tax Change</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: diffTax <= 0 ? 'var(--green)' : 'var(--red)' }}>
              {diffTax >= 0 ? '+' : ''}{formatFullCurrency(diffTax)}
            </div>
          </div>
          <div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Stress Change</div>
            <div style={{ fontSize: '1.8rem', fontWeight: 800, color: stressChange <= 0 ? 'var(--green)' : 'var(--red)' }}>
              {stressChange >= 0 ? '+' : ''}{stressChange.toFixed(1)}
            </div>
          </div>
        </div>
        <div style={{ marginTop: '16px', fontSize: '1rem' }}>
          <span style={{ fontWeight: 700, color: diffAnnual >= 0 ? 'var(--green)' : 'var(--red)' }}>
            You are {formatFullCurrency(Math.abs(diffAnnual))}/year {diffAnnual >= 0 ? 'BETTER' : 'WORSE'} off
          </span>
        </div>
      </div>
    </div>
  );
}