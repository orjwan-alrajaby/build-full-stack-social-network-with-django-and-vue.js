<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div class="col-span-3 space-y-4 main-center lg:col-span-2">
      <div class="border rounded-lg bg-gray-950 border-lime-300">
        <div class="p-4">
          <textarea
            class="w-full p-4 rounded-lg bg-slate-200 text-slate-950"
            placeholder="What are you thinking about?"
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
          <div>
            <button
              href="#"
              class="px-4 py-2 mx-2 font-medium bg-transparent border rounded-lg text-lime-300 border-lime-300"
              ><svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              ><path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
                />
              </svg>
            </button>

            <button
              href="#"
              class="px-4 py-2 mx-2 font-medium rounded-lg bg-lime-300 text-slate-900"
              >
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
</svg>

            </button>
          </div>
        </div>
      </div>
      <template v-if="postsStore.posts.all.data.length > 0 && !postsStore.posts.all.isError">
      <div class="p-4 border rounded-lg bg-gray-950 border-lime-300" v-for="post in postsStore.posts.all.data" :key="post.id">
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center space-x-6">
            <img
              src="https://mighty.tools/mockmind-api/content/human/37.jpg"
              class="w-[40px] rounded-full"
            />

            <p class="text-slate-200"><strong>{{ post.created_by.name }}</strong></p>
          </div>

          <p class="text-sm text-slate-400">{{ post.created_at_formatted }} ago</p>
        </div>

        <p class="text-slate-200">
          {{ post.body }}
        </p>

        <div class="flex justify-between my-6">
          <div class="flex space-x-6">
            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6 text-slate-200"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                ></path>
              </svg>

              <span class="text-xs text-slate-400">82 likes</span>
            </div>

            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6 text-slate-200"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
                ></path>
              </svg>

              <span class="text-xs text-slate-400">0 comments</span>
            </div>
          </div>

          <div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6 text-slate-200"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
              ></path>
            </svg>
          </div>
        </div>
      </div>
      
            <div class="p-4 border rounded-lg bg-gray-950 border-lime-300">
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center space-x-6">
            <img
              src="https://mighty.tools/mockmind-api/content/human/49.jpg"
              class="w-[40px] rounded-full"
            />

            <p class="text-slate-200"><strong>Angelica Johnson</strong></p>
          </div>

          <p class="text-sm text-slate-400">18 minutes ago</p>
        </div>

        <img
          src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=2670&amp;q=80"
          class="w-full rounded-lg"
        />

        <div class="flex justify-between my-6">
          <div class="flex space-x-6">
            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6 text-slate-200"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                ></path>
              </svg>

              <span class="text-xs text-slate-400">90 likes</span>
            </div>

            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
                ></path>
              </svg>

              <span class="text-xs text-slate-400">12 comments</span>
            </div>
          </div>

          <div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6 text-slate-200"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
              ></path>
            </svg>
          </div>
        </div>
      </div>
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
  },
  mounted() {
    if (this.userStore.user.isAuthenticated && this.userStore.user.accessToken) {
      this.postsStore.getAllPosts(this.userStore.user.accessToken)
    }
  },
};
</script>