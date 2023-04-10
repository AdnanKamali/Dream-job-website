<script lang="ts" setup>
const props = defineProps({
  isMyJobPage: {
    type: Boolean,
  },
});

const isMyJobPage = computed(() => props.isMyJobPage);
</script>

<template>
  <div>
    <div class="p-6 flex items-center justify-between bg-gray-100">
      <div>
        <h1 class="text-xl font-semibold">The job position</h1>
        <p class="text-gray-600">The company name</p>
      </div>
      <div>
        <h1 class="font-semibold">Worldwide</h1>
        <p class="text-gray-600">$90-$120</p>
      </div>
      <div>
        <p>Posted Dec. 1. 2022</p>
      </div>
      <div class="space-x-4">
        <nuxt-link
          to="/browse/1"
          class="py-4 px-6 bg-teal-700 text-white rounded-xl"
          >Detail</nuxt-link
        >
        <nuxt-link
          v-if="isMyJobPage"
          to="/browse/1"
          class="py-4 px-6 bg-cyan-700 text-white rounded-xl"
          >Edit</nuxt-link
        >
        <nuxt-link
          v-if="isMyJobPage"
          to="/browse/1"
          class="py-4 px-6 bg-rose-700 text-white rounded-xl"
          >Delete</nuxt-link
        >
      </div>
    </div>
  </div>
</template>