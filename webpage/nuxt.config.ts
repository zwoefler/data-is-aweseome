// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: [
        '@nuxtjs/strapi',
        '@nuxtjs/tailwindcss'
    ],
    strapi: {
        url: 'http://localhost:1337'
      },
})
