<template>
  <div class="relative inline-block">
    <div class="flex">
      <UPopover
        mode="hover"
        :ui="{
          width: 'max-w-64',
          background: 'bg-white dark:bg-white',
          ring: 'ring-1 dark:ring-gray-300',
          shadow: 'shadow-xl',
        }"
        class="mt-1"
      >
        <UAvatar
          size="sm"
          :src="props.author.image"
          :alt="props.author.username"
          class="border border-gray-900"
        />
        <template #panel class="">
          <div class="p-2">
            <PostPostAuthorPopoverContent
              :profileId="props.author.profile_id"
              :userImage="props.author.image"
              :username="props.author.username"
            />
          </div>
        </template>
      </UPopover>

      <div class="ml-1 space-y-[-4px]">
        <ULink
          to="/profile"
          inactive-class="text-sm font-bold text-gray-700 hover:underline "
        >
          {{ props.author.username }}
        </ULink>

        <div class="text-xs font-thin text-gray-700">{{ createdDate }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { formatDate } from "~/utils/dateFns.js";

const props = defineProps({
  author: {
    type: Object,
    required: true,
  },
  created: {
    type: Object,
    requied: true,
  },
  created: {
    type: Object,
    requied: true,
  },
});

const createdDate = computed(() => {
  return formatDate(new Date(props.created));
});
</script>
