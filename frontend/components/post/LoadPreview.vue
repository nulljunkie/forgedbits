<template>
  <div class="px-8">
    <h1 class="text-4xl font-extrabold text-gray-800 text-center mb-8">
      {{ props.title }}
    </h1>
    <hr class="mb-4" />
    <CustomRenderer :markdown="parsedMarkdown" />
    <div class="flex flex-row text-sm text-gray-700">
      <div v-for="tag in props.tags" :key="tag.id" class="">
        <UButton
          @click=""
          icon="i-mingcute-hashtag-fill"
          size="xm"
          color="amber"
          variant="ghost"
          :label="tag.name"
          :trailing="false"
          class="px-1 my-2 mx-1"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import markdownParser from "@nuxt/content/transformers/markdown";
import CustomRenderer from "./CustomRenderer.vue";

const parsedMarkdown = ref("");

const props = defineProps({
  title: {
    type: Object,
    required: true,
  },
  content: {
    type: Object,
    required: true,
  },
  tags: {
    type: Object,
    required: false,
  },
});

if (props.content) {
  parsedMarkdown.value = await markdownParser.parse(null, props.content);
  console.log("paresed: ", parsedMarkdown);
}

// import Prism from "prismjs";
//
// onMounted(async () => {
//   // Ensure content is rendered before highlighting
//   await nextTick();
//   Prism.highlightAll();
// });
</script>
