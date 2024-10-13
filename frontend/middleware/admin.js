import { useAuth } from "#imports";

export default defineNuxtRouteMiddleware((to, from) => {
  const auth = useAuth();

  if (auth.user !== "admin") {
    // return navigateTo("/error?message=Authentication%20Failed");
    return navigateTo(
      `/error?message=${encodeURIComponent("Authentication Failed")}`,
    );
  }
});
