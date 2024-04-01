<template>
  <div
    class="items-center justify-between px-6 py-6 mx-auto border rounded-lg lg:max-w-5xl lg:flex lg:px-12 bg-slate-950 border-lime-300">
    <div class="py-4 lg:border-y lg:border-lime-300 lg:w-2/5">
      <h1 class="mb-6 text-xl font-bold text-center text-lime-300">Hello and
        welcome to Chatter!</h1>
      <p class="text-lg text-center text-slate-200">Sign up today to start
        chatting with your friends!</p>
    </div>
    <form class="block space-y-6 lg:w-3/6" v-on:submit.prevent="submitForm">
      <div>
        <label class="block mb-3 text-slate-200">Full Name</label>
        <input placeholder="Enter full name" type="text"
          class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          v-model="form.name" required />
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Email Address</label>
        <input placeholder="Enter email address" type="text"
          class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          v-model="form.email" required />
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Password</label>
        <input placeholder="Enter password" type="password"
          class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          v-model="form.password1" required />
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Confirm Password</label>
        <input placeholder="Confirm password" type="password"
          class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          v-model="form.password2" required />
      </div>
      <div>
        <button
          class="flex items-center justify-center w-full h-10 px-4 py-2 font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-slate-600"
          :disabled="isLoading">
          <span class="px-4" v-if="!isLoading">Create Account</span>
          <LoaderIcon v-if="isLoading" classes="text-slate-950" />
        </button>
      </div>
      <p class="mt-10 text-sm text-slate-400">Already have an account? Go ahead
        and <router-link :to="{ name: 'login' }" class="text-lime-300">Log
          In</router-link>.</p>
    </form>
  </div>
</template>

<script>
import LoaderIcon from '@/components/icons/LoaderIcon.vue';

import useSignUp from "@/composables/user/useSignUp";
import { useToast } from "vue-toastification";

export default {
  name: 'SignUpView',
  components: {
    LoaderIcon
  },
  setup() {
    const toast = useToast();

    const { handleSignUp, data, isLoading, error, isError } = useSignUp();

    return {
      toast,
      handleSignUp,
      data,
      isLoading,
      error,
      isError
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

      if (this.errors.length > 0) {
        const messages = this.errors.reduce((str, msg, index) => {
          if (index > 0) {
            str = `- ${msg}`;
          } else {
            str = str + `- ${msg}`;
          }
          return str
        }, '')
        this.toast.error(messages, {
          toastClassName: "!bg-red-700 !text-slate-200",
        })
        return
      }

      this.handleSignUp(this.form).then((res) => {
        if (res.status === "error") {
          
          this.toast.error(response.data.message, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });

          const errorsObj = response.data.errors;
          const values = Object.values(errorsObj);
          
          if (values.length > 0) {
            const message = values.reduce((str, msgArr, index) => {
              if (index === 0) {
                str = `- ${msgArr[0]}`
              } else {
                str = str + "\n" + `- ${msgArr[0]}`
              }
              return str
            }, "")
            
            this.toast.error(message, {
              toastClassName: "!bg-red-700 !text-slate-200",
            });
          }
          return
        }

        this.toast.success('The user has been registered successfully. Now please log in.', {
          toastClassName: "!bg-emerald-700 !text-slate-200",
        });

        this.form = {
          email: '',
          name: '',
          password1: '',
          password2: ''
        }
        
        this.$router.push({ name: 'login' })
      })
    }
  },
}
</script>
