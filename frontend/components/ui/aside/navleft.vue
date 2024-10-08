<template>
  <div class="sticky top-10 p-2">
    <div class="flex flex-col gap-2 w-48">
      <NuxtLink
        v-for="link in links"
        :key="link.id"
        :to="link.to"
        class="text-gray-700 px-4 py-2 rounded-md"
      >
        <span class="flex items-center gap-2">
          <Icon :name="link.icon" size="24" />

          <span>
            {{ link.label }}
          </span>
        </span>
      </NuxtLink>

      <hr class="border-gray-300" />

      <div class="flex flex-col gap-2 mt-4 pl-4 truncate">
        <p class="text-gray-700">
          <Icon name="cil-tags" />
          Tags
        </p>
        <div v-for="tag in tags" :key="tag.id">
          <NuxtLink
            :to="{ name: 'posts-tag-slug', params: { slug: tag.name } }"
          >
            <span class="flex items-center text-gray-600 group">
              <Icon
                name="i-mingcute-hashtag-fill"
                class="text-gray-400 group-hover:text-gray-500"
              />
              <p class="group-hover:text-gray-800">
                {{ tag.name }} ({{ tag.posts_count }})
              </p>
            </span>
          </NuxtLink>
        </div>

        <NuxtLink
          to="/all-tags"
          class="bg-bg_primary text-blue-500 hover:text-blue-600 hover:underline"
          >see all tags</NuxtLink
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";

const profile = useProfile();
const route = useRoute();

const { data: tags } = await useFetch("http://127.0.0.1:8000/api/posts/tags/");

const links = [
  {
    label: "Trending",
    icon: "heroicons:chart-bar",
    to: "/posts/trending",
  },
  {
    label: "Latest",
    icon: "material-symbols:add-comment-outline-rounded",
    to: "/posts/latest",
  },
  {
    label: "Contact",
    icon: "material-symbols:android-contacts-outline",
    to: "/contact",
  },
  {
    label: "About",
    icon: "heroicons:question-mark-circle",
    to: "/about",
  },
];
</script>

<style scoped>
.router-link-active {
  @apply bg-white font-bold;
}
</style>
