<template>
  <div class="grid grid-cols-4 gap-4 mx-auto max-w-7xl">
    <div class="col-span-4 space-y-4 main-left lg:col-span-3">
      <form
        class="border rounded-lg bg-slate-950 border-lime-300"
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
            <SearchIcon width="1.5rem" height="1.5rem" classes="text-slate-950"/>
          </button>
        </div>
      </form>
      <template
        v-if="searchStore.search.isLoading || searchStore.search.isError"
      >
        <PageFeedback v-if="searchStore.search.isLoading" title="Searching...">
          <LoaderIcon />
        </PageFeedback>

        <PageFeedback 
           v-else-if="searchStore.search.isError" 
           :isError="true"
           :title="'Something went wrong :('"
           :subtitle="'Please press [CTRL + R] to refresh, or try to logout and login again.'"
         >
          <WarningIcon />
        </PageFeedback>
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
              class="col-span-4 p-4 space-y-6 text-center border rounded-lg bg-slate-950 border-lime-300 lg:col-span-1 md:col-span-2"
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
                  <p class="text-xs text-slate-400">{{ user.posts_count }} posts</p>
                </div>

              <template  v-if="user.is_friend_of_user">
                <div class="flex items-center justify-center w-40 h-10 px-4 py-2 mx-auto font-medium rounded-lg bg-lime-300 text-slate-950">
                  <TwoFriendsIcon width="1.5rem" height="1.5rem"/>
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
          <PostItem 
           v-for="post in searchStore.search.posts"
           :key="post.id"
           :post="post"/>
        </template>
      </template>
      <template v-else-if="searchStore.search.hasSearched">
        <PageFeedback title="No Results Found" subtitle="Try a different query.">
          <OfficeBoxIcon />
        </PageFeedback>
      </template>
      <template v-else-if="!searchStore.search.hasSearched">
        <PageFeedback title="Nothing is here yet." subtitle="Use the search bar above to look for users, or posts.">
          <EmptyOfficeBoxIcon />
        </PageFeedback>
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
import PostItem from "../components/PostItem.vue";
import PageFeedback from "@/components/PageFeedback.vue"
import LoaderIcon from "@/components/icons/LoaderIcon.vue"
import WarningIcon from "@/components/icons/WarningIcon.vue";
import OfficeBoxIcon from "@/components/icons/OfficeBoxIcon.vue"
import EmptyOfficeBoxIcon from "@/components/icons/EmptyOfficeBoxIcon.vue"
import TwoFriendsIcon from "@/components/icons/TwoFriendsIcon.vue"
import { SearchIcon } from "@/components/icons/outlined/index.js"

import { useSearchStore } from "@/stores/search";
import { useUserStore } from "@/stores/user";

export default {
  name: "SearchView",
  components: {
    PeopleYouMayKnow,
    Trends,
    PostItem,
    SearchIcon,
    PageFeedback,
    LoaderIcon,
    WarningIcon,
    OfficeBoxIcon,
    EmptyOfficeBoxIcon,
    TwoFriendsIcon
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