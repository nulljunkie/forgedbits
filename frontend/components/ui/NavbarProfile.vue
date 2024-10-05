<script setup>
import { useAuth } from "#imports";
import { useProfile } from "#imports";

const auth = useAuth();
const profile = useProfile();
const profileDropDownToggle = ref(false);
</script>

<template>
  <button
    v-if="auth.user"
    @click="profileDropDownToggle = !profileDropDownToggle"
  >
    <UAvatar
      :src="profile.image"
      :alt="auth.user"
      size="sm"
      class="border border-gray-800 font-extrabold text-gray-800"
    />
    <div
      v-if="profileDropDownToggle"
      class="absolute border border-gray-300 z-100 p-8 mt-4 right-1 w-52 rounded-xl shadow-2xl bg-white text-start text-gray-800 hover:text-gray-800 divide-y divide-gray-800"
    >
      <div class="flex flex-col p-1">
        <NuxtLink class="p-1 rounded-md hover:bg-gray-100" to="/profile">
          <div class="font-bold">{{ auth.user }}</div>
          <div v-if="profile.email" class="truncate">{{ profile.email }}</div>
        </NuxtLink>
      </div>
      <div class="flex flex-col py-1">
        <NuxtLink class="py-1 hover:bg-gray-100" to="/about">Settings</NuxtLink>
        <NuxtLink class="py-1 hover:bg-gray-100" to="/post/create"
          >Create post</NuxtLink
        >
        <NuxtLink class="py-1 hover:bg-gray-100" to="/"
          ><a @click="auth.logout"
            ><Icon name="tabler:logout" />Sign out</a
          ></NuxtLink
        >
      </div>
    </div>
  </button>
</template>
