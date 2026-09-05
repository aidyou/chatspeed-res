import { viteBundler } from '@vuepress/bundler-vite'
import { defineUserConfig } from 'vuepress/cli'
import { hopeTheme } from 'vuepress-theme-hope'

// English is the default locale at the site root; Chinese lives under /zh/.
const navbarEn = [
  { text: 'Home', link: '/' },
  { text: 'MCP Servers', link: '/mcp/' },
  { text: 'Model Providers', link: '/models/' },
  { text: 'Free AI', link: '/free-ai/' },
  { text: 'Guide', link: '/guide/' },
  {
    text: 'More',
    children: [
      { text: 'ChatSpeed Site', link: 'https://aidyou.ai' },
      { text: 'Submit a resource', link: 'https://github.com/aidyou/chatspeed-res' }
    ]
  }
]

const navbarZh = [
  { text: '首页', link: '/zh/' },
  { text: 'MCP 服务', link: '/zh/mcp/' },
  { text: '模型供应商', link: '/zh/models/' },
  { text: '免费 AI', link: '/zh/free-ai/' },
  { text: '使用说明', link: '/zh/guide/' },
  {
    text: '更多',
    children: [
      { text: 'ChatSpeed 官网', link: 'https://aidyou.ai' },
      { text: '提交资源', link: 'https://github.com/aidyou/chatspeed-res' }
    ]
  }
]

export default defineUserConfig({
  lang: 'en-US',
  title: 'ChatSpeed Resource Center',
  description: 'MCP servers, model providers, and free AI services for ChatSpeed.',
  base: '/',

  locales: {
    '/': { lang: 'en-US', title: 'ChatSpeed Resource Center', description: 'MCP servers, model providers, and free AI services for ChatSpeed.' },
    '/zh/': { lang: 'zh-CN', title: 'ChatSpeed 资源中心', description: '为 ChatSpeed 收集 MCP、模型供应商和免费 AI 服务。' }
  },

  head: [
    ['meta', { name: 'theme-color', content: '#b85c3d' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    // First visit only: if the browser language is Chinese and the user lands on
    // the English root, switch to /zh/. The stored key means a later manual switch
    // via the navbar language dropdown is respected and never overridden.
    ['script', {}, "(function(){try{var K='cs-res-locale';if(localStorage.getItem(K))return;var l=(navigator.language||'').toLowerCase();var zh=l.indexOf('zh')===0;localStorage.setItem(K,zh?'zh':'en');if(zh&&(location.pathname==='/'||/\\/index\\.html$/.test(location.pathname)))location.replace('/zh/');}catch(e){}})();"]
  ],

  theme: hopeTheme({
    logo: 'https://www.google.com/s2/favicons?domain=aidyou.ai&sz=64',
    editLink: false,
    contributors: false,
    lastUpdated: false,
    git: false,
    sidebar: false,
    plugins: {
      git: false
    },
    locales: {
      '/': { navbar: navbarEn },
      '/zh/': { navbar: navbarZh }
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
