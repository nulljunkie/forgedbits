import { defineStore } from "pinia";
import { useAuth } from "#imports";

export const useChat = defineStore("chat", () => {
  const auth = useAuth();

  const showChat = ref(false);
  const showChatList = ref(true);
  const selectedChat = ref({});

  const isConversationOpen = computed(
    () => !showChatList.value && selectedChat.value,
  );

  const myChats = ref([]);

  const playMessageSound = () => {
    const audio = new Audio("/sounds/message.mp3");
    audio
      .play()
      .catch((error) => console.error("error playing chat sound: ", error));
  };

  const getMyChats = async () => {
    myChats.value = [];
    if (auth.user && process.client) {
      try {
        const { data, error } = await useFetch(
          "http://127.0.0.1:8000/api/chat/",
          {
            headers: {
              Authorization: `Bearer ${auth.accessToken}`,
            },
            onResponse({ response }) {
              if (response._data.length) {
                response._data.forEach((obj, index) => {
                  const chat = { messages: [] };
                  chat.chatId = obj.id;
                  chat.user = obj.user.username;
                  chat.image = obj.user.image;
                  chat.ws = handleWebSocket(obj.id, index);
                  myChats.value.push(chat);
                });
              }
            },
          },
        );
      } catch (error) {
        console.error("Error fetching chats:", error);
      }
    }
  };

  const handleWebSocket = (id, index) => {
    const ws = new WebSocket(
      `ws://127.0.0.1:8000/ws/chat/?token=${encodeURIComponent(auth.accessToken)}&chat_id=${encodeURIComponent(id)}`,
    );

    ws.onopen = () => {
      console.log(`WS for chat #${id} connected`);
    };

    ws.onclose = () => {
      console.log(`WS for chat #${id} disconnected`);
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      myChats.value[index].messages.unshift(data.message);
      playMessageSound();
    };

    return ws;
  };

  const getOldMessages = async () => {
    if (auth.user && selectedChat.value.chatId) {
      const messages = await $fetch(
        `http://127.0.0.1:8000/api/chat/messages/${selectedChat.value.chatId}`,
        {
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
        },
      );
      console.log("messages", messages);
      //TODO: implement a caching mechanism
      selectedChat.value.messages = [...messages];
    }
  };

  // FIXME: image and username
  const letsChat = async (user) => {
    if (!auth.user) {
      navigateTo("/auth/login");
    } else {
      const chat = myChats.value.find((obj) => obj.user === user);
      if (chat) {
        showChat.value = true;
        showChatList.value = false;
        selectedChat.value = chat;
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

        const chat = { messages: [] };
        chat.chatId = response.id;
        chat.user = response.user.username;
        chat.image = response.user.image;
        chat.ws = handleWebSocket(response.id, 0);
        myChats.value.unshift(chat);
        selectedChat.value = chat;
        showChat.value = true;
        showChatList.value = false;
      }
    }
  };

  const toggleChat = () => {
    if (auth.user) {
      showChat.value = !showChat.value;
    } else {
      navigateTo("/auth/login");
    }
  };

  const goBackToChatList = () => {
    if (auth.user) {
      showChatList.value = true;
      selectedChat.value = {};
    }
  };

  const selectChat = (chat) => {
    if (auth.user) {
      selectedChat.value = chat;
      showChatList.value = false;
    }
  };

  return {
    showChat,
    myChats,
    toggleChat,
    showChatList,
    selectedChat,
    goBackToChatList,
    getOldMessages,
    selectChat,
    getMyChats,
    letsChat,
    isConversationOpen,
  };
});
