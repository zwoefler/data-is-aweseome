<template>
  <div>
    <h1>Abiturnoten</h1>
    <div>
      <select v-model="selectedOption">
        <option v-for="option in selectionOptions" :key="option" :value="option">{{ option }}</option>
      </select>
    </div>
    <Linechart :chartData="chartData" :chartOptions="chartOptions"></Linechart>
  </div>
</template>

<script setup lang="ts">
import grades_data from 'assets/abitur_grades.json'

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

  var selectedOption = ref()
  var selectionOptions = ref(["Total"])
  for (const key in grades_data[2006]["states"]){
    selectionOptions.value.push(key)
  }


  for (const key in grades_data) {
    chartData["labels"].push(grades_data[key]["year"])
    chartData["datasets"][0]["data"].push(grades_data[key]["average_grade"])

  }


</script>