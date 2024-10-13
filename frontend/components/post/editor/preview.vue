<template>
  <div class="px-8">
    <div class="content-center">
      <h1 class="text-4xl font-extrabold text-gray-700 text-center mb-8">
        {{ props.title }}
      </h1>
      <TagList :tags="props.tags" class="mx-auto" />
    </div>
    <PostEditorRender :markdown="parsedMarkdown" />
  </div>
</template>

<script setup lang="ts">
import markdownParser from "@nuxt/content/transformers/markdown";

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

import Prism from "prismjs";

onMounted(async () => {
  // Ensure content is rendered before highlighting
  await nextTick();
  Prism.highlightAll();
});
</script>
