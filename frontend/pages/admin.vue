<script setup>
definePageMeta({
  layout: "basic",
});
</script>

<template>
  <div
    class="p-32 relative h-screen flex items-center justify-center bg-orange-300"
  >
    <div
      class="p-32 relative h-full w-full flex items-center justify-center bg-sky-300"
    >
      <div
        class="p-32 relative h-full w-full flex items-center justify-center bg-violet-300"
      >
        <div
          class="p-32 relative h-full w-full flex items-center justify-center bg-red-300"
        >
          <div class="fixed bg-gray-400 inset-0 h-48 w-48 z-50"></div>
        </div>
      </div>
    </div>
  </div>
</template>
