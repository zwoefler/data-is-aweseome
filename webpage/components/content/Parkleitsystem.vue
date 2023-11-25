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


let selectedWeek = ref(startOfISOWeek(new Date()));

const cycleWeek = (delta) => {
    selectedWeek.value = addWeeks(selectedWeek.value, delta);
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
    var updatedChartData = updateChartData(jsonData, selectedWeek.value)
    chartLabels.value = updatedChartData.labels
    chartData.value = updatedChartData.data
}

updateChart()



</script>