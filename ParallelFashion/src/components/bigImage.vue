<script setup>
import { computed, defineProps, ref } from 'vue'

const props = defineProps(['product'])
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
      <button class="arrow-button" @click="incrementVersionIndex(-1)" >
        <img src="../assets/left-arrow.png" alt="Previous" draggable="false"  />
      </button>
      <img class="bigImage" :src="images[versionIndex]" alt="product image" draggable="false" />
      <button class="arrow-button" @click="incrementVersionIndex(1)" >
        <img src="../assets/right-arrow.png" alt="Next" draggable="false" />
      </button>
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
</style>
