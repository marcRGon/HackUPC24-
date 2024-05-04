<script setup>
import { computed, defineProps, ref, defineEmits } from 'vue'
import GetSimilarProductButton from './getSimilarProductButton.vue'

const props = defineProps(['product'])
const emit = defineEmits()
const images = computed(() => {
  if (!props.product.IMAGE_VERSION_3) {
    return [props.product.IMAGE_VERSION_1, props.product.IMAGE_VERSION_2]
  }
  return [props.product.IMAGE_VERSION_1, props.product.IMAGE_VERSION_2, props.product.IMAGE_VERSION_3]
})
let versionIndex = ref(0)

function incrementVersionIndex(increment) {
  versionIndex.value = (versionIndex.value + increment) % images.value.length;
  if (versionIndex.value < 0) {
    versionIndex.value += images.value.length;
  }
}

</script>

<template>

  <div class="arrowContainer">
      <button class="arrow-button" @click="incrementVersionIndex(-1)" draggable="false" >
        <img src="../assets/left-arrow.png" alt="Previous" />
      </button>
      <img class="bigImage" :src="images[versionIndex]" alt="product image" draggable="false" />
      <button class="arrow-button" @click="incrementVersionIndex(1)" >
        <img src="../assets/right-arrow.png" alt="Next" draggable="false" />
      </button>
    </div>

    <br />
    
    <div class="modalButtonContainer">
      <button class="modalButton" @click="emit('closeModal')">Close</button>
      <GetSimilarProductButton :currentSelectedProductId="product.id" :version="versionIndex" />
    </div>

</template>

<style scoped>
.bigImage {
  width: 200px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.arrowContainer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.arrow-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  img {
    width: 50px;
  }
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
