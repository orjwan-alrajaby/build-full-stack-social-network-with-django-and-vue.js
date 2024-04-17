import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useCancelFriendRequest = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const cancelFriendRequest = async (receiverId) => {
    isLoading.value = true;
    try {
      const response = await axios.delete(URLS.deleteSentRequest(receiverId));
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
    cancelFriendRequest
  };
};

export default useCancelFriendRequest;
