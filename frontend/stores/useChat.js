import { defineStore } from "pinia";
import { useAuth } from "#imports";

export const useChat = defineStore("chat", () => {
  const auth = useAuth();

  const showChat = ref(false);
  const showChatList = ref(true);
  const selectedChatId = ref(0);

  const myChats = ref([]); // [messages, socket, chatId, alice, bob]

  // TODO:  1. get all active chats with their old messages
  //            chat[messages, socket, ]
  //        2. foreach chat create socket and listen on it, when new
  //            message add it messages of that chat

  const letsChat = async (user) => {
    // TODO: 1. if chat in chats, sectect the chat
    //       2. else create new chat,
    //          2.1. get chatId, user at the other end
    //          2.2. create socket, connect and listen
    //          2.3. add chat to chats

    const chat = myChats.value.find((obj) => obj.reciever === user);
    if (chat) {
      console.log("let's chat", chat);
      showChat.value = true;
      showChatList.value = false;
      selectedChatId.value = chat.chatId;
    } else {
      const response = await $fetch("http://127.0.0.1:8000/api/chat/", {
        method: "post",
        headers: {
          Authorization: `Bearer ${auth.accessToken}`,
        },
        body: {
          alice: auth.user,
          bob: user,
        },
      });

      console.log("chat created", response);
      // response should be {chatId:int, alice:username, bob:userame}
      const chat = { messages: [] };
      ({ id: chat.chatId, alice: chat.alice, bob: chat.bob } = response);
      chat.socket = new WebSocket(
        `ws://127.0.0.1:8000/ws/chat/?token="${auth.accessToken}&id=${chat.chatId}`,
      );
      console.log("your chat is ready ", chat);
      myChats.value.unshift(chat);
      showChat.value = true;
      showChatList.value = false;
      selectedChatId.value = chat.chatId;
    }
  };

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
    letsChat,
  };
});
