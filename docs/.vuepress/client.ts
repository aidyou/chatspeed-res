import { defineClientConfig } from 'vuepress/client'
import ResourceBrowser from './components/ResourceBrowser.vue'

export default defineClientConfig({
  enhance({ app }) {
    app.component('ResourceBrowser', ResourceBrowser)
  }
})
