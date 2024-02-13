<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div class="col-span-3 space-y-4 main-center lg:col-span-2">
      <div class="border rounded-lg bg-slate-950 border-lime-300">
        <div class="p-4">
          <textarea
            class="w-full p-4 rounded-lg bg-slate-200 text-slate-950"
            placeholder="What are you thinking about?"
            v-model="body"
          ></textarea>
        </div>
        <div
          class="flex items-center justify-between pt-4 m-4 mt-0 border-t border-slate-700"
        >
          <div>
            <img
              src="https://mighty.tools/mockmind-api/content/human/43.jpg"
              class="hidden w-12 rounded-full sm:block"
            />
          </div>
          <form method="POST" @submit.prevent="submitForm">
            <button
              class="w-16 h-10 mx-2 font-medium bg-transparent border rounded-lg text-lime-300 border-lime-300"
            >
              <PictureIcon
                height="1.5rem"
                width="1.5rem"
                classes="text-lime-300"
              />
            </button>

            <button
              class="w-16 h-10 mx-2 font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-lime-900 disabled:cursor-not-allowed"
              :disabled="!body || postsStore.posts.newPost.isLoading"
              @click="submitForm"
            >
              <LoaderIcon
                v-if="postsStore.posts.newPost.isLoading"
                width="1.5rem"
                height="1.5rem"
                classes="text-slate-950"
              />
              <SendIcon
                v-else
                height="1.5rem"
                width="1.5rem"
                classes="text-slate-950"
              />
            </button>
          </form>
        </div>
      </div>
      <template
        v-if="
          postsStore.posts.all.data.length > 0 && !postsStore.posts.all.isError
        "
      >
        <PostItem
          v-for="post in postsStore.posts.all.data"
          :key="post.id"
          :post="post"
        />
      </template>
      <PageFeedback
        v-else-if="
          postsStore.posts.all.isLoading && !postsStore.posts.all.isError
        "
        :title="'Feed is loading...'"
      >
        <LoaderIcon />
      </PageFeedback>

      <PageFeedback
        v-else-if="
          postsStore.posts.all.isLoading && postsStore.posts.all.isError
        "
        :title="'Something went wrong :('"
        :subtitle="'Please press [CTRL + R] to refresh, or try to logout and login again.'"
        :isError="true"
      >
        <WarningIcon />
      </PageFeedback>

      <PageFeedback
        v-else
        :title="'There is nothing here yet.'"
        :subtitle="'Make your first post and start the conversation :)'"
      >
        <MessageBubble1Icon />
      </PageFeedback>
    </div>

    <div class="col-span-3 space-y-4 main-right lg:col-span-1">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>

<script>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import PageFeedback from "@/components/PageFeedback.vue";
import Trends from "../components/Trends.vue";
import PostItem from "../components/PostItem.vue";
import LoaderIcon from "../components/icons/LoaderIcon.vue";
import MessageBubble1Icon from "../components/icons/MessageBubble1Icon.vue";
import PictureIcon from "../components/icons/PictureIcon.vue";
import WarningIcon from "@/components/icons/WarningIcon.vue";
import SendIcon from "@/components/icons/SendIcon.vue";

import { usePostsStore } from "@/stores/posts";
import { useUserStore } from "@/stores/user";
import { useToast } from "vue-toastification";

export default {
  setup() {
    const postsStore = usePostsStore();
    const userStore = useUserStore();
    const toast = useToast();

    return {
      postsStore,
      userStore,
      toast,
    };
  },
  name: "FeedView",
  components: {
    PeopleYouMayKnow,
    Trends,
    PostItem,
    PageFeedback,
    LoaderIcon,
    MessageBubble1Icon,
    PictureIcon,
    WarningIcon,
    SendIcon,
  },
  data() {
    return {
      body: "",
    };
  },
  mounted() {
    if (
      this.userStore.user.isAuthenticated &&
      this.userStore.user.accessToken
    ) {
      this.postsStore.getAllPosts(this.userStore.user.accessToken);
    }
  },
  methods: {
    submitForm() {
      this.postsStore
        .createPost(this.userStore.user.accessToken, this.body, this.toast)
        .then(() => {
          this.body = "";
          this.postsStore.updatePostList();
        });
    },
  },
};
</script>