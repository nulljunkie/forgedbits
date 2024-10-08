<template>
  <div class="container sm:max-w-6xl mx-auto px-4">
    <footer class="text-gray-700">
      <div
        class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between"
      >
        <span class="text-sm text-gray-500 sm:text-center"
          >© 2024
          <NuxtLink class="hover:underline hover:text-black" to="/"
            >forgedbits.io</NuxtLink
          >
          . All Rights Reserved.
        </span>
        <ul
          class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 sm:mt-0"
        >
          <li>
            <NuxtLink class="p-2 hover:text-gray-700" to="/">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink class="p-2 hover:text-gray-700" to="/posts/create"
              >Write</NuxtLink
            >
          </li>
          <li v-if="!auth.user">
            <NuxtLink class="p-2 hover:text-gray-700" to="/auth/login"
              >Sign in</NuxtLink
            >
          </li>
          <li v-if="!auth.user">
            <NuxtLink class="p-2 hover:text-gray-700" to="/auth/register"
              >Sign up</NuxtLink
            >
          </li>
          <li v-else @click="auth.logout" class="p-2 mx-2 hover:text-gray-700">
            <NuxtLink to="/auth/login">logout</NuxtLink>
          </li>
        </ul>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";

const auth = useAuth();
</script>
