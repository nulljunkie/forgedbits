import { defineStore } from "pinia";
import { useAuth } from "#imports";

const API_URL = "http://127.0.0.1:8000/api/posts/";

export const usePost = defineStore("post", () => {
  const auth = useAuth();

  const allPosts = ref([]);
  const myPosts = ref([]);
  const currentPost = ref(null);

  const nextPage = ref(null);

  const getAllPosts = async () => {
    const { data: posts } = await useFetch("http://127.0.0.1:8000/api/posts/", {
      headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
    });
    allPosts.value.push(...posts.value.results);
    nextPage.value = posts.value.next;
  };

  const getNextPosts = async () => {
    if (nextPage.value) {
      const posts = await $fetch(nextPage.value, {
        headers: auth.user
          ? { Authorization: `Bearer ${auth.accessToken}` }
          : {},
      });
      console.log("next posts", posts);
    }
  };

  const getPost = async (postId) => {
    const { data, error } = await useFetch(`${API_URL}post/${postId}`, {
      headers: auth.user ? { Authorization: `Bearer ${auth.accessToken}` } : {},
    });

    if (data.value) {
      currentPost.value = data.value;
    } else if (error.value) {
      currentPost.value = null;
      console.log(error.value);
    }
  };

  const getMyPosts = async () => {
    const { data, error } = await useFetch(`${API_URL}me/`, {
      headers: {
        Authorization: `Bearer ${auth.accessToken}`,
      },
    });
    if (data.value) {
      myPosts.value = data.value;
    }
    if (error.value) {
      console.log(error.value);
    }
  };

  const deleteMyPost = async (postId) => {
    try {
      const res = await $fetch(`${API_URL}post/${postId}`, {
        method: "delete",
        headers: {
          Authorization: `Bearer ${auth.accessToken}`,
        },
      });
      const index = myPosts.value.findIndex((post) => post.id == postId);
      myPosts.value.splice(index, 1);
    } catch (err) {
      console.error("failed to delete post: ", err);
    }
  };

  const addPost = async (formData) => {
    try {
      const res = await $fetch(`${API_URL}create/`, {
        method: "post",
        headers: {
          Authorization: `Bearer ${auth.accessToken}`,
        },
        body: formData,
      });
    } catch (error) {
      console.error(error);
    }
  };

  const saveDraft = () => {};
  const updateMyPost = () => {};

  return {
    allPosts,
    myPosts,
    currentPost,
    getPost,
    addPost,
    saveDraft,
    getMyPosts,
    getAllPosts,
    deleteMyPost,
    getNextPosts,
    updateMyPost,
  };
});
