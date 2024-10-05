<template>
  <div>
    <div v-if="pending" class="h-28 flex items-center justify-center">
      <Icon name="eos-icons-loading" size="64" class="text-gray-700" />
    </div>
    <div v-else>
      <div class="flex items-center space-x-4 mb-3">
        <UAvatar
          size="xl"
          :src="props.userImage"
          :alt="props.username"
          class="pt-1"
        />
        <div>
          <ULink
            to="/profile"
            inactive-class="text-xl font-semibold text-gray-800 "
          >
            {{ props.username }}
          </ULink>

          <p class="text-sm text-gray-600">{{ authorProfile.email }}</p>
        </div>
      </div>
      <p class="text-sm text-gray-700 mt-2 leading-relaxed text-wrap">
        {{ authorProfile.bio }}
      </p>

      <div v-if="props.username != auth.user" class="mt-4">
        <FollowButton :user="authorProfile" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";
import FollowButton from "./FollowButton";

const authorProfile = ref({});
const auth = useAuth();

const props = defineProps({
  profileId: {
    type: Number,
    requied: true,
  },
  userImage: {
    type: String,
    requied: true,
  },
  username: {
    type: String,
    requied: true,
  },
});

const { pending, error } = useLazyFetch(
  `http://127.0.0.1:8000/api/users/profile/glimps/${props.profileId}`,
  {
    headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
    onResponse({ request, response, options }) {
      authorProfile.value = response._data;
    },
  },
);
</script>
