<template>
  <div class="w-full min-h-[350px]">
    <Line class="w-full h-full min-h-[350px]" :data="chartDataSet" :options="chartOptions" />
  </div>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs'
import vw_monthly_deliveries from "assets/vw_deliveries_filtered.json"
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

const labels = ref(vw_monthly_deliveries.months)

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
        text: 'Auslieferungen an Kunden',
        color: 'rgba(255, 255, 255, 1)',
      }
    },
    x: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      },
      title: {
        display: true,
        text: 'Monate',
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

Object.keys(vw_monthly_deliveries.data).forEach((category, index) => {
  chartDataSet.value.datasets.push({
    label: category,
    data: vw_monthly_deliveries.data[category],
    fill: false,
    borderColor: colors[index % colors.length],
    tension: 0.1
  })
})

</script>
