<template>
  <main class="w-full flex justify-center">
    <ContentDoc v-slot="{ doc }">
      <article class="prose md:prose-xl prose-invert w-full">
        <ContentRenderer :value="doc">
        </ContentRenderer>
      </article>
    </ContentDoc>
  </main>
</template>
