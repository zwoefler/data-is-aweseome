<template>
  <div class="overflow-x-auto">
    <h1 class="text-2xl font-bold mb-4">Proteste in Hessen</h1>

    <table class="border border-gray-300 shadow-sm rounded-md text-xs ">
      <thead>
        <tr v-if="tableData.length > 0">
          <th v-for="(value, key) in tableData[0]" :key="key" class="text-xs p-2 border-b font-bold">{{
            key }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in tableData" :key="index">
          <td v-for="(value, key) in row" :key="key" class="text-xs p-2 border-b">{{ value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const csv = await useAsyncData('demos', () => queryContent('sources', 'demos').findOne())
const csvData = csv.data.value.body
const tableData = csvData.map(({ Latitude, Longitude, ...rest }) => rest);
console.log(tableData)
</script>