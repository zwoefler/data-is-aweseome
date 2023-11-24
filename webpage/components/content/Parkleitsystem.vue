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

// var chartLabels = []
// var chartData = []

var chartDataSet = ref({
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
const options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric' }

jsonData.sort((a, b) => parseTimestamp(a.timestamp) - parseTimestamp(b.timestamp));


const cycleWeek = (delta) => {
    selectedWeek.value = addWeeks(selectedWeek.value, delta);
    console.log("LAST WEEK?!", selectedWeek.value)
    updateChartData();
};

const updateChartData = () => {
    console.log("UPDATING DATA")
    chartDataSet.value.labels = []
    chartDataSet.value.datasets.data = []

    jsonData.forEach((item) => {
        const itemDate = parseTimestamp(item.timestamp)

        if (itemDate >= selectedWeek.value && itemDate < addWeeks(selectedWeek.value, 1)){
            chartDataSet.value.labels.push(parseTimestamp(item.timestamp).toLocaleDateString("de-DE", options))
            chartDataSet.value.datasets.data.push(item.occupied_spaces)
        }
    })
}


updateChartData()



</script>