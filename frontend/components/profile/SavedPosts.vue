<template>
  <div class="w-full">
    <h2 class="text-2xl font-semibold text-gray-800 mb-4">Saved Posts</h2>
    <div v-if="posts && posts.length">
      <div
        v-for="post in posts"
        :key="post.id"
        class="bg-white p-2 mb-1 rounded-lg shadow-sm"
      >
        <NuxtLink :to="`/posts/post/${post.id}`">
          <h3 class="text-lg font-medium text-gray-800 line-clamp-1">
            {{ post.title }}
          </h3>
        </NuxtLink>
        <p class="text-sm text-gray-600">by {{ post.author }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();

const { data: posts } = await useFetch(
  "http://127.0.0.1:8000/api/posts/saved/",
  {
    headers: {
      Authorization: `Bearer ${auth.accessToken}`,
    },
  },
);

console.log("posts: ", posts);
</script>
