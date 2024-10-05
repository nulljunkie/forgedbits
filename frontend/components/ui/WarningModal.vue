<script setup>
const isOpen = ref(false);
const error = ref(true);

const router = useRouter();

router.beforeRouteLeave((to, from, next) => {
  if (error.value) next(false);
  else next();
});
</script>

<template>
  <div>
    <UButton label="Open" @click="isOpen = true" />

    <UModal v-model="isOpen" prevent-close>
      <div class="h-48 w-full flex flex-col items-center justify-center">
        <UIcon name="i-fe-warning" class="w-20 h-20 text-red-500 mb-2" />
        <p class="text-gray-600 mb-2">Are you sure you want to exit?</p>
        <div class="space-x-4">
          <UButton @click="isOpen = false" label="Keep editing" color="gray" />
          <UButton @click="isOpen = false" label="Discard" color="red" />
        </div>
      </div>
    </UModal>
  </div>
</template>
