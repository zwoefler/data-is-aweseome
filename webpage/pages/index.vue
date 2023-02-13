<template>
  <div>
    <div v-for="resp in response.data">
      <router-link class="text-blue-500" :to="`article/${ resp.id }`">
        <p class="font-bold">
          {{ resp.attributes.title }}
        </p>
      </router-link>
        {{ resp.attributes.publishedAt }}
    </div>
  </div>
</template>

<script setup lang="ts">
  const { find } = useStrapi()
  const response = await find<Article>('articles', { populate: "images"})
</script>