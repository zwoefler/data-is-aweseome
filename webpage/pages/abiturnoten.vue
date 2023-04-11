<template>
  <div>
    <h1>Abiturnoten</h1>
    <div>
      <select v-model="selectedOption">
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
      min: 1.0,
      max: 4.0
    }
  }
})

var selectedOption = ref("Total")
var selectionOptions = ref(["Total"])
for (const key in grades_data[2006]["states"]){
  selectionOptions.value.push(key)
}


  watch(
  () => selectedOption.value,
  () => {
    changeSelection(selectedOption.value)
  }
)

function changeSelection(selection: string){
  labels.value = []
  data.value = []
  for (const key in grades_data) {
      if (selection == "Total"){
        labels.value.push(grades_data[key]["year"])
        data.value.push(grades_data[key]["average_grade"])
      } else {
        labels.value.push(grades_data[key]["year"])
        data.value.push(grades_data[key]["states"][selection]["Notenmittel"])
      }
    }
}

for (const key in grades_data) {
  labels.value.push(grades_data[key]["year"])
  data.value.push(grades_data[key]["average_grade"])
}

</script>