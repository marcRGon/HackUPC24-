<script setup>

import { defineProps } from 'vue'

const props = defineProps(['currentSelectedProductId', 'version'])

const ENDPOINT = 'http://localhost:5000/similarProducts'

async function getSimilarProducts() {
	const id = props.currentSelectedProductId
  const version = props.version
	const url = `${ENDPOINT}/${id}/${version}`
	console.log(url)
  const response = await fetch(url, {
	method: 'GET',
	headers: {
	  'Content-Type': 'application/json'
	}
  })
  const data = await response.json()
	console.log(data)
  const ids = data.products
  const query = `?ids=${ids.join(',')}`
  window.location.href = `/related${query}`
}

</script>

<template>
  <button class="modalButton highlight" @click="getSimilarProducts">
	Get similar products
</button>
</template>

<style scoped>
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
