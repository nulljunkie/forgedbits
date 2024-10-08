export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: [
    "@pinia/nuxt",
    "@pinia-plugin-persistedstate/nuxt",
    "@nuxt/ui",
    "@nuxtjs/mdc",
    "@nuxt/content",
    "@nuxtjs/i18n",
    "nuxt-tiptap-editor",
    "@nuxt/image",
  ],
  // plugins: [
  //   { src: "@/plugins/prism.js", mode: "client" }, // Ensure Prism is loaded on client side
  // ],

  content: {
    highlight: {
      langs: ["c", "cpp", "java", "python"],
      theme: "github-light",
    },
  },

  compatibilityDate: "2024-08-25",

  experimental: {
    defaults: {
      nuxtLink: {
        // default values
        componentName: "NuxtLink",
        externalRelAttribute: "noopener noreferrer",
        activeClass: "router-link-active",
        exactActiveClass: "router-link-exact-active",
        prefetchedClass: undefined, // can be any valid string class name
        trailingSlash: undefined, // can be 'append' or 'remove'
      },
    },
  },
});
