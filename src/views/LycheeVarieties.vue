<template>
  <div class="lychee-varieties-container">
    <h2>Lychee Varieties</h2>
    <div v-if="error" class="error-message">
      <p>Error fetching varieties: {{ error.message }}</p>
    </div>
    <div v-if="!varieties.length && !error" class="loading-message">
      <p>Loading varieties...</p>
    </div>
    <ul v-if="varieties.length" class="varieties-list">
      <li v-for="variety in varieties" :key="variety.id" class="variety-item">
        <router-link :to="{ name: 'LycheeDetail', params: { id: variety.id } }">
          <h3>{{ variety.name }}</h3>
          <img v-if="variety.image_url" :src="variety.image_url" :alt="variety.name" class="variety-image" />
          <p v-if="variety.description">{{ variety.description.substring(0, 100) }}...</p>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const varieties = ref([]);
const error = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get('/api/lychee/varieties');
    if (response.data && Array.isArray(response.data)) {
      varieties.value = response.data;
    } else {
      console.warn('Unexpected response format:', response.data);
      varieties.value = []; // Set to empty array if format is not as expected
    }
  } catch (err) {
    console.error('Error fetching lychee varieties:', err);
    error.value = err;
  }
});
</script>

<style scoped>
.lychee-varieties-container {
  padding: 20px;
  font-family: Arial, sans-serif;
}

.varieties-list {
  list-style-type: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.variety-item {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  transition: box-shadow 0.3s ease;
}

.variety-item:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.variety-item a {
  text-decoration: none;
  color: inherit;
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

.error-message, .loading-message {
  color: #d9534f;
  padding: 10px;
  border: 1px solid #d9534f;
  border-radius: 4px;
}

.loading-message {
  color: #5bc0de;
  border-color: #5bc0de;
}
</style>
