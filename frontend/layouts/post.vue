<template>
  <div class="bg-bg_primary">
    <NuxtLoadingIndicator color="#ff0000" height="5" />
    <NuxtRouteAnnouncer />
    <navbar />
    <div class="max-w-[800px] mx-auto flex justify-center my-8">
      <slot />
    </div>
    <Footer />
    <UNotifications />
  </div>
</template>

<script setup>
import Footer from "../components/ui/Footer.vue";
import navbar from "@/components/ui/nav/navbar.vue";
</script>
