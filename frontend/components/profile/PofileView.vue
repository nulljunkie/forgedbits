<script setup>
import { ref } from "vue";
import { useAuth } from "#imports";
import { useProfile } from "#imports";
import ProfileEdit from "./ProfileEdit.vue";

const auth = useAuth();
const profile = useProfile();

const isEdit = ref(false);

onMounted(async () => {
  if (auth.user) {
    await profile.get();
  }
});
</script>

<template>
  <div class="flex flex-col items-center">
    <h1 class="text-6xl m-4 text-gray-600 font-rubik font-bold">
      {{ auth.user }}
    </h1>
    <div>
      <img class="size-48 rounded-full" :src="profile.image" />
    </div>
    <div>
      <label class="text-lg font-bold text-gray-800" for="bio">Bio:</label>
      <article class="font-thin text-gray-700" id="bio">
        {{ profile.bio }}
      </article>
    </div>

    <div>
      <button
        @click="isEdit = true"
        class="text-2xl py-1 px-2 m-2 font-semibold text-green-600 border border-green-600 rounded-md hover:text-white hover:bg-green-600 active:outline active:outline-green-600"
      >
        Edit
      </button>
      <button
        class="text-2xl py-1 px-2 m-2 font-semibold text-red-600 border border-red-600 rounded-md hover:text-white hover:bg-red-600 active:outline active:outline-red-600"
      >
        Delete
      </button>
    </div>
    <ProfileEdit
      v-if="isEdit"
      @cancelEdit="isEdit = false"
      @submited="isEdit = false"
    />
  </div>
</template>
