import React from 'react';
import { useLanguage } from '../contexts/LanguageContext';

export default function LanguageToggle() {
  const { language, toggleLanguage } = useLanguage();

  return (
    <button
      onClick={toggleLanguage}
      style={{
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '10px 20px',
        background: 'linear-gradient(135deg, #6366f1, #4f46e5)',
        border: 'none',
        borderRadius: '25px',
        color: 'white',
        fontSize: '0.9rem',
        fontWeight: '600',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        gap: '8px',
        boxShadow: '0 4px 15px rgba(99, 102, 241, 0.3)',
        transition: 'all 0.3s',
        zIndex: 1000,
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'translateY(-2px)';
        e.target.style.boxShadow = '0 6px 20px rgba(99, 102, 241, 0.4)';
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'translateY(0)';
        e.target.style.boxShadow = '0 4px 15px rgba(99, 102, 241, 0.3)';
      }}
    >
      <span style={{ fontSize: '1.2rem' }}>🌐</span>
      <span>{language === 'en' ? 'हिंदी' : 'English'}</span>
    </button>
  );
}