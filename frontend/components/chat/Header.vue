<template>
  <div class="h-12 w-full bg-gray-700 flex items-center justify-between px-2">
    <div v-if="chatStore.isConversationOpen" class="flex items-center gap-2">
      <button
        @click="chatStore.goBackToChatList"
        class="h-6 w-6 rounded-full text-gray-200 hover:text-gray-50 overflow-hidden"
      >
        <Icon name="material-symbols:arrow-back-ios" size="24" class="ml-0.5" />
      </button>
      <img
        :src="chatStore.selectedChat.image"
        class="w-8 h-8 rounded-full border border-gray-300"
      />
      <div>
        {{ chatStore.selectedChat.user }}
      </div>
    </div>
    <div v-else class="text-white">chat list</div>
    <ChatHideXButton />
  </div>
</template>

<script setup>
import { useChat } from "#imports";
import { useProfile } from "#imports";

const chatStore = useChat();
const profile = useProfile();
</script>
