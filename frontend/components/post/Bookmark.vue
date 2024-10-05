<template>
  <div>
    <UButton
      :icon="Icon"
      @click="handleBookmark"
      size="sm"
      color="primary"
      square
      variant="none"
    />
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

const Icon = computed(() => {
  if (saved.value) return "i-material-symbols-bookmark-added-rounded";
  else return "i-material-symbols-bookmark-add-outline-rounded";
});

const handleBookmark = async () => {
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
};
</script>
