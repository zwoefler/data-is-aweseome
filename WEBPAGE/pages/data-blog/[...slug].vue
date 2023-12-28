<template>
  <main class="w-full flex justify-center">
    <ContentDoc v-slot="{ doc }">
      <article class="prose md:prose-xl">
        <ContentRenderer :value="doc">
        </ContentRenderer>
      </article>
    </ContentDoc>
  </main>
</template>
