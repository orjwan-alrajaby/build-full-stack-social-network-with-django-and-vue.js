<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div class="order-last col-span-3 p-4 space-y-4 border rounded-lg main-left lg:col-span-1 lg:order-none bg-gray-950 border-lime-300">
        <button v-for="conversation in conversations" :key="conversation.id" @click="selectConversation(conversation.id)" class="block w-full p-3 bg-gray-900 rounded-lg" :class="{'border-2 border-lime-300': activeConversationId === conversation.id,
        'border-2 border-gray-900': activeConversationId !== conversation.id
      }">
          <span class="flex items-center justify-between">
            <span class="flex items-center space-x-4">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />
              <template v-for="user in conversation.users">
                <p class="text-xs" v-if="user.id !== userStore.user.id" :key="user.id">
                  <strong>{{ user.name }}</strong>
                </p>
              </template>
            </span>

            <span class="text-xs text-slate-500">{{ conversation.modified_at_formatted }} ago</span>
          </span>
        </button>
    </div>

    <div
      class="order-first col-span-3 space-y-4 border rounded-lg main-center lg:col-span-2 lg:order-none bg-gray-950 border-lime-300"
    >
    <div class="flex flex-col items-center justify-between">
          <div class="flex flex-col flex-grow w-full p-4 overflow-y-auto h-[420px]">
          <template v-for="message in activeConversation.messages">
           <div class="flex justify-end w-full max-w-md mt-4 ml-auto space-x-3" v-if="message.created_by.id === userStore.user.id" :key="message.id">
            <div>
              <div
                class="p-3 rounded-l-lg rounded-br-lg bg-lime-400 text-slate-900"
              >
                <p class="text-sm">
                  {{ message.body }}
                </p>
              </div>
              <span class="block mt-2 text-xs text-right text-lime-600">{{ message.created_at_formatted }}</span>
            </div>
            <div class="flex-shrink-0 w-10 h-10 bg-gray-300 rounded-full">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />
            </div>
          </div>
          <div class="flex w-full max-w-md mt-6 space-x-3" v-if="message.created_by.id !== userStore.user.id" :key="message.id">
            <div class="flex-shrink-0 w-10 h-10 bg-gray-300 rounded-full">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />
            </div>
            <div>
              <div
                class="p-3 rounded-r-lg rounded-bl-lg bg-slate-600 text-slate-200"
              >
                <p class="text-sm">{{ message.body }}</p>
              </div>
              <span class="block mt-2 text-xs text-slate-500">{{message.created_at_formatted}}</span>
            </div>
          </div>
          </template>
        </div>
          <form
      class="w-full pt-4 rounded-lg"
      @submit.prevent="submitForm"
    >
      <div class="flex p-4 space-x-4 bg-gray-900 rounded-lg">
        <img
          src="https://mighty.tools/mockmind-api/content/human/49.jpg"
          class="w-full rounded-full max-w-10"
        />
        <input
          type="search"
          class="w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          placeholder="What do you think?"
          v-model="messageBody"
        />

        <button
          class="px-4 py-2 mx-2 font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-lime-900 disabled:cursor-not-allowed"
          :disabled="!messageBody"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 mx-auto"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5"
            />
          </svg>
        </button>
      </div>
    </form>
    </div>

    </div>
  </div>
</template>

<script>
import useGetConversationList from "@/composition-functions/useGetConversationList"
import useGetConversation from "@/composition-functions/useGetConversation"
import useSendMessage from "@/composition-functions/useSendMessage"
import { useUserStore } from "@/stores/user";
import { useToast } from "vue-toastification";
  
export default {
  setup() { 
    const toast = useToast();
    const userStore = useUserStore();
    const { data: conversationsList, getConversationList } = useGetConversationList();
    const { data: singleConversation, getConversation } = useGetConversation();
    const { data: conversationMessage, sendMessage } = useSendMessage();

    return {
      toast,
      userStore,
      getConversationList,
      conversationsList,
      getConversation,
      singleConversation,
      sendMessage,
      conversationMessage
    }
  },
  data() {
    return {
      messageBody: "",
      conversations: [],
      activeConversationId: "",
      activeConversation: {
        messages: []
      },
    }
   },
  methods: {
    getConversations(userId) {
     this.getConversationList(userId).then((res) => {
       if (res.status === "success") {
         this.conversations = this.conversationsList;
         this.activeConversation = this.conversationsList[0];
         this.activeConversationId = this.activeConversation.id;
         this.getSingleConversation(this.userStore.user.accessToken, this.activeConversationId);
      } else {
        this.toast.error(`Failed to fetch your conversations.`, {
          toastClassName: "!bg-red-700 !text-slate-200",
        });
      }
    })
    },
    getSingleConversation(accessToken, id) { 
      this.getConversation(accessToken, id).then((res) => {
        if (res.status === "success") {
          this.activeConversation = this.singleConversation;
        } else {
          this.toast.error(`Failed to fetch conversation.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      })
    },
    selectConversation(id) { 
      this.activeConversationId = id;
      this.getSingleConversation(this.userStore.user.accessToken, id)
    },
    submitForm() {
      this.sendMessage(this.activeConversationId, this.messageBody).then(res => {
        if (res.status === "success" && res.code === 201) {
          this.activeConversation.messages.push(this.conversationMessage)
        } else {
          this.toast.error(`Failed to send message.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      })
    }
  },
  mounted() {
    this.getConversations(this.userStore.user.accessToken);
  },
}
</script>