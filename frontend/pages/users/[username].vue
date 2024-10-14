<template>
  <div class="text-4xl font-bold text-gray-700">
    {{ username }}
  </div>
</template>

<script setup>
const route = useRoute();

const username = computed(() => route.params.username);

definePageMeta({
  layout: "basic",
});
</script>
