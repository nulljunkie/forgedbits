import { defineNuxtPlugin } from "#app";
import Prism from "prismjs";
import "prismjs/themes/prism-okaidia.css"; // Replace with the theme you want
import "prismjs/components/prism-javascript.min.js"; // Import the languages you need
import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-css.min.js";

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.provide("prism", Prism);
});
