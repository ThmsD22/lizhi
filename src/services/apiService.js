// A simple API service using fetch
const API_BASE_URL = 'http://127.0.0.1:5000/api'; // Make sure this matches your Flask backend URL

export default {
  async get(endpoint) {
    try {
      const response = await fetch(`${API_BASE_URL}/${endpoint}`);
      if (!response.ok) {
        let errorMessage = `HTTP error! status: ${response.status}`;
        try {
            const errorBody = await response.json();
            errorMessage = errorBody.message || errorBody.error || errorMessage;
        } catch (e) { /* Ignore if error body is not JSON */ }
        throw new Error(errorMessage);
      }
      return await response.json();
    } catch (error) {
      console.error(`Error fetching data from ${endpoint}:`, error);
      throw error; // Re-throw to allow components to handle it
    }
  },

  async post(endpoint, data) {
    try {
      const response = await fetch(`${API_BASE_URL}/${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      if (!response.ok) {
        let errorMessage = `HTTP error! status: ${response.status}`;
        try {
            const errorBody = await response.json();
            errorMessage = errorBody.message || errorBody.error || errorMessage;
        } catch (e) { /* Ignore if error body is not JSON */ }
        throw new Error(errorMessage);
      }
      return await response.json();
    } catch (error) {
      console.error(`Error posting data to ${endpoint}:`, error);
      throw error; // Re-throw to allow components to handle it
    }
  }
};
