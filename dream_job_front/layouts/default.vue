<script setup lang="ts">
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();
</script>

<template>
  <div>
    <nav class="p-6 flex items-center justify-between bg-teal-800">
      <nuxt-link to="/" class="text-xl text-white">D Job</nuxt-link>
      <div class="flex items-center space-x-4">
        <nuxt-link to="/" class="text-white hover:text-teal-300"
          >Home</nuxt-link
        >
        <nuxt-link to="/browse" class="text-white hover:text-teal-300"
          >Browse</nuxt-link
        >
      </div>
    </nav>

    <slot />

    <footer class="p-6 flex flex-wrap items-center justify-between bg-gray-900">
      <p class="text-gray-300">Copyright (c) 2023 - Djob</p>

      <div class="flex mt-6 md:mt-0 items-center space-x-4">
        <template v-if="userStore.user.isAuthenticated">
          <nuxt-link
            to="/myjobs"
            class="py-4 px-6 bg-teal-900 hover:bg-teal-300 text-white rounded-xl"
            >My Jobs</nuxt-link
          >
          <nuxt-link
            to="/createjob"
            class="py-4 px-6 bg-teal-600 hover:bg-teal-300 text-white rounded-xl"
            >Create Job</nuxt-link
          >
          <nuxt-link
            to="/"
            class="py-4 px-6 bg-rose-600 hover:bg-rose-300 text-white rounded-xl"
            >Log Out</nuxt-link
          >
        </template>
        <template v-else>
          <nuxt-link
            to="/login"
            class="py-4 px-6 bg-teal-900 hover:bg-teal-300 text-white rounded-xl"
            >Login</nuxt-link
          >
          <nuxt-link
            to="/signup"
            class="py-4 px-6 bg-teal-600 hover:bg-teal-300 text-white rounded-xl"
            >Sign Up</nuxt-link
          >
        </template>
      </div>
    </footer>
  </div>
</template>