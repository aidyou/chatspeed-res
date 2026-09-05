---
title: "LoveTell"
description: "Project Overview Lovetell, the Book of True Love, is an intelligent agent focused on providing emotional and marital counseling by integrating traditional Chinese astrology (including BaZi and Zi Wei…"
---

# LoveTell

Project Overview Lovetell, the Book of True Love, is an intelligent agent focused on providing emotional and marital counseling by integrating traditional Chinese astrology (including BaZi and Zi Wei…

## Project Overview

Lovetell, the Book of True Love, is an intelligent agent focused on providing emotional and marital counseling by integrating traditional Chinese astrology (including BaZi and Zi Wei Dou Shu) with modern psychological knowledge. It offers in-depth, multi-dimensional emotional analysis to help users better understand their own emotional needs and partner relationships. This project develops its MCP (Modelscope Computing Platform) toolkit, which covers core astrological dimensions such as Peach Blossom Star, Spouse Star, and Marriage Palace, along with a psychological perspective for analyzing emotions and interaction patterns.

### Tool Introduction

- **Peach Blossom Star Calculation**: Analyzes the "Peach Blossom Star" in the BaZi to identify the foundation of personal charm and opposite-sex relationships, providing astrological basis for emotional opportunities.
- **Spouse Star Calculation**: Interprets the "Spouse Star" in the BaZi to predict the characteristics of the right partner and the trend of marriage.
- **Marriage Palace Calculation**: Uses the day branch as the "Marriage Palace" to analyze the quality of spousal relationships, marital stability, and family interaction patterns.
- **Emotional Pattern Analysis**: Combines psychological methods to interpret the underlying emotional tone and deep-seated needs, enhancing self-awareness in emotions.
- **Interaction Pattern Analysis**: Analyzes the ways users and their partners interact in communication, socializing, and division of responsibilities, promoting harmonious relationships.
- **Partner Traits Prediction**: Predicts potential partner's appearance, occupation, family background, personality, and values, assisting users in clarifying their mate selection direction.

## Deployment Guide
    
json
{
    "name": "love-tell-ai-mcp-v2",
    "type": "stdio",
    "command": "uvx",
    "args": [
        "love-tell-ai-mcp-v2"
    ],
    "env": {
        "api_key": "sk-xxx"
    }
}

## Design Philosophy

The core design principle of this project's MCP tools is "integration": we do not simply encapsulate the terms of BaZi astrology but deeply integrate the logic behind them with modern psychological models. The goal is to provide a set of tools that align with traditional cultural understanding while also offering modern scientific explanations.

## Overall Architecture

The MCP service adopts a clear layered architecture to ensure stability, scalability, and maintainability.
- **Protocol Layer**: Strictly adheres to the MCP protocol standards, implementing core interfaces such as listTools, callTool, and readResource.
- **Core Calculation Engine**: Utilizes the [Bailian Application] to build a unified astrology calculation module, capable of calculating information like the Peach Blossom Star and Marriage Palace based on the user's birth data. The raw results from the calculation engine are then interpreted and mapped to psychological dimensions.
- **Knowledge Base and Resources**: Through the MCP's resources function, static, background knowledge documents are provided to the intelligent agent, significantly enhancing its knowledge base and enabling it to better explain our analytical results to users.
- **Context Awareness**: The tool design fully considers the context of the conversation. For example, when the intelligent agent consecutively calls the Spouse Star Calculation and Partner Traits Prediction, the service internally caches the user's BaZi information to avoid redundant calculations and maintain consistency in the analysis.

## Usage Example

- Try out the MCP tools on ModelScope (requires API key configuration; service not yet open)

 
   
 

## Test Example

Can you calculate my marriage fate? My BaZi information is:
  "Gender": "Male",
  "Gregorian Date": "July 31, 1998 14:10:00",
  "Lunar Date": "Lunar Year Wuyin, 6th month, 9th day, Xinwei hour",
  "BaZi": "Wuyin Yiwu Jiyou Xinyou",
  "Chinese Zodiac": "Tiger",
  "Day Master": "Ji",
  "Year Pillar": {
    "Heavenly Stem": {
      "Stem": "Wu",
      "Five Elements": "Earth",
      "Yin Yang": "Yang",
      "Ten Gods": "Rob Wealth"
    },
    "Earthly Branch": {
      "Branch": "Yin",
      "Five Elements": "Wood",
      "Yin Yang": "Yang",
      "Hidden Stems": {
        "Main Qi": {
          "Stem": "Jia",
          "Ten Gods": "Direct Official"
        },
        "Middle Qi": {
          "Stem": "Bing",
          "Ten Gods": "Direct Seal"
        },
        "Remaining Qi": {
          "Stem": "Wu",
          "Ten Gods": "Rob Wealth"
        }
      }
    },
    "Nayin": "City Wall Earth",
    "Xun": "Jiaxu",
    "Kongwang": "Shen You",
    "Star Fate": "Death",
    "Self-Sitting": "Longevity"
  },
  "Month Pillar": {
    "Heavenly Stem": {
      "Stem": "Yi",
      "Five Elements": "Earth",
      "Yin Yang": "Yin",
      "Ten Gods": "Peer"
    },
    "Earthly Branch": {
      "Branch": "Wei",
      "Five Elements": "Earth",
      "Yin Yang": "Yin",
      "Hidden Stems": {
        "Main Qi": {
          "Stem": "Yi",
          "Ten Gods": "Peer"
        },
        "Middle Qi": {
          "Stem": "Ding",
          "Ten Gods": "Indirect Seal"
        },
        "Remaining Qi": {
          "Stem": "Yi",
          "Ten Gods": "Seven Kill"
        }
      }
    },
    "Nayin": "Heavenly Fire",
    "Xun": "Jia Yin",
    "Kongwang": "Zi Chou",
    "Star Fate": "Guan Dai",
    "Self-Sitting": "Guan Dai"
  },
  "Day Pillar": {
    "Heavenly Stem": {
      "Stem": "Ji",
      "Five Elements": "Earth",
      "Yin Yang": "Yin"
    },
    "Earthly Branch": {
      "Branch": "Mao",
      "Five Elements": "Wood",
      "Yin Yang": "Yin",
      "Hidden Stems": {
        "Main Qi": {
          "Stem": "Yi",
          "Ten Gods": "Seven Kill"
        }
      }
    },
    "Nayin": "City Wall Earth",
    "Xun": "Jia Xu",
    "Kongwang": "Shen You",
    "Star Fate": "Illness",
    "Self-Sitting": "Illness"
  },
  "Hour Pillar": {
    "Heavenly Stem": {
      "Stem": "Xin",
      "Five Elements": "Metal",
      "Yin Yang": "Yin",
      "Ten Gods": "Food God"
    },
    "Earthly Branch": {
      "Branch": "Wei",
      "Five Elements": "Earth",
      "Yin Yang": "Yin",
      "Hidden Stems": {
        "Main Qi": {
          "Stem": "Yi",
          "Ten Gods": "Peer"
        },
        "Middle Qi": {
          "Stem": "Ding",
          "Ten Gods": "Indirect Seal"
        },
        "Remaining Qi": {
          "Stem": "Yi",
          "Ten Gods": "Seven Kill"
        }
      }
    },
    "Nayin": "Roadside Earth",
    "Xun": "Jia Zi",
    "Kongwang": "Xu Hai",
    "Star Fate": "Guan Dai",
    "Self-Sitting": "Decline"
  }- When integrating the agent with the MCP tool, the parsing results can be rendered as HTML cards.

## Contact Us

- The Book of True Love Lovetell is an agent project created by re4.ai. If you are interested in participating in the design, [please leave us a message](https://u1hk68mdmio.feishu.cn/share/base/form/shrcnSiKfeSUaN96xt3zEswdGLc).
- Visit https://re4.ai/ to consult on end-to-end AI solutions that help businesses and startup teams solve real-world problems and create significant value through artificial intelligence technology.

**Official site: ** [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`, `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `uvx`
- Args: `love-tell-ai-mcp-v2`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/wanghh-lovetell.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
