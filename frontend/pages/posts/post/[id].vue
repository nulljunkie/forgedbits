<template>
  <div class="flex flex-row">
    <div class="hidden md:block mr-4">
      <div class="sticky top-24 space-y-4">
        <Bookmark
          :saved="postStore.currentPost.is_saved"
          :postId="postStore.currentPost.id"
          class="border border-black"
        />
        <VoteView
          :votes="postStore.currentPost.votes"
          :object_id="postStore.currentPost.id"
          :is_voted="postStore.currentPost.is_voted"
          contentType="post"
          direction="col"
        />
      </div>
    </div>
    <div class="">
      <section class="bg-white shadow-md rounded-lg">
        <PostPostContent />
        <CommentList :postId="postStore.currentPost.id" />
      </section>
    </div>
  </div>
</template>

<script setup>
import { usePost } from "#imports";

const postStore = usePost();

const route = useRoute();
const id = computed(() => +route.params.id);

await postStore.getPost(id.value);

definePageMeta({
  layout: "post",
});
</script>
