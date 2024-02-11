import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useGetConversation = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const getConversation = async (accessToken, id) => {
    isLoading.value = true;
    axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
    try {
      const response = await axios.get(URLS.getConversation(id));
      isError.value = false;
      error.value = null;
      data.value = response.data.conversation;
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
    getConversation
  };
};

export default useGetConversation;
