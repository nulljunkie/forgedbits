<template>
  <div class="flex flex-col md:flex-row p-8 gap-4">
    <SideBar />
    <div class="flex flex-col gap-3">
      <div v-for="post in posts" :key="post.id">
        <div class="border border-black p-2 rounded-md bg-white">
          <div class="flex flex-row items-center justify-between">
            <div class="flex flex-row">
              <div class="p-1">
                <img :src="profile.image" class="size-10 rounded-full" />
              </div>
              <div class="ml-1 pt-1">
                <div class="font-extrabold">Username</div>
                <div class="text-xs font-thin">created at aug 24, 1999</div>
              </div>
            </div>
            <div class="mr-2">
              <Icon
                name="material-symbols:bookmark-add-outline-rounded"
                size="30"
              />
            </div>
          </div>
          <div class="p-4">
            <NuxtLink :to="{ name: 'posts-post-id', params: { id: post.id } }">
              <div class="text-2xl font-bold">{{ post.title }}</div>
            </NuxtLink>
            <div class="flex flex-row gap-2 p-2">
              <div v-for="tag in post.tags" :key="tag.id">
                <button class="text-gray-700 hover:text-gray-900">
                  #{{ tag.name }}
                </button>
              </div>
            </div>
          </div>

          <div class="flex flex-row justify-between items-center">
            <div class="flex flex-row ml-4">
              <div class="flex flex-row items-center mr-2">
                <button class="">
                  <Icon
                    name="bx:upvote"
                    size="25"
                    class="hover:bg-red-600"
                  /></button
                >{{ 923 }}
              </div>
              <div class="flex flex-row items-center">
                <button class="">
                  <Icon
                    name="bx:downvote"
                    size="25"
                    class="hover:bg-red-600"
                  /></button
                >{{ 22 }}
              </div>
            </div>

            <div class="flex flex-row mr-4 gap-8 items-center">
              <div class="flex flex-row items-center gap-1">
                29<Icon name="iconamoon:comment-dots" size="25" />
              </div>
              <div class="flex flex-row items-center gap-1">
                {{ post.views_count }}<Icon name="ph-eye" size="25" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
//TODO: upvoted icon filled, saved icone with check
import SideBar from "../components/ui/SideBar.vue";
import { useProfile } from "#imports";

const profile = useProfile();

const { data: posts } = await useFetch("http://127.0.0.1:8000/api/posts/");
console.log("posts: ", posts);

definePageMeta({
  layout: "main",
});
</script>
