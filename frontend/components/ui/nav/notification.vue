<template>
  <button
    v-if="auth.user"
    @click="navigateTo('/test')"
    class="relative w-6 h-6"
  >
    <UIcon
      name="i-material-symbols-notifications-outline-rounded"
      class="w-6 h-6 text-gray-700"
    />
    <div class="absolute top-0 right-0 h-2 w-2 bg-red-500 rounded-full"></div>
  </button>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();
</script>
