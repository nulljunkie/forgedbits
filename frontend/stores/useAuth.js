import { defineStore } from "pinia";
import { ref } from "vue";
import { useRouter } from "#app";
import { useProfile } from "./useProfile";

const API_URL = "http://127.0.0.1:8000/api/users/";

export const useAuth = defineStore("auth", () => {
  const user = useCookie("USER", {
    maxAge: 60 * 60,
  });
  const accessToken = useCookie("JWT_ACCESS_TOKEN", {
    maxAge: 60 * 60,
  });
  const refreshToken = useCookie("JWT_REFRESH_TOKEN", {
    maxAge: 60 * 60,
  });

  const errorMessage = ref("");

  const router = useRouter();
  const profile = useProfile();

  const register = async (username, password1, password2) => {
    try {
      const response = await $fetch(`${API_URL}register/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: {
          username,
          password1,
          password2,
        },
      });

      setTokens(response);
      setUser(username);
      router.push("/");
    } catch (error) {
      errorMessage.value = error.data
        ? Object.keys(error.data)[0]
        : "Registeration failed";
    }
  };

  const login = async (username, password) => {
    try {
      const response = await $fetch(`${API_URL}token/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: {
          username,
          password,
        },
      });

      setTokens(response);
      console.log("Login: ", response);
      setUser(username);
      router.push("/");
    } catch (error) {
      errorMessage.value = error.data?.detail || "Login failed";
    }
  };

  const logout = () => {
    clearTokens();
    clearUser();
    profile.reset();
    router.push("/auth/login");
  };

  const refresh = async () => {
    try {
      if (refreshToken.value) {
        const response = await $fetch(`${API_URL}token/refresh/`, {
          method: "POST",
          body: {
            refresh: refreshToken.value,
          },
        });
        accessToken.value = response.access;
        console.log("jwt refresh :", response);
      }
    } catch (error) {
      console.log("JWT refresh error: ", error.data);
      logout();
    }
  };

  const setTokens = (res) => {
    accessToken.value = res.access;
    refreshToken.value = res.refresh;
    errorMessage.value = "";
  };

  const clearTokens = () => {
    accessToken.value = null;
    refreshToken.value = null;
  };

  const setUser = (username) => {
    user.value = username;
  };

  const clearUser = () => {
    user.value = null;
  };

  return {
    user,
    accessToken,
    refreshToken,
    errorMessage,
    register,
    login,
    logout,
    refresh,
  };
});
