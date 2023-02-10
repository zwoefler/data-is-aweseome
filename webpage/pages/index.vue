<template>
  <div>
    {{ response }}
    <div></div>
    <div class="bg-gray-500 h-32" v-for="resp in response.data">
      <p>
        {{ resp.attributes.title }}
      </p>
        {{ resp.attributes.text }}
        <img :src="'http://localhost:1337' + resp.attributes.images.data[0].attributes.url" alt="">
    </div>
  </div>
</template>

<script setup lang="ts">
  const { find } = useStrapi()
  const url = useStrapiUrl()
  const response = await find<Article>('articles', { populate: "images"})
</script>