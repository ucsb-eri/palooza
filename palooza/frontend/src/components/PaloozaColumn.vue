<script setup>
import { defineProps, defineEmits } from 'vue'
import PaloozaCard from './PaloozaCard.vue'
const props = defineProps({
  status: String,
  cards: Array,
})
const emit = defineEmits(['moveCard'])
const drop = (event) => {
  const cardId = event.dataTransfer.getData('text/plain')
  emit('moveCard', parseInt(cardId, 10), props.status)
}
</script>

<template>
  <div
    class="palooza-column flex-1 bg-white shadow rounded p-4 flex-1 mx-2"
    @dragover.prevent
    @drop="drop($event)"
  >
    <h2 class="font-bold mb-2">{{ status }}</h2>
    <PaloozaCard v-for="card in cards" :key="card.id" :card="card"></PaloozaCard>
  </div>
</template>
