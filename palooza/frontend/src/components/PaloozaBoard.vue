<script setup lang="ts">
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import PaloozaColumn from './PaloozaColumn.vue'

const emit = defineEmits(['updateStatus'])

enum Status {
  PLANNED = "PLANNED",
  IN_PROGRESS = "IN_PROGRESS",
  ISSUES = "ISSUES",
  COMPLETE = "COMPLETE"
}
const statuses = Object.keys(Status)


const props = defineProps(['nodes'])

const moveCard = (nodeId, newStatus) => {
  const card = props.nodes.find((node) => node.id === nodeId)
  if (card) {
    card.status = newStatus
    emit('updateStatus', {nodeId: nodeId, status: newStatus})

  }
}
</script>

<template>
  <div class="palooza-board flex flex-row justify-around p-5 bg-gray-100 min-h-screen min-w-full">
    <PaloozaColumn
      v-for="status in statuses"
      :key="status"
      :status="status"
      :cards="nodes.filter((node) => node.status === status)"
      @moveCard="moveCard"
    ></PaloozaColumn>
  </div>
</template>
