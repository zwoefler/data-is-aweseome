<template>
  <div class="w-full p-4 bg-gray-900">
    <div class="mb-4">
      <label for="parkhouse-select" class="text-white">Select Parkhouse:</label>
      <select id="parkhouse-select" v-model="selectedParkhouse" @change="updateChart" class="ml-2 p-2 rounded bg-white">
        <option v-for="parkhouse in parkhouses" :key="parkhouse.name" :value="parkhouse">{{ parkhouse.name }}
        </option>
      </select>
    </div>
    <div>
      <p class="font-bold text-2xl">{{ selectedParkhouse.name }}</p>
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
      <p v-if="!chartDataSet" class="bg-orange-500 text-black font-xl">LOADING DATA</p>
      <p v-if="noData">NO DATA AVAILABLE FOR SELECTED TIMEFRAME</p>
      <Line v-else class="h-full" :data="chartDataSet" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { startOfISOWeek, endOfISOWeek, subWeeks, addWeeks, isAfter, isBefore } from 'date-fns';

import ambahnhof from "assets/parkhouses/am bahnhof.json"
import amkino from "assets/parkhouses/am kino.json"
import dernpassage from "assets/parkhouses/dern-passage.json"
import karstadt from "assets/parkhouses/karstadt.json"
import liebigcenter from "assets/parkhouses/liebig-center.json"
import rathaus from "assets/parkhouses/rathaus.json"
import selterstor from "assets/parkhouses/selters tor.json"

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

const parkhouses = [
  ambahnhof,
  amkino,
  dernpassage,
  karstadt,
  liebigcenter,
  rathaus,
  selterstor,
]

const extractChartData = (data, weekStart, weekEnd) => {
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

//
// VARIABLES
//
const selectedParkhouse = ref(parkhouses[0]);
var chartDataSet = ref(null);
var chartOptions = ref(null)
let selectedWeekStart = ref(startOfISOWeek(new Date()));
let selectedWeekEnd = ref(endOfISOWeek(selectedWeekStart.value))
let updatedChartData = ref(null)
let noData = ref(true)

const shortDate = (date) => {
  var options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric' }
  return date.toLocaleDateString("de-DE", options)
}

const labelDateFull = (date) => {
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

const labelDateShort = (date) => {
  var options = {
    weekday: 'short',
    timeZone: 'GMT'
  };
  return date.toLocaleString("de-DE", options);
}

const isNextWeekDisabled = computed(() => {
  const timestamps = selectedParkhouse.value.occupation_data.map(entry => entry.timestamp * 1000);
  const lastAvailableDate = new Date(Math.max(...timestamps));

  const nextWeekEnd = endOfISOWeek(addWeeks(selectedWeekStart.value, 1));
  return isAfter(nextWeekEnd, lastAvailableDate);
});

const isPreviousWeekDisabled = computed(() => {
  const timestamps = selectedParkhouse.value.occupation_data.map(entry => entry.timestamp * 1000);
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
  console.log("Selected:", selectedParkhouse.value.name)
  console.log(selectedParkhouse.value)
  updatedChartData.value = extractChartData(selectedParkhouse.value.occupation_data, selectedWeekStart.value, selectedWeekEnd.value)
  if (updatedChartData.value.occupiedSpaces.length < 1) {
    noData.value = true
  } else {
    noData.value = false
  }
  chartDataSet.value = {
    labels: updatedChartData.value.shortLabels, // Time (x-axis)
    datasets: [
      {
        label: 'Besetze Parkplätze',
        borderColor: 'rgba(255, 122, 0, 1)',
        backgroundColor: 'rgba(255, 122, 0, 0.2)',
        data: updatedChartData.value.occupiedSpaces, // Occupied Spaces (y-axis)
      },
      {
        label: 'Verfügbare Plätze',
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        data: updatedChartData.value.maxSpaces, // Occupied Spaces (y-axis)
      },
    ],
  }
  chartOptions.value = {
    scales: {
      x: {
        title: {
          display: true,
          text: 'Weekdays'
        }
      }
    },
    plugins: {
      tooltip: {
        callbacks: {
          title: function (tooltipItems) {
            const index = tooltipItems[0].dataIndex;
            return updatedChartData.value.fullLabels[index];
          }
        }
      }
    }
  }
}

updateChart()

</script>