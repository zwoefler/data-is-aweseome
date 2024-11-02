<template>
  <div class="w-full space-y-4">
    <div>
      <label for="parkhouse-select" class="text-white">Wähle ein Parkhaus:</label>
      <select id="parkhouse-select" v-model="selectedParkhouse"
        class="bg-blue-500 text-xs font-bold text-white p-2 rounded ml-2">
        <option v-for="parkhouse in parkhouses" :key="parkhouse.json.name" :value="parkhouse">{{ parkhouse.json.name }}
        </option>
      </select>
      <div class="font-bold text-3xl">{{ selectedParkhouse.json.name }}</div>
      <div>{{ shortDate(selectedWeekStart) }} - {{ shortDate(selectedWeekEnd) }}</div>
      <div class="space-x-2">
        <button @click="previousWeek" :disabled="isPreviousWeekDisabled"
          class="disabled:bg-gray-700 disabled:text-gray-300 bg-blue-500 text-xs text-white p-2 py-2 rounded">Letzte
          Woche</button>
        <button @click="nextWeek" :disabled="isNextWeekDisabled"
          class="disabled:bg-gray-700 disabled:text-gray-300 bg-blue-500 text-xs text-white p-2 rounded">Nächste
          Woche</button>
      </div>
    </div>
    <div class="w-full relative">
      <Line class="h-full" :data="chartDataSet" :options="chartOptions" />
      <p v-if="noData"
        class="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/3 inset-x-0 p-2 bg-orange-500 text-xs text-white font-bold text-center">
        KEINE DATEN FÜR DIESEN ZEITRAUM</p>
    </div>
    <button class="flex w-max bg-blue-500 text-xs font-bold text-white p-2 rounded space-x-2" @click="downloadCSVFile">
      <svg class="w-4 h-4 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
        <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
      </svg>
      <span>CSV / Excel herunterladen</span>
    </button>
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { startOfISOWeek, endOfISOWeek, subWeeks, addWeeks, isAfter, isBefore } from 'date-fns';
import { extractChartData } from "~/utils/chartUtils";


import ambahnhof from "assets/parkhouses/am bahnhof.json"
import amkino from "assets/parkhouses/am kino.json"
import dernpassage from "assets/parkhouses/dern-passage.json"
import karstadt from "assets/parkhouses/karstadt.json"
import liebigcenter from "assets/parkhouses/liebig-center.json"
import rathaus from "assets/parkhouses/rathaus.json"
import selterstor from "assets/parkhouses/selters tor.json"
import ambahnhofCSV from "assets/parkhouses/am bahnhof.csv?url"
import amkinoCSV from "assets/parkhouses/am kino.csv?url"
import dernpassageCSV from "assets/parkhouses/dern-passage.csv?url"
import karstadtCSV from "assets/parkhouses/karstadt.csv?url"
import liebigcenterCSV from "assets/parkhouses/liebig-center.csv?url"
import rathausCSV from "assets/parkhouses/rathaus.csv?url"
import selterstorCSV from "assets/parkhouses/selters tor.csv?url"

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
  { json: ambahnhof, csv: ambahnhofCSV },
  { json: amkino, csv: amkinoCSV },
  { json: dernpassage, csv: dernpassageCSV },
  { json: karstadt, csv: karstadtCSV },
  { json: liebigcenter, csv: liebigcenterCSV },
  { json: rathaus, csv: rathausCSV },
  { json: selterstor, csv: selterstorCSV },
];

var selectedParkhouse = ref(parkhouses[0]);
const initialWeekStart = computed(() => {
  const lastEntry = selectedParkhouse.value.json.occupation_data.at(-1)
  const latestTimestamp = lastEntry.timestamp * 1000
  const latestDate = new Date(latestTimestamp);

  return startOfISOWeek(latestDate);
});

let selectedWeekStart = ref(initialWeekStart.value)
let selectedWeekEnd = computed(() => {
  return endOfISOWeek(selectedWeekStart.value)
})

let updatedChartData = computed(() => {
  return extractChartData(
    selectedParkhouse.value.json.occupation_data,
    selectedWeekStart.value,
    selectedWeekEnd.value
  )
})

let noData = ref(true)

const chartDataSet = computed(() => {
  console.log("chartDataSet")
  console.log(selectedParkhouse.value.json)
  console.log(updatedChartData.value.occupiedSpaces)
  if (!updatedChartData.value || updatedChartData.value.occupiedSpaces.length < 1) {
    noData.value = true;
    return dummyChartData;
  } else {
    console.log("UPDATED", updatedChartData.value.shortLabels)
    noData.value = false;
    return {
      labels: updatedChartData.value.shortLabels, // Time (x-axis)
      datasets: [
        {
          label: 'Besetze Parkplätze',
          borderColor: 'rgba(255, 122, 0, 1)',
          data: updatedChartData.value.occupiedSpaces, // Occupied Spaces (y-axis)
        },
        {
          label: 'Verfügbare Plätze',
          borderColor: 'rgba(75, 192, 192, 1)',
          data: updatedChartData.value.maxSpaces, // Occupied Spaces (y-axis)
        },
      ],
    };
  }
});

var chartOptions = computed(() => ({
  scales: {
    x: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)'
      },
      title: {
        display: true,
        text: 'Wochentage',
        color: 'rgba(255, 255, 255, 1)',
      },
    },
    y: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      }
    }
  },
  plugins: {
    legend: {
      labels: {
        color: 'rgba(255, 255, 255, 1)'
      }
    },
    tooltip: {
      callbacks: {
        title: function (tooltipItems) {
          const index = tooltipItems[0].dataIndex;
          return updatedChartData.value.fullLabels[index];
        }
      }
    }
  }
}))


const dummyChartData = {
  labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], // Time (x-axis)
  datasets: [
    {
      label: '',
      borderColor: 'rgba(255, 122, 0, 0.2)',
      data: [0, 1, 5, 2, 4, 6, 6, 7, 3, 2, 0], // Occupied Spaces (y-axis)
    }
  ],
}

const shortDate = (date) => {
  var options = { weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric' }
  return date.toLocaleDateString("de-DE", options)
}

const isNextWeekDisabled = computed(() => {
  const lastEntry = selectedParkhouse.value.json.occupation_data.at(-1)
  const lastEntryTimestamp = lastEntry.timestamp * 1000
  const lastAvailableDate = new Date(lastEntryTimestamp);

  const nextWeekEnd = endOfISOWeek(addWeeks(selectedWeekStart.value, 1));
  return isAfter(nextWeekEnd, lastAvailableDate);
});

const isPreviousWeekDisabled = computed(() => {
  const firstEntry = selectedParkhouse.value.json.occupation_data.at(0)
  const firstEntryTimestamp = firstEntry.timestamp * 1000
  const firstAvailableDate = new Date(firstEntryTimestamp);

  const previousWeek = endOfISOWeek(subWeeks(selectedWeekStart.value, 1));
  return isBefore(previousWeek, firstAvailableDate);
});

const previousWeek = () => {
  selectedWeekStart.value = subWeeks(selectedWeekStart.value, 1)
}

const nextWeek = () => {
  selectedWeekStart.value = addWeeks(selectedWeekStart.value, 1)
}

const downloadCSVFile = () => downloadCSV(selectedParkhouse.value.csv, `${selectedParkhouse.value.json.name}.csv`)


</script>