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
    initializeStore() {
      if (localStorage.getItem('user.accessToken')) {
        this.user = {
          isAuthenticated: true,
          id: localStorage.getItem('user.id'),
          name: localStorage.getItem('user.name'),
          email: localStorage.getItem('user.email'),
          accessToken: localStorage.getItem('user.accessToken'),
          refreshToken: localStorage.getItem('user.refreshToken'),
        }

        this.refreshToken();

        console.log({
          status: "initialize user",
          user: this.user
        })
      }
    },

    setToken(data) {
      console.log({
        status: 'set token',
        data,
      })

      this.user = {
        ...this.user,
        accessToken: data.accessToken,
        refreshToken: data.refreshToken,
        isAuthenticated: true
      }

      localStorage.setItem('user.accessToken', data.accessToken)
      localStorage.setItem('user.refreshToken', data.refreshToken)
    },

    removeToken() {
      console.log({
        status: 'remove token'
      })

      this.user = {
        isAuthenticated: false,
        id: '',
        name: '',
        email: '',
        accessToken: '',
        refreshToken: '',
      }

      localStorage.removeItem('user.id')
      localStorage.removeItem('user.name')
      localStorage.removeItem('user.email')
      localStorage.removeItem('user.accessToken')
      localStorage.removeItem('user.refreshToken')
    },

    setUserInfo(user) {
      console.log({
        status: 'BEFORE set user info',
        user,
      })

      this.user = {
        ...this.user,
        id: user.id,
        name: user.name,
        email: user.email
      }

      localStorage.setItem('user.id', user.id);
      localStorage.setItem('user.name', user.name);
      localStorage.setItem('user.email', user.email);

      console.log({
        status: 'AFTER set user info',
        user,
      })
    },

   async refreshToken() {
     try {
       response = await axios.post(URLS.refreshToken, {
         refreshToken: this.user.refreshToken
       })

       this.user.accessToken = response.data.access

       localStorage.setItem('user.accessToken', response.data.access)

       axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`
     }
     catch (error) {
       this.removeToken();
     }
    }
  }
})