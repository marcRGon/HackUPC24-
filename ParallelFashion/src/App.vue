<script setup>
import products from './assets/images.json'
import ImageGrid from './components/imageGrid.vue';
import Pager from './components/pager.vue';

import { ref } from 'vue'

const PRODUCTS_PER_PAGE = 10
const totalPages = Math.ceil(products.products.length / PRODUCTS_PER_PAGE)
const currentPage = ref(1)
const theProducts = ref(products.products.slice(0, PRODUCTS_PER_PAGE))

function updatePage(page) {
  currentPage.value = page
  theProducts.value = products.products.slice((currentPage.value - 1) * PRODUCTS_PER_PAGE, currentPage.value * PRODUCTS_PER_PAGE)
}
function nextPage() {
  if (currentPage.value < totalPages) {
    updatePage(currentPage.value + 1)
  }
}
function previousPage() {
  if (currentPage.value > 1) {
    updatePage(currentPage.value - 1)
  }
}
</script>
<template>
  <div>
    <h1>Parallel Fashion</h1>
    <ImageGrid :products="theProducts" />
    <br />
    <Pager :currentPage="currentPage" :totalPages="totalPages" @next="nextPage" @previous="previousPage" />
  </div>
</template>

<style scoped>

</style>
