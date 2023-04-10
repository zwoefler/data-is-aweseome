<template>
  <div>
    INDEX PAGE
    <p>Data Analysis</p>
    <p v-for="project in projects">
      {{ project.project }}
    </p>
  </div>
</template>

<script setup lang="ts">
interface Project {
  project: string;
  link:string;
}

  const projects: Object[] = [
    {
      project: "Abiturnoten",
      link: "/abiturnoten"
    }
  ]
</script>