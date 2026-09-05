---
title: "ResearchArxivPaper-WithMcp-Mic"
description: "Based on the arXiv Open API for Paper Search --- Introduction arXiv 是一个用于发布科学论文的开放存取库，涵盖了物理学、数学、计算机科学等多个领域。通过使用 arXiv 提供的开放 API，开发者可以轻松地进行论文搜索和获取相关信息。 Getting Started Prerequisites - 你需要一个 arXiv API 密…"
---

# ResearchArxivPaper-WithMcp-Mic

Based on the arXiv Open API for Paper Search --- Introduction arXiv 是一个用于发布科学论文的开放存取库，涵盖了物理学、数学、计算机科学等多个领域。通过使用 arXiv 提供的开放 API，开发者可以轻松地进行论文搜索和获取相关信息。 Getting Started Prerequisites - 你需要一个 arXiv API 密…

我帮你整理了一份更新后的 README，并把 **Keyword Optimizer** 和 **Summary/Conclusion** 功能详细说明都加上了，同时保持了原来的风格和示例。下面是修改后的版本：

---

# 📚 研究论文查找与导出工具 (MCP 服务器)

该工具允许用户通过主题名称在 **arXiv** 上搜索研究论文，优化关键词以提升搜索效果，查看详细信息，并以多种格式导出结果（TXT、DOCX、PDF、Excel）。它还可以基于搜索结果生成 **学术总结/结论**，并记录导出活动，以便智能系统或代理后续使用。

---

## ✅ 输入描述

* **类型**: `string`
* **格式**: 研究主题名称（可选带年份）
* **示例**：

  * `"Transformer"`
  * `"Sign Language Recognition 2025"`
  * `"Graph Neural Network"`

---

## 🔑 功能模块

### 1. Keyword Optimizer (关键词优化)

* **功能**:
  自动将用户输入的研究主题翻译为英文，并扩展为更清晰、完整且适合学术搜索的关键词短语或相关术语。
* **示例**：

  * 输入: `"手语识别"`
  * 输出:

```
    Suggested Keywords:
    "Sign Language Recognition", "Transformer-based Sign Language Model", "Video-based Gesture Recognition"
```
* **用途**:

  * 提高 arXiv 搜索的相关性和覆盖范围
  * 提供更多潜在检索词，提高文献发现率

---

### 2. Search Papers (论文搜索)

* **功能**:
  根据用户输入或优化后的关键词在 **arXiv** 上搜索论文，并返回：

  * 标题
  * 作者
  * 发表日期
  * PDF 链接
  * 摘要
* **可设置**: 返回结果数量（1\~10 条）
* **示例输出**:

```
  🔍 Search Results for: Transformer
  📄 Paper 1:
  Title      : Transformer for Sign Language Recognition
  Authors    : John Doe, Jane Smith
  Published  : 2023-11-01
  PDF Link   : http://arxiv.org/pdf/...
  Abstract   : 本文探讨了...
  --------------------------------------------------
```

---

### 3. Generate Summary / Conclusion (学术总结)

* **功能**:
  基于已搜索论文的标题和摘要生成简明学术总结，包括：

  * 核心发现
  * 研究趋势
  * 潜在应用
* **用途**:

  * 快速把握主题研究现状
  * 用于科研报告或文献综述
* **示例**:

```
  This collection of papers on "Transformer-based Sign Language Recognition" highlights recent advances in deep learning for gesture understanding, showing improved accuracy and efficiency in video-based recognition systems. Emerging trends focus on multi-modal approaches and real-time applications.
```

---

### 4. Export Results (导出结果)

* **支持格式**: Text (.txt), Word (.docx), PDF (.pdf), Excel (.xlsx)
* **导出路径**: `outputs/`
* **导出内容**: 包含论文标题、作者、发表日期、PDF 链接及摘要
* **用途**:

  * 保存检索结果用于后续分析
  * 提供科研汇报或文献管理参考
* **示例文件名**:

```
  outputs/exported_results_20250830_213045.pdf
```

---

## ⚡ 使用流程

1. 输入研究主题或关键词（可带年份）
2. 点击 **“✨ Search For Keywords”** 获取优化关键词
3. 选择结果数量，点击 **“🔍 Search with Original Keyword”** 或使用优化关键词搜索论文
4. 查看搜索结果，可点击 **“📝 Generate Summary”** 获取学术总结
5. 选择导出格式并点击 **“📦 Export”** 下载结果文件

---

## 📝 技术实现说明

* **搜索引擎**: [arXiv API](http://export.arxiv.org/api/query)
* **关键词优化**: 使用 AI（Spark API）生成英文扩展关键词
* **导出文件**:

  * Word: `python-docx`
  * PDF: `reportlab`
  * Excel: `pandas`
* **总结/结论生成**: AI 模型（API）处理标题和摘要生成学术总结

---

**Official site: ** [https://www.modelscope.cn/studios/Mic752/ResearchArxivPaper-WithMcp](https://www.modelscope.cn/studios/Mic752/ResearchArxivPaper-WithMcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `calendar management`, `search`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://mic752-researcharxivpaper-withmcp.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/mic752-researcharxivpaper-withmcp-mic.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
