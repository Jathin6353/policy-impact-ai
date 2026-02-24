import React from 'react';

export default function StressGauge({ stress }) {
  const { composite, riskLevel, riskColor, riskDesc, scores, weights } = stress;
  const circumference = 2 * Math.PI * 85;
  const dashOffset = circumference - (composite / 100) * circumference;

  return (
    <div className="card animate-in">
      <div className="card-title"><span className="icon">🎯</span> Financial Stress Index</div>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '30px', alignItems: 'center', justifyContent: 'center' }}>
        <div className="stress-gauge">
          <svg className="stress-ring" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="85" fill="none" stroke="var(--border)" strokeWidth="12" />
            <circle
              cx="100" cy="100" r="85"
              fill="none"
              stroke={riskColor}
              strokeWidth="12"
              strokeDasharray={circumference}
              strokeDashoffset={dashOffset}
              strokeLinecap="round"
              transform="rotate(-90 100 100)"
              style={{ transition: 'stroke-dashoffset 1s ease, stroke 0.5s' }}
            />
          </svg>
          <div className="stress-score-display">
            <div className="stress-score-number" style={{ color: riskColor }}>{composite}</div>
            <div className="stress-level-text" style={{ color: riskColor }}>{riskLevel}</div>
          </div>
        </div>
        <div style={{ flex: 1, minWidth: '250px' }}>
          <p style={{ color: 'var(--text-secondary)', marginBottom: '16px', fontSize: '0.95rem' }}>{riskDesc}</p>
          <table className="breakdown-table">
            <thead>
              <tr><th>Factor</th><th>Score</th><th>Weight</th></tr>
            </thead>
            <tbody>
              {Object.entries(scores).map(([key, val]) => (
                <tr key={key}>
                  <td style={{ textTransform: 'capitalize' }}>{key.replace(/_/g, ' ')}</td>
                  <td>
                    <span style={{ color: val < 30 ? 'var(--green)' : val < 60 ? 'var(--yellow)' : 'var(--red)' }}>
                      {val.toFixed(0)}
                    </span>
                  </td>
                  <td style={{ color: 'var(--text-muted)' }}>{((weights[key] || 0) * 100).toFixed(0)}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}