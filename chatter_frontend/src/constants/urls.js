const URLS = {
  refreshToken: "/api/refresh/",
  signUp: "/api/signup/",
  login: "/api/login/",
  me: "/api/me/",
  allPosts: "/api/posts/",
  createPost: "/api/posts/create/",
  userPosts: (id) => `/api/posts/by/${id}`,
  search: (query) => `/api/search/${query}`,
  addFriend: (id) => `/api/friends/${id}/add/`,
  getFriendsAndRequests: (id) => `/api/friends/${id}/`,
  respondToFriendRequest: (status, senderId) => `/api/friends/request/${senderId}/${status}/`,
  deleteSentRequest: (receiverId) => `/api/friends/request/${receiverId}/delete/`,
  likePost: (id) => `/api/posts/${id}/`,
  createComment: (postId) => `/api/posts/${postId}/comments/create/`,
}

export default URLS