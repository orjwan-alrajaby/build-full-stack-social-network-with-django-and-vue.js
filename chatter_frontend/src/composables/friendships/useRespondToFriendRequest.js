import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useRespondToFriendRequest = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const respondToFriendRequest = async (status, senderId) => {
    isLoading.value = true;
    try {
      const response = await axios.post(URLS.respondToFriendRequest(status, senderId));
      isError.value = false;
      error.value = null;
      data.value = response.data;
      return { status: "success", code: response.status };
    } catch (error) {
      error.value = error;
      isError.value = true;
      return { status: "error" };
    } finally {
      isLoading.value = false;
    }
  };

  return {
    data,
    isLoading,
    error,
    isError,
    respondToFriendRequest
  };
};

export default useRespondToFriendRequest;
