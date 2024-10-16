<template>
  <div>
    <button
      @click="chatStore.showChat = false"
      class="text-red-500 rounded-full inline-block text-center leading-loose w-6 h-6 hover:bg-opacity-30 hover:bg-red-500"
    >
      <Icon name="material-symbols:close" size="22" class="m-auto" />
    </button>
  </div>
</template>

<script setup>
import { useChat } from "#imports";

const chatStore = useChat();
</script>
