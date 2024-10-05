<template>
  <div class="min-h-screen max-w-[1200px] mx-auto">
    <ProfilePicture />
    <div class="flex flex-col md:flex-row mt-[140px] mx-8 gap-6">
      <div class="md:w-1/2">
        <PersonalInfo />
      </div>
      <div class="md:mt-0 mt-8">
        <SavedPosts />
        <LikedPosts />
      </div>
    </div>
  </div>
</template>

<script setup>
import PersonalInfo from "~/components/profile/PersonalInfo.vue";
import ProfilePicture from "~/components/profile/ProfilePicture.vue";
import SavedPosts from "~/components/profile/SavedPosts.vue";
import LikedPosts from "~/components/profile/LikedPosts.vue";
import { useProfile } from "#imports";

const profile = useProfile();

definePageMeta({
  layout: "basic",
});
</script>
