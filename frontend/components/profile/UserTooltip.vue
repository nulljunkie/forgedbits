<template>
  <div class="relative inline-block">
    <div class="flex flex-row items-center">
      <UPopover mode="hover">
        <UAvatar
          size="sm"
          :src="props.author.image"
          :alt="props.author.username"
          class="pt-1"
        />
        <template #panel>
          <div class="p-2 w-[240px]">
            <Tooltip
              :profileId="props.author.profile_id"
              :userImage="props.author.image"
              :username="props.author.username"
            />
          </div>
        </template>
      </UPopover>

      <div class="ml-1 pt-1">
        <ULink
          to="/profile"
          inactive-class="text-sm font-bold text-gray-700 hover:underline "
        >
          {{ props.author.username }}
        </ULink>

        <div class="text-xs font-thin">{{ createdDate }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { formatDate } from "~/utils/dateFns.js";
import Tooltip from "./Tooltip.vue";

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
