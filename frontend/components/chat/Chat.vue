<template>
  <div>
    <button
      @click="chatStore.toggleChat"
      class="fixed bottom-0 z-20 right-0 w-10 h-10 rounded-full bg-orange-600 text-white m-4 flex items-center justify-center"
    >
      <Icon name="bx:bxs-conversation" size="24" class="bg-white" />
    </button>

    <div
      v-show="chatStore.showChat"
      class="fixed z-30 bottom-12 right-0 m-4 w-80 h-[60%] bg-white rounded-md overflow-hidden border shadow-xl"
    >
      <ChatSelectedConversation
        v-if="!chatStore.showChatList && chatStore.selectedChatId"
      />
      <ChatList
        v-else-if="chatStore.showChatList && !chatStore.selectedChatId"
      />
      <div class="text-black">showChatList: {{ chatStore.showChatList }}</div>
      <div class="text-black">
        selectedChatId: {{ chatStore.selectedChatId }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import { useChat } from "#imports";

const profile = useProfile();
const chatStore = useChat();
</script>
