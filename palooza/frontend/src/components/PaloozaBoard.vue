<script setup>
import { ref } from 'vue'
import PaloozaColumn from './PaloozaColumn.vue'
const cards = ref([
  { id: 1, title: 'Task 1', status: 'New' },
  // Add more cards with various statuses
])
const columnStatuses = ['New', 'To Do', 'In Progress', 'Done']
const moveCard = (cardId, newStatus) => {
  const card = cards.value.find((card) => card.id === cardId)
  if (card) {
    card.status = newStatus
  }
}
</script>

<template>
  <div class="palooza-board flex flex-row justify-around p-5 bg-gray-100 min-h-screen min-w-full">
    <PaloozaColumn
      v-for="status in columnStatuses"
      :key="status"
      :status="status"
      :cards="cards.filter((card) => card.status === status)"
      @moveCard="moveCard"
    ></PaloozaColumn>
  </div>
</template>
