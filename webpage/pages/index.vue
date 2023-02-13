<template>
  <div>
    <div v-for="resp in response.data">
      <router-link class="text-blue-500" :to="`article/${ resp.id }`">
        <p class="font-bold">
          {{ resp.attributes.title }}
        </p>
      </router-link>
      {{ formatDate(resp.attributes.publishedAt) }}

    </div>
  </div>
</template>

<script setup lang="ts">
  const { find } = useStrapi()
  const response = await find<Article>('articles', { populate: "images"})

  function formatDate(iso8601_date) {
    const date = new Date(iso8601_date);
    const options = {
      day: 'numeric',
      month: 'numeric',
      year: 'numeric',
      hour: 'numeric',
      minute: 'numeric'
    };
    const formattedDate = date.toLocaleDateString('de-DE', options)

    return formattedDate
  }
</script>