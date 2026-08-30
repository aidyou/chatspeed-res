---
title: "TuriX电脑操作智能体"
description: "TuriX · 桌面操作，由AI驱动 与您的计算机对话，观看它工作。 观看我们的演示并下载MCP服务，我们在GitHub上完全开源。 📞 联系方式与社区 通过电子邮件联系我们：contact@turix.ai 如果您对我们的服务感兴趣，欢迎加入我们的微信群。 TuriX 让您强大的AI模型直接在桌面上执行实际的、动手的操作。 它附带了一个最先进的计算机使用代理（通过了我们内部OSWorld风格测试集的68%以上），同时对于个人和研究用途保持100%开源且免费。 更喜欢自己的模型？在config.json中更改即可。"
---

# TuriX电脑操作智能体

TuriX · 桌面操作，由AI驱动 与您的计算机对话，观看它工作。 观看我们的演示并下载MCP服务，我们在GitHub上完全开源。 📞 联系方式与社区 通过电子邮件联系我们：contact@turix.ai 如果您对我们的服务感兴趣，欢迎加入我们的微信群。 TuriX 让您强大的AI模型直接在桌面上执行实际的、动手的操作。 它附带了一个最先进的计算机使用代理（通过了我们内部OSWorld风格测试集的68%以上），同时对于个人和研究用途保持100%开源且免费。 更喜欢自己的模型？在config.json中更改即可。

TuriX · 桌面操作，由AI驱动

与您的计算机对话，观看它工作。

观看我们的演示并下载MCP服务，我们在[GitHub](https://github.com/TurixAI/TuriX-CUA/tree/mac_mcp)上完全开源。
　
## 📞 联系方式与社区

通过电子邮件联系我们：contact@turix.ai

如果您对我们的服务感兴趣，欢迎加入我们的微信群。![二维码](/mcp-assets/36c9a922c3d018dcb69e44be7ccb8e29.jpg)

TuriX 让您强大的AI模型直接在桌面上执行实际的、动手的操作。
它附带了一个**最先进的计算机使用代理**（通过了我们内部OSWorld风格测试集的68%以上），同时对于个人和研究用途保持100%开源且免费。

更喜欢自己的模型？**在`config.json`中更改即可。**

## 目录
- [📞 联系方式与社区](#-联系方式与社区)
- [🚀 快速开始 (macOS 15)](#-快速开始-macos-15)
   - [1. 创建Python 3.12环境](#2-创建python-312环境)
   - [2. 授予macOS权限](#3-授予macos权限)
      - [2.1 辅助功能](#31-辅助功能)
      - [2.2 Safari自动化](#32-safari自动化)
   - [3. MCP支持](#5-mcp支持)

## 🚀 快速开始 (macOS 15)

### 1. 创建Python 3.12环境
首先克隆仓库并运行：
```bash
conda create -n turix_env python=3.12
conda activate turix_env        # requires conda ≥ 22.9
pip install -r requirements.txt
```
### 2. 授予macOS权限

#### 2.1 辅助功能
1. 打开 **系统设置 ▸ 隐私与安全性 ▸ 辅助功能**  
2. 点击 **＋**，然后添加 **终端** 和 **Visual Studio Code** 或任何你使用的IDE
3. 如果代理仍然失败，请也添加 **/usr/bin/python3**

#### 2.2 Safari自动化
1. **Safari ▸ 设置 ▸ 高级** → 启用 **显示Web开发者功能**  
2. 在新的 **开发** 菜单中，启用  
    * **允许远程自动化**  
    * **允许Apple事件中的JavaScript**  

##### 触发权限对话框（每个shell会话运行一次）
```
# macOS Terminal
osascript -e 'tell application "Safari" \
to do JavaScript "alert(\"Triggering accessibility request\")" in document 1'

# VS Code integrated terminal (repeat to grant VS Code)
osascript -e 'tell application "Safari" \
to do JavaScript "alert(\"Triggering accessibility request\")" in document 1'
```
> **在每个对话框上点击“允许”**，以便代理可以控制Safari。

### 3. MCP支持

TuriX 支持 [Model Context Protocol](https://modelcontextprotocol.io/overview)。您可以使用Claude for Desktop将TuriX作为MCP服务器调用，配置如下（假设您有turix_env conda环境）:
```json
{
  "mcpServers": {
    "mcp_agent": {
      "command": "/ABSOLUTE/PATH/TO/YOUR/CONDA/ENV/bin/python",
      "args": [
        "/ABSOLUTE/PATH/TO/FOLDER/TuriX-CUA/src/mcp/mcp_server.py"
      ],
      "env": {
        "LLM_PROVIDER": "turix",
        "LLM_MODEL":   "turix-model",
        "LLM_TEMP":    "0",
        "OPENAI_API_KEY":  "YOUR_KEY_HERE",
        "OPENAI_API_BASE": "YOUR_BASE_URL",
        "MCP_TIMEOUT_SEC": "600"
      }
    }
  }
}
```
您也可以通过更改json文件中的环境来设置您的LLM模型。MCP_TIMEOUT_SEC是时间限制，如果任务运行时间超过设定值，任务将被终止。

如果您想在运行时终止代理，请按cmd+shift+2。

**官方网站：** [https://github.com/TurixAI/TuriX-CUA/tree/mac_mcp](https://github.com/TurixAI/TuriX-CUA/tree/mac_mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`browser`
- 标签：`other`, `browser automation`, `computer-use-agent`, `computer-automation`, `电脑自动化`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`/ABSOLUTE/PATH/TO/YOUR/CONDA/ENV/bin/python`
- 参数：`/ABSOLUTE/PATH/TO/FOLDER/TuriX-CUA/src/mcp/mcp_server.py`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/dennisyk348-turix-computer-use-agent.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
