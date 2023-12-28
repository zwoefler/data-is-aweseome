<template>
  <div>
    <div class="flex flex-col">
      <router-link :to="blog._path" v-for="blog in data">
        {{ blog.title }} - {{ blog.description }}
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