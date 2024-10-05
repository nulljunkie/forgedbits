<template>
  <div class="">
    <!-- File Input -->
    <input
      type="file"
      @change="handleFileUpload"
      accept="image/*"
      class="hidden"
      ref="fileInput"
    />
    <button @click="triggerFileInput" class="btn-upload">Select Image</button>

    <!-- Error Message -->
    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>

    <!-- Image Preview -->
    <div v-if="previewData" class="image-preview">
      <img :src="previewData.src" alt="Image Preview" class="preview-image" />
      <div class="preview-info">
        <p><strong>Name:</strong> {{ previewData.name }}</p>
        <p><strong>Size:</strong> {{ previewData.size }} KB</p>
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
  };

  img.onerror = () => {
    errorMessage.value = "There was an error loading the image.";
  };
};
</script>

<style scoped>
.image-uploader {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
}

.btn-upload {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  font-weight: bold;
}

.error-message {
  margin-top: 10px;
  color: red;
}

.image-preview {
  margin-top: 20px;
  display: flex;
  align-items: center;
  gap: 20px;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 4px;
}

.preview-image {
  width: 50px;
  height: 50px;
  object-fit: cover;
  border-radius: 4px;
}

.preview-info {
  text-align: left;
}

.preview-info p {
  margin: 0;
}
</style>
