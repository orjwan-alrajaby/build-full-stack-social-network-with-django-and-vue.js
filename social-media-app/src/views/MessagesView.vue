<template>
  <div class="max-w-7xl mx-auto grid grid-cols-3 gap-4">
    <div class="main-left lg:col-span-1 col-span-3 order-last lg:order-none">
      <div class="p-4 bg-gray-950 border border-lime-300 rounded-lg">
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />

              <p class="text-xs"><strong>Code With Stein</strong></p>
            </div>

            <span class="text-xs text-slate-500">18 minutes ago</span>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />

              <p class="text-xs"><strong>Code With Stein</strong></p>
            </div>

            <span class="text-xs text-slate-500">18 minutes ago</span>
          </div>

          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />

              <p class="text-xs"><strong>Code With Stein</strong></p>
            </div>

            <span class="text-xs text-slate-500">18 minutes ago</span>
          </div>
        </div>
      </div>
    </div>

    <div class="main-center lg:col-span-2 col-span-3 space-y-4 order-first lg:order-none">
      <div class="bg-gray-950 border border-lime-300 rounded-lg">
        <div class="flex flex-col flex-grow p-4">
          <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
            <div>
              <div
                class="bg-lime-400 text-slate-900 p-3 rounded-l-lg rounded-br-lg"
              >
                <p class="text-sm">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod.
                </p>
              </div>
              <span class="text-xs text-lime-600 leading-none">2 min ago</span>
            </div>
            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />
            </div>
          </div>

          <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
            <div>
              <div
                class="bg-lime-400 text-slate-900 p-3 rounded-l-lg rounded-br-lg"
              >
                <p class="text-sm">Lorem ipsum dolor sit amet</p>
              </div>
              <span class="text-xs text-lime-600 leading-none">2 min ago</span>
            </div>
            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />
            </div>
          </div>

          <div class="flex w-full mt-2 space-x-3 max-w-md">
            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
              <img
                src="https://mighty.tools/mockmind-api/content/human/49.jpg"
                class="w-[40px] rounded-full"
              />
            </div>
            <div>
              <div class="bg-slate-600 text-slate-200 p-3 rounded-r-lg rounded-bl-lg">
                <p class="text-sm">
                  I'm the other person
                </p>
              </div>
              <span class="text-xs text-slate-500 leading-none">2 min ago</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-gray-950 border border-lime-300 rounded-lg">
        <div class="p-4">
          <textarea
            class="p-4 w-full bg-slate-200 rounded-lg text-slate-900"
            placeholder="What do you want to say?"
          ></textarea>
        </div>

        <div class="p-4 border-t border-slate-700 flex justify-between">
            <button
              href="#"
              class="py-2 px-4 bg-lime-300 text-slate-900 rounded-lg font-medium"
              >
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
</svg>

            </button>
        </div>
      </div>
    </div>
  </div>
</template>