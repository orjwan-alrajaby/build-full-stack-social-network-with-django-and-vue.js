<template>
  <div class="flex flex-col items-center justify-center p-4 font-medium text-center h-72 text-slate-400" :class="{'!text-red-700': isError}">
    <slot/>
    <span class="mt-4 text-2xl">{{ title }}</span>
    <span class="mt-2 text-lg">{{ subtitle }}</span>
  </div>
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      default: null
    },
    title: {
      type: String,
      default: "Enter your title here"
    },
    subtitle: {
      type: String,
      default: ""
    },
    isError: {
      type: Boolean,
      default: false
    }
  }
}
</script>
