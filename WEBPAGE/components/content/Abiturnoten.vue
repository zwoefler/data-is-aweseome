<template>
  <div class="w-full">
    <div>
      <label for="parkhouse-select" class="text-white">Wähle ein Bundesland:</label>
      <select id="parkhouse-select" v-model="selectedOption"
        class="bg-blue-500 text-xs font-bold text-white p-2 rounded ml-2">
        <option v-for="option in selectionOptions" :key="option" :value="option">{{ option }}</option>
      </select>
    </div>
    <Linechart :chartOptions="chartOptions" :labels="labels" :data="data" :label="label"></Linechart>
  </div>
</template>

<script setup lang="ts">
import grades_data from 'assets/abitur_grades.json'

var label = 'Durchschnittliche Abiturnoten Deutschland 2006 - 2022'
var labels = ref([])
var data = ref([])
var chartOptions = ref({
  responsive: true,
  maintainAspectRatio: true,
  scales: {
    y: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      },
      min: 1.0,
      max: 3.0
    },
    x: {
      ticks: {
        color: 'rgba(255, 255, 255, 1)',
      },
      title: {
        display: true,
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
  }
})

var selectedOption = ref("Total")
var selectionOptions = ref(["Total"])
labels.value = grades_data["years"]
data.value = grades_data["average_grade"][selectedOption.value]

for (const key in grades_data[2006]["states"]) {
  selectionOptions.value.push(key)
}


watch(
  () => selectedOption.value,
  () => {
    changeSelection(selectedOption.value)
  }
)

function changeSelection(selection: string) {
  data.value = []
  data.value = grades_data["average_grade"][selection]
}



</script>