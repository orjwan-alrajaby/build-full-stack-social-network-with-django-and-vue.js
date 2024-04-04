import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useGetFeedPosts = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const getFeedPosts = async () => {
    isLoading.value = true;
    try {
      const response = await axios.get(URLS.allPosts);
      isError.value = false;
      error.value = null;
      data.value = response.data.posts;
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
    getFeedPosts
  };
};

export default useGetFeedPosts;
