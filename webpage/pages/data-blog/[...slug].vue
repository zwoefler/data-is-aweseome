<template>
  <main>
    <ContentDoc v-slot="{ doc }">
      <article class="prose-xl">
        <ContentRenderer :value="doc"></ContentRenderer>
      </article>
    </ContentDoc>
  </main>
</template>
