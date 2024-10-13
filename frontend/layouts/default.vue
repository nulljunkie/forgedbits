<template>
  <div class="bg-bg_primary">
    <navbar />
    <div
      class="flex flex-row gap-4 min-h-screen max-w-[1200px] mx-auto mt-8 px-4"
    >
      <div class="hidden md:block">
        <navleft />
      </div>
      <div class="w-full">
        <slot />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import Footer from "../components/ui/Footer.vue";
import navbar from "@/components/ui/nav/navbar.vue";
import navleft from "@/components/ui/aside/navleft.vue";
import UsersBar from "../components/ui/UsersBar.vue";
</script>
