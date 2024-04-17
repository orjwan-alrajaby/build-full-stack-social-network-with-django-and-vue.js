<template>
  <div class="p-4 space-y-4 border rounded-lg bg-gray-950 border-lime-300">
    <h3 class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700">
      Outgoing Friend Requests ({{ list.length }})
    </h3>

    <div
      class="flex items-center justify-between"
      v-for="request in list"
      :key="request.id"
    >
      <div class="flex items-center space-x-2">
        <img
          src="https://mighty.tools/mockmind-api/content/human/49.jpg"
          class="rounded-full w-[40px]"
        />

        <p class="text-xs text-slate-200 text-ellipsis">
          <strong>
            <router-link
              :to="{
                name: 'user-profile',
                params: { id: request.created_for.id },
              }"
            >
              {{ request.created_for.name }}
            </router-link>
          </strong>
        </p>
      </div>
      <div class="flex items-center space-x-2">
        <button
          class="flex items-center justify-center w-16 p-2 space-x-2 text-xs font-medium border rounded-lg border-lime-300 text-lime-300 disabled:text-lime-900 disabled:border-lime-900 disabled:cursor-not-allowed"
          @click="handleCancel(request.created_for.id)"
          :disabled="isLoading"
        >
          <LoaderIcon v-if="isLoading" width="1.5rem" height="1.5rem" classes="text-lime-300"/>
          <span v-else>Cancel</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { LoadingIcon } from "@/components/icons";

import { useUserStore } from "@/stores/user";
import { useFriendshipsStore } from "@/stores/friendships";
import { useToast } from "vue-toastification";

import useCancelFriendRequest from "@/composables/friendships/useCancelFriendRequest"

export default {
  name: "OutgoingFriendRequests",
  components: {
    LoadingIcon,
  },
  setup() {
    const userStore = useUserStore();
    const friendshipsStore = useFriendshipsStore();
    const toast = useToast();
    const { cancelFriendRequest, isLoading } = useCancelFriendRequest();

    return {
      userStore,
      friendshipsStore,
      toast,

      //
      cancelFriendRequest,
      isLoading 
    };
  },
  props: {
    list: Array,
  },
  methods: {
    handleCancel(receiverId) {
      this.friendshipsStore
        .cancelSentRequest(receiverId)
        .then((res) => {
          if (res.status === "error") {
            this.toast.error(
              `Failed to cancel friend request. Reload the page and try again.`,
              {
                toastClassName: "!bg-red-700 !text-slate-200",
              }
            );
            return;
          }
          this.friendshipsStore.deleteSentRequest(receiverId);
          this.toast.success(
              `Friend request has been cancelled successfully!`,
              {
                toastClassName: "!bg-emerald-700 !text-slate-200",
              }
            );
        });
    },
  },
};
</script>
