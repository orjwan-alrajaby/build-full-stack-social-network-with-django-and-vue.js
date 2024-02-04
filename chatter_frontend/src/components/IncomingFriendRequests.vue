<template>
  <div class="p-4 border rounded-lg bg-gray-950 border-lime-300">
    <h3 class="pb-3 mb-4 text-xl border-b text-slate-400 border-slate-700">
      Incoming Friend Requests ({{ list.length }})
    </h3>
    <div class="grid grid-cols-2 gap-3">
      
      <div
        class="col-span-2 p-4 space-y-4 text-center bg-gray-900 rounded-lg md:col-span-2 sm:col-span-1"
        v-for="item in list"
        :key="item.id"
      >
        <img
          src="https://mighty.tools/mockmind-api/content/human/40.jpg"
          class="block w-full mx-auto mb-6 rounded-full max-w-40"
        />
        <p class="text-sm uppercase text-slate-200">
          <strong>
            <router-link
              :to="{ name: 'user-profile', params: { id: item.created_by.id } }"
              >{{ item.created_by.name }}</router-link
            >
          </strong>
        </p>
        <div class="flex justify-around mt-6 space-x-8">
          <p class="text-xs text-slate-400">182 friends</p>
          <p class="text-xs text-slate-400">120 posts</p>
        </div>
        <div class="space-x-3">
          <button
            href="#"
            class="w-10 h-10 text-xs font-medium border rounded-full border-lime-300 text-lime-300"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="block w-5 h-5 mx-auto"
            >
              <path
                fill-rule="evenodd"
                d="M16.5 4.478v.227a48.816 48.816 0 0 1 3.878.512.75.75 0 1 1-.256 1.478l-.209-.035-1.005 13.07a3 3 0 0 1-2.991 2.77H8.084a3 3 0 0 1-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 0 1-.256-1.478A48.567 48.567 0 0 1 7.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 0 1 3.369 0c1.603.051 2.815 1.387 2.815 2.951Zm-6.136-1.452a51.196 51.196 0 0 1 3.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 0 0-6 0v-.113c0-.794.609-1.428 1.364-1.452Zm-.355 5.945a.75.75 0 1 0-1.5.058l.347 9a.75.75 0 1 0 1.499-.058l-.346-9Zm5.48.058a.75.75 0 1 0-1.498-.058l-.347 9a.75.75 0 0 0 1.5.058l.345-9Z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
          <button
            class="w-10 h-10 text-xs font-medium rounded-full bg-lime-300 text-slate-900"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="block w-5 h-5 mx-auto"
            >
              <path
                d="M5.25 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM2.25 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM18.75 7.5a.75.75 0 0 0-1.5 0v2.25H15a.75.75 0 0 0 0 1.5h2.25v2.25a.75.75 0 0 0 1.5 0v-2.25H21a.75.75 0 0 0 0-1.5h-2.25V7.5Z"
              />
            </svg>
          </button>
        </div>
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
