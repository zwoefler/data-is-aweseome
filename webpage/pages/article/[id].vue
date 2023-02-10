<template>
  <div>
    {{ response }}
  </div>
</template>

<script setup lang="ts">
  import type { Articles } from '~/types'
  const { find } = useStrapi()
  const response = await find<Article>('articles')
</script>