<template>
  <div>
    <label class="block text-sm font-medium text-gray-700">{{
      props.label
    }}</label>
    <input
      v-model="profile.firstName"
      placeholder="your first name..."
      class="text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
    />
  </div>
</template>

<script setup>
import { useProfile } from "#imports";

const profile = useProfile();

const props = defineProps({
  label: {
    type: String,
  },
  input: {
    type: String,
  },
});
</script>
