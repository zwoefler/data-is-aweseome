<template>
  <div>
    <p id="title" class="font-bold">{{ article.title }}</p>
    <p id="published">{{ article.publishedAt }}</p>
    <br>
    <img :src="imageURL" alt="">
    <div>
      <p>{{ article.text }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
  import type { Articles } from '~/types'

  const { findOne } = useStrapi()
  const route = useRoute()
  const baseURL = useStrapiUrl()
  route.params.id

  const response = await findOne<Article>('articles', route.params.id, { populate: ["images"]})
  const article = response.data.attributes
  const imageURL = new URL(article.images.data[0].attributes.url, baseURL).toString()


</script>