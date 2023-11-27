// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devServer: {},
    modules: [
        '@nuxt/content',
        '@nuxtjs/tailwindcss',
        '@nuxt/test-utils',
        'vitest'
    ],
})
