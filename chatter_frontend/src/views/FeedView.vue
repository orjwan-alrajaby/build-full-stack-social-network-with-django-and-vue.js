<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div class="col-span-3 space-y-4 main-center lg:col-span-2">
      <CreatePostForm />
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
import WarningIcon from "@/components/icons/WarningIcon.vue";
import CreatePostForm from "@/components/forms/CreatePostForm.vue"

import { usePostsStore } from "@/stores/posts";
import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const postsStore = usePostsStore();
    const userStore = useUserStore();

    return {
      postsStore,
      userStore,
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
    WarningIcon,
    CreatePostForm,
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
};
</script>