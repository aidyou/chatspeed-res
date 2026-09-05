---
title: "ResearchArxivPaper-WithMcp-Mic"
description: "Based on the arXiv Open API for Paper Search Introduction arXiv is an open-access repository for publishing scientific papers, covering physics, mathematics, computer science, and many other fields. B…"
---

# ResearchArxivPaper-WithMcp-Mic

Based on the arXiv Open API for Paper Search Introduction arXiv is an open-access repository for publishing scientific papers, covering physics, mathematics, computer science, and many other fields. B…

# Research Paper Finder & Export Tool (MCP Server)

This tool allows users to search research papers on **arXiv** by topic name, optimize keywords to improve search results, view detailed information, and export results in multiple formats (TXT, DOCX, PDF, Excel). It can also generate an **academic summary/conclusion** based on the search results, and logs export activities for later use by intelligent systems or agents.

---

## Input Description

* **Type**: `string`
* **Format**: research topic name (optionally with a year)
* **Examples**:
  * `"Transformer"`
  * `"Sign Language Recognition 2025"`
  * `"Graph Neural Network"`

---

## Feature Modules

### 1. Keyword Optimizer

* **Function**: automatically translates the user's research topic into English and expands it into clearer, more complete keyword phrases or related terms suitable for academic search.
* **Example**:
  * Input: `"手语识别"` (sign language recognition)
  * Output:

```
    Suggested Keywords:
    "Sign Language Recognition", "Transformer-based Sign Language Model", "Video-based Gesture Recognition"
```

* **Use cases**:
  * Improve the relevance and coverage of arXiv searches
  * Provide more potential search terms to improve literature discovery

---

### 2. Search Papers

* **Function**: searches for papers on **arXiv** based on the user input or optimized keywords, and returns:
  * Title
  * Authors
  * Publication date
  * PDF link
  * Abstract
* **Configurable**: number of results (1-10)
* **Example output**:

```
  Search Results for: Transformer
  Paper 1:
  Title      : Transformer for Sign Language Recognition
  Authors    : John Doe, Jane Smith
  Published  : 2023-11-01
  PDF Link   : http://arxiv.org/pdf/...
  Abstract   : This paper explores...
  --------------------------------------------------
```

---

### 3. Generate Summary / Conclusion

* **Function**: generates a concise academic summary based on the titles and abstracts of the searched papers, including:
  * Core findings
  * Research trends
  * Potential applications
* **Use cases**:
  * Quickly grasp the current state of research on a topic
  * Use in research reports or literature reviews
* **Example**:

```
  This collection of papers on "Transformer-based Sign Language Recognition" highlights recent advances in deep learning for gesture understanding, showing improved accuracy and efficiency in video-based recognition systems. Emerging trends focus on multi-modal approaches and real-time applications.
```

---

### 4. Export Results

* **Supported formats**: Text (.txt), Word (.docx), PDF (.pdf), Excel (.xlsx)
* **Export path**: `outputs/`
* **Exported content**: paper title, authors, publication date, PDF link, and abstract
* **Use cases**:
  * Save search results for later analysis
  * Provide references for research reporting or literature management
* **Example file name**:

```
  outputs/exported_results_20250830_213045.pdf
```

---

## Usage Flow

1. Enter a research topic or keyword (optionally with a year)
2. Click **"Search For Keywords"** to get optimized keywords
3. Choose the number of results, then click **"Search with Original Keyword"** or search with the optimized keywords
4. View the search results; you can click **"Generate Summary"** to get an academic summary
5. Choose an export format and click **"Export"** to download the result file

---

## Technical Implementation Notes

* **Search engine**: [arXiv API](http://export.arxiv.org/api/query)
* **Keyword optimization**: uses AI (Spark API) to generate expanded English keywords
* **Export files**:
  * Word: `python-docx`
  * PDF: `reportlab`
  * Excel: `pandas`
* **Summary/conclusion generation**: an AI model (API) processes titles and abstracts to generate the academic summary

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
