<template>
  <Line :data="props.chartData" :options="props.chartOptions" />
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
  chartOptions: {
    type: Object,
    required: true
  },
  chartData: {
    type: Object,
    required: true
  }
})

</script>