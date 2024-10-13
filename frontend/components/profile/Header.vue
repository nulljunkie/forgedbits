<template>
  <div>
    <div class="relative">
      <!-- Banner -->

      <div
        class="relative flex items-center justify-center overflow-hidden h-48 bg-slate-200"
      >
        <img
          :src="profile.banner"
          alt="upload your banner"
          class="w-full text-gray-400 text-4xl text-center"
        />

        <label
          for="banner"
          class="absolute right-0 bottom-0 transform -translate-x-1 -translate-y-1 rounded-full border border-black bg-white"
        >
          <div class="flex items-center justify-center size-auto">
            <Icon name="i-material-symbols-ink-pen-outline" size="36" />
            <input
              id="banner"
              type="file"
              @change="onBannerSelected"
              class="hidden"
            />
          </div>
        </label>
      </div>

      <!-- Avatar -->
      <div class="absolute top-32 transform translate-x-1/4">
        <div class="relative">
          <UAvatar
            :src="profile.image"
            :alt="profile.username"
            :ui="{
              size: {
                xxl: 'h-40 w-40 text-6xl bg-gray-200',
              },
            }"
            size="xxl"
            class="border border-gray-800 font-extrabold text-gray-800"
          />

          <label
            for="avatar"
            class="absolute right-0 bottom-0 transform -translate-y-3 -translate-x-2 rounded-full border border-black bg-white"
          >
            <div class="flex items-center justify-center size-auto">
              <Icon name="i-material-symbols-ink-pen-outline" size="36" />
              <input
                id="avatar"
                type="file"
                @change="onAvatarSelected"
                class="hidden"
              />
              <ClientOnly>
                <Teleport to="#profile-page">
                  <ImageCropper
                    v-if="avatarUrl"
                    @sendBlob="uploadCroppedAvatar"
                    @cancelCrop="avatarUrl = ''"
                    :imageUrl="avatarUrl"
                    cropWidth="280"
                    cropHeigth="280"
                  />
                </Teleport>
              </ClientOnly>
            </div>
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";
import ImageCropper from "@/utils/ImageCropper.vue";

const profile = useProfile();

const avatarUrl = ref("");

const onAvatarSelected = (event) => {
  const file = event.target.files[0];
  if (file) {
    avatarUrl.value = URL.createObjectURL(file);
  }

  // if (file) {
  //   await profile.uploadProfileImage(file, null);
  // }
};

console.log(ImageCropper);

const uploadCroppedAvatar = async (blob) => {
  if (blob) {
    console.log("blob: ", blob);
    await profile.uploadProfileImage(blob, null);
  }
};

const onBannerSelected = async (event) => {
  const file = event.target.files[0];
  if (file) {
    await profile.uploadProfileImage(null, file);
  }
};
</script>
