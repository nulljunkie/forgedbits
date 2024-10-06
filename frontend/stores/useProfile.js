import { defineStore } from "pinia";
import { ref } from "vue";
import { useAuth } from "#imports";

const API_URL = "http://127.0.0.1:8000/api/users/";

export const useProfile = defineStore(
  "profile",
  () => {
    // NOTE: this line cannot be outside
    // because the pinia store is not yet active
    const auth = useAuth();

    const image = ref(null);
    const banner = ref(null);
    const bio = ref(null);
    const firstName = ref(null);
    const lastName = ref(null);
    const email = ref(null);
    const username = ref(null);
    const birth_date = ref(null);
    const phone_number = ref(null);
    const location = ref(null);
    const website = ref(null);
    const linkedin_profile = ref(null);
    const github_profile = ref(null);

    const get = async () => {
      if (auth.user)
        try {
          // NOTE: request's error are passed to error
          // not error in catch below, those are for try block errors
          const { data, error } = await useFetch(`${API_URL}profile/`, {
            headers: {
              Authorization: `Bearer ${auth.accessToken}`,
            },
          });

          if (data.value) {
            console.log(data.value);
            setProfile(data.value);
          } else if (error.value) {
            console.log("error.value for useFetch profile.get");
            // console.log("profile useFetch error: ", error.value);
            // try {
            //   await auth.refresh();
            //   console.log("jwt refreshed 100%");
            //   const res = await $fetch(`${API_URL}profile/`, {
            //     headers: {
            //       Authorization: `Bearer ${auth.accessToken}`,
            //     },
            //   });
            //   console.log("res: ", res);
            // } catch (error) {
            //   console.log("second attempt for fetching profile failed");
            // }
          }
        } catch (error) {
          console.error("get profile errror: ", error);
        }
      else navigateTo("/auth/login");
    };

    const save = async (info) => {
      try {
        const response = await $fetch(`${API_URL}profile/upload/`, {
          method: "patch",
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: {
            username: username.value,
            firstName: firstName.value,
            lastName: lastName.value,
            email: email.value,
            bio: bio.value,
            location: location.value,
            phone_number: phone_number.value,
            website: website.value,
            linkedin_profile: linkedin_profile.value,
            github_profile: github_profile.value,
            birth_date: birth_date.value,
          },
        });
        setProfile(response);
      } catch (error) {
        console.error("Profile Save Error: ", error.data);
        // try {
        //   await auth.refresh();
        //   const response = await $fetch(`${API_URL}profile/upload/`, {
        //     method: "post",
        //     headers: {
        //       Authorization: `Bearer ${auth.accessToken}`,
        //     },
        //     body: formData,
        //   });
        //   console.log("profile save retry 100%: \n", response);
        //   setProfile(response);
        // } catch (error) {
        //   console.log("profile save retry failed");
        // }
      }
    };

    const uploadProfileImage = async (avatar = null, banner = null) => {
      try {
        const formData = new FormData();
        if (avatar) {
          console.log("avatar");
          formData.append("image", avatar);
        } else if (banner) {
          console.log("banner");
          formData.append("banner", banner);
        }

        const res = await $fetch(`${API_URL}profile/upload/`, {
          method: "patch",
          headers: {
            Authorization: `Bearer ${auth.accessToken}`,
          },
          body: formData,
        });

        // console.log(res);
        // image.value = res.image;
        // banner.value = res.banner;

        setProfile(res);
      } catch (err) {
        throw new Error("fucking error", err);
      }
    };

    const setProfile = (data) => {
      image.value = data.image;
      banner.value = data.banner;
      bio.value = data.bio;
      firstName.value = data.firstName;
      lastName.value = data.lastName;
      email.value = data.email;
      username.value = data.username;
      location.value = data.location;
      birth_date.value = data.birth_date;
      website.value = data.website;
      phone_number.value = data.phone_number;
      linkedin_profile.value = data.linkedin_profile;
      github_profile.value = data.github_profile;
    };

    const reset = () => {
      image.value = null;
      banner.value = null;
      bio.value = null;
      firstName.value = null;
      lastName.value = null;
      email.value = null;
      username.value = null;
      location.value = null;
      birth_date.value = null;
      phone_number.value = null;
      website.value = null;
      github_profile.value = null;
      linkedin_profile.value = null;
    };

    return {
      firstName,
      lastName,
      username,
      email,
      image,
      banner,
      bio,
      get,
      save,
      reset,
      uploadProfileImage,
      website,
      phone_number,
      birth_date,
      linkedin_profile,
      github_profile,
      location,
    };
  },
  { persist: true },
);
