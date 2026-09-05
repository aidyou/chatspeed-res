---
title: "tblife-image-generate"
description: "Create a Text-to-Image with a Taobao Life character. Introduction This document guides you through using a specific API to create text-to-image outputs with Taobao Life character avatars. Taobao Life…"
---

# tblife-image-generate

Create a Text-to-Image with a Taobao Life character. Introduction This document guides you through using a specific API to create text-to-image outputs with Taobao Life character avatars. Taobao Life…

# Create a Text-to-Image with a Taobao Life Character

## Introduction
This document guides you through using a specific API to create text-to-image outputs with Taobao Life character avatars. Taobao Life is a virtual social app launched by Alibaba Group, where users can create their own virtual character and interact in a virtual world.

## Preparation
- You need a valid API key.
- Make sure your development environment has the required libraries installed, such as `requests`, so you can send HTTP requests.
- Basic Python programming knowledge.

## API Call Example
Below is a simple Python script example showing how to generate an image containing a Taobao Life character via the API. Make sure to replace `your_api_key` with your actual API key.

```python
import requests
import json

url = "https://api.example.com/generate_image"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_api_key'
}
data = {
    "character": "TaobaoLife",
    "scene": "Garden Party",
    "style": "Cartoon"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    with open('output.png', 'wb') as f:
        f.write(response.content)
    print("Image saved successfully.")
else:
    print(f"Failed to generate image: {response.text}")
```

### Parameter description
- `character`: specifies the Taobao Life character type to use.
- `scene`: sets the scene background, e.g., garden party.
- `style`: defines the overall image style, e.g., cartoon.

## Notes
- Before using it in production, read the API documentation carefully for more information about supported characters, scenes, and styles.
- Keep your API key secure; do not make it public or share it with others.
- Depending on the API provider's terms, some usage limits or conditions may apply.

We hope this guide helps you get started quickly and begin creating fun Taobao Life images! If you have any questions or need further help, refer to the official documentation or contact customer support.

**Official site: ** [https://github.com/driveRoad/city-mcp.git](https://github.com/driveRoad/city-mcp.git)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y 12306-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/skychumo-tblife-image-generate.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
