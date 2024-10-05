<template>
  <div class="markdown-content">
    <ContentRenderer :value="props.markdown" />
  </div>
</template>

<script setup>
const props = defineProps({
  markdown: {
    type: Object,
    required: true,
  },
});
</script>
