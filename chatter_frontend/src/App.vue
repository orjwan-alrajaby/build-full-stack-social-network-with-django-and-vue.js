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
                class="flex items-center p-2 text-lime-300">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                  viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                  class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                </svg>
                <span class="ml-2">Home</span>
              </router-link>
              
              <router-link :to="{name: 'messages'}" class="flex items-center p-2 text-slate-200">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                  viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                  class="w-6 h-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z">
                  </path>
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



