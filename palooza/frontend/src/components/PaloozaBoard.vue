<script setup>
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import PaloozaColumn from './PaloozaColumn.vue'

const url = ref('http://localhost:1234/')
const refetch = ref(false)

// const toggleRefetch = useToggle(refetch)

const { data, error, abort, statusCode, isFetching, isFinished, canAbort, execute } = useFetch(
  url,
  { refetch },
).get()

console.log(data)

// const text = stringify(reactive({
// isFinished,
// isFetching,
// canAbort,
// statusCode,
// //   error,
// //   data: computed(() => {
// //     try {
// //       return JSON.parse(data.value as string)
// //     }
// //     catch (e) {
// //       return null
// //     }
// //   }),
// }))

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
