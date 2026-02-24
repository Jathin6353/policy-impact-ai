import React, { useState } from 'react';
import { formatFullCurrency } from '../utils/formatters';

export default function SharePanel({ simulation, profile }) {
  const [shareUrl, setShareUrl] = useState('');
  const [copied, setCopied] = useState(false);

  if (!simulation) return null;

  const generateShareableLink = () => {
    const data = btoa(JSON.stringify({
      income: profile.annualIncome,
      state: profile.state,
      family: profile.familySize,
      occupation: profile.occupation,
      scenario: simulation.scenario.id,
      timestamp: Date.now(),
    }));
    
    const url = `${window.location.origin}?share=${data}`;
    setShareUrl(url);
    return url;
  };

  const copyToClipboard = () => {
    const url = generateShareableLink();
    navigator.clipboard.writeText(url);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const shareToWhatsApp = () => {
    const url = generateShareableLink();
    const message = `
🏛️ *Policy Impact Analysis*

📊 Income: ${formatFullCurrency(profile.annualIncome)}
💰 Tax: ${formatFullCurrency(simulation.tax.totalTax)}
📈 Inflation Impact: ${formatFullCurrency(simulation.inflation.totalAnnualIncrease)}
🎯 Stress Score: ${simulation.stress.composite}/100

🔗 View full analysis: ${url}
    `.trim();

    window.open(`https://wa.me/?text=${encodeURIComponent(message)}`, '_blank');
  };

  const shareToTwitter = () => {
    const url = generateShareableLink();
    const message = `I just analyzed how government policies affect my finances using Policy Impact AI. My financial stress score: ${simulation.stress.composite}/100. Check yours!`;
    window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(message)}&url=${encodeURIComponent(url)}`, '_blank');
  };

  const downloadAsImage = async () => {
    // Simple implementation - in production use html2canvas
    alert('Downloading dashboard image... (Feature uses html2canvas in production)');
  };

  const exportToJSON = () => {
    const data = {
      profile,
      simulation: {
        tax: simulation.tax,
        inflation: simulation.inflation,
        stress: simulation.stress,
        netDisposable: simulation.netDisposableAnnual,
      },
      generatedAt: new Date().toISOString(),
    };

    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `policy-impact-${Date.now()}.json`;
    a.click();
  };

  return (
    <div className="card animate-in" style={{ background: 'linear-gradient(135deg, rgba(99,102,241,0.05), rgba(16,185,129,0.05))' }}>
      <div className="card-title">
        <span className="icon">📤</span> 
        Share & Export Your Analysis
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '12px' }}>
        {/* WhatsApp Share */}
        <button
          onClick={shareToWhatsApp}
          style={{
            padding: '14px',
            background: '#25D366',
            color: 'white',
            border: 'none',
            borderRadius: '12px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '8px',
            fontSize: '0.95rem',
            fontWeight: '600',
            transition: 'transform 0.2s',
          }}
          onMouseEnter={(e) => e.target.style.transform = 'translateY(-2px)'}
          onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}
        >
          <span style={{ fontSize: '1.3rem' }}>📱</span>
          WhatsApp
        </button>

        {/* Twitter Share */}
        <button
          onClick={shareToTwitter}
          style={{
            padding: '14px',
            background: '#1DA1F2',
            color: 'white',
            border: 'none',
            borderRadius: '12px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '8px',
            fontSize: '0.95rem',
            fontWeight: '600',
            transition: 'transform 0.2s',
          }}
          onMouseEnter={(e) => e.target.style.transform = 'translateY(-2px)'}
          onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}
        >
          <span style={{ fontSize: '1.3rem' }}>🐦</span>
          Twitter
        </button>

        {/* Copy Link */}
        <button
          onClick={copyToClipboard}
          style={{
            padding: '14px',
            background: copied ? 'var(--green)' : 'var(--accent)',
            color: 'white',
            border: 'none',
            borderRadius: '12px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '8px',
            fontSize: '0.95rem',
            fontWeight: '600',
            transition: 'all 0.2s',
          }}
          onMouseEnter={(e) => !copied && (e.target.style.transform = 'translateY(-2px)')}
          onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}
        >
          <span style={{ fontSize: '1.3rem' }}>{copied ? '✅' : '🔗'}</span>
          {copied ? 'Copied!' : 'Copy Link'}
        </button>

        {/* Download Image */}
        <button
          onClick={downloadAsImage}
          style={{
            padding: '14px',
            background: 'var(--orange)',
            color: 'white',
            border: 'none',
            borderRadius: '12px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '8px',
            fontSize: '0.95rem',
            fontWeight: '600',
            transition: 'transform 0.2s',
          }}
          onMouseEnter={(e) => e.target.style.transform = 'translateY(-2px)'}
          onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}
        >
          <span style={{ fontSize: '1.3rem' }}>🖼️</span>
          Image
        </button>

        {/* Export JSON */}
        <button
          onClick={exportToJSON}
          style={{
            padding: '14px',
            background: 'var(--cyan)',
            color: 'white',
            border: 'none',
            borderRadius: '12px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '8px',
            fontSize: '0.95rem',
            fontWeight: '600',
            transition: 'transform 0.2s',
          }}
          onMouseEnter={(e) => e.target.style.transform = 'translateY(-2px)'}
          onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}
        >
          <span style={{ fontSize: '1.3rem' }}>📄</span>
          JSON
        </button>

        {/* Print/PDF */}
        <button
          onClick={() => window.print()}
          style={{
            padding: '14px',
            background: 'var(--purple)',
            color: 'white',
            border: 'none',
            borderRadius: '12px',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '8px',
            fontSize: '0.95rem',
            fontWeight: '600',
            transition: 'transform 0.2s',
          }}
          onMouseEnter={(e) => e.target.style.transform = 'translateY(-2px)'}
          onMouseLeave={(e) => e.target.style.transform = 'translateY(0)'}
        >
          <span style={{ fontSize: '1.3rem' }}>🖨️</span>
          Print/PDF
        </button>
      </div>

      {/* Shareable Link Preview */}
      {shareUrl && (
        <div style={{
          marginTop: '16px',
          padding: '12px',
          background: 'var(--bg-secondary)',
          borderRadius: '8px',
          border: '1px solid var(--border)',
        }}>
          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '6px' }}>
            📎 Shareable Link
          </div>
          <div style={{
            fontSize: '0.85rem',
            color: 'var(--accent)',
            wordBreak: 'break-all',
            fontFamily: 'monospace',
          }}>
            {shareUrl}
          </div>
        </div>
      )}

      {/* Social Preview */}
      <div style={{
        marginTop: '16px',
        padding: '16px',
        background: 'var(--bg-secondary)',
        borderRadius: '12px',
        border: '1px solid var(--border)',
      }}>
        <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: '10px' }}>
          📱 Social Media Preview
        </div>
        <div style={{
          padding: '12px',
          background: 'var(--bg-card)',
          borderRadius: '8px',
          borderLeft: '3px solid var(--accent)',
        }}>
          <div style={{ fontWeight: 'bold', marginBottom: '6px' }}>
            🏛️ My Policy Impact Analysis
          </div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', lineHeight: '1.5' }}>
            📊 Income: {formatFullCurrency(profile.annualIncome)}<br />
            💰 Tax: {formatFullCurrency(simulation.tax.totalTax)}<br />
            🎯 Stress: {simulation.stress.composite}/100 ({simulation.stress.riskLevel})
          </div>
        </div>
      </div>
    </div>
  );
}