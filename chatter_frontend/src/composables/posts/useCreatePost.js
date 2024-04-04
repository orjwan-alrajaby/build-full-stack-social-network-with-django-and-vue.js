import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useCreatePost = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const createPost = async (body) => {
    isLoading.value = true;
    try {
      const response = await axios.post(URLS.createPost, {
        body
      });
      isError.value = false;
      error.value = null;
      data.value = response.data.post;
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
    createPost
  };
};

export default useCreatePost;
