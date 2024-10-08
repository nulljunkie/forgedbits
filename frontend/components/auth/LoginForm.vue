<template>
  <div class="w-full sm:max-w-md md:mt-0 xl:p-0">
    <div class="p-6 space-y-4 sm:p-8 md:space-y-6">
      <div class="flex flex-col items-center">
        <NuxtLink to="/" class="mb-4">
          <span class="text-3xl font-bold font-rubik text-gray-700"
            >Forged</span
          >
          <span class="text-3xl font-rubik text-gray-400">bits</span></NuxtLink
        >
        <h1
          class="text-xl font-bold tracking-tight leading-tight text-center text-gray-700 md:text-2xl"
        >
          Sign in to your account
        </h1>
        <p class="text-sm font-light text-gray-500">
          Don’t have an account?
          <span class="font-bold hover:underline text-blue_1"
            ><NuxtLink to="/auth/register">Sign up</NuxtLink></span
          >
        </p>
      </div>

      <transition name="shake">
        <div
          v-if="auth.errorMessage"
          class="text-red-500 font-bold text-center"
        >
          {{ auth.errorMessage }}
        </div>
      </transition>

      <form class="mt-6 flex flex-col gap-4" @submit.prevent="handleSubmit">
        <label for="username" class="text-gray-700">
          Username
          <span class="text-red-500">*</span> <br />
          <input
            id="username"
            v-model="username"
            class="flex items-center flex-1 border border-gray-400 rounded-lg w-full p-3 px-4 text-gray-700 bg-white"
            placeholder="username"
            autocomplete="username"
            type="text"
            required
          />
        </label>
        <label for="password" class="text-gray-700">
          Password
          <span class="text-red-500">*</span> <br />
          <div class="relative flex items-center w-full">
            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              @input="handleInputChanged"
              class="flex items-center flex-1 border border-gray-400 rounded-lg w-full p-3 px-4 text-gray-700 bg-white"
              placeholder="********"
              autocomplete="autocomplete"
              required="true"
            />
            <Icon
              name="ion:eye-outline"
              size="20"
              class="absolute cursor-pointer right-4"
              @click="showPassword = !showPassword"
              v-if="showPassword"
            />
            <Icon
              name="ion:eye-off-outline"
              size="20"
              class="absolute cursor-pointer right-4"
              @click="showPassword = !showPassword"
              v-else
            />
          </div>
        </label>
        <button
          class="flex items-center justify-center gap-4 mt-4 text-lg text-white font-bold bg-gray-800 p-3 rounded-lg active:ring-2 active:ring-gray-800"
        >
          <!-- <LoadingIcon v-if="isPending" stroke="4" size="16" color="#fff" /> -->
          <span>{{ buttonText }}</span>
        </button>
      </form>
      <AuthSocialAuth />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuth } from "#imports";

const username = ref("");
const password = ref("");
const showPassword = ref(false);
const buttonText = ref("Login");

const auth = useAuth();

const handleSubmit = async () => {
  try {
    auth.login(username.value, password.value);
  } catch (error) {
    console.error("Login Failed", error);
  }
};
</script>

<style scoped>
.shake-enter-active {
  animation: shake-that-ass 0.2s;
}
@keyframes shake-that-ass {
  0% {
    transform: translateX(0);
  }
  25% {
    transform: translateX(-20px);
  }
  50% {
    transform: translateX(0);
  }
  75% {
    transform: translateX(20px);
  }
  100% {
    transform: translateX(0);
  }
}
</style>
