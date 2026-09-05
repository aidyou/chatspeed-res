---
title: "usensedata-mcp-server-query-china-company"
description: "Yushan Data API service is now fully compatible with the MCP protocol, creating a data service MCP Server. The usensedata-mcp-server-query-china-company project serves as a server for enterprise data…"
---

# usensedata-mcp-server-query-china-company

Yushan Data API service is now fully compatible with the MCP protocol, creating a data service MCP Server. The usensedata-mcp-server-query-china-company project serves as a server for enterprise data…

## Introduction
The Yushan Data API service is now fully compatible with the MCP protocol, creating a data service MCP Server. The usensedata-mcp-server-query-china-company project serves as a server for enterprise data query services. Users can quickly access Yushan Data's enterprise data services via LLM through simple configuration. Built on the MCP TypeScript SDK, it can be quickly integrated into MCP-protocol-supporting agent assistants.

## Tool List

### 1. `verify_company_name_and_president`
**Introduction**: verifies whether the legal representative's name matches the company name. Returns 0 if they match, and 1 if they do not.
**Parameters**:
- `operName`: name of the legal representative
- `entName`: full company name

---

### 2. `fuzzy_query_company`
**Introduction**: fuzzy query of company information by company-name keyword.
**Parameters**:
- `keyWord`: company name keyword

---

### 3. `query_company_basic_info`
**Introduction**: queries basic enterprise information (legal representative, registered capital, unified social credit code, etc.) by full company name.
**Parameters**:
- `entname`: full company name

---

### 4. `query_company_overseas_investments`
**Introduction**: queries an enterprise's external investment information, such as investment amount, shareholding ratio, and shareholder type.
**Parameters**:
- `entName`: full company name

---

### 5. `query_company_change_records`
**Introduction**: queries an enterprise's change records by full company name.
**Parameters**:
- `entName`: full company name

---

### 6. `query_company_software_copyright_info`
**Introduction**: queries an enterprise's software copyright registration information by full company name.
**Parameters**:
- `entName`: full company name

---

### 7. `query_company_trademark_list`
**Introduction**: queries an enterprise's trademark list information, including trademark names, enterprise names, and status.
**Parameters**:
- `entName`: full company name

---

### 8. `query_company_court_litigation_related_info`
**Introduction**: queries court-related litigation information for a company.
**Parameters**:
- `name`: full company name

---

### 9. `query_company_abnormal_business_operation`
**Introduction**: queries an enterprise's abnormal business operation information by full company name.
**Parameters**:
- `keyWord`: full company name

## Environment

### Getting the Usense UserID and Key
Contact [Yushan Data](https://www.yushanshuju.com/) to get the user account and key

### Installing node.js
The installation is successful when you can get the version number in the terminal; on mac, install it with brew
```
node -v
npm -v
```

### Installing dependencies
```
npm install
```

### TypeScript packaging
```
npm run build
```

### Updating the version
First log in to the npm account; the version number must be updated in package.json
```
npm login
npm publish --access public
```

### Configuring the MCP server config
macos/linux
```
"mcpServers": {
  "usense-corp": {
    "command": "npx",
    "args": [
      "-y",
      "usensedata-mcp-server-query-china-company"
    ],
    "env": {
      "USENSEDATA_API_KEY": "your_api_key",
      "USENSEDATA_API_USERID": "your_api_userid"
    }
  }
}
```
windows
```
"mcpServers": {
  "usense-corp": {
    "command": "cmd",
    "args": [
      "/c",
      "npx",
      "-y",
      "usensedata-mcp-server-query-china-company"
    ],
    "env": {
      "USENSEDATA_API_KEY": "your_api_key",
      "USENSEDATA_API_USERID": "your_api_userid"
    }
  }
}
```

#### Effect
Actual user request: **"Help me check the external investment situation of Yushan Data"**

## Explanation
1. Get the company name to be queried from the actual request: "Yushan Data"

2. Call the enterprise fuzzy query [fuzzy_query_of_enterprises] to get the list of enterprises related to "Yushan Data", and get the full company name from it.

3. Then call the external investment query [query_company_overseas_investments] to get the company's investment information.

4. Then call the basic enterprise info query [query_basic_enterprise_information] to get the company's basic information.

5. Finally, organize all of the above information and output the final result.

#### Agent result

#### MCP tools loading

**Official site: ** [https://github.com/usensedata/usensedata-mcp-server-query-china-company](https://github.com/usensedata/usensedata-mcp-server-query-china-company)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `企业数据`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y usensedata-mcp-server-query-china-company`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/steven233-usensedata-query-china-company.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
