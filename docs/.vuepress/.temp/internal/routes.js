export const redirects = JSON.parse("{}")

export const routes = Object.fromEntries([
  ["/", { loader: () => import(/* webpackChunkName: "index.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/README.md"), meta: {"title":"ChatSpeed 资源中心"} }],
  ["/free-ai/", { loader: () => import(/* webpackChunkName: "free-ai_index.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/free-ai/README.md"), meta: {"title":"免费 AI"} }],
  ["/free-ai/modelscope-free-quota.html", { loader: () => import(/* webpackChunkName: "free-ai_modelscope-free-quota.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/free-ai/modelscope-free-quota.md"), meta: {"title":"魔塔免费调用额度"} }],
  ["/free-ai/nvidia-nim-free-tier.html", { loader: () => import(/* webpackChunkName: "free-ai_nvidia-nim-free-tier.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/free-ai/nvidia-nim-free-tier.md"), meta: {"title":"NVIDIA NIM API"} }],
  ["/free-ai/openrouter-free-models.html", { loader: () => import(/* webpackChunkName: "free-ai_openrouter-free-models.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/free-ai/openrouter-free-models.md"), meta: {"title":"OpenRouter 免费模型"} }],
  ["/guide/", { loader: () => import(/* webpackChunkName: "guide_index.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/guide/README.md"), meta: {"title":"使用说明"} }],
  ["/mcp/", { loader: () => import(/* webpackChunkName: "mcp_index.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/mcp/README.md"), meta: {"title":"MCP 服务"} }],
  ["/mcp/context7.html", { loader: () => import(/* webpackChunkName: "mcp_context7.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/mcp/context7.md"), meta: {"title":"Context7"} }],
  ["/models/", { loader: () => import(/* webpackChunkName: "models_index.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/models/README.md"), meta: {"title":"模型供应商"} }],
  ["/models/modelscope.html", { loader: () => import(/* webpackChunkName: "models_modelscope.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/models/modelscope.md"), meta: {"title":"魔塔社区"} }],
  ["/models/nvidia-nim.html", { loader: () => import(/* webpackChunkName: "models_nvidia-nim.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/models/nvidia-nim.md"), meta: {"title":"NVIDIA NIM"} }],
  ["/models/openrouter.html", { loader: () => import(/* webpackChunkName: "models_openrouter.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/models/openrouter.md"), meta: {"title":"OpenRouter"} }],
  ["/404.html", { loader: () => import(/* webpackChunkName: "404.html" */"/home/xc/dev/rust/chatspeed/chatspeed-res/docs/.vuepress/.temp/pages/404.html.vue"), meta: {"title":""} }],
]);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  __VUE_HMR_RUNTIME__.updateRoutes?.(routes)
  __VUE_HMR_RUNTIME__.updateRedirects?.(redirects)
}

if (import.meta.hot) {
  import.meta.hot.accept((m) => {
    __VUE_HMR_RUNTIME__.updateRoutes?.(m.routes)
    __VUE_HMR_RUNTIME__.updateRedirects?.(m.redirects)
  })
}
