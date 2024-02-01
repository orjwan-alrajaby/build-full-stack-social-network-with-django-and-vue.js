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
      newPost: {
        isLoading: false,
        data: {},
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
    async createPost(accessToken, body, toast) {
      this.posts.newPost.isLoading = true
      try {
        axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
        const response = await axios.post(URLS.createPost, {
          body
        });
        this.posts.newPost.data = response.data.data;
        toast.success("Post has been submitted successfully.", {
          toastClassName: "!bg-emerald-700 !text-slate-200"
        })
        this.posts.all.data = [this.posts.newPost.data, ...this.posts.all.data]
        return;
      } catch (error) {
        this.posts.newPost.isError = true;
        this.posts.newPost.error = error;
        toast.error("Post has failed to submit. Please try again.", {
          toastClassName: "!bg-red-700 !text-slate-200",
        })
        return;
      } finally {
        this.posts.newPost.isLoading = false;
      }
    },
  }
})