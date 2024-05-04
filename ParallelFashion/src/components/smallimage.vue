<script setup>
import { defineProps, ref } from 'vue'

const props = defineProps(['product'])
const imgurl = ref(props.product.IMAGE_VERSION_1)

</script>

<template>

  <div >
	<img class="small-image" :src="props.product.IMAGE_VERSION_1" alt="product image" />
  </div>

</template>

<style scoped>
.small-image {
  width: 200px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
