<template>
  <div class="w-full">
    <div>
      <select v-model="selectedOption">
        <option v-for="option in selectionOptions" :key="option" :value="option">{{ option }}</option>
      </select>
    </div>
    <Linechart :chartOptions="chartOptions" :labels="labels" :data="data" :label="label"></Linechart>
  </div>
</template>

<script setup lang="ts">
import parkleitsystem from 'assets/parkleitsystem.json'



</script>