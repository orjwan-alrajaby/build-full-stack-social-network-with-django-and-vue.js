<script setup>
import { useToastStore } from '@/stores/toast'

const store = useToastStore()
</script>

<template>
    <div
        v-if="store.isVisible"
        class="fixed px-6 py-6 transition duration-500 ease-in-out delay-500 shadow-xl top-full right-8 rounded-xl"
        :class="store.classes"
    >
        {{ store.message }}
    </div>
</template>