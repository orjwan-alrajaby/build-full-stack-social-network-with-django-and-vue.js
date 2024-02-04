<template>
  <div class="grid grid-cols-5 gap-3 mx-auto xl:grid-cols-4 max-w-7xl">
    <div class="col-span-5 space-y-4 main-left md:col-span-3">
      <div
        class="h-full p-4 space-y-4 border rounded-lg bg-gray-950 border-lime-300"
      >
        <template
          v-if="friendshipsStore.friendships.getFriendsAndRequests.isLoading"
        >
          <div
            class="flex flex-col items-center justify-center h-96 text-slate-200"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="5rem"
              height="5rem"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
                opacity="0.5"
              />
              <path
                fill="currentColor"
                d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z"
              >
                <animateTransform
                  attributeName="transform"
                  dur="0.75s"
                  repeatCount="indefinite"
                  type="rotate"
                  values="0 12 12;360 12 12"
                />
              </path>
            </svg>
            <span class="mt-4 text-lg">Loading Friends...</span>
          </div>
        </template>
        <h2
          class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700"
          v-if="
            friendshipsStore.friendships.getFriendsAndRequests.friends.length >
              0 && !friendshipsStore.friendships.getFriendsAndRequests.isLoading
          "
        >
          My Friends ({{
            friendshipsStore.friendships.getFriendsAndRequests.friends.length
          }})
        </h2>
        <div class="grid grid-cols-5 gap-3 xl:grid-cols-4">
          <template
            v-if="
              friendshipsStore.friendships.getFriendsAndRequests.friends
                .length > 0 &&
              !friendshipsStore.friendships.getFriendsAndRequests.isLoading
            "
          >
            <div
              class="col-span-5 p-4 space-y-4 text-center bg-gray-900 rounded-lg xl:col-span-1 sm:col-span-2"
              v-for="friend in friendshipsStore.friendships
                .getFriendsAndRequests.friends"
              :key="friend.id"
            >
              <img
                src="https://mighty.tools/mockmind-api/content/human/40.jpg"
                class="block w-full mx-auto mb-6 rounded-full max-w-40"
              />

              <p class="uppercase text-lime-300">
                <strong>
                  <router-link
                    :to="{ name: 'user-profile', params: { id: friend.id } }"
                    >{{ friend.name }}</router-link
                  >
                </strong>
              </p>

              <div class="flex justify-around mt-6 space-x-8">
                <p class="text-xs text-slate-400">182 friends</p>
                <p class="text-xs text-slate-400">120 posts</p>
              </div>
              <div class="space-x-3">
                <button
                  class="p-2 text-xs font-medium border rounded-lg w-fit border-lime-300 text-lime-300"
                >
                  <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mx-auto">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
                  </svg> -->
                  Delete
                </button>

                <router-link
                  :to="{ name: 'user-profile', params: { id: friend.id } }"
                  class="p-2 text-xs font-medium rounded-lg bg-lime-300 text-slate-900"
                >
                Show
                  <!-- <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                    class="w-5 h-5 mx-auto"
                  >
                    <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z" />
                    <path
                      fill-rule="evenodd"
                      d="M1.323 11.447C2.811 6.976 7.028 3.75 12.001 3.75c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113-1.487 4.471-5.705 7.697-10.677 7.697-4.97 0-9.186-3.223-10.675-7.69a1.762 1.762 0 0 1 0-1.113ZM17.25 12a5.25 5.25 0 1 1-10.5 0 5.25 5.25 0 0 1 10.5 0Z"
                      clip-rule="evenodd"
                    />
                  </svg> -->
                </router-link>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
    <div class="col-span-5 space-y-4 main-right xl:col-span-1 md:col-span-2">
      <template
        v-if="
          !friendshipsStore.friendships.getFriendsAndRequests.isLoading &&
          friendshipsStore.friendships.getFriendsAndRequests.requests.length > 0
        "
      >
        <IncomingFriendRequests
          v-if="friendshipsStore.friendships.getFriendsAndRequests.requests"
          :list="friendshipsStore.friendships.getFriendsAndRequests.requests"
        />

        <OutgoingFriendRequests :list="[]" />

        <PeopleYouMayKnow />
      </template>
      <template
        v-else-if="
          friendshipsStore.friendships.getFriendsAndRequests.isLoading &&
          !friendshipsStore.friendships.getFriendsAndRequests.isError
        "
      >
        <div
          class="flex flex-col items-center justify-center h-full border rounded-lg text-slate-200 bg-gray-950 border-lime-300"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="5rem"
            height="5rem"
            viewBox="0 0 24 24"
          >
            <path
              fill="currentColor"
              d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
              opacity="0.5"
            />
            <path
              fill="currentColor"
              d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z"
            >
              <animateTransform
                attributeName="transform"
                dur="0.75s"
                repeatCount="indefinite"
                type="rotate"
                values="0 12 12;360 12 12"
              />
            </path>
          </svg>
          <span class="mt-4 text-lg">Loading Requests...</span>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import { useUserStore } from "@/stores/user";
import { useFriendshipsStore } from "@/stores/friendships";
import { useToast } from "vue-toastification";
import IncomingFriendRequests from "../components/IncomingFriendRequests.vue";
import OutgoingFriendRequests from "../components/OutgoingFriendRequests.vue";

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
  name: "UserFriendView",
  components: {
    PeopleYouMayKnow,
    IncomingFriendRequests,
    OutgoingFriendRequests,
  },
  data() {
    return {
      body: "",
    };
  },
  mounted() {
    this.getFriendsAndRequests();
  },
  methods: {
    async getFriendsAndRequests() {
      this.friendshipsStore
        .getFriendsAndRequests(
          this.userStore.user.accessToken,
          this.$route.params.id
        )
        .then((res) => {
          if (res.status === "error") {
            this.toast.error(
              `friends and friend requests have failed to load. Try reloading the page.`,
              {
                toastClassName: "!bg-red-700 !text-slate-200",
              }
            );
          }
        });
    },
  },
  unmounted() {
    this.friendshipsStore.resetFriendshipsStore();
  },
};
</script>
