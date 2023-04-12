<script lang="ts" setup>
import { JobT } from "@/types/job";

const props = defineProps({
  isMyJobPage: {
    type: Boolean,
  },
  job: {
    type: Object,
  },
});

const isMyJobPage = computed(() => props.isMyJobPage);
const job = computed(() => props.job as JobT);
</script>

<template>
  <div>
    <div class="p-6 flex items-center justify-between bg-gray-100">
      <div>
        <h1 class="text-xl font-semibold">{{ job.position_location }}</h1>
        <p class="text-gray-600">{{ job.company_name }}</p>
      </div>
      <div>
        <h1 class="font-semibold">Worldwide</h1>
        <p class="text-gray-600">{{ job.position_salary }}</p>
      </div>
      <div>
        <p>Posted {{ job.created_at_formatted }}</p>
      </div>
      <div class="space-x-4">
        <nuxt-link
          :to="`/browse/${job.id}`"
          class="py-4 px-6 bg-teal-700 text-white rounded-xl"
          >Detail</nuxt-link
        >
        <nuxt-link
          v-if="isMyJobPage"
          :to="`/browse/${job.id}`"
          class="py-4 px-6 bg-cyan-700 text-white rounded-xl"
          >Edit</nuxt-link
        >
        <nuxt-link
          v-if="isMyJobPage"
          :to="`/browse/${job.id}`"
          class="py-4 px-6 bg-rose-700 text-white rounded-xl"
          >Delete</nuxt-link
        >
      </div>
    </div>
  </div>
</template>