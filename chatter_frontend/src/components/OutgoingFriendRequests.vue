<template>
  <div class="p-4 space-y-4 border rounded-lg bg-gray-950 border-lime-300">
    <h3 class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700">
      Outgoing Friend Requests ({{ list.length }})
    </h3>

    <div class="flex items-center justify-between" v-for="request in list" :key="request.id">
      <div class="flex items-center space-x-2">
        <img
          src="https://mighty.tools/mockmind-api/content/human/49.jpg"
          class="rounded-full w-[40px]"
        />

        <p class="text-xs text-slate-200 text-ellipsis">
          <strong>
            <router-link :to="{ name: 'user-profile', params: { id: request.created_for.id } }">
              {{ request.created_for.name }}
            </router-link>
          </strong>
        </p>
      </div>
      <div class="flex items-center space-x-2">
        <button
          class="flex items-center justify-center w-16 p-2 space-x-2 text-xs font-medium border rounded-lg border-lime-300 text-lime-300 disabled:text-lime-900 disabled:border-lime-900 disabled:cursor-not-allowed"
          @click="handleCancel(request.created_for.id)"
          :disabled="friendshipsStore.friendships.deleteRequest.isLoading"
        >
        <svg v-if="friendshipsStore.friendships.deleteRequest.isLoading" xmlns="http://www.w3.org/2000/svg" width="1.5rem" height="1.5rem" viewBox="0 0 24 24" class="mx-auto">
          	<path fill="currentColor" d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z" opacity="0.5" />
          	<path fill="currentColor" d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z">
          		<animateTransform attributeName="transform" dur="0.75s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12" />
          	</path>
          </svg>
          <span v-else>Cancel</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";
import { useFriendshipsStore } from "@/stores/friendships";
import { useToast } from "vue-toastification";

export default {
    setup() {
    const userStore = useUserStore();
    const friendshipsStore = useFriendshipsStore();
    const toast = useToast();

    return {
      userStore,
      friendshipsStore,
      toast,
    };
  },
  props: {
    list: Array,
  },
  methods: {
    handleCancel(receiverId) {
      this.friendshipsStore.cancelSentRequest(this.userStore.user.accessToken, receiverId).then((res) => {
        if (res.status === "success") {
          this.toast.success(`Friend request has been cancelled successfully!`, {
            toastClassName: "!bg-emerald-700 !text-slate-200"
          });
        } else {
          this.toast.error(`Failed to cancel friend request. Reload the page and try again.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });          
        }
      })
    }
  }
};
</script>
