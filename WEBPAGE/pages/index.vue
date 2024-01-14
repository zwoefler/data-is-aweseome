<template>
  <div class="space-y-2">
    <h1 class="text-3xl font-bold">ARTIKEL:</h1>
    <div class="flex flex-col">
      <router-link class="p-2 flex flex-col border border-2 border-gray-600/20" :to="blog._path" v-for="blog in data">
        <p class="font-bold text-xl">{{ blog.title }}</p>
        <p>{{ blog.description }}</p>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
const { data } = await useAsyncData('home', () => queryContent('data-blog')
  .only(['title', '_path', 'description'])
  .where({ draft: { $ne: true } })
  .find()
)

</script>