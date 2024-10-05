<template>
  <section class="flex flex-col gap-2 bg-bg_primary">
    <PostList />
  </section>
</template>

<script setup>
import PostList from "../components/post/PostList.vue";

definePageMeta({
  layout: "main",
});
</script>
