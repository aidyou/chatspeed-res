export const siteData = JSON.parse("{\"base\":\"/\",\"lang\":\"zh-CN\",\"title\":\"ChatSpeed 资源中心\",\"description\":\"为 ChatSpeed 收集 MCP、模型供应商和免费 AI 服务。\",\"head\":[[\"meta\",{\"name\":\"theme-color\",\"content\":\"#00d4ff\"}],[\"meta\",{\"name\":\"apple-mobile-web-app-capable\",\"content\":\"yes\"}]],\"locales\":{\"/\":{\"lang\":\"zh-CN\",\"title\":\"ChatSpeed 资源中心\",\"description\":\"为 ChatSpeed 收集 MCP、模型供应商和免费 AI 服务。\"}}}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  __VUE_HMR_RUNTIME__.updateSiteData?.(siteData)
}

if (import.meta.hot) {
  import.meta.hot.accept((m) => {
    __VUE_HMR_RUNTIME__.updateSiteData?.(m.siteData)
  })
}
