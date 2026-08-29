import vue from '@astrojs/vue'
import { defineConfig } from 'astro/config'

export default defineConfig({
  site: 'https://res.aidyou.ai',
  output: 'static',
  integrations: [vue()]
})
