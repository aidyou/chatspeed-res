export const themeData = JSON.parse("{\"encrypt\":{},\"logo\":\"https://www.google.com/s2/favicons?domain=aidyou.ai&sz=64\",\"editLink\":false,\"contributors\":false,\"lastUpdated\":false,\"git\":false,\"locales\":{\"/\":{\"lang\":\"zh-CN\",\"navbarLocales\":{\"langName\":\"简体中文\",\"selectLangAriaLabel\":\"选择语言\"},\"metaLocales\":{\"author\":\"作者\",\"date\":\"写作日期\",\"origin\":\"原创\",\"views\":\"访问量\",\"category\":\"分类\",\"tag\":\"标签\",\"readingTime\":\"阅读时间\",\"words\":\"字数\",\"toc\":\"此页内容\",\"prev\":\"上一页\",\"next\":\"下一页\",\"contributors\":\"贡献者\",\"editLink\":\"编辑此页\",\"print\":\"打印\"},\"outlookLocales\":{\"themeColor\":\"主题色\",\"darkmode\":\"外观\",\"fullscreen\":\"全屏\"},\"routerLocales\":{\"skipToContent\":\"跳至主要內容\",\"notFoundTitle\":\"页面不存在\",\"notFoundMsg\":[\"这里什么也没有\",\"我们是怎么来到这儿的？\",\"这 是 四 零 四 !\",\"看起来你访问了一个失效的链接\"],\"back\":\"返回上一页\",\"home\":\"带我回家\"},\"navbar\":[{\"text\":\"首页\",\"link\":\"/\"},{\"text\":\"MCP 服务\",\"link\":\"/mcp/\"},{\"text\":\"模型供应商\",\"link\":\"/models/\"},{\"text\":\"免费 AI\",\"link\":\"/free-ai/\"},{\"text\":\"使用说明\",\"link\":\"/guide/\"},{\"text\":\"更多\",\"children\":[{\"text\":\"ChatSpeed 官网\",\"link\":\"https://aidyou.ai\"},{\"text\":\"提交资源\",\"link\":\"https://github.com/aidyou/chatspeed-res\"}]}],\"sidebar\":false}}}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateThemeData) {
    __VUE_HMR_RUNTIME__.updateThemeData(themeData)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ themeData }) => {
    __VUE_HMR_RUNTIME__.updateThemeData(themeData)
  })
}
