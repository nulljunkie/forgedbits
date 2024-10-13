<template>
  <div id="profile-page" class="min-h-screen max-w-[1200px] mx-auto">
    <ProfileHeader />
    <div class="flex flex-col md:flex-row mt-[140px] mx-8 gap-6">
      <div class="md:w-1/2">
        <ProfilePersonalInfo />
      </div>
      <div class="md:mt-0 mt-8">
        <ProfileSavedPosts />
        <ProfileLikedPosts />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";

const profile = useProfile();

definePageMeta({
  layout: "basic",
});
</script>
