import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useStartConversation = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const startConversation = async (userId) => {
    isLoading.value = true;
    try {
      const response = await axios.get(URLS.startConversation(userId));
      isError.value = false;
      error.value = null;
      data.value = response.data.conversation;
      return { status: "success", code: response.status };
    } catch (error) {
      error.value = error;
      isError.value = true;
      return { status: "error" , error};
    } finally {
      isLoading.value = false;
    }
  };

  return {
    data,
    isLoading,
    error,
    isError,
    startConversation
  };
};

export default useStartConversation;
