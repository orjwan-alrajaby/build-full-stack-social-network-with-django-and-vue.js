import { defineStore } from "pinia";
import axios from "axios";
import URLS from "@/constants/urls";

export const usePostsStore = defineStore({
  id: 'posts',

  state: () => ({
    posts: {
      all: [],
    }
  }),

  actions: {
    async initializeStore() {
      await this.getAllPosts();
    },
    async getAllPosts(accessToken) {
      axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
      const response = await axios.get(URLS.allPosts);
      this.posts.all = response.data.data;
    },
  }
})