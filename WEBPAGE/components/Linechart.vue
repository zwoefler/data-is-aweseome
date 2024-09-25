<template>
  <Line :data="chartData" :options="props.chartOptions" />
</template>


<script setup lang="ts">
import { Line } from 'vue-chartjs'
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


const props = defineProps({
  labels: {
    type: Array,
    required: true
  },
  data: {
    type: Array,
    required: true
  },
  label: {
    type: String,
    required: true
  },
  chartOptions: {
    type: Object,
    required: true
  },
})

var chartData = ref({
  labels: props.labels,
  datasets: [
    {
      label: 'Durchschnittliche Abiturnoten Deutschland 2006 - 2022',
      backgroundColor: '#f87979',
      data: props.data,
      fill: false,
      borderColor: 'rgba(105,105,105,0.5)'
    },
  ],
})

watch(
  () => props.data,
  () => {
    console.log(props.data)
    chartData.value = {
      labels: props.labels,
      datasets: [
        {
          label: 'Durchschnittliche Abiturnoten Deutschland 2006 - 2022',
          backgroundColor: '#f87979',
          data: props.data,
          fill: false,
          borderColor: '#f87979'
        },
      ],
    }
  }
)


</script>