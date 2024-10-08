<template>
  <div class="relative w-full max-w-md mx-auto">
    <div
      class="flex items-center border border-gray-500 text-gray-800 bg-stone-100 rounded-full px-2 h-10 gap-1"
    >
      <Icon name="bx:search" size="28" />

      <input
        @input="handleSearch"
        v-model="query"
        placeholder="Search..."
        class="h-8 w-full bg-transparent focus:outline-none"
      />
    </div>

    <div
      v-if="query"
      class="absolute w-[500px] max-h-[600px] overflow-auto left-0 right-0 mt-2 bg-white border border-gray-300 rounded-lg shadow-lg z-50"
    >
      <ul>
        <li
          v-for="result in results"
          :key="result.id"
          @click="navigateTo(`/posts/post/${result.id}`)"
          class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
        >
          <div class="font-bold text-gray-900">
            {{ result.title }}
          </div>
          <div class="text-xs text-gray-600">
            by <strong>{{ result.author }}</strong>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
const query = ref("");
const showResults = ref(false);
const results = ref([]);

const handleSearch = () => {
  setTimeout(async () => {
    await submitSearchQuery();
  }, 100);
};

const submitSearchQuery = async () => {
  if (query.value.trim() === "") {
    showResults.value = false;
    results.value = [];
    return;
  }
  const { data, error } = await useFetch(
    "http://127.0.0.1:8000/api/posts/search",
    {
      query: {
        q: query.value,
      },
      watch: [query],
      key: "search-query",
      headers: { accept: "application/json" },
      immediate: false,
      clientOnly: true,
    },
  );

  if (data.value) {
    results.value = data.value;
    showResults.value = true;
  } else if (error.value) {
    showResults.value = false;
    results.value = [];
  }
};
</script>
