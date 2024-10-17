import { defineStore } from "pinia";
import { useAuth } from "#imports";

export const useChat = defineStore("chat", () => {
  const auth = useAuth();

  const showChat = ref(false);
  const showChatList = ref(true);
  const selectedChatId = ref(0);

  const myChats = ref([]); // [messages[id, message, timestamp, sender, chat], socket, chatId, alice, bob]

  const getMyChats = async () => {
    if (auth.user) {
      const { data } = useLazyFetch("http://127.0.0.1:8000/api/chat/", {
        headers: {
          Authorization: `Bearer ${auth.accessToken}`,
        },
      });

      if (data.value) {
        data.value.forEach((obj) => {
          const chat = {};
          ({ id: chat.chatId, alice: chat.alice, bob: chat.bob } = obj);
          // get old messages
          const messages = $fetch(
            `http://127.0.0.1:8000/api/chat/messages/${chat.chatId}`,
            {
              headers: {
                Authorization: `Bearer ${auth.accessToken}`,
              },
            },
          );
          console.log("messages", messages);
          //TODO: messges go to chat.messages array

          chat.socket = new WebSocket(
            `ws://127.0.0.1:8000/ws/chat/?token="${auth.accessToken}&id=${chat.chatId}`,
          );
          chat.socket.onmessage = (event) => {
            console.log(`Message from WebSocket ${chat.chatId}:`, event.data);
          };
          chat.socket.onopen = () => {
            console.log(`WebSocket ${chat.chatId} connected`);
          };

          chat.socket.onclose = () => {
            console.log(`WebSocket ${chat.chatId} disconnected`);
          };
          chat.socket.onerror = (error) => {
            console.error(`WebSocket ${chat.chatId} error:`, error);
          };
          myChats.value.push(chat);
        });
      }
    }
  };

  const letsChat = async (user) => {
    if (!auth.user) {
      navigateTo("/auth/login");
    } else {
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
    }
  };

  const toggleChat = () => {
    if (auth.user) {
      showChat.value = !showChat.value;
    }
  };

  const goBackToChatList = () => {
    if (auth.user) {
      showChatList.value = true;
      selectedChatId.value = 0;
    }
  };

  const selectChat = (id) => {
    if (auth.user) {
      selectedChatId.value = id;
      showChatList.value = false;
    }
  };

  return {
    showChat,
    toggleChat,
    showChatList,
    selectedChatId,
    goBackToChatList,
    selectChat,
    getMyChats,
    letsChat,
  };
});
