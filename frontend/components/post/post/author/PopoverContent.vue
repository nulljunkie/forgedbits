<template>
  <div>
    <!-- <div v-if="pending" class="w-full h-full flex items-center justify-center"> -->
    <!--   <Icon name="eos-icons-loading" size="64" class="text-gray-700" /> -->
    <!-- </div> -->
    <!---->
    <!-- <section v-if="!pending"> -->
    <section>
      <div class="flex items-center space-x-4 mb-3">
        <img
          :src="authorProfile.image"
          alt="Author Avatar"
          class="w-12 h-12 rounded-full border border-gray-500"
        />
        <div>
          <span class="font-semibold text-lg text-gray-900"
            >{{ authorProfile.first_name }} {{ authorProfile.last_name }}</span
          >
          <div class="flex text-gray-700 text-sm items-center">
            <!-- <Icon name="hugeicons:birthday-cake" size="20" /> -->
            Joined: {{ dateJoined }}
          </div>
        </div>
      </div>

      <p class="text-gray-600 text-sm line-clamp-3 mb-3">
        {{ authorProfile.bio }}
      </p>

      <div class="flex text-sm text-gray-900 font-extrabold mb-2 gap-2">
        <div>{{ authorProfile.posts_count }} Posts</div>
        <div>{{ authorProfile.comments_count }} Comments</div>
      </div>

      <div class="flex text-sm text-gray-900 font-extrabold mb-2 gap-2">
        <div>{{ authorProfile.followers }} Followers</div>
        <div>{{ authorProfile.following }} Following</div>
      </div>

      <div v-if="props.username != auth.user">
        <div class="flex justify-end gap-2">
          <button
            class="py-1 px-2 inline-flex items-center text-xs font-bold rounded-lg bg-sky-500 text-gray-50 hover:bg-sky-600"
          >
            Chat
          </button>

          <PostPostAuthorFollowButton :user="authorProfile" />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";

const authorProfile = ref({});
const auth = useAuth();

const dateJoined = ref(null);

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

      const date = new Date(authorProfile.value.date_joined);
      dateJoined.value = date.toLocaleDateString("en-GB", {
        day: "numeric",
        month: "short",
        year: "numeric",
      });

      console.log(dateJoined.value);
    },
  },
);
</script>
