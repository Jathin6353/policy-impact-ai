export function formatCurrency(amount) {
  if (Math.abs(amount) >= 10000000) return `₹${(amount / 10000000).toFixed(2)} Cr`;
  if (Math.abs(amount) >= 100000) return `₹${(amount / 100000).toFixed(2)} L`;
  if (Math.abs(amount) >= 1000) return `₹${(amount / 1000).toFixed(1)}K`;
  return `₹${Math.round(amount).toLocaleString('en-IN')}`;
}

export function formatFullCurrency(amount) {
  return `₹${Math.round(amount).toLocaleString('en-IN')}`;
}

export function formatPercent(value) {
  return `${value.toFixed(1)}%`;
}