<template>
  <section class="flex flex-col gap-2 bg-bg_primary">
    <CreateForm />
  </section>
</template>

<script setup lang="ts">
import CreateForm from "../../components/post/CreateForm.vue";

definePageMeta({
  layout: "basic",
});
</script>
