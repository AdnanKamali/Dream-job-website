<script setup lang="ts">
import { JobT } from "@/types/job";

const route = useRoute();

const { data: job } = await useFetch<JobT>(
  "http://127.0.0.1:8000/api/v1/jobs/" + route.params.id + "/"
);
</script>

<template>
  <Html>
    <Head>
      <Title>{{ job?.title }}</Title>
    </Head>
  </Html>
  <div class="py-10 px-6 grid md:grid-cols-4 gap-3">
    <div class="md:col-span-3">
      <h1 class="mb-6 text-3xl">{{ job?.title }}</h1>

      <p>{{ job?.description }}</p>

      <a
        href="a"
        class="inline-block mt-6 py-4 px-6 bg-teal-700 text-white rounded-xl"
        >Apply</a
      >
    </div>
    <div class="md:col-span-1 py-6 px-6 bg-teal-700 text-white rounded-xl">
      <h1 class="text-3xl mb-6">Company</h1>

      <p class="mb-2">{{ job?.company_name }}</p>
      <p>{{ job?.company_location }}</p>

      <hr class="opacity-30 my-6" />

      <h1 class="text-3xl mb-6">Position</h1>

      <p class="mb-2">{{ job?.position_location }}</p>
      <p>{{ job?.position_salary }}</p>
      <hr class="opacity-30 my-6" />

      <p>Posted at {{ job?.created_at_formatted }}</p>
    </div>
  </div>
</template>