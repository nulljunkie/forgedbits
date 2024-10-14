<template>
  <div>
    <button
      v-if="!isFollowed"
      @click="follow"
      class="py-1 px-2 inline-flex items-center text-xs font-bold rounded-lg border border-gray-900 bg-gray-800 text-white hover:bg-gray-900 focus:outline-none focus:bg-gray-900"
    >
      Follow
    </button>
    <button
      v-if="isFollowed"
      @click="unfollow"
      class="py-1 px-2 inline-flex items-center text-xs font-bold rounded-lg border border-black bg-gray-50 text-gray-800 hover:bg-gray-100"
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

// FIXME: if follow button state is changed within author tooltip,
// it should also be changed within user list sidebar if user is in it

const isFollowed = ref(props.user.is_followed);

const follow = async () => {
  await userStore.follow(props.user.id);
  isFollowed.value = true;
  // const index = userStore.users.findIndex((obj) => obj.id == props.user.id);
  // console.log("index: ", index);
  // if (index >= 0) {
  //   userStore.users[index].is_followed = true;
  // }
};

const unfollow = async () => {
  await userStore.unfollow(props.user.id);
  isFollowed.value = false;
  // const index = userStore.users.findIndex((obj) => obj.id == props.user.id);
  // console.log("index: ", index);
  // if (index >= 0) {
  //   userStore.users[index].is_followed = false;
  // }
};
</script>
