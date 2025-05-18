import { defineStore } from "pinia";
import { useAuth } from "#imports";

export const useNotification = defineStore("notification", () => {
  const auth = useAuth();

  const items = ref([]);
  const unread_count = ref(0);

  const playNotificationSound = () => {
    const audio = new Audio("/sounds/alert.wav");
    audio
      .play()
      .catch((error) => console.error("error playing sound: ", error));
  };

  //NOTE: websocket create upon the init of this fucking pinia store
  const socket = new WebSocket(
    `ws://localhost:8000/ws/notifications/?token=${auth.accessToken}`,
  );

  socket.onmessage = (event) => {
    let data = JSON.parse(event.data);
    console.log("notification from websocket: ", data.notification.message);
    items.value.unshift(data.notification);
    if (!data.notification.is_read) {
      unread_count.value++;
      playNotificationSound();
    }
  };

  socket.onclose = function (event) {
    console.log("WebSocket is closed now.");
  };

  const getUnreadCount = async () => {
    const { data } = await useFetch(
      "http://127.0.0.1:8000/api/notifications/",
      {
        headers: {
          Authorization: `Bearer ${auth.accessToken}`,
        },
      },
    );
    unread_count.value = data.value;
    console.log("unread_count", data.value);
  };

  const getNotifications = async () => {
    const { data } = await useFetch(
      "http://127.0.0.1:8000/api/notifications/",
      {
        headers: {
          Authorization: `Bearer ${auth.accessToken}`,
        },
      },
    );
    items.value = data.value.items;
    unread_count.value = data.value.unread_count;
    console.log("notifications", data.value);
  };

  const read = async (id) => {
    const item = items.value.find((obj) => obj.id === id);
    if (item && !item.is_read && unread_count.value) {
      console.log("reading item", item.id);
      const response = await $fetch(
        `http://127.0.0.1:8000/api/notifications/${id}/`,
        {
          method: "patch",
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: {
            is_read: true,
          },
        },
      );
      item.is_read = true;
      unread_count.value--;
    }
  };

  return {
    items,
    unread_count,
    getNotifications,
    getUnreadCount,
    read,
  };
});
