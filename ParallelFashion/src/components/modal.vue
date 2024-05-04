<script setup>
import { defineEmits } from 'vue'

const emit = defineEmits()

</script>

<template>
    <div className="modal__wrapper" @click="emit('close')">
        <div className="modal" @click.stop>
            <slot/>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.modal{
  border-radius: 10px;
  background-color: black;
  padding: 50px 50px;
  z-index: 1200;
 &__wrapper{
  background-color: rgba(0,0,0,0.4);
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  position: absolute;
  top: o;
}
}

</style>
