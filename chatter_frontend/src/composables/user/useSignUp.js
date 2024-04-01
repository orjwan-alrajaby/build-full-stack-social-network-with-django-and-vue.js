import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useSignUp = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const handleSignUp = async (form) => {
    isLoading.value = true;
    try {
      const response = await axios.post(URLS.signUp, form);
      data.value = response.data;
      if (response.data.status === 201) {
        return {
          status: "success",
          message: "The user has been registered successfully. Now please log in."
        }
      } else {
        return {
          status: "error",
          message: response.data.message
        }
      }
    } catch (error) {
      console.error(error);
      isError.value = true;
      error.value = error;
      return {
        status: "error",
        message: "Failed to sign user up."
      }
    } finally {
      isLoading.value = false;
    }
  }

  return {
    data,
    isLoading,
    error,
    isError,
    handleSignUp
  };
}

export default useSignUp;
