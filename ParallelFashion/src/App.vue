<script setup>
import products from './assets/images.json'
import BigImage from './components/bigImage.vue';
import ImageGrid from './components/imageGrid.vue';
import Modal from './components/modal.vue';

import Pager from './components/pager.vue';

import { ref } from 'vue'

const PRODUCTS_PER_PAGE = 10
const totalPages = Math.ceil(products.products.length / PRODUCTS_PER_PAGE)
const currentPage = ref(1)
const currentSelectedProduct = ref(null)
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
  <div class="body-wrapper">
    <div>
      <h1>Parallel Fashion</h1>
      <ImageGrid :products="theProducts" @click-image="currentSelectedProduct = $event" />
      <br />
      <Pager :currentPage="currentPage" :totalPages="totalPages" @next="nextPage" @previous="previousPage" />
    </div>
    <Modal v-if="currentSelectedProduct !== null" @close="currentSelectedProduct = null">
      <BigImage :product="currentSelectedProduct" />
      <br />
      <div class="modalButtonContainer">
        <button class="modalButton" @click="currentSelectedProduct = null">Close</button>
        <button class="modalButton highlight">Get similar products</button>
      </div>
    </Modal>
  </div>
</template>

<style scoped>
.body-wrapper {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modalButtonContainer {
  display: flex;
  justify-content: center;
}
.modalButton {
  background-color: white;
  color: black;
  border: none;
  padding: 10px 20px;
  margin: 10px;
  cursor: pointer;
  &.highlight {
    background-color: rgb(233, 217, 76);
  }
}
</style>
