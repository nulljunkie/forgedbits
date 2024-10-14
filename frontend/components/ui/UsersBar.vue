<template>
  <div class="bg-white text-gray-600 w-48 p-4">
    <h2 class="text-xl font-bold mb-4 text-center">Top Users</h2>
    <ul>
      <li
        v-for="user in userStore.users"
        :key="user.id"
        class="mb-2 p-2 border-b last:border-none"
      >
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <img
              :src="user.image"
              :alt="user.username[0]"
              class="h-8 min-w-8 bg-gray-300 leading-7 text-center border border-black rounded-full"
            />
            <div>
              <NuxtLink
                :to="`/users/${user.username}`"
                class="font-semibold text-gray-800 text-sm overflow-ellipsis hover:underline"
              >
                {{ user.username }}
              </NuxtLink>
              <div class="text-xs">{{ user.followers }} followers</div>
            </div>
          </div>
        </div>
        <div class="flex justify-between items-center">
          <p class="text-xs font-thin overflow-ellipsis line-clamp-2">
            {{ user.bio }}
          </p>
          <UiFollowButton
            v-if="user.username !== profile.username"
            :user="user"
            class="text-end mt-2"
          />
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useUser } from "#imports";
import { useProfile } from "#imports";

const userStore = useUser();
const profile = useProfile();

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
