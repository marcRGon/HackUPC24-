<script setup>
import products from './assets/images.json'
import BigImage from './components/bigImage.vue';
import ImageGrid from './components/imageGrid.vue';
import Modal from './components/modal.vue';

import { ref, defineProps } from 'vue'

const props = defineProps(['query'])

const currentSelectedProduct = ref(null)

if (!props.query) {
  window.location.href = '/'
}
const [paramName, paramValue] = props.query.split('=')
const ids = paramValue.split(',').map(id => parseInt(id))
const theProducts = ref(products.products.filter(product => ids.includes(product.id)))
</script>
<template>
  <div class="body-wrapper">
    <div>
      <h1 style="text-align: center;">Similar products</h1>
      <br />
      <ImageGrid :products="theProducts" @click-image="currentSelectedProduct = $event" />
    </div>
    <Modal v-if="currentSelectedProduct !== null" @close="currentSelectedProduct = null">
      <BigImage :product="currentSelectedProduct" @closeModal="currentSelectedProduct = null"/>
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

</style>
