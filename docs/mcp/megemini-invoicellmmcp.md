---
title: "发票识别LLM MCP（MCP&Agent挑战赛 - -作品4）"
description: "InvoiceLLM 是一个智能发票识别代理，使用先进的OCR技术和本地大模型从发票文档中提取结构化信息。该系统支持图片和PDF格式，为敏感财务文档处理提供注重隐私的解决方案。"
---

# 发票识别LLM MCP（MCP&Agent挑战赛 - -作品4）

InvoiceLLM 是一个智能发票识别代理，使用先进的OCR技术和本地大模型从发票文档中提取结构化信息。该系统支持图片和PDF格式，为敏感财务文档处理提供注重隐私的解决方案。

---
domain:
- cv
tags:
- invoice
- ocr
- document-processing
- financial
models:
- Qwen3-0.6B
deployspec:
  entry_file: app.py
license: Apache License 2.0
---

# 📄 InvoiceLLM - 智能发票识别智能体

## 📖 项目简介
InvoiceLLM 是一个智能发票识别智能体，使用先进的OCR技术和本地大模型从发票文档中提取结构化信息。该系统支持图片和PDF格式，为敏感财务文档处理提供注重隐私的解决方案。

## ✨ 功能特点
- 📋 **多格式支持**: 处理图片文件（JPG、PNG等）和PDF文档
- 🔍 **先进OCR技术**: 使用PaddleOCR进行准确的文本提取
- 🤖 **AI驱动分析**: 利用本地大模型（Qwen3-0.6B）进行智能字段提取
- 🔒 **隐私保护**: 所有处理都在本地进行，确保敏感发票数据安全
- 📊 **全面字段提取**: 提取关键发票信息，包括：
  - 📝 通用字段：发票号码、发票代码、开票日期、金额、税额
  - 🏢 购买方和销售方信息：公司详情、纳税人识别号、地址、电话、银行账户
  - 🛍️ 商品信息：商品名称、规格型号、数量、单价、税率
  - 👤 其他信息：收款人、复核、开票人

## 🏗️ 技术架构
1. **📄 文档处理**:
   - 🖼️ 图片：使用PaddleOCR进行OCR处理
   - 📑 PDF：使用PyMuPDF直接提取文本
   
2. **🧠 信息提取**:
   - 🤖 本地大模型（Qwen3-0.6B）进行智能字段解析
   - ✅ 高级验证和纠正算法
   
3. **💻 用户界面**:
   - 🌐 基于Gradio的Web界面
   - ⚡ 实时处理和可视化

## 🚀 使用方法
1. 📤 上传发票文件（图片或PDF）
2. ✅ 点击提交处理发票
3. 📋 以JSON格式查看提取的结构化信息

## 📦 部署指南

### 环境要求
- Python 3.8 或更高版本
- 操作系统：Linux、macOS 或 Windows
- 至少 4GB RAM（推荐 8GB 或更多）
- 至少 2GB 可用磁盘空间（用于模型文件）

### 安装步骤

1. **克隆项目**
```bash
   git clone https://www.modelscope.cn/studios/megemini/InvoiceLLM.git
   cd InvoiceLLM
```

2. **创建虚拟环境（推荐）**
```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # 或
   venv\Scripts\activate     # Windows
```

3. **安装依赖**
```bash
   pip install -r requirements.txt
```

4. **下载模型文件**
   - Qwen3-0.6B 模型将自动在首次运行时下载
   - 或者手动下载并放置在模型目录中

### 运行应用

1. **启动 Web 界面**
```bash
   python app.py
```

2. **访问应用**
   - 打开浏览器访问 `http://127.0.0.1:7860`
   - 或使用 Gradio 提供的本地链接

3. **作为 MCP Server 使用**
   - 启动应用后，MCP Server 会自动运行
   - Streamable HTTP URL: `http://127.0.0.1:7860/gradio_api/mcp/`
   - SSE URL: `http://127.0.0.1:7860/gradio_api/mcp/sse`

## 💡 使用示例

### 示例 1：处理图片发票

1. 点击"选择文件"按钮上传一张发票图片（JPG、PNG等格式）
2. 点击"开始识别"按钮
3. 查看识别结果：
   - 左侧显示 OCR 可视化结果
   - 右侧显示提取的结构化 JSON 数据

### 示例 2：处理 PDF 发票

1. 上传 PDF 格式的发票文件
2. 点击"开始识别"按钮
3. 系统将自动提取 PDF 中的文本并使用 AI 模型解析
4. 查看提取的发票信息

### 示例 3：使用示例文件

1. 在页面底部的"示例"区域，点击任意示例发票图片
2. 或点击"处理示例"按钮
3. 系统将自动处理示例文件并显示结果

## 🛠️ 依赖项
- 🔧 PaddleOCR：图片处理OCR引擎
- 📄 PyMuPDF：PDF文本提取
- 🤖 Qwen3-0.6B：本地大语言模型
- 🖥️ Gradio：Web界面框架
- 🖼️ PIL：图像处理
- 🔥 PyTorch：模型推理后端

## 📜 许可证
Apache License 2.0

**官方网站：** [https://megemini-invoicellm.ms.show/gradio_api/mcp/](https://megemini-invoicellm.ms.show/gradio_api/mcp/)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`productivity`
- 标签：`other`, `办公自动化`, `发票识别`, `ocr`, `llm`, `本地大模型`

## MCP 配置

- 传输方式：`http`
- 启动命令：``
- 参数：无

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/megemini-invoicellmmcp.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
