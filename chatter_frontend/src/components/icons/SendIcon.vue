<template>
  <span class="flex items-center justify-center">
    <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    stroke-width="1.5"
    stroke="currentColor"
    :width="width"
    :height="height"
    :class="classes"
  >
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5"
    />
  </svg>
  </span>
</template>
<script>
export default {
  props: {
    classes: {
      type: String,
      default: "text-slate-400"
    },
    width: {
      type: String,
      default: "5rem",
    },
    height: {
      type: String,
      default: "5rem",
    },
  },
};
</script>