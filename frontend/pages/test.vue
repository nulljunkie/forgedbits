<template>
  <div
    class="bg-white text-black flex flex-col h-screen items-center pt-28 gap-4"
  >
    <h1 class="text-blue-500 font-extrabold text-4xl">
      testing notifiction websocket
    </h1>
    <transition-group name="list" tag="ul" class="space-y-4">
      <li
        class="bg-slate-100 rounded-md p-4 w-full text-center text-gray-700 text-lg"
        v-for="notification in notifications"
        :key="notification.id"
      >
        {{ notification.notification }}
      </li>
    </transition-group>

    <button class="bg-blue-500 rounded-md px-4 py-2 text-white">
      Change user
    </button>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();

const notifications = ref([]);

const socket = new WebSocket(
  `ws://localhost:8000/ws/notifications/?token=${auth.accessToken}`,
);

socket.onmessage = function (event) {
  let data = JSON.parse(event.data);
  notifications.value.push(data);
  console.log(data.notification);
};

socket.onclose = function (event) {
  console.log("WebSocket is closed now.");
};

definePageMeta({
  layout: "basic",
});
</script>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
