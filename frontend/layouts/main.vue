<template>
  <div class="bg-bg_primary">
    <NuxtLoadingIndicator color="#ff0000" height="5" />
    <NuxtRouteAnnouncer />
    <navbar />
    <div
      class="flex flex-row gap-4 min-h-screen max-w-[1200px] mx-auto mt-3 px-4"
    >
      <div class="hidden md:block">
        <navleft />
      </div>
      <div class="w-full">
        <slot />
      </div>
      <div class="hidden lg:block w-[480px] space-y-4">
        <div class="shadow-md rounded-md bg-white">
          <UsersBar />
        </div>
        <div class="sticky top-16 shadow-md rounded-md bg-white">
          <UsersBar />
        </div>
      </div>
    </div>
    <Footer />
    <UNotifications />
  </div>
</template>

<script setup>
import Footer from "../components/ui/Footer.vue";
import UsersBar from "../components/ui/UsersBar.vue";
import navleft from "@/components/ui/aside/navleft.vue";
import navbar from "@/components/ui/nav/navbar.vue";
</script>
