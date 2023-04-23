<script setup lang="ts">
const props = defineProps(["label", "type", "modelValue"]);
const emit = defineEmits(["update:modelValue"]);
const modelValue = computed({
  get: () => props.modelValue,
  set: (value) => emit("update:modelValue", value),
});
</script>

<template>
  <div>
    <label>{{ props.label }}</label>
    <input
      :type="props.type ?? 'text'"
      :value="props.modelValue"
      v-model="modelValue"
      class="w-full mt-2 mb-2 p-4 rounded-xl bg-gray-100"
    />
  </div>
</template>