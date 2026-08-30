---
title: "stata-mcp"
description: "Stata-MCP 让LLM帮助你使用Stata进行回归分析 ✨ --- 寻找其他Stata集成或其他工具？ - VScode或Cursor集成在这里。感到困惑？💡 差异 - Jupyter Lab使用（重要：Stata 17+）在这里 - NBER-MCP 🔧 正在建设中 - AER-MCP - Econometrics-Agent - TexIV - 一个由机器学习驱动的框架，使用先进的NLP和ML技术将文本数据转换为可用于实证研究的变量 💡 快速开始 标准配置要求：请确保Stata安装在默认路径下，并且Sta"
---

# stata-mcp

Stata-MCP 让LLM帮助你使用Stata进行回归分析 ✨ --- 寻找其他Stata集成或其他工具？ - VScode或Cursor集成在这里。感到困惑？💡 差异 - Jupyter Lab使用（重要：Stata 17+）在这里 - NBER-MCP 🔧 正在建设中 - AER-MCP - Econometrics-Agent - TexIV - 一个由机器学习驱动的框架，使用先进的NLP和ML技术将文本数据转换为可用于实证研究的变量 💡 快速开始 标准配置要求：请确保Stata安装在默认路径下，并且Sta

Stata-MCP

让LLM帮助你使用Stata进行回归分析 ✨

![en](/mcp-assets/0eedd0c75f6dbccbae1486d81bfae9d0.svg)



[![PyPI version](/mcp-assets/8ba846b66dd1319463f712d5d7b0ebcf.svg)](https://pypi.org/project/stata-mcp/)
[![License: MIT](/mcp-assets/d21e3b2e66556b6b0c8644ab4bcf5a8d.svg)](https://github.com/sepinetam/stata-mcp/blob/HEAD/LICENSE)
[![Issue](/mcp-assets/6254c643f4b946be409d2492b9ce6d6e.svg)](https://github.com/sepinetam/stata-mcp/issues/new)
[![Ask DeepWiki](/mcp-assets/0c95d8c98b281c617e230e437947ee44.svg)](https://deepwiki.com/SepineTam/stata-mcp)

---

> 寻找其他Stata集成或其他工具？
>
> - VScode或Cursor集成[在这里](https://github.com/hanlulong/stata-mcp)。感到困惑？💡 差异
> - Jupyter Lab使用（重要：Stata 17+）[在这里](https://github.com/sepinetam/Jupyter-Stata)
> - [NBER-MCP](https://github.com/sepinetam/NBER-MCP) 🔧 正在建设中
> - [AER-MCP](https://github.com/sepinetam/AER-MCP)
> - [Econometrics-Agent](https://github.com/FromCSUZhou/Econometrics-Agent)
> - [TexIV](https://github.com/sepinetam/TexIV) - 一个由机器学习驱动的框架，使用先进的NLP和ML技术将文本数据转换为可用于实证研究的变量

## 💡 快速开始
> 标准配置要求：请确保Stata安装在默认路径下，并且Stata命令行界面（适用于macOS和Linux）存在。

标准配置json如下，您可以通过添加环境变量来自定义您的配置。
```json
{
  "mcpServers": {
    "stata-mcp": {
      "command": "uvx",
      "args": [
        "stata-mcp"
      ]
    }
  }
}
```
有关更详细的使用信息，请访问使用指南。

对于一些高级用法，请访问高级指南。

### 先决条件
- [uv](https://github.com/astral-sh/uv) - 包安装程序和虚拟环境管理器
- Claude, Cline, ChatWise 或其他LLM服务
- Stata许可证
- 您从LLM获取的API-KEY

### 安装
对于新版本，您不需要再次安装`stata-mcp`包，只需使用以下命令检查您的计算机是否可以使用stata-mcp。
```bash
uvx stata-mcp --usable
uvx stata-mcp --version
```
如果您想在本地使用它，可以通过pip安装或下载源代码。

**通过pip下载**
```bash
pip install stata-mcp
```
**下载源代码并编译**
```bash
git clone https://github.com/sepinetam/stata-mcp.git
cd stata-mcp

uv build
```
然后您可以在`dist`目录中找到编译后的`stata-mcp`二进制文件。您可以直接使用它或将它添加到您的PATH中。

例如：
```bash
uvx /path/to/your/whl/stata_mcp-1.6.0-py3-non-any.whl  # here is the wheel file name, you can change it to your version
```
## 📝 文档
- 更详细的使用信息，请访问使用指南。
- 高级用法，请访问高级。
- 一些问题，请访问问题。
- 与[Stata-MCP@hanlulong](https://github.com/hanlulong/stata-mcp)的区别，请访问区别。

## 💡 问题
- Cherry Studio 32000 错误
- Cherry Studio 32000 错误
- Windows 支持
- 运行Stata-MCP时出现网络错误

## 🚀 路线图
- [x] macOS支持
- [x] Windows支持
- [ ] 其他LLM集成
- [ ] 性能优化

## ⚠️ 免责声明
本项目仅用于研究目的。我对因使用本项目而造成的任何损害不承担责任。请确保您拥有使用Stata的适当许可。

更多信息，请参阅声明。

## 🐛 报告问题
如果您遇到任何错误或有功能请求，请[打开一个问题](https://github.com/sepinetam/stata-mcp/issues/new)。

## 📄 许可证
[MIT许可证](https://github.com/sepinetam/stata-mcp/blob/HEAD/LICENSE)及扩展

## 📚 引用
如果您在研究中使用了Stata-MCP，请使用以下格式之一引用此仓库：

### BibTeX
PLACEHOLDER_CODE_5### APA
```
Song Tan. (2025). Stata-MCP: Let LLM help you achieve your regression analysis with Stata (Version 1.6.0) [Computer software]. https://github.com/sepinetam/stata-mcp
```
### Chicago
```
Song Tan. 2025. "Stata-MCP: Let LLM help you achieve your regression analysis with Stata." Version 1.6.0. https://github.com/sepinetam/stata-mcp.
```
## 📬 联系方式
电子邮件: [sepinetam@gmail.com](mailto:sepinetam@gmail.com)

或者直接通过提交 [Pull Request](https://github.com/sepinetam/stata-mcp/pulls) 来贡献！我们欢迎各种类型的贡献，从修复错误到添加新功能。

## ❤️ 致谢
作者衷心感谢Stata官方团队的支持以及Stata许可证授权进行测试开发。

## ✨ Star 历史

[![Star History Chart](/mcp-assets/7ff5ea12648cd650854ef8cf69c6f49e.svg)](https://www.star-history.com/#sepinetam/stata-mcp&Date)

**官方网站：** [https://github.com/sepinetam/stata-mcp](https://github.com/sepinetam/stata-mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`data`
- 标签：`research and data`, `stata`, `回归分析`, `实证研究`, `经济学`, `计量经济学`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`stata-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/sepinetam-stata.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
