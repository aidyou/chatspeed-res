---
title: "像素实验室MCP"
description: "🎨 Pixelle MCP - 全模态融合智能体框架 ✨ 基于 MCP 协议的 AIGC 方案，零代码将 ComfyUI 工作流无缝转化为 MCP Tool，让 LLM 与 ComfyUI 强强联合。 官网地址 https://github.com/AIDC-AI/Pixelle-MCP --- 🌟 简介 Pixelle 是一个开源的全模态代理框架，通过 模型上下文协议 (MCP) 将 Comfy…"
---

# 像素实验室MCP

🎨 Pixelle MCP - 全模态融合智能体框架 ✨ 基于 MCP 协议的 AIGC 方案，零代码将 ComfyUI 工作流无缝转化为 MCP Tool，让 LLM 与 ComfyUI 强强联合。 官网地址 https://github.com/AIDC-AI/Pixelle-MCP --- 🌟 简介 Pixelle 是一个开源的全模态代理框架，通过 模型上下文协议 (MCP) 将 Comfy…

🎨 Pixelle MCP - 全模态融合智能体框架

✨ 基于 MCP 协议的 AIGC 方案，零代码将 ComfyUI 工作流无缝转化为 MCP Tool，让 LLM 与 ComfyUI 强强联合。

### 官网地址 https://github.com/AIDC-AI/Pixelle-MCP

---

## 🌟 简介

**Pixelle** 是一个开源的全模态代理框架，通过 **模型上下文协议 (MCP)** 将 ComfyUI 与大型语言模型 (LLM) 无缝集成。它允许用户将复杂的 ComfyUI 工作流转换为可调用的 MCP 工具，**无需任何代码**，让 LLM 能够执行包括文本、图像、声音/语音和视频等多种 AIGC 任务。

Pixelle 构建于可扩展的 ComfyUI 生态系统之上，采用强大的客户端-服务器架构，为开发、部署与多模态 AI 生成功能的利用，提供灵活统一的解决方案。

---

## 🚀 主要特性

- ✅ **全模态支持**：支持 TISV（Text、Image、Sound/Speech、Video）全模态的互转与生成
- ✅ **ComfyUI 生态**：底层基于 [ComfyUI](https://github.com/comfyanonymous/ComfyUI)，兼容其开放生态下的所有能力
- ✅ **零代码开发**：创新性“Workflow 即 MCP Tool”方案，0代码即可动态添加新工具
- ✅ **MCP Server**：服务端基于 [MCP 协议](https://modelcontextprotocol.io/introduction)，兼容任意 MCP 客户端（如 Cursor、Claude Desktop 等）
- ✅ **MCP Client**：客户端基于 [Chainlit](https://github.com/Chainlit/chainlit) 框架开发，支持丰富交互控件，可集成多个 MCP Server
- ✅ **灵活部署**：可独立部署 Server（仅服务端）、Client（仅客户端），或联合部署
- ✅ **统一配置**：采用 YAML 配置，一个文件管理所有服务
- ✅ **多 LLM 支持**：支持主流 LLM，包括 OpenAI、Ollama、Gemini、DeepSeek、Claude、Qwen 等

---

## 🖥️ Demo 演示

| Demo 名称         | 演示                                                         | 简要描述                      |
| ----------------- | ---------------------------------------------------------------- | ----------------------------- |
| 捣蛋鬼Pixelle       | [demo链接](https://demo.pixelle.ai/?starter=wan)                | 连贯故事情节推理（推理能力及一致性能力）          |
| 无声航线             | [demo链接](https://demo.pixelle.ai/?starter=silent-route)        | 基于风格参考的转绘视频    |
| 概念车宣传视频        | [demo链接](http://demo.pixelle.ai/?starter=car)                  | 使用Flux-Krea进行原型概念设计（快速兼容最新模型能力）     |

> 每个 Demo 提供了不同场景下的全模态智能体能力，欢迎点击体验更多功能！

---

## 📁 项目结构

| 模块          | 描述                                                            |
| ------------- | --------------------------------------------------------------- |
| `mcp-base`    | 🔧 基础服务，提供文件存储和通用服务能力                         |
| `mcp-client`  | 🌐 MCP 客户端，基于 Chainlit 构建的 Web 界面                    |
| `mcp-server`  | 🗄️ MCP 服务端，集成多种 AIGC 工具与服务                         |

---

## 💡 适用场景

- 通用多模态智能体研发
- 零代码定制 AIGC 工作流
- 强化 LLM 工具调用能力
- 灵活部署企业级 AI 服务

---

> 欢迎 Star ⭐️、Fork 🎉、提交 Issue 或 PR，共同完善 Pixelle MCP！

**官方网站：** [https://github.com/AIDC-AI/Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`media`
- 标签：`entertainment and media`, `art and culture`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`npx`
- 参数：`mcp-pixellab --secret=your-pixellab-secret-here`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/pixelle-lab-pixelle.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
