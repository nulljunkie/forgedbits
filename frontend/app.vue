<template>
  <NuxtLayout>
    <NuxtLoadingIndicator color="#ff0000" height="5" />
    <NuxtRouteAnnouncer />
    <NuxtPage />
    <UNotifications />
    <Chat />
  </NuxtLayout>
</template>

<script setup>
import Chat from "@/components/chat/Chat.vue";
</script>
