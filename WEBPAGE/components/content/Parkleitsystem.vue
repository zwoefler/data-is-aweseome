<template>
  <div class="w-full p-4 bg-gray-900">
    <div>
      <p class="font-bold text-2xl">{{ parkhouse }}</p>
      <p>{{ shortDate(selectedWeekStart) }} - {{ shortDate(selectedWeekEnd) }}</p>
      <div class="space-x-2">
        <button @click="previousWeek" :disabled="isPreviousWeekDisabled"
          class="disabled:bg-gray-700 disabled:text-gray-300 bg-blue-500 text-xs text-white p-2 py-2 rounded">Letzte
          Woche</button>
        <button @click="nextWeek" :disabled="isNextWeekDisabled"
          class="disabled:bg-gray-700 disabled:text-gray-300 bg-blue-500 text-xs text-white p-2 rounded">Nächste
          Woche</button>
      </div>
    </div>
    <div class="h-80 w-full">
      <Line class="h-full" :data="chartDataSet" />
    </div>
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { startOfISOWeek, endOfISOWeek, subWeeks, addWeeks, isAfter, isBefore } from 'date-fns';
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
    {
      label: 'Max Available Spaces',
      data: [], // Occupied Spaces (y-axis)
    },
  ],
});



const shortDate = (date) => {
  var options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric' }
  return date.toLocaleDateString("de-DE", options)
}

const labelDate = (date) => {
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


let selectedWeekStart = ref(startOfISOWeek(new Date()));
let selectedWeekEnd = ref(endOfISOWeek(selectedWeekStart.value))

const isNextWeekDisabled = computed(() => {
  const timestamps = jsonData.occupation_data.map(entry => entry.timestamp * 1000);
  const lastAvailableDate = new Date(Math.max(...timestamps));

  const nextWeekEnd = endOfISOWeek(addWeeks(selectedWeekStart.value, 1));
  return isAfter(nextWeekEnd, lastAvailableDate);
});

const isPreviousWeekDisabled = computed(() => {
  const timestamps = jsonData.occupation_data.map(entry => entry.timestamp * 1000);
  const firstAvailableDate = new Date(Math.min(...timestamps));

  const previousWeek = endOfISOWeek(subWeeks(selectedWeekStart.value, 1));
  return isBefore(previousWeek, firstAvailableDate);
});

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
        label: 'Besetze Parkplätze',
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        data: updatedChartData.occupiedSpaces, // Occupied Spaces (y-axis)
      },
      {
        label: 'Verfügbare Plätze',
        data: updatedChartData.maxSpaces, // Occupied Spaces (y-axis)
      },
    ],
  }
}

const extractChartData = (data, weekStart, weekEnd) => {
  const labels = []
  const occupiedSpaces = []
  const maxSpaces = []

  data.forEach(entry => {
    const entryDate = new Date(entry.timestamp * 1000)
    if (entryDate >= weekStart && entryDate <= weekEnd) {
      labels.push(labelDate(entryDate))
      occupiedSpaces.push(entry.occupied_spaces)
      maxSpaces.push(entry.max_spaces)
    }
  })

  return {
    labels,
    occupiedSpaces,
    maxSpaces,
  }
}

updateChart()

</script>