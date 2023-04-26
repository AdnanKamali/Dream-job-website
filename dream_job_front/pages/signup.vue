<script setup lang="ts">
import { Router } from "vue-router";
import { User } from "~/types/user";

const router: Router = useRouter();

const user: User = reactive<User>({
  username: "",
  password: "",
});

const rePassword = ref("");
const errors: Ref<string[]> = ref([]);

async function signUp() {
  errors.value = [];

  try {
    const response = await $fetch("http://127.0.0.1:8000/api/v1/users/", {
      method: "POST",
      body: user,
    });
    router.push({ path: "/login" });
  } catch (er: any) {
    if (er.response)
      for (const property in er.response._data)
        errors.value.push(`${property}: ${er.response._data[property]}`);
    else if (er.message)
      errors.value.push("Something went wrong. Please try again");
  }
}
</script>

<template>
  <Html>
    <Head>
      <Title>Sign Up</Title>
    </Head>
  </Html>
  <div class="py-10 px-6">
    <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl">
      <h1 class="mb-6 text-2xl">Sign up</h1>
      <form @submit.prevent="signUp">
        <input
          type="email"
          v-model="user.username"
          placeholder="Your email address..."
          class="w-full mb-4 py-4 px-6 rounded-xl"
        />
        <input
          type="password"
          v-model="user.password"
          placeholder="Your password..."
          class="w-full mb-4 py-4 px-6 rounded-xl"
        />
        <input
          type="password"
          v-model="rePassword"
          placeholder="Repeat password..."
          class="w-full mb-4 py-4 px-6 rounded-xl"
        />

        <div
          v-if="errors.length"
          class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl"
        >
          <p v-for="error in errors" :key="error">
            {{ error }}
          </p>
        </div>

        <button class="py-4 px-6 bg-teal-700 rounded-xl text-white">
          Sign Up
        </button>
      </form>
    </div>
  </div>
</template>