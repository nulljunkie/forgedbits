<template>
  <div class="h-full">
    <!-- <div class="h-12 bg-blue-600"></div> -->
    <ul class="h-full bg-white overflow-y-scroll">
      <li
        v-for="chat in chatStore.myChats"
        :key="chat.id"
        @click="chatStore.selectChat(chat)"
        class="flex gap-2 items-center p-2 hover:bg-gray-200 cursor-pointer"
      >
        <img
          :src="chat.image"
          class="w-8 h-8 rounded-full border border-gray-300"
        />
        <div class="text-gray-900">{{ chat.user }}</div>
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
