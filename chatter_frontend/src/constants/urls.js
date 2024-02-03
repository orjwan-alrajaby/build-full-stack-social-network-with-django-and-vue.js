const URLS = {
  refreshToken: "/api/refresh/",
  signUp: "/api/signup/",
  login: "/api/login/",
  me: "/api/me/",
  allPosts: "/api/posts/",
  createPost: "/api/posts/create/",
  userPosts: (id) => `/api/posts/by/${id}`,
  search: (query) => `/api/search/${query}`,
  addFriend: (id) => `/api/friends/add/${id}/`
}

export default URLS