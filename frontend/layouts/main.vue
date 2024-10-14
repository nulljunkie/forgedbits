<!-- <template> -->
<!--   <div class="relative bg-stone-100"> -->
<!--     <div -->
<!--       v-if="auth.authenticating" -->
<!--       class="fixed inset-0 bg-black bg-opacity-85 flex items-center justify-center z-50" -->
<!--     > -->
<!--       <Icon name="eos-icons:three-dots-loading" size="96" /> -->
<!--     </div> -->
<!--     <navbar /> -->
<!--     <div -->
<!--       class="flex flex-row gap-4 min-h-screen max-w-[1200px] mx-auto mt-3 px-4" -->
<!--     > -->
<!--       <div class="hidden md:block"> -->
<!--         <navleft /> -->
<!--       </div> -->
<!--       <div class="w-full"> -->
<!--         <slot /> -->
<!--       </div> -->
<!--       <div class="hidden lg:block w-[480px] space-y-4"> -->
<!--         <div class="shadow-md rounded-md bg-gray-100"> -->
<!--           <UsersBar /> -->
<!--         </div> -->
<!--         <div class="sticky top-16 shadow-md rounded-md bg-gray-100"> -->
<!--           <UsersBar /> -->
<!--         </div> -->
<!--       </div> -->
<!--     </div> -->
<!--     <Footer /> -->
<!--   </div> -->
<!-- </template> -->

<template>
  <div class="bg-stone-100">
    <!-- <div -->
    <!--   v-if="auth.authenticating" -->
    <!--   class="fixed inset-0 bg-black bg-opacity-85 flex items-center justify-center z-50" -->
    <!-- > -->
    <!--   <Icon name="eos-icons:three-dots-loading" size="96" /> -->
    <!-- </div> -->
    <navbar />
    <div
      class="flex flex-row gap-4 min-h-screen max-w-[1200px] mx-auto mt-3 px-4"
    >
      <div class="hidden md:block">
        <navleft />
      </div>
      <div class="flex-grow overflow-auto">
        <slot />
      </div>
      <div class="hidden lg:block w-[480px] space-y-4 sticky top-16">
        <div class="shadow-md rounded-md bg-gray-100">
          <UsersBar />
        </div>
        <div class="shadow-md rounded-md bg-gray-100">
          <UsersBar />
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import Footer from "@/components/ui/Footer.vue";
import UsersBar from "@/components/ui/UsersBar.vue";
import navleft from "@/components/ui/aside/navleft.vue";
import navbar from "@/components/ui/nav/navbar.vue";
import { useAuth } from "#imports";

const auth = useAuth();
</script>
