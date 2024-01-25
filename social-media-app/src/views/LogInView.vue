<template>
  <div class="lg:max-w-5xl mx-auto lg:flex items-center justify-between py-6 px-6 lg:px-12 bg-gray-950 border border-lime-300 rounded-lg">
    <div class="lg:border-y lg:border-lime-300 py-4 lg:w-2/5">
      <h1 class="text-lime-300 text-xl mb-6 font-bold text-center">Hello and welcome to Chatter!</h1>
      <p class="text-lg text-slate-200 text-center">Log onto your account and start chatting with your friends!</p>
    </div>
    <form class="block space-y-6 lg:w-3/6">
      <div>
        <label class="block mb-3 text-slate-200">Email Address</label>
        <input placeholder="Enter email address" type="text" class="block p-2 w-full rounded-lg bg-slate-200 text-slate-900"/>
      </div>
      <div>
        <label class="block mb-3 text-slate-200">Confirm Password</label>
        <input placeholder="Repeat password" type="password" class="block p-2 w-full rounded-lg bg-slate-200 text-slate-900"/>
      </div>
      <div>
        <button class="block py-2 px-4 bg-lime-300 text-slate-900 rounded-lg w-full font-medium">Log in</button>
      </div>
      <p class="text-sm text-slate-400 mt-10">Don't have an account? Go ahead and <router-link :to="{name:'signUp'}" class="text-lime-300">Create one</router-link>.</p>
    </form>
  </div>
</template>

<script>

export default {
  name: 'SignUpView',
  components: {}
}
</script>
