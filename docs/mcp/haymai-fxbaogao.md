---
title: "fxbaogao"
description: "The Discovery Report is a professional research report search platform. It comprehensively covers the search and reading of related research reports including industry analysis, company research, macr…"
---

# fxbaogao

The Discovery Report is a professional research report search platform. It comprehensively covers the search and reading of related research reports including industry analysis, company research, macr…

# 📊 Discovery Report (MCP Tool)

This tool is integrated into the MCP protocol, providing search and content extraction capabilities for research reports on the Discovery Report website. It is suitable for scenarios such as financial analysis, industry research, and investment analysis.

💡 Official New Version Released: Now supports skills, mcp, cli. [Try it now](https://www.fxbaogao.com/agent-interface)
---

## ✨ Tool One: `search_reports`

Searches for a list of research reports based on conditions such as keywords, authors, organization names, and time ranges.

### 🔧 Parameter Description

| Parameter Name | Type              | Required | Description |
|---------------|-------------------|----------|-------------|
| `keywords`    | `str`             | No       | Search keywords, supports both Chinese and English. |
| `authors`     | `List[str]`       | No       | List of author names, e.g., `["Zhang San", "Li Si"]`. |
| `org_names`   | `List[str]`       | No       | List of organization names, e.g., `["Discovery Report", "Alibaba"]`. |
| `start_time`  | `int`             | No       | Start time, in milliseconds, e.g., `1640995200000` represents 2022-01-01 00:00:00. |
| `end_time`    | `int` / `str`     | No       | End time, supports millisecond timestamp or relative time string:
• `"last3day"`
• `"last7day"`
• `"last1mon"`
• `"last3mon"`
• `"last1year"` |
| `page_size`   | `int`             | No       | Number of results to return, default is 10, maximum is 100. |

### 📥 Usage Example

```python

# Search by keyword

search_reports(keywords="AI")

# Search by institution

search_reports(org_names=["Discovery Reports"])

# Search reports by a specific author from the last week

search_reports(authors=["Wang Lei"], end_time="last7day")

# Search within an exact time range

search_reports(

    keywords="new energy",

    start_time=1748707200000,

    end_time=1749398399999

)

```
## ✨ Tool Two: `get_report_content`

Fetches detailed content and summary information of a report based on the report ID (`doc_id`).

---

### 🔧 Parameter Description

| Parameter Name | Type   | Required | Description |
|---------------|--------|----------|-------------|
| `doc_id`      | `int`  | Yes      | The document ID of the research report, obtained from the `docId` field in the result returned by `search_reports`. |

---

### 📥 Usage Example

```python

# Get the content of this report

content = await get_report_content(doc_id)

```
## Server Configuration:
```json
{
  "mcpServers": {
    "fxbaogao-mcp": {
      "args": [
        "fxbaogao-mcp@latest"
      ],
      "command": "uvx"
    }
  }
}
```
## Notes
This tool is intended for educational and research purposes only. Do not use it for commercial purposes.
Please comply with the terms of use and relevant laws and regulations of Discovery Report.

**Official site: ** [https://www.fxbaogao.com/](https://www.fxbaogao.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `finance`, `data`
- Tags: `finance`, `research and data`, `search`, `研究报告`, `行业报告`, `咨询管理`, `产业研究`, `投资分析`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `fxbaogao-mcp@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/haymai-fxbaogao.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
