import { defineStore } from "pinia";
import { useAuth } from "#imports";

export const useUser = defineStore(
  "user",
  () => {
    const auth = useAuth();

    const users = ref([]);

    const getUsers = async () => {
      const { data, error } = await useFetch(
        "http://127.0.0.1:8000/api/users/list/",
        {
          headers: auth.user
            ? { Authorization: `Bearer ${auth.accessToken}` }
            : {},
        },
      );
      if (data.value) {
        users.value = data.value;
      }
      if (error.value) {
        console.log(error.value);
      }
    };

    const follow = async (profileId) => {
      if (auth.user) {
        try {
          const res = await $fetch(
            `http://127.0.0.1:8000/api/users/followers/follow/`,
            {
              method: "post",
              headers: {
                Authorization: `Bearer ${auth.accessToken}`,
              },
              body: {
                profile_id: profileId,
              },
            },
          );
          const user = users.value.find((profile) => profile.id == profileId);
          user.is_followed = res.is_followed;
          user.followers++;
        } catch (err) {
          console.error(err);
        }
      }
    };
    const unfollow = async (profileId) => {
      if (auth.user) {
        try {
          const res = await $fetch(
            `http://127.0.0.1:8000/api/users/followers/unfollow/`,
            {
              method: "delete",
              headers: {
                Authorization: `Bearer ${auth.accessToken}`,
              },
              body: {
                profile_id: profileId,
              },
            },
          );
          const user = users.value.find((profile) => profile.id == profileId);
          user.is_followed = res.is_followed;
          user.followers--;
        } catch (err) {
          console.error(err);
        }
      }
    };

    const isFollowed = (profileId) => {};

    const getFollowers = (prifileId) => {};

    return { users, getUsers, getFollowers, follow, unfollow, isFollowed };
  },
  {},
);
