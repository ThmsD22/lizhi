<template>
  <div class="farmer-card" v-if="farmer">
    <div class="card-header">
      <img v-if="farmer.profile_picture_url" :src="farmer.profile_picture_url" :alt="farmer.name" class="profile-picture" />
      <div class="farmer-info">
        <h3 class="farmer-name">{{ farmer.name }}</h3>
        <p v-if="farmer.brand_name" class="brand-name">{{ farmer.brand_name }}</p>
      </div>
    </div>
    <div class="card-body">
      <p v-if="farmer.bio" class="bio">{{ farmer.bio }}</p>
      <p v-if="farmer.contact_info" class="contact-info">
        <strong>Contact:</strong> {{ farmer.contact_info }}
      </p>
      <div v-if="farmer.associated_varieties_ids && farmer.associated_varieties_ids.length" class="associated-varieties">
        <strong>Associated Varieties IDs:</strong> {{ farmer.associated_varieties_ids.join(', ') }}
      </div>
    </div>
  </div>
</template>

<script setup>
// eslint-disable-next-line no-unused-vars
const props = defineProps({
  farmer: {
    type: Object,
    required: true,
    default: () => null // Provide a default to prevent errors if prop isn't immediately available
  }
});
</script>

<style scoped>
.farmer-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  font-family: Arial, sans-serif;
  max-width: 400px; /* Constrain width for better card appearance */
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.profile-picture {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin-right: 15px;
  object-fit: cover;
  border: 2px solid #f0f0f0;
}

.farmer-info {
  flex-grow: 1;
}

.farmer-name {
  margin: 0;
  font-size: 1.4em;
  color: #333;
}

.brand-name {
  margin: 0;
  font-size: 1em;
  color: #555;
}

.bio {
  font-size: 0.95em;
  line-height: 1.5;
  color: #444;
  margin-bottom: 10px;
}

.contact-info {
  font-size: 0.9em;
  color: #666;
  margin-bottom: 10px;
}

.contact-info strong {
  color: #333;
}

.associated-varieties {
  font-size: 0.85em;
  color: #777;
}

.associated-varieties strong {
  color: #333;
}
</style>
