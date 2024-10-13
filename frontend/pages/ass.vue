<template>
  <div
    class="card max-w-sm mx-auto rounded-lg shadow-lg overflow-hidden bg-white"
  >
    <!-- Cover Image with Gradient -->
    <div class="relative">
      <img
        class="w-full h-auto"
        src="https://picsum.photos/seed/picsum/400/200"
        alt="Cover Image"
      />
      <div class="gradient-overlay"></div>
    </div>

    <!-- Card Content -->
    <div class="px-4 pb-4">
      <h2 class="text-gray-700 text-lg font-bold">Exploring Tailwind CSS</h2>
      <p class="text-gray-500 text-sm">By John Smith</p>
      <p class="text-gray-700 my-2">
        Tailwind CSS is a utility-first CSS framework that provides low-level
        utility classes.
      </p>

      <!-- Stats -->
      <div class="stats flex justify-between text-gray-500 text-sm mt-3">
        <span class="">💬 8 Comments</span>
        <span class="">❤️ 20 Likes</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.cover-image {
  display: block; /* Removes space below the image */
}

.gradient-overlay {
  background: linear-gradient(to top, white, transparent); /* Gradient effect */
}
</style>
