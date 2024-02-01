import { defineStore } from "pinia";
import axios from "axios";
import URLS from "@/constants/urls";

export const usePostsStore = defineStore({
  id: 'posts',

  state: () => ({
    posts: {
      all: {
        isLoading: false,
        data: [],
        isError: false,
        error: null,
      },
    }
  }),

  actions: {
    async initializeStore() {
      await this.getAllPosts();
    },
    async getAllPosts(accessToken) {
      this.posts.all.isLoading = true
      try {
        axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
        const response = await axios.get(URLS.allPosts);
        this.posts.all.data = response.data.data;
      } catch (error) {
        this.posts.all.isError = true;
        this.posts.all.error = error;
      } finally {
        this.posts.all.isLoading = false
      }
    },
  }
})