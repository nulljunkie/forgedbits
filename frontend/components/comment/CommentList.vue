<template>
  <div class="p-8">
    <CommentForm label="Leave a comment:" :postId="props.postId" class="mb-8" />

    <ul>
      <Comment
        v-for="comment in commentStore.comments"
        :key="comment.id"
        :comment="comment"
      />
    </ul>
  </div>
</template>

<script setup>
import CommentForm from "../../components/comment/CommentForm.vue";
import Comment from "./Comment.vue";
import { useComment } from "#imports";
import { useAuth } from "#imports";

const props = defineProps({
  postId: {
    type: Number,
    required: true,
  },
});

const auth = useAuth();

const commentStore = useComment();

await commentStore.getComments(props.postId);

// const { data: comments } = await useFetch(
//   `http://127.0.0.1:8000/api/comments/post/${props.postId}`,
//   {
//     headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
//   },
// );
</script>
