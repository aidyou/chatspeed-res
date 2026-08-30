---
title: "MinerU：文档解析器(PDF/Word/PPT/图片)"
description: "MinerU MCP 服务 1. 概述 MinerU MCP 是一个强大的文档解析服务，专门用于将在线文档转换为高质量的 Markdown 格式。我们的服务支持多种文档格式，包括 PDF、Word、PowerPoint 以及各种图片格式。 2. 核心功能 多格式支持: 支持 PDF、DOC/DOCX、PPT/PPTX、以及 JPG/JPEG/PNG 等图片格式 批量处理: 支持同时处理多个文档URL（通过提供由空格、逗号或换行符分隔的 URL 列表） OCR 识别: 可选启用 OCR 功能，处理扫描版文档和图片中的"
---

# MinerU：文档解析器(PDF/Word/PPT/图片)

MinerU MCP 服务 1. 概述 MinerU MCP 是一个强大的文档解析服务，专门用于将在线文档转换为高质量的 Markdown 格式。我们的服务支持多种文档格式，包括 PDF、Word、PowerPoint 以及各种图片格式。 2. 核心功能 多格式支持: 支持 PDF、DOC/DOCX、PPT/PPTX、以及 JPG/JPEG/PNG 等图片格式 批量处理: 支持同时处理多个文档URL（通过提供由空格、逗号或换行符分隔的 URL 列表） OCR 识别: 可选启用 OCR 功能，处理扫描版文档和图片中的

# MinerU MCP 服务

## 1. 概述

**MinerU MCP** 是一个强大的文档解析服务，专门用于将在线文档转换为高质量的 Markdown 格式。我们的服务支持多种文档格式，包括 PDF、Word、PowerPoint 以及各种图片格式。

## 2. 核心功能

* **多格式支持**: 支持 PDF、DOC/DOCX、PPT/PPTX、以及 JPG/JPEG/PNG 等图片格式
* **批量处理**: 支持同时处理多个文档URL（通过提供由空格、逗号或换行符分隔的 URL 列表）
* **OCR 识别**: 可选启用 OCR 功能，处理扫描版文档和图片中的文字
* **多语言支持**: 支持中文、英文等多种语言的文档识别
* **智能解析**: 保持文档原有格式和结构，生成高质量的 Markdown 内容
* **页面范围选择**: 支持指定特定页面进行转换，提高处理效率

## 3. API 密钥获取

要使用 MinerU API，请访问 [MinerU 官网](https://mineru.net) 注册账号并申请 API 密钥。

## 4. 使用方法

我们提供以下 API 功能：

### 4.1 文档解析 (parse_documents)

将在线文档URL转换为Markdown格式。

**参数说明：**

| 参数                | 类型    | 说明                                                                | 默认值   |
| ------------------- | ------- | ------------------------------------------------------------------- | -------- |
| `file_sources`      | 字符串  | 文档URL，多个可用逗号或换行符分隔 (支持pdf、ppt、pptx、doc、docx以及图片格式jpg、jpeg、png) | -        |
| `enable_ocr`        | 布尔值  | 是否启用 OCR 功能                                                   | `false`  |
| `language`          | 字符串  | 文档语言，默认"ch"中文，可选"en"英文等                            | `ch`     |
| `page_ranges`       | 字符串 (可选) | 指定页码范围，格式为逗号分隔的字符串。例如："2,4-6"：表示选取第2页、第4页至第6页；"2--2"：表示从第2页一直选取到倒数第二页。  | `None`   |

### 4.2 获取OCR语言列表 (get_ocr_languages)

获取支持的OCR识别语言列表，无需参数。

## 5. 支持的文档格式

- **PDF文档**: .pdf
- **Word文档**: .doc, .docx  
- **PowerPoint演示**: .ppt, .pptx
- **图片文件**: .jpg, .jpeg, .png

## 6. 本地部署选项

### 6.1 本地API部署

如果您需要部署本地API进行文档解析（适用于对数据隐私有高要求或需要离线使用的场景），请参考项目的 **[README](https://github.com/opendatalab/MinerU/blob/master/projects/mcp/README.md)** 文档获取详细的本地部署指南。

### 6.2 本地文件解析

我们的在线API服务**不支持本地文件解析**，只能处理可公开访问的在线文档URL。

如果您需要处理本地文件，请考虑以下方案：
- **本地MCP部署**：在本地部署MCP服务器，详细配置请参考项目的 **[README](https://github.com/opendatalab/MinerU/blob/master/projects/mcp/README.md)** 文档
- **文件上传**：将本地文件上传到可公开访问的云存储服务（如云盘、对象存储等），然后使用其公开链接进行解析

## 7. 常见问题

### 7.1 API 密钥问题

**问题**：无法连接 MinerU API 或返回 401 错误。

**解决方案**：请检查你的 API 密钥是否正确。确保从 [MinerU 官网](https://mineru.net) 获取有效的 API 密钥。

### 7.2 URL 访问问题

**问题**：处理在线文档时报无法访问URL错误。

**解决方案**：请确保提供的URL是可公开访问的有效链接，我们的服务器需要能够下载这些文档。

### 7.3 处理大文件超时

**问题**：处理大型文档时出现超时。

**解决方案**：建议将大文档分成多个较小的部分进行处理，或者使用页面范围参数只处理需要的特定页面。

### 7.4 本地文件处理

**问题**：如何处理本地文件？

**解决方案**：我们的在线API不支持直接处理本地文件。您可以：
- 将文件上传到云存储服务获取公开链接后使用
- 参考 README 文档部署本地MCP服务器进行本地文件处理

**官方网站：** [https://github.com/opendatalab/MinerU/tree/master/projects/mcp](https://github.com/opendatalab/MinerU/tree/master/projects/mcp)
**状态：** `active`　**最后核验：** `2026-08-30`

## 分类与标签

- 分类：`development`, `memory`, `files`
- 标签：`file systems`, `developer tools`, `knowledge and memory`, `pdf、图片、word、ppt`, `chinese`

## MCP 配置

- 传输方式：`stdio`
- 启动命令：`uvx`
- 参数：`mineru-mcp`

该配置可通过资源站点索引导入 ChatSpeed。导入前请确认命令、参数和权限来源可信。

## 数据来源

资源文件：`resources/mcp/adrianwangs-mineru.json`。内容最后核验于 `2026-08-30`；免费额度和服务限制可能随官方政策变化。
