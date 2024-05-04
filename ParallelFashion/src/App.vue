<script setup>
import { ref, computed } from 'vue'
import MainPage from './MainPage.vue';
import RelatedPage from './RelatedPage.vue';

console.log("computed", window.location.href)
const currentPath = ref(window.location.href)

window.addEventListener('hashchange', () => {
  console.log("window hashchange")
  currentPath.value = window.location.href
})
const currentView = computed(() => {
  const [path, query] = currentPath.value.split('?')
  if (path.endsWith('/related')) {
    return {
      component: RelatedPage,
      query: query
    }
  }
  return {
    component: MainPage,
    query: query
  }
})
</script>

<template>
  <component :is="currentView.component" :query="currentView.query" />
</template>
