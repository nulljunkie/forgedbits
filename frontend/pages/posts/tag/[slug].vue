<template>
  <div>
    <div
      v-if="pending"
      class="flex h-screen items-center justify-center text-gray-700 text-7xl font-bold"
    >
      Loading...
    </div>
    <div
      v-else-if="!posts.length"
      class="flex h-screen items-center justify-center text-gray-700 text-7xl font-bold"
    >
      there are no post with this tag
    </div>

    <div v-else>
      <div v-for="post in posts" class="p-4 mb-4 bg-white rounded-md shadow-md">
        <div>{{ post.title }}</div>
        <div>by {{ post.author_details.username }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();

const route = useRoute();
const tag = computed(() => route.params.slug);

const {
  data: posts,
  pending,
  error,
} = useLazyFetch(`http://127.0.0.1:8000/api/posts/tag/${tag.value}`, {
  headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
});

definePageMeta({
  layout: "main",
});
</script>
