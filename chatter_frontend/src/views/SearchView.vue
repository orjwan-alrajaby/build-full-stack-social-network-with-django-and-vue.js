<template>
  <div class="grid grid-cols-4 gap-4 mx-auto max-w-7xl">
    <div class="col-span-4 space-y-4 main-left lg:col-span-3">
      <form
        class="border rounded-lg bg-gray-950 border-lime-300"
        @submit.prevent="submitForm"
      >
        <div class="flex p-4 space-x-4">
          <input
            type="search"
            class="w-full p-4 rounded-lg bg-slate-200 text-slate-950"
            placeholder="What are you looking for?"
            v-model="query"
          />

          <button
            class="px-4 py-2 mx-2 font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-lime-900 disabled:cursor-not-allowed"
            :disabled="!query || searchStore.search.isLoading"
          >
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
                d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
              />
            </svg>
          </button>
        </div>
      </form>

      <template
        v-if="searchStore.search.isLoading || searchStore.search.isError"
      >
        <div
          class="flex flex-col items-center justify-center h-72 text-slate-200"
          v-if="searchStore.search.isLoading"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="5rem"
            height="5rem"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
              opacity="0.5"
            />
            <path
              fill="currentColor"
              d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z"
            >
              <animateTransform
                attributeName="transform"
                dur="0.75s"
                repeatCount="indefinite"
                type="rotate"
                values="0 12 12;360 12 12"
              />
            </path>
          </svg>
          <span class="mt-4 text-lg">Searching...</span>
        </div>
        <div
          class="flex flex-col items-center justify-center bg-red-700 border rounded-lg text-slate-200 h-72"
          v-else-if="searchStore.search.isError"
        >
          >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            width="5rem"
            height="5rem"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z"
            />
          </svg>

          <span class="mt-4 text-lg"
            >Something went wrong :( Please try to search again, or try to
            logout and login again.</span
          >
        </div>
      </template>

      <template
        v-else-if="
          searchStore.search.users.length > 0 ||
          searchStore.search.posts.length > 0
        "
      >
        <template v-if="searchStore.search.users.length > 0">
          <div class="w-full border border-slate-700 !mt-6"></div>

          <h2 class="pb-3 text-2xl font-medium text-slate-400">
            SEARCH RESULTS: IN USERS
          </h2>
          <div class="grid grid-cols-4 gap-4">
            <div
              class="col-span-4 p-4 space-y-6 text-center border rounded-lg bg-gray-950 border-lime-300 lg:col-span-1 md:col-span-2"
              v-for="user in searchStore.search.users"
              :key="user.id"
            >
                <img
                  src="https://mighty.tools/mockmind-api/content/human/40.jpg"
                  class="w-full mx-auto mb-6 rounded-full max-w-40"
                />

                <p class="uppercase text-lime-300">
                  <strong>
                    <router-link
                      :to="{ name: 'user-profile', params: { id: user.id } }"
                    >
                      {{ user.name }}
                    </router-link>
                  </strong>
                </p>

                <div class="flex justify-around mt-6 space-x-8">
                  <p class="text-xs text-slate-400">
                    <router-link :to="{ name: 'user-friends', params: { id: user.id } }">
                      {{ user.friends_count }} friends
                    </router-link>
                  </p>
                  <p class="text-xs text-slate-400">120 posts</p>
                </div>

              <template  v-if="user.is_friend_of_user">
                                <div class="flex items-center justify-center w-40 h-10 px-4 py-2 mx-auto font-medium rounded-lg bg-lime-300 text-slate-900">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                  <path d="M4.5 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM14.25 8.625a3.375 3.375 0 1 1 6.75 0 3.375 3.375 0 0 1-6.75 0ZM1.5 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM17.25 19.128l-.001.144a2.25 2.25 0 0 1-.233.96 10.088 10.088 0 0 0 5.06-1.01.75.75 0 0 0 .42-.643 4.875 4.875 0 0 0-6.957-4.611 8.586 8.586 0 0 1 1.71 5.157v.003Z" />
                </svg>
                <span class="ml-2">Friends</span>
              </div>
              </template>
            </div>
          </div>
        </template>

        <template v-if="searchStore.search.posts.length > 0">
          <div class="w-full border border-slate-700 !mt-6"></div>
          <h2 class="pb-3 text-2xl font-medium text-slate-400">
            SEARCH RESULTS: IN POSTS
          </h2>
          <div
            class="p-4 border rounded-lg bg-gray-950 border-lime-300"
            v-for="post in searchStore.search.posts"
            :key="post.id"
          >
            <div class="flex items-center justify-between mb-6">
              <div class="flex items-center space-x-6">
                <img
                  src="https://mighty.tools/mockmind-api/content/human/37.jpg"
                  class="w-[40px] rounded-full"
                />

                <p class="text-slate-200">
                  <strong>
                    <router-link :to="{name: 'user-profile', params: { id: post.created_by.id }}">
                      {{ post.created_by.name }}
                    </router-link>
                  </strong>
                </p>
              </div>

              <p class="text-sm text-slate-400">
                {{ post.created_at_formatted }}
                ago
              </p>
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
        </template>
      </template>
      <template v-else-if="searchStore.search.hasSearched">
        <div
          class="flex flex-col items-center justify-center p-4 text-2xl font-medium h-72 text-slate-400"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            width="5rem"
            height="5rem"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m20.25 7.5-.625 10.632a2.25 2.25 0 0 1-2.247 2.118H6.622a2.25 2.25 0 0 1-2.247-2.118L3.75 7.5m6 4.125 2.25 2.25m0 0 2.25 2.25M12 13.875l2.25-2.25M12 13.875l-2.25 2.25M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z"
            />
          </svg>
          <span class="mt-4 text-lg">
            Nothing has been found. Try to look for something else.
          </span>
        </div>
      </template>
      <template v-else-if="!searchStore.search.hasSearched">
        <div
          class="flex flex-col items-center justify-center p-4 text-2xl font-medium h-72 text-slate-400"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" width="5rem" height="5rem">
            <path stroke-linecap="round" stroke-linejoin="round" d="m20.25 7.5-.625 10.632a2.25 2.25 0 0 1-2.247 2.118H6.622a2.25 2.25 0 0 1-2.247-2.118L3.75 7.5M10 11.25h4M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z" />
          </svg>
          <span class="mt-4 text-lg">
            Nothing is here yet. Use the search bar above to look for users, or posts. 
          </span>
        </div>
      </template>
    </div>

    <div class="col-span-4 space-y-4 main-right lg:col-span-1">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>

<script>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";

import { useSearchStore } from "@/stores/search";
import { useUserStore } from "@/stores/user";
import { useToast } from "vue-toastification";

export default {
  name: "SearchView",
  components: {
    PeopleYouMayKnow,
    Trends,
  },
  setup() {
    const searchStore = useSearchStore();
    const userStore = useUserStore();

    return {
      searchStore,
      userStore,
    };
  },
  data() {
    return {
      query: "",
    };
  },
  methods: {
    submitForm() {
      this.searchStore.searchUsersAndPostsList(
        this.userStore.user.accessToken,
        this.query
      );
    },
  },
  unmounted() {
    this.searchStore.resetSearch();
  },
};
</script>