<script setup lang="ts">
import { Store } from "pinia";
import { Router } from "vue-router";
import { useUserStore } from "~/stores/user";
import { User } from "~/types/user";

const router: Router = useRouter();
const useStore = useUserStore();

const user: User = reactive<User>({
  username: "",
  password: "",
});
const errors: Ref<string[]> = ref([]);

async function logIn() {
  errors.value = [];

  try {
    const response: any = await $fetch(
      "http://127.0.0.1:8000/api/v1/token/login/",
      {
        method: "POST",
        body: user,
      }
    );

    useStore.setToken(response.auth_token, user.username);

    router.push({ path: "/" });
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
      <Title>Log In</Title>
    </Head>
  </Html>
  <div class="py-10 px-6">
    <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl">
      <h1 class="mb-6 text-2xl">Log in</h1>
      <form @submit.prevent="logIn">
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

        <div
          v-if="errors.length"
          class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl"
        >
          <p v-for="error in errors" :key="error">
            {{ error }}
          </p>
        </div>

        <button class="py-4 px-6 bg-teal-700 rounded-xl text-white">
          Login
        </button>
      </form>
    </div>
  </div>
</template>