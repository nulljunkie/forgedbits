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
            {{ formatDate(new Date(item.created_at)) }}
          </p>
        </div>
      </div>
    </div>

    <NotificationEmpty v-else />
  </div>
</template>

<script setup>
import { useAuth } from "#imports";
import { useNotification } from "#imports";
import { formatDate } from "@/utils/dateFns.js";

const auth = useAuth();
const notificationStore = useNotification();

await notificationStore.getNotifications();
</script>
