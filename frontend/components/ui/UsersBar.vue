<template>
  <div class="bg-white text-gray-600 p-4">
    <h2 class="text-xl font-bold mb-4">User List</h2>
    <ul>
      <li
        v-for="user in userStore.users"
        :key="user.id"
        class="mb-2 p-2 border-b last:border-none"
      >
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <UAvatar
              :src="user.image"
              :alt="user.username"
              size="xs"
              class="border border-gray-800 bg-gray-200"
            />
            <div class="">
              <h3 class="font-semibold text-sm overflow-ellipsis">
                {{ user.username }}
              </h3>
              <p class="text-xs font-thin overflow-ellipsis line-clamp-2">
                this merely a simple fucking bio for this motherfucking useless
                user
              </p>
            </div>
          </div>
          <!-- <FollowButton :profileId="user.id" :isFollowed="user.isFollowed" /> -->
          <FollowButton :user="user" />
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import FollowButton from "../profile/FollowButton.vue";

import { useUser } from "#imports";

const userStore = useUser();

await userStore.getUsers();

// import { useAuth } from "#imports";

// const auth = useAuth();

// const {
//   data: users,
//   pending,
//   error,
// } = await useFetch("http://127.0.0.1:8000/api/users/list/", {
//   headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
// });

// console.log("users: ", users.value);
</script>
