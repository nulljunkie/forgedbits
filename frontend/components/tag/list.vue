<template>
  <div class="flex flex-row flex-wrap gap-2 p-2 w-max">
    <div v-for="(tag, index) in props.tags" :key="index">
      <NuxtLink :to="{ name: 'posts-tag-slug', params: { slug: tag.name } }">
        <span
          :class="`flex items-center rounded-lg bg-gray-50 bg-opacity-70 px-3 py-1 text-sm font-bold transition duration-300 ease-in group ${classes[Math.floor(Math.random() * classes.length)]} `"
          >#
          <p class="text-gray-600 bg-em font-normal group-hover:text-gray-800">
            {{ tag.name }}
          </p></span
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
  "hover:bg-rose-50 hover:border-rose-200 text-rose-300",
  "hover:bg-teal-50 hover:border-teal-200 text-teal-300 ",
  "hover:bg-sky-100 hover:border-sky-200 text-sky-400 ",
  "hover:bg-emerald-100 hover:border-emerald-200 text-emerald-400 ",
  "hover:bg-orange-100 hover:border-orange-200 text-orange-400 ",
]);
</script>
