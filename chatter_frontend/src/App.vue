<template>
  <div class="relative h-screen bg-gray-950">
    <nav class="px-2 py-4 border-b md:py-6 md:px-8 border-lime-300">
      <div class="m-auto max-w-7xl">
        <div class="flex items-center justify-between">
          <div class="p-2 menu-left">
            <router-link :to="{name: 'home'}" class="flex items-center text-2xl font-bold text-lime-300 md:text-3xl">
              <img src="./assets/logo.png" alt="chatter logo" class="w-10 md:w-12"/>
              <span class="mx-2">Chatter</span>
            </router-link>
          </div>

          <template v-if="userStore.user.isAuthenticated && userStore.user.id">
            <div class="justify-between hidden menu-center md:space-x-12 lg:flex">
              <router-link :to="{ name: 'home' }"
                class="flex items-center p-2 text-slate-200">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                  viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                  class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                </svg>
                <span class="ml-2">Home</span>
              </router-link>
              
              <router-link :to="{name: 'user-friends', params: {id: userStore.user.id }}" class="flex items-center p-2 text-slate-200">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 0 0 3.741-.479 3 3 0 0 0-4.682-2.72m.94 3.198.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0 1 12 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 0 1 6 18.719m12 0a5.971 5.971 0 0 0-.941-3.197m0 0A5.995 5.995 0 0 0 12 12.75a5.995 5.995 0 0 0-5.058 2.772m0 0a3 3 0 0 0-4.681 2.72 8.986 8.986 0 0 0 3.74.477m.94-3.197a5.971 5.971 0 0 0-.94 3.197M15 6.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm6 3a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Zm-13.5 0a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Z" />
                </svg>
                <span class="ml-2">Friends</span>
              </router-link>
              <router-link :to="{name: 'messages'}" class="flex items-center p-2 text-slate-200">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 0 1-.825-.242m9.345-8.334a2.126 2.126 0 0 0-.476-.095 48.64 48.64 0 0 0-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0 0 11.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" />
</svg>

                <span class="ml-2">Chat</span>
              </router-link>

              <a href="#" class="flex items-center p-2 text-slate-200">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                  viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                  class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0">
                  </path>
                </svg>
                <span class="ml-2">Notifications</span>
              </a>

              <router-link :to="{name: 'search'}" class="flex items-center p-2 text-slate-200">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                  viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                  class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z">
                  </path>
                </svg>
                <span class="ml-2">Search</span>
              </router-link>
            </div>

            <div class="hidden p-2 menu-right lg:flex">
              <button class="flex items-center justify-center bg-transparent border-none text-slate-400 w-36" @click="handleLogOut" v-if="isUserProfile">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15" />
                </svg>
                <span class="ml-2">Log out</span>
              </button>

              <router-link :to="{name: 'user-profile', params: {id: userStore.user.id}}" class="flex items-center justify-center p-2 w-36 text-slate-200" v-else>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                </svg>
                <span class="ml-2">My Account</span>
              </router-link>
            </div>

          </template>
          <template v-if="!userStore.user.isAuthenticated">
            <div class="hidden p-2 menu-right lg:flex">
              <router-link :to="{name:'login'}" class="px-4 py-2 ml-4 font-medium bg-transparent border rounded-lg text-lime-300 border-lime-300">
                Log in
              </router-link>
              <router-link :to="{name:'sign-up'}"  class="px-4 py-2 ml-4 font-medium rounded-lg bg-lime-300 text-gray-950">
                Sign up
              </router-link>
            </div>
          </template>
        </div>
      </div>
    </nav>
    <main class="min-h-full px-4 py-6 bg-gray-900 md:p-10 sm:p-8">
      <router-view />
    </main>
  </div>
</template>


<script>
import { useToast } from "vue-toastification";
import { useUserStore } from '@/stores/user';

export default {
  setup() {
    const userStore = useUserStore();
    const toast = useToast();

    return {
      userStore,
      toast,
    }
  },
  methods: {
    handleLogOut() {
      this.userStore.handleRemoveToken();
      this.toast.info("You have been logged out.", {
        toastClassName: "!bg-blue-700 !text-slate-200",
      })
      this.$router.push({name: 'login'})
    }
  },
  data() {
    return {
      isUserProfile: false
    }
   },
  beforeCreate() {
    this.userStore.initializeStore()
  },
  mounted() {
    setTimeout(() => {
      if (this.userStore.user.isAuthenticated) {
        this.$router.push({ name: 'home' })
      } else {
        this.$router.push({ name: 'login' })
      }
    });
  },
  watch: { 
    $route(to, from) {
      if (!this.userStore.user.isAuthenticated && (to.name !== 'login' && to.name !== "sign-up")) {
        this.$router.push({ name: 'login' })
      } else if (to.name === 'user-profile' && this.userStore.user.id === to.params.id) {
        this.isUserProfile = true;
      } else {
        this.isUserProfile = false;
      }
    }
  },
  name: 'AppView',
  components: {}
}
</script>



