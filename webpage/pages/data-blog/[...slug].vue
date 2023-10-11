<template>
  <main class="w-full">
    <ContentDoc v-slot="{ doc }">
      <article class="prose">
        <ContentRenderer :value="doc">
        </ContentRenderer>
      </article>
    </ContentDoc>
  </main>
</template>
