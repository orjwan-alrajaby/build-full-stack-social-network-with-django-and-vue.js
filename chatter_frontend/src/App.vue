<template>
  <div class="relative h-screen bg-slate-950">
    <NavigationBar />
    <main class="min-h-full px-4 py-6 bg-slate-900 md:p-10 sm:p-8">
      <router-view />
    </main>
  </div>
</template>

<script>
import NavigationBar from './components/layout/NavigationBar.vue';

export default {
  name: 'AppView',
  components: {
    NavigationBar
  },
}
</script>



