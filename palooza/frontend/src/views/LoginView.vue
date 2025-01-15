<script setup lang="ts">
import { useCookies } from '@vueuse/integrations/useCookies'
import { useFetch } from '@vueuse/core'
import { ref } from 'vue'
import { useRouter } from 'vue-router';
const router = useRouter()


const url = ref(`${import.meta.env.VITE_API_URL}/login`)
const cookies = useCookies()
const username = ref()
const password = ref()

const login = async function (evt) {
  const { data, error, abort, statusCode, isFetching, isFinished, canAbort, execute } =
    await useFetch(url, {}).post({ "username": username.value, "password": password.value }).json()
  if (error.value) {
    console.log(error.value)
    throw error.value
  } else {
    cookies.set('jwt', data.value.access_token)
    router.push({name: 'home'})
  }
}
</script>

<template>
  <div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">
        Sign in to your account
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" v-on:submit.prevent="login">
        <div>
          <label for="email" class="block text-sm/6 font-medium text-gray-900">GRIT User</label>
          <div class="mt-2">
            <input
              name="username"
              id="username"
              required
              class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
              v-model="username"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
            <div class="text-sm">
              <a
                href="https://selfservice.grit.ucsb.edu/"
                class="font-semibold text-indigo-600 hover:text-indigo-500"
                >Forgot password?</a
              >
            </div>
          </div>
          <div class="mt-2">
            <input
              type="password"
              name="password"
              id="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
              v-model="password"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Sign in
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
