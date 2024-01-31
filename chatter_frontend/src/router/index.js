import { createRouter, createWebHistory } from 'vue-router'
import SignUpView from "../views/SignUpView.vue"
import LogInView from "../views/LogInView.vue"
import FeedView from "../views/FeedView.vue"
import MessagesView from "../views/MessagesView.vue"
import SearchView from "../views/SearchView.vue"

const routes = [
  {
    path: '/',
    name: 'home',
    component: FeedView
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/messages',
    name: 'messages',
    component: MessagesView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
