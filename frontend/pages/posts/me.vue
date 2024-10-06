<template>
  <div>
    <div class="mt-8">
      <TransitionGroup name="list" tag="ul">
        <li
          v-for="post in postStore.myPosts"
          :key="post.id"
          class="bg-white mb-4 p-2 rounded-md shadow-sm border border-gray-300"
        >
          <h1 class="text-gray-800 text-2xl font-bold">{{ post.title }}</h1>
          <div class="text-sm font-thin text-gray-600">
            by {{ post.author_details.username }}
          </div>
          <div class="flex flex-row gap-2">
            <div v-for="tag in post.tags" :key="tag.id">
              <div class="text-gray-500 text-bold">#{{ tag.name }}</div>
            </div>
          </div>

          <div class="flex justify-end mr-2 gap-4">
            <UButton @click="" label="Edit" color="blue" variant="outline" />
            <UButton
              @click="postStore.deleteMyPost(post.id)"
              label="Delete"
              color="pink"
            />
          </div>
        </li>
      </TransitionGroup>
    </div>
  </div>
</template>

<script setup>
import { usePost } from "#imports";

const postStore = usePost();

await postStore.getMyPosts();

definePageMeta({
  layout: "basic",
});
</script>

<style scoped>
.list-enter-active {
  animation: bounce-in 0.5s;
}
.list-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}
</style>
