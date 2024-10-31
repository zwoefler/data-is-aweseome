<template>
  <div class="w-full min-h-[370px]">
    <div class="w-full min-h-[350px]">
      <Line class="w-full h-full min-h-[350px]" :data="chartDataSet" :options="chartOptions" />
    </div>
    <div class="flex text-white space-x-2 ">
      <button class="flex w-max bg-blue-500 text-xs font-bold text-white p-2 rounded space-x-2" @click="downloadJSON">
        <svg class="w-4 h-4 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
        </svg>
        <span>
          JSON Daten herunterladen
        </span>
      </button>
      <button class="flex w-max bg-blue-500 text-xs font-bold text-white p-2 rounded space-x-2" @click="downloadCSV">
        <svg class="w-4 h-4 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
        </svg>
        <span>
          CSV / Excel herunterladen
        </span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs'
import dailyConsumption from "assets/daily_german_meat_consumption.json"
import dailyConsumptionCSV from "assets/daily_german_meat_consumption.csv?url"
import { ref } from 'vue'
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

const labels = ref(dailyConsumption.years)

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      },
      title: {
        display: true,
        text: 'Konsum, min. 1x täglich (%)',
        color: 'rgba(255, 255, 255, 1)',
      }
    },
    x: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      },
      title: {
        display: true,
        text: 'Jahre',
        color: 'rgba(255, 255, 255, 1)',
      }
    }
  },
  plugins: {
    legend: {
      position: 'top',
      labels: {
        color: 'rgba(255, 255, 255, 1)',
        boxWidth: 15,
        padding: 10,
        font: {
          size: 12
        },
      },
    }
  }
})


interface Dataset {
  label: string
  data: (number | null)[]
  fill: boolean
  borderColor: string
  tension: number
}

const chartDataSet = ref<{
  labels: string[],
  datasets: Dataset[]
}>({
  labels: labels.value,
  datasets: []
})

const colors = [
  'rgba(75, 192, 192, 1)',
  'rgba(255, 99, 132, 1)',
  'rgba(54, 162, 235, 1)',
  'rgba(255, 206, 86, 1)',
  'rgba(153, 102, 255, 1)',
  'rgba(255, 159, 64, 1)',
  'rgba(50, 205, 50, 1)',
  'rgba(0, 100, 0, 1)'
]

Object.keys(dailyConsumption.data).forEach((category, index) => {
  console.log("CATEGORY", category)
  chartDataSet.value.datasets.push({
    label: category,
    data: dailyConsumption.data[category],
    fill: false,
    borderColor: colors[index % colors.length],
    tension: 0.1
  })
})

const downloadJSON = () => {
  const dataStr = JSON.stringify(dailyConsumption, null, 2)
  const blob = new Blob([dataStr], { type: 'application/json' })
  const url = URL.createObjectURL(blob)

  const link = document.createElement('a')
  link.href = url
  link.download = 'daily_german_meat_consumption.json'
  link.click()

  URL.revokeObjectURL(url)
}

const downloadCSV = () => {
  const link = document.createElement('a')
  link.href = dailyConsumptionCSV
  link.download = 'daily_german_meat_consumption.csv'
  link.click()
}

</script>
