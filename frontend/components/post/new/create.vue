<template>
  <div class="flex flex-row justify-between items-center">
    <div class="text-xl text-gray-700">Create post</div>
    <div class="flex flex-fow justify-between items-center">
      <UButton
        @click="navigateTo('/posts/post/3')"
        size="sm"
        color="blue"
        variant="link"
        label="first time using markdown?"
        :trailing="false"
        class="m-2 inline-block"
      />
      <UButton
        @click="preview = false"
        icon="i-heroicons-pencil-square"
        size="sm"
        color="rose"
        variant="link"
        label="Edit"
        :trailing="false"
      />
      <UButton
        @click="togglePreview"
        icon="i-material-symbols-visibility-outline-rounded"
        size="sm"
        color="rose"
        variant="link"
        label="Preview"
        :trailing="false"
      />
    </div>
  </div>
  <div class="p-8 h-auto border-2 rounded-md bg-white">
    <div v-if="!preview">
      <PostNewBanner
        ref="coverPost"
        @upload-cover="handleCover"
        @remove-cover="removeCover"
      />

      <input
        v-model="title"
        name="title"
        placeholder="New post title here..."
        class="bg-white text-3xl text-gray-700 my-4 p-2 focus:outline-none"
      />

      <div class="border border-gray-400 rounded-lg pt-4">
        <PostEditor v-model="content" />
      </div>

      <PostNewTags ref="tagsRef" @select-tags="handleTags" />
    </div>

    <!-- render preview -->
    <PostEditorPreview v-else :title="title" :content="content" :tags="tags" />

    <div class="flex flex-row items-center gap-4">
      <button
        @click="submitPost"
        class="bg-gray-700 py-2 px-4 text-white font-bold border border-gray-700 rounded-lg hover:bg-gray-800 hover:border-gray-800 transform active:scale-[102%]"
      >
        <div class="flex items-center gap-1">
          <Icon name="material-symbol:publish" size="24" />
          <span>Publish</span>
        </div>
      </button>

      <button
        @click=""
        class="bg-gray-50 py-2 px-4 text-gray-700 font-bold border border-gray-700 rounded-lg hover:bg-gray-100 hover:border-gray-800 transform active:scale-[102%]"
      >
        <div class="flex items-center gap-1">
          <Icon name="ci:save" size="24" />
          <span>Save draft</span>
        </div>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { usePost } from "#imports";
import { addSuccessToast, addErrorToast } from "/utils/toast.js";

const title = ref("");
const content = ref("");
const preview = ref(false);
const coverImage = ref(null);
const tagList = ref([]);
const isDraft = ref(false);

const coverPost = ref(null);
const tagsRef = ref(null);

const postStore = usePost();
const toast = useToast();

const handleCover = (img) => {
  coverImage.value = img;
  console.log("coverImage [1]: ", coverImage.value);
  console.log("coverImage [1]: ", img);
};

const removeCover = () => {
  coverImage.value = "";
  console.log("coverImage [3]: ", coverImage.value);
};

const handleTags = (tags) => {
  tagList.value = tags;
};

const clearAllTags = () => {
  if (tagsRef.value) {
    tagsRef.value.clearTags();
  }
};

const clearFile = () => {
  if (coverPost.value) {
    // coverPost.value.clearInputFile();
    coverPost.value.removeCover();
  }
};

const submitPost = async () => {
  if (title.value && content.value) {
    const formData = new FormData();
    if (coverImage.value) {
      console.log("coverImage [2]: ", coverImage.value);
      formData.append("cover", coverImage.value, "cover.jpeg");
    }
    formData.append("title", title.value);
    formData.append("content", content.value);
    formData.append("tags", JSON.stringify(tagList.value));
    formData.append("is_draft", isDraft.value);

    console.log(formData);
    try {
      await postStore.addPost(formData);
      addSuccessToast("Done", "published Successfully");
      title.value = "";
      content.value = "";
      tagList.value = [];
      clearAllTags();
      clearFile();
      coverImage.value = null;
    } catch (error) {
      addErrorToast("Error", "publishing Failed");
      console.error("publish error: ", error);
    }
  } else {
    addErrorToast("Error", "Your post is incomplete");
  }
};

// handle rendering md for preview
const togglePreview = () => {
  if (content.value || title.value) preview.value = true;
};
</script>
