<template>
  <section class="max-w-4xl mx-auto p-8 bg-white shadow-md rounded-lg">
    <!-- Header Section -->
    <header class="text-center mb-12">
      <h1 class="text-4xl font-bold text-gray-900 mb-4">About Us</h1>
      <p class="text-lg text-gray-600">
        Learn more about our mission, values, and the team behind this blog.
      </p>
    </header>

    <!-- Mission Statement -->
    <section class="mb-12">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">Our Mission</h2>
      <p class="text-gray-700 leading-relaxed">
        Our mission is to provide insightful content that informs, educates, and
        inspires our readers. We are dedicated to creating a space where
        knowledge is shared, and conversations are sparked.
      </p>
    </section>

    <!-- Values -->
    <section class="mb-12">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">Our Values</h2>
      <ul class="list-disc list-inside text-gray-700 leading-relaxed">
        <li>Integrity: We believe in honest and transparent content.</li>
        <li>Community: We value our readers and their diverse perspectives.</li>
        <li>Excellence: We strive for quality in everything we produce.</li>
        <li>Innovation: We embrace creativity and new ideas.</li>
      </ul>
    </section>

    <!-- Team Section -->
    <section class="mb-12">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">Meet the Team</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Team Member 1 -->
        <div class="text-center">
          <img
            class="w-32 h-32 rounded-full mx-auto mb-4"
            src="https://via.placeholder.com/150"
            alt="Team Member 1"
          />
          <h3 class="text-xl font-medium text-gray-900">John Doe</h3>
          <p class="text-gray-600">Founder & Chief Editor</p>
        </div>
        <!-- Team Member 2 -->
        <div class="text-center">
          <img
            class="w-32 h-32 rounded-full mx-auto mb-4"
            src="https://via.placeholder.com/150"
            alt="Team Member 2"
          />
          <h3 class="text-xl font-medium text-gray-900">Jane Smith</h3>
          <p class="text-gray-600">Content Strategist</p>
        </div>
        <!-- Team Member 3 -->
        <div class="text-center">
          <img
            class="w-32 h-32 rounded-full mx-auto mb-4"
            src="https://via.placeholder.com/150"
            alt="Team Member 3"
          />
          <h3 class="text-xl font-medium text-gray-900">Alice Johnson</h3>
          <p class="text-gray-600">Marketing Specialist</p>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="text-center mt-12">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">
        Join Our Community
      </h2>
      <p class="text-gray-700 leading-relaxed mb-6">
        We invite you to be part of our growing community. Subscribe to our
        newsletter to stay updated with the latest posts and news.
      </p>
      <NuxtLink
        to="/contact"
        class="inline-block bg-blue-600 text-white py-3 px-6 rounded hover:bg-blue-700 transition-colors duration-300"
      >
        Contact Us
      </NuxtLink>
    </section>
  </section>
</template>

<script setup></script>
