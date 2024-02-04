import { defineStore } from "pinia";
import axios from "axios";
import URLS from "@/constants/urls";

export const useFriendshipsStore = defineStore({
  id: 'friendships',

  state: () => ({
    friendships: {
      addFriend: {
        isLoading: false,
        isError: false,
        error: null,
        data: null,
      },
      getFriendsAndRequests: {
        isLoading: false,
        isError: false,
        error: null,
        user: {},
        friends: [],
        requests: []
      }
    },
  }),
  actions: {
    async addFriend(accessToken, id) {
      this.friendships.addFriend.isLoading = true
      try {
        axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
        const response = await axios.post(URLS.addFriend(id));
        this.friendships.addFriend.data = response.data;
        return {status: "success"};
      } catch (error) {
        this.friendships.addFriend.isError = true;
        this.friendships.addFriend.error = error;
        return { status: "error" };
      } finally {
        this.friendships.addFriend.isLoading = false;
      }
    },
    async getFriendsAndRequests(accessToken, id) {
      this.friendships.getFriendsAndRequests.isLoading = true
      try {
        axios.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`
        const response = await axios.get(URLS.getFriendsAndRequests(id));
        console.log("Response is here! 123", {
          response
        })
        this.friendships.getFriendsAndRequests.user = response.data.user;
        this.friendships.getFriendsAndRequests.friends = response.data.friends;
        this.friendships.getFriendsAndRequests.requests = response.data.requests;
        return {status: "success"};
      } catch (error) {
        this.friendships.getFriendsAndRequests.isError = true;
        this.friendships.getFriendsAndRequests.error = error;
        return { status: "error" };
      } finally {
        this.friendships.getFriendsAndRequests.isLoading = false;
      }
    },
    resetFriendshipsStore() {
      this.friendships.addFriend = {
        isLoading: false,
        isError: false,
        error: null,
        data: null,        
      };
      this.friendships.getFriendsAndRequests = {
        isLoading: false,
        isError: false,
        error: null,  
        user: {},
        friends: [],
        requests: []
      }
    }
  }
})