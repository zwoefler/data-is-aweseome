import { addWeeks } from 'date-fns';


export const parseTimestamp = (timestamp) => {
    const day = parseInt(timestamp.substring(0, 2), 10);
    const month = parseInt(timestamp.substring(2, 4), 10) - 1; // Month is zero-based
    const year = parseInt(timestamp.substring(4, 8), 10);
    const hour = parseInt(timestamp.substring(9, 11), 10);
    const minute = parseInt(timestamp.substring(11), 10);

    return new Date(year, month, day, hour, minute);
};

export const updateChartData = (parkhouseData, selectedWeek) => {
    var chartData = {
        labels: [],
        data: []
    }
    const options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric' }

    parkhouseData.sort((a, b) => parseTimestamp(a.timestamp) - parseTimestamp(b.timestamp));

    parkhouseData.forEach((item) => {
        const itemDate = parseTimestamp(item.timestamp)

        if (itemDate >= selectedWeek && itemDate < addWeeks(selectedWeek, 1)){
            chartData.labels.push(parseTimestamp(item.timestamp).toLocaleDateString("de-DE", options))
            chartData.data.push(item.occupied_spaces)
        }
    })

    return chartData
}