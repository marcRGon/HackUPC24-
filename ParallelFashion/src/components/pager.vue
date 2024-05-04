<script setup>

import { defineProps, defineEmits } from 'vue'

const emit = defineEmits()
const props = defineProps(['currentPage', 'totalPages'])

</script>

<template>

  <!-- Pager with text 1/N and buttons for moving left and right  -->
  <div class="pager">
	<button @click="emit('previous')" :disabled="currentPage === 1">Previous</button>
	<span>{{currentPage}} / {{totalPages}}</span>
	<button @click="emit('next')" :disabled="currentPage === totalPages">Next</button>
</div>

</template>

<style scoped>
.pager {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

</style>
