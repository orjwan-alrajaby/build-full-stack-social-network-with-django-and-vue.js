<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div class="col-span-3 space-y-4 main-center lg:col-span-2">
      <div class="border rounded-lg bg-gray-950 border-lime-300">
        <div class="p-4">
          <textarea
            class="w-full p-4 rounded-lg bg-slate-200 text-slate-950"
            placeholder="What are you thinking about?"
            v-model="body"
          ></textarea>
        </div>

        <div
          class="flex items-center justify-between pt-4 m-4 mt-0 border-t border-slate-700"
        >
          <div>
            <img
              src="https://mighty.tools/mockmind-api/content/human/43.jpg"
              class="hidden w-12 rounded-full sm:block"
            />
          </div>
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
      <template v-if="postsStore.posts.all.data.length > 0 && !postsStore.posts.all.isError">
        <PostItem v-for="post in postsStore.posts.all.data" :key="post.id" :post="post"/>
      </template>
      <div class="flex flex-col items-center justify-center h-72 text-slate-200" v-else-if="postsStore.posts.all.isLoading && !postsStore.posts.all.isError">
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

    <div class="col-span-3 space-y-4 main-right lg:col-span-1">
      <PeopleYouMayKnow />
      
      <Trends />
    </div>
  </div>
</template>

<script>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import { usePostsStore } from '@/stores/posts';
import { useUserStore } from '@/stores/user';
import { useToast } from "vue-toastification";
import PostItem from "../components/PostItem.vue";

export default {
  setup() {
    const postsStore = usePostsStore();
    const userStore = useUserStore();
    const toast = useToast();

    return {
      postsStore,
      userStore,
      toast
    }
  },
  name: "FeedView",
  components: {
    PeopleYouMayKnow,
    Trends,
    PostItem,
  },
  data() {
    return {
      body: ""
    }
  },
  mounted() {
    if (this.userStore.user.isAuthenticated && this.userStore.user.accessToken) {
      this.postsStore.getAllPosts(this.userStore.user.accessToken)
    }
  },
  methods: {
    submitForm() {
      this.postsStore.createPost(this.userStore.user.accessToken, this.body, this.toast).then(() => {
        this.body = ""
        this.postsStore.updatePostList()
      });
    }
  }
};
</script>