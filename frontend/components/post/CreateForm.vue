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
      <PostBannerUpload ref="coverPost" @upload-image="handleImage" />

      <!-- title -->
      <UInput
        v-model="title"
        :padded="true"
        name="title"
        placeholder="New post title here..."
        variant="none"
        :ui="{
          size: { xxxl: 'text-3xl' },
          //TODO: add custom ui attributes
          font: { bold: 'text-red-600', semibold: 'font-semibold' },
        }"
        class="w-full p-2 my-4"
        size="xxxl"
        font="bold"
      />
      <div class="border border-gray-400 rounded-lg pt-4">
        <MarkdownEditor v-model="content" />
      </div>

      <PostAddTags ref="tagsRef" @select-tags="handleTags" />
    </div>

    <!-- render preview -->
    <LoadPreview v-else :title="title" :content="content" :tags="tags" />
    <div class="flex flex-row items-center gap-4">
      <UButton
        @click="submitPost"
        label="Publish"
        icon="material-symbols-publish"
        class="text-white bg-gray-700 border border-gray-700 py-2 hover:text-white hover:bg-gray-700 active:ring-2 active:ring-gray-700"
      />
      <UButton
        @click=""
        label="Save draft"
        icon="ci-save"
        class="text-gray-700 bg-white hover:bg-gray-700 border border-gray-700 hover:text-white py-2"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import LoadPreview from "./LoadPreview.vue";
import MarkdownEditor from "./MarkdownEditor.vue";
import PostBannerUpload from "./PostBannerUpload.vue";
import PostAddTags from "./PostAddTags.vue";
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

const handleImage = (img) => {
  coverImage.value = img;
  console.log("coverImage: ", coverImage.value);
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
    coverPost.value.clearInputFile();
  }
};

const submitPost = async () => {
  if (title.value && content.value) {
    const formData = new FormData();
    if (coverImage.value) {
      formData.append("cover", coverImage.value);
    }
    formData.append("title", title.value);
    formData.append("content", content.value);
    formData.append("tags", JSON.stringify(tagList.value));
    formData.append("is_draft", isDraft.value);
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
