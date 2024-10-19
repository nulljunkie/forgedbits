<template>
  <div class="h-full overflow-hidden flex flex-col">
    <div class="flex-1 bg-white text-gray-900 overflow-y-auto">
      <div class="overflow-y-scroll h-full flex flex-col-reverse gap-2 p-2">
        <div v-for="msg in chatStore.selectedChat.messages">
          <div
            class="p-2 rounded-md w-fit max-w-[80%]"
            :class="
              msg.sender == auth.user
                ? 'bg-sky-600 text-white ml-auto'
                : 'bg-gray-100 text-gray-800'
            "
          >
            {{ msg.message }}
          </div>
        </div>
      </div>
    </div>

    <form @submit.prevent="sendMessage" class="flex bg-white">
      <input
        type="text"
        v-model="message"
        placeholder="type message..."
        class="w-full text-gray-800 bg-white px-2 py-1 focus:outline-none"
      />
      <button class="h-full px-2 bg-blue-500">
        <Icon name="tabler:send" />
      </button>
    </form>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";
import { useChat } from "#imports";

const auth = useAuth();
const chatStore = useChat();

await chatStore.getOldMessages();

const message = ref("");

const sendMessage = () => {
  chatStore.selectedChat.ws.send(
    JSON.stringify({
      sender: auth.user,
      message: message.value,
    }),
  );
  message.value = "";
};
</script>
