<template>
  <div class="py-4 pl-6 space-y-4 border-t border-slate-700">
    <form
      class="bg-gray-900 border-l-4 rounded-r-lg border-lime-300"
      @submit.prevent="submitForm"
    >
      <div class="flex p-4 space-x-4">
        <img
          src="https://mighty.tools/mockmind-api/content/human/49.jpg"
          class="w-full rounded-full max-w-10"
        />
        <input
          type="search"
          class="w-full p-2 rounded-lg bg-slate-200 text-slate-950"
          placeholder="What do you think?"
          v-model="commentBody"
        />

        <button
          class="px-4 py-2 mx-2 font-medium rounded-lg bg-lime-300 disabled:bg-lime-900 disabled:cursor-not-allowed"
          :disabled="!commentBody"
        >
          <SendIcon width="1.5rem" height="1.5rem" classes="text-slate-950" />
        </button>
      </div>
    </form>
    <template v-if="commentListIsLoading">
      <div class="flex flex-col items-center justify-center h-32 text-lime-300">
        <LoaderIcon width="2.5rem" height="2.5rem" classes="text-lime-300" />
        <span class="mt-4 text-xs">Post's comments are loading...</span>
      </div>
    </template>
    <template v-else-if="commentsList && commentsList.length > 0">
      <div
        class="p-4 pr-2 space-y-3 bg-gray-900 border-l-4 rounded-r-lg border-lime-300"
        v-for="comment in commentsList"
        :key="comment.id"
      >
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-4">
            <img
              src="https://mighty.tools/mockmind-api/content/human/49.jpg"
              class="w-full rounded-full max-w-10"
            />
            <p class="text-sm text-slate-200">
              <strong>{{ comment.created_by.name }}</strong>
            </p>
          </div>
          <p class="pr-2 text-xs text-slate-400">
            {{ comment.created_at_formatted }} ago
          </p>
        </div>
        <div>
          <p class="text-sm text-slate-200">{{ comment.body }}</p>
        </div>
        <div class="flex items-center justify-between w-full">
          <button
            type="button"
            @click="likeComment(comment)"
            class="flex items-center space-x-2"
          >
            <MessageBubbleIcon v-if="comment.is_liked" width="1.5rem" height="1.5rem" :isFilled="true" />
            <MessageBubbleIcon width="1.5rem" height="1.5rem" v-else />
            <span class="text-xs text-slate-400"
              >{{ comment.likes_count }} likes</span
            >
          </button>
          <template v-if="userStore.user.id === comment.created_by.id">
            <button id="delete-comment-btn" @click="deleteComment(comment.id)" class="mr-2">
              <TrashIcon width="1.5rem" height="1.5rem" classes="text-red-700"/>
            </button>
          </template>
          <template v-else>
            <button id="options-btn">
              <EyeIcon width="1.5rem" height="1.5rem" classes="text-slate-200"/>
            </button>
            <ul class="hidden">
              <li><button>show</button></li>
            </ul>
          </template>
        </div>
      </div>
    </template>
  </div>
</template>
<script>
import { SendIcon, LoaderIcon, MessageBubbleIcon } from '@/components/icons';

import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";
import useCreateCommentOnPost from "@/composables/posts/useCreateCommentOnPost.js";
import useGetPostComments from "@/composables/posts/useGetPostComments.js";
import useLikeComment from "@/composables/posts/useLikeComment.js";
import useDeleteComment from "@/composables/posts/useDeleteComment.js"

export default {
  components: { 
    SendIcon,
    LoaderIcon,
    MessageBubbleIcon
   },
  props: {
    postId: String,
  },
  setup() {
    const userStore = useUserStore();
    const { data: newComment, createCommentOnPost } = useCreateCommentOnPost();
    const {
      data: commentsList,
      isLoading: commentListIsLoading,
      getPostCommentsList,
    } = useGetPostComments();
    const { createLikeForComment } = useLikeComment();
    const { deleteCommentOnPost } = useDeleteComment();
    
    const toast = useToast();
    return {
      createCommentOnPost,
      newComment,
      getPostCommentsList,
      commentsList,
      commentListIsLoading,
      toast,
      createLikeForComment,
      deleteCommentOnPost,
      userStore,
    };
  },
  data() {
    return {
      commentBody: "",
    };
  },
  mounted() {
    this.getCommentsList();
  },
  methods: {
    getCommentsList() {
      this.getPostCommentsList(this.postId).then((res) => {
        if (res.status === "success") {
          return;
        } else {
          this.toast.error(`Failed to fetch post's comments.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      });
    },
    likeComment(comment) {
      this.createLikeForComment(this.postId, comment.id).then((res) => {
        if (res.status === "success") {
          if (res.code === 201) {
            comment.is_liked = true;
            comment.likes_count = comment.likes_count + 1;
          } else {
            comment.is_liked = false;
            comment.likes_count = comment.likes_count - 1;
          }
          return;
        } else {
          this.toast.error(`Failed to like the comment.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      });
    },
    submitForm() {
      this.createCommentOnPost(this.postId, this.commentBody).then((res) => {
        if (res.status === "success" && res.code === 201) {
          this.toast.success(`Comment posted successfully!`, {
            toastClassName: "!bg-emerald-700 !text-slate-200",
          });
          this.commentsList = [this.newComment, ...this.commentsList];
          this.commentBody = "";
        } else {
          this.toast.error(`Failed to comment on the post.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      });
    },
    deleteComment(commentId) {
      this.deleteCommentOnPost(this.postId, commentId).then(res => {
        if (res.status === "success" && res.code === 204) {
          this.commentsList = this.commentsList.filter(comment => comment.id !== commentId);
          this.toast.success(`Comment deleted successfully!`, {
            toastClassName: "!bg-emerald-700 !text-slate-200",
          });
        } else {
          this.toast.error(`Failed to delete comment.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      })
    },
  },
};
</script>