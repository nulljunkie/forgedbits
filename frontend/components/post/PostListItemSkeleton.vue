<template>
  <div class="border p-2 rounded-md bg-white shadow-sm mb-4">
    <div class="flex flex-row items-center justify-between">
      <USkeleton class="h-6 w-24" :ui="{ rounded: 'rounded' }" />
      <USkeleton class="h-6 w-6 rounded-full" />
    </div>

    <div class="p-4">
      <USkeleton class="h-8 w-full mb-2" :ui="{ rounded: 'rounded' }" />
      <div class="flex flex-row flex-wrap gap-2 p-2">
        <USkeleton class="h-6 w-12 rounded" />
        <USkeleton class="h-6 w-16 rounded" />
        <USkeleton class="h-6 w-10 rounded" />
      </div>
    </div>

    <div class="flex flex-row justify-between items-center">
      <div class="flex items-center gap-2">
        <USkeleton class="h-6 w-6 rounded-full" />
        <USkeleton class="h-6 w-10" />
      </div>

      <div class="flex flex-row mr-4 gap-8 items-center">
        <USkeleton class="h-6 w-6 rounded-full" />
        <USkeleton class="h-6 w-6 rounded-full" />
      </div>
    </div>
  </div>
</template>
