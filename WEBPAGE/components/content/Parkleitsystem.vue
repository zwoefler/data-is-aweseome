<template>
  <div class="w-full">
    <p class="font-bold text-2xl">{{ parkhouse }}</p>
    <p>{{ shortDate(selectedWeekStart) }} - {{ shortDate(selectedWeekEnd) }}</p>
    <div class="my-4">
      <button @click="previousWeek" class="bg-blue-500 text-white px-4 py-2 rounded">Previous Week</button>
      <button @click="nextWeek" class="bg-blue-500 text-white px-4 py-2 rounded ml-2">Next Week</button>
    </div>
    <Line :data="chartDataSet" :options="chartOptions" />
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { startOfISOWeek, endOfISOWeek, subWeeks, addWeeks } from 'date-fns';
import parkleitsystem from 'assets/parkhouses/am bahnhof.json'
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

var chartOptions = ref({
  scales: {
    xAxes: [
      {
        type: 'time',
        time: {
          unit: 'day',
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


const jsonData = parkleitsystem
const parkhouse = ref(jsonData.name)

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



const shortDate = (date) => {
  var options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric' }
  return date.toLocaleDateString("de-DE", options)
}


let selectedWeekStart = ref(startOfISOWeek(new Date()));
let selectedWeekEnd = ref(endOfISOWeek(selectedWeekStart.value))

const previousWeek = () => {
  selectedWeekStart.value = subWeeks(selectedWeekStart.value, 1)
  selectedWeekEnd.value = endOfISOWeek(selectedWeekStart.value)
  updateChart()
}

const nextWeek = () => {
  selectedWeekStart.value = addWeeks(selectedWeekStart.value, 1)
  selectedWeekEnd.value = endOfISOWeek(selectedWeekStart.value)
  updateChart()
}

const updateChart = () => {
  var updatedChartData = extractChartData(jsonData.occupation_data, selectedWeekStart.value, selectedWeekEnd.value)
  chartDataSet.value = {
    labels: updatedChartData.labels, // Time (x-axis)
    datasets: [
      {
        label: 'Occupied Spaces',
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        data: updatedChartData.occupiedSpaces, // Occupied Spaces (y-axis)
      },
    ],
  }
}

const extractChartData = (data, weekStart, weekEnd) => {
  const labels = []
  const occupiedSpaces = []

  data.forEach(entry => {
    const entryDate = new Date(entry.timestamp * 1000)
    if (entryDate >= weekStart && entryDate <= weekEnd) {
      labels.push(shortDate(entryDate))
      occupiedSpaces.push(entry.occupied_spaces)
    }
  })

  return {
    labels,
    occupiedSpaces,
  }
}

updateChart()

</script>