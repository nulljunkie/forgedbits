import { useAuth } from "#imports";

export default defineNuxtRouteMiddleware(async (to, from) => {
  const auth = useAuth();

  if (to.query.code) {
    auth.authenticating = true;

    try {
      const response = await $fetch(
        "http://127.0.0.1:8000/api/users/oauth2/github/authenticate/",
        {
          method: "post",
          body: {
            code: to.query.code,
          },
        },
      );

      // const user = useCookie("githubUser");
      auth.user = response.username;
      auth.accessToken = response.access;
      auth.refreshToken = response.refresh;
      //   // auth.authenticating = false;
      return navigateTo({ path: "/" });
    } catch (error) {
      console.error(error);
    }
  }
});
