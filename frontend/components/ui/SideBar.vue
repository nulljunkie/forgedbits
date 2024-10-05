<script setup>
import { useProfile } from "#imports";

const profile = useProfile();
const route = useRoute();

const { data: tags } = await useFetch("http://127.0.0.1:8000/api/posts/tags/");

const links = [
  [
    {
      label: "Home",
      icon: "i-heroicons-home",
      to: "/",
    },
    {
      label: "Trending",
      icon: "i-heroicons-chart-bar",
      to: "/posts/trending",
    },
    {
      label: "Latest",
      icon: "i-material-symbols-add-comment-outline-rounded",
      to: "/posts/latest",
    },
  ],
  [
    {
      label: "Contact",
      icon: "i-material-symbols-android-contacts-outline",
      to: "/contact",
    },
    {
      label: "About",
      icon: "i-heroicons-question-mark-circle",
      to: "/about",
    },
  ],
];
</script>

<template>
  <div class="w-[190px]">
    <UVerticalNavigation
      :links="links"
      :ui="{
        wrapper: 'space-y-2',
        base: 'text-start before:hidden',
        padding: 'px-4 py-1 mb-2',
        rounded: 'rounded-md',
        font: '',
        ring: 'hover:ring-2 hover:ring-white',
        active: 'font-black bg-slate-100 ',
        inactive: 'hover:bg-white  text-gray-700 hover:text-gray-900 ',

        label: 'truncate relative',
        icon: {
          base: 'flex-shrink-0 w-5 h-5 relative',
          active: 'text-gray-700 ',
          inactive: 'text-gray-400 group-hover:text-gray-700 ',
        },

        avatar: {
          base: 'flex-shrink-0',
          size: 'xs',
        },
        badge: {
          base: 'flex-shrink-0 ml-auto relative rounded',
          color: 'gray',
          variant: 'solid',
          size: 'xs',
        },
        divider: {
          wrapper: {
            base: 'p-2',
          },
        },
      }"
    />
    <hr />
    <div class="flex flex-col gap-2 mt-4 pl-4 truncate">
      <p class="text-gray-700">
        <Icon name="cil-tags" />
        Tags
      </p>
      <div v-for="tag in tags" :key="tag.id">
        <NuxtLink :to="{ name: 'posts-tag-slug', params: { slug: tag.name } }">
          <span class="flex items-center text-gray-600 group">
            <Icon
              name="i-mingcute-hashtag-fill"
              class="text-gray-400 group-hover:text-gray-500"
            />
            <p class="group-hover:text-gray-800">
              {{ tag.name }}
            </p>
          </span>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
