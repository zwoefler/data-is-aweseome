<template>
  <main class="w-full">
    <ContentDoc v-slot="{ doc }">
      <article class="prose prose-lg md:prose-xl">
        <ContentRenderer :value="doc">
        </ContentRenderer>
      </article>
    </ContentDoc>
  </main>
</template>
