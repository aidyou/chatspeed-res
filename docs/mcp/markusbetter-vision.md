---
title: "vision-mcp-server"
description: "An MCP (Model Context Protocol) server for image analysis, supporting image content analysis and description. For example, when the client model only supports text input, you can use this vision MCP t…"
---

# vision-mcp-server

An MCP (Model Context Protocol) server for image analysis, supporting image content analysis and description. For example, when the client model only supports text input, you can use this vision MCP t…

# Vision MCP Server | Visual Analysis MCP Server

## Version 1.1 of this project has been released, supporting the addition of multiple visual model providers and fallback models.

## Chinese

This is a local MCP Server that analyzes images through visual models.

For example, if the primary model you use on the client side only supports text input, you can add this MCP to your Agent tool, and have the `analyze_image` tool call an independent visual model to complete image understanding.

v1.1 supports:

- ModelScope, Zhipu BigModel, and other OpenAI Chat Completions compatible visual interfaces
- Configuring multiple models under the same API Key and falling back in order
- Cross-provider fallback
- Automatic rotation, format validation, and proportional scaling of images, with the default longest side being 2048
- Local directory restrictions, download limits, log desensitization, and online image SSRF protection

***Please keep your API Key secure and do not publicly share MCP configurations containing real keys.

Choose one of the following four configuration methods.

## Please note that if you have already installed this project, it is recommended to clear the cache of the previously installed package, or during installation, change
 "args": ["-y", "vision-mcp-server"]
 to
  "args": ["-y", "vision-mcp-server@latest"]
If you are unsure how to do this, you can ask the AI in your agent for help.

## Method One: ModelScope, Multiple Models with One Key

Suitable for users who only use ModelScope API-Inference.

json
{
  "mcpServers": {
    "vision-mcp-server": {
      "command": "npx",
      "args": ["-y", "vision-mcp-server"],
      "env": {
        "MODELSCOPE_TOKEN": "your_modelscope_token",
        "MODELSCOPE_MODELS": "Qwen/Qwen3.5-397B-A17B,Qwen/Qwen3.5-35B-A3B"
      }
    }
  }
}

`MODELSCOPE_MODELS` is an ordered list separated by commas:

1. First, call `Qwen/Qwen3.5-397B-A17B`.
2. If it returns rate limiting, timeout, or server error, call the next model.
3. All models share the same `MODELSCOPE_TOKEN`.

Please confirm that the models you list currently support ModelScope API-Inference and image input. The available models on ModelScope may change, and this project does not restrict specific Model IDs.

The old single-model configuration is still compatible:

json
{
  "MODELSCOPE_TOKEN": "your_modelscope_token",
  "MODELSCOPE_MODEL": "Qwen/Qwen3.5-397B-A17B"
}

If both `MODELSCOPE_MODELS` and `MODELSCOPE_MODEL` are set, `MODELSCOPE_MODELS` takes precedence.

## Method Two: Zhipu, Any Visual Model with One Key

Zhipu mode does not hard-code models. Users must explicitly specify the visual models they have permission to use via `VISION_MODELS`:

json
{
  "mcpServers": {
    "vision-mcp-server": {
      "command": "npx",
      "args": ["-y", "vision-mcp-server"],
      "env": {
        "VISION_PROVIDER": "zhipu",
        "ZAI_API_KEY": "your_zhipu_api_key",
        "VISION_MODELS": "glm-4v-flash"
      }
    }
  }
}

The default example uses only the free `glm-4v-flash`. For other models, please first confirm your Zhipu account permissions and billing rules, then manually add them to `VISION_MODELS`, such as:

- `glm-5v-turbo`: Paid visual model
- `glm-4.6v`: Paid visual model
- `glm-4.1v-thinking-flashx`: Enhanced visual model, availability depends on account permissions
- `glm-4.6v-flash`: Free visual model
- `glm-4.1v-thinking-flash`: Free visual model
- `glm-4v-flash`: Free basic image understanding model

Refer to the [official Zhipu model list](https://docs.bigmodel.cn/cn/guide/start/model-overview) for actual available models, prices, and permissions.

Note: In our real-world integration testing on 2026-08-09, we frequently encountered HTTP 429 and business code `1305` (model access volume too high) from `glm-4.6v-flash`, while `glm-4v-flash` could be called normally. This is a temporary overload of Zhipu's free shared service, not an image format error from this MCP. If you need to configure a paid model as a fallback, please first confirm the billing rules and account quota.

## Method Three: A General OpenAI Compatible Interface, Configuring Multiple Models

Suitable for OpenRouter, SiliciumFlow, self-built vLLM/LM Studio, or other compatible interfaces. The interface must support:

- `POST {baseUrl}/chat/completions`
- OpenAI-style `messages[].content[]`- `image_url.url` in the base64 data URL

json
{
  "mcpServers": {
    "vision-mcp-server": {
      "command": "npx",
      "args": ["-y", "vision-mcp-server"],
      "env": {
        "VISION_PROVIDER": "openai-compatible",
        "OPENAI_BASE_URL": "https://provider.example/v1",
        "OPENAI_API_KEY": "your_api_key",
        "VISION_MODELS": "vision-model-a,vision-model-b,vision-model-c"
      }
    }
  }
}

The three models share the `OPENAI_API_KEY` and fallback in the order specified in `VISION_MODELS`.

"OpenAI compatible" does not necessarily mean that third-party providers support images. If an endpoint only supports text or does not accept base64 images, this MCP cannot enable visual capabilities for it.

## Method Four: Configuring ModelScope, Zhipu, and Other Providers Simultaneously

When cross-provider fallback is needed, use `VISION_ROUTES`. The keys are still placed in `env`; `VISION_ROUTES` only references the environment variable names where the keys are located via `apiKeyEnv`.

json
{
  "mcpServers": {
    "vision-mcp-server": {
      "command": "npx",
      "args": ["-y", "vision-mcp-server"],
      "env": {
        "MODELSCOPE_TOKEN": "your_modelscope_token",
        "ZAI_API_KEY": "your_zhipu_api_key",
        "CUSTOM_OPENAI_API_KEY": "your_custom_api_key",
        "VISION_ROUTES": "[{\"name\":\"modelscope\",\"baseUrl\":\"https://api-inference.modelscope.cn/v1\",\"apiKeyEnv\":\"MODELSCOPE_TOKEN\",\"models\":[\"Qwen/Qwen3.5-397B-A17B\",\"Qwen/Qwen3.5-35B-A3B\"],\"maxImageEdge\":2048},{\"name\":\"zhipu\",\"baseUrl\":\"https://open.bigmodel.cn/api/paas/v4\",\"apiKeyEnv\":\"ZAI_API_KEY\",\"models\":[\"glm-4v-flash\"],\"maxImageEdge\":2048},{\"name\":\"custom-openai\",\"baseUrl\":\"https://provider.example/v1\",\"apiKeyEnv\":\"CUSTOM_OPENAI_API_KEY\",\"models\":[\"your-vision-model\"],\"maxImageEdge\":2048}]"
      }
    }
  }
}

The complete call sequence in the example above is:

1. First ModelScope model
2. Second ModelScope model (same ModelScope key)
3. First Zhipu model
4. Subsequent Zhipu models (same Zhipu key)
5. Custom OpenAI-compatible model

Once `VISION_ROUTES` is set, it overrides the first three simplified configurations.

### VISION_ROUTES Fields

| Field | Required | Description |
|---|---:|---|
| `name` | No | Route name, used only for security logs and test filtering |
| `baseUrl` | Yes | Base URL of the OpenAI-compatible endpoint |
| `apiKeyEnv` | Yes | Environment variable name where the API Key is located, not the key itself |
| `model` | One of two | Single model ID |
| `models` | One of two | Ordered array of model IDs, sharing the same key within the same route |
| `headers` | No | Additional request headers; do not store API Keys here |
| `timeoutMs` | No | Request timeout for this route, in milliseconds |
| `maxImageEdge` | No | Maximum edge length of the image accepted by this route |
| `extraBody` | No | Provider-specific request fields, e.g., `thinking` for Zhipu |

Example of a route field to enable thinking mode for Zhipu:

json
{
  "extraBody": {
    "thinking": { "type": "enabled" }
  }
}

## When Does Fallback Occur?

Fallback to the next model will occur in the following cases:

- HTTP `408`, `429`, `500`, `502`, `503`, `504`
- Request timeout, connection reset, DNS, or other network connection errors

Fallback will not occur in the following cases:

- HTTP `400`: Image, prompt, or request parameter error
- HTTP `401/403`: Key, permission, or model authorization error
- Content security rejection
- Local image does not exist, invalid format, or path not allowed

Failed models will enter a cooldown period, defaulting to 60 seconds. This prevents each tool call from hitting a rate-limited model first.

## Configuration Parameter Summary

### Providers and Models

| Environment Variable | Use Case | Description |
|---|---|---|
| `MODELSCOPE_TOKEN` | ModelScope | ModelScope API Token |
| `MODELSCOPE_MODEL` | Old single ModelScope model | Single model ID |
| `MODELSCOPE_MODELS` | Multiple ModelScope models | Comma-separated list, takes precedence over `MODELSCOPE_MODEL` |
| `VISION_PROVIDER` | Simplified configuration | `zhipu` or `openai-compatible`; defaults to ModelScope compatibility mode if not set |
| `ZAI_API_KEY` | Zhipu | Zhipu API Key || `OPENAI_BASE_URL` | Generic compatible interface | Base URL, e.g., `https://provider.example/v1` |
| `OPENAI_API_KEY` | Generic compatible interface | API Key |
| `VISION_API_KEY_ENV` | Simplified configuration advanced option | Use the specified name for the Key environment variable |
| `VISION_MODELS` | Zhipu/Generic compatible interface | Required; a comma-separated list of ordered models in English |
| `VISION_ROUTES` | Multi-vendor | Advanced routing JSON; overrides simplified configuration if set |

### Images, Security, and Reliability

| Environment Variable | Default Value | Description |
|---|---:|---|
| `VISION_MAX_IMAGE_EDGE` | `2048` | Default maximum edge length for simplified configuration |
| `VISION_MAX_IMAGE_BYTES` | `20971520` | Maximum bytes for input or processed images |
| `VISION_MAX_IMAGE_PIXELS` | `40000000` | Maximum number of pixels for decoded images |
| `VISION_ALLOWED_DIRS` | Unrestricted | Allowed local directories, separated by commas |
| `VISION_IMAGE_DOWNLOAD_TIMEOUT_MS` | `15000` | Timeout for downloading online images |
| `VISION_REQUEST_TIMEOUT_MS` | `60000` | Timeout for model requests |
| `VISION_FALLBACK_COOLDOWN_MS` | `60000` | Cool-down time for failed routes |
| `VISION_DEBUG` | `false` | Output sanitized debug logs to stderr |

It is recommended to configure allowed directories for local images:

json
{
  "VISION_ALLOWED_DIRS": "D:\\Pictures,D:\\Screenshots"
}

## MCP Tools

### `analyze_image`

| Parameter | Required | Description |
|---|---:|---|
| `image` | Yes | Local absolute path, HTTP/HTTPS URL, or image data URL |
| `prompt` | No | Question about the image, default is "Please describe the content of this image" |

Example:

json
{
  "name": "analyze_image",
  "arguments": {
    "image": "D:\\Pictures\\chart.png",
    "prompt": "Extract the title, data, and units from the chart"
  }
}

## Image Processing

Before sending to the provider, this MCP will:

1. Validate the actual file content, accepting only JPEG, PNG, WebP, and GIF.
2. Apply EXIF orientation.
3. Scale proportionally to the smallest `maxImageEdge` among all candidate routes, without enlarging smaller images.
4. Output as PNG if there is a transparent channel, otherwise output as JPEG.
5. Clear EXIF and other metadata.
6. Send the image as a base64 data URL to the vision endpoint.

Online images are first securely downloaded and processed similarly; localhost, internal network addresses, and cloud metadata addresses are prohibited by default.

## Installation Requirements

- Node.js `20.9.0` or higher
- MCP client supports local stdio Server

## English

Vision MCP Server adds image understanding to MCP agents by calling a separately configured vision model.

For a local stdio installation, put provider credentials and model IDs in the MCP host configuration under `mcpServers..env`. Models in the same comma-separated `VISION_MODELS`/`MODELSCOPE_MODELS` list share one API key and are tried in order. Use `VISION_ROUTES` for ordered fallback across multiple providers.

Supported configurations:

- ModelScope: `MODELSCOPE_TOKEN` + `MODELSCOPE_MODELS`
- Zhipu: `VISION_PROVIDER=zhipu` + `ZAI_API_KEY` + explicit `VISION_MODELS`
- Generic OpenAI-compatible endpoint: `VISION_PROVIDER=openai-compatible` + `OPENAI_BASE_URL` + `OPENAI_API_KEY` + `VISION_MODELS`
- Multiple providers: `VISION_ROUTES`

Zhipu models are not hardcoded. Free and paid vision model IDs can be mixed in any order. See the complete configuration examples above.

The server falls back only for rate limits, timeouts, network failures, and selected 5xx responses. Invalid images, authentication failures, and request validation errors do not trigger fallback.

**Official site: ** [https://github.com/Markusbetter/vision-mcp-server](https://github.com/Markusbetter/vision-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `data`
- Tags: `research and data`, `视觉`, `通义千问`, `魔搭社区`, `图片识别`, `文字识别`, `图片`, `智普`, `openai`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y vision-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/markusbetter-vision.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
