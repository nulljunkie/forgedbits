<template>
  <button
    @click="authWithGithub"
    class="flex gap-2 items-center justify-center h-12 w-full bg-gray-800 text-white border border-gray-800 font-bold rounded-md active:scale-[102%] transition ease-in"
  >
    <Icon name="i-simple-icons-github" size="20" />
    <p>Continue with Github</p>
  </button>
</template>

<script setup>
const authWithGithub = async () => {
  const response = await $fetch(
    "http://127.0.0.1:8000/api/users/oauth2/github/",
  );
  console.log(response);
  navigateTo(response.oauth_url, { external: true });
};
</script>
