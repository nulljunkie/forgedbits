<template>
  <div class="">
    <h2 class="text-2xl font-semibold text-gray-700 mb-4">
      Personal Information
    </h2>
    <form @submit.prevent @keydown.enter.prevent>
      <div class="bg-white p-4 rounded-md shadow-md">
        <div class="flex flex-row gap-4">
          <div class="flex-1">
            <label class="block text-sm font-medium text-gray-700"
              >First Name</label
            >
            <input
              v-model="profile.firstName"
              placeholder="your first name..."
              class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
            />
          </div>

          <div class="flex-1">
            <label class="block text-sm font-medium text-gray-700"
              >Last Name</label
            >

            <input
              v-model="profile.lastName"
              placeholder="your last name..."
              class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
            />
          </div>
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Username</label
          >
          <input
            v-model="profile.username"
            class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700">Email</label>

          <input
            v-model="profile.email"
            type="email"
            placeholder="your-email@example.com"
            class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Phone number:</label
          >

          <input
            v-model="profile.phone_number"
            type="tel"
            placeholder="+1 123 456 7890"
            class="text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700">Bio</label>

          <textarea
            v-model="profile.bio"
            rows="6"
            placeholder="about you..."
            class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
          />
        </div>

        <div class="flex flex-col md:flex-row gap-4 mt-4">
          <div class="col-span-2">
            <label class="block text-sm font-medium text-gray-700"
              >Birth date:</label
            >

            <input
              v-model="profile.birth_date"
              type="date"
              class="text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
            />
          </div>

          <div class="col-span-2">
            <label class="block text-sm font-medium text-gray-700"
              >Location:</label
            >

            <input
              v-model="profile.location"
              placeholder="your residence address..."
              class="text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
            />
          </div>
        </div>
        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Linkedin:</label
          >

          <input
            v-model="profile.linkedin_profile"
            placeholder="your linkedin profile.."
            type="url"
            class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700">Github:</label>

          <input
            v-model="profile.github_profile"
            placeholder="your github profile.."
            type="url"
            class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Website:</label
          >

          <input
            v-model="profile.website"
            placeholder="your website url..."
            type="url"
            class="w-full text-gray-700 font-bold bg-gray-50 ring-1 ring-gray-300 focus:ring-gray-500 focus:shadow-md px-2 py-1 rounded-md"
          />
        </div>
      </div>

      <button
        @click="save"
        class="mt-4 text-white font-bold px-4 py-2 bg-gray-700 hover:bg-gray-800 rounded-md active:scale-[102%]"
      >
        Save
      </button>
    </form>
  </div>
</template>

<script setup>
import { useProfile } from "#imports";

const profile = useProfile();

const save = async () => {
  console.log("saving profileinfo [1]");
  await profile.save();
};
</script>
