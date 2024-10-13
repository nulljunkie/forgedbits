<template>
  <div class="bg-bg_primary">
    <navbar />
    <div class="min-h-screen max-w-[980px] mx-auto">
      <slot />
    </div>
    <Footer />
  </div>
</template>

<script setup>
import Footer from "../components/ui/Footer.vue";
import navbar from "@/components/ui/nav/navbar.vue";
</script>
