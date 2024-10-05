<template>
  <section class="max-w-4xl mx-auto p-8 bg-white shadow-md rounded-lg">
    <!-- Header Section -->
    <header class="text-center mb-12">
      <h1 class="text-4xl font-bold text-gray-900 mb-4">Contact Me</h1>
      <p class="text-lg text-gray-600">
        I would love to hear from you! Whether you have a question, feedback, or
        just want to say hello, feel free to reach out.
      </p>
    </header>

    <!-- Contact Form -->
    <form @submit.prevent="submitForm" class="space-y-6">
      <div>
        <label for="name" class="block text-gray-700 font-medium mb-2"
          >Name</label
        >
        <input
          type="text"
          id="name"
          v-model="form.name"
          class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-600"
          placeholder="Your Name"
          required
        />
      </div>

      <div>
        <label for="email" class="block text-gray-700 font-medium mb-2"
          >Email</label
        >
        <input
          type="email"
          id="email"
          v-model="form.email"
          class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-600"
          placeholder="Your Email"
          required
        />
      </div>

      <div>
        <label for="message" class="block text-gray-700 font-medium mb-2"
          >Message</label
        >
        <textarea
          id="message"
          v-model="form.message"
          class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-600"
          rows="5"
          placeholder="Your Message"
          required
        ></textarea>
      </div>

      <div class="text-center">
        <button
          type="submit"
          class="bg-blue-600 text-white py-3 px-6 rounded hover:bg-blue-700 transition-colors duration-300"
        >
          Send Message
        </button>
      </div>
    </form>

    <!-- Contact Info -->
    <section class="mt-12 text-center">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">Get in Touch</h2>
      <p class="text-gray-700 leading-relaxed mb-4">
        You can also reach me via email at:
        <a
          href="mailto:your-email@example.com"
          class="text-blue-600 hover:underline"
        >
          your-email@example.com
        </a>
      </p>
      <p class="text-gray-700 leading-relaxed">Or follow me on social media:</p>
      <div class="mt-4 flex justify-center space-x-4">
        <a href="#" class="text-blue-600 hover:underline">Twitter</a>
        <a href="#" class="text-blue-600 hover:underline">LinkedIn</a>
        <a href="#" class="text-blue-600 hover:underline">GitHub</a>
      </div>
    </section>
  </section>
</template>

<script setup>
import { ref } from "vue";

const form = ref({
  name: "",
  email: "",
  message: "",
});

const submitForm = () => {
  console.log("Form submitted:", form.value);
  // Here you would typically send the form data to an API or email service
};
</script>
