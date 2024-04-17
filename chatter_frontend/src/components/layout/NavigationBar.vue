<template>
  <nav class="px-2 py-4 border-b md:py-6 md:px-8 border-lime-300">
    <div class="m-auto max-w-7xl">
      <div class="flex items-center justify-between">
        <div class="p-2 menu-left">
          <router-link
            :to="{ name: 'home' }"
            class="flex items-center text-2xl font-bold text-lime-300 md:text-3xl"
          >
            <img
              src="@/assets/logo.png"
              alt="chatter logo"
              class="w-10 md:w-12"
            />
            <span class="mx-2">Chatter</span>
          </router-link>
        </div>

        <template v-if="userStore.user.isAuthenticated && userStore.user.id">
          <div class="justify-between hidden menu-center md:space-x-12 lg:flex">
            <router-link
              :to="{ name: 'home' }"
              class="flex items-center p-2 text-slate-200"
            >
              <HomeIcon width="1.5rem" height="1.5rem" classes="inherit" />
              <span class="ml-2">Home</span>
            </router-link>

            <router-link
              :to="{ name: 'user-friends', params: { id: userStore.user.id } }"
              class="flex items-center p-2 text-slate-200"
            >
              <ThreeUsersIcon width="1.5rem" height="1.5rem" classes="inherit" />
              <span class="ml-2">Friends</span>
            </router-link>
            <router-link
              :to="{ name: 'messages' }"
              class="flex items-center p-2 text-slate-200"
            >
              <TwoMessageBubblesIcon width="1.5rem" height="1.5rem" classes="inherit" />
              <span class="ml-2">Chat</span>
            </router-link>

            <a href="#" class="flex items-center p-2 text-slate-200">
              <NotificationsIcon width="1.5rem" height="1.5rem" classes="inherit" />
              <span class="ml-2">Notifications</span>
            </a>

            <router-link
              :to="{ name: 'search' }"
              class="flex items-center p-2 text-slate-200"
            >
              <SearchIcon width="1.5rem" height="1.5rem" classes="inherit"/>
              <span class="ml-2">Search</span>
            </router-link>
          </div>

          <div class="hidden p-2 menu-right lg:flex">
            <button
              class="flex items-center justify-center bg-transparent border-none text-slate-400 w-36"
              @click="handleLogOut"
              v-if="isUserProfile"
            >
              <LeavingIcon width="1.5rem" height="1.5rem" />
              <span class="ml-2">Log out</span>
            </button>

            <router-link
              :to="{ name: 'user-profile', params: { id: userStore.user.id } }"
              class="flex items-center justify-center p-2 w-36 text-slate-200"
              v-else
            >
              <OneUserIcon width="1.5rem" height="1.5rem" classes="inherit" />
              <span class="ml-2">My Account</span>
            </router-link>
          </div>
        </template>
        <template v-if="!userStore.user.isAuthenticated">
          <div class="hidden p-2 menu-right lg:flex">
            <router-link
              :to="{ name: 'login' }"
              class="px-4 py-2 ml-4 font-medium bg-transparent border rounded-lg text-lime-300 border-lime-300"
            >
              Log in
            </router-link>
            <router-link
              :to="{ name: 'sign-up' }"
              class="px-4 py-2 ml-4 font-medium rounded-lg bg-lime-300 text-slate-950"
            >
              Sign up
            </router-link>
          </div>
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
import {
  HomeIcon,
  ThreeUsersIcon,
  OneUserIcon,
  TwoMessageBubblesIcon,
  NotificationsIcon,
  LeavingIcon,
  SearchIcon
} from "@/components/icons"

import { useToast } from "vue-toastification";
import { useUserStore } from '@/stores/user';
import useRefreshToken from "@/composables/user/useRefreshToken";

export default {
  name: 'NavigationBar',
  components: {
    HomeIcon,
    ThreeUsersIcon,
    OneUserIcon,
    TwoMessageBubblesIcon,
    NotificationsIcon,
    LeavingIcon,
    SearchIcon
  },
  setup() {
    const userStore = useUserStore();
    const toast = useToast();
    const { handleRefreshToken } = useRefreshToken();

    return {
      userStore,
      toast,
      handleRefreshToken
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
    this.userStore.initializeStore();
    this.handleRefreshToken(this.userStore.user.refreshToken).then(res => {
      if (res.status === "error") {
        this.userStore.handleRemoveToken();
        // this.toast.info("Your session has expired, you must login again.", {
        //   toastClassName: "!bg-blue-700 !text-slate-200",
        // })
        return;
      }
    });
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
}
</script>



