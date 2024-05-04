<script setup>
import SmallImage from './smallimage.vue';
import { defineEmits, defineProps, ref } from 'vue'

const props = defineProps(['products'])
const emit = defineEmits()
const NUM_COLUMNS = 5

const numRows = ref(Math.ceil(props.products.length / NUM_COLUMNS))

</script>

<template>

  <div class="image-grid">
	<div class="image-grid-row" v-for="rowIndex in numRows">
	  <div class="image-grid-column" v-for="columnIndex in NUM_COLUMNS">
		<template v-if="props.products[(rowIndex - 1) * NUM_COLUMNS + columnIndex - 1]">
		  <SmallImage :product="props.products[(rowIndex - 1) * NUM_COLUMNS + columnIndex - 1]" @click-image="emit('click-image', $event)" />
		</template>
	</div>
  </div>
</div>


</template>

<style scoped>
.image-grid {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.image-grid-row {
  display: flex;
  gap: 1rem;
}


.image-grid-column {
  flex: 1;
}

</style>
