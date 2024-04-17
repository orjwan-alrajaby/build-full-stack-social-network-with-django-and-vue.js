import { defineStore } from "pinia";

export const useFriendshipsStore = defineStore({
  id: 'friendships',
  state: () => ({
    friends: [],
    sentRequests: [],
    receivedRequests: [],
  }),
  actions: {
    setFriendsAndRequests({friends, sent_requests, received_requests}) {
      this.friends = friends;
      this.sentRequests = sent_requests;
      this.receivedRequests = received_requests;
    },
    deleteSentRequest(receiverId) {
      this.sentRequests = this.sentRequests.filter(ele => ele.created_for.id !== receiverId);
    }
  }
})