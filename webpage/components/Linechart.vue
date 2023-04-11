<template>
  <Line :data="chartData" :options="chartOptions" />
</template>


<script setup lang="ts">
import { Line } from 'vue-chartjs'
import grades_data from 'assets/abitur_grades.json'
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

    var chartData = {
      labels: [],
      datasets: [
        {
          label: 'Durchschnittliche Abiturnoten Deutschland 2006 - 2022',
          backgroundColor: '#f87979',
          data: []
        },
      ],
    }

    var chartOptions = {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: {
          min: 1.0,
          max: 4.0
        }
      }
    }

    for (const key in grades_data) {
      chartData["labels"].push(grades_data[key]["year"])
      chartData["datasets"][0]["data"].push(grades_data[key]["average_grade"])
    }
</script>