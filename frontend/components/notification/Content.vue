<template>
  <div
    class="absolute right-0 top-8 z-30 w-56 rounded-md bg-white overflow-hidden border shadow-xl divide-gray-500"
  >
    <div
      v-if="notificationStore.items && notificationStore.items.length"
      class="max-h-64 overflow-y-scroll"
    >
      <div class="text-gray-700">
        unread_count: {{ notificationStore.unread_count }}
      </div>
      <div
        v-for="item in notificationStore.items"
        :key="item.id"
        @click="notificationStore.read(item.id)"
        :class="item.is_read ? 'bg-gray-50' : 'bg-gray-200 cursor-pointer'"
        class="flex p-2 gap-2"
      >
        <img :src="item.image" class="bg-gray-300 rounded-full w-6 h-6" />
        <div class="flex flex-col gap-1">
          <p class="text-gray-700 font-thin text-xs">
            {{ item.message }}
          </p>
          <p class="text-gray-500 font-thin text-xs">
            {{ item.created_at }}
          </p>
        </div>
      </div>
      <!-- <div class="text-gray-700">count: {{ notifications.count }}</div> -->
    </div>

    <NotificationEmpty v-else />
  </div>
</template>

<script setup>
import { useAuth } from "#imports";
import { useNotification } from "#imports";

const auth = useAuth();
const notificationStore = useNotification();

await notificationStore.getNotifications();

// const { data: notifications } = await useFetch(
//   "http://127.0.0.1:8000/api/notifications/",
//   {
//     headers: {
//       Authorization: `Bearer ${auth.accessToken}`,
//     },
//   },
// );
//
// const read = async (id) => {
//   const item = notifications.value.items.find((obj) => obj.id === id);
//   if (item && !item.is_read) {
//     console.log("reading item", item.id);
//     item.is_read = true;
//
//     const response = await $fetch(
//       `http://127.0.0.1:8000/api/notifications/${id}/`,
//       {
//         method: "patch",
//         headers: {
//           Authorization: `Bearer ${auth.accessToken}`,
//         },
//         body: {
//           is_read: true,
//         },
//       },
//     );
//   }
// };
</script>
