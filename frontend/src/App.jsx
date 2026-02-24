import React, { useState, useCallback, useEffect } from 'react';
import { useLanguage } from './contexts/LanguageContext';

// Components
import LanguageToggle from './components/LanguageToggle';
import UserInputForm from './components/UserInputForm';
import HouseholdProfiles from './components/HouseholdProfiles';
import ScenarioSelector from './components/ScenarioSelector';
import ImpactDashboard from './components/ImpactDashboard';
import StressGauge from './components/StressGauge';
import ExplainerPanel from './components/ExplainerPanel';
import PolicyComparator from './components/PolicyComparator';
import AIRecommendations from './components/AIRecommendations';
import ComparisonSlider from './components/ComparisonSlider';
import SharePanel from './components/SharePanel';
import EducationalGuide from './components/EducationalGuide';
import ThemeAccessibility from './components/ThemeAccessibility';
import { ExpenseProjectionChart, InflationBreakdownChart, MonteCarloChart } from './components/ProjectionChart';

// Engine
import { runFullSimulation } from './engine/projectionEngine';
import { projectExpenses } from './engine/inflationSimulator';
import { runMonteCarlo } from './engine/monteCarloEngine';
import { getIncomeBracket, EXPENDITURE_PATTERNS } from './engine/policyData';

export default function App() {
  const { t } = useLanguage();
  
  // State
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
  const [isLoading, setIsLoading] = useState(false);
  const [showWelcome, setShowWelcome] = useState(true);

  // Check for shared link on load
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const shareData = params.get('share');
    if (shareData) {
      try {
        const decoded = JSON.parse(atob(shareData));
        setProfile({
          annualIncome: decoded.income || 900000,
          state: decoded.state || 'karnataka',
          familySize: decoded.family || 4,
          occupation: decoded.occupation || 'salaried',
          monthlyEmi: decoded.emi || 0,
          fuelSpend: decoded.fuel || 5000,
        });
        if (decoded.scenario) {
          setSelectedScenario(decoded.scenario);
        }
        setShowWelcome(false);
      } catch (e) {
        console.error('Invalid share link');
      }
    }
  }, []);

  // Profile preset handler
  const handleProfilePreset = (preset) => {
    setProfile({
      annualIncome: preset.income,
      state: preset.state,
      familySize: preset.family,
      occupation: preset.occupation,
      monthlyEmi: preset.emi,
      fuelSpend: 3000,
    });
    setSimulation(null);
    setShowWelcome(false);
  };

  // Main simulation handler
  const handleSimulate = useCallback(() => {
    if (!profile.annualIncome || profile.annualIncome <= 0) {
      alert('Please enter a valid annual income');
      return;
    }

    setIsLoading(true);
    setShowWelcome(false);

    // Simulate async processing for UX
    setTimeout(() => {
      try {
        const result = runFullSimulation(profile, selectedScenario);
        setSimulation(result);

        // Generate projections
        const inflRate = result.inflation.baseRate;
        const proj = projectExpenses(profile.annualIncome, profile.familySize, 3, inflRate);
        setProjections(proj);

        // Run Monte Carlo
        const bracket = getIncomeBracket(profile.annualIncome);
        const savingsRate = EXPENDITURE_PATTERNS[bracket]?.savings || 0.10;
        const mc = runMonteCarlo(profile.annualIncome, 1 - savingsRate, 3, 500);
        setMcData(mc);
      } catch (error) {
        console.error('Simulation error:', error);
        alert('Error running simulation. Please check your inputs.');
      }
      setIsLoading(false);
    }, 800);
  }, [profile, selectedScenario]);

  // Comparison handler
  const handleCompare = useCallback(() => {
    if (!profile.annualIncome || !selectedScenario || !scenarioB) {
      alert('Please select two different scenarios to compare');
      return;
    }

    setIsLoading(true);

    setTimeout(() => {
      try {
        const resultA = runFullSimulation(profile, selectedScenario);
        const resultB = runFullSimulation(profile, scenarioB);
        setSimA(resultA);
        setSimB(resultB);
      } catch (error) {
        console.error('Comparison error:', error);
      }
      setIsLoading(false);
    }, 800);
  }, [profile, selectedScenario, scenarioB]);

  // Reset handler
  const handleReset = () => {
    setSimulation(null);
    setSimA(null);
    setSimB(null);
    setProjections(null);
    setMcData(null);
    setSelectedScenario('status_quo');
    setScenarioB('');
  };

  return (
    <div className="app">
      {/* Language Toggle */}
      <LanguageToggle />

      {/* Header */}
      <header className="header">
        <div className="header-glow"></div>
        <h1>
          <span className="header-icon">🏛️</span> 
          {t('appTitle')}
        </h1>
        <p className="subtitle">{t('appSubtitle')}</p>
        <div className="badge-container">
          <span className="badge">{t('appBadge')}</span>
          <span className="badge tech">
            🔒 100% Client-Side Processing
          </span>
        </div>
        
        {/* Stats Bar */}
        <div className="stats-bar">
          <div className="stat-item">
            <span className="stat-value">500+</span>
            <span className="stat-label">Simulations</span>
          </div>
          <div className="stat-item">
            <span className="stat-value">10</span>
            <span className="stat-label">Scenarios</span>
          </div>
          <div className="stat-item">
            <span className="stat-value">7</span>
            <span className="stat-label">Risk Factors</span>
          </div>
          <div className="stat-item">
            <span className="stat-value">0</span>
            <span className="stat-label">Data Stored</span>
          </div>
        </div>
      </header>

      {/* Navigation Tabs */}
      <div className="tabs">
        <button 
          className={`tab-btn ${activeTab === 'simulate' ? 'active' : ''}`} 
          onClick={() => { setActiveTab('simulate'); handleReset(); }}
        >
          {t('tabSimulate')}
        </button>
        <button 
          className={`tab-btn ${activeTab === 'compare' ? 'active' : ''}`} 
          onClick={() => { setActiveTab('compare'); handleReset(); }}
        >
          {t('tabCompare')}
        </button>
        <button 
          className={`tab-btn ${activeTab === 'learn' ? 'active' : ''}`} 
          onClick={() => setActiveTab('learn')}
        >
          {t('tabEducation')}
        </button>
      </div>

      {/* Welcome Screen */}
      {showWelcome && activeTab !== 'learn' && (
        <div className="welcome-card card animate-in">
          <div className="welcome-content">
            <div className="welcome-icon">🎯</div>
            <h2>Welcome to Policy Impact AI</h2>
            <p>India's first AI-powered financial impact simulator</p>
            <div className="welcome-features">
              <div className="welcome-feature">
                <span>📊</span>
                <span>Personalized tax analysis</span>
              </div>
              <div className="welcome-feature">
                <span>📈</span>
                <span>Inflation impact projections</span>
              </div>
              <div className="welcome-feature">
                <span>🤖</span>
                <span>AI recommendations</span>
              </div>
              <div className="welcome-feature">
                <span>🔒</span>
                <span>100% private - no data stored</span>
              </div>
            </div>
            <p className="welcome-cta">Select a household profile below or enter your details to begin</p>
          </div>
        </div>
      )}

      {/* SIMULATE TAB */}
      {activeTab === 'simulate' && (
        <>
          <HouseholdProfiles onSelect={handleProfilePreset} />
          
          <UserInputForm 
            profile={profile} 
            setProfile={setProfile} 
            onSubmit={handleSimulate}
            isLoading={isLoading}
          />
          
          <ScenarioSelector
            selected={selectedScenario}
            onSelect={setSelectedScenario}
            compareMode={false}
          />

          {/* Loading State */}
          {isLoading && (
            <div className="loading-card card">
              <div className="loading-spinner"></div>
              <p>Running 500 Monte Carlo simulations...</p>
              <p className="loading-sub">Analyzing tax impact, inflation, subsidies...</p>
            </div>
          )}

          {/* Results */}
          {simulation && !isLoading && (
            <>
              {/* Summary Banner */}
              <div className="summary-banner animate-in">
                <div className="summary-item">
                  <span className="summary-label">Your Scenario</span>
                  <span className="summary-value">{simulation.scenario.name}</span>
                </div>
                <div className="summary-item">
                  <span className="summary-label">Income Bracket</span>
                  <span className="summary-value bracket-badge">
                    {simulation.bracket.replace(/_/g, ' ').toUpperCase()}
                  </span>
                </div>
                <div className="summary-item">
                  <span className="summary-label">Risk Level</span>
                  <span className="summary-value" style={{ color: simulation.stress.riskColor }}>
                    {simulation.stress.riskLevel}
                  </span>
                </div>
              </div>

              <ImpactDashboard simulation={simulation} />
              
              <AIRecommendations simulation={simulation} profile={profile} />
              
              <SharePanel simulation={simulation} profile={profile} />
              
              <StressGauge stress={simulation.stress} />
              
              <ComparisonSlider profile={profile} currentScenario={selectedScenario} />
              
              <ExplainerPanel simulation={simulation} />

              {/* Detailed Breakdown Section */}
              <div className="section-header animate-in">
                <h2>📊 Detailed Analysis</h2>
                <p>Deep dive into your financial breakdown</p>
              </div>

              <div className="dashboard-grid">
                {/* Tax Breakdown */}
                <div className="card animate-in">
                  <div className="card-title">
                    <span className="icon">📝</span> 
                    {t('taxBreakdownTitle')}
                  </div>
                  <table className="breakdown-table">
                    <tbody>
                      <tr>
                        <td>{t('grossIncome')}</td>
                        <td className="value">₹{simulation.tax.grossIncome.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr>
                        <td>{t('standardDeduction')}</td>
                        <td className="value deduction">-₹{simulation.tax.standardDeduction.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr>
                        <td>{t('taxableIncome')}</td>
                        <td className="value">₹{simulation.tax.taxableIncome.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr>
                        <td>{t('basicTax')}</td>
                        <td className="value">₹{simulation.tax.basicTax.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr>
                        <td>{t('rebate')}</td>
                        <td className="value positive">-₹{simulation.tax.rebate.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr>
                        <td>Surcharge</td>
                        <td className="value">₹{simulation.tax.surcharge.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr>
                        <td>{t('cess')}</td>
                        <td className="value">₹{simulation.tax.cess.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr className="total-row">
                        <td>{t('totalTax')}</td>
                        <td className="value negative">₹{simulation.tax.totalTax.toLocaleString('en-IN')}</td>
                      </tr>
                      <tr className="highlight-row">
                        <td>Effective Tax Rate</td>
                        <td className="value">{simulation.tax.effectiveRate}%</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                {/* Subsidy Eligibility */}
                <div className="card animate-in">
                  <div className="card-title">
                    <span className="icon">🏛️</span> 
                    {t('subsidyEligibilityTitle')}
                  </div>
                  <table className="breakdown-table">
                    <thead>
                      <tr>
                        <th>{t('scheme')}</th>
                        <th>{t('status')}</th>
                        <th>{t('benefit')}</th>
                      </tr>
                    </thead>
                    <tbody>
                      {simulation.subsidies.subsidies.map((s, i) => (
                        <tr key={i}>
                          <td>{s.name}</td>
                          <td>
                            <span className={`status-badge ${s.eligible ? 'eligible' : 'ineligible'}`}>
                              {s.eligible ? `✓ ${t('eligible')}` : `✗ ${t('ineligible')}`}
                            </span>
                          </td>
                          <td className={s.eligible ? 'positive' : ''}>
                            {s.eligible ? `₹${s.annualBenefit.toLocaleString('en-IN')}/yr` : '-'}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                    <tfoot>
                      <tr className="total-row">
                        <td colSpan="2">Total Annual Benefit</td>
                        <td className="positive">₹{simulation.subsidies.totalAnnual.toLocaleString('en-IN')}</td>
                      </tr>
                    </tfoot>
                  </table>
                </div>
              </div>

              {/* Charts Section */}
              <div className="section-header animate-in">
                <h2>📈 Visual Projections</h2>
                <p>See your financial future in charts</p>
              </div>

              <InflationBreakdownChart categories={simulation.inflation.categories} />
              
              {projections && <ExpenseProjectionChart data={projections} />}
              
              {mcData && <MonteCarloChart mcData={mcData} />}

              {/* Action Buttons */}
              <div className="action-buttons animate-in">
                <button onClick={handleReset} className="btn-secondary">
                  🔄 Run New Simulation
                </button>
                <button onClick={() => window.print()} className="btn-secondary">
                  🖨️ Print Report
                </button>
                <button onClick={() => setActiveTab('compare')} className="btn-primary">
                  ⚖️ Compare with Other Scenarios
                </button>
              </div>
            </>
          )}
        </>
      )}

      {/* COMPARE TAB */}
      {activeTab === 'compare' && (
        <>
          <HouseholdProfiles onSelect={handleProfilePreset} />
          
          <UserInputForm 
            profile={profile} 
            setProfile={setProfile} 
            onSubmit={handleCompare}
            isLoading={isLoading}
            buttonText={t('compareButton')}
          />
          
          <ScenarioSelector
            selected={selectedScenario}
            onSelect={setSelectedScenario}
            compareMode={true}
            selectedB={scenarioB}
            onSelectB={setScenarioB}
          />

          {selectedScenario && scenarioB && !simA && !simB && (
            <div style={{ textAlign: 'center', margin: '30px 0' }}>
              <button 
                className="btn-primary btn-large" 
                onClick={handleCompare}
                disabled={isLoading}
              >
                {isLoading ? '⏳ Comparing...' : '⚖️ Compare These Policies'}
              </button>
            </div>
          )}

          {/* Loading State */}
          {isLoading && (
            <div className="loading-card card">
              <div className="loading-spinner"></div>
              <p>Comparing policy scenarios...</p>
            </div>
          )}

          {/* Comparison Results */}
          {simA && simB && !isLoading && (
            <>
              <PolicyComparator simA={simA} simB={simB} />
              
              <div className="section-header animate-in">
                <h2>🎯 Stress Index Comparison</h2>
                <p>See how each scenario affects your financial stress</p>
              </div>
              
              <div className="dashboard-grid">
                <div className="comparison-stress-card">
                  <h3 style={{ color: 'var(--accent)', marginBottom: '10px' }}>
                    📘 {simA.scenario.name}
                  </h3>
                  <StressGauge stress={simA.stress} />
                </div>
                <div className="comparison-stress-card">
                  <h3 style={{ color: 'var(--green)', marginBottom: '10px' }}>
                    📗 {simB.scenario.name}
                  </h3>
                  <StressGauge stress={simB.stress} />
                </div>
              </div>

              <SharePanel simulation={simB} profile={profile} />

              <div className="action-buttons animate-in">
                <button onClick={handleReset} className="btn-secondary">
                  🔄 New Comparison
                </button>
                <button onClick={() => setActiveTab('simulate')} className="btn-primary">
                  🔍 Run Full Simulation
                </button>
              </div>
            </>
          )}
        </>
      )}

      {/* LEARN TAB */}
      {activeTab === 'learn' && (
        <>
          <div className="learn-header card animate-in">
            <div className="learn-icon">📚</div>
            <h2>Financial Education Center</h2>
            <p>Learn how policies affect your money</p>
          </div>
          
          <EducationalGuide />
          
          {/* Video Tutorials Placeholder */}
          <div className="card animate-in">
            <div className="card-title">
              <span className="icon">🎥</span>
              Quick Video Guides
            </div>
            <div className="video-grid">
              <div className="video-card">
                <div className="video-thumbnail">▶️</div>
                <div className="video-title">Understanding Income Tax Slabs</div>
                <div className="video-duration">5 min</div>
              </div>
              <div className="video-card">
                <div className="video-thumbnail">▶️</div>
                <div className="video-title">How Inflation Affects You</div>
                <div className="video-duration">4 min</div>
              </div>
              <div className="video-card">
                <div className="video-thumbnail">▶️</div>
                <div className="video-title">Government Subsidies Explained</div>
                <div className="video-duration">6 min</div>
              </div>
              <div className="video-card">
                <div className="video-thumbnail">▶️</div>
                <div className="video-title">Smart Tax Saving Strategies</div>
                <div className="video-duration">7 min</div>
              </div>
            </div>
          </div>

          {/* Quick Quiz */}
          <div className="card animate-in">
            <div className="card-title">
              <span className="icon">🧠</span>
              Test Your Knowledge
            </div>
            <div className="quiz-prompt">
              <p>What is the maximum deduction under Section 80C?</p>
              <div className="quiz-options">
                <button className="quiz-option">₹1,00,000</button>
                <button className="quiz-option correct">₹1,50,000</button>
                <button className="quiz-option">₹2,00,000</button>
                <button className="quiz-option">₹2,50,000</button>
              </div>
            </div>
          </div>

          <div className="action-buttons animate-in">
            <button onClick={() => setActiveTab('simulate')} className="btn-primary">
              🔍 Start Your Analysis
            </button>
          </div>
        </>
      )}

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <div className="footer-logo">🏛️</div>
          <p className="footer-title">{t('footerTitle')}</p>
          <p className="footer-text">{t('footerData')}</p>
          <p className="footer-source">{t('footerSource')}</p>
          
          <div className="footer-tech">
            <span className="tech-badge">React</span>
            <span className="tech-badge">Recharts</span>
            <span className="tech-badge">Monte Carlo</span>
            <span className="tech-badge">Client-Side AI</span>
          </div>
          
          <div className="footer-social">
            <span>Made with ❤️ for India</span>
          </div>
        </div>
      </footer>

      {/* Accessibility Controls */}
      <ThemeAccessibility />
    </div>
  );
}