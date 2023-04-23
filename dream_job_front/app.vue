<script setup lang="ts">
import { onMounted } from "vue";
import { useUserStore } from "@/stores/user";

const useStore = useUserStore();

onMounted(() => useStore.initStore());
</script>

<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
