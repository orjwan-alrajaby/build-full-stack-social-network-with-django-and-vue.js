<template>
  <div
    class="border rounded-lg bg-slate-950 border-lime-300"
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
          <PictureIcon width="1.5rem" height="1.5rem" classes="text-lime-300" />
        </button>

        <button
          class="w-16 h-10 mx-2 font-medium rounded-lg bg-lime-300 disabled:bg-lime-900 disabled:cursor-not-allowed"
          :disabled="!body || postsStore.posts.newPost.isLoading"
          @click="submitForm"
        >
          <LoaderIcon width="1.5rem" height="1.5rem" classes="text-slate-950" v-if="postsStore.posts.newPost.isLoading" />
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
</template>

<script>
import SendIcon from "@/components/icons/SendIcon.vue";
import LoaderIcon from "@/components/icons/LoaderIcon.vue";
import PictureIcon from "@/components/icons/PictureIcon.vue";

import { usePostsStore } from "@/stores/posts";
import { useUserStore } from "@/stores/user";
import { useToast } from "vue-toastification";

export default {
  name: "CreatePostForm",
  components: {
    SendIcon,
    LoaderIcon,
    PictureIcon,
  },
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
  data() {
    return {
      body: "",
    };
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
  },
};
</script>