<template>
  <div class="bg-bg_primary">
    <NuxtLoadingIndicator color="#ff0000" height="5" />
    <NuxtRouteAnnouncer />
    <navbar />
    <div class="min-h-screen max-w-[980px] mx-auto">
      <slot />
    </div>
    <div>
      <Footer />
    </div>
    <div>
      <UNotifications />
    </div>
  </div>
</template>

<script setup>
import Footer from "../components/ui/Footer.vue";
import navbar from "@/components/ui/nav/navbar.vue";
</script>
