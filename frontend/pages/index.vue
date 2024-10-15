<template>
  <section class="flex flex-col gap-3">
    <!-- <PostPostList :posts="posts" /> -->
    <PostPostList :posts="postStore.allPosts" />
    <!-- <div v-if="loading" class="text-gray-700 text-4xl text-center m-4"> -->
    <!--   <div class="fixed z-50 top-0 w-full h-96 bg-sky-500"></div> -->
    <!--   Loading... -->
    <!-- </div> -->
  </section>
</template>

<script setup>
import { useAuth } from "#imports";
import { usePost } from "#imports";

const auth = useAuth();
const postStore = usePost();

// const page = ref(1);
const loading = ref(false);

await postStore.getAllPosts();

if (process.client) {
  const handleScroll = async () => {
    // console.log("H: ", window.innerHeight);
    // console.log("S: ", window.scrollY);
    // console.log("body H: ", document.body.offsetHeight);
    if (
      window.innerHeight + window.scrollY >= document.body.offsetHeight - 100 &&
      !loading.value
    ) {
      loading.value = true;
      // page.value++;
      // console.log("page #", page.value);
      // await postStore.getAllPosts(page.value);
      await postStore.getNextPosts();
      loading.value = false;
    }
  };

  onMounted(() => {
    window.addEventListener("scroll", handleScroll);
  });

  onBeforeUnmount(() => {
    window.removeEventListener("scroll", handleScroll);
  });
}

onMounted(() => {
  auth.authenticating = false;
});

definePageMeta({
  layout: "main",
  middleware: "oauth",
});
</script>
