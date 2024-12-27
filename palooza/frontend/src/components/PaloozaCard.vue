<script setup>
import { defineProps } from 'vue'
const props = defineProps({
  card: Object,
})
const dragStart = (event, card) => {
  event.dataTransfer.setData('text/plain', card.id)
}
</script>

<template>
  <div
    class="palooza-card bg-gray-100 rounded shadow p-3 mb-2 cursor-pointer min-w-full"
    draggable="true"
    @dragstart="dragStart($event, card)"
  >
    {{ card.title }}
  </div>
</template>
