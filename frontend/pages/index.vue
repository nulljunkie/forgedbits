<template>
  <section class="flex flex-col gap-2 bg-bg_primary">
    <PostList :posts="posts" />
  </section>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();

const { data: posts } = await useFetch("http://127.0.0.1:8000/api/posts/", {
  headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
});

definePageMeta({
  layout: "main",
});
</script>
