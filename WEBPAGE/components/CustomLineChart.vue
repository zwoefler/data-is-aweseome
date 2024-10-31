<!-- src/components/CustomLineChart.vue -->
<template>
  <div class="w-full min-h-[370px]">
    <div class="w-full min-h-[350px]">
      <Line class="w-full h-full min-h-[350px]" :data="chartDataSet" :options="computedChartOptions" />
    </div>
    <div class="flex text-white space-x-2">
      <button class="flex w-max bg-blue-500 text-xs font-bold text-white p-2 rounded space-x-2"
        @click="downloadJSONFile">
        <svg class="w-4 h-4 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
        </svg>
        <span>JSON Daten herunterladen</span>
      </button>
      <button class="flex w-max bg-blue-500 text-xs font-bold text-white p-2 rounded space-x-2"
        @click="downloadCSVFile">
        <svg class="w-4 h-4 fill-white" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z" />
        </svg>
        <span>CSV / Excel herunterladen</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs'
import { downloadCSV, downloadJSON } from '~/utils/downloadUtils'
import { defineProps, computed } from 'vue'

type ChartData = {
  labels: string[];
  data: {
    [key: string]: number[];
  };
};

interface Dataset {
  label: string
  data: (number | null)[]
  fill: boolean
  borderColor: string
  tension: number
}

const props = defineProps<{
  chartData: ChartData,
  xAxisTitle: string,
  yAxisTitle: string,
  downloadOptions: { jsonFileName: string, csvUrl: string, csvFileName: string }
}>()

const labels = ref(props.chartData.labels)

const chartDataSet = ref<{
  labels: string[],
  datasets: Dataset[]
}>({
  labels: labels.value,
  datasets: []
})

const computedChartOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      },
      title: {
        display: true,
        text: props.yAxisTitle,
        color: 'rgba(255, 255, 255, 1)',
      }
    },
    x: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      },
      title: {
        display: true,
        text: props.xAxisTitle,
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
}))

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

Object.keys(props.chartData.data).forEach((category, index) => {
  chartDataSet.value.datasets.push({
    label: category,
    data: props.chartData.data[category],
    fill: false,
    borderColor: colors[index % colors.length],
    tension: 0.1
  })
})

const downloadJSONFile = () => downloadJSON(props.chartData, props.downloadOptions.jsonFileName)
const downloadCSVFile = () => downloadCSV(props.downloadOptions.csvUrl, props.downloadOptions.csvFileName)
</script>
