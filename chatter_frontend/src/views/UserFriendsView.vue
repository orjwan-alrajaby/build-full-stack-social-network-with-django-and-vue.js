<template>
  <div class="grid grid-cols-5 gap-3 mx-auto xl:grid-cols-4 max-w-7xl">
    <div class="col-span-5 space-y-4 main-left md:col-span-3">
      <div class="h-full p-4 space-y-4 border rounded-lg bg-gray-950 border-lime-300">
        <h2 class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700">My Friends</h2>
        <div class="grid grid-cols-5 gap-3 xl:grid-cols-4">
          <div
            class="col-span-5 p-4 text-center bg-gray-900 rounded-lg xl:col-span-1 sm:col-span-2"
          >
              <img
                src="https://mighty.tools/mockmind-api/content/human/40.jpg"
                class="block w-full mx-auto mb-6 rounded-full max-w-40"
              />

              <p class="uppercase text-lime-300">
                <strong>
                  <router-link to="#">Orjwana banana</router-link>
                </strong>
              </p>

              <div class="flex justify-around mt-6 space-x-8">
                <p class="text-xs text-slate-400">182 friends</p>
                <p class="text-xs text-slate-400">120 posts</p>
              </div>
          </div>

          <div
            class="col-span-5 p-4 text-center bg-gray-900 rounded-lg xl:col-span-1 sm:col-span-2"
          >
              <img
                src="https://mighty.tools/mockmind-api/content/human/40.jpg"
                class="block w-full mx-auto mb-6 rounded-full max-w-40"
              />

              <p class="uppercase text-lime-300">
                <strong>
                  <router-link to="#">Orjwana banana</router-link>
                </strong>
              </p>

              <div class="flex justify-around mt-6 space-x-8">
                <p class="text-xs text-slate-400">182 friends</p>
                <p class="text-xs text-slate-400">120 posts</p>
              </div>
          </div>

          <div
            class="col-span-5 p-4 text-center bg-gray-900 rounded-lg xl:col-span-1 sm:col-span-2"
          >
              <img
                src="https://mighty.tools/mockmind-api/content/human/40.jpg"
                class="block w-full mx-auto mb-6 rounded-full max-w-40"
              />

              <p class="uppercase text-lime-300">
                <strong>
                  <router-link to="#">Orjwana banana</router-link>
                </strong>
              </p>

              <div class="flex justify-around mt-6 space-x-8">
                <p class="text-xs text-slate-400">182 friends</p>
                <p class="text-xs text-slate-400">120 posts</p>
              </div>
          </div>

          <div
            class="col-span-5 p-4 text-center bg-gray-900 rounded-lg xl:col-span-1 sm:col-span-2"
          >
              <img
                src="https://mighty.tools/mockmind-api/content/human/40.jpg"
                class="block w-full mx-auto mb-6 rounded-full max-w-40"
              />

              <p class="uppercase text-lime-300">
                <strong>
                  <router-link to="#">Orjwana banana</router-link>
                </strong>
              </p>

              <div class="flex justify-around mt-6 space-x-8">
                <p class="text-xs text-slate-400">182 friends</p>
                <p class="text-xs text-slate-400">120 posts</p>
              </div>
          </div>

          <div
            class="col-span-5 p-4 text-center bg-gray-900 rounded-lg xl:col-span-1 sm:col-span-2"
          >
              <img
                src="https://mighty.tools/mockmind-api/content/human/40.jpg"
                class="block w-full mx-auto mb-6 rounded-full max-w-40"
              />

              <p class="uppercase text-lime-300">
                <strong>
                  <router-link to="#">Orjwana banana</router-link>
                </strong>
              </p>

              <div class="flex justify-around mt-6 space-x-8">
                <p class="text-xs text-slate-400">182 friends</p>
                <p class="text-xs text-slate-400">120 posts</p>
              </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-span-5 space-y-4 main-right xl:col-span-1 md:col-span-2">
      <FriendRequests type="Incoming"/>
      <FriendRequests type="Outgoing"/>
      <PeopleYouMayKnow />
    </div>
  </div>
</template>

<script>
import FriendRequests from "../components/FriendRequests.vue";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";

import { useSearchStore } from "@/stores/search";
import { useUserStore } from "@/stores/user";
import { useToast } from "vue-toastification";

export default {
  name: "FriendsView",
  components: {
    FriendRequests,
    PeopleYouMayKnow,
  },
};
</script>