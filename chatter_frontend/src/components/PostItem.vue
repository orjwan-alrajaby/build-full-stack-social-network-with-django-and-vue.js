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

        <div class="flex justify-between my-6">
          <div class="flex space-x-6">
              <button type="button" @click="likePost(post.id)" class="flex items-center space-x-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                  class="w-6 h-6 text-lime-300"
                  v-if="post.is_liked"
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
                <span class="text-xs text-slate-400">
                  {{ post.likes_count }} likes
                </span>
              </button>

              <button type="button" @click="toggleComments()" class="flex items-center space-x-2">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                  class="w-6 h-6 text-lime-300"
                  v-if="post.comments_count > 0 && post.has_commented"
                >
                  <path
                    fill-rule="evenodd"
                    d="M4.848 2.771A49.144 49.144 0 0 1 12 2.25c2.43 0 4.817.178 7.152.52 1.978.292 3.348 2.024 3.348 3.97v6.02c0 1.946-1.37 3.678-3.348 3.97-1.94.284-3.916.455-5.922.505a.39.39 0 0 0-.266.112L8.78 21.53A.75.75 0 0 1 7.5 21v-3.955a48.842 48.842 0 0 1-2.652-.316c-1.978-.29-3.348-2.024-3.348-3.97V6.741c0-1.946 1.37-3.68 3.348-3.97Z"
                    clip-rule="evenodd"
                  />
                </svg>

                <svg
                  v-else
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M2.25 12.76c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.076-4.076a1.526 1.526 0 0 1 1.037-.443 48.282 48.282 0 0 0 5.68-.494c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z"
                  />
                </svg>
                <span class="text-xs text-slate-400">{{ post.comments_count }} comments</span>
              </button>
          </div>

          <div>
          <template v-if="userStore.user.id === post.created_by.id">
            <button id="delete-comment-btn" @click="removePost(post.id)">
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
      </div>
      <Comments v-if="renderComments" v-show="showComments" :postId="post.id" />
    </div>
  </div>
</template>

<script>
import useLikePost from "@/composition-functions/useLikePost";
import useDeletePost from "@/composition-functions/useDeletePost.js"
import { useToast } from "vue-toastification";
import Comments from "@/components/Comments.vue";
import { useUserStore } from "@/stores/user";

export default {
  components: {
    Comments,
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
      deletePost
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
      this.deletePost(id).then(res => {
        if (res.status === "success" && res.code === 204) {
          this.toast.success(`Post deleted successfully!`, {
            toastClassName: "!bg-emerald-700 !text-slate-200",
          });
        } else {
          this.toast.error(`Failed to delete post.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
      })
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