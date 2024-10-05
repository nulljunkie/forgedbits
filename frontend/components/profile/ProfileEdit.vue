<template>
  <div
    class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
  >
    <div class="bg-white rounded-lg shadow-lg max-w-lg w-full p-6">
      <div class="text-2xl text-center font-semibold mb-4 text-gray-700">
        Edit your profile
      </div>

      <div class="text-gray-700 mb-4">
        <div class="divide-y space-y-2">
          <form @submit.prevent="savePorfile">
            <div class="flex flex-col">
              <label
                for="profile_image"
                class="block mb-2 font-rubik font-bold text-gray-700"
                >Avatar</label
              >
              <input type="file" ref="fileInput" id="profile_image" />
            </div>
            <div class="flex flex-col">
              <label
                for="profile_bio"
                class="block mb-2 font-rubik font-bold text-gray-700"
                >Bio</label
              >
              <textarea
                v-model="profile.bio"
                id="profile_bio"
                rows="4"
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                placeholder="write about yourself...."
              ></textarea>
            </div>
          </form>
        </div>
      </div>

      <div class="flex justify-end space-x-2">
        <button
          @click="emit('cancelEdit')"
          class="hover:bg-red-600 hover:text-white text-red-600 border border-red-600 px-4 py-2 rounded active:outline active:outline-red-600"
        >
          Cancel
        </button>
        <button
          @click="savePorfile"
          type="submit"
          class="hover:bg-green-600 hover:text-white text-green-600 border border-green-600 px-4 py-2 rounded active:outline active:outline-green-600"
        >
          Save
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuth } from "#imports";
import { useProfile } from "#imports";

const auth = useAuth();
const profile = useProfile();

const emit = defineEmits(["cancelEdit", "submited"]);

const fileInput = ref("");

const savePorfile = async () => {
  const formData = new FormData();
  if (fileInput.value.files[0]) {
    formData.append("image", fileInput.value.files[0]);
  }
  formData.append("bio", profile.bio);

  try {
    await profile.save(formData);
    emit("submited");
  } catch (error) {
    console.error(error);
  }
};
</script>
