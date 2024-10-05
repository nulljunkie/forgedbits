<template>
  <div class="bg-bg_primary">
    <NuxtLoadingIndicator color="#ff0000" height="5" />
    <NuxtRouteAnnouncer />
    <Navbar />
    <div class="max-w-[800px] mx-auto flex justify-center my-8">
      <slot />
    </div>
    <Footer />
    <UNotifications />
  </div>
</template>

<script setup>
import Footer from "../components/ui/Footer.vue";
import Navbar from "../components/ui/Navbar.vue";
</script>
