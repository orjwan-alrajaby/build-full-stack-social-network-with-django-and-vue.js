import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useCreateCommentOnPost = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const createCommentOnPost = async (postId, commentBody) => {
    isLoading.value = true;
    try {
      const response = await axios.post(URLS.createComment(postId), {
        body: commentBody
      });
      isError.value = false;
      error.value = null;
      data.value = response.data; // Assuming the response contains the created comment
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
    createCommentOnPost
  };
};

export default useCreateCommentOnPost;
