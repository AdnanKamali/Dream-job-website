<script setup lang="ts">
import { onMounted } from "vue";
import { useUserStore } from "~/stores/user";
import { JobT } from "~/types/job";

const useStore = useUserStore();
const router = useRouter();

const myJobs = ref<JobT[]>([]);

async function getMyJobs() {
  try {
    const response: JobT[] = await $fetch(
      "http://127.0.0.1:8000/api/v1/jobs/my/",
      {
        headers: {
          Authorization: `Token ${useStore.user.token}`,
        },
      }
    );
    myJobs.value = response;
  } catch (error: any) {
    console.log("Error");
  }
}

function deleteJobView(id: number) {
  myJobs.value = myJobs.value.filter((job) => job.id !== id);
}

onMounted(() => {
  if (useStore.user.isAuthenticated) getMyJobs();
  else router.push("/login");
});
</script>

<template>
  <Html>
    <Head>
      <Title>My Jobs</Title>
    </Head>
  </Html>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">My Jobs</h1>
    <div class="space-y-4">
      <Job
        v-for="myJob in myJobs"
        :key="myJob.id"
        :job="myJob"
        :is-my-job-page="true"
        @delete-job-view="deleteJobView"
      />
    </div>
  </div>
</template>