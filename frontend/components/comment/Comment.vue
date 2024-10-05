<template>
  <div class="w-full">
    <article class="pt-4 text-base bg-white rounded-lg">
      <footer class="flex justify-between items-center mb-2">
        <div class="flex items-center">
          <p
            class="inline-flex items-center mr-3 text-sm text-gray-900 font-semibold"
          >
            <UAvatar
              size="xs"
              :src="comment.author_details.image"
              :alt="comment.author_details.username"
            />
            <p class="ml-1">{{ comment.author_details.username }}</p>
          </p>
          <p class="text-sm text-gray-600">
            {{ createdDate }}
          </p>
        </div>
      </footer>
      <p class="text-gray-600 mb-2">{{ comment.content }}</p>
      <div v-if="!replyMode" class="flex items-center">
        <VoteView
          :votes="comment.votes"
          :object_id="comment.id"
          :is_voted="comment.is_voted"
          contentType="comment"
          direction="row"
        />

        <UButton
          @click="replyMode = true"
          icon="i-carbon-reply"
          size="xs"
          color="gray"
          square
          label="reply"
          variant="link"
        />
      </div>

      <CommentForm
        v-if="replyMode"
        reply="true"
        @cancelReply="replyMode = false"
        :commentId="comment.id"
        :postId="comment.post"
        class="mb-2"
      />
    </article>

    <button
      v-if="comment.replies.length"
      @click="toggleReplies"
      class="ml-2 text-orange-500 hover:text-orange-700 focus:outline-none"
    >
      {{ showReplies ? "[-]" : "[+] " + pluralize(comment.replies.length) }}
    </button>

    <div v-if="showReplies">
      <div
        v-for="reply in comment.replies"
        :key="reply.id"
        class="ml-6 flex items-center"
      >
        <Comment :comment="reply" />
      </div>
    </div>
  </div>
</template>

<script setup>
import CommentForm from "~/components/comment/CommentForm.vue";
import VoteView from "~/components/vote/VoteView.vue";
import { useProfile } from "#imports";
import { formatDate } from "~/utils/dateFns.js";

const profile = useProfile();

const props = defineProps({
  comment: {
    type: Object,
    required: true,
  },
});

const createdDate = computed(() => {
  return formatDate(new Date(props.comment.created_at));
});

const showReplies = ref(false);
const replyMode = ref(false);

function pluralize(n) {
  return n + (n === 1 ? " reply" : " replies");
}

function toggleReplies() {
  showReplies.value = !showReplies.value;
}
</script>
