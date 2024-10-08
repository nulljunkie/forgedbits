<template>
  <div class="flex flex-row flex-wrap gap-2 p-2">
    <div v-for="(tag, index) in props.tags" :key="index">
      <NuxtLink :to="{ name: 'posts-tag-slug', params: { slug: tag.name } }">
        <span
          :class="`rounded-full px-3 py-1 text-sm font-semibold ${classes[index % classes.length]} `"
          >#{{ tag.name }}</span
        >
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  tags: {
    type: Array,
    required: true,
  },
});

const classes = ref([
  "bg-rose-50 hover:bg-rose-100 text-gray-700",
  "bg-teal-50 hover:bg-teal-100 text-gray-700",
  "bg-indigo-50 hover:bg-indigo-100 text-gray-700",
]);
</script>
