import React, { useState } from 'react';
import { useLanguage } from '../contexts/LanguageContext';
import { BUDGET_2026_HIGHLIGHTS, BUDGET_ALLOCATIONS } from '../engine/policyData';

export default function BudgetHighlights() {
  const { t } = useLanguage();
  const [expanded, setExpanded] = useState(false);

  const formatCrore = (value) => {
    if (value >= 100000) {
      return `₹${(value / 100000).toFixed(2)} Lakh Cr`;
    }
    return `₹${value.toLocaleString('en-IN')} Cr`;
  };

  return (
    <div className="card animate-in budget-highlights">
      <div className="card-title">
        <span className="icon">🇮🇳</span>
        Union Budget 2026-27 Highlights
        <span className="budget-badge">Latest</span>
      </div>

      {/* Key Numbers */}
      <div className="budget-stats-grid">
        <div className="budget-stat">
          <div className="budget-stat-value">₹53.47L Cr</div>
          <div className="budget-stat-label">Total Expenditure</div>
        </div>
        <div className="budget-stat">
          <div className="budget-stat-value">₹12.2L Cr</div>
          <div className="budget-stat-label">Capital Expenditure</div>
          <div className="budget-stat-badge positive">Record High</div>
        </div>
        <div className="budget-stat">
          <div className="budget-stat-value">4.3%</div>
          <div className="budget-stat-label">Fiscal Deficit</div>
        </div>
        <div className="budget-stat">
          <div className="budget-stat-value">10%</div>
          <div className="budget-stat-label">GDP Growth (Nominal)</div>
        </div>
      </div>

      {/* Tax Changes */}
      <div className="budget-section">
        <h3>💰 Tax Changes (Income Tax Act, 2025)</h3>
        <div className="budget-changes-grid">
          <div className="budget-change positive">
            <span className="change-icon">✓</span>
            <div>
              <div className="change-title">Zero Tax up to ₹4 Lakh</div>
              <div className="change-desc">Increased from ₹3 Lakh</div>
            </div>
          </div>
          <div className="budget-change positive">
            <span className="change-icon">✓</span>
            <div>
              <div className="change-title">Standard Deduction ₹1 Lakh</div>
              <div className="change-desc">Increased from ₹75,000</div>
            </div>
          </div>
          <div className="budget-change positive">
            <span className="change-icon">✓</span>
            <div>
              <div className="change-title">Rebate up to ₹12 Lakh income</div>
              <div className="change-desc">Effectively zero tax up to ₹12L</div>
            </div>
          </div>
          <div className="budget-change neutral">
            <span className="change-icon">→</span>
            <div>
              <div className="change-title">MAT Reduced to 14%</div>
              <div className="change-desc">From 15% earlier</div>
            </div>
          </div>
          <div className="budget-change negative">
            <span className="change-icon">!</span>
            <div>
              <div className="change-title">STT Increased</div>
              <div className="change-desc">F&O: 0.05% Futures, 0.15% Options</div>
            </div>
          </div>
          <div className="budget-change positive">
            <span className="change-icon">✓</span>
            <div>
              <div className="change-title">TCS Reduced to 2%</div>
              <div className="change-desc">For education & medical remittances</div>
            </div>
          </div>
        </div>
      </div>

      {/* Major Allocations */}
      {expanded && (
        <>
          <div className="budget-section">
            <h3>🏗️ Major Allocations</h3>
            <div className="allocations-grid">
              {Object.entries(BUDGET_ALLOCATIONS).map(([key, alloc]) => (
                <div key={key} className="allocation-item">
                  <span className="allocation-icon">{alloc.icon}</span>
                  <div className="allocation-info">
                    <div className="allocation-name">{alloc.name}</div>
                    <div className="allocation-amount">{formatCrore(alloc.amount)}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Key Initiatives */}
          <div className="budget-section">
            <h3>🚀 Key Initiatives</h3>
            <div className="initiatives-grid">
              <div className="initiative">
                <span>🚄</span>
                <span>7 High-Speed Rail Corridors</span>
              </div>
              <div className="initiative">
                <span>🚢</span>
                <span>20 National Waterways</span>
              </div>
              <div className="initiative">
                <span>💻</span>
                <span>Semiconductor Mission 2.0 (₹76,000 Cr)</span>
              </div>
              <div className="initiative">
                <span>🌱</span>
                <span>Green Hydrogen Mission (₹19,700 Cr)</span>
              </div>
              <div className="initiative">
                <span>🌾</span>
                <span>Bharat-VISTAAR (AI for Farmers)</span>
              </div>
              <div className="initiative">
                <span>💊</span>
                <span>Biopharma SHAKTI (₹10,000 Cr)</span>
              </div>
              <div className="initiative">
                <span>🏠</span>
                <span>1 Cr Houses PM Surya Ghar Solar</span>
              </div>
              <div className="initiative">
                <span>📱</span>
                <span>Electronics Component Scheme (₹40,000 Cr)</span>
              </div>
            </div>
          </div>

          {/* Data Sources */}
          <div className="budget-sources">
            <div className="source-title">📎 Official Sources</div>
            <a href="https://www.indiabudget.gov.in" target="_blank" rel="noopener noreferrer">
              India Budget Portal
            </a>
            <a href="https://www.incometax.gov.in" target="_blank" rel="noopener noreferrer">
              Income Tax Department
            </a>
          </div>
        </>
      )}

      <button 
        className="expand-btn"
        onClick={() => setExpanded(!expanded)}
      >
        {expanded ? '▲ Show Less' : '▼ Show All Details'}
      </button>
    </div>
  );
}