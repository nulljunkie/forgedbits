<template>
  <div class="bg-bg_primary">
    <NuxtLoadingIndicator color="#ff0000" height="5" />
    <NuxtRouteAnnouncer />
    <Navbar />
    <div
      class="flex flex-row gap-4 min-h-screen max-w-[1200px] mx-auto mt-8 px-4"
    >
      <div class="hidden md:block">
        <div class="sticky top-20 p-2 shadow-md rounded-md bg-white">
          <SideBar />
        </div>
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
import Navbar from "../components/ui/Navbar.vue";
import SideBar from "../components/ui/SideBar.vue";
import UsersBar from "../components/ui/UsersBar.vue";
</script>
