import { viteBundler } from '@vuepress/bundler-vite'
import { defineUserConfig } from 'vuepress/cli'
import { hopeTheme } from 'vuepress-theme-hope'

export default defineUserConfig({
  lang: 'zh-CN',
  title: 'ChatSpeed 资源中心',
  description: '为 ChatSpeed 收集 MCP、模型供应商和免费 AI 服务。',
  base: '/',

  head: [
    ['meta', { name: 'theme-color', content: '#00d4ff' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }]
  ],

  theme: hopeTheme({
    logo: 'https://www.google.com/s2/favicons?domain=aidyou.ai&sz=64',
    editLink: false,
    contributors: false,
    lastUpdated: false,
    git: false,
    navbar: [
      { text: '首页', link: '/' },
      { text: 'MCP 服务', link: '/mcp/' },
      { text: '模型供应商', link: '/models/' },
      { text: '免费 AI', link: '/free-ai/' },
      { text: '使用说明', link: '/guide/' },
      {
        text: '更多',
        children: [
          { text: 'ChatSpeed 官网', link: 'https://aidyou.ai' },
          { text: '提交资源', link: 'https://github.com/aidyou/chatspeed-res' }
        ]
      }
    ],
    sidebar: false,
    plugins: {
      git: false
    }
  }),

  bundler: viteBundler({
    viteOptions: {
      define: {
        __VUE_HMR_RUNTIME__: '{}'
      },
      css: {
        preprocessorOptions: {
          scss: { charset: false, quietDeps: true }
        }
      }
    }
  })
})
