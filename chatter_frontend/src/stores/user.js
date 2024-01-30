import { defineStore } from "pinia";
import axios from "axios";
import URLS from "@/constants/urls";

export const useUserStore = defineStore({
  id: 'user',

  state: () => ({
    user: {
      isAuthenticated: false,
      id: '',
      name: '',
      email: '',
      accessToken: '',
      refreshToken: '',
    }
  }),

  actions: {
    async initializeStore() {
      if (localStorage.getItem('user.accessToken')) {
        this.user.isAuthenticated = true;
        this.user.id = localStorage.getItem('user.id');
        this.user.name = localStorage.getItem('user.name');
        this.user.email = localStorage.getItem('user.email');
        this.user.accessToken = localStorage.getItem('user.accessToken');
        this.user.refreshToken = localStorage.getItem('user.refreshToken');
        await this.handleRefreshToken();
      }
    },

    handleSetToken(data) {
      this.user.accessToken = data.access;
      this.user.refreshToken = data.refresh;
      this.user.isAuthenticated = true;

      localStorage.setItem('user.accessToken', data.access)
      localStorage.setItem('user.refreshToken', data.refresh)

      axios.defaults.headers.common["Authorization"] = `Bearer ${data.access}`
    },

    handleRemoveToken() {
      this.user.id = "";
      this.user.name = "";
      this.user.email = "";
      this.user.accessToken = "";
      this.user.refreshToken = "";
      this.user.isAuthenticated = false;

      localStorage.removeItem('user.id')
      localStorage.removeItem('user.name')
      localStorage.removeItem('user.email')
      localStorage.removeItem('user.accessToken')
      localStorage.removeItem('user.refreshToken')
    },

    setUserInfo(user) {
      this.user.id = user.id;
      this.user.name = user.name;
      this.user.email = user.email;

      localStorage.setItem('user.id', user.id);
      localStorage.setItem('user.name', user.name);
      localStorage.setItem('user.email', user.email);
    },

    async handleRefreshToken() {
     try {
       if (this.user.refreshToken) {
         const response = await axios.post(URLS.refreshToken, {
           refresh: this.user.refreshToken
          })

         this.user.accessToken = response.data.access
         localStorage.setItem('user.accessToken', response.data.access)
         axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`
       }
     } catch (error) {
       console.error(error)
       this.handleRemoveToken();
     }
    }
  }
})