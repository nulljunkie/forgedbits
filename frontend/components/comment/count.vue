<template>
  <button
    class="flex items-center gap-1 hover:text-gray-800 bg-slate-100 rounded-full px-2 h-6"
  >
    <Icon name="uil:comment-dots" class="w-4 h-4" />
    <p v-if="props.count">
      {{ props.count }}
    </p>
    <p v-else>0</p>
  </button>
</template>

<script setup>
const props = defineProps({
  count: {
    type: Number,
    required: true,
  },
});
</script>
