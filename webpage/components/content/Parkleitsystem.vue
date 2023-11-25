<template>
    <div class="w-full">
        <button @click="cycleWeek(-1)">vorherige Woche</button>
        <button @click="cycleWeek(1)">nächste Woche</button>
        <Line :data="chartDataSet" :options="chartOptions" />
    </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { addWeeks, startOfISOWeek } from 'date-fns';
import parkleitsystem from 'assets/parkhouses/am bahnhof_data_20112023.json'
import { ref } from 'vue';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)


const jsonData = parkleitsystem

var chartLabels = ref([])
var chartData = ref([])

var chartDataSet = ref({
    labels: chartLabels.value, // Time (x-axis)
    datasets: [
        {
            label: 'Occupied Spaces',
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            data: chartData.value, // Occupied Spaces (y-axis)
        },
    ],
});
var chartOptions = ref({
    scales: {
        xAxes: [
            {
                type: 'time',
                time: {
                    unit: 'hour',
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Time',
                },
            },
        ],
        yAxes: [
            {
                scaleLabel: {
                    display: true,
                    labelString: 'Besetzte Parkplätze',
                },
            },
        ],
    },
})


const parseTimestamp = (timestamp) => {
    const day = parseInt(timestamp.substring(0, 2), 10);
    const month = parseInt(timestamp.substring(2, 4), 10) - 1; // Month is zero-based
    const year = parseInt(timestamp.substring(4, 8), 10);
    const hour = parseInt(timestamp.substring(9, 11), 10);
    const minute = parseInt(timestamp.substring(11), 10);

    return new Date(year, month, day, hour, minute);
};


let selectedWeek = ref(startOfISOWeek(new Date()));

const cycleWeek = (delta) => {
    selectedWeek.value = addWeeks(selectedWeek.value, delta);
    console.log("LAST WEEK?!", selectedWeek.value)
    updateChartData(jsonData, selectedWeek.value);
};


watch([chartLabels, chartData], ([newChartLabel, newChartData]) => {
    chartDataSet.value = {
    labels: newChartLabel, // Time (x-axis)
    datasets: [
        {
            label: 'Occupied Spaces',
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            data: newChartData, // Occupied Spaces (y-axis)
        },
    ],
    }
})



var cData = updateChartData(jsonData, selectedWeek.value)
console.log("CLABEL", cData)
chartLabels.value = cData.labels
chartData.value = cData.data
console.log("LABELS", chartLabels.value, "DATA", chartData.value)



</script>