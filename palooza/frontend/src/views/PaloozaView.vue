<script setup lang="ts">
import PaloozaBoard from '@/components/PaloozaBoard.vue'
import { useFetch } from '@vueuse/core'
import { ref } from 'vue'

const baseUrl = 'http://localhost:1234/api'
const url = ref(`${baseUrl}/paloozas`)

// const toggleRefetch = useToggle(refetch)

let nodes = ref([])

const { data, error, abort, statusCode, isFetching, isFinished, canAbort, execute } =
  await useFetch(url, { refetch: true }).get().json()
nodes = ref(data.value.nodes)

const updateStatus = async function ({ nodeId, status }) {
  const res = await useFetch(`${baseUrl}/nodes/${nodeId}`).put({ status }).json()
}
</script>

<template>
  <h1>{{ data.description }}</h1>
  <PaloozaBoard :nodes="nodes" @updateStatus="updateStatus" />
</template>
