<template>
  <div class="px-4">
    <div class="toolbar flex space-x-2 mb-4">
      <button
        @click="applyBold"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="material-symbols-format-bold" size="24" />
      </button>

      <button
        @click="applyItalic"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="material-symbols-format-italic" size="24" />
      </button>
      <button
        @click="applyHeading1"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="gravity-ui:heading-1" size="24" />
      </button>
      <button
        @click="applyHeading2"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="gravity-ui:heading-2" size="24" />
      </button>

      <button
        @click="applyHeading3"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="gravity-ui:heading-3" size="24" />
      </button>

      <button
        @click="applyUnorderedList"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="ic:baseline-format-list-bulleted" size="24" />
      </button>

      <button
        @click="applyOrderedList"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="ic:baseline-format-list-numbered" size="24" />
      </button>

      <button
        @click="applyCodeBlock"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="material-symbols:code-rounded" size="24" />
      </button>

      <button
        @click="applyImage"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="material-symbols:image-outline" size="24" />
      </button>

      <button
        @click="applyLink"
        class="text-white bg-gray-800 h-8 w-8 flex items-center justify-center rounded-md hover:bg-gray-900"
      >
        <Icon name="material-symbols:add-link" size="24" />
      </button>
    </div>
    <textarea
      v-model="localValue"
      name="contentarea"
      placeholder="Write post content here..."
      autoresize
      rows="12"
      class="text-gray-700 bg-white w-full scroll-m-4 outline-none"
    />
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: String,
});
const emit = defineEmits(["update:modelValue"]);

const localValue = ref(props.modelValue);

watch(localValue, (newValue) => {
  emit("update:modelValue", newValue);
});

watch(
  () => props.modelValue,
  (newValue) => {
    localValue.value = newValue;
  },
);

const applyBold = () => wrapSelection("**");
const applyItalic = () => wrapSelection("*");
const applyHeading1 = () => insertAtCursor("# ");
const applyHeading2 = () => insertAtCursor("## ");
const applyHeading3 = () => insertAtCursor("### ");
const applyUnorderedList = () => insertAtCursor("- ");
const applyOrderedList = () => insertAtCursor("1. ");
const applyCodeBlock = () => wrapSelection("```", "\n```\n");
const applyImage = () => insertAtCursor("![alt text](url)");
const applyLink = () => insertAtCursor("[link text](url)");

const wrapSelection = (wrapper, endWrapper = wrapper) => {
  const textarea = document.querySelector("textarea");
  const start = textarea.selectionStart;
  const end = textarea.selectionEnd;
  localValue.value =
    localValue.value.substring(0, start) +
    wrapper +
    localValue.value.substring(start, end) +
    endWrapper +
    localValue.value.substring(end);
};

const insertAtCursor = (text) => {
  const textarea = document.querySelector("textarea");
  const start = textarea.selectionStart;
  localValue.value =
    localValue.value.substring(0, start) +
    text +
    localValue.value.substring(start);
};
</script>
