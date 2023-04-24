<script setup lang="ts">
import { useUserStore } from "~/stores/user";
import { Category } from "~/types/category";

// Use this for better error view
enum Labels {
  title = "Title",
  description = "Description",
  category = "Category",
  position_salary = "Salary",
  position_location = "Location",
  company_name = "Company name",
  company_location = "Company location",
  company_email = "Company e-mail",
}

const useStore = useUserStore();
const router = useRouter();

// Create job information for send to server

const jobModel = reactive({
  category: "",
  title: "",
  description: "",
  position_salary: "",
  position_location: "",
  company_name: "",
  company_location: "",
  company_email: "",
});

const errors = ref<string[]>([]);

const { data: categories } = await useFetch<Category[]>(
  "http://127.0.0.1:8000/api/v1/jobs/categories/"
);

function fieldsEmptyCheck() {
  for (const [key, value] of Object.entries(jobModel)) {
    if (!value) {
      // @ts-ignore
      errors.value.push(`The field of ${Labels[key]} should not be empty`);
    }
  }
}

async function createJobSubmit() {
  errors.value = [];

  fieldsEmptyCheck();
  if (errors.value.length) {
    return;
  }
  try {
    console.log("Try");
    const response = await $fetch("http://127.0.0.1:8000/api/v1/jobs/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${useStore.user.token}`,
      },
      body: jobModel,
    });
  } catch (er: any) {
    console.log(er);
  }
}
onMounted(() => {
  if (!useStore.user.isAuthenticated) {
    router.push("/login");
  }
});
</script>

<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">Create job</h1>
    <form @submit.prevent="createJobSubmit">
      <div>
        <label>Category</label>
        <select
          v-model="jobModel.category"
          class="w-full mt-2 mb-2 p-4 rounded-xl bg-gray-100"
        >
          <option value="">Select category</option>
          <option
            v-for="category in categories"
            :key="category.id"
            :value="category.id"
          >
            {{ category.title }}
          </option>
        </select>
      </div>

      <CreateJobInput label="Title" v-model="jobModel.title" />

      <div>
        <label>Description</label>
        <textarea
          type="text"
          v-model="jobModel.description"
          class="w-full mt-2 mb-2 p-4 rounded-xl bg-gray-100"
        ></textarea>
      </div>

      <CreateJobInput label="Salary" v-model="jobModel.position_salary" />

      <CreateJobInput label="Location" v-model="jobModel.position_location" />

      <CreateJobInput label="Company name" v-model="jobModel.company_name" />

      <CreateJobInput
        label="Company location"
        v-model="jobModel.company_location"
      />

      <CreateJobInput
        label="Company e-mail"
        type="email"
        v-model="jobModel.company_email"
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
        Submit
      </button>
    </form>
  </div>
</template>