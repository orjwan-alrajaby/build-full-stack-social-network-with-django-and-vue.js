<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div class="col-span-3 space-y-4 main-center lg:col-span-2">
      <CreatePostForm />
      <template
        v-if="
          postsStore.all.posts.length > 0 && !isError
        "
      >
        <PostItem
          v-for="post in postsStore.all.posts"
          :key="post.id"
          :post="post"
        />
      </template>
      <PageFeedback
        v-else-if="
          isLoading && !isError
        "
        :title="'Feed is loading...'"
      >
        <LoaderIcon />
      </PageFeedback>

      <PageFeedback
        v-else-if="
          isLoading && isError
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
        <DashedMessageBubbleIcon />
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
import DashedMessageBubbleIcon from "../components/icons/DashedMessageBubbleIcon.vue";
import WarningIcon from "@/components/icons/WarningIcon.vue";
import CreatePostForm from "@/components/forms/CreatePostForm.vue";

import { usePostsStore } from "@/stores/posts";
import { useUserStore } from "@/stores/user";

import useGetFeedPosts from "@/composables/posts/useGetFeedPosts";

export default {
  name: "FeedView",
  components: {
    PeopleYouMayKnow,
    Trends,
    PostItem,
    PageFeedback,
    LoaderIcon,
    DashedMessageBubbleIcon,
    WarningIcon,
    CreatePostForm,
  },
  setup() {
    const postsStore = usePostsStore();
    const userStore = useUserStore();

    const { getFeedPosts, data, isLoading, isError, error } = useGetFeedPosts();

    return {
      postsStore,
      userStore,

      //
      getFeedPosts,
      data,
      isLoading,
      isError,
      error
    };
  },
  data() {
    return {
      body: "",
    };
  },
  beforeMount() {
    if (
      this.userStore.user.isAuthenticated &&
      this.userStore.user.accessToken
    ) {
      this.getFeedPosts().then(res => {
        if (res.status === "error") {
          return;
        }
        this.postsStore.setAllPosts(this.data);
      });
    }
  },
};
</script>