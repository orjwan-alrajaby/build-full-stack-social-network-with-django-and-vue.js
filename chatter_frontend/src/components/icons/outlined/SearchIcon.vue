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
        d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
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