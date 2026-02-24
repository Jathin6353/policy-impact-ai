import React from 'react';

const PRESETS = [
  { emoji: '👨‍🌾', name: 'Farmer Family', income: 250000, family: 5, occupation: 'farmer', emi: 0, state: 'uttar_pradesh' },
  { emoji: '🏭', name: 'Factory Worker', income: 400000, family: 4, occupation: 'daily_wage', emi: 3000, state: 'maharashtra' },
  { emoji: '👩‍💼', name: 'Salaried Middle Class', income: 900000, family: 4, occupation: 'salaried', emi: 18000, state: 'karnataka' },
  { emoji: '👨‍💻', name: 'IT Professional', income: 1800000, family: 3, occupation: 'salaried', emi: 35000, state: 'telangana' },
  { emoji: '🏪', name: 'Small Business Owner', income: 600000, family: 5, occupation: 'small_business', emi: 10000, state: 'gujarat' },
  { emoji: '👴', name: 'Retired Senior', income: 500000, family: 2, occupation: 'retired', emi: 0, state: 'kerala' },
];

export default function HouseholdProfiles({ onSelect }) {
  return (
    <div className="card">
      <div className="card-title"><span className="icon">👥</span> Quick Profiles — Select a Household</div>
      <div className="profile-cards">
        {PRESETS.map((p, i) => (
          <div key={i} className="profile-preset" onClick={() => onSelect(p)}>
            <div className="emoji">{p.emoji}</div>
            <div className="name">{p.name}</div>
            <div className="detail">₹{(p.income / 100000).toFixed(1)}L / Family: {p.family}</div>
            <div className="detail">{p.occupation}</div>
          </div>
        ))}
      </div>
    </div>
  );
}