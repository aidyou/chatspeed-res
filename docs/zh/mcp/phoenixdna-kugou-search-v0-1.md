---
title: "搜狗搜索（MCP&Agent挑战赛）"
description: "根据给定查询执行搜狗网页搜索。 参数： query：用于查询搜狗的搜索关键字字符串。 numresults：返回的搜索结果数量。默认为 10。 返回： 包含搜索结果的字符串，每个结果之间用空行分隔。"
---

# 搜狗搜索（MCP&Agent挑战赛）

根据给定查询执行搜狗网页搜索。 参数： query：用于查询搜狗的搜索关键字字符串。 numresults：返回的搜索结果数量。默认为 10。 返回： 包含搜索结果的字符串，每个结果之间用空行分隔。

## 项目简介
搜狗MCP网页查询，调用搜狗的搜索引擎查询关键词网页信息并返回默认前10条的信息；

## 部署指南

### 环境依赖：
Node.js 18+ 或 Python 3.8+（根据实际运行环境选择）

### 配置说明
参考以下 JSON 配置格式（以 SSE 传输为例）：
json
{
  "mcpServers": {
    "your-server-name": {
      "args": [
        "mcp-remote",
        "https://phoenixdna-t2i-modelscope-mcp.ms.show/gradio_api/mcp/sse",
        "--transport",
        "sse-only"
      ],
      "command": "npx"
    }
  }
}

## 使用示例

### 参数：
query：用于查询搜狗的搜索关键字字符串。
num_results：返回的搜索结果数量。默认为 10。

### 示例
默认为带编号的字典格式的字符串，每个结果之间用空行来分隔
1. {'title': 'SenseTime |商汤科技-坚持原创,让AI引领人类进步', 'url': 'https://www.sogou.com/link?url=DSOYnZeCC_r0JEYtrsRsN6sEpU36pJ_rbhhp9J6i36M.', 'description': '作为人工智能软件公司,商汤科技以“坚持原创,让AI引领人类进步”为使命,旨在持续引领人工智能前沿研究,持续打造更具拓展性更普惠的人工智能软件平台,推动经济、社会...'}

2. {'title': '商汤科技（中国人工智能平台企业）- 搜狗百科', 'url': 'https://baike.sogou.com/v142872499.htm?ch=frombaikevr&fromTitle=%E5%95%86%E6%B1%A4%E7%A7%91%E6%8A%80', 'description': '北京市商汤科技开发有限公司，简称“商汤科技”，成立于2014年，位于北京市海淀区北四环西路，是一家致力于在计算机视觉和深度学习领域原创技术研发的企业，董事长兼经理徐冰。创立人为汤晓鸥...详情'}

3. {'title': '「商汤科技」北京市商汤科技开发有限公司_简介_联系方式_新闻_合作...', 'url': 'https://www.sogou.com/link?url=hedJjaC291Mr8Y1Fgcy1yHoqS6FAC7xcsS6wnfnr1uOpKIaVX01p5bbAp6VRqT6Q', 'description': '2025年8月13日-「商汤科技」简介/介绍，北京市商汤科技开发有限公司成立于2014年11月14日，是一家科技创新公司，致力于打造新一代的计算机视觉理解和人工智能引...'}

4. {'title': '商汤科技| 项目信息-36氪', 'url': 'https://www.sogou.com/link?url=hedJjaC291Nr3Lyvh1x5vtaDV2pBWJbK_CFRTdGaeosnrnQ3SrXh1SXw5Pqtik-2', 'description': '2025年7月28日-商汤科技是一家计算机视觉技术研发商，基于人脸检测跟踪、人脸身份认证、人脸聚类等技术，研发了人脸动态比对服务器、视图情报研判系统等产品，可以在...'}

5. {'title': '商汤科技企业文化-今日头条', 'url': 'https://www.sogou.com/link?url=hedJjaC291PD0T3DYzJqFDoBhFbePHve3pbAgkwwypkj70kbxGDIZBJCd4SN4Yc6q9Y_VloGZf4.', 'description': '2025年3月26日-您在查找商汤科技企业文化吗？今日头条提供详尽的搜索结果聚合，每天实时更新。我们致力于连接人与信息，让优质丰富的信息得到高效精准的分发，促...'}

6. {'title': '商汤科技_相关资讯', 'url': 'https://www.sogou.com/sogou?ie=utf8&interation=1728053249&interV=&query=%E5%95%86%E6%B1%A4%E7%A7%91%E6%8A%80', 'description': '8月26日,商汤科技旗下家用机器人品牌“元萝卜SenseRobot”联动迪士尼经典动画电影《疯狂动物城》发布年度重磅新...'}7. {'title': '商汤科技SenseTime战略投资实习生北京/上海', 'url': 'http://mp.weixin.qq.com/s?src=11&timestamp=1756282041&ver=6199&signature=CcbznusV3Pgo4jQJaZJ3gGWoRC9NK7VLfaf-avyqjJPnbTLV19tMKtuq7hgY5vyHn1I5t2DwvRCCTtjWSCQufgXNL5vu9jubKtIMZX406WY96OXp4KrWcXOk4MG6NOum&new=1', 'description': '5小时前 - 公司介绍: 商汤科技SenseTime是亚洲领先的AI算法提供商、全球领先的人工智能平台公司，业务涵盖智慧城市、智慧交通以及教育、医疗等多个行业。在商汤战投团队，你将全方位参与投资决策的各个环节，培养完整的科技领域投资逻辑；接触科技创新领域的顶尖企业与杰出创业者，收获前沿视野....'}

8. {'title': '智慧城市_企业智能化_智慧出行_SenseTime | 商汤科技', 'url': 'https://www.sogou.com/link?url=hedJjaC291OTJNvFrk_AvREQWJOtJRKQdVip9XM4Qyo6dyZGIu6E4riDEpCfFsCt', 'description': '商汤科技智慧城市AI智能设备产品服务频道旨在为大家呈现商汤科技最新科技产品以及服务，秉承坚持原创的使命，具有完善的产学研体系，拥有多项核心技术能力，让AI赋能百业...'}

9. {'title': '深圳市商汤科技有限公司 - 企查查', 'url': 'https://www.sogou.com/link?url=DSOYnZeCC_qWHpyZ4a2nmuNjyZdYzTj2NE9Wofk1-Rzds8EWy1o8uun2rwl5gxib2ijcy4TUJ_c4d2X6F0SQYA..', 'description': '2025年8月15日-企查查为您提供深圳市商汤科技有限公司的最新工商信息、公司简介、公司地址、电话号码、招聘信息、信用信息、财务信息、法律诉讼等多维度详细信息查询...'}

10. {'title': '北京市商汤科技开发有限公司', 'url': 'https://www.qcc.com/firm/b530c6b779749d4494d4d5f2456ba4b5.html', 'description': '刘强'}

**官方网站：** [https://modelscope.cn/studios/phoenixdna/sogou_search](https://modelscope.cn/studios/phoenixdna/sogou_search)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`
- 标签：`search`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-remote https://phoenixdna-sogou-search.ms.show/gradio_api/mcp/sse --transport sse-only`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/phoenixdna-kugou-search-v0-1.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
