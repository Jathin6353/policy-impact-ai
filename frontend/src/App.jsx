import React, { useState, useCallback } from 'react';
import { useLanguage } from './contexts/LanguageContext';
import LanguageToggle from './components/LanguageToggle';
import UserInputForm from './components/UserInputForm';
import HouseholdProfiles from './components/HouseholdProfiles';
import ScenarioSelector from './components/ScenarioSelector';
import ImpactDashboard from './components/ImpactDashboard';
import StressGauge from './components/StressGauge';
import ExplainerPanel from './components/ExplainerPanel';
import PolicyComparator from './components/PolicyComparator';
import { ExpenseProjectionChart, InflationBreakdownChart, MonteCarloChart } from './components/ProjectionChart';
import { runFullSimulation } from './engine/projectionEngine';
import { projectExpenses } from './engine/inflationSimulator';
import { runMonteCarlo } from './engine/monteCarloEngine';
import { getIncomeBracket, EXPENDITURE_PATTERNS } from './engine/policyData';

export default function App() {
  const { t } = useLanguage();
  const [activeTab, setActiveTab] = useState('simulate');
  const [profile, setProfile] = useState({
    annualIncome: 900000,
    state: 'karnataka',
    familySize: 4,
    occupation: 'salaried',
    monthlyEmi: 18000,
    fuelSpend: 5000,
  });
  const [selectedScenario, setSelectedScenario] = useState('status_quo');
  const [scenarioB, setScenarioB] = useState('');
  const [simulation, setSimulation] = useState(null);
  const [simA, setSimA] = useState(null);
  const [simB, setSimB] = useState(null);
  const [projections, setProjections] = useState(null);
  const [mcData, setMcData] = useState(null);

  const handleProfilePreset = (preset) => {
    setProfile({
      annualIncome: preset.income,
      state: preset.state,
      familySize: preset.family,
      occupation: preset.occupation,
      monthlyEmi: preset.emi,
      fuelSpend: 3000,
    });
  };

  const handleSimulate = useCallback(() => {
    if (!profile.annualIncome || profile.annualIncome <= 0) return;

    const result = runFullSimulation(profile, selectedScenario);
    setSimulation(result);

    const inflRate = result.inflation.baseRate;
    const proj = projectExpenses(profile.annualIncome, profile.familySize, 3, inflRate);
    setProjections(proj);

    const bracket = getIncomeBracket(profile.annualIncome);
    const savingsRate = EXPENDITURE_PATTERNS[bracket]?.savings || 0.10;
    const mc = runMonteCarlo(profile.annualIncome, 1 - savingsRate, 3, 500);
    setMcData(mc);
  }, [profile, selectedScenario]);

  const handleCompare = useCallback(() => {
    if (!profile.annualIncome || !selectedScenario || !scenarioB) return;
    const resultA = runFullSimulation(profile, selectedScenario);
    const resultB = runFullSimulation(profile, scenarioB);
    setSimA(resultA);
    setSimB(resultB);
  }, [profile, selectedScenario, scenarioB]);

  return (
    <div className="app">
      <LanguageToggle />

      {/* Header */}
      <header className="header">
        <h1>🏛️ {t('appTitle')}</h1>
        <p className="subtitle">{t('appSubtitle')}</p>
        <span className="badge">{t('appBadge')}</span>
      </header>

      {/* Tabs */}
      <div className="tabs">
        <button className={`tab-btn ${activeTab === 'simulate' ? 'active' : ''}`} onClick={() => setActiveTab('simulate')}>
          {t('tabSimulate')}
        </button>
        <button className={`tab-btn ${activeTab === 'compare' ? 'active' : ''}`} onClick={() => setActiveTab('compare')}>
          {t('tabCompare')}
        </button>
      </div>

      {/* Simulate Tab */}
      {activeTab === 'simulate' && (
        <>
          <HouseholdProfiles onSelect={handleProfilePreset} />
          <UserInputForm profile={profile} setProfile={setProfile} onSubmit={handleSimulate} />
          <ScenarioSelector
            selected={selectedScenario}
            onSelect={setSelectedScenario}
            compareMode={false}
          />

          {simulation && (
            <>
              <ImpactDashboard simulation={simulation} />
              <StressGauge stress={simulation.stress} />
              <ExplainerPanel simulation={simulation} />

              <div className="dashboard-grid">
                {/* Tax Breakdown */}
                <div className="card animate-in">
                  <div className="card-title"><span className="icon">📝</span> {t('taxBreakdownTitle')}</div>
                  <table className="breakdown-table">
                    <tbody>
                      <tr><td>{t('grossIncome')}</td><td>₹{simulation.tax.grossIncome.toLocaleString('en-IN')}</td></tr>
                      <tr><td>{t('standardDeduction')}</td><td>₹{simulation.tax.standardDeduction.toLocaleString('en-IN')}</td></tr>
                      <tr><td>{t('taxableIncome')}</td><td>₹{simulation.tax.taxableIncome.toLocaleString('en-IN')}</td></tr>
                      <tr><td>{t('basicTax')}</td><td>₹{simulation.tax.basicTax.toLocaleString('en-IN')}</td></tr>
                      <tr><td>{t('rebate')}</td><td style={{ color: 'var(--green)' }}>-₹{simulation.tax.rebate.toLocaleString('en-IN')}</td></tr>
                      <tr><td>{t('cess')}</td><td>₹{simulation.tax.cess.toLocaleString('en-IN')}</td></tr>
                      <tr style={{ fontWeight: 700 }}><td>{t('totalTax')}</td><td style={{ color: 'var(--red)' }}>₹{simulation.tax.totalTax.toLocaleString('en-IN')}</td></tr>
                    </tbody>
                  </table>
                </div>

                {/* Subsidy Eligibility */}
                <div className="card animate-in">
                  <div className="card-title"><span className="icon">🏛️</span> {t('subsidyEligibilityTitle')}</div>
                  <table className="breakdown-table">
                    <thead>
                      <tr><th>{t('scheme')}</th><th>{t('status')}</th><th>{t('benefit')}</th></tr>
                    </thead>
                    <tbody>
                      {simulation.subsidies.subsidies.map((s, i) => (
                        <tr key={i}>
                          <td>{s.name}</td>
                          <td>
                            <span style={{
                              padding: '2px 8px',
                              borderRadius: '8px',
                              fontSize: '0.75rem',
                              background: s.eligible ? 'rgba(34,197,94,0.15)' : 'rgba(239,68,68,0.15)',
                              color: s.eligible ? 'var(--green)' : 'var(--red)',
                            }}>
                              {s.eligible ? `✓ ${t('eligible')}` : `✗ ${t('ineligible')}`}
                            </span>
                          </td>
                          <td>{s.eligible ? `₹${s.annualBenefit.toLocaleString('en-IN')}/yr` : '-'}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>

              <InflationBreakdownChart categories={simulation.inflation.categories} />
              {projections && <ExpenseProjectionChart data={projections} />}
              {mcData && <MonteCarloChart mcData={mcData} />}
            </>
          )}
        </>
      )}

      {/* Compare Tab */}
      {activeTab === 'compare' && (
        <>
          <HouseholdProfiles onSelect={handleProfilePreset} />
          <UserInputForm profile={profile} setProfile={setProfile} onSubmit={handleCompare} />
          <ScenarioSelector
            selected={selectedScenario}
            onSelect={setSelectedScenario}
            compareMode={true}
            selectedB={scenarioB}
            onSelectB={setScenarioB}
          />

          {selectedScenario && scenarioB && (
            <div style={{ textAlign: 'center', margin: '20px 0' }}>
              <button className="btn-primary" onClick={handleCompare}>
                {t('compareButton')}
              </button>
            </div>
          )}

          {simA && simB && (
            <>
              <PolicyComparator simA={simA} simB={simB} />
              <div className="dashboard-grid">
                <StressGauge stress={simA.stress} />
                <StressGauge stress={simB.stress} />
              </div>
            </>
          )}
        </>
      )}

      {/* Footer */}
      <footer style={{ textAlign: 'center', padding: '40px 20px', color: 'var(--text-muted)', fontSize: '0.8rem' }}>
        <p>🏛️ {t('footerTitle')}</p>
        <p>{t('footerData')}</p>
        <p>{t('footerSource')}</p>
      </footer>
    </div>
  );
}