<template>
  <div class="w-full sm:max-w-md md:mt-0 xl:p-0">
    <div class="p-6 space-y-4 sm:p-8 md:space-y-6">
      <div class="flex flex-col items-center">
        <NuxtLink to="/" class="mb-4">
          <span class="text-3xl font-bold font-rubik text-gray-700"
            >Forged</span
          >
          <span class="text-3xl font-rubik text-gray-400">bits</span></NuxtLink
        >
        <h1
          class="text-xl font-bold tracking-tight leading-tight text-center text-gray-700 md:text-2xl"
        >
          Create a new account
        </h1>
        <p class="text-sm font-light text-gray-500">
          Already have an account?
          <span class="font-bold hover:underline text-blue_1"
            ><NuxtLink to="/auth/login">Login</NuxtLink></span
          >
        </p>
      </div>

      <form class="mt-6 flex flex-col gap-4" @submit.prevent="handleSubmit">
        <label for="username">
          Username
          <span class="text-red-500">*</span> <br />
          <input
            id="username"
            v-model="username"
            class="flex items-center flex-1 border rounded-lg w-full p-3 px-4 bg-white"
            placeholder="username"
            autocomplete="username"
            type="text"
            required
          />
          <p v-if="auth.errorMessage === 'EXISTS'" class="text-red-600">
            {{ username }} is taken
          </p>
        </label>

        <label for="password1">
          Password
          <span class="text-red-500">*</span> <br />

          <div class="relative flex items-center w-full">
            <input
              :type="showPassword1 ? 'text' : 'password'"
              v-model="password1"
              @input="handleInputChanged1"
              class="flex items-center flex-1 border rounded-lg w-full p-3 px-4 bg-white"
              placeholder="********"
              autocomplete="autocomplete"
              required="true"
            />
            <Icon
              name="ion:eye-outline"
              size="20"
              class="absolute cursor-pointer right-4"
              @click="showPassword1 = !showPassword1"
              v-if="showPassword1"
            />
            <Icon
              name="ion:eye-off-outline"
              size="20"
              class="absolute cursor-pointer right-4"
              @click="showPassword1 = !showPassword1"
              v-else
            />
          </div>
          <p v-if="!strongPassword" class="text-red-600">
            password should be at least 8 character and contains a Symbol,
            Digit, Upper and Lower case
          </p>
        </label>

        <label for="password2">
          Confirm password
          <span class="text-red-500">*</span> <br />

          <div class="relative flex items-center w-full">
            <input
              :type="showPassword2 ? 'text' : 'password'"
              v-model="password2"
              @input="handleInputChanged2"
              class="flex items-center flex-1 border rounded-lg w-full p-3 px-4 bg-white"
              placeholder="********"
              autocomplete="autocomplete"
              required="true"
            />
            <Icon
              name="ion:eye-outline"
              size="20"
              class="absolute cursor-pointer right-4"
              @click="showPassword2 = !showPassword2"
              v-if="showPassword2"
            />
            <Icon
              name="ion:eye-off-outline"
              size="20"
              class="absolute cursor-pointer right-4"
              @click="showPassword2 = !showPassword2"
              v-else
            />
          </div>
          <p v-if="passwordsDoNotMatch" class="text-red-600">
            password confirm didn't match
          </p>
        </label>

        <button
          class="flex items-center justify-center gap-4 mt-4 text-lg text-white font-bold bg-gray-700 p-3 rounded-lg active:ring-2 active:ring-gray-700"
        >
          <!-- <LoadingIcon v-if="isPending" stroke="4" size="16" color="#fff" /> -->
          <span>{{ buttonText }}</span>
        </button>
      </form>
      <AuthSocialAuth />
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuth } from "#imports";

const username = ref("");
const password1 = ref("");
const password2 = ref("");
const showPassword1 = ref(false);
const showPassword2 = ref(false);
const buttonText = ref("Sign up");
const passwordsDoNotMatch = ref(false);
const strongPassword = ref(true);

const auth = useAuth();

const numbers = /[0-9]/;
const uppercase = /[A-Z]/;
const lowercase = /[a-z]/;
const symbols = /[!@#$%^&*(),.?":{}|<>[\]\/\\~`+=-]/g;

const passwordCheck = () => {
  if (
    password1.value.match(numbers) &&
    password1.value.match(uppercase) &&
    password1.value.match(lowercase) &&
    password1.value.match(symbols) &&
    password1.value.length >= 8
  ) {
    strongPassword.value = true;
  } else {
    strongPassword.value = false;
    // FIXME: input gets unfocused
    // password1.value.focus();
  }
};

const handleSubmit = async () => {
  // check for strong passwords
  passwordCheck();

  if (password1.value === password2.value) {
    passwordsDoNotMatch.value = false;
    try {
      await auth.register(username.value, password1.value, password2.value);
    } catch (error) {
      console.log("Regsiter Failed", error);
    }
  } else {
    passwordsDoNotMatch.value = true;
  }
};
</script>
