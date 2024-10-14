<template>
  <div>
    <button
      v-if="!isFollowed"
      @click="follow"
      class="py-1 px-2 inline-flex items-center text-xs font-bold rounded-md border border-gray-900 bg-gray-800 text-white hover:bg-gray-900 focus:outline-none focus:bg-gray-900"
    >
      Follow
    </button>
    <button
      v-if="isFollowed"
      @click="unfollow"
      class="py-1 px-2 inline-flex items-center text-xs font-bold rounded-md border border-gray-300 bg-gray-300 text-gray-800 hover:text-gray-900"
    >
      Unfollow
    </button>
  </div>
</template>

<script setup>
import { useUser } from "#imports";

const userStore = useUser();

const props = defineProps({
  user: {
    type: Object,
    required: true,
  },
});

const isFollowed = ref(false);

watch(
  () => props.user.is_followed,
  (newVal) => {
    isFollowed.value = newVal;
  },
);

const follow = async () => {
  await userStore.follow(props.user.id);
  isFollowed.value = true;
};

const unfollow = async () => {
  await userStore.unfollow(props.user.id);
  isFollowed.value = false;
};
</script>
