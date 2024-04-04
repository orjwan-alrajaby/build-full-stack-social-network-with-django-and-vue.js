import { defineStore } from "pinia";

export const usePostsStore = defineStore({
  id: 'posts',

  state: () => ({
    all: {
      posts: []
    },
    user: {
      posts: [],
      author: null
    }
  }),

  actions: {
    setAllPosts(posts) {
      this.all.posts = posts
    },
    addNewPost(post) { 
      this.all.posts = [post, ...this.all.posts];
      this.user.posts = [post, ...this.user.posts];
    },
    setUserPosts(author, posts) {
      this.user.author = author;
      this.user.posts = posts;
    },
  }
})