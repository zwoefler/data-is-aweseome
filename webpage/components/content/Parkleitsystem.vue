<template>
    <div class="w-full">
        <button @click="cycleWeek(-1)">vorherige Woche</button>
        <button @click="cycleWeek(1)">nächste Woche</button>
        <Line :data="chartData" :options="chartOptions" />
    </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { addWeeks, subWeeks, startOfISOWeek } from 'date-fns';
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


import parkleitsystem from 'assets/parkhouses/am bahnhof_data_20112023.json'
import { ref } from 'vue';



const jsonData = parkleitsystem

var chartData = ref({
    labels: [], // Time (x-axis)
    datasets: [
        {
            label: 'Occupied Spaces',
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            data: [], // Occupied Spaces (y-axis)
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
    updateChartData();
};

const updateChartData = () => {
    const options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric' }

    chartData.value.labels = []
    chartData.value.datasets[0].data = []

    jsonData.sort((a, b) => parseTimestamp(a.timestamp) - parseTimestamp(b.timestamp));

    jsonData.forEach((item) => {
        const itemDate = parseTimestamp(item.timestamp)


        if (itemDate >= selectedWeek.value && itemDate < addWeeks(selectedWeek.value, 1)){
            chartData.value.labels.push(parseTimestamp(item.timestamp).toLocaleDateString("de-DE", options))
            chartData.value.datasets[0].data.push(item.occupied_spaces)
        }
    })
}

// jsonData.forEach((item) => {
//     chartData.value.labels.push(parseTimestamp(item.timestamp));
//     chartData.value.datasets[0].data.push(item.occupied_spaces);
// });

updateChartData()



</script>