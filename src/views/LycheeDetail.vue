<template>
  <div class="lychee-detail-container">
    <div v-if="error" class="error-message">
      <p>Error fetching variety details: {{ error.message }}</p>
      <router-link to="/lychee-varieties">Back to varieties</router-link>
    </div>
    <div v-if="varietyDetail" class="variety-content">
      <h2>{{ varietyDetail.name }}</h2>

      <img v-if="varietyDetail.image_url" :src="varietyDetail.image_url" :alt="varietyDetail.name" class="variety-image-detail" />

      <p v-if="varietyDetail.description" class="description">{{ varietyDetail.description }}</p>

      <div v-if="varietyDetail.video_url" class="video-section">
        <h4>Promotional Video</h4>
        <a :href="varietyDetail.video_url" target="_blank" rel="noopener noreferrer">Watch Video</a>
        <!-- Basic iframe embed attempt for YouTube -->
        <div v-if="isYouTubeUrl(varietyDetail.video_url)" class="video-embed">
          <iframe :src="getYouTubeEmbedUrl(varietyDetail.video_url)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
      </div>

      <div v-if="varietyDetail.origin_story" class="content-section">
        <h4>Origin Story</h4>
        <p>{{ varietyDetail.origin_story }}</p>
      </div>

      <div v-if="varietyDetail.cultivation_techniques" class="content-section">
        <h4>Cultivation Techniques</h4>
        <p>{{ varietyDetail.cultivation_techniques }}</p>
      </div>

      <div class="placeholder-section">
        <h4>Production Areas</h4>
        <ProductionMap :areas="productionAreas" />
      </div>

      <CommentsSection v-if="varietyDetail && varietyDetail.id" :variety-id="varietyDetail.id" />

      <LikeButton v-if="varietyDetail && varietyDetail.id" :variety-id="varietyDetail.id" />

      <div class="content-section farmer-profiles-section" v-if="farmers.length">
        <h4>Farmer Profiles</h4>
        <FarmerCard v-for="farmer in farmers" :key="farmer.id" :farmer="farmer" />
        <!--
          Alternatively, to display only the first farmer or a specific one:
          <FarmerCard v-if="farmers.length" :farmer="farmers[0]" />
        -->
      </div>
      <div v-else-if="farmersError" class="error-message">
        <p>Could not load farmer profiles: {{ farmersError.message }}</p>
      </div>

      <router-link to="/lychee-varieties" class="back-link">Back to varieties list</router-link>
    </div>
    <div v-if="!varietyDetail && !error" class="loading-message">
      <p>Loading variety details...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import ProductionMap from '@/components/ProductionMap.vue';
import FarmerCard from '@/components/FarmerCard.vue';
import CommentsSection from '@/components/CommentsSection.vue';
import LikeButton from '@/components/LikeButton.vue';

const route = useRoute();
const varietyDetail = ref(null);
const productionAreas = ref([]); // Placeholder for areas data
const error = ref(null); // For variety detail fetching
const farmers = ref([]);
const farmersError = ref(null); // For farmers fetching

const fetchVarietyDetail = async (id) => {
  if (!id) return;
  error.value = null;
  varietyDetail.value = null;
  try {
    const response = await axios.get(`/api/lychee/varieties/${id}`);
    varietyDetail.value = response.data;
    //
    // TODO: In a real scenario, you would also fetch production areas here:
    // e.g., const areasResponse = await axios.get(`/api/lychee/varieties/${id}/areas`);
    // productionAreas.value = areasResponse.data;
    // For now, we'll use placeholder data if needed or pass empty
  } catch (err) {
    console.error(`Error fetching details for variety ID ${id}:`, err);
    error.value = err;
  }
};

onMounted(() => {
  fetchVarietyDetail(route.params.id);
  fetchFarmerProfiles();
  // Example: Fetch production areas
  // fetchProductionAreas(route.params.id);
});

const fetchFarmerProfiles = async () => {
  try {
    const response = await axios.get('/api/lychee/farmers');
    farmers.value = response.data;
  } catch (err) {
    console.error('Error fetching farmer profiles:', err);
    farmersError.value = err;
  }
};

// Example function to fetch production areas (currently not called automatically)
// const fetchProductionAreas = async (id) => {
//   try {
//     const response = await axios.get(`/api/lychee/varieties/${id}/areas`);
//     productionAreas.value = response.data;
//   } catch (err) {
//     console.error(`Error fetching production areas for variety ID ${id}:`, err);
//     // Handle error appropriately
//   }
// };

watch(() => route.params.id, (newId) => {
  if (newId) {
    fetchVarietyDetail(newId);
    // Optionally, re-fetch farmers if relevant to the new variety ID,
    // though current API fetches all.
    // fetchFarmerProfiles();
  }
});

// Helper to attempt YouTube embed
const isYouTubeUrl = (url) => {
  if (!url) return false;
  return url.includes('youtube.com/watch') || url.includes('youtu.be/');
};

const getYouTubeEmbedUrl = (url) => {
  if (!url) return '';
  let videoId;
  if (url.includes('youtube.com/watch')) {
    videoId = url.split('v=')[1];
    const ampersandPosition = videoId.indexOf('&');
    if (ampersandPosition !== -1) {
      videoId = videoId.substring(0, ampersandPosition);
    }
  } else if (url.includes('youtu.be/')) {
    videoId = url.split('youtu.be/')[1];
  }
  return videoId ? `https://www.youtube.com/embed/${videoId}` : '';
};
</script>

<style scoped>
.lychee-detail-container {
  padding: 20px;
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
}

.variety-content h2 {
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

.variety-image-detail {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 20px;
}

.description, .content-section p {
  line-height: 1.6;
  color: #555;
  margin-bottom: 15px;
}

.content-section h4, .video-section h4, .placeholder-section h4 {
  color: #444;
  margin-top: 20px;
  margin-bottom: 10px;
  border-bottom: 1px solid #eee;
  padding-bottom: 5px;
}

.video-section a {
  color: #007bff;
  text-decoration: none;
}
.video-section a:hover {
  text-decoration: underline;
}

.video-embed {
  margin-top: 10px;
  position: relative;
  padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
  height: 0;
  overflow: hidden;
}

.video-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 8px;
}

.placeholder-section, .farmer-profiles-section {
  background-color: #f9f9f9;
  border: 1px dashed #ccc;
  padding: 15px;
  margin-top: 20px;
  border-radius: 4px;
  text-align: center;
  color: #777;
}
.farmer-profiles-section {
  text-align: left; /* Align farmer cards normally */
  padding: 15px;
  background-color: #fff; /* Or a light background */
  border-style: solid;
}

.error-message, .loading-message {
  text-align: center;
  padding: 20px;
  border-radius: 4px;
}

.error-message {
  color: #d9534f;
  background-color: #f2dede;
  border: 1px solid #ebccd1;
  margin-top: 10px; /* Add some space if it appears */
}

.loading-message {
  color: #31708f;
  background-color: #d9edf7;
  border: 1px solid #bce8f1;
}

.back-link {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.back-link:hover {
  background-color: #0056b3;
}
</style>
