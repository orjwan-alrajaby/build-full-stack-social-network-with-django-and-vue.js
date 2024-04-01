import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useGetPostDetails = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const getPost = async (id) => {
    isLoading.value = true;
    try {
      const response = await axios.get(URLS.getPost(id));
      isError.value = false;
      error.value = null;
      data.value = response.data.post;
      return { status: "success", code: response.status }
    } catch (error) {
      error.value = error;
      isError.value = true;
      return { status: "error" }
    } finally {
      isLoading.value = false;
    }
  }

  return {
    data,
    isLoading,
    error,
    isError,
    getPost
  };
}

export default useGetPostDetails;