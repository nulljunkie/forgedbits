<template>
  <!-- class="max-h-[320px] w-full rounded-t-lg overflow-hidden flex items-center justify-center" -->
  <div>
    <div class="w-[900px]">
      <div v-if="postStore.currentPost.cover" class="h-[320px] w-full">
        <img
          :src="postStore.currentPost.cover"
          alt="Blog Cover"
          class="h-full w-full object-fill"
        />
      </div>
      <div class="text-gray-600">published by @imad on dec 24, 2060</div>
      <PostEditorPreview
        :title="postStore.currentPost.title"
        :content="postStore.currentPost.content"
        :tags="postStore.currentPost.tags"
        class="pt-8"
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
import { usePost } from "#imports";

const postStore = usePost();
</script>
