import { useCookies } from '@vueuse/integrations/useCookies'
import { createFetch } from '@vueuse/core'
import router from './router'

const baseUrl = `${import.meta.env.VITE_API_URL}`
const cookies = useCookies()

export const networkClient = createFetch({
  baseUrl,
  options: {
    beforeFetch({ options, cancel }) {
      const token = cookies.get('jwt')

      if (!token) {
        cancel()
        router.push({ path: '/login', replace: true })
      }
      options.headers.Authorization = `Bearer ${token}`

      return { options }
    },
    afterFetch(ctx) {
      // if the response contains a data property, return it
      if (ctx.data) {
        return ctx.data
      }

      return ctx
    },
  },
  fetchOptions: {
    mode: 'cors',
  },
})
