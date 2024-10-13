<template>
  <div class="px-4">
    <div class="toolbar flex space-x-2 mb-4">
      <UButton
        @click="applyBold"
        icon="i-material-symbols-format-bold"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyItalic"
        icon="i-material-symbols-format-italic"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyHeading1"
        icon="i-gravity-ui-heading-1"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyHeading2"
        icon="i-gravity-ui-heading-2"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyHeading3"
        icon="i-gravity-ui-heading-3"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyUnorderedList"
        icon="i-ic-baseline-format-list-bulleted"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyOrderedList"
        icon="i-ic:baseline-format-list-numbered"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyCodeBlock"
        icon="i-material-symbols-code-rounded"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyImage"
        icon="i-material-symbols-image-outline"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
      <UButton
        @click="applyLink"
        icon="i-material-symbols-add-link"
        size="sm"
        color="gray"
        :ui="{
          icon: { size: { md: 'w-6 h-6' } },
          color: {
            gray: {
              solid:
                'bg-gray-600 hover:text-white hover:bg-gray-700 text-white',
            },
          },
        }"
      />
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
// Define props and emits
const props = defineProps({
  modelValue: String,
});
const emit = defineEmits(["update:modelValue"]);

// Local reactive value based on the prop
const localValue = ref(props.modelValue);

// Watch for changes in the local value and emit them to the parent
watch(localValue, (newValue) => {
  emit("update:modelValue", newValue);
});

// Update local value if the parent value changes
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
