<template>
  <div class="flex justify-center items-center mt-16">
    <LoginForm />
  </div>
</template>

<script setup>
import LoginForm from "~/components/auth/LoginForm.vue";

definePageMeta({
  layout: "basic",
});
</script>
