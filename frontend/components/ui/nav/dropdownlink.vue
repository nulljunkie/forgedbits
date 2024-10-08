<template>
  <NuxtLink
    :to="props.link"
    class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
  >
    <span class="flex items-center gap-2">
      <Icon :name="props.icon" size="24" />
      <span> {{ props.value }} </span>
    </span>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  link: {
    type: String,
  },
  icon: {
    type: String,
  },
  value: {
    type: String,
  },
});
</script>
