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
      <div class="flex flex-col h-full">
        <div class="h-12">
          <ChatHeader />
        </div>
        <div class="flex-1 overflow-hidden">
          <transition name="chat-slide">
            <ChatSelectedConversation v-if="chatStore.isConversationOpen" />
          </transition>
          <transition name="chat-list-slide">
            <ChatList v-if="!chatStore.isConversationOpen" />
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import { useChat } from "#imports";

const profile = useProfile();
const chatStore = useChat();

await chatStore.getMyChats();
</script>

<style scoped>
/* .chat-slide-enter-active, */
/* .chat-slide-leave-active { */
/*   transition: transform 0.3s ease; */
/* } */
/**/
/* .chat-slide-enter-to { */
/*   transform: translateX(100%); */
/* } */

/* .chat-slide-enter { */
/*   transform: translateX(0); */
/* } */

/* .chat-slide-leave { */
/*   transform: translateX(0); */
/* } */

/* .chat-slide-leave-to { */
/*   transform: translateX(100%); */
/* } */
</style>
