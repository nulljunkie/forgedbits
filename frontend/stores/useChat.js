import { defineStore } from "pinia";
import { useAuth } from "#imports";

export const useChat = defineStore("chat", () => {
  const auth = useAuth();

  const showChat = ref(false);
  const showChatList = ref(true);
  const selectedChatId = ref(0);

  const toggleChat = () => {
    showChat.value = !showChat.value;
  };

  const goBackToChatList = () => {
    showChatList.value = true;
    selectedChatId.value = 0;
  };

  const selectChat = (id) => {
    selectedChatId.value = id;
    showChatList.value = false;
  };

  return {
    showChat,
    toggleChat,
    showChatList,
    selectedChatId,
    goBackToChatList,
    selectChat,
  };
});
