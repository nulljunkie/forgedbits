<template>
  <div class="my-4">
    <label for="tag-input" class="block text-gray-700 font-bold mb-2"
      >Tags</label
    >
    <div class="rounded-lg p-2 flex flex-wrap items-center gap-2">
      <!-- Existing Tags -->
      <div
        v-for="(tag, index) in tags"
        :key="index"
        class="bg-gray-100 text-gray-600 flex items-center gap-1 px-2 py-1 rounded-full"
      >
        <span>{{ tag }}</span>
        <button
          @click="removeTag(index)"
          class="text-red-500 font-bold hover:text-red-700"
        >
          x
        </button>
      </div>

      <input
        id="tag-input"
        v-model="newTag"
        @keyup.enter="addTag"
        placeholder="Type and press Enter to add a tag"
        class="border-none outline-none flex-grow px-2 py-1"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const tags = ref([]);
const newTag = ref("");

const emit = defineEmits(["select-tags"]);

const addTag = () => {
  const trimmedTag = newTag.value.trim();
  if (trimmedTag && !tags.value.includes(trimmedTag)) {
    tags.value.push(trimmedTag);
    newTag.value = "";
  }
  emit("select-tags", tags.value);
};

const removeTag = (index) => {
  tags.value.splice(index, 1);
  emit("select-tags", tags.value);
};

const clearTags = () => {
  tags.value = [];
};

defineExpose({ clearTags });
</script>
