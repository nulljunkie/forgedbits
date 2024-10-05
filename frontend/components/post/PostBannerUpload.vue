<template>
  <div class="">
    <input
      type="file"
      @change="handleFileUpload"
      accept="image/*"
      class="hidden"
      ref="fileInput"
    />
    <div class="flex items-center gap-2">
      <UButton
        @click="triggerFileInput"
        label="Upload a cover"
        icon="i-bx-image-add"
        color="gray"
        variant="outline"
        class="p-2 hover:underline"
      />

      <div>
        <!-- Error Message -->
        <div v-if="errorMessage" class="text-red-500">
          {{ errorMessage }}
        </div>

        <!-- Image Preview -->
        <div
          v-if="previewData"
          class="flex gap-4 items-center border border-gray-200 p-1 text-gray-700 rounded-lg"
        >
          <img
            :src="previewData.src"
            alt="Image Preview"
            class="w-8 h-8 object-cover rounded-md"
          />
          <div class="text-left">
            <p class="text-sm font-semibold">Name: {{ previewData.name }}</p>
            <p class="text-xs">Size: {{ previewData.size }} KB</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

// Refs to manage the file input and preview data
const fileInput = ref(null);
const previewData = ref(null);
const errorMessage = ref("");

const emit = defineEmits(["upload-image"]);

// Function to trigger the file input click
const triggerFileInput = () => {
  fileInput.value.click();
};

// Function to handle the file upload
const handleFileUpload = (event) => {
  // Get the selected file
  const file = event.target.files[0];
  if (!file) return;

  // Reset error message and preview data
  errorMessage.value = "";
  previewData.value = null;

  // Check if the file is an image
  if (!file.type.startsWith("image/")) {
    errorMessage.value = "Please select a valid image file.";
    return;
  }

  // Create an image element to check its dimensions
  const img = new Image();
  img.src = URL.createObjectURL(file);

  img.onload = () => {
    // Check if the image is wide
    if (img.width <= img.height) {
      errorMessage.value = "Please select a wide image (width > height).";
      return;
    }

    // Show preview data
    previewData.value = {
      src: img.src,
      name: file.name,
      size: (file.size / 1024).toFixed(2), // size in KB
    };
    console.log("img: ", img);
    console.log("file: ", file);
    emit("upload-image", file);
  };

  img.onerror = () => {
    errorMessage.value = "There was an error loading the image.";
  };
};

const clearInputFile = () => {
  errorMessage.value = "";
  previewData.value = null;
};

defineExpose({ clearInputFile });
</script>
