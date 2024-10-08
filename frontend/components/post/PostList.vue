<template>
  <div v-for="post in props.posts" :key="post.id">
    <div class="border p-2 rounded-md bg-white shadow-sm">
      <div class="flex flex-row items-center justify-between">
        <UserTooltip
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
            class="flex items-center gap-1 hover:text-gray-800 bg-slate-100 rounded-full px-2 py-1"
          >
            <Icon name="ph-eye" size="20" />
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
import VoteView from "../vote/VoteView.vue";
import UserTooltip from "../profile/UserTooltip.vue";
import Bookmark from "./Bookmark.vue";

const profile = useProfile();
const auth = useAuth();

const props = defineProps({
  posts: {
    type: Array,
    required: true,
  },
});
</script>
