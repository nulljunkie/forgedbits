<template>
  <div
    v-for="post in props.posts"
    :key="post.id"
    class="bg-white border border-gray-200 rounded-md shadow-sm overflow-hidden"
  >
    <div class="relative" :class="post.cover ? '-mb-8 -z-0' : ''">
      <img :src="post.cover" class="w-full" />
      <div
        class="absolute z-10 bottom-0 bg-gradient-to-t from-white to-transparent h-[15%] w-full text-black"
      ></div>
    </div>
    <div class="p-2">
      <div class="flex flex-row items-center justify-between">
        <AuthorPopover
          :author="post.author_details"
          :created="post.created_at"
          :updated="post.updated_at"
        />

        <Bookmark :saved="post.is_saved" :postId="post.id" />
      </div>
      <div class="px-4 py-2 text-gray-600">
        <NuxtLink :to="{ name: 'posts-post-id', params: { id: post.id } }">
          <div class="text-2xl p-2 hover:text-gray-800 font-bold">
            {{ post.title }}
          </div>
        </NuxtLink>
        <TagList :tags="post.tags" />
      </div>

      <div class="flex flex-row justify-between items-center">
        <VoteView
          :votes="post.votes"
          :object_id="post.id"
          :is_voted="post.is_voted"
          contentType="post"
          direction="row"
        />

        <div
          class="flex flex-row mr-4 gap-8 items-center text-gray-600 text-sm"
        >
          <CommentCount :count="post.comments_count" />
          <div
            class="flex items-center gap-1 hover:text-gray-800 bg-slate-100 rounded-full px-1 h-6"
          >
            <Icon name="ph-eye" class="w-4 h-4" />
            <p v-if="post.views_count">
              {{ post.views_count }}
            </p>
            <p v-else>0</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import { useAuth } from "#imports";
import VoteView from "../../vote/VoteView.vue";
import Bookmark from "../Bookmark.vue";
import AuthorPopover from "./author/AuthorPopover.vue";

const profile = useProfile();
const auth = useAuth();

const props = defineProps({
  posts: {
    type: Array,
    required: true,
  },
});
</script>
