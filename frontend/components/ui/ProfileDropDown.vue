<script setup lang="ts">
import { useAuth } from "#imports";
import { useProfile } from "#imports";

const auth = useAuth();
const profile = useProfile();

onMounted(async () => {
  if (auth.user) {
    await profile.get();
  }
});

const route = {
  profile: () => navigateTo("/profile"),
  settings: () => navigateTo("/settings"),
  myPosts: () => navigateTo("/posts/me"),
  create: () => navigateTo("/posts/create"),
};

const items = [
  [
    {
      label: auth.user,
      slot: "account",
      click: route.profile,
    },
  ],
  [
    {
      label: "Settings",
      icon: "i-heroicons-cog-8-tooth",
      click: route.settings,
    },
  ],
  [
    {
      label: "My posts",
      icon: "material-symbols-article-outline",
      click: route.myPosts,
    },
    {
      label: "Create post",
      icon: "i-heroicons-pencil-square",
      click: route.create,
    },
  ],
  [
    {
      label: "Sign out",
      icon: "i-ic-outline-logout",
      click: auth.logout,
    },
  ],
];
</script>

<template>
  <div class="flex justify-center items-center">
    <UDropdown
      :items="items"
      :ui="{
        item: {
          disabled: 'cursor-text select-text',
          size: 'text-base',
        },
        shadow: 'shadow-2xl',
        width: 'min-w-[280px]',
        ring: 'ring-1 ring-gray-300',
        padding: 'p-2',
        base: 'relative focus:outline-none overflow-hidden ',
      }"
      :popper="{ arrow: true }"
    >
      <UAvatar
        :src="profile.image"
        :alt="auth.user"
        size="sm"
        class="border border-gray-800 bg-gray-200"
      />

      <template #account="{ item }">
        <div class="text-left">
          <p>Signed in as</p>
          <p class="truncate font-medium text-gray-900">
            {{ item.label }}
          </p>
          <p
            v-if="profile.email"
            class="overflow-ellipsis font-medium text-gray-900"
          >
            {{ profile.email }}
          </p>
        </div>
      </template>

      <template
        #item="{ item }"
        class="flex flex-row justify-start items-center bg-red-200"
      >
        <span class="truncate">{{ item.label }}</span>
        <UIcon
          :name="item.icon"
          class="flex-shrink-0 h-4 w-4 text-gray-700 ms-auto"
        />
      </template>
    </UDropdown>
  </div>
</template>
