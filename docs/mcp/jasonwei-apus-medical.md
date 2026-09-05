---
title: "apus-medical-mcp"
description: "Qihuang & Zhicao MCP Medical Assistant apus-medical-mcp-server Version Information v1.0.0 Product Description Short Description Qihuang & Zhicao MCP Medical Assistant is a medical consultation service…"
---

# apus-medical-mcp

Qihuang & Zhicao MCP Medical Assistant apus-medical-mcp-server Version Information v1.0.0 Product Description Short Description Qihuang & Zhicao MCP Medical Assistant is a medical consultation service…

# Qihuang & Zhicao MCP Medical Assistant

apus-medical-mcp-server

## Version Information

v1.0.0

## Product Description

### Short Description

Qihuang & Zhicao MCP Medical Assistant is a medical consultation service based on the MCP protocol, providing intelligent medical consultation services that integrate both Western and Traditional Chinese Medicine, helping users to obtain professional medical advice and diagnoses.

### Long Description

Qihuang & Zhicao MCP Medical Assistant is a medical consultation server based on the MCP protocol, integrating two specialized medical consultation systems: Western Medicine and Traditional Chinese Medicine. It provides intelligent medical consultation services through MCP, capable of offering professional medical advice and diagnoses based on the user's specific symptoms and issues. Behind this service are the large models trained by APUS, namely Qihuang (for Western Medicine) and Zhicao (for Traditional Chinese Medicine).

### Quick Experience:
Unified entry for APUS large models, Qihuang Western Medicine large model, and Zhicao Traditional Chinese Medicine large model:
https://chat.apusai.com

## Category

Medical Consultation

## Tags

Medical, Traditional Chinese Medicine, Western Medicine, Intelligent Diagnosis

## Tools

### Tool1: Western Medicine Consultation (Qihuang)

#### Detailed Description

Provides Western medicine-related medical advice and diagnoses, including symptom analysis, treatment plans, and medication recommendations.

#### Parameters Required for Debugging

Input:
* query: User's question (required)
* conversation_id: Conversation ID (optional)
* user_id: User ID (optional)

Output:
* Western medicine-related medical advice and diagnosis

### Tool2: Traditional Chinese Medicine Consultation (Zhicao)

#### Detailed Description

Provides Traditional Chinese Medicine-related medical advice and diagnoses, including TCM syndrome differentiation, herbal prescriptions, and health preservation suggestions.

#### Parameters Required for Debugging

Input:
* query: User's question (required)
* conversation_id: Conversation ID (optional)
* user_id: User ID (optional)

Output:
* Traditional Chinese Medicine-related medical advice and diagnosis

## Authentication Method

API Key

## Usage

### Method 1: Download Code to Local

bash
git clone https://github.com/AiLMe-AI/apus-medical-mcp-server

cd mcp-server-doctor

uv pip install -e .

npx -y @modelcontextprotocol/inspector uv run mcp-server-doctor

Access the page to start using the Qihuang and Zhicao MCP services.

### Method 2: Configure in Client
json
  "mcpServers": {
    "mcp-server-doctor": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-doctor",
        "run",
        "mcp-server-doctor"
      ],
      "env": {
        "DOCTOR_API_KEY": "sk-****"
      }
    }
  }

## API Key Acquisition

To obtain an API Key, please contact: bd [at] apusai.com

**Official site: ** [https://github.com/AiLMe-AI/apus-medical-mcp-server](https://github.com/AiLMe-AI/apus-medical-mcp-server)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`

## MCP Configuration

- Transport: `stdio`
- Command: `uv`
- Args: `--directory /path/to/mcp-server-doctor run mcp-server-doctor`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/jasonwei-apus-medical.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
