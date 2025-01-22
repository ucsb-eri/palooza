<script setup lang="ts">
import PaloozaBoard from '@/components/PaloozaBoard.vue'
import { useFetch } from '@vueuse/core'
import { ref } from 'vue'
import { useCookies } from '@vueuse/integrations/useCookies'
// import { useJwt } from '@vueuse/integrations/useJwt'
import { networkClient } from '@/networkClient'

const baseUrl = ref(`${import.meta.env.VITE_API_URL}`)
const url = ref(`${baseUrl.value}/paloozas`)
const cookies = useCookies()

let nodes = ref([])
let description = ref("")

const { data, error } = await networkClient('/paloozas', {refetch: true}).get().json()
if (data.value) {
  nodes = ref(data.value.nodes)
  description = ref(data.value.description)
}

const updateStatus = async function ({ nodeId, status }) {
  await useFetch(`${baseUrl.value}/nodes/${nodeId}`, { refetch: true }).put({ status }).json()
}
</script>

<template>
  <h1>{{ description }}</h1>
  <PaloozaBoard :nodes="nodes" @updateStatus="updateStatus" />
</template>
