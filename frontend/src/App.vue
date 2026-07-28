<script setup>
import { ref, onMounted } from "vue";
import request from "./api/request";

const backend = ref("");

onMounted(async () => {
  try {
    const res = await request.get("/");
    backend.value = JSON.stringify(res.data);
  } catch (err) {
    backend.value = err.message;
  }
});
</script>

<template>
  <div>
    <h1>GrayProject Frontend</h1>

    <p>{{ backend }}</p>
  </div>
</template>