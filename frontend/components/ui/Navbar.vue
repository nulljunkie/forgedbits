<script setup>
import { useAuth } from "#imports";
import { useProfile } from "#imports";
import { ref } from "vue";
import NavbarProfile from "./NavbarProfile.vue";
import ProfileDropDown from "./ProfileDropDown.vue";
import SearchBar from "./SearchBar.vue";

const auth = useAuth();
const profile = useProfile();

const profileDropDownToggle = ref(false);

const createPost = () => {
  navigateTo("/posts/create");
};
</script>

<template>
  <div class="sticky top-0 z-10 bg-white border-b shadow-sm">
    <header class="container sm:max-w-6xl mx-auto py-1 px-4">
      <nav class="flex flex-row justify-between items-center">
        <div class="flex flex-row items-center gap-6">
          <NuxtLink to="/" class="ml-4">
            <span class="text-2xl font-bold font-rubik text-gray-700"
              >Forged</span
            >
            <span class="text-2xl font-rubik text-gray-400"
              >bits</span
            ></NuxtLink
          >

          <SearchBar />
        </div>

        <ul class="flex flex-row items-center gap-3">
          <li>
            <UButton
              v-if="auth.user"
              @click="createPost"
              icon="i-heroicons-pencil-square"
              label="Write"
              class="text-gray-700 bg-white hover:bg-gray-700 border border-gray-700 hover:text-white py-2"
            />
          </li>
          <li>
            <UButton
              v-if="!auth.user"
              @click="navigateTo('/auth/login')"
              icon="ic-baseline-log-in"
              label="Login"
              class="text-gray-700 bg-white hover:bg-gray-700 border border-gray-700 hover:text-white py-2"
            />
          </li>
          <li>
            <UButton
              v-if="!auth.user"
              @click="navigateTo('/auth/register')"
              label="Sign up"
              class="text-white bg-gray-700 hover:bg-white border border-gray-700 hover:text-gray-700 py-2"
            />
          </li>
          <UChip
            v-if="auth.user"
            size="xs"
            color="red"
            :ui="{
              translate: {
                'top-right':
                  'translate-y-[8px] -translate-x-[8px] transform z-2',
              },
            }"
          >
            <UButton
              icon="i-material-symbols-notifications-outline-rounded"
              @click=""
              color="black"
              variant="ghost"
              class="text-4xl"
            />
          </UChip>

          <ProfileDropDown v-if="auth.user" />
        </ul>
      </nav>
    </header>
  </div>
</template>
