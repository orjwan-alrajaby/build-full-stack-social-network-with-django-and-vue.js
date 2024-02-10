<template>
  <div class="w-full max-w-5xl mx-auto">
    <template v-if="isLoading">
      <div class="flex flex-col items-center justify-center h-72 text-slate-200">
         <svg xmlns="http://www.w3.org/2000/svg" width="5rem" height="5rem" viewBox="0 0 24 24">
          	<path fill="currentColor" d="M12,1A11,11,0,1,0,23,12,11,11,0,0,0,12,1Zm0,19a8,8,0,1,1,8-8A8,8,0,0,1,12,20Z" opacity="0.5" />
          	<path fill="currentColor" d="M12,4a8,8,0,0,1,7.89,6.7A1.53,1.53,0,0,0,21.38,12h0a1.5,1.5,0,0,0,1.48-1.75,11,11,0,0,0-21.72,0A1.5,1.5,0,0,0,2.62,12h0a1.53,1.53,0,0,0,1.49-1.3A8,8,0,0,1,12,4Z">
          		<animateTransform attributeName="transform" dur="0.75s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12" />
          	</path>
          </svg>
          <span class="mt-4 text-lg">Post is loading...</span>
      </div>
    </template>
    <template v-else-if="post">
      <PostItem :post="post"/>
    </template>
  </div>
</template>
<script>
import PostItem from '@/components/PostItem.vue';
import useGetPostDetails from "@/composition-functions/useGetPostDetails.js"

export default {
  setup() { 
    const { getPost, data, isLoading } = useGetPostDetails();
    return {
      getPost,
      data,
      isLoading
    }
  },
  components: {
    PostItem
  },
  data() {
    return {
      post: null
    }
  },
  mounted() {
    this.getPost(this.$route.params.id).then(res => {
      if (res.status === "success" && res.code === 200) {
        console.log("this.data", this.data)
        this.post = this.data;
        } else {
          this.toast.error(`Failed to fetch and display post.`, {
            toastClassName: "!bg-red-700 !text-slate-200",
          });
        }
    })
  },
}
</script>