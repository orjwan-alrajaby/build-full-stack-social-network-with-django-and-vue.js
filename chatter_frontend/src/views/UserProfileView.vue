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
          postsStore.user.posts.length > 0 &&
          !isError
        "
      >
        <PostItem
          v-for="post in postsStore.user.posts"
          :key="post.id"
          :post="post"
        />
      </template>
      <PageFeedback
        title="Feed is loading..."
        v-else-if="
          isLoading &&
          !isError
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
          !isLoading &&
          isError
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

import useGetUserPosts from "@/composables/posts/useGetUserPosts";

export default {
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
  setup() {
    const postsStore = usePostsStore();
    const userStore = useUserStore();
    const {
      getUserPosts,
      data,
      isLoading,
      isError,
      error
    } = useGetUserPosts();

    return {
      postsStore,
      userStore,

      // 
      getUserPosts,
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
  methods: {
    getPosts() {
      this.getUserPosts(this.$route.params.id).then(res => {
        if (res.status === "error") {
          return;
        }

        this.postsStore.setUserPosts(this.data.author, this.data.posts);
      })
    }
  },
  beforeMount() {
    if (!this.$route.params.id) {
      this.$router.push({ name: "feed" });
    } else if (
      this.userStore.user.isAuthenticated &&
      this.userStore.user.accessToken &&
      this.$route.params.id
    ) {
      this.getPosts();
    }
  },
  watch: {
    $route(to, from) {
      if (
        this.userStore.user.isAuthenticated &&
        from.name === to.name &&
        from.params.id !== to.params.id
      ) {
        this.getPosts();
      }
    },
  },
};
</script>