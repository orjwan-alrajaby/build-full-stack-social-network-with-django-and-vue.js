<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div
      class="order-last col-span-3 space-y-4 main-center lg:col-span-2 lg:order-first"
    >
      <div
        class="border rounded-lg bg-slate-950 border-lime-300"
        v-if="this.$route.params.id === userStore.user.id"
      >
        <div class="p-4">
          <textarea
            class="w-full p-4 rounded-lg bg-slate-200 text-slate-950"
            placeholder="What are you thinking about?"
            v-model="body"
          ></textarea>
        </div>

        <div
          class="flex items-center justify-end pt-4 m-4 mt-0 border-t border-slate-700"
        >
          <form method="POST" @submit.prevent="submitForm">
            <button
              class="w-16 h-10 mx-2 font-medium bg-transparent border rounded-lg border-lime-300"
            >
              <PictureIcon
                width="1.5rem"
                height="1.5rem"
                classes="text-lime-300"
              />
            </button>

            <button
              class="w-16 h-10 mx-2 font-medium rounded-lg bg-lime-300 disabled:bg-lime-900 disabled:cursor-not-allowed"
              :disabled="!body || postsStore.posts.newPost.isLoading"
              @click="submitForm"
            >
              <LoaderIcon v-if="postsStore.posts.newPost.isLoading" />
              <SendIcon
                v-else
                width="1.5rem"
                height="1.5rem"
                classes="text-slate-950"
              />
            </button>
          </form>
        </div>
      </div>
      <template
        v-if="
          postsStore.posts.userPosts.data.length > 0 &&
          !postsStore.posts.userPosts.isError
        "
      >
        <PostItem
          v-for="post in postsStore.posts.userPosts.data"
          :key="post.id"
          :post="post"
        />
      </template>
      <PageFeedback
        title="Feed is loading..."
        v-else-if="
          postsStore.posts.userPosts.isLoading &&
          !postsStore.posts.userPosts.isError
        "
      >
        <LoaderIcon />
      </PageFeedback>
      <PageFeedback
        title="Something went wrong"
        subtitle="Please press [CTRL + R] to refresh, or try to
          logout and login again."
        :isError="true"
        v-else-if="
          !postsStore.posts.userPosts.isLoading &&
          postsStore.posts.userPosts.isError
        "
      >
        <WarningIcon />
      </PageFeedback>
    </div>
    <div class="order-first col-span-3 main-right lg:col-span-1 lg:order-last">
      <div
        class="px-4 py-8 space-y-6 text-center border rounded-lg bg-slate-950 border-lime-300 text-slate-200"
      >
        <img
          src="https://mighty.tools/mockmind-api/content/human/43.jpg"
          class="block w-full mx-auto mb-6 rounded-full max-w-40"
        />

        <p class="mb-4 text-xl uppercase text-lime-300">
          <strong>{{ postsStore.posts.userPosts.author.name }}</strong>
        </p>
        <p
          class="font-medium text-md text-slate-200"
          v-if="this.$route.params.id === userStore.user.id"
        >
          {{ postsStore.posts.userPosts.author.email }}
        </p>
        <div class="flex justify-center mt-6 space-x-8">
          <p class="text-xs text-slate-400">
            {{ postsStore.posts.userPosts.author.friends_count }} friends
          </p>
          <p class="text-xs text-slate-400">
            {{ postsStore.posts.userPosts.author.posts_count }} posts
          </p>
        </div>
        <div v-if="this.$route.params.id !== userStore.user.id" class="mt-8">
          <template v-if="postsStore.posts.userPosts.author.is_friend_of_user">
            <div class="flex items-center justify-center space-x-4">
              <div
                class="flex items-center justify-center h-10 px-4 py-2 font-medium rounded-lg w-fit bg-lime-300 text-slate-950"
              >
                <TwoFriendsIcon
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
            v-else-if="
              postsStore.posts.userPosts.author.has_sent_friend_request_to
            "
          >
            <div
              class="flex items-center justify-center h-10 px-4 py-2 mx-auto font-medium rounded-lg w-fit bg-lime-300 text-slate-950"
            >
              <CircledTickIcon
                width="1.5rem"
                height="1.5rem"
                classes="text-slate-950"
              />
              <span class="ml-2">Sent friend request</span>
            </div>
          </template>
          <template
            v-else-if="
              postsStore.posts.userPosts.author.has_received_friend_request_from
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
    </div>
  </div>
</template>

<script>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import PostItem from "../components/PostItem.vue";
import { usePostsStore } from "@/stores/posts";
import { useUserStore } from "@/stores/user";
import { useFriendshipsStore } from "@/stores/friendships";
import useStartConversation from "@/composition-functions/useStartConversation";
import { useToast } from "vue-toastification";
import SendIcon from "@/components/icons/SendIcon.vue";
import LoaderIcon from "@/components/icons/LoaderIcon.vue";
import PictureIcon from "@/components/icons/PictureIcon.vue";
import WarningIcon from "@/components/icons/WarningIcon.vue";
import PageFeedback from "@/components/PageFeedback.vue";
import TwoFriendsIcon from "@/components/icons/TwoFriendsIcon.vue";
import DottedMessageBubbleIcon from "@/components/icons/DottedMessageBubbleIcon.vue";
import CircledTickIcon from "../components/icons/CircledTickIcon.vue";
import PlusUserIcon from "../components/icons/PlusUserIcon.vue";

export default {
  setup() {
    const postsStore = usePostsStore();
    const userStore = useUserStore();
    const friendshipsStore = useFriendshipsStore();
    const { startConversation } = useStartConversation();
    const toast = useToast();

    return {
      postsStore,
      userStore,
      friendshipsStore,
      toast,
      startConversation,
    };
  },
  name: "UserProfileView",
  components: {
    PeopleYouMayKnow,
    Trends,
    PostItem,
    SendIcon,
    LoaderIcon,
    PictureIcon,
    WarningIcon,
    PageFeedback,
    TwoFriendsIcon,
    DottedMessageBubbleIcon,
    CircledTickIcon,
    PlusUserIcon,
  },
  data() {
    return {
      body: "",
    };
  },
  mounted() {
    if (!this.$route.params.id) {
      this.$router.push({ name: "feed" });
    } else if (
      this.userStore.user.isAuthenticated &&
      this.userStore.user.accessToken &&
      this.$route.params.id
    ) {
      this.postsStore.getUserPosts(
        this.userStore.user.accessToken,
        this.$route.params.id
      );
    }
  },
  methods: {
    submitForm() {
      this.postsStore
        .createPost(this.userStore.user.accessToken, this.body, this.toast)
        .then(() => {
          this.body = "";
          this.postsStore.updatePostList(
            this.userStore.user.id,
            this.$route.params.id
          );
        });
    },
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
  watch: {
    $route(to, from) {
      if (
        this.userStore.user.isAuthenticated &&
        from.name === to.name &&
        from.params.id !== to.params.id
      ) {
        this.postsStore.getUserPosts(
          this.userStore.user.accessToken,
          to.params.id
        );
      }
    },
  },
  unmounted() {
    this.friendshipsStore.resetFriendshipsStore();
  },
};
</script>