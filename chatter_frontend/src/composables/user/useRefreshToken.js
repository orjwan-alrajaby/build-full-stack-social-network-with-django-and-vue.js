import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useRefreshToken = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const handleRefreshToken = async (refreshToken) => {
    try {
      const response = await axios.post(URLS.refreshToken, {
        refresh: refreshToken
      })

      data.value = response.data;
      return {
        status: "success",
        message: "Refreshed token successfully."
      }
    } catch (error) {
      console.error(error);
      isError.value = true;
      error.value = error;
      return {
        status: "error",
        message: "Failed to refresh token. Please try again later."
      }
    }
  }
  return {
    data,
    isLoading,
    error,
    isError,
    handleRefreshToken
  };
}

export default useRefreshToken;
