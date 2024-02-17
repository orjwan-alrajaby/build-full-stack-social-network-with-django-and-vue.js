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
        d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"
      />
    </svg>
  </span>
</template>

<script>
export default {
  props: {
    classes: {
      type: String,
      default: "text-slate-400",
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