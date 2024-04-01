<template>
  <div
    class="items-center justify-between px-6 py-6 mx-auto border rounded-lg lg:max-w-5xl lg:flex lg:px-12 bg-slate-950 border-lime-300">
    <div class="py-4 lg:border-y lg:border-lime-300 lg:w-2/5">
      <h1 class="mb-6 text-xl font-bold text-center text-lime-300">
        Hello and welcome to Chatter!
      </h1>
      <p class="text-lg text-center text-slate-200">
        Log onto your account and start chatting with your friends!
      </p>
    </div>
    <form class="block space-y-6 lg:w-3/6" v-on:submit.prevent="submitForm">
      <div>
        <label class="block mb-3 text-slate-200">Email Address</label>
        <input placeholder="Enter email address" type="text"
          class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          v-model="form.email" />
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Password</label>
        <input placeholder="Enter password" type="password"
          class="block w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          v-model="form.password" />
      </div>
      <div>
        <button
          class="flex items-center justify-center w-full h-10 px-4 py-2 font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-slate-600"
          :disabled="isLoading">
          <span class="px-4" v-if="!isLoading">Log In</span>
          <LoaderIcon v-if="isLoading" width="1.5rem" height="1.5rem"
            classes="text-slate-950" />
        </button>
      </div>
      <p class="mt-10 text-sm text-slate-400">
        Don't have an account? Go ahead and
        <router-link :to="{ name: 'sign-up' }" class="text-lime-300">Create
          one</router-link>.
      </p>
    </form>
  </div>
</template>

<script>
import LoaderIcon from "@/components/icons/LoaderIcon.vue";
import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";
import useLogin from "@/composables/user/useLogin";
import useGetUser from "@/composables/user/useGetUser";

export default {
  name: "LoginView",
  components: {
    LoaderIcon,
  },
  setup() {
    const { handleLogin, isLoading: loginIsLoading } = useLogin();
    const { handleGetUser, isLoading: getUserIsLoading } = useGetUser();
    const toast = useToast();
    const userStore = useUserStore();

    return {
      toast,
      userStore,

      // useLogin composable
      handleLogin,
      
      // useGetUser composable
      handleGetUser,
      
      isLoading: loginIsLoading || getUserIsLoading,
    };
  },
  data() {
    return {
      form: {
        email: "orjwan.alrajaby@gmail.com",
        password: "Kiitos123456@@@",
      },
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];

      if (!this.form.email) {
        this.errors.push("You must enter a valid email address!");
      }

      if (!this.form.password) {
        this.errors.push("You must enter a valid password!");
      }

      if (this.errors.length > 0) {
        const messages = this.errors.reduce((str, msg, index) => {
          if (index === 0) {
            str = `- ${msg}`;
          } else {
            str = str + "\n" + `- ${msg}`;
          }
          return str;
        }, "");

        this.toast.error(messages, {
          toastClassName: "!bg-red-700 !text-slate-200",
        });

        return;
      }

      this.handleLogin(this.form).then((res) => {
        if (res.status === "error") {
          this.toast.error(res.message, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
          return;
        }

        this.userStore.handleSetToken(res.data);

        this.handleGetUser().then((res) => {
          this.userStore.setUserInfo(res.data);

          this.form = {
            email: "",
            password: "",
          };

          this.toast.success("You have logged in successfully.", {
            toastClassName: "!bg-emerald-700 !text-slate-200",
          });

          this.$router.push({ name: "home" });
        })
      })
    },
  },
};
</script>
