<template>
  <div>
    <ul v-if="pending" class="">
      <li v-for="i in 5" :key="i.id">
        <PostListItemSkeleton />
      </li>
    </ul>
    <div
      v-else-if="!posts.length"
      class="flex h-48 bg-white items-center justify-center text-gray-700 text-4xl font-bold px-8 text-center"
    >
      there are no post with this tag
    </div>

    <div v-else class="space-y-2">
      <PostPostList :posts="posts" />
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
