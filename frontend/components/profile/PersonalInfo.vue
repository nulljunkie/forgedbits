<template>
  <div class="">
    <h2 class="text-2xl font-semibold text-gray-700 mb-4">
      Personal Information
    </h2>
    <form>
      <div class="">
        <div class="flex flex-row gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700"
              >First Name</label
            >
            <UInput
              v-model="profile.firstName"
              resize
              autoresize
              color="gray"
              placeholder="Type your first name in here..."
              :ui="{
                color: {
                  gray: { outline: 'focus:ring-gray-700 focus:ring-1' },
                },
              }"
              class="font-black"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700"
              >Last Name</label
            >
            <UInput
              v-model="profile.lastName"
              resize
              autoresize
              color="gray"
              placeholder="Type your last name in here..."
              :ui="{
                color: {
                  gray: { outline: 'focus:ring-gray-700 focus:ring-1' },
                },
              }"
              class="font-black"
            />
          </div>
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Username</label
          >
          <UInput
            v-model="profile.username"
            resize
            autoresize
            color="gray"
            :ui="{
              color: {
                gray: { outline: 'focus:ring-gray-700 focus:ring-1' },
              },
            }"
            class="font-black w-64"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700">Email</label>
          <UInput
            v-model="profile.email"
            resize
            autoresize
            color="gray"
            placeholder="Type your email in here..."
            :ui="{
              color: {
                gray: { outline: 'focus:ring-gray-700 focus:ring-1' },
              },
            }"
            class="font-black w-[340px]"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Phone number:</label
          >
          <UInput
            v-model="profile.phone_number"
            color="gray"
            type="tel"
            :ui="{
              color: {
                gray: { outline: 'focus:ring-gray-700 focus:ring-1' },
              },
            }"
            class="font-black w-48"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700">Bio</label>
          <UTextarea
            v-model="profile.bio"
            resize
            autoresize
            color="gray"
            placeholder="Introcude yourself..."
            :ui="{
              color: { gray: { outline: 'focus:ring-gray-700 focus:ring-1' } },
            }"
            class="font-black max-w-[560px]"
          />
        </div>

        <div class="flex flex-col md:flex-row gap-4 mt-4">
          <div class="col-span-2">
            <label class="block text-sm font-medium text-gray-700"
              >Birth date:</label
            >
            <UInput
              v-model="profile.birth_date"
              type="date"
              color="gray"
              :ui="{
                color: {
                  gray: { outline: 'focus:ring-gray-700 focus:ring-1' },
                },
              }"
              class="font-black w-48"
            />
          </div>

          <div class="col-span-2">
            <label class="block text-sm font-medium text-gray-700"
              >Location:</label
            >
            <UInput
              v-model="profile.location"
              color="gray"
              :ui="{
                color: {
                  gray: { outline: 'focus:ring-gray-700 focus:ring-1' },
                },
              }"
              class="font-black w-48"
            />
          </div>
        </div>
        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Linkedin:</label
          >
          <UInput
            v-model="profile.linkedin_profile"
            color="gray"
            type="url"
            :ui="{
              color: { gray: { outline: 'focus:ring-gray-700 focus:ring-1' } },
            }"
            class="font-black max-w-[560px]"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700">Github:</label>
          <UInput
            v-model="profile.github_profile"
            color="gray"
            type="url"
            :ui="{
              color: { gray: { outline: 'focus:ring-gray-700 focus:ring-1' } },
            }"
            class="font-black max-w-[560px]"
          />
        </div>

        <div class="col-span-2 mt-4">
          <label class="block text-sm font-medium text-gray-700"
            >Website:</label
          >
          <UInput
            v-model="profile.website"
            color="gray"
            type="url"
            :ui="{
              color: { gray: { outline: 'focus:ring-gray-700 focus:ring-1' } },
            }"
            class="font-black max-w-[560px]"
          />
        </div>
      </div>
      <UButton
        @click="saveProfile"
        size="lg"
        padding="true"
        label="Save info"
        class="mt-4 text-white bg-gray-700 border border-gray-700 py-2 hover:text-white hover:bg-gray-700 active:ring-2 active:ring-gray-700"
      />
    </form>
  </div>
</template>

<script setup lang="ts">
import { useProfile } from "#imports";

const profile = useProfile();

const saveProfile = async () => {
  await profile.save();
};
</script>
