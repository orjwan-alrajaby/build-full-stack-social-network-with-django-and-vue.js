<template>
  <div class="grid grid-cols-5 gap-3 mx-auto xl:grid-cols-4 max-w-7xl">
    <div class="col-span-5 space-y-4 main-left md:col-span-3">
      <div
        class="h-full p-4 space-y-4 border rounded-lg bg-slate-950 border-lime-300"
      >
        <template
          v-if="isLoading"
        >
          <PageFeedback title="Loading Friends...">
              <LoaderIcon />
          </PageFeedback>
        </template>
        <h2
          class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700"
          v-if="
            friendshipsStore.friends.length >
              0 && !isLoading
          "
        >
          Friends ({{
            friendshipsStore.friends.length
          }})
        </h2>
        <div class="grid grid-cols-5 gap-3 xl:grid-cols-4">
          <template
            v-if="
              friendshipsStore.friends
                .length > 0 &&
              !isLoading
            "
          >
            <div
              class="col-span-5 p-4 space-y-4 text-center rounded-lg bg-slate-900 xl:col-span-1 sm:col-span-2"
              v-for="friend in friendshipsStore.friends"
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
                <p class="text-xs text-slate-400">
                  <router-link :to="{ name: 'user-friends', params: { id: friend.id } }">
                    {{ friend.friends_count }} friends
                  </router-link>
                </p>
                <p class="text-xs text-slate-400">{{ friend.posts_count }} posts</p>
              </div>
              <div class="space-x-3">
                <button
                  class="p-2 text-xs font-medium border rounded-lg w-fit border-lime-300 text-lime-300"
                >
                  Delete
                </button>

                <router-link
                  :to="{ name: 'user-profile', params: { id: friend.id } }"
                  class="p-2 text-xs font-medium rounded-lg bg-lime-300 text-slate-950"
                >
                Show
                </router-link>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>
    <template v-if="userStore.user.id === $route.params.id">
          <div class="col-span-5 space-y-4 main-right xl:col-span-1 md:col-span-2">
      <template
        v-if="
          !isLoading &&
          friendshipsStore.receivedRequests.length > 0
        "
      >
        <IncomingFriendRequests
          v-if="friendshipsStore.receivedRequests.length > 0"
          :list="friendshipsStore.receivedRequests"
        />

        <OutgoingFriendRequests
        v-if="friendshipsStore.sentRequests.length > 0"
         :list="friendshipsStore.sentRequests"
         />

        <PeopleYouMayKnow />
      </template>
      <template
        v-else-if="
          isLoading &&
          !friendshipsStore.isError
        "
      >
        <PageFeedback title="Loading Requests...">
          <LoaderIcon />
        </PageFeedback>
      </template>
    </div>
    </template>
  </div>
</template>

<script>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import { useUserStore } from "@/stores/user";
import { useFriendshipsStore } from "@/stores/friendships";
import { useToast } from "vue-toastification";
import IncomingFriendRequests from "../components/IncomingFriendRequests.vue";
import OutgoingFriendRequests from "../components/OutgoingFriendRequests.vue";
import LoaderIcon from "@/components/icons/LoaderIcon.vue"
import useGetFriendsAndRequests from "@/composables/friendships/useGetFriendsAndRequests"

export default {
  name: "UserFriendsView",
  components: {
    PeopleYouMayKnow,
    IncomingFriendRequests,
    OutgoingFriendRequests,
    LoaderIcon,
  },
  setup() {
    const toast = useToast();
    const userStore = useUserStore();
    const friendshipsStore = useFriendshipsStore();
    const { getFriendsAndRequests, data, isLoading, isError } = useGetFriendsAndRequests();

    return {
      userStore,
      friendshipsStore,
      toast,

      // 
      getFriendsAndRequests,
      data,
      isLoading,
      isError 
    };
  },
  data() {
    return {
      body: "",
    };
  },
  methods: {
    fetchFriendsAndRequests() {
      this.getFriendsAndRequests(
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
            return
          }
          this.friendshipsStore.setFriendsAndRequests(this.data);
        });
    },
  },
  mounted() {
    this.fetchFriendsAndRequests();
  },
  watch: {
    $route(to, from) {
      if (this.userStore.user.isAuthenticated && from.name === to.name && (from.params.id !== to.params.id)) {
        this.getFriendsAndRequests();
      }
    } 
   },
};
</script>
