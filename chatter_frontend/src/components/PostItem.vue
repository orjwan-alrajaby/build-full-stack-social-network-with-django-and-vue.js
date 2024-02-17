<template>
  <div>
    <div class="p-4 border rounded-lg bg-gray-950 border-lime-300">
      <div>
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center space-x-4">
            <img
              src="https://mighty.tools/mockmind-api/content/human/37.jpg"
              class="w-[40px] rounded-full"
            />

            <p class="text-slate-200">
              <strong>
                <router-link
                  :to="{
                    name: 'user-profile',
                    params: { id: post.created_by.id },
                  }"
                >
                  {{ post.created_by.name }}
                </router-link>
              </strong>
            </p>
          </div>

          <p class="text-sm text-slate-400">
            {{ post.created_at_formatted }} ago
          </p>
        </div>

        <p class="text-slate-200">
          {{ post.body }}
        </p>

        <div class="flex items-center my-6 space-x-6">
          <button
            type="button"
            @click="likePost(post.id)"
            class="flex items-center space-x-2"
          >
            <HeartIcon
              v-if="post.is_liked"
              :isFilled="true"
              width="1.5rem"
              height="1.5rem"
              classes="text-lime-300"
            />
            <HeartIcon
              v-else
              width="1.5rem"
              height="1.5rem"
              classes="text-slate-200"
            />
            <span class="text-xs text-slate-400">
              {{ post.likes_count }} likes
            </span>
          </button>

          <button
            type="button"
            @click="toggleComments()"
            class="flex items-center space-x-2"
          >
            <MessageBubbleIcon
              v-if="post.comments_count > 0 && post.has_commented"
              width="1.5rem"
              height="1.5rem"
              classes="text-lime-300"
              :isFilled="true"
             />
            <MessageBubbleIcon
              v-else
              width="1.5rem"
              height="1.5rem"
              classes="text-slate-200"
             />
            <span class="text-xs text-slate-400"
              >{{ post.comments_count }} comments</span
            >
          </button>
          <router-link
            id="show-btn"
            class="flex items-center space-x-2"
            :to="{ name: 'post-details', params: { id: post.id } }"
          >
            <EyeIcon width="1.5rem" height="1.5rem" classes="text-slate-200"/>
            <span class="text-xs text-slate-400">show</span>
          </router-link>
          <button
            id="delete-comment-btn"
            v-if="userStore.user.id === post.created_by.id"
            @click="removePost(post.id)"
            class="flex items-center space-x-2"
          >
            <TrashIcon width="1.5rem" height="1.5rem" classes="text-red-700"/>
            <span class="text-xs text-red-700">delete</span>
          </button>
        </div>
      </div>
      <Comments v-if="renderComments" v-show="showComments" :postId="post.id" />
    </div>
  </div>
</template>

<script>
import Comments from "@/components/Comments.vue";
import { HeartIcon, EyeIcon, EmptyMessageBubble, TrashIcon, MessageBubbleIcon } from "./icons";

import useLikePost from "@/composition-functions/useLikePost";
import useDeletePost from "@/composition-functions/useDeletePost.js";
import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";

export default {
  components: {
    Comments,
    HeartIcon,
    EmptyMessageBubble,
    EyeIcon,
    TrashIcon,
    MessageBubbleIcon
  },
  setup() {
    const { data, isLoading, error, isError, createLikeForPost } =
      useLikePost();
    const { deletePost } = useDeletePost();

    const toast = useToast();
    const userStore = useUserStore();

    return {
      data,
      error,
      isError,
      isLoading,
      createLikeForPost,
      toast,
      userStore,
      deletePost,
    };
  },
  props: {
    post: Object,
  },
  data() {
    return {
      showComments: false,
      renderComments: false,
    };
  },
  mounted() {
    if (this.$route.name === "post-details") {
      this.renderComments = true;
      this.showComments = true;
    }
  },
  methods: {
    likePost(postId) {
      this.createLikeForPost(postId).then((res) => {
        if (res.status === "success") {
          if (res.code === 204) {
            this.post.is_liked = false;
            this.post.likes_count--;
          } else {
            this.post.is_liked = true;
            this.post.likes_count++;
          }
        } else {
          this.toast.error(`Failed to like the post.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      });
    },
    removePost(id) {
      this.deletePost(id).then((res) => {
        if (res.status === "success" && res.code === 204) {
          this.toast.success(`Post deleted successfully!`, {
            toastClassName: "!bg-emerald-700 !text-slate-200",
          });
        } else {
          this.toast.error(`Failed to delete post.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      });
    },
    renderPostComments() {
      this.renderComments = true;
    },
    toggleComments() {
      this.renderPostComments();
      this.showComments = !this.showComments;
    },
  },
};
</script>

<style>
</style>