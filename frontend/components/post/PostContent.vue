<template>
  <div>
    <div class="w-[900px]">
      <div
        v-if="postStore.currentPost.cover"
        class="max-h-[320px] w-full rounded-t-lg mb-8 overflow-hidden flex items-center justify-center"
      >
        <img
          :src="postStore.currentPost.cover"
          alt="Blog Cover"
          class="w-full"
        />
      </div>
      <LoadPreview
        :title="postStore.currentPost.title"
        :content="postStore.currentPost.content"
        :tags="postStore.currentPost.tags"
      />
    </div>
    <div class="mt-8 px-8">
      {{
        postStore.currentPost.comments_count
          ? "comments " + "(" + postStore.currentPost.comments_count + ")"
          : "No comments yet."
      }}
    </div>
  </div>
</template>

<script setup>
import LoadPreview from "./LoadPreview.vue";
import { usePost } from "#imports";

const postStore = usePost();
</script>
