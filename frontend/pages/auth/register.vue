<template>
  <div class="flex justify-center items-center mt-16">
    <RegisterFrom />
  </div>
</template>

<script setup>
import RegisterFrom from "../../components/auth/RegisterFrom.vue";

definePageMeta({
  layout: "basic",
});
</script>
