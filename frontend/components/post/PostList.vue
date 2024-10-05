<template>
  <div v-for="post in posts" :key="post.id">
    <div class="border p-2 rounded-md bg-white shadow-sm">
      <div class="flex flex-row items-center justify-between">
        <UserTooltip
          :author="post.author_details"
          :created="post.created_at"
          :updated="post.updated_at"
        />

        <Bookmark :saved="post.is_saved" :postId="post.id" />
      </div>
      <div class="p-4">
        <NuxtLink :to="{ name: 'posts-post-id', params: { id: post.id } }">
          <div class="text-2xl font-bold">{{ post.title }}</div>
        </NuxtLink>
        <div class="flex flex-row flex-wrap gap-2 p-2">
          <div v-for="tag in post.tags" :key="tag.id">
            <UButton
              @click=""
              icon="i-mingcute-hashtag-fill"
              size="xm"
              color="amber"
              variant="ghost"
              :label="tag.name"
              :trailing="false"
              class="hover:border hover-border-yellow-300"
            />
          </div>
        </div>
      </div>

      <div class="flex flex-row justify-between items-center">
        <VoteView
          :votes="post.votes"
          :object_id="post.id"
          :is_voted="post.is_voted"
          contentType="post"
          direction="row"
        />

        <div class="flex flex-row mr-4 gap-8 items-center">
          <UButton
            icon="i-iconamoon-comment-dots"
            size="xs"
            color="primary"
            square
            variant="none"
            :label="post.comments_count || '0'"
          />
          <UButton
            icon="i-ph-eye"
            size="xs"
            color="primary"
            square
            disabled
            variant="none"
            :label="post.views_count || '0'"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import { useAuth } from "#imports";
import VoteView from "../vote/VoteView.vue";
// import UserToolTip from "./UserToolTip.vue";
import UserTooltip from "../profile/UserTooltip.vue";
import Bookmark from "./Bookmark.vue";

const profile = useProfile();
const auth = useAuth();

const { data: posts } = await useFetch("http://127.0.0.1:8000/api/posts/", {
  headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
});
</script>
