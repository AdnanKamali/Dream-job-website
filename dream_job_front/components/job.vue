<script lang="ts" setup>
import { JobT } from "@/types/job";
import { useUserStore } from "~/stores/user";

const useStore = useUserStore();

const props = defineProps({
  isMyJobPage: {
    type: Boolean,
  },
  job: {
    type: Object,
  },
});

const job = computed(() => props.job as JobT);

const emitDeleteJobView = defineEmits(["deleteJobView"]);

async function deleteJob(id: number) {
  try {
    const response = await $fetch(
      "http://127.0.0.1:8000/api/v1/jobs/" + id + "/delete/",
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + useStore.user.token,
        },
      }
    );
    emitDeleteJobView("deleteJobView", id);
  } catch (err) {
    console.log("Error", err);
  }
}
</script>

<template>
  <div>
    <div class="p-6 flex items-center justify-between bg-gray-100">
      <div>
        <h1 class="text-xl font-semibold">{{ job.title }}</h1>
        <p class="text-gray-600">{{ job.company_name }}</p>
      </div>
      <div>
        <h1 class="font-semibold">{{ job.position_location }}</h1>
        <p class="text-gray-600 text-center">${{ job.position_salary }}</p>
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
          v-if="props.isMyJobPage"
          :to="`/edit/${job.id}`"
          class="py-4 px-6 bg-cyan-700 text-white rounded-xl"
          >Edit</nuxt-link
        >
        <a
          v-if="props.isMyJobPage"
          @click="deleteJob(job.id)"
          class="py-4 px-6 bg-rose-700 text-white rounded-xl cursor-pointer"
          >Delete</a
        >
      </div>
    </div>
  </div>
</template>