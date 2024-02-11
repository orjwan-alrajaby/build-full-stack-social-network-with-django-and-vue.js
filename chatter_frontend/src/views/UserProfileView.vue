<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div class="order-last col-span-3 space-y-4 main-center lg:col-span-2 lg:order-first">
      <div class="border rounded-lg bg-gray-950 border-lime-300" v-if="this.$route.params.id === userStore.user.id">
        <div class="p-4">
          <textarea
            class="w-full p-4 rounded-lg bg-slate-200 text-slate-950"
            placeholder="What are you thinking about?"
            v-model="body"
          ></textarea>
        </div>

        <div
          class="flex items-center justify-end pt-4 m-4 mt-0 border-t border-slate-700"
        >
          <form method="POST" @submit.prevent="submitForm">
            <button
              class="w-16 h-10 mx-2 font-medium bg-transparent border rounded-lg text-lime-300 border-lime-300"
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6 mx-auto"
              ><path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
                />
              </svg>
            </button>

            <button
              class="w-16 h-10 mx-2 font-medium rounded-lg bg-lime-300 text-slate-900 disabled:bg-lime-900 disabled:cursor-not-allowed"
              :disabled="!body || postsStore.posts.newPost.isLoading"
              @click="submitForm"
              >
              <svg v-if="postsStore.posts.newPost.isLoading" xmlns="http://www.w3.org/2000/svg" width="1.5rem" height="1.5rem" viewBox="0 0 24 24" class="mx-auto">
              	<path fill="currentColor" d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z" opacity="0.5" />
              	<path fill="currentColor" d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z">
              		<animateTransform attributeName="transform" dur="0.75s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12" />
              	</path>
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mx-auto">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
              </svg>
             
            </button>
          </form>
        </div>
      </div>
      <template v-if="postsStore.posts.userPosts.data.length > 0 && !postsStore.posts.userPosts.isError">
        <PostItem v-for="post in postsStore.posts.userPosts.data" :key="post.id" :post="post"/>      
      </template>
      <div class="flex flex-col items-center justify-center h-72 text-slate-200" v-else-if="postsStore.posts.userPosts.isLoading && !postsStore.posts.userPosts.isError">
         <svg xmlns="http://www.w3.org/2000/svg" width="5rem" height="5rem" viewBox="0 0 24 24">
          	<path fill="currentColor" d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z" opacity="0.5" />
          	<path fill="currentColor" d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z">
          		<animateTransform attributeName="transform" dur="0.75s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12" />
          	</path>
          </svg>
          <span class="mt-4 text-lg">Feed is loading...</span>
      </div>
      <div class="flex flex-col items-center justify-center bg-red-700 border rounded-lg text-slate-200 h-72" v-else>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="5rem" height="5rem">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" />
        </svg>

          <span class="mt-4 text-lg">Something went wrong :( Please press "CTRL + R" to refresh, or try to logout and login again.</span>
      </div>
    </div>
    <div class="order-first col-span-3 main-right lg:col-span-1 lg:order-last">
      <div class="px-4 py-8 space-y-6 text-center border rounded-lg bg-gray-950 border-lime-300 text-slate-200">
        <img src="https://mighty.tools/mockmind-api/content/human/43.jpg" class="block w-full mx-auto mb-6 rounded-full max-w-40">
          
        <p class="mb-4 text-xl uppercase text-lime-300"><strong>{{ postsStore.posts.userPosts.author.name }}</strong></p>
        <p class="font-medium text-md text-slate-200" v-if="this.$route.params.id === userStore.user.id">{{ postsStore.posts.userPosts.author.email }}</p>
        <div class="flex justify-center mt-6 space-x-8">
            <p class="text-xs text-slate-400">{{ postsStore.posts.userPosts.author.friends_count }} friends</p>
            <p class="text-xs text-slate-400">120 posts</p>
        </div>
        <div v-if="this.$route.params.id !== userStore.user.id" class="mt-8">
          <template v-if="postsStore.posts.userPosts.author.is_friend_of_user">
            <div class="flex items-center justify-center space-x-4">
              <div class="flex items-center justify-center h-10 px-4 py-2 font-medium rounded-lg w-fit bg-lime-300 text-slate-900">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                <path d="M4.5 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM14.25 8.625a3.375 3.375 0 1 1 6.75 0 3.375 3.375 0 0 1-6.75 0ZM1.5 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM17.25 19.128l-.001.144a2.25 2.25 0 0 1-.233.96 10.088 10.088 0 0 0 5.06-1.01.75.75 0 0 0 .42-.643 4.875 4.875 0 0 0-6.957-4.611 8.586 8.586 0 0 1 1.71 5.157v.003Z" />
              </svg>
              <span class="ml-2">Friends</span>
            </div>
            <button class="flex items-center justify-center h-10 px-4 py-2 font-medium rounded-lg w-fit bg-lime-300 text-slate-900" @click="messageUser">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
              <path fill-rule="evenodd" d="M12 2.25c-2.429 0-4.817.178-7.152.521C2.87 3.061 1.5 4.795 1.5 6.741v6.018c0 1.946 1.37 3.68 3.348 3.97.877.129 1.761.234 2.652.316V21a.75.75 0 0 0 1.28.53l4.184-4.183a.39.39 0 0 1 .266-.112c2.006-.05 3.982-.22 5.922-.506 1.978-.29 3.348-2.023 3.348-3.97V6.741c0-1.947-1.37-3.68-3.348-3.97A49.145 49.145 0 0 0 12 2.25ZM8.25 8.625a1.125 1.125 0 1 0 0 2.25 1.125 1.125 0 0 0 0-2.25Zm2.625 1.125a1.125 1.125 0 1 1 2.25 0 1.125 1.125 0 0 1-2.25 0Zm4.875-1.125a1.125 1.125 0 1 0 0 2.25 1.125 1.125 0 0 0 0-2.25Z" clip-rule="evenodd" />
            </svg>
            <span class="ml-2">Message</span>
            </button>
            </div>
          </template>
          <template v-else-if="postsStore.posts.userPosts.author.has_sent_friend_request_to">
            <div class="flex items-center justify-center h-10 px-4 py-2 mx-auto font-medium rounded-lg w-fit bg-lime-300 text-slate-900">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                <path fill-rule="evenodd" d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12Zm13.36-1.814a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z" clip-rule="evenodd" />
              </svg>
              <span class="ml-2">Sent friend request</span>
            </div>
          </template>
          <template v-else-if="postsStore.posts.userPosts.author.has_received_friend_request_from">
            respond to friend request
          </template>
          <template v-else>
            <button type="button" @click.prevent="addFriend" class="flex items-center justify-center w-40 h-10 px-4 py-2 mx-auto font-medium rounded-lg bg-lime-300 text-slate-900 disabled:bg-lime-900 disabled:cursor-not-allowed" :disabled="friendshipsStore.friendships.addFriend.isLoading">
            <template v-if="friendshipsStore.friendships.addFriend.isLoading">
              <svg xmlns="http://www.w3.org/2000/svg" width="1.5rem" height="1.5rem" viewBox="0 0 24 24" class="mx-auto">
              	<path fill="currentColor" d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z" opacity="0.5" />
              	<path fill="currentColor" d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z">
              		<animateTransform attributeName="transform" dur="0.75s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12" />
              	</path>
              </svg>
            </template>
            <template v-else>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M18 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0ZM3 19.235v-.11a6.375 6.375 0 0 1 12.75 0v.109A12.318 12.318 0 0 1 9.374 21c-2.331 0-4.512-.645-6.374-1.766Z" />
              </svg>
              <span class="ml-2">Add friend</span>
            </template>
          </button>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import PostItem from "../components/PostItem.vue";
import { usePostsStore } from '@/stores/posts';
import { useUserStore } from '@/stores/user';
import { useFriendshipsStore } from '@/stores/friendships';
import useStartConversation from "@/composition-functions/useStartConversation"
import { useToast } from "vue-toastification";

export default {
  setup() {
    const postsStore = usePostsStore();
    const userStore = useUserStore();
    const friendshipsStore = useFriendshipsStore();
    const { startConversation } = useStartConversation();
    const toast = useToast();

    return {
      postsStore,
      userStore,
      friendshipsStore,
      toast,
      startConversation
    }
  },
  name: "FeedView",
  components: {
    PeopleYouMayKnow,
    Trends,
    PostItem
  },
  data() {
    return {
      body: ""
    }
  },
  mounted() {
    console.log("mounted!!!")
    if (!this.$route.params.id) {
      this.$router.push({name: 'feed'})
    } else if (this.userStore.user.isAuthenticated && this.userStore.user.accessToken && this.$route.params.id) {
      this.postsStore.getUserPosts(this.userStore.user.accessToken, this.$route.params.id)
    }
  },
  methods: {
    submitForm() {
      this.postsStore.createPost(this.userStore.user.accessToken, this.body, this.toast).then(() => {
        this.body = ""
        this.postsStore.updatePostList(this.userStore.user.id, this.$route.params.id)
      });
    },
    async addFriend() {
      this.friendshipsStore.addFriend(this.userStore.user.accessToken, this.$route.params.id).then((res) => {
        if (res.status === "success") {
          this.toast.success(`Friend request has been sent successfully!`, {
            toastClassName: "!bg-emerald-700 !text-slate-200"
          });
        } else {
          this.toast.error(`Friend request has failed to send. Reload the page and try again.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      })
    },
    messageUser() {
      this.startConversation(this.$route.params.id).then(res => {
        if (res.status === "success") {
          this.$router.push({name: "messages"})
        } else {
          this.toast.error(`Failed to start conversation with user.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
       })
    }
  },
  watch: {
    $route(to, from) {
      if (this.userStore.user.isAuthenticated && from.name === to.name && (from.params.id !== to.params.id)) {
        this.postsStore.getUserPosts(this.userStore.user.accessToken, to.params.id)
      }
    } 
   },
  unmounted() {
    console.log("unmounted!!!")
    this.friendshipsStore.resetFriendshipsStore();
  }
};
</script>