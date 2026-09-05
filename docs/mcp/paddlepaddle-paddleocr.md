---
title: "PaddleOCR"
description: "PaddleOCR MCP Server Overview The PaddleOCR MCP Server provides industrial-grade OCR and document parsing capabilities for AI applications. Based on PaddleOCR, a mature solution verified by over 50,00…"
---

# PaddleOCR

PaddleOCR MCP Server Overview The PaddleOCR MCP Server provides industrial-grade OCR and document parsing capabilities for AI applications. Based on PaddleOCR, a mature solution verified by over 50,00…

# PaddleOCR MCP Server
## Overview
The PaddleOCR MCP Server provides industrial-grade OCR and document parsing capabilities for AI applications. Based on PaddleOCR, a mature solution verified by over 50,000 GitHub stars and deeply integrated into leading projects such as MinerU, RAGFlow, and OmniParser, it has been specifically optimized following the MCP philosophy.

* **Official Documentation**: [https://paddlepaddle.github.io/PaddleOCR/latest/version3.x/deployment/mcp_server.html](https://paddlepaddle.github.io/PaddleOCR/latest/version3.x/deployment/mcp_server.html)
* **PaddleOCR GitHub Repository**: [https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
* **Online Experience of PaddleOCR Production Features:**
    * [PaddleOCR Official Website](https://aistudio.baidu.com/paddleocr)

    * ModelScope Community
        * [PP-OCRv5](https://modelscope.cn/studios/PaddlePaddle/PP-OCRv5_Online_Demo)
        * [PP-StructureV3](https://modelscope.cn/studios/PaddlePaddle/PP-StructureV3_Online_Demo)
        * [PaddleOCR-VL](https://modelscope.cn/studios/PaddlePaddle/PaddleOCR-VL_Online_Demo)

## Core Features
### Text Recognition (Based on PP-OCRv5)
* **Multi-language Support**: Supports 37 languages including Chinese, English, Japanese, and Korean, with support for printed and handwritten text recognition.
* **High-accuracy Recognition**: Achieves leading accuracy levels among open-source solutions.
* **Structured Output**: Returns JSON data containing text coordinates and content.

### Document Parsing (Based on PP-StructureV3) & Large Model Document Parsing (Based on PaddleOCR-VL)
* **Intelligent Layout Analysis**: Identifies layout elements such as text blocks, headings, paragraphs, images, and tables.
* **Structured Conversion**: Converts PDFs and images into Markdown format while preserving the original structure.
* **Complex Document Handling**: Processes documents containing complex tables, formulas, and handwritten text.

### MCP Optimizations
* **Smart Output Modes**:
    * `simple` mode includes key information such as recognized text/Markdown content.
    * `detailed` mode includes detailed information such as bounding box coordinates.

* **PP-OCRv5**: Both output modes include confidence scores and statistical information to help agents assess the quality of the results.
* **PP-StructureV3 and PaddleOCR-VL**: Both output modes support mixed text and image output, preserving the original position of images.

## Deployment Modes
### Operation Modes
* **Local Python Library**: Run PaddleOCR models directly on your local machine.
* **PaddleOCR Official Service**: Call the cloud services provided by the PaddleOCR official website.
* **Self-hosted Service**: Connect to a self-hosted PaddleOCR service.

### Transmission Mechanisms
* **stdio**: Standard input/output mode suitable for local integration.
* **Streamable HTTP**: Supports remote invocation via streamable HTTP transmission.

## Deploying Remote Services on ModelScope
1. On the [PaddleOCR Official Website](https://aistudio.baidu.com/paddleocr/task), click "API" in the top left corner. In the code example for the desired feature, copy the base service URL (`API_URL` without `/ocr` or other endpoint suffixes) and the access token (`TOKEN`).
2. On the right side of this page, configure `PADDLEOCR_MCP_AISTUDIO_ACCESS_TOKEN` and `PADDLEOCR_MCP_SERVER_URL`, setting them to the access token and base service URL obtained in the previous step, respectively. Set `PADDLEOCR_MCP_PIPELINE` to the pipeline name (`OCR`, `PP-StructureV3`, or `PaddleOCR-VL`):

    | Feature | `PADDLEOCR_MCP_PIPELINE` |
    | - | - |
    | Text Recognition (PP-OCRv5) | `OCR` |
    | Document Parsing (PP-StructureV3) | `PP-StructureV3` |
    | Large Model Document Parsing (PaddleOCR-VL) | `PaddleOCR-VL` |

3. Click "Connect" to start the service, which can then be used in MCP hosts like Claude for Desktop and Cherry Studio.

## Typical Application Scenarios
### Document Digitization
* Extract the content of handwritten notes and store it in note-taking software.
* Convert image/PDF documents into editable Word/Excel formats.

### Development Workflow
* Convert handwritten ideas/pseudo-code into executable scripts.
* Quickly convert document images into Markdown-formatted project documentation.

## Technical Advantages
* **Mature and Stable**: An industrial-grade OCR solution validated in numerous production environments.
* **Leading Accuracy**: Surpasses many commercial solutions in public evaluations for OCR and document parsing.
* **Easy Integration**: Simple deployment steps, with integration completed in minutes.
* **Cost-effective**: Supports local deployment, avoiding data transfer and API call costs.

---

**Start using the PaddleOCR MCP Server to give your AI applications industrial-grade document understanding capabilities.**

**Official site: ** [https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`
- Tags: `developer tools`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `--from paddleocr-mcp paddleocr_mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/paddlepaddle-paddleocr.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
