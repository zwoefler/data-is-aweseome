<template>
    <div class="w-full">
        <p class="font-bold text-2xl">{{ parkhouse }}</p>
        <p>{{ shortDate(selectedWeekStart) }} - {{ shortDate(selectedWeekEnd) }}</p>
        <button @click="cycleWeek(-1)">vorherige Woche</button>
        <button @click="cycleWeek(1)">nächste Woche</button>
        <Line :data="chartDataSet" :options="chartOptions" />
    </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { addWeeks, startOfISOWeek, endOfISOWeek } from 'date-fns';
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

const parkhouse = ref(jsonData[0].name)

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


const shortDate = (date) => {
    var options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric' }
    return date.toLocaleDateString("de-DE", options)
}


let selectedWeekStart = ref(startOfISOWeek(new Date()));
let selectedWeekEnd = ref(endOfISOWeek(selectedWeekStart.value))
let oldWeekStart = ref("")

const cycleWeek = (delta) => {
    oldWeekStart.value = selectedWeekStart.value
    selectedWeekStart.value = addWeeks(selectedWeekStart.value, delta);
    selectedWeekEnd.value = endOfISOWeek(selectedWeekStart.value)
    updateChart();
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

const updateChart = () => {
    var updatedChartData = updateChartData(jsonData, selectedWeekStart.value)
    if (updatedChartData.data.length === 0){
        selectedWeekStart.value = oldWeekStart.value
        selectedWeekEnd.value = endOfISOWeek(selectedWeekStart.value)
    } else {
        chartLabels.value = updatedChartData.labels
        chartData.value = updatedChartData.data
    }
}

updateChart()



</script>