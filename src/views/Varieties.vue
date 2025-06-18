<template>
  <div class="varieties-page">
    <h1>Lychee Varieties</h1>
    <div v-if="isLoading" class="loading">Loading varieties...</div>
    <div v-if="fetchError" class="error-message">
      Error fetching varieties: {{ fetchError }}
      <p><em>(Ensure your Flask backend is running and data is available.)</em></p>
    </div>
    <div v-if="!isLoading && !fetchError && varieties.length === 0" class="no-data">
      No lychee varieties found.
    </div>
    <div v-if="!isLoading && !fetchError && varieties.length > 0" class="varieties-grid">
      <div v-for="variety in varieties" :key="variety.id" class="variety-card">
        <img v-if="variety.image_url" :src="variety.image_url" :alt="`Image of ${variety.name}`" class="variety-image"/>
        <div v-else class="variety-image-placeholder">No Image</div>
        <div class="variety-info">
          <h3>{{ variety.name }}</h3>
          <p class="description">{{ truncateText(variety.description, 100) }}</p>
          <!-- Add a link/button for details later: <router-link :to="`/varieties/${variety.id}`">View Details</router-link> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiService from '@/services/apiService.js';

const varieties = ref([]);
const isLoading = ref(true);
const fetchError = ref(null);

const truncateText = (text, maxLength) => {
  if (!text) return 'No description available.';
  if (text.length <= maxLength) return text;
  return text.substr(0, maxLength) + '...';
};

onMounted(async () => {
  try {
    isLoading.value = true;
    fetchError.value = null;
    const data = await apiService.get('varieties');
    varieties.value = data;
  } catch (err) {
    console.error('Failed to fetch varieties:', err);
    fetchError.value = err.message || 'An unexpected error occurred.';
  } finally {
    isLoading.value = false;
  }
});
</script>

<style scoped>
.varieties-page {
  padding: 20px;
}
.loading, .error-message, .no-data {
  margin-top: 20px;
  padding: 15px;
  border-radius: 5px;
  text-align: center;
}
.loading { background-color: #e0e0e0; }
.error-message { background-color: #ffdddd; color: #d8000c; }
.no-data { background-color: #fff3cd; color: #856404; }

.varieties-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.variety-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}
.variety-image, .variety-image-placeholder {
  width: 100%;
  height: 180px;
  object-fit: cover;
  background-color: #f0f0f0; /* Placeholder background */
  display: flex;
  align-items: center;
  justify-content: center;
  color: #aaa; /* Placeholder text color */
}
.variety-info {
  padding: 15px;
  flex-grow: 1; /* Ensures info section takes available space */
}
.variety-info h3 {
  margin-top: 0;
  margin-bottom: 10px;
  font-size: 1.2em;
  color: #333;
}
.description {
  font-size: 0.9em;
  color: #666;
  line-height: 1.4;
}
</style>
