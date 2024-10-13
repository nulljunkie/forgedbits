<template>
  <section class="flex flex-col gap-3">
    <PostPostList :posts="posts" />
  </section>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();

const { data: posts } = await useFetch("http://127.0.0.1:8000/api/posts/", {
  headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
});

onMounted(() => {
  auth.authenticating = false;
});

definePageMeta({
  layout: "main",
  middleware: "oauth",
});
</script>
