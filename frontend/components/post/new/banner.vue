<template>
  <div>
    <div class="flex gap-4">
      <label
        for="file-input"
        class="bg-gray-100 h-12 px-4 py-2 border border-gray-500 rounded-md text-gray-700"
      >
        <div class="flex items-center gap-1">
          <Icon name="bx:image-add" size="24" />
          <span>Upload a cover</span>
        </div>
        <input
          type="file"
          @change="handleFileUpload"
          accept="image/*"
          class="hidden"
          ref="inputRef"
          id="file-input"
        />
      </label>
      <div v-if="croppedCoverUrl" class="relative">
        <img
          :src="croppedCoverUrl"
          class="h-20 border border-gray-300 rounded-md"
        />
        <button
          @click="removeCover"
          class="absolute h-6 w-6 top-0 right-0 text-red-600 rounded-full border border-red-600 bg-red-100 hover:bg-red-200"
        >
          <Icon name="material-symbols:close" size="24" />
        </button>
      </div>
    </div>

    <ClientOnly>
      <Teleport to="#create-page">
        <ImageCropper
          v-if="coverUrl"
          @sendBlob="uploadCroppedCover"
          @cancelCrop="coverUrl = ''"
          :imageUrl="coverUrl"
          cropWidth="530"
          cropHeigth="200"
        />
      </Teleport>
    </ClientOnly>
  </div>
</template>

<script setup>
/*
    1. get image from input elem
    2. get url of image
    3. copper (url, w, h)
    4. grap blob from sendBlob event
    5. get url of blob for displaying
    6. send blob to prent in event upload-image
*/

import ImageCropper from "@/utils/ImageCropper.vue";

const inputRef = ref(null);
const coverUrl = ref("");
const croppedCoverUrl = ref("");

const emit = defineEmits(["upload-cover", "remove-cover"]);

// NOTE: we didn't use inputRef.value.files
//       we used instead @change='handler', pass event to handler
const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    coverUrl.value = URL.createObjectURL(file);
  }
};

const uploadCroppedCover = (blob) => {
  if (blob) {
    croppedCoverUrl.value = URL.createObjectURL(blob);
    emit("upload-cover", blob);
  }
};

const clearInputFile = () => {
  coverUrl.value = "";
  croppedCoverUrl.value = "";
  inputRef.value.value = "";
};

const removeCover = () => {
  emit("remove-cover");
  clearInputFile();
};

defineExpose({ removeCover });

// const previewData = ref(null);
// const errorMessage = ref("");
//
// const emit = defineEmits(["upload-image"]);
//
// const triggerFileInput = () => {
//   fileInput.value.click();
// };
//
// const handleFileUpload = (event) => {
//   const file = event.target.files[0];
//   if (!file) return;
//
//   errorMessage.value = "";
//   previewData.value = null;
//
//   if (!file.type.startsWith("image/")) {
//     errorMessage.value = "Please select a valid image file.";
//     return;
//   }
//
//   // Create an image element to check its dimensions
//   const img = new Image();
//   img.src = URL.createObjectURL(file);
//
//   img.onload = () => {
//     // Check if the image is wide
//     if (img.width <= img.height) {
//       errorMessage.value = "Please select a wide image (width > height).";
//       return;
//     }
//
//     // Show preview data
//     previewData.value = {
//       src: img.src,
//       name: file.name,
//       size: (file.size / 1024).toFixed(2), // size in KB
//     };
//     console.log("img: ", img);
//     console.log("file: ", file);
//     emit("upload-image", file);
//   };
//
//   img.onerror = () => {
//     errorMessage.value = "There was an error loading the image.";
//   };
// };
//
// const clearInputFile = () => {
//   errorMessage.value = "";
//   previewData.value = null;
// };
//
// defineExpose({ clearInputFile });
</script>
