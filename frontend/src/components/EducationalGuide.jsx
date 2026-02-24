import React, { useState } from 'react';

export default function EducationalGuide() {
  const [activeSection, setActiveSection] = useState('tax');

  const content = {
    tax: {
      title: '💰 Understanding Income Tax',
      icon: '💰',
      sections: [
        {
          q: 'What is Income Tax?',
          a: 'Income tax is a percentage of your earnings paid to the government. In India, it follows a slab system where higher income attracts higher tax rates.',
        },
        {
          q: 'Old vs New Tax Regime?',
          a: 'Old Regime: Lower rates but requires investments (80C, 80D). New Regime: Simplified rates, fewer deductions. Choose based on your investment capacity.',
        },
        {
          q: 'What is Standard Deduction?',
          a: 'A flat deduction from gross income before calculating tax. Currently ₹75,000 in new regime, ₹50,000 in old regime.',
        },
        {
          q: 'How to reduce tax legally?',
          a: 'Invest in: PPF (₹1.5L), NPS (₹50K extra), Health Insurance (₹25K-₹50K), Home Loan Interest (₹2L). Total potential saving: ₹46,800/year for ₹10L income.',
        },
      ],
    },
    inflation: {
      title: '📈 Inflation Explained',
      icon: '📈',
      sections: [
        {
          q: 'What is Inflation?',
          a: 'Inflation is the rate at which prices increase over time. If inflation is 6%, something that costs ₹100 today will cost ₹106 next year.',
        },
        {
          q: 'Why does it matter?',
          a: 'Your salary might increase 5% but if inflation is 7%, you can actually buy less. Your real income is NEGATIVE 2%.',
        },
        {
          q: 'How to protect against inflation?',
          a: 'Invest in assets that beat inflation: Equity (12-15% avg), Real Estate (8-10%), Gold (8%). Fixed deposits (6%) barely match inflation.',
        },
        {
          q: 'Category-wise inflation',
          a: 'Food: 8-10% | Education: 10-12% | Healthcare: 12-15% | Housing: 5-7%. Budget accordingly.',
        },
      ],
    },
    subsidies: {
      title: '🏛️ Government Subsidies',
      icon: '🏛️',
      sections: [
        {
          q: 'What are Government Subsidies?',
          a: 'Financial assistance from government to reduce your expenses. Available for farmers, low-income families, students, and businesses.',
        },
        {
          q: 'Major Schemes',
          a: 'PM-KISAN: ₹6K/year for farmers | PMUY: LPG subsidy | PMJAY: ₹5L health cover | Scholarships: ₹20K-₹50K/year',
        },
        {
          q: 'How to apply?',
          a: 'Visit respective ministry websites, submit Aadhaar, income certificate, and required documents. Process usually takes 30-60 days.',
        },
        {
          q: 'Common eligibility',
          a: 'Most schemes target income below ₹3-8L/year. Check specific scheme guidelines on official government portals.',
        },
      ],
    },
    savings: {
      title: '💎 Smart Savings Strategy',
      icon: '💎',
      sections: [
        {
          q: 'How much should I save?',
          a: 'Thumb rule: 50% needs, 30% wants, 20% savings. For ₹50K income: Save ₹10K. For ₹1L: Save ₹20K-₹30K.',
        },
        {
          q: 'Emergency Fund First',
          a: 'Save 6 months of expenses BEFORE investing. For ₹40K monthly expenses, build ₹2.4L emergency fund in liquid assets.',
        },
        {
          q: 'Where to invest?',
          a: 'Age <30: 70% equity, 30% debt | Age 30-45: 60% equity, 40% debt | Age >45: 40% equity, 60% debt',
        },
        {
          q: 'Compounding Magic',
          a: '₹10K/month at 12% for 20 years = ₹99L (invested ₹24L). Start early, stay consistent.',
        },
      ],
    },
  };

  return (
    <div className="card animate-in" style={{ background: 'linear-gradient(135deg, rgba(99,102,241,0.05), rgba(234,179,8,0.05))' }}>
      <div className="card-title">
        <span className="icon">📚</span> 
        Financial Education Center
        <span style={{
          marginLeft: '10px',
          padding: '4px 10px',
          background: 'rgba(234,179,8,0.2)',
          borderRadius: '10px',
          fontSize: '0.7rem',
          color: 'var(--yellow)',
          fontWeight: 'bold',
        }}>
          Learn the Basics
        </span>
      </div>

      {/* Section Tabs */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(120px, 1fr))',
        gap: '8px',
        marginBottom: '20px',
      }}>
        {Object.entries(content).map(([key, section]) => (
          <button
            key={key}
            onClick={() => setActiveSection(key)}
            style={{
              padding: '12px',
              background: activeSection === key ? 'var(--accent)' : 'var(--bg-secondary)',
              color: activeSection === key ? 'white' : 'var(--text-secondary)',
              border: activeSection === key ? 'none' : '1px solid var(--border)',
              borderRadius: '10px',
              cursor: 'pointer',
              fontSize: '0.85rem',
              fontWeight: activeSection === key ? '700' : '500',
              transition: 'all 0.3s',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: '4px',
            }}
          >
            <span style={{ fontSize: '1.5rem' }}>{section.icon}</span>
            <span>{section.title.replace(/[💰📈🏛️💎]\s/, '')}</span>
          </button>
        ))}
      </div>

      {/* Content */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {content[activeSection].sections.map((item, idx) => (
          <details
            key={idx}
            style={{
              background: 'var(--bg-secondary)',
              borderRadius: '10px',
              padding: '14px',
              border: '1px solid var(--border)',
              cursor: 'pointer',
            }}
          >
            <summary style={{
              fontWeight: '600',
              color: 'var(--text-primary)',
              listStyle: 'none',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}>
              <span>❓ {item.q}</span>
              <span style={{ fontSize: '0.8rem', color: 'var(--accent)' }}>▼</span>
            </summary>
            <div style={{
              marginTop: '12px',
              paddingTop: '12px',
              borderTop: '1px solid var(--border)',
              color: 'var(--text-secondary)',
              lineHeight: '1.6',
              fontSize: '0.9rem',
            }}>
              {item.a}
            </div>
          </details>
        ))}
      </div>

      {/* Quick Tips */}
      <div style={{
        marginTop: '20px',
        padding: '16px',
        background: 'linear-gradient(135deg, rgba(234,179,8,0.1), rgba(251,191,36,0.1))',
        borderRadius: '12px',
        border: '2px solid var(--yellow)',
      }}>
        <div style={{ fontWeight: 'bold', marginBottom: '8px', color: 'var(--yellow)' }}>
          💡 Quick Action Tip
        </div>
        <div style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
          {activeSection === 'tax' && 'File ITR before July 31st to avoid penalty. Use new regime if your 80C investments are less than ₹1L.'}
          {activeSection === 'inflation' && 'Review your portfolio every 6 months. Rebalance if equity exceeds target allocation by 10%.'}
          {activeSection === 'subsidies' && 'Check eligibility on DBT Bharat portal. Link Aadhaar to bank account for direct benefit transfer.'}
          {activeSection === 'savings' && 'Automate savings on salary day. Set up SIP for mutual funds, recurring deposit for emergency fund.'}
        </div>
      </div>
    </div>
  );
}