<script setup>

import { defineProps, defineEmits } from 'vue'

const emit = defineEmits()
const props = defineProps(['currentPage', 'totalPages'])

</script>

<template>
  <div class="pagerContainer">
    <div class="pager">
      <button class="arrow-button" @click="emit('previous')" :disabled="currentPage === 1">
        <img src="../assets/left-arrow.png" alt="Previous" draggable="false" />
      </button>
      <span class="pager-text">{{ currentPage }} / {{ totalPages }}</span>
      <button class="arrow-button" @click="emit('next')" :disabled="currentPage === totalPages">
        <img src="../assets/right-arrow.png" alt="Next" draggable="false" />
      </button>
    </div>
  </div>
</template>


<style scoped>
.pagerContainer {
  display: flex;
  justify-content: center;
  align-items: center;
}
.pager {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.pager-text {
  font-size: 1.5rem;
}

.arrow-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  img {
    width: 50px;
  }
  &:disabled {
    cursor: not-allowed;
    img {
      opacity: 0.2;
    }
  }
}

</style>
