---
title: "Agentic_Document_Processing_MCP"
description: "About ADP MCP Server ADP MCP Server is the Model Context Protocol server for Laiye Technology's Agentic Document Processing (ADP) product, enabling any AI client that supports the MCP protocol (such a…"
---

# Agentic_Document_Processing_MCP

About ADP MCP Server ADP MCP Server is the Model Context Protocol server for Laiye Technology's Agentic Document Processing (ADP) product, enabling any AI client that supports the MCP protocol (such a…

## About ADP MCP Server

ADP MCP Server is the Model Context Protocol server for Laiye Technology's **Agentic Document Processing (ADP)** product, enabling any AI client that supports the MCP protocol (such as Claude Desktop, Cursor, Copilot Chat, Tongyi Lingma, Coze, etc.) to invoke ADP's document parsing and extraction capabilities without writing any code. Unlike CLI tools, the MCP Server operates via **Streamable HTTP** transmission, allowing all available tools to be discovered, invoked, and queried for results—all within a single connection and entirely through the conversation window.

The ADP product deeply integrates Visual-Language Models (VLM), Large Language Models (LLM), and agent-based autonomous decision-making technologies, completely revolutionizing traditional document processing methods. It upgrades the long-standing, rule-driven mechanical field extraction to a goal-driven, fully intelligent and automated process. The product focuses on the intelligent processing of various business documents, automatically classifying and accurately extracting key fields from overseas invoices, domestic bills, procurement contracts, logistics documents, financial statements, transaction contracts, and more. It also supports table parsing, content verification, and multilingual recognition, eliminating the need for manual template creation, data annotation, and rule maintenance, thus efficiently handling large volumes of documents.

---

## Quick Integration

### 1. Obtain API Key

Visit [https://adp.laiye.com/](https://adp.laiye.com/ to register for an ADP account and copy your unique API Key.

### 2. Configure MCP Client

#### Method One: Visual Interface Configuration (Recommended)

Most MCP clients (Cursor, Tongyi Lingma, Coze, etc.) support adding MCP services directly through their settings interface. For example, using Cursor:

1. Open **Settings → MCP**
2. Click **Add new MCP server**
3. Fill in the following information:
   - **Name**: `ADP` (custom name)
   - **Type**: `streamable-http`
   - **URL**: `https://adp.laiye.com/mcp?key=`
4. Save the configuration, and you can now use ADP tools in the conversation.

#### Method Two: Edit Configuration File

For example, with Claude Desktop, add the following to the `claude_desktop_config.json` file:

json
{
  "mcpServers": {
    "adp": {
      "url": "https://adp.laiye.com/mcp?key=",
      "transport": "streamable-http"
    }
  }
}

The configuration method for other clients is similar, with the core parameters being:

| Parameter | Value |
|-----------|-------|
| **Endpoint** | `https://adp.laiye.com/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication Method** | URL Query `?key=` |

> For private deployment environments, replace the domain with the actual service address.

### 3. Start Using

Once connected, the AI client will automatically discover all available ADP tools. Simply describe your needs in the conversation, such as:

- "Help me parse the structure of this PDF"
- "Extract the information from this ID card"
- "Extract the amount and date from this invoice"

---

## Tool List

### Document Parsing

| Tool Name | Title | Description |
|-----------|-------|-------------|
| `parse_document` | General Document Parsing | Parses the layout of PDFs, images, Word, Excel, PPT, and other documents, returning structured text blocks, tables, reading order, and page coordinates. Suitable for scenarios where the document type is uncertain and the original structure needs to be obtained before further processing. If the document is confirmed to be an invoice, ID, or other specific type, please use the corresponding dedicated extraction tool first. |

### Invoice and Order Extraction

| Tool Name | Title | Description |
|-----------|-------|-------------|
| `extract_china_invoice` | Chinese Invoices | Covers over 30 common types of invoices in China: supports electronic invoices, general invoices, special invoices, taxi receipts, train tickets, flight itineraries, fiscal invoices, and other common financial documents. Extracts key information such as invoice number, issue date, amount, buyer, seller, and also supports verifying the authenticity of invoices. |
| `extract_global_invoice` | Overseas Invoices/Receipts | Extracts key fields (invoice number, issue date, amount, tax, currency, line items, etc.) from PDF or image formats of overseas invoices, receipts, and bills. Suitable for cross-border trade, expense reimbursement, and accounts payable automation. For VAT invoices in mainland China, please use the dedicated domestic invoice tool. || `extract_purchase_order` | Order | Extracts key fields (order number, buyer and seller information, order date, item details, quantity, unit price, total amount, delivery address, etc.) from purchase orders or sales orders in PDF or image format. Suitable for e-commerce order entry, supply chain reconciliation, and automation of warehouse management scenarios. |

### Card and Certificate Extraction

| Tool Name | Title | Description |
|-----------|-------|-------------|
| `extract_id_card` | ID Card | Extracts key fields (name, gender, ethnicity, date of birth, ID number, address, issuing authority, validity period, etc.) from images of Chinese resident ID cards, supporting both front and back recognition. Suitable for real-name authentication, user registration, and other scenarios. |
| `extract_bank_card` | Bank Card | Extracts key fields (card number, issuing bank, card type, validity period, etc.) from the front image of a bank card. Suitable for card binding, payment account entry, and payment channel configuration scenarios. Note: Only public information on the card surface is recognized; sensitive fields such as CVV are not involved. |
| `extract_vehicle_cert` | Vehicle Compliance Certificate | Extracts key fields (certificate number, vehicle brand, model, vehicle identification number VIN, engine number, manufacturing date, etc.) from images of motor vehicle compliance certificates. Suitable for vehicle registration, used car transactions, and vehicle asset management scenarios. |
| `extract_account_permit` | Account Opening Permit | Extracts key fields (company name, basic account number, opening bank, approval number, issue date, etc.) from images of corporate account opening permits. Suitable for corporate collection account verification, financial review, and payee information verification in accounts payable scenarios. |
| `extract_driver_license` | Driver's License | Extracts key fields (name, gender, nationality, date of birth, driver's license number, authorized vehicle types, initial issuance date, validity period, etc.) from images of Chinese motor vehicle driver's licenses, supporting both main and supplementary page recognition. Suitable for driver qualification verification, ride-hailing/freight driver admission review, and other scenarios. |
| `extract_business_license` | Business License | Extracts key fields (company name, unified social credit code, legal representative, registered capital, establishment date, business scope, registered address, etc.) from images of Chinese business licenses. Suitable for corporate account opening, merchant onboarding, supplier qualification review, and corporate real-name authentication scenarios. |
| `extract_passport_cn` | Passport - China | Extracts key fields (Chinese name, name in Pinyin, gender, date of birth, passport number, nationality, issue date, validity period, issuing authority, etc.) from images of People's Republic of China passports. Suitable for outbound services, cross-border identity verification, visa application, and other scenarios; foreign passports are not supported. |
| `extract_vehicle_license` | Vehicle Registration Certificate | Extracts key fields (license plate number, vehicle type, owner, vehicle identification number VIN, engine number, registration date, issue date, etc.) from images of Chinese motor vehicle registration certificates, supporting both main and supplementary page recognition. Suitable for vehicle registration, insurance application, and ride-hailing/freight vehicle admission scenarios. |
| `extract_org_code_cert` | Organization Code Certificate | Extracts key fields (organization name, organization code, legal representative, address, issue date, validity period, etc.) from images of organization code certificates. Suitable for historical archive digitization and existing enterprise qualification verification; new enterprises are advised to use the business license tool. |
| `extract_household_book` | Household Register | Extracts key fields (household number, household type, address, list of family members, including member names, ID numbers, relationship with the head of household, etc.) from images of Chinese household registers, supporting both the first page and individual pages. Suitable for household registration verification, kinship certification, and social security services. |
| `extract_hk_macao_permit` | Hong Kong/Macau Permit | Extracts key fields (name, gender, date of birth, document number, issue date, validity period, issuing authority, etc.) from images of Hong Kong/Macau travel permits. Suitable for entry and exit services, hotel check-in, and ticketing real-name scenarios. |

### Custom Extraction

In addition to the out-of-the-box tools mentioned above, MCP provides two fixed tools for using custom extraction applications you create on the ADP platform:

| Tool Name | Title | Description |
|-----------|-------|-------------|| `list_custom_extract_apps` | List Custom Extraction Apps | Lists all custom document extraction applications created by the current user, returning each application's ID, name, description, tags, and output field definitions. Can be used to find the `app_id` required for `execute_custom_extract_app`. |
| `execute_custom_extract_app` | Execute Custom Extraction App | Processes a file using the specified custom document extraction application. You need to first obtain an available `app_id` via `list_custom_extract_apps`. |

**Usage Flow:** First, call `list_custom_extract_apps` to view the list of available applications and get the target `app_id`, then call `execute_custom_extract_app` passing in the `app_id` and the file for extraction.

---

## Tool Input Parameters

### Document Parsing and OOTB Extraction Tools

All out-of-the-box tools share a unified input schema:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | string | Yes | File URL or Base64 encoded content |
| `file_name` | string | No | File name (including extension) |
| `with_rec_result` | boolean | No | Whether to include OCR intermediate results, default `true` |
| `wait` | boolean | No | Whether to synchronously wait for the result, default `true` |
| `timeout_seconds` | integer | No | Synchronous waiting timeout in seconds, default `300`, range 1–900 |

### execute_custom_extract_app

In addition to the above parameters, it includes:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `app_id` | string | Yes | Custom extraction application ID (obtained through `list_custom_extract_apps`) |

### list_custom_extract_apps

No input parameters are required.

**File Input Methods:**

- **URL**: Pass a URL starting with `http://`, `https://`, or `file://` into `file`
- **Base64**: Pass Base64 encoded file content into `file` (automatically recognized if not in URL format)

**Synchronous vs Asynchronous:**

- `wait=true` (default): Blocks until processing is complete, returns the result directly
- `wait=false`: Returns `task_id` immediately, status can be queried later

---

## Tool Output

### parse_document Output

json
{
  "task_id": "fabd7f0a4e7211f1bbc4d85ed35661fd",
  "status": 4,
  "message": "",
  "doc_recognize_result": [
    {
      "page_num": 1,
      "document_content": "Full text content of this page...",
      "document_details": [
        {
          "type": "Text",
          "text": "Paragraph content...",
          "position": [{"points": [{"x": 311, "y": 50}, {"x": 500, "y": 50}, {"x": 500, "y": 80}, {"x": 311, "y": 80}]}],
          "ocr_confidence": {
            "ocr_mean_confidence": 0.999,
            "ocr_min_confidence": 0.998,
            "is_overall_confidence": 1
          }
        },
        {
          "type": "Table",
          "text": "Column A\tColumn B\nValue 1\tValue 2",
          "position": [{"points": [...]}],
          "ocr_confidence": {...}
        },
        {
          "type": "Picture",
          "text": "https://adp.laiye.com/web/.../file/abc123",
          "position": [{"points": [...]}],
          "ocr_confidence": {...}
        }
      ]
    }
  ]
}

| Field | Type | Description |
|-------|------|-------------|
| `task_id` | string | Task ID |
| `status` | integer | Task status code |
| `message` | string | Status message |
| `doc_recognize_result` | array | Recognition results for each page |
| `doc_recognize_result[].page_num` | integer | Page number (starts from 1) |
| `doc_recognize_result[].document_content` | string | Full text of the page (in reading order) |
| `doc_recognize_result[].document_details` | array | Element-level details |
| `document_details[].type` | string | Element type: `Text`, `Table`, `Picture` |
| `document_details[].text` | string | Text content; for `Picture` type, it is the image URL |
| `document_details[].position` | array | Bounding box coordinates (4 corner points) |
| `document_details[].ocr_confidence.ocr_mean_confidence` | float | Average OCR confidence (0–1) |
| `document_details[].ocr_confidence.ocr_min_confidence` | float | Minimum OCR confidence (0–1) |

### extract Tool Output

json
{
  "task_id": "91283e544e7111f18cd6d85ed35661fd",
  "status": 4,
  "message": "",
  "extraction_result": [
    {
      "field_key": "invoice_number",
      "field_name": "发票号码",
      "field_values": [
        {
          "field_value": "24VLT0591617",
          "field_confidence": 1.0,
          "references": []
        }
      ]
    },
    {
      "field_key": "line_items",
      "field_name": "商品明细",
      "references": [],
      "field_confidence": 1.0,
      "table_values": [
        [
          {
            "field_name": "商品名称",
            "field_key": "line_items_description",
            "field_values": [
              {
                "field_value": "TESLA MODEL 3",
                "field_confidence": 1.0,
                "references": "Description: TESLA MODEL 3"
              }
            ]
          }
        ]
      ]
    }
  ]
}**Regular Fields** (without `table_values`):

| Field | Type | Description |
|-------|------|-------------|
| `field_key` | string | Field identifier |
| `field_name` | string | Field name |
| `field_values` | array | List of extracted values |
| `field_values[].field_value` | string | Extracted value |
| `field_values[].field_confidence` | float | Confidence (0–1) |

**Table Fields** (with `table_values`):

| Field | Type | Description |
|-------|------|-------------|
| `field_key` | string | Table identifier |
| `field_name` | string | Table name |
| `table_values` | array[array] | 2D array: each row is an array of cells, each cell contains `field_name`, `field_key`, and `field_values` |

**Determination Method:** If the field object contains `table_values` → Table field; if it only contains `field_values` → Regular field.

### Asynchronous Response (`wait=false`)

json
{
  "task_id": "fabd7f0a4e7211f1bbc4d85ed35661fd",
  "status": "running"
}

---

## Task Status Codes

| Status Code | MCP Status | Description |
|-------------|------------|-------------|
| 0 | running | Unknown |
| 1 | running | Ready/Queued |
| 2 | running | Processing |
| 4 | success | Success |
| 5 | failed | Failed |
| 6 | failed | Canceled |

---

## Supported File Formats

| Format | Extensions | Description |
|--------|------------|-------------|
| PDF | `.pdf` | Supports scanned and electronic versions |
| Images | `.jpg` `.jpeg` `.png` `.bmp` `.tiff` `.webp` | Supports mobile phone captures |
| Word | `.doc` `.docx` | - |
| Excel | `.xls` `.xlsx` | - |
| PPT | `.ppt` `.pptx` | - |

---

## Authentication Instructions

ADP MCP Server uses API Key authentication, passed through URL Query parameters:

https://adp.laiye.com/mcp?key=

- The API Key can be obtained from the ADP Console on the "My MCP" page.
- Each API Key is bound to a user and can only access applications and data under that user.
- The API Key will not appear in the request body or response, and is used solely for authentication.

---

## Frequently Asked Questions

**Q: Why can't I see certain card tools after connecting to MCP?**

A: The tool list is dynamically generated based on the current user's initialized applications. When connecting for the first time, the system automatically initializes all out-of-the-box applications. After initialization, refresh the tool list to see all tools.

**Q: Why does the card tool return "Document extraction failed"?**

A: Please ensure that the uploaded file matches the tool type (e.g., use `extract_id_card` for ID card images, not `extract_vehicle_cert`). The file format must be one of the supported image or PDF formats.

**Q: How to handle timeouts?**

A: The default timeout is 300 seconds (5 minutes), which can be adjusted using the `timeout_seconds` parameter (maximum 900 seconds). For large files or complex documents, it is recommended to use the asynchronous mode with `wait=false` and then query the result using the `task_id`.

**Q: What are the differences between ADP CLI / OpenAPI?**

A: All three have equivalent functionality, differing only in the method of integration:

| Integration Method | Suitable Scenarios |
|--------------------|--------------------|
| **MCP Server** | Direct calls from AI clients (Claude Desktop, Cursor, etc.) without coding |
| **ADP CLI** | Terminal command line, script automation, AI Skill integration |
| **OpenAPI** | Business system integration, backend service calls |

---

## Licensing

- **MCP Server**: Free to connect, provided as part of the ADP product.
- **ADP Service**: Public cloud-based AI document processing service, billed based on usage.

Free Quota: New users receive **100 free credits** per month after registration.

[Experience Now](https://adp.laiye.com/)

---

## Support and Contact

- **API Documentation:** [Open API User Guide](https://laiye-tech.feishu.cn/wiki/PO9Jw4cH3iV2ThkMPW2c539pnkc)
- **ADP Product Manual:** [Public Cloud Operation Manual](https://laiye-tech.feishu.cn/wiki/UDYIwG42pisBbFkJI39ctpeKnWh)
- **Email:** mkt@laiye.com
- **Website:** [Laiye Technology](https://laiye.com/product/adp-platform)

**Building the Future of Intelligent Agents with ❤️**
Copyright © 2026 [Laiye Technology (Beijing) Co., Ltd.] All rights reserved.

**Official site: ** [https://github.com/Laiye-ADP/adp-mcp](https://github.com/Laiye-ADP/adp-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `development`, `memory`, `communication`
- Tags: `communication`, `knowledge and memory`, `developer tools`, `文档解析`, `文档识别`, `文档抽取`, `ocr`, `数据录入`, `chinese`

## MCP Configuration

- Transport: `http`
- Command: ``
- Args: none

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/laiyelijingao-agentic-document-processing.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
