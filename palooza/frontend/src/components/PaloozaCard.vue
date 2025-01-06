<script setup>
import { defineProps } from 'vue'
const props = defineProps({
  card: Object,
})

let iconPath = `${props.card.os_name}.svg`

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
    <div class="flex flex-col">
      <span class="self-start"><b>{{ card.name }}</b></span>
      <span class="self-end"><img :src="iconPath" style="max-width: 50px"></img></span>
      <span class="self-end inline-flex items-center rounded-md bg-gray-50 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">{{card.os_version}}</span>

    </div>
  </div>
</template>
