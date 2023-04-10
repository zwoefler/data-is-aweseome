<template>
  <div>
    INDEX PAGE
    <p>Data Analysis</p>
    <router-link :to="project.project" v-for="project in projects">
      {{ project.project }}
    </router-link>
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