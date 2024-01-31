<template>
  <div class="items-center justify-between px-6 py-6 mx-auto border rounded-lg lg:max-w-5xl lg:flex lg:px-12 bg-gray-950 border-lime-300">
    <div class="py-4 lg:border-y lg:border-lime-300 lg:w-2/5">
      <h1 class="mb-6 text-xl font-bold text-center text-lime-300">Hello and welcome to Chatter!</h1>
      <p class="text-lg text-center text-slate-200">Sign up today to start chatting with your friends!</p>
    </div>
    <form class="block space-y-6 lg:w-3/6" v-on:submit.prevent="submitForm">
      <div> 
        <label class="block mb-3 text-slate-200">Full Name</label>
        <input placeholder="Enter full name" type="text" class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950" v-model="form.name" required/>
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Email Address</label>
        <input placeholder="Enter email address" type="text" class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950" v-model="form.email" required/>
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Password</label>
        <input placeholder="Enter password" type="password" class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950" v-model="form.password1" required/>
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Confirm Password</label>
        <input placeholder="Confirm password" type="password" class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950" v-model="form.password2" required/>
      </div>
      <div>
        <button class="flex items-center justify-center w-full h-10 px-4 py-2 font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-slate-600" :disabled="isLoading">
          <span class="px-4" v-if="!isLoading">Create Account</span>
          <svg v-if="isLoading" xmlns="http://www.w3.org/2000/svg" width="1.5rem" height="1.5rem" viewBox="0 0 24 24">
          	<path fill="currentColor" d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z" opacity="0.5" />
          	<path fill="currentColor" d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z">
          		<animateTransform attributeName="transform" dur="0.75s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12" />
          	</path>
          </svg>
        </button>
      </div>
      <p class="mt-10 text-sm text-slate-400">Already have an account? Go ahead and <router-link :to="{name:'login'}" class="text-lime-300">Log In</router-link>.</p>
    </form>
  </div>
</template>

<script>
import URLS from '@/constants/urls';
import axios from 'axios';
import { useToast } from "vue-toastification";

export default {
  setup() {
    const toast = useToast();

    return {
      toast,
    }
  },

  data() {
    return {
      form: {
        email: '',
        name: '',
        password1: '',
        password2: ''
      },
      errors: [],
      isLoading: false,
    }
  },

  methods: {
    async submitForm() {
      this.errors = [];

      if (!this.form.email) {
        this.errors.push('You must enter a valid email address!')
      }

      if (!this.form.name) {
        this.errors.push('You must enter your name!')
      }

      if (!this.form.password1) {
        this.errors.push('You must enter a valid password!')
      }

      if (!this.form.password2) {
         this.errors.push('You must confirm your password!')
      }

      if (!this.form.password1 === this.form.password2) {
         this.errors.push('Passwords do not match!')
      }

      if (this.errors.length === 0) {
        this.isLoading = true;
        try {
          const response = await axios.post(URLS.signUp, this.form);
          if (response.data.status === 201) {
            this.toast.success('The user has been registered successfully. Now please log in.', {
              toastClassName: "!bg-emerald-700 !text-slate-200",
            });

            this.form = {
              email: '',
              name: '',
              password1: '',
              password2: ''
            }
            this.$router.push({name: 'login'})
          } else {
            this.toast.error(response.data.message, {
              toastClassName: "!bg-red-700 !text-slate-200",
            });

            const errorsObj = response.data.errors;
            const values = Object.values(errorsObj);
            if (values.length > 0) {
              const message = values.reduce((accum, msgArr, index) => {
                if (index === 0) {
                  accum = `- ${msgArr[0]}` 
                } else {
                  accum = accum + "\n" + `- ${msgArr[0]}`
                }
                return accum
              }, "")
              this.toast.error(message, {
                toastClassName: "!bg-red-700 !text-slate-200",
              });
            }            
          }
        }
        catch (error) {
          console.error(error)
        } finally {
          this.isLoading = false;
        }
      } else { 
        const messages = this.errors.reduce((accum, msg, index) => {
          if (index > 0) {
            accum = `- ${msg}`;
          } else {
            accum = accum + `- ${msg}`;
          }
          return accum
        }, '')    
        this.toast.error(messages, {
          toastClassName: "!bg-red-700 !text-slate-200",
        })   
      }
    }
  },
  name: 'SignUpView',
  components: {}
}
</script>
