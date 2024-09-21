export const labelDateFull = (date) => {
  var options = {
    weekday: 'short',
    year: '2-digit',
    month: 'numeric',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
    timeZone: 'GMT'
  };
  return date.toLocaleString("de-DE", options).replace(',', '');
}

export const labelDateShort = (date) => {
  var options = {
    weekday: 'short',
    timeZone: 'GMT'
  };
  return date.toLocaleString("de-DE", options);
}

export const extractChartData = (data, weekStart, weekEnd) => {
  const fullLabels = []
  const shortLabels = []
  const occupiedSpaces = []
  const maxSpaces = []

  data.forEach(entry => {
    const entryDate = new Date(entry.timestamp * 1000)
    if (entryDate >= weekStart && entryDate <= weekEnd) {
      fullLabels.push(labelDateFull(entryDate))
      shortLabels.push(labelDateShort(entryDate))
      occupiedSpaces.push(entry.occupied_spaces)
      maxSpaces.push(entry.max_spaces)
    }
  })

  return {
    fullLabels,
    shortLabels,
    occupiedSpaces,
    maxSpaces,
  }
}