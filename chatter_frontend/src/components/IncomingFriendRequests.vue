<template>
  <div class="p-4 border rounded-lg bg-gray-950 border-lime-300">
    <h3 class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700">
      Incoming Friend Requests ({{ list.length }})
    </h3>
    <div class="grid grid-cols-2 gap-3">
      <div
        class="col-span-2 p-4 space-y-4 text-center bg-gray-900 rounded-lg md:col-span-2 sm:col-span-1"
        v-for="item in list"
        :key="item.id"
      >
        <img
          src="https://mighty.tools/mockmind-api/content/human/40.jpg"
          class="block w-full mx-auto mb-6 rounded-full max-w-40"
        />
        <p class="text-sm uppercase text-slate-200">
          <strong>
            <router-link
              :to="{ name: 'user-profile', params: { id: item.created_by.id } }"
              >{{ item.created_by.name }}</router-link
            >
          </strong>
        </p>
        <div class="flex justify-around mt-6 space-x-8">
          <p class="text-xs text-slate-400">
            <router-link
              :to="{ name: 'user-friends', params: { id: item.created_by.id } }"
            >
              {{ item.created_by.friends_count }} friends
            </router-link>
          </p>
          <p class="text-xs text-slate-400">
            {{ item.created_by.posts_count }} posts
          </p>
        </div>
        <div class="space-x-3">
          <button
            id="reject-request-button"
            class="w-10 h-10 text-xs font-medium border rounded-full border-lime-300 text-lime-300"
            @click="handleFriendshipRequest('rejected', item.created_by.id)"
          >
            <TrashIcon width="1.5rem" height="1.5rem" classes="text-lime-300" />
          </button>
          <button
            id="accept-request-button"
            class="w-10 h-10 text-xs font-medium rounded-full bg-lime-300 text-slate-950"
            @click="handleFriendshipRequest('accepted', item.created_by.id)"
          >
            <PlusUserIcon
              :isFilled="true"
              width="1.5rem"
              height="1.5rem"
              classes="text-slate-950"
            />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { TrashIcon, PlusUserIcon } from "@/components/icons";

import { useFriendshipsStore } from "@/stores/friendships";
import { useUserStore } from "@/stores/user";
import { useToast } from "vue-toastification";
import useRespondToFriendRequest from "@/composables/friendships/useRespondToFriendRequest"

export default {
  name: "IncomingFriendRequests",
  components: {
    TrashIcon,
    PlusUserIcon,
  },
  setup() {
    const { respondToFriendRequest } = useRespondToFriendRequest();
    const friendshipsStore = useFriendshipsStore();
    const userStore = useUserStore();
    const toast = useToast();

    return {
      friendshipsStore,
      userStore,
      toast,

      //
      respondToFriendRequest,
    };
  },
  props: {
    list: Array,
  },
  methods: {
    handleFriendshipRequest(status, senderId) {
      this.respondToFriendRequest(
          status,
          senderId
        )
        .then((res) => {
          if (res.status === "error") {
            this.toast.error(
              `Failed to respond to friend request. Reload the page and try again.`,
              {
                toastClassName: "!bg-red-700 !text-slate-200",
              }
            );
            return;
          }
          
          this.toast.success(
            `Friend request has been ${status} successfully!`,
            {
              toastClassName: "!bg-emerald-700 !text-slate-200",
            }
          ); 
        });
    },
  },
};
</script>
