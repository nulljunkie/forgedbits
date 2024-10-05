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
});
