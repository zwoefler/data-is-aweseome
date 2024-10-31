<template>
  <CustomLineChart :chartData="dailyConsumption" xAxisTitle="Jahre" yAxisTitle="Konsum, min. 1x täglich (%)"
    :downloadOptions="{
      jsonFileName: 'daily_german_meat_consumption.json',
      csvUrl: dailyConsumptionCSV,
      csvFileName: 'daily_german_meat_consumption.csv'
    }" />
</template>

<script setup lang="ts">
import dailyConsumption from "assets/daily_german_meat_consumption.json"
import dailyConsumptionCSV from "assets/daily_german_meat_consumption.csv?url"
</script>
