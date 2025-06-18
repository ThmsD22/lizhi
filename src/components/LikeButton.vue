<template>
  <div class="like-section">
    <button @click="addLike" :disabled="isProcessing || likedByUser" class="like-button">
      <span v-if="likedByUser">❤️ Liked!</span>
      <span v-else>🤍 Like</span>
    </button>
    <p class="like-count">Likes: {{ likeCountDisplay }}</p>
    <div v-if="error" class="error-message">
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import axios from 'axios';

const props = defineProps({
  varietyId: {
    type: [String, Number],
    required: true
  }
});

const likeCount = ref(0);
const likedByUser = ref(false); // Simulates if current user has liked. True state needs auth.
const isProcessing = ref(false);
const error = ref(null);

const likeCountDisplay = computed(() => {
    return likeCount.value === null ? 'Loading...' : likeCount.value;
});

const fetchLikeCount = async (id) => {
  if (!id) return;
  isProcessing.value = true;
  error.value = null;
  try {
    const response = await axios.get(`/api/lychee/varieties/${id}/likes`);
    likeCount.value = response.data.count !== undefined ? response.data.count : 0;
  } catch (err) {
    console.error(`Error fetching likes for variety ID ${id}:`, err);
    error.value = 'Could not fetch like count.';
    likeCount.value = 0; // Reset or handle error state
  } finally {
    isProcessing.value = false;
  }
};

const addLike = async () => {
  if (!props.varietyId || likedByUser.value) return; // Don't do anything if already liked
  isProcessing.value = true;
  error.value = null;
  try {
    // For now, hardcode user_id as 1, as per subtask instructions.
    // In a real app, this would come from user authentication state.
    const response = await axios.post(`/api/lychee/varieties/${props.varietyId}/like`, { user_id: 1 });

    if (response.data.success) {
      likedByUser.value = true; // Visually indicate like
      // Increment count locally or refetch. Refetching is safer for consistency.
      await fetchLikeCount(props.varietyId);
    } else {
      // Handle specific error messages from backend, e.g., already liked by this user
      error.value = response.data.message || 'Could not add like.';
      if (response.status === 409) { // Conflict, e.g. already liked
          likedByUser.value = true; // User might have liked in another session/tab
      }
    }
  } catch (err) {
    console.error('Error adding like:', err);
    if (err.response && err.response.status === 409) {
        error.value = err.response.data.message || 'You have already liked this variety.';
        likedByUser.value = true; // Ensure UI reflects this state
    } else {
        error.value = 'An unexpected error occurred while adding your like.';
    }
  } finally {
    isProcessing.value = false;
  }
};

onMounted(() => {
  if (props.varietyId) {
    fetchLikeCount(props.varietyId);
  }
});

watch(() => props.varietyId, (newId) => {
  likedByUser.value = false; // Reset liked state for new variety
  if (newId) {
    fetchLikeCount(newId);
  } else {
    likeCount.value = 0;
    error.value = null;
  }
});

</script>

<style scoped>
.like-section {
  margin-top: 20px;
  padding: 15px;
  background-color: #f9f9f9;
  border-radius: 8px;
  text-align: center; /* Center button and text */
  font-family: Arial, sans-serif;
}

.like-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.2s, transform 0.1s;
  margin-bottom: 10px;
}

.like-button:hover:not(:disabled) {
  background-color: #0056b3;
  transform: scale(1.02);
}

.like-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.like-button span {
  margin-right: 5px;
}

.like-count {
  font-size: 1.1em;
  color: #333;
  margin: 0;
}

.error-message {
  color: #d9534f;
  font-size: 0.9em;
  margin-top: 10px;
}
</style>
