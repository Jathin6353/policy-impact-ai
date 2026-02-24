import React, { useState } from 'react';

const OCCUPATIONS = [
  'Salaried', 'Government', 'Self Employed', 'Small Business',
  'Entrepreneur', 'Farmer', 'Agriculture', 'Daily Wage',
  'Freelance', 'Retired', 'Student'
];

const STATES = [
  'Delhi', 'Maharashtra', 'Karnataka', 'Tamil Nadu', 'Telangana',
  'Uttar Pradesh', 'West Bengal', 'Rajasthan', 'Kerala',
  'Gujarat', 'Madhya Pradesh', 'Andhra Pradesh', 'Bihar',
  'Punjab', 'Haryana'
];

export default function UserInputForm({ profile, setProfile, onSubmit }) {
  const handleChange = (field, value) => {
    setProfile(prev => ({ ...prev, [field]: value }));
  };

  return (
    <div className="card animate-in">
      <div className="card-title"><span className="icon">📋</span> Your Financial Profile</div>
      <div className="form-grid">
        <div className="form-group">
          <label>Annual Income (₹)</label>
          <input
            type="number"
            placeholder="e.g. 800000"
            value={profile.annualIncome || ''}
            onChange={e => handleChange('annualIncome', Number(e.target.value))}
          />
        </div>
        <div className="form-group">
          <label>State</label>
          <select value={profile.state || ''} onChange={e => handleChange('state', e.target.value)}>
            <option value="">Select State</option>
            {STATES.map(s => <option key={s} value={s.toLowerCase().replace(/ /g, '_')}>{s}</option>)}
          </select>
        </div>
        <div className="form-group">
          <label>Family Size</label>
          <input
            type="number"
            min="1" max="15"
            value={profile.familySize || ''}
            onChange={e => handleChange('familySize', Number(e.target.value))}
          />
        </div>
        <div className="form-group">
          <label>Occupation</label>
          <select value={profile.occupation || ''} onChange={e => handleChange('occupation', e.target.value)}>
            <option value="">Select Occupation</option>
            {OCCUPATIONS.map(o => <option key={o} value={o.toLowerCase().replace(/ /g, '_')}>{o}</option>)}
          </select>
        </div>
        <div className="form-group">
          <label>Monthly EMI (₹)</label>
          <input
            type="number"
            placeholder="0"
            value={profile.monthlyEmi || ''}
            onChange={e => handleChange('monthlyEmi', Number(e.target.value))}
          />
        </div>
        <div className="form-group">
          <label>Monthly Fuel Spend (₹)</label>
          <input
            type="number"
            placeholder="e.g. 5000"
            value={profile.fuelSpend || ''}
            onChange={e => handleChange('fuelSpend', Number(e.target.value))}
          />
        </div>
      </div>
      <div style={{ textAlign: 'center', marginTop: '24px' }}>
        <button className="btn-primary" onClick={onSubmit}>
          🔍 Simulate Impact
        </button>
      </div>
    </div>
  );
}