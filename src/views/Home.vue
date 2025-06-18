<template>
  <div class="home">
    <h1>Welcome to the Lychee Culture Showcase</h1>
    <p>Discover the fascinating world of lychee varieties, their origins, and cultural significance.</p>

    <h2>Featured Lychee Varieties</h2>
    <div v-if="isLoading" class="loading">Loading varieties...</div>
    <div v-if="fetchError" class="error-message">
      Error fetching varieties: {{ fetchError }}
      <p><em>(Ensure your Flask backend is running at http://127.0.0.1:5000 and is accessible. You might also need to seed the database with some data.)</em></p>
    </div>
    <div v-if="!isLoading && !fetchError && varieties.length === 0" class="no-data">
      No lychee varieties found. Data might be unavailable or the backend is not seeded.
    </div>
    <ul v-if="!isLoading && !fetchError && varieties.length > 0" class="variety-list">
      <li v-for="variety in varieties" :key="variety.id" class="variety-item">
        <h3>{{ variety.name }}</h3>
        <p>{{ variety.description || 'No description available.' }}</p>
        <img v-if="variety.image_url" :src="variety.image_url" :alt="`Image of ${variety.name}`" class="variety-image"/>
        <a v-if="variety.video_url" :href="variety.video_url" target="_blank">Watch video</a>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiService from '@/services/apiService.js';

const varieties = ref([]);
const isLoading = ref(true);
const fetchError = ref(null);

onMounted(async () => {
  try {
    isLoading.value = true;
    fetchError.value = null;
    // Fetch only a few varieties for the home page, e.g., limit if API supports
    // For now, it fetches all and we can decide to slice or limit in template if needed
    const data = await apiService.get('varieties');
    varieties.value = data;
  } catch (err) {
    console.error('Failed to fetch varieties for Home page:', err);
    fetchError.value = err.message || 'An unexpected error occurred while loading data.';
  } finally {
    isLoading.value = false;
  }
});
</script>

<style scoped>
.home {
  padding: 20px;
  text-align: center;
}
.loading, .error-message, .no-data {
  margin-top: 20px;
  padding: 15px;
  border-radius: 5px;
}
.loading {
  background-color: #e0e0e0;
}
.error-message {
  background-color: #ffdddd;
  color: #d8000c;
  border: 1px solid #d8000c;
}
.error-message p {
  font-size: 0.9em;
  color: #555;
}
.no-data {
  background-color: #fff3cd;
  color: #856404;
  border: 1px solid #ffeeba;
}
.variety-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}
.variety-item {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 15px;
  width: 300px; /* Adjust as needed */
  box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
}
.variety-item h3 {
  margin-top: 0;
  color: #333;
}
.variety-image {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
  border-radius: 4px;
  margin-bottom: 10px;
}
</style>
