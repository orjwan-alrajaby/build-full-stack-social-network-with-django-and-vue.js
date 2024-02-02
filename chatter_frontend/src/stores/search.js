import { defineStore } from "pinia";
import axios from "axios";
import URLS from "@/constants/urls";

export const useSearchStore = defineStore({
  id: 'search',

  state: () => ({
    search: {
      isLoading: false,
      isError: false,
      error: null,
      users: [],
      posts: [],
      hasSearched: false,
    }
  }),
  actions: {
    async searchUsersAndPostsList(accessToken, query) {
      this.search.isLoading = true
      try {
        axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
        const response = await axios.get(URLS.search(query));
        this.search.users = response.data.users;
        this.search.posts = response.data.posts;
      } catch (error) {
        this.search.isError = true;
        this.search.error = error;
      } finally {
        this.search.isLoading = false;
        this.search.hasSearched = true;
      }
    },
    resetSearch() {
      this.search.users = [];
      this.search.posts = [];
      this.search.isLoading = false;
      this.search.isError = false;
      this.search.error = null;
      this.search.hasSearched = false;
    }
  }
})