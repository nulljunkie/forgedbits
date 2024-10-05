import { defineStore } from "pinia";
import { useAuth } from "#imports";

export const useComment = defineStore(
  "comment",
  () => {
    const auth = useAuth();

    const comments = ref([]);

    const getComments = async (postId) => {
      const { data, error } = await useFetch(
        `http://127.0.0.1:8000/api/comments/post/${postId}`,
        {
          headers: auth.user
            ? { Authorization: `Bearer ${auth.accessToken}` }
            : {},
        },
      );

      if (data.value) {
        comments.value = data.value;
      }
      if (error.value) {
        console.log(error.value);
      }
    };

    const setComment = async (comment, postId, parentId = null) => {
      if (parentId === null) {
        comments.value.unshift(comment);
        console.log("setting new comment with parent null");
      } else {
        // FIXME: set replies
        await getComments(postId);
        // const parent = comments.value.find(
        //   (comment) => comment.parent == parentId,
        // );
        // console.log("setting comment in parent: ", parent);
      }
    };

    const addComment = async (content, postId, parentId) => {
      try {
        const res = await $fetch("http://127.0.0.1:8000/api/comments/add/", {
          method: "post",
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: {
            content: content,
            post: postId,
            parent: parentId || null,
          },
        });
        console.log(res);
        if (parentId) {
          setComment(res, postId, parentId);
        } else {
          setComment(res, postId);
        }
        console.log("comments: ", comments.value);
      } catch (err) {
        throw new Error(err);
      }
    };

    return { comments, getComments, setComment, addComment };
  },
  {},
);
