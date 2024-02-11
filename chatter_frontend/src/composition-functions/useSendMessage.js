import { ref } from 'vue';
import axios from 'axios';
import URLS from '@/constants/urls';

const useSendMessage = () => {
  const data = ref(null);
  const error = ref(null);
  const isLoading = ref(false);
  const isError = ref(false);

  const sendMessage = async (conversationId, messageBody) => {
    isLoading.value = true;
    try {
      const response = await axios.post(URLS.sendMessage(conversationId), {
        body: messageBody
      });
      isError.value = false;
      error.value = null;
      data.value = response.data.conversation_message;
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
    sendMessage
  };
};

export default useSendMessage;
