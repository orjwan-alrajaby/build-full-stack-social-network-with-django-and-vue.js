import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useLogin = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const handleLogin = async (form) => {
    isLoading.value = true;
    try {
      const response = await axios.post(URLS.login, form);
      data.value = response.data;
      return {
        status: "success",
        message: "You've been logged in, successfully!",
        data: response.data
      }
    } catch (error) {
      console.error(error);
      isError.value = true;
      error.value = error;

      let message = "";
      if (error.response.status === 401) {
        message = "No user found for the entered credentials!";
      } else {
        message = error.message;
      }
      return {
        status: "error",
        message,
        error
      };
    } finally {
      isLoading.value = false;
    }
  }

  return {
    data,
    isLoading,
    error,
    isError,
    handleLogin
  };
}

export default useLogin;
