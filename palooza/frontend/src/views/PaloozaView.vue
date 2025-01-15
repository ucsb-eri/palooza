<script setup lang="ts">
import PaloozaBoard from '@/components/PaloozaBoard.vue'
import { useFetch } from '@vueuse/core'
import { ref } from 'vue'
import { useCookies } from '@vueuse/integrations/useCookies'
// import { useJwt } from '@vueuse/integrations/useJwt'

const baseUrl = ref(`${import.meta.env.VITE_API_URL}`)
const url = ref(`${baseUrl.value}/paloozas`)
const cookies = useCookies()

let nodes = ref([])

const beforeFetch = async function ({ url, options, cancel }) {
  const token = cookies.get('jwt')

  if (!token) {
    cancel()
  }

  options.headers = {
    ...options.headers,
    Authorization: `Bearer ${token}`,
  }

  return {
    options,
  }
}

const { data, error, abort, statusCode, isFetching, isFinished, canAbort, execute } =
  await useFetch(url, {
    refetch: true,
    beforeFetch,
  })
    .get()
    .json()
nodes = ref(data.value.nodes)

const updateStatus = async function ({ nodeId, status }) {
  await useFetch(`${baseUrl.value}/nodes/${nodeId}`, { refetch: true, beforeFetch })
    .put({ status })
    .json()
}
</script>

<template>
  <h1>{{ data.description }}</h1>
  <PaloozaBoard :nodes="nodes" @updateStatus="updateStatus" />
</template>
