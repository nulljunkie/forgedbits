<template>
  <div>
    <button
      @click="handleBookmark"
      class="h-7 w-7 flex items-center justify-center text-gray-700 rounded-full hover:bg-gray-100"
    >
      <Icon :name="saveIcon" size="24" />
    </button>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();

const props = defineProps({
  saved: {
    type: String,
    required: true,
  },
  postId: {
    type: Number,
    required: true,
  },
});

const saved = ref(props.saved);

const saveIcon = computed(() => {
  if (saved.value) return "i-material-symbols-bookmark-added-rounded";
  else return "i-material-symbols-bookmark-add-outline-rounded";
});

const handleBookmark = async () => {
  if (auth.user) {
    if (!saved.value) {
      try {
        const res = await $fetch(
          "http://127.0.0.1:8000/api/users/bookmarks/add/",
          {
            method: "post",
            headers: {
              Authorization: `Bearer ${auth.accessToken}`,
            },
            body: {
              post_id: props.postId,
            },
          },
        );
        saved.value = true;
      } catch (err) {
        throw new Error(err);
      }
    } else {
      try {
        const res = await $fetch(
          "http://127.0.0.1:8000/api/users/bookmarks/delete/",
          {
            method: "delete",
            headers: {
              Authorization: `Bearer ${auth.accessToken}`,
            },
            body: {
              post_id: props.postId,
            },
          },
        );
        saved.value = false;
      } catch (err) {
        throw new Error(err);
      }
    }
  } else {
    navigateTo("/auth/login");
  }
};
</script>
