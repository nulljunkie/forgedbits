<template>
  <div>
    <button
      @click="showChat = !showChat"
      class="fixed bottom-0 z-20 right-0 w-10 h-10 rounded-full bg-orange-600 text-white m-4 flex items-center justify-center"
    >
      <Icon name="bx:bxs-conversation" size="24" class="bg-white" />
    </button>

    <div
      v-show="showChat"
      class="fixed z-30 bottom-12 right-0 m-4 w-80 h-[60%] bg-white rounded-md overflow-hidden border shadow-xl"
    >
      <div
        class="h-12 w-full bg-gray-700 flex items-center justify-between px-2"
      >
        <div class="flex items-center gap-2">
          <img
            :src="profile.image"
            class="w-8 h-8 rounded-full border border-gray-300"
          />
          <div>
            {{ profile.username }}
          </div>
        </div>
        <button
          @click="showChat = !showChat"
          class="text-red-500 rounded-full inline-block text-center leading-loose w-6 h-6 hover:bg-opacity-30 hover:bg-red-500"
        >
          <Icon name="material-symbols:close" size="22" class="m-auto" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";

const profile = useProfile();
const showChat = ref(false);
</script>
