---
title: "InvoiceLLMMCP"
description: "InvoiceLLM is an intelligent invoice recognition agent that uses advanced OCR technology and local large models to extract structured information from invoice documents. The system supports image and…"
---

# InvoiceLLMMCP

InvoiceLLM is an intelligent invoice recognition agent that uses advanced OCR technology and local large models to extract structured information from invoice documents. The system supports image and…

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

# InvoiceLLM - Intelligent Invoice Recognition Agent

## Project Introduction
InvoiceLLM is an intelligent invoice recognition agent that uses advanced OCR technology and a local large model to extract structured information from invoice documents. The system supports image and PDF formats, providing a privacy-focused solution for handling sensitive financial documents.

## Features
- **Multi-format support**: handles image files (JPG, PNG, etc.) and PDF documents
- **Advanced OCR technology**: uses PaddleOCR for accurate text extraction
- **AI-driven analysis**: leverages the local large model (Qwen3-0.6B) for intelligent field extraction
- **Privacy protection**: all processing happens locally, keeping sensitive invoice data secure
- **Comprehensive field extraction**: extracts key invoice information, including:
  - General fields: invoice number, invoice code, issue date, amount, tax amount
  - Buyer and seller info: company details, taxpayer ID, address, phone, bank account
  - Item info: product name, specification/model, quantity, unit price, tax rate
  - Other info: payee, reviewer, issuer

## Technical Architecture
1. **Document processing**:
   - Images: OCR processing with PaddleOCR
   - PDF: direct text extraction with PyMuPDF

2. **Information extraction**:
   - Local large model (Qwen3-0.6B) for intelligent field parsing
   - Advanced validation and correction algorithms

3. **User interface**:
   - Gradio-based web interface
   - Real-time processing and visualization

## Usage
1. Upload an invoice file (image or PDF)
2. Click submit to process the invoice
3. View the extracted structured information in JSON format

## Deployment Guide

### Requirements
- Python 3.8 or higher
- OS: Linux, macOS, or Windows
- At least 4GB RAM (8GB or more recommended)
- At least 2GB free disk space (for model files)

### Installation steps

1. **Clone the project**
```bash
   git clone https://www.modelscope.cn/studios/megemini/InvoiceLLM.git
   cd InvoiceLLM
```

2. **Create a virtual environment (recommended)**
```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Download the model files**
   - The Qwen3-0.6B model will be downloaded automatically on first run
   - Or download it manually and place it in the model directory

### Running the app

1. **Start the web interface**
```bash
   python app.py
```

2. **Access the app**
   - Open your browser and visit `http://127.0.0.1:7860`
   - Or use the local link provided by Gradio

3. **Use as an MCP Server**
   - After the app starts, the MCP Server runs automatically
   - Streamable HTTP URL: `http://127.0.0.1:7860/gradio_api/mcp/`
   - SSE URL: `http://127.0.0.1:7860/gradio_api/mcp/sse`

## Usage Examples

### Example 1: Processing an image invoice

1. Click the "Choose File" button to upload an invoice image (JPG, PNG, etc.)
2. Click the "Start Recognition" button
3. View the recognition results:
   - The left side shows the OCR visualization
   - The right side shows the extracted structured JSON data

### Example 2: Processing a PDF invoice

1. Upload an invoice file in PDF format
2. Click the "Start Recognition" button
3. The system automatically extracts the text from the PDF and parses it with the AI model
4. View the extracted invoice information

### Example 3: Using the sample files

1. In the "Examples" section at the bottom of the page, click any sample invoice image
2. Or click the "Process Example" button
3. The system automatically processes the sample file and shows the results

## Dependencies
- PaddleOCR: OCR engine for image processing
- PyMuPDF: PDF text extraction
- Qwen3-0.6B: local large language model
- Gradio: web interface framework
- PIL: image processing
- PyTorch: model inference backend

## License
Apache License 2.0

**Official site: ** [https://megemini-invoicellm.ms.show/gradio_api/mcp/](https://megemini-invoicellm.ms.show/gradio_api/mcp/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `办公自动化`, `发票识别`, `ocr`, `llm`, `本地大模型`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/megemini-invoicellmmcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
