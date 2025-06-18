<template>
  <div class="comments-section">
    <h4>Comments</h4>
    <div v-if="fetchError" class="error-message">
      <p>Error fetching comments: {{ fetchError.message }}</p>
    </div>

    <form @submit.prevent="submitComment" class="comment-form">
      <div class="form-group">
        <label for="userName">Name:</label>
        <input type="text" id="userName" v-model="userName" required />
      </div>
      <div class="form-group">
        <label for="commentText">Comment:</label>
        <textarea id="commentText" v-model="newCommentText" required></textarea>
      </div>
      <button type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? 'Submitting...' : 'Submit Comment' }}
      </button>
      <div v-if="submitError" class="error-message submit-error">
        <p>Error submitting comment: {{ submitError.message }}</p>
      </div>
    </form>

    <div v-if="comments.length === 0 && !fetchError" class="no-comments">
      <p>No comments yet. Be the first to comment!</p>
    </div>

    <ul v-if="comments.length > 0" class="comments-list">
      <li v-for="comment in comments" :key="comment.id" class="comment-item">
        <p class="comment-author"><strong>{{ comment.user_name }}</strong> <span class="comment-date">({{ formatDate(comment.created_at) }})</span></p>
        <p class="comment-text">{{ comment.comment_text }}</p>
        <!-- Placeholder for nested replies if implemented later -->
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';

const props = defineProps({
  varietyId: {
    type: [String, Number],
    required: true
  }
});

const comments = ref([]);
const newCommentText = ref('');
const userName = ref('');
const fetchError = ref(null);
const submitError = ref(null);
const isSubmitting = ref(false);

const fetchComments = async (id) => {
  if (!id) return;
  fetchError.value = null;
  try {
    const response = await axios.get(`/api/lychee/varieties/${id}/comments`);
    comments.value = response.data;
  } catch (err) {
    console.error(`Error fetching comments for variety ID ${id}:`, err);
    fetchError.value = err;
    comments.value = []; // Clear comments on error
  }
};

const submitComment = async () => {
  if (!props.varietyId || !userName.value.trim() || !newCommentText.value.trim()) {
    submitError.value = { message: "Name and comment text cannot be empty." };
    return;
  }
  isSubmitting.value = true;
  submitError.value = null;
  try {
    await axios.post(`/api/lychee/varieties/${props.varietyId}/comments`, {
      user_name: userName.value,
      comment_text: newCommentText.value,
      // parent_comment_id: null // Or implement reply functionality
    });
    newCommentText.value = '';
    userName.value = ''; // Optionally clear username or persist it
    await fetchComments(props.varietyId); // Refresh comments list
  } catch (err) {
    console.error('Error submitting comment:', err);
    submitError.value = err.response ? err.response.data : err;
     if (!submitError.value.message && err.message) { // Fallback for network errors
        submitError.value = { message: err.message };
    }
  } finally {
    isSubmitting.value = false;
  }
};

onMounted(() => {
  if (props.varietyId) {
    fetchComments(props.varietyId);
  }
});

watch(() => props.varietyId, (newId) => {
  if (newId) {
    fetchComments(newId);
  } else {
    comments.value = []; // Clear comments if varietyId becomes invalid
    fetchError.value = null;
  }
});

const formatDate = (dateString) => {
  if (!dateString) return '';
  const options = { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};
</script>

<style scoped>
.comments-section {
  margin-top: 20px;
  padding: 15px;
  background-color: #f9f9f9;
  border-radius: 8px;
  font-family: Arial, sans-serif;
}

.comments-section h4 {
  margin-top: 0;
  margin-bottom: 15px;
  color: #333;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

.comment-form {
  margin-bottom: 20px;
  background-color: #fff;
  padding: 15px;
  border-radius: 6px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

.form-group input[type="text"],
.form-group textarea {
  width: calc(100% - 20px); /* Account for padding */
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 0.95em;
}

.form-group textarea {
  min-height: 80px;
  resize: vertical;
}

.comment-form button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
  font-size: 1em;
}

.comment-form button:hover:not(:disabled) {
  background-color: #0056b3;
}

.comment-form button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.comments-list {
  list-style-type: none;
  padding: 0;
}

.comment-item {
  background-color: #fff;
  border: 1px solid #e7e7e7;
  padding: 10px 15px;
  margin-bottom: 10px;
  border-radius: 6px;
}

.comment-author strong {
  color: #007bff;
}

.comment-date {
  font-size: 0.8em;
  color: #777;
  margin-left: 8px;
}

.comment-text {
  margin-top: 5px;
  line-height: 1.5;
  color: #444;
}

.no-comments {
  text-align: center;
  color: #777;
  padding: 15px;
}

.error-message {
  color: #d9534f;
  background-color: #f2dede;
  border: 1px solid #ebccd1;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 10px;
  font-size: 0.9em;
}
.submit-error {
  margin-top:10px;
}
</style>
