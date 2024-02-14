<template>
  <div
    class="p-4 space-y-6 text-center border rounded-lg bg-slate-950 border-lime-300"
  >
    <img
      src="https://mighty.tools/mockmind-api/content/human/40.jpg"
      class="w-full mx-auto mb-6 rounded-full max-w-40"
    />

    <p class="uppercase text-lime-300">
      <strong>
        <router-link :to="{ name: 'user-profile', params: { id: user.id } }">
          {{ user.name }}
        </router-link>
      </strong>
    </p>

    <div class="flex justify-around mt-6 space-x-8">
      <p class="text-xs text-slate-400">
        <router-link :to="{ name: 'user-friends', params: { id: user.id } }">
          {{ user.friends_count }} friends
        </router-link>
      </p>
      <p class="text-xs text-slate-400">{{ user.posts_count }} posts</p>
    </div>

    <template v-if="user.is_friend_of_user">
      <div
        class="flex items-center justify-center w-40 h-10 px-4 py-2 mx-auto font-medium rounded-lg bg-lime-300 text-slate-900"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          class="w-6 h-6"
        >
          <path
            d="M4.5 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM14.25 8.625a3.375 3.375 0 1 1 6.75 0 3.375 3.375 0 0 1-6.75 0ZM1.5 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM17.25 19.128l-.001.144a2.25 2.25 0 0 1-.233.96 10.088 10.088 0 0 0 5.06-1.01.75.75 0 0 0 .42-.643 4.875 4.875 0 0 0-6.957-4.611 8.586 8.586 0 0 1 1.71 5.157v.003Z"
          />
        </svg>
        <span class="ml-2">Friends</span>
      </div>
    </template>
  </div>
</template>
<script>
export default {
  props: {
    user: {
      
    }
  }
}
</script>