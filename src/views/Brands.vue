<template>
  <div class="brands-page">
    <h1>Lychee Brands & Farmers</h1>
    <div v-if="isLoading" class="loading">Loading farmer information...</div>
    <div v-if="fetchError" class="error-message">
      Error fetching data: {{ fetchError }}
      <p><em>(Ensure your Flask backend is running and farmer data is available.)</em></p>
    </div>
    <div v-if="!isLoading && !fetchError && farmers.length === 0" class="no-data">
      No farmer or brand information found.
    </div>
    <div v-if="!isLoading && !fetchError && farmers.length > 0" class="farmers-grid">
      <div v-for="farmer in farmers" :key="farmer.id" class="farmer-card">
        <img v-if="farmer.image_url" :src="farmer.image_url" :alt="`Image of ${farmer.brand_name || farmer.name}`" class="farmer-image"/>
        <div v-else class="farmer-image-placeholder">No Image</div>
        <div class="farmer-info">
          <h3>{{ farmer.brand_name || farmer.name }}</h3>
          <p v-if="farmer.brand_name && farmer.name !== farmer.brand_name" class="farmer-name">Contact: {{ farmer.name }}</p>
          <p v-if="farmer.contact_info">Contact: {{ farmer.contact_info }}</p>
          <p v-if="farmer.area_id">Area ID: {{ farmer.area_id }}
             <!-- Display area_name if available from API -->
             <span v-if="farmer.area_name"> ({{ farmer.area_name }})</span>
          </p>
          <p v-if="farmer.variety_name">Grows: {{ farmer.variety_name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiService from '@/services/apiService.js';

const farmers = ref([]);
const isLoading = ref(true);
const fetchError = ref(null);

onMounted(async () => {
  try {
    isLoading.value = true;
    fetchError.value = null;
    const data = await apiService.get('farmers'); // API endpoint for all farmers
    // The 'farmers' endpoint in the backend now returns area_name and variety_name
    farmers.value = data;
  } catch (err) {
    console.error('Failed to fetch farmers:', err);
    fetchError.value = err.message || 'An unexpected error occurred.';
  } finally {
    isLoading.value = false;
  }
});
</script>

<style scoped>
.brands-page {
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

.farmers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.farmer-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  background-color: #fff;
}
.farmer-image, .farmer-image-placeholder {
  width: 100%;
  height: 200px; /* Adjust as needed */
  object-fit: cover;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #aaa;
}
.farmer-info {
  padding: 15px;
  flex-grow: 1;
}
.farmer-info h3 {
  margin-top: 0;
  margin-bottom: 10px;
  font-size: 1.3em;
  color: #333;
}
.farmer-info p {
  font-size: 0.9em;
  color: #555;
  margin-bottom: 5px;
}
.farmer-name {
  font-style: italic;
  color: #777;
}
</style>
