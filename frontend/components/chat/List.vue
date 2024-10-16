<template>
  <div class="h-full">
    <div class="h-12 bg-blue-600"></div>
    <ul class="h-full bg-red-200 overflow-y-scroll">
      <li
        v-for="i in 15"
        :key="i.id"
        @click="chatStore.selectChat(i)"
        class="flex gap-2 items-center p-2 hover:bg-gray-100"
      >
        <img
          :src="profile.image"
          class="w-8 h-8 rounded-full border border-gray-300"
        />
        <div>
          {{ profile.username }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import { useChat } from "#imports";

const profile = useProfile();
const chatStore = useChat();
</script>
