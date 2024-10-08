<template>
  <div class="sticky top-0 z-10 bg-white border-b shadow-sm">
    <header class="container sm:max-w-6xl mx-auto py-2 px-4">
      <nav class="flex flex-row justify-between items-center">
        <div class="flex flex-row items-center gap-6">
          <UiNavLogo />
          <UiNavSearch />
        </div>

        <ul class="flex flex-row items-center gap-3">
          <li>
            <button
              v-if="auth.user"
              @click="createPost"
              class="group hidden md:block text-gray-700 bg-white rounded-md h-10 px-3 hover:bg-gray-700 border border-gray-700 hover:text-white"
            >
              <div class="flex items-center">
                <UIcon name="i-heroicons-pencil-square" class="w-5 h-5" />
                <div class="group-hover:underline">Write</div>
              </div>
            </button>
          </li>
          <li>
            <button
              v-if="!auth.user"
              @click="navigateTo('/auth/login')"
              type="button"
              class="h-10 px-2 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-black bg-gray-50 text-gray-800 hover:bg-gray-100"
            >
              <div class="flex items-center gap-1">
                <Icon name="material-symbols:login" size="24" />
                <div class="font-bold">Login</div>
              </div>
            </button>
          </li>
          <li>
            <button
              v-if="!auth.user"
              @click="navigateTo('/auth/register')"
              type="button"
              class="h-10 px-3 inline-flex items-center gap-x-2 text-sm font-bold rounded-lg border border-gray-900 bg-gray-800 text-white hover:bg-gray-900 focus:outline-none focus:bg-gray-900"
            >
              Sign up
            </button>
          </li>

          <UiNavNotification />
          <UiNavDropdown v-if="auth.user" />
        </ul>
      </nav>
    </header>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";
import { useProfile } from "#imports";

const auth = useAuth();
const profile = useProfile();

const profileDropDownToggle = ref(false);

const createPost = () => {
  navigateTo("/posts/create");
};
</script>
