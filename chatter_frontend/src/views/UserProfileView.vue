<template>
  <div class="grid grid-cols-3 gap-4 mx-auto max-w-7xl">
    <div
      class="order-last col-span-3 space-y-4 main-center lg:col-span-2 lg:order-first"
    >
      <template v-if="this.$route.params.id === userStore.user.id">
        <CreatePostForm />
      </template>
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
      <UserProfileCard />
    </div>
  </div>
</template>

<script>
import Trends from "@/components/Trends.vue";
import PostItem from "@/components/PostItem.vue";
import LoaderIcon from "@/components/icons/LoaderIcon.vue";
import WarningIcon from "@/components/icons/WarningIcon.vue";
import PageFeedback from "@/components/PageFeedback.vue";
import CreatePostForm from "@/components/forms/CreatePostForm.vue";
import UserProfileCard from "@/components/UserProfileCard.vue";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";

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
  name: "UserProfileView",
  components: {
    PeopleYouMayKnow,
    Trends,
    PostItem,
    LoaderIcon,
    WarningIcon,
    PageFeedback,
    CreatePostForm,
    UserProfileCard,
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
};
</script>