<template>
  <CustomLineChart :chartData="vwDeliveries" xAxisTitle="Monate" yAxisTitle="Auslieferung an Kunden" :downloadOptions="{
    jsonFileName: 'vw_deliveries_filtered.json',
    csvUrl: vwDeliveriesCSV,
    csvFileName: 'vw_deliveries_filtered.csv'
  }" />
</template>

<script setup lang="ts">
import vwDeliveries from "assets/vw_deliveries_filtered.json"
import vwDeliveriesCSV from "assets/vw_deliveries_filtered.csv?url"
</script>
