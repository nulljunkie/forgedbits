<template>
  <div class="sticky top-20">
    <footer>
      <div class="text-center">
        <span class="text-sm text-gray-500 sm:text-center"
          >© 2024
          <NuxtLink class="hover:underline hover:text-black" to="/"
            >forgedbits.io</NuxtLink
          >
          . All Rights Reserved.
        </span>
        <ul class="mt-2 flex items-center justify-evenly text-gray-600 text-xs">
          <li>
            <NuxtLink to="/">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink class="hover:underline" to="/posts/create"
              >Write</NuxtLink
            >
          </li>
          <li v-if="!auth.user">
            <NuxtLink class="hover:underline" to="/auth/login"
              >Sign in</NuxtLink
            >
          </li>
          <li v-if="!auth.user">
            <NuxtLink class="hover:underline" to="/auth/register"
              >Sign up</NuxtLink
            >
          </li>
          <li v-else @click="auth.logout">
            <NuxtLink class="hover:underline" to="/auth/login">logout</NuxtLink>
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
