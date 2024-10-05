<template>
  <div>
    <UButton
      v-if="!isFollowed"
      @click="follow"
      size="xs"
      color="black"
      variant="solid"
      label="Follow"
    />
    <UButton
      v-if="isFollowed"
      @click="unfollow"
      size="xs"
      color="black"
      variant="outline"
      label="Unfollow"
    />
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
