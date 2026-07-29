<script setup>
import { ref, onMounted } from "vue";
import api from "./api";

const project = ref("");
const backendStatus = ref("Loading...");

onMounted(async () => {
  try {
    const res = await api.get("/");

    project.value = res.data.project;
    backendStatus.value = res.data.status;
  } catch (error) {
    console.error(error);
    backendStatus.value = "Connection Failed";
  }
});
</script>

<template>
  <div class="container">
    <h1>GrayProject</h1>

    <p class="subtitle">
      Personal AI Operating System
    </p>

    <div class="card">
      <h2>Backend</h2>
      <p>{{ backendStatus }}</p>
    </div>

    <div class="card">
      <h2>Frontend</h2>
      <p>Running</p>
    </div>

    <div class="card">
      <h2>Project</h2>
      <p>{{ project }}</p>
    </div>

    <div class="card">
      <h2>Version</h2>
      <p>0.1.0</p>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 900px;
  margin: 80px auto;
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
}

.subtitle {
  color: #666;
  margin-bottom: 40px;
}

.card {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 20px;
  margin: 20px auto;
  max-width: 500px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}
</style>