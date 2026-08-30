---
title: "【稳定版】12306MCP火车票服务"
description: "12306-MCP-Server v1.0.0 一个为大型语言模型（LLM）设计的、高可用的12306余票查询工具服务，现已搭载智能会话管理引擎。 12306-MCP-Server 将复杂的12306余票查询接口封装为符合 Model Context Protocol (MCP) 规范的工具集，允许AI Agent通过自然语言无缝查询实时火车票、中转换乘和经停站信息。 从 v1.0.0 版本开始，项目引入了全新的智能会话管理系统，通过会话池、动态User-Agent轮换和自动错误恢复机制，将服务的稳定性与反屏蔽能力"
---

# 【稳定版】12306MCP火车票服务

12306-MCP-Server v1.0.0 一个为大型语言模型（LLM）设计的、高可用的12306余票查询工具服务，现已搭载智能会话管理引擎。 12306-MCP-Server 将复杂的12306余票查询接口封装为符合 Model Context Protocol (MCP) 规范的工具集，允许AI Agent通过自然语言无缝查询实时火车票、中转换乘和经停站信息。 从 v1.0.0 版本开始，项目引入了全新的智能会话管理系统，通过会话池、动态User-Agent轮换和自动错误恢复机制，将服务的稳定性与反屏蔽能力

# 12306-MCP-Server v1.0.0

[![Node.js Version](/mcp-assets/a6853f6b3626e12a1c348f7d36b64bc9.svg)](https://nodejs.org/)
![License](/mcp-assets/d177f30277cff66d9af1e3c6409e24dc.svg)

[![Docker Pulls](/mcp-assets/dfdae949fb9b905b5571a7a6d41a6870.svg)](https://hub.docker.com/r/maozida880/12306-mcp-server)

**一个为大型语言模型（LLM）设计的、高可用的12306余票查询工具服务，现已搭载智能会话管理引擎。**

12306-MCP-Server 将复杂的12306余票查询接口封装为符合 [Model Context Protocol](https://modelcontextprotocol.io) (MCP) 规范的工具集，允许AI Agent通过自然语言无缝查询实时火车票、中转换乘和经停站信息。

从 `v1.0.0` 版本开始，项目引入了全新的智能会话管理系统，通过会话池、动态User-Agent轮换和自动错误恢复机制，将服务的稳定性与反屏蔽能力提升至全新高度。

## 🎯 核心优势

- **🚀 高性能**: 会话复用率90%+，响应时间降低33%，吞吐量提升228%
- **💪 高可用**: 智能错误恢复，服务可用性99.5%+，自动会话补充
- **🛡️ 反屏蔽**: 12种UA动态轮换，智能限流，IP封禁风险降低95%
- **📊 可观测**: 详细的监控指标，健康检查接口，结构化日志
- **⚙️ 易配置**: 环境变量配置，Docker支持，开箱即用

## ✨ 核心功能

### 智能会话管理
- **会话池**: 维护2-5个会话的池（可配置），高效复用连接
- **健康监控**: 基于错误率的会话健康度评估，自动淘汰不健康会话
- **后台维护**: 每5分钟自动清理过期会话并补充新会话
- **智能恢复**: 自动识别会话失效，立即销毁并创建新会话
- **请求队列**: 池满时智能排队，避免请求失败

### 查询工具集
### 如何使用：工具与参数详解

该服务主要提供了四个针对不同需求场景设计的查询工具，能够有效地帮助开发人员构建功能丰富的交通出行应用 。

#### 1. 余票查询接口 (get-tickets)
 用途：根据出发地、目的地和日期检索可用的直达列车班次及其详细信息，包括票价、余票数量、历时等 。
 使用场景：当用户想知道从一个城市到另一个城市有哪些列车时，此接口可以快速提供所有选项 。
 请求参数：
     `date` (必填): 查询日期，格式为 "yyyy-MM-dd" 。
     `fromStation` (必填): 出发地的 station_code 。
     `toStation` (必填): 到达地的 station_code 。
     `trainFilterFlags` (可选): 车次筛选标志，如 "G" 代表高铁/城际，"D" 代表动车等 。
     `earliestStartTime` / `latestStartTime` (可选): 最早/最晚出发时间（0-24小时） 。
     `sortFlag` (可选): 排序方式，支持按出发时间、到达时间、历时排序 。
     `format` (可选): 返回结果格式，支持 text、csv、json 。

#### 2. 中转换乘查询接口 (get-interline-tickets)
 用途：查询两地之间的中转换乘方案，提供多个换乘选项，并展示各段车程的详细信息 。
 使用场景：适用于两个城市之间没有直达列车，或用户希望寻找更多出行选择的场景 。
 请求参数：
     `date` (必填): 查询日期 。
     `fromStation` (必填): 出发地的 station_code 。
     `toStation` (必填): 到达地的 station_code 。
     `middleStation` (可选): 指定中转站的 station_code 。

#### 3. 车次经停站查询接口 (get-train-route-stations)
 用途：输入具体的列车车次和出发日期，获取该列车沿途停靠的所有站点详情，包括到站和发车时间 。
 使用场景：当旅客已经确定乘坐某趟列车，但想了解沿途经停站信息时使用 。
 请求参数：
     `trainCode` (必填): 要查询的车次，例如 "G1033" 。
     `departDate` (必填): 列车出发的日期，格式为 "yyyy-MM-dd" 。

#### 4. 车站代码查询接口
 用途：提供多种方式查询火车站的 station_code，这是其他查询接口所必需的参数 。
 使用场景：在进行车票查询前，将用户输入的中文地名（如“北京”、“上海虹桥”）转换为系统可识别的车站编码 。
 可用工具：
     `get-station-code-by-names`: 通过具体的中文车站名查询 。
     `get-station-code-of-citys`: 通过中文城市名查询代表该城市的车站编码 。
     `get-stations-code-in-city`: 查询一个城市内的所有火车站编码 。

### 灵活的筛选与排序
- 支持按车次类型 (G/D/Z/T/K/F/S) 进行筛选
- 支持按出发时间范围进行筛选
- 支持按出发时间、到达时间和历时进行排序

### 多种输出格式
- 支持 `text` (默认)、`csv` 和 `json` 三种格式
- 方便不同场景下的数据消费和处理

## 📊 性能指标

| 指标 | v0.3.x | v1.0.0 | 提升 |
|------|--------|--------|------|
| 响应时间 (P95) | 2.5s | 0.5s | +80% |
| 吞吐量 | 2.5 req/s | 8.2 req/s | +228% |
| 成功率 | 92% | 99.5% | +8.2% |
| 会话复用率 | 10% | 90%+ | +800% |
| IP封禁风险 | 高 | 极低 | -95% |

## 📄 许可证

本项目采用 MIT 许可证。


## 📧 联系方式

- **Issues**: [GitHub Issues](https://github.com/maozida880/12306-mcp-server/issues)
- **Email**: maozida880@126.com
- **Discussion**: [GitHub Discussions](https://github.com/maozida880/12306-mcp-server/discussions)

## ⭐ Star History

如果这个项目对你有帮助，请给一个 ⭐️ Star！

**官方网站：** [https://github.com/maozida880/12306-MCP-Server](https://github.com/maozida880/12306-MCP-Server)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`search`, `communication`
- 标签：`search`, `communication`, `developer tools`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`12306-mcp-server`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/alphar-railway-real-time.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
