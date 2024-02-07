import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useLikePost = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const createLikeForPost = async (id) => {
    isLoading.value = true;
    try {
      const response = await axios.post(URLS.likePost(id));
      isError.value = false;
      error.value = null;
      data.value = response;
      return {status: "success", code: response.status}
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
    createLikeForPost
  };
}

export default useLikePost;