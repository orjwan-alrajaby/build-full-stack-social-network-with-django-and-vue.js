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
        class="flex items-center justify-center w-40 h-10 px-4 py-2 mx-auto font-medium rounded-lg bg-lime-300 text-slate-950"
      >
        <TwoUsersIcon
          width="1.5rem"
          height="1.5rem"
          classes="text-slate-950"
         />
        <span class="ml-2">Friends</span>
      </div>
    </template>
  </div>
</template>

<script>
import TwoUsersIcon from './icons/TwoUsersIcon.vue'

export default {
  name: "UserCard",
  components: { TwoUsersIcon },
  props: {
    user: {}
  }
}
</script>