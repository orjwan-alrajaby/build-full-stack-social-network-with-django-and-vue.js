<template>
  <div>
    <template v-if="user?.author?.name">
  <div
    class="px-4 py-8 space-y-6 text-center border rounded-lg bg-slate-950 border-lime-300 text-slate-200"
  >
    <img
      src="https://mighty.tools/mockmind-api/content/human/43.jpg"
      class="block w-full mx-auto mb-6 rounded-full max-w-40"
    />
    <p class="mb-4 text-xl uppercase text-lime-300">
      <strong>{{ user.author.name }}</strong>
    </p>
    <p
      class="font-medium text-md text-slate-200"
      v-if="this.$route.params.id === userStore.user.id"
    >
      {{ user.author.email }}
    </p>
    <div class="flex justify-center mt-6 space-x-8">
      <p class="text-xs text-slate-400">
        {{ user.author.friends_count }} friends
      </p>
      <p class="text-xs text-slate-400">
        {{ user.author.posts_count }} posts
      </p>
    </div>
    <div v-if="this.$route.params.id !== userStore.user.id" class="mt-8">
      <template v-if="user.author.is_friend_of_user">
        <div class="flex items-center justify-center space-x-4">
          <div
            class="flex items-center justify-center h-10 px-4 py-2 font-medium rounded-lg w-fit bg-lime-300 text-slate-950"
          >
            <TwoUsersIcon
              width="1.5rem"
              height="1.5rem"
              classes="text-slate-950"
            />
            <span class="ml-2">Friends</span>
          </div>
          <button
            class="flex items-center justify-center h-10 px-4 py-2 font-medium rounded-lg w-fit bg-lime-300 text-slate-950"
            @click="messageUser"
          >
            <DottedMessageBubbleIcon
              classes="text-slate-950"
              width="1.5rem"
              height="1.5rem"
            />
            <span class="ml-2">Message</span>
          </button>
        </div>
      </template>
      <template
        v-else-if="user.author.has_sent_friend_request_to"
      >
        <div
          class="flex items-center justify-center h-10 px-4 py-2 mx-auto font-medium rounded-lg w-fit bg-lime-300 text-slate-950"
        >
          <!-- <CircledTickIcon
            width="1.5rem"
            height="1.5rem"
            classes="text-slate-950"
          /> -->
          <span class="ml-2">Sent friend request</span>
        </div>
      </template>
      <template
        v-else-if="
          user.author.has_received_friend_request_from
        "
      >
        respond to friend request
      </template>
      <template v-else>
        <button
          type="button"
          @click.prevent="addFriend"
          class="flex items-center justify-center w-40 h-10 px-4 py-2 mx-auto font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-lime-900 disabled:cursor-not-allowed"
          :disabled="friendshipsStore.friendships.addFriend.isLoading"
        >
          <template v-if="friendshipsStore.friendships.addFriend.isLoading">
            <LoaderIcon
              width="1.5rem"
              height="1.5rem"
              classes="text-slate-950"
            />
          </template>
          <template v-else>
            <PlusUserIcon
              width="1.5rem"
              height="1.5rem"
              classes="text-slate-950"
            />
            <span class="ml-2">Add friend</span>
          </template>
        </button>
      </template>
    </div>
  </div>
</template>
  </div>
</template>

<script>
import {
  LoaderIcon,
  TwoUsersIcon,
  DottedMessageBubbleIcon,
  // CircledTickIcon,
  PlusUserIcon
} from "@/components/icons"

import useStartConversation from "@/composables/chat/useStartConversation";
import { usePostsStore } from "@/stores/posts";
import { useUserStore } from "@/stores/user";
import { useFriendshipsStore } from "@/stores/friendships";
import { useToast } from "vue-toastification";
import { storeToRefs } from "pinia";

export default {
  name: "UserProfileCard",
  components: {
    LoaderIcon,
    TwoUsersIcon,
    DottedMessageBubbleIcon,
    // CircledTickIcon,
    PlusUserIcon,
  },
  setup() {
    const { user } = storeToRefs(usePostsStore());
    const userStore = useUserStore();
    const friendshipsStore = useFriendshipsStore();
    const { startConversation } = useStartConversation();
    const toast = useToast();

    return {
      user,
      userStore,
      friendshipsStore,
      toast,
      startConversation,
    };
  },
  data() {
    return {
      body: "",
    };
  },
  methods: {
    async addFriend() {
      this.friendshipsStore
        .addFriend(this.userStore.user.accessToken, this.$route.params.id)
        .then((res) => {
          if (res.status === "success") {
            this.toast.success(`Friend request has been sent successfully!`, {
              toastClassName: "!bg-emerald-700 !text-slate-200",
            });
          } else {
            this.toast.error(
              `Friend request has failed to send. Reload the page and try again.`,
              {
                toastClassName: "!bg-red-700 !text-slate-200",
              }
            );
          }
        });
    },
    messageUser() {
      this.startConversation(this.$route.params.id).then((res) => {
        if (res.status === "success") {
          this.$router.push({ name: "messages" });
        } else {
          this.toast.error(`Failed to start conversation with user.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      });
    },
  },
  unmounted() {
    this.friendshipsStore.resetFriendshipsStore();
  },
};
</script>