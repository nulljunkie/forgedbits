<template>
  <div class="space-y-2">
    <label v-if="props.label" class="text-gray-700">{{ label }}</label>
    <UTextarea
      v-model="content"
      resize
      autoresize
      color="gray"
      placeholder="Type your comment in here..."
      :ui="{ color: { gray: { outline: 'focus:ring-gray-700 focus:ring-1' } } }"
    />

    <div class="flex flex-row items-center gap-4">
      <UButton
        @click="submitForm"
        :size="props.reply ? 'xs' : 'md'"
        :label="props.reply ? 'Reply' : 'Comment'"
        class="text-white bg-gray-700 border border-gray-700 py-2 hover:text-white hover:bg-gray-700 active:ring-2 active:ring-gray-700"
      />
      <UButton
        @click=""
        :size="props.reply ? 'xs' : 'md'"
        label="Preview"
        class="text-gray-700 bg-white hover:bg-gray-700 border border-gray-700 hover:text-white py-2"
      />
      <UButton
        v-if="reply"
        @click="emit('cancelReply')"
        size="xs"
        label="Cancel"
        class="text-gray-700 bg-white hover:bg-white border border-gray-700 hover:text-gray-700 py-2"
      />
    </div>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";
import { useComment } from "#imports";

const auth = useAuth();
const commentStore = useComment();

const content = ref("");

const props = defineProps({
  label: {
    type: String,
  },
  reply: {
    type: Boolean,
    default: false,
  },
  postId: {
    type: Number,
    required: true,
  },
  commentId: {
    type: Number,
  },
});

const emit = defineEmits(["cancelReply"]);

const submitForm = async () => {
  await commentStore.addComment(content.value, props.postId, props.commentId);
  // try {
  //   const res = await $fetch("http://127.0.0.1:8000/api/comments/add/", {
  //     method: "post",
  //     headers: {
  //       Authorization: `Bearer ${auth.accessToken}`,
  //     },
  //     body: {
  //       content: content.value,
  //       post: props.postId,
  //       parent: props.commentId || null,
  //     },
  //   });
  //   console.log(res);
  // } catch (err) {
  //   throw new Error(err);
  // }
};
</script>
