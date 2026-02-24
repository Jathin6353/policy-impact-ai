import React from 'react';
import { useLanguage } from '../contexts/LanguageContext';

export default function AIRecommendations({ simulation, profile }) {
  const { t } = useLanguage();
  
  if (!simulation) return null;

  const generateRecommendations = () => {
    const recommendations = [];
    const { tax, inflation, stress, subsidies, netDisposableMonthly } = simulation;

    // Tax Optimization
    if (tax.effectiveRate > 15 && tax.regime !== 'old') {
      recommendations.push({
        type: 'tax',
        priority: 'high',
        icon: '💰',
        title: 'Tax Optimization Opportunity',
        message: `You could save ₹${Math.round(tax.totalTax * 0.12).toLocaleString('en-IN')} by investing in 80C instruments (PPF, ELSS, NPS)`,
        action: 'Invest ₹1.5L in tax-saving instruments',
        savings: Math.round(tax.totalTax * 0.12),
      });
    }

    // Emergency Fund
    const emergencyFund = profile.annualIncome * 0.5;
    const currentSavings = netDisposableMonthly * 12;
    if (currentSavings < emergencyFund) {
      recommendations.push({
        type: 'savings',
        priority: 'critical',
        icon: '🚨',
        title: 'Emergency Fund Gap',
        message: `You need ₹${(emergencyFund / 100000).toFixed(1)}L emergency fund. Currently saving only ₹${(currentSavings / 100000).toFixed(1)}L/year`,
        action: `Increase monthly savings by ₹${Math.round((emergencyFund - currentSavings) / 12).toLocaleString('en-IN')}`,
        savings: emergencyFund - currentSavings,
      });
    }

    // Inflation Protection
    if (inflation.purchasingPowerLoss > 5) {
      recommendations.push({
        type: 'inflation',
        priority: 'high',
        icon: '📈',
        title: 'Inflation Protection Needed',
        message: `Inflation is eroding ${inflation.purchasingPowerLoss}% of your income. Consider equity investments for inflation-beating returns`,
        action: 'Allocate 30-40% to equity mutual funds',
        savings: Math.round(inflation.totalAnnualIncrease * 0.6),
      });
    }

    // Subsidy Awareness
    const eligibleSubsidies = subsidies.subsidies.filter(s => s.eligible && s.annualBenefit > 0);
    const missedSubsidies = subsidies.subsidies.filter(s => !s.eligible && s.scheme !== 'pm_kisan');
    
    if (eligibleSubsidies.length > 0) {
      recommendations.push({
        type: 'subsidy',
        priority: 'medium',
        icon: '🏛️',
        title: `You're Eligible for ${eligibleSubsidies.length} Government Schemes`,
        message: `Total potential benefit: ₹${subsidies.totalAnnual.toLocaleString('en-IN')}/year. Have you applied?`,
        action: 'Apply for all eligible subsidies',
        savings: subsidies.totalAnnual,
      });
    }

    // Debt Management
    if (profile.monthlyEmi > netDisposableMonthly * 0.4) {
      recommendations.push({
        type: 'debt',
        priority: 'critical',
        icon: '🏦',
        title: 'High Debt Burden Detected',
        message: `Your EMI is ${((profile.monthlyEmi / (profile.annualIncome / 12)) * 100).toFixed(0)}% of income. Consider debt restructuring`,
        action: 'Refinance high-interest loans or consolidate debt',
        savings: Math.round(profile.monthlyEmi * 12 * 0.15),
      });
    }

    // Health Insurance
    if (!subsidies.subsidies.find(s => s.scheme === 'ayushman_bharat' && s.eligible)) {
      recommendations.push({
        type: 'insurance',
        priority: 'medium',
        icon: '🏥',
        title: 'Health Insurance Gap',
        message: 'Medical emergencies can wipe out savings. Get family health cover of ₹10L minimum',
        action: 'Buy comprehensive health insurance (₹15K-25K/year premium)',
        savings: 500000, // Potential medical emergency cost
      });
    }

    // Investment Diversification
    if (stress.scores.income_volatility > 60) {
      recommendations.push({
        type: 'diversification',
        priority: 'medium',
        icon: '📊',
        title: 'Income Volatility Risk',
        message: 'Your income source is volatile. Build passive income streams',
        action: 'Invest in dividend-paying stocks or REITs',
        savings: Math.round(profile.annualIncome * 0.05),
      });
    }

    // Retirement Planning
    if (profile.occupation !== 'retired' && stress.scores.savings_adequacy > 50) {
      recommendations.push({
        type: 'retirement',
        priority: 'medium',
        icon: '🎯',
        title: 'Retirement Planning Required',
        message: 'Start investing 15% of income for retirement to maintain lifestyle',
        action: 'Open NPS or PPF account, invest ₹' + Math.round(profile.annualIncome * 0.15 / 12).toLocaleString('en-IN') + '/month',
        savings: Math.round(profile.annualIncome * 0.15),
      });
    }

    return recommendations.sort((a, b) => {
      const priority = { critical: 3, high: 2, medium: 1 };
      return priority[b.priority] - priority[a.priority];
    });
  };

  const recommendations = generateRecommendations();

  return (
    <div className="card animate-in" style={{ background: 'linear-gradient(135deg, rgba(99,102,241,0.05), rgba(168,85,247,0.05))' }}>
      <div className="card-title">
        <span className="icon">🤖</span> 
        AI-Powered Financial Recommendations
        <span style={{ 
          marginLeft: '10px', 
          padding: '4px 12px', 
          background: 'rgba(34,197,94,0.2)', 
          borderRadius: '12px', 
          fontSize: '0.75rem',
          color: 'var(--green)',
          fontWeight: 'bold'
        }}>
          {recommendations.length} Actions
        </span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {recommendations.map((rec, idx) => (
          <div
            key={idx}
            style={{
              background: 'var(--bg-card)',
              border: `2px solid ${
                rec.priority === 'critical' ? 'var(--red)' :
                rec.priority === 'high' ? 'var(--orange)' :
                'var(--accent)'
              }`,
              borderRadius: '12px',
              padding: '16px',
              position: 'relative',
              overflow: 'hidden',
            }}
          >
            {/* Priority Badge */}
            <div style={{
              position: 'absolute',
              top: '12px',
              right: '12px',
              padding: '4px 10px',
              background: rec.priority === 'critical' ? 'var(--red)' :
                          rec.priority === 'high' ? 'var(--orange)' :
                          'var(--accent)',
              color: 'white',
              borderRadius: '8px',
              fontSize: '0.7rem',
              fontWeight: 'bold',
              textTransform: 'uppercase',
            }}>
              {rec.priority}
            </div>

            <div style={{ display: 'flex', gap: '14px', marginBottom: '12px' }}>
              <div style={{ fontSize: '2rem' }}>{rec.icon}</div>
              <div style={{ flex: 1 }}>
                <div style={{ fontWeight: 'bold', fontSize: '1.05rem', marginBottom: '6px', color: 'var(--text-primary)' }}>
                  {rec.title}
                </div>
                <div style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: '1.5', marginBottom: '10px' }}>
                  {rec.message}
                </div>
                
                <div style={{
                  background: 'rgba(99,102,241,0.1)',
                  borderLeft: '3px solid var(--accent)',
                  padding: '10px 12px',
                  borderRadius: '6px',
                  marginBottom: '10px',
                }}>
                  <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '4px' }}>
                    ✅ RECOMMENDED ACTION
                  </div>
                  <div style={{ fontWeight: '600', color: 'var(--accent)' }}>
                    {rec.action}
                  </div>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                    💰 Potential Savings/Benefit:
                  </div>
                  <div style={{ 
                    fontSize: '1.2rem', 
                    fontWeight: 'bold', 
                    color: 'var(--green)',
                    background: 'rgba(34,197,94,0.1)',
                    padding: '4px 12px',
                    borderRadius: '8px',
                  }}>
                    ₹{(rec.savings / 1000).toFixed(0)}K
                  </div>
                </div>
              </div>
            </div>

            {/* Progress indicator for critical items */}
            {rec.priority === 'critical' && (
              <div style={{
                height: '4px',
                background: 'rgba(239,68,68,0.2)',
                borderRadius: '2px',
                overflow: 'hidden',
                marginTop: '8px',
              }}>
                <div style={{
                  width: '60%',
                  height: '100%',
                  background: 'var(--red)',
                  animation: 'pulse 2s infinite',
                }} />
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Total Potential Savings */}
      <div style={{
        marginTop: '20px',
        padding: '16px',
        background: 'linear-gradient(135deg, rgba(34,197,94,0.1), rgba(16,185,129,0.1))',
        borderRadius: '12px',
        border: '2px solid var(--green)',
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '4px' }}>
              💡 Total Potential Annual Savings/Benefits
            </div>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
              By implementing these {recommendations.length} recommendations
            </div>
          </div>
          <div style={{
            fontSize: '2rem',
            fontWeight: '900',
            color: 'var(--green)',
          }}>
            ₹{(recommendations.reduce((sum, r) => sum + r.savings, 0) / 100000).toFixed(1)}L
          </div>
        </div>
      </div>
    </div>
  );
}