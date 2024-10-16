<template>
  <div class="h-full">
    <div class="h-12 w-full bg-gray-700 flex items-center justify-between px-2">
      <div class="flex items-center gap-2">
        <button
          @click="chatStore.goBackToChatList"
          class="h-6 w-6 rounded-full text-gray-200 hover:text-gray-50 overflow-hidden"
        >
          <Icon
            name="material-symbols:arrow-back-ios"
            size="24"
            class="ml-0.5"
          />
        </button>
        <img
          :src="profile.image"
          class="w-8 h-8 rounded-full border border-gray-300"
        />
        <div>
          {{ profile.username }}
        </div>
      </div>
      <ChatHideXButton />
    </div>
    <!--TODO:  chat selected body, messages -->
    <div class="h-full bg-sky-200 text-gray-900">
      {{ chatStore.selectedChatId }}
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import { useChat } from "#imports";

const profile = useProfile();
const chatStore = useChat();
</script>
