import React from 'react';
import { SCENARIOS } from '../engine/policyData';

export default function ScenarioSelector({ selected, onSelect, compareMode, selectedB, onSelectB }) {
  const scenarios = Object.values(SCENARIOS);

  return (
    <div className="card animate-in">
      <div className="card-title">
        <span className="icon">📜</span>
        {compareMode ? 'Select Two Scenarios to Compare' : 'Select Policy Scenario'}
      </div>
      {compareMode && (
        <p style={{ color: 'var(--text-muted)', marginBottom: '16px', fontSize: '0.85rem' }}>
          Click once for Scenario A (blue), click again on another for Scenario B (green)
        </p>
      )}
      <div className="scenario-grid">
        {scenarios.map(s => (
          <div
            key={s.id}
            className={`scenario-card ${selected === s.id ? 'selected' : ''} ${selectedB === s.id ? 'selected' : ''}`}
            onClick={() => {
              if (compareMode) {
                if (!selected || selected === s.id) onSelect(s.id);
                else if (!selectedB || selectedB === s.id) onSelectB(s.id);
                else { onSelect(selectedB); onSelectB(s.id); }
              } else {
                onSelect(s.id);
              }
            }}
            style={{
              borderColor: selected === s.id ? 'var(--accent)' : selectedB === s.id ? 'var(--green)' : undefined,
            }}
          >
            <div className="scenario-name">{s.name}</div>
            <div className="scenario-desc">{s.description}</div>
            <span className="scenario-category">{s.category}</span>
          </div>
        ))}
      </div>
    </div>
  );
}