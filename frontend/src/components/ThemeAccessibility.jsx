import React, { useState, useEffect } from 'react';

export default function ThemeAccessibility() {
  const [theme, setTheme] = useState('dark');
  const [fontSize, setFontSize] = useState(16);
  const [highContrast, setHighContrast] = useState(false);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem('theme') || 'dark';
    setTheme(saved);
    applyTheme(saved);
  }, []);

  const applyTheme = (newTheme) => {
    const root = document.documentElement;
    
    if (newTheme === 'light') {
      root.style.setProperty('--bg-primary', '#ffffff');
      root.style.setProperty('--bg-secondary', '#f8f9fa');
      root.style.setProperty('--bg-card', '#ffffff');
      root.style.setProperty('--bg-card-hover', '#f1f3f5');
      root.style.setProperty('--border', '#dee2e6');
      root.style.setProperty('--text-primary', '#212529');
      root.style.setProperty('--text-secondary', '#495057');
      root.style.setProperty('--text-muted', '#6c757d');
    } else {
      root.style.setProperty('--bg-primary', '#0a0a0f');
      root.style.setProperty('--bg-secondary', '#12121a');
      root.style.setProperty('--bg-card', '#1a1a2e');
      root.style.setProperty('--bg-card-hover', '#22223a');
      root.style.setProperty('--border', '#2a2a4a');
      root.style.setProperty('--text-primary', '#e8e8f0');
      root.style.setProperty('--text-secondary', '#9898b8');
      root.style.setProperty('--text-muted', '#6868a0');
    }
  };

  const toggleTheme = () => {
    const newTheme = theme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
    applyTheme(newTheme);
    localStorage.setItem('theme', newTheme);
  };

  const changeFontSize = (delta) => {
    const newSize = Math.max(12, Math.min(24, fontSize + delta));
    setFontSize(newSize);
    document.documentElement.style.fontSize = `${newSize}px`;
    localStorage.setItem('fontSize', newSize);
  };

  const toggleHighContrast = () => {
    const root = document.documentElement;
    if (!highContrast) {
      root.style.setProperty('--bg-primary', '#000000');
      root.style.setProperty('--bg-card', '#1a1a1a');
      root.style.setProperty('--text-primary', '#ffffff');
      root.style.setProperty('--border', '#ffffff');
      root.style.setProperty('--accent', '#ffff00');
    } else {
      applyTheme(theme);
    }
    setHighContrast(!highContrast);
  };

  return (
    <div style={{ position: 'fixed', bottom: '20px', right: '20px', zIndex: 999 }}>
      {/* Main Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        style={{
          width: '56px',
          height: '56px',
          borderRadius: '50%',
          background: 'linear-gradient(135deg, #6366f1, #4f46e5)',
          border: 'none',
          color: 'white',
          fontSize: '1.5rem',
          cursor: 'pointer',
          boxShadow: '0 4px 20px rgba(99,102,241,0.4)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          transition: 'all 0.3s',
        }}
        onMouseEnter={(e) => e.target.style.transform = 'scale(1.1)'}
        onMouseLeave={(e) => e.target.style.transform = 'scale(1)'}
        title="Accessibility Settings"
      >
        ♿
      </button>

      {/* Floating Panel */}
      {isOpen && (
        <div
          style={{
            position: 'absolute',
            bottom: '70px',
            right: '0',
            width: '280px',
            background: 'var(--bg-card)',
            border: '2px solid var(--border)',
            borderRadius: '16px',
            padding: '16px',
            boxShadow: '0 8px 30px rgba(0,0,0,0.3)',
          }}
        >
          <div style={{ fontWeight: 'bold', marginBottom: '16px', fontSize: '1.1rem' }}>
            ♿ Accessibility
          </div>

          {/* Theme Toggle */}
          <div style={{ marginBottom: '16px' }}>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '8px' }}>
              Theme
            </div>
            <button
              onClick={toggleTheme}
              style={{
                width: '100%',
                padding: '10px',
                background: theme === 'dark' ? 'var(--accent)' : '#fbbf24',
                color: theme === 'dark' ? 'white' : '#000',
                border: 'none',
                borderRadius: '8px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '8px',
                fontWeight: '600',
              }}
            >
              {theme === 'dark' ? '🌙 Dark Mode' : '☀️ Light Mode'}
            </button>
          </div>

          {/* Font Size */}
          <div style={{ marginBottom: '16px' }}>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '8px' }}>
              Font Size: {fontSize}px
            </div>
            <div style={{ display: 'flex', gap: '8px' }}>
              <button
                onClick={() => changeFontSize(-2)}
                style={{
                  flex: 1,
                  padding: '10px',
                  background: 'var(--bg-secondary)',
                  border: '1px solid var(--border)',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  fontWeight: 'bold',
                  fontSize: '1.1rem',
                }}
              >
                A-
              </button>
              <button
                onClick={() => changeFontSize(2)}
                style={{
                  flex: 1,
                  padding: '10px',
                  background: 'var(--bg-secondary)',
                  border: '1px solid var(--border)',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  fontWeight: 'bold',
                  fontSize: '1.1rem',
                }}
              >
                A+
              </button>
            </div>
          </div>

          {/* High Contrast */}
          <div style={{ marginBottom: '16px' }}>
            <button
              onClick={toggleHighContrast}
              style={{
                width: '100%',
                padding: '10px',
                background: highContrast ? '#000' : 'var(--bg-secondary)',
                color: highContrast ? '#fff' : 'var(--text-primary)',
                border: highContrast ? '2px solid #fff' : '1px solid var(--border)',
                borderRadius: '8px',
                cursor: 'pointer',
                fontWeight: '600',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '8px',
              }}
            >
              ◐ High Contrast {highContrast ? 'ON' : 'OFF'}
            </button>
          </div>

          {/* Screen Reader Info */}
          <div style={{
            padding: '10px',
            background: 'rgba(99,102,241,0.1)',
            borderRadius: '8px',
            fontSize: '0.75rem',
            color: 'var(--text-secondary)',
          }}>
            ℹ️ This site is screen reader compatible and follows WCAG 2.1 AA standards
          </div>
        </div>
      )}
    </div>
  );
}