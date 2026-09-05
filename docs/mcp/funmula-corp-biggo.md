---
title: "BigGo-MCP-Server"
description: "A server that enables searching products across multiple e-commerce platforms, tracking price history, and comparing product specifications using BigGo's price comparison APIs."
---

# BigGo-MCP-Server

A server that enables searching products across multiple e-commerce platforms, tracking price history, and comparing product specifications using BigGo's price comparison APIs.

# BigGo MCP Server
![PyPI - Python Version](/mcp-assets/258e22dc90f89c4f02fa44bf71fd6b43.svg)
[![PyPI - Version](/mcp-assets/06285530e460209b944272ca02a84852.svg)](https://pypi.org/project/BigGo-MCP-Server/)
![PyPI - License](/mcp-assets/eb08a39e4af3626c2d0c50dd4a992374.svg)

## Introduction
BigGo MCP Server utilizes APIs from BigGo, a professional price comparison website.
## Features
> Supports `stdio` and `SSE` transports

- **Product Discovery**: Search for products across multiple e-commerce platforms (Amazon, Aliexpress, Ebay, Taobao, Shopee ... etc.)
- **Price History Tracking**: Track product price history by supplying product url or related terms.
- **Spec Comparison [Disabled on versions >= v0.1.28]**: Compare and find products based on their specifications, from basic infos to more complex technical specs.

## Installation
### Prerequisites
1. Python >= 3.10
2. [uvx package manager ( Included with uv )](https://docs.astral.sh/uv/getting-started/installation/)
3. BigGo Certification (`client_id` and `client_secret`) for specification search. 

#### How to obtain BigGo certification?
  - [Register](https://account.biggo.com/?url=https%3A%2F%2Fbiggo.com%2F&lang=en&source=web&type=biggo3&method=register) a BigGo account if you don't have one.
  - Go to [BigGo Certification Page](https://account.biggo.com/setting/token)
  - Click "Generate certification" button
  - 
  - Copy the `client_id` and `client_secret`
  - Use them in the MCP Server configuration (`BIGGO_MCP_SERVER_CLIENT_ID` and `BIGGO_MCP_SERVER_CLIENT_SECRET`)

### Installation Config
```json
{
  "mcpServers": {
    "biggo-mcp-server": {
      "command": "uvx",
      "args": [ "BigGo-MCP-Server@latest"],
      "env": {
        "BIGGO_MCP_SERVER_CLIENT_ID": "CLIENT_ID",
        "BIGGO_MCP_SERVER_CLIENT_SECRET": "CLIENT_SECRET",
        "BIGGO_MCP_SERVER_REGION": "REGION"
      }
    }
  }
}
```
> For specific version use `BigGo-MCP-Server@VERSION`, ex: `BigGo-MCP-Server@0.1.1`

## Environment Variables
| Variable                         | Description               | Default | Choices                                    |
| -------------------------------- | ------------------------- | ------- | ------------------------------------------ |
| `BIGGO_MCP_SERVER_CLIENT_ID`     | Client ID                 | None    | Required for specification search          |
| `BIGGO_MCP_SERVER_CLIENT_SECRET` | Client Secret             | None    | Required for specification search          |
| `BIGGO_MCP_SERVER_REGION`        | Region for product search | TW      | US, TW, JP, HK, SG, MY, IN, PH, TH, VN, ID |
| `BIGGO_MCP_SERVER_SSE_PORT`      | Port for SSE server       | 9876    | Any available port number                  |
| `BIGGO_MCP_SERVER_SERVER_TYPE`   | Server transport type     | stdio   | stdio, sse                                 |

> Default SSE URL: http://localhost:9876/sse

## Available Tools
- `product_search`: Product search with BigGo search api
- `price_history_graph`: Link that visualizes product price history
- `price_history_with_history_id`: Uses history IDs from product search results
- `price_history_with_url`: Tracks price history using product URLs
- `spec_indexes`: Lists available Elasticsearch indexes for product specifications
- `spec_mapping`: Shows Elasticsearch index mapping with example documents
- `spec_search`: Query product specifications from Elasticsearch
- `get_current_region`: Get the current region

## FAQ
### How to trigger tool usage?
For **Product Discovery** related:
```
Look for Nike running shoes
```
For **Price History Tracking** related:
```
Show me the price history of this product: https://some-product-url
```
For **Spec Comparison** related:
```
Find me phones with 16GB RAM and 1TB storage
```
```
Please show me diving watches that can withstand the most water pressure
```

## Build
See [build.md](https://github.com/funmula-corp/biggo-mcp-server/blob/HEAD/docs/build.md) for more details.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/funmula-corp/biggo-mcp-server/blob/HEAD/LICENSE) file for details.

**Official site: ** [https://github.com/funmula-corp/biggo-mcp-server](https://github.com/funmula-corp/biggo-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`
- Tags: `ecommerce and retail`, `search`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `BigGo-MCP-Server@latest`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/funmula-corp-biggo.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
