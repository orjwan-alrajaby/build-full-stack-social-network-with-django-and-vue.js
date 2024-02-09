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
          class="px-4 py-2 mx-2 font-medium rounded-lg bg-lime-300 text-slate-950 disabled:bg-lime-900 disabled:cursor-not-allowed"
          :disabled="!commentBody"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 mx-auto"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5"
            />
          </svg>
        </button>
      </div>
    </form>
    <template v-if="commentListIsLoading">
      <div class="flex flex-col items-center justify-center h-32 text-lime-300">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="2.5rem"
          height="2.5rem"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z"
            opacity="0.5"
          />
          <path
            fill="currentColor"
            d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z"
          >
            <animateTransform
              attributeName="transform"
              dur="0.75s"
              repeatCount="indefinite"
              type="rotate"
              values="0 12 12;360 12 12"
            />
          </path>
        </svg>
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
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="w-6 h-6 text-lime-300"
              v-if="comment.is_liked"
            >
              <path
                d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z"
              />
            </svg>

            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6 text-slate-200"
              v-else
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
              ></path>
            </svg>
            <span class="text-xs text-slate-400"
              >{{ comment.likes_count }} likes</span
            >
          </button>
          <template v-if="userStore.user.id === comment.created_by.id">
            <button id="delete-comment-btn" @click="deleteComment(comment.id)" class="mr-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-5 h-5 mx-auto text-red-700"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
                />
              </svg>
            </button>
          </template>
          <template v-else>
            <button id="options-btn">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6 text-slate-200"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
                ></path>
              </svg>
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
import useCreateCommentOnPost from "@/composition-functions/usePostComment.js";
import useGetPostComments from "@/composition-functions/useGetPostComments.js";
import useLikeComment from "@/composition-functions/useLikeComment.js";
import useDeleteComment from "@/composition-functions/useDeleteComment.js"
import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";

export default {
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
