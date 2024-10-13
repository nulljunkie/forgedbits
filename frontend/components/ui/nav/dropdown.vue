<template>
  <div class="relative">
    <button
      @click="toggleDropdown"
      ref="profileButton"
      class="focus:outline-none"
    >
      <img
        :src="profile.image"
        alt="Profile"
        class="w-10 h-10 border-2 border-gray-500 rounded-full"
      />
    </button>

    <div
      v-if="isDropdownOpen"
      class="absolute z-20 right-[-8px] w-52 bg-white rounded-sm shadow-xl border border-gray-200"
    >
      <UiNavDropdownlink
        link="/profile"
        icon="bx:user"
        :value="profile.username"
      />
      <hr class="bg-black m-2" />
      <UiNavDropdownlink link="/settings" icon="bx:cog" value="Settings" />
      <hr class="bg-black m-2" />
      <UiNavDropdownlink
        link="/posts/create"
        icon="bx:edit"
        value="Create post"
      />
      <UiNavDropdownlink link="/posts/me" icon="bx:archive" value="My posts" />

      <hr class="bg-black m-2" />
      <button
        @click="auth.logout"
        class="text-red-500 bg-red-50 hover:bg-red-100 px-4 py-2 w-full"
      >
        <span class="flex items-center gap-2">
          <Icon name="bx-exit" size="20" />
          <span>Sign out </span>
        </span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import { useAuth } from "#imports";

const profile = useProfile();
const auth = useAuth();

await profile.get();

const isDropdownOpen = ref(false);
const profileButton = ref(null);

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value;
};

const closeDropdown = (event) => {
  if (isDropdownOpen.value && !profileButton.value.contains(event.target)) {
    isDropdownOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener("click", closeDropdown);
});

onBeforeUnmount(() => {
  document.removeEventListener("click", closeDropdown);
});
</script>
