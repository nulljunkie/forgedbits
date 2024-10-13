<template>
  <div class="space-y-4">
    <div class="w-full flex items-center justify-stretch gap-2 text-gray-700">
      <hr class="border-gray-500 w-full" />
      <p class="">OR</p>
      <hr class="border-gray-500 w-full" />
    </div>

    <AuthOauth2Github />

    <button
      class="flex gap-2 items-center justify-center h-12 w-full bg-white-800 border border-gray-700 text-gray-700 font-bold rounded-md active:scale-[102%] transition ease-in"
    >
      <Icon name="devicon-google" size="20" />
      <p>Continue with Google</p>
    </button>
  </div>
</template>
