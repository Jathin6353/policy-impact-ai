import React from 'react';
import { formatFullCurrency } from '../utils/formatters';

export default function ExplainerPanel({ simulation }) {
  const { tax, inflation, fuelImpact, foodGstImpact, subsidies, totalSubsidy, ubiBenefit, emiChange, stress } = simulation;

  const insights = [];

  // Tax
  insights.push({
    icon: '💰', category: 'tax',
    text: `Your effective tax rate is ${tax.effectiveRate}%. You pay ${formatFullCurrency(tax.monthlyTax)}/month in taxes.`,
    severity: tax.effectiveRate < 10 ? 'low' : tax.effectiveRate < 20 ? 'medium' : 'high',
  });

  // Inflation
  insights.push({
    icon: '📈', category: 'inflation',
    text: `Inflation erodes ${formatFullCurrency(inflation.totalMonthlyIncrease)}/month from your purchasing power (${inflation.purchasingPowerLoss}% annual loss).`,
    severity: inflation.purchasingPowerLoss < 3 ? 'low' : inflation.purchasingPowerLoss < 6 ? 'medium' : 'high',
  });

  // Fuel
  if (fuelImpact.annualIncrease > 0) {
    insights.push({
      icon: '⛽', category: 'fuel',
      text: `Fuel price changes cost an additional ${formatFullCurrency(fuelImpact.annualIncrease)}/year (${formatFullCurrency(fuelImpact.monthlyIncrease)}/month).`,
      severity: fuelImpact.annualIncrease < 5000 ? 'low' : fuelImpact.annualIncrease < 15000 ? 'medium' : 'high',
    });
  }

  // Food GST
  if (foodGstImpact.annualBurden > 0) {
    insights.push({
      icon: '🍽️', category: 'gst',
      text: `Food GST adds ${formatFullCurrency(foodGstImpact.annualBurden)}/year to your food expenses.`,
      severity: 'medium',
    });
  }

  // Subsidies
  if (totalSubsidy > 0) {
    insights.push({
      icon: '🏛️', category: 'subsidy',
      text: `You are eligible for ${formatFullCurrency(totalSubsidy)}/year in government subsidies.`,
      severity: 'positive',
    });
  }

  // UBI
  if (ubiBenefit > 0) {
    insights.push({
      icon: '💵', category: 'ubi',
      text: `Universal Basic Income provides ${formatFullCurrency(ubiBenefit)}/year additional income.`,
      severity: 'positive',
    });
  }

  // EMI
  if (emiChange > 0) {
    insights.push({
      icon: '🏦', category: 'emi',
      text: `Interest rate hike increases your EMI by ${formatFullCurrency(emiChange)}/month (${formatFullCurrency(emiChange * 12)}/year).`,
      severity: 'high',
    });
  }

  // Stress
  insights.push({
    icon: '🎯', category: 'stress',
    text: `Financial Stress Index: ${stress.composite}/100 (${stress.riskLevel}). ${stress.riskDesc}`,
    severity: stress.composite < 40 ? 'low' : stress.composite < 70 ? 'medium' : 'high',
  });

  // Disposable
  insights.push({
    icon: '💵', category: 'disposable',
    text: `After all impacts, your effective monthly disposable income is ${formatFullCurrency(simulation.netDisposableMonthly)}.`,
    severity: simulation.netDisposableMonthly > simulation.tax.grossIncome / 12 * 0.3 ? 'low' : 'high',
  });

  return (
    <div className="card animate-in">
      <div className="card-title"><span className="icon">💡</span> Plain English Insights</div>
      {insights.map((ins, i) => (
        <div key={i} className={`insight-card severity-${ins.severity}`}>
          <span className="insight-icon">{ins.icon}</span>
          <span className="insight-text">{ins.text}</span>
        </div>
      ))}
    </div>
  );
}