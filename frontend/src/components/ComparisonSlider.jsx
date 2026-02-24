import React, { useState } from 'react';
import { runFullSimulation } from '../engine/projectionEngine';

export default function ComparisonSlider({ profile, currentScenario }) {
  const [customFuelHike, setCustomFuelHike] = useState(10);
  const [customInflation, setCustomInflation] = useState(5.5);
  const [customTaxRate, setCustomTaxRate] = useState(0.04);

  const runCustomSimulation = () => {
    const customScenario = {
      id: 'custom',
      name: 'Custom Scenario',
      changes: {
        fuel_hike: customFuelHike,
        inflation_override: customInflation,
        cess_rate: customTaxRate,
      },
    };
    
    // This would integrate with your main simulation
    return runFullSimulation(profile, 'status_quo');
  };

  return (
    <div className="card animate-in">
      <div className="card-title">
        <span className="icon">🎚️</span> 
        Interactive Policy Simulator
        <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)', marginLeft: '10px' }}>
          Adjust sliders to create custom scenarios
        </span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
        {/* Fuel Price Slider */}
        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
            <label style={{ fontWeight: '600', color: 'var(--text-secondary)' }}>
              ⛽ Fuel Price Change
            </label>
            <span style={{
              padding: '4px 12px',
              background: customFuelHike > 10 ? 'rgba(239,68,68,0.2)' : 'rgba(99,102,241,0.2)',
              color: customFuelHike > 10 ? 'var(--red)' : 'var(--accent)',
              borderRadius: '8px',
              fontWeight: 'bold',
              fontSize: '0.9rem',
            }}>
              {customFuelHike > 0 ? '+' : ''}{customFuelHike}%
            </span>
          </div>
          <input
            type="range"
            min="-20"
            max="50"
            value={customFuelHike}
            onChange={(e) => setCustomFuelHike(Number(e.target.value))}
            style={{
              width: '100%',
              height: '8px',
              borderRadius: '4px',
              background: `linear-gradient(to right, 
                var(--green) 0%, 
                var(--accent) ${((customFuelHike + 20) / 70) * 100}%, 
                var(--red) 100%)`,
              outline: 'none',
              cursor: 'pointer',
            }}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>
            <span>-20% (Subsidy)</span>
            <span>0% (Current)</span>
            <span>+50% (Crisis)</span>
          </div>
        </div>

        {/* Inflation Slider */}
        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
            <label style={{ fontWeight: '600', color: 'var(--text-secondary)' }}>
              📈 Annual Inflation Rate
            </label>
            <span style={{
              padding: '4px 12px',
              background: customInflation > 7 ? 'rgba(239,68,68,0.2)' : 'rgba(99,102,241,0.2)',
              color: customInflation > 7 ? 'var(--red)' : 'var(--accent)',
              borderRadius: '8px',
              fontWeight: 'bold',
              fontSize: '0.9rem',
            }}>
              {customInflation.toFixed(1)}%
            </span>
          </div>
          <input
            type="range"
            min="2"
            max="12"
            step="0.5"
            value={customInflation}
            onChange={(e) => setCustomInflation(Number(e.target.value))}
            style={{
              width: '100%',
              height: '8px',
              borderRadius: '4px',
              background: `linear-gradient(to right, 
                var(--green) 0%, 
                var(--accent) ${((customInflation - 2) / 10) * 100}%, 
                var(--red) 100%)`,
              outline: 'none',
              cursor: 'pointer',
            }}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>
            <span>2% (Low)</span>
            <span>5.5% (Current)</span>
            <span>12% (High)</span>
          </div>
        </div>

        {/* Tax Cess Slider */}
        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
            <label style={{ fontWeight: '600', color: 'var(--text-secondary)' }}>
              💰 Education & Health Cess
            </label>
            <span style={{
              padding: '4px 12px',
              background: 'rgba(99,102,241,0.2)',
              color: 'var(--accent)',
              borderRadius: '8px',
              fontWeight: 'bold',
              fontSize: '0.9rem',
            }}>
              {(customTaxRate * 100).toFixed(0)}%
            </span>
          </div>
          <input
            type="range"
            min="0"
            max="10"
            step="0.5"
            value={customTaxRate * 100}
            onChange={(e) => setCustomTaxRate(Number(e.target.value) / 100)}
            style={{
              width: '100%',
              height: '8px',
              borderRadius: '4px',
              background: `linear-gradient(to right, 
                var(--green) 0%, 
                var(--accent) ${(customTaxRate * 100 / 10) * 100}%, 
                var(--red) 100%)`,
              outline: 'none',
              cursor: 'pointer',
            }}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>
            <span>0% (None)</span>
            <span>4% (Current)</span>
            <span>10% (Max)</span>
          </div>
        </div>

        {/* Impact Preview */}
        <div style={{
          padding: '16px',
          background: 'rgba(99,102,241,0.05)',
          borderRadius: '12px',
          border: '1px solid var(--border)',
        }}>
          <div style={{ fontSize: '0.85rem', fontWeight: '600', marginBottom: '10px', color: 'var(--text-secondary)' }}>
            📊 Estimated Impact on Your Finances
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
            <div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Monthly Fuel Impact</div>
              <div style={{ fontSize: '1.1rem', fontWeight: 'bold', color: customFuelHike > 10 ? 'var(--red)' : 'var(--accent)' }}>
                +₹{Math.round((profile.annualIncome / 12) * 0.07 * (customFuelHike / 100))}
              </div>
            </div>
            <div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Annual Tax Impact</div>
              <div style={{ fontSize: '1.1rem', fontWeight: 'bold', color: 'var(--red)' }}>
                +₹{Math.round(profile.annualIncome * 0.20 * (customTaxRate - 0.04))}
              </div>
            </div>
          </div>
        </div>

        <button
          onClick={runCustomSimulation}
          className="btn-primary"
          style={{ width: '100%' }}
        >
          🎯 Apply Custom Scenario
        </button>
      </div>
    </div>
  );
}