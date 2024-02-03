import { defineStore } from "pinia";
import axios from "axios";
import URLS from "@/constants/urls";

export const useFriendshipsStore = defineStore({
  id: 'friendships',

  state: () => ({
    friendships: {
      isLoading: false,
      isError: false,
      error: null,
      addFriend: null,
    },
  }),
  actions: {
    async addFriend(accessToken, id) {
      this.friendships.isLoading = true
      try {
        axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
        const response = await axios.post(URLS.addFriend(id));
        this.friendships.addFriend = response.data.response;
        return {status: "success"};
      } catch (error) {
        this.friendships.isError = true;
        this.friendships.error = error;
        return { status: "error" };
      } finally {
        this.friendships.isLoading = false;
      }
    },
    resetFriendshipsStore() {
      this.friendships.addFriend = null;
      this.friendships.isLoading = false;
      this.friendships.isError = false;
      this.friendships.error = null;
    }
  }
})