<template>
  <div
    ref="notificationComp"
    class="relative flex items-center justify-center rounded-full h-7 w-7 overflow-visible"
  >
    <button @click="show = !show" class="relative w-6 h-6 rounded-full">
      <UIcon
        name="i-material-symbols-notifications-outline-rounded"
        class="w-6 h-6 text-gray-700"
      />
      <div
        v-show="notificationStore.unread_count"
        class="absolute top-0 right-0 z-20 h-2 w-2 bg-red-500 rounded-full"
      ></div>
    </button>
    <NotificationContent v-if="show" />
  </div>
</template>

<script setup>
const show = ref(false);
const notificationComp = ref(null);

import { useNotification } from "#imports";

const notificationStore = useNotification();

await notificationStore.getUnreadCount();

// for closing dropdown
const closeDropdown = (event) => {
  if (show.value && !notificationComp.value.contains(event.target)) {
    show.value = false;
  }
};

onMounted(() => {
  document.addEventListener("click", closeDropdown);
});

onBeforeUnmount(() => {
  document.removeEventListener("click", closeDropdown);
});
</script>
