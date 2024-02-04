<template>
  <div class="p-4 border rounded-lg bg-gray-950 border-lime-300">
    <h3 class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700">
      Outgoing Friend Requests ({{ list.length }})
    </h3>

      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <img
            src="https://mighty.tools/mockmind-api/content/human/49.jpg"
            class="rounded-full w-[40px]"
          />

          <p class="text-xs text-slate-200 text-ellipsis">
            <strong>
              <router-link :to="{name: 'user-profile', params: {id: '#'}}">
                Angelica Johnson
              </router-link>
            </strong>
          </p>
        </div>
        <div class="flex items-center space-x-2">
              <button class="h-10 p-2 text-xs font-medium border rounded-lg w-fit border-lime-300 text-lime-300">
              <!-- <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 mx-auto">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
              </svg> -->
              Cancel request
            </button>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  props: {
    list: [],
  },
  mounted() {
    console.log("Meow meow meow", this.list);
  },
};
</script>
