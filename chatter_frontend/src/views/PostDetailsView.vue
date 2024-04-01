<template>
  <div class="w-full max-w-5xl mx-auto">
    <template v-if="isLoading">
      <PageFeedback title="Post is loading...">
        <LoaderIcon />
      </PageFeedback>
    </template>
    <template v-else-if="post">
      <PostItem :post="post" />
    </template>
  </div>
</template>
<script>
import PostItem from "@/components/PostItem.vue";
import LoaderIcon from "@/components/icons/LoaderIcon.vue";
import PageFeedback from "@/components/PageFeedback.vue";

import useGetPostDetails from "@/composables/posts/useGetPostDetails.js";

export default {
  setup() {
    const { getPost, data, isLoading } = useGetPostDetails();
    return {
      getPost,
      data,
      isLoading,
    };
  },
  name: "PostDetailsView",
  components: {
    PostItem,
    LoaderIcon,
    PageFeedback,
  },
  data() {
    return {
      post: null,
    };
  },
  mounted() {
    this.getPost(this.$route.params.id).then((res) => {
      if (res.status === "success" && res.code === 200) {
        this.post = this.data;
      } else {
        this.toast.error(`Failed to fetch and display post.`, {
          toastClassName: "!bg-red-700 !text-slate-200",
        });
      }
    });
  },
};
</script>