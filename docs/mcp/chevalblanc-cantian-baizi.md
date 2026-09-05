---
title: "MCP-cantian-baizi"
description: "Unlock precise Bazi insights with the Bazi MCP, the first AI-powered Bazi calculator."
---

# MCP-cantian-baizi

Unlock precise Bazi insights with the Bazi MCP, the first AI-powered Bazi calculator.

# Bazi MCP by Cantian AI

[Smithery](https://smithery.ai/server/@cantian-ai/bazi-mcp)
[mseep.ai](https://mseep.ai/app/453ac410-d93a-45fb-8563-7d3cccfbe956)

Unlock precise Bazi insights with the **Bazi MCP**, the first AI-powered Bazi calculator. Built to address inaccuracies in existing AI fortune-telling tools like GPT and DeepSeek, our MCP delivers reliable Bazi data for personality analysis, destiny forecasting, and more.

### Why Bazi MCP?

- **Accurate Bazi Calculations**: Provide insightful Bazi information.
- **AI Agent Integration**: Empowers AI agents with precise Bazi data.
- **Community-Driven**: Join enthusiasts to advance Chinese metaphysics.

Originating from the popular [_Chinese Bazi Fortune Teller_](https://chatgpt.com/g/g-67c3f7b74d148191a2167f44fd13412d-chinese-bazi-fortune-teller-can-tian-ba-zi-suan-ming-jing-zhun-pai-pan-jie-du) GPTs in the GPT Store, this project is now integrated with **Cantian AI** ([cantian.ai](https://cantian.ai)). We invite Bazi practitioners and AI enthusiasts to collaborate, share insights, and contribute to our open-source community.

### Get Involved

- **Contact**: [support@cantian.ai](mailto:support@cantian.ai)

## Prerequisite

Node.js 22 or above.

## Start

Configure your AI application (e.g. Claude Desktop).

```json
{
  "mcpServers": {
    "Bazi": {
      "command": "npx",
      "args": ["bazi-mcp"]
    }
  }
}
```

### Installing via Smithery

To install bazi-mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@cantian-ai/bazi-mcp):

```bash
npx -y @smithery/cli install @cantian-ai/bazi-mcp --client claude
```

## Tools

### getBaziDetail

> Calculate the Bazi results based on the solar/lunar datetime.

#### Arguments

- solarDatetime: `String`

  > Solar datetime in ISO format. Example: `2000-05-15T12:00:00+08:00`.

- lunarDatetime: `String`

  > Lunar datetime. Example: `2000-05-15 12:00:00`.

- gender: `Number`

  > Gender. Optional. 0 for female, 1 for male. 1 by default.

- eightCharProviderSect: `Number`

  > Configuration for eight char provider. Optional. 1 for meaning the day stem of 23:00-23:59 is for tomorrow, 2 for meaning the day stem of 23:00-23:59 is for today. 2 by default.

#### Result example

```json
{
  "gender": "Male",
  "solar": "1998-07-31 14:10:00",
  "lunar": "Lunar Year Wuyin, 6th month, 9th day, XINWEI hour",
  "bazi": "戊寅 己未 己卯 辛未",
  "zodiac": "Tiger",
  "dayMaster": "己",
  "yearPillar": {
    "heavenlyStem": {
      "stem": "戊",
      "fiveElement": "Earth",
      "yinYang": "Yang",
      "tenGod": "Friend"
    },
    "earthlyBranch": {
      "branch": "寅",
      "fiveElement": "Wood",
      "yinYang": "Yang",
      "hiddenStems": {
        "main": {"stem": "甲", "tenGod": "Direct Officer"},
        "middle": {"stem": "丙", "tenGod": "Direct Seal"},
        "residual": {"stem": "戊", "tenGod": "Friend"}
      }
    },
    "naYin": "City Earth",
    "xun": "甲戌",
    "kongWang": "申酉",
    "starLuck": "Death",
    "selfSit": "Long Life"
  },
  "monthPillar": {
    "heavenlyStem": {
      "stem": "己",
      "fiveElement": "Earth",
      "yinYang": "Yin",
      "tenGod": "Shoulder"
    },
    "earthlyBranch": {
      "branch": "未",
      "fiveElement": "Earth",
      "yinYang": "Yin",
      "hiddenStems": {
        "main": {"stem": "己", "tenGod": "Shoulder"},
        "middle": {"stem": "丁", "tenGod": "Indirect Seal"},
        "residual": {"stem": "乙", "tenGod": "Seven Killings"}
      }
    },
    "naYin": "Sky Fire",
    "xun": "甲寅",
    "kongWang": "子丑",
    "starLuck": "Crown Belt",
    "selfSit": "Crown Belt"
  },
  "dayPillar": {
    "heavenlyStem": {
      "stem": "己",
      "fiveElement": "Earth",
      "yinYang": "Yin"
    },
    "earthlyBranch": {
      "branch": "卯",
      "fiveElement": "Wood",
      "yinYang": "Yin",
      "hiddenStems": {
        "main": {"stem": "乙", "tenGod": "Seven Killings"}
      }
    },
    "naYin": "City Earth",
    "xun": "甲戌",
    "kongWang": "申酉",
    "starLuck": "Sick",
    "selfSit": "Sick"
  },
  "hourPillar": {
    "heavenlyStem": {
      "stem": "辛",
      "fiveElement": "Metal",
      "yinYang": "Yin",
      "tenGod": "Eating God"
    },
    "earthlyBranch": {
      "branch": "未",
      "fiveElement": "Earth",
      "yinYang": "Yin",
      "hiddenStems": {
        "main": {"stem": "己", "tenGod": "Shoulder"},
        "middle": {"stem": "丁", "tenGod": "Indirect Seal"},
        "residual": {"stem": "乙", "tenGod": "Seven Killings"}
      }
    },
    "naYin": "Roadside Earth",
    "xun": "甲子",
    "kongWang": "戌亥",
    "starLuck": "Crown Belt",
    "selfSit": "Decline"
  },
  "taiYuan": "庚戌",
  "taiXi": "甲戌",
  "mingGong": "乙卯",
  "shenGong": "乙卯",
  "shenSha": {
    "yearPillar": ["National Seal", "Dead God"],
    "monthPillar": ["Heavenly Virtue Harmony", "Monthly Virtue Harmony", "Tianyi Noble", "Taiji Noble", "Fortune Star Noble", "Golden Chariot", "Blood Blade", "Flower Canopy", "Heavenly Joy", "Original Chen"],
    "dayPillar": ["Heavenly Virtue Harmony", "Monthly Virtue Harmony", "Peach Blossom", "Nine Ugly", "Child Killer"],
    "hourPillar": ["Tianyi Noble", "Taiji Noble", "Fortune Star Noble", "Golden Chariot", "Blood Blade", "Flower Canopy", "Heavenly Joy", "Original Chen", "Child Killer"]
  },
  "daYun": {
    "startAge": 4,
    "startDate": "2001-01-26",
    "luckPeriods": [
      {
        "ganZhi": "庚申",
        "startYear": 2001,
        "endYear": 2010,
        "stemTenGod": "Hurting Officer",
        "branchTenGods": ["Hurting Officer", "Direct Wealth", "Friend"],
        "branchHiddenStems": ["庚", "壬", "戊"],
        "startAge": 4,
        "endAge": 13
      },
      {
        "ganZhi": "辛酉",
        "startYear": 2011,
        "endYear": 2020,
        "stemTenGod": "Eating God",
        "branchTenGods": ["Eating God"],
        "branchHiddenStems": ["辛"],
        "startAge": 14,
        "endAge": 23
      },
      {
        "ganZhi": "壬戌",
        "startYear": 2021,
        "endYear": 2030,
        "stemTenGod": "Direct Wealth",
        "branchTenGods": ["Friend", "Eating God", "Indirect Seal"],
        "branchHiddenStems": ["戊", "辛", "丁"],
        "startAge": 24,
        "endAge": 33
      },
      {
        "ganZhi": "癸亥",
        "startYear": 2031,
        "endYear": 2040,
        "stemTenGod": "Indirect Wealth",
        "branchTenGods": ["Direct Wealth", "Direct Officer"],
        "branchHiddenStems": ["壬", "甲"],
        "startAge": 34,
        "endAge": 43
      },
      {
        "ganZhi": "甲子",
        "startYear": 2041,
        "endYear": 2050,
        "stemTenGod": "Direct Officer",
        "branchTenGods": ["Indirect Wealth"],
        "branchHiddenStems": ["癸"],
        "startAge": 44,
        "endAge": 53
      },
      {
        "ganZhi": "乙丑",
        "startYear": 2051,
        "endYear": 2060,
        "stemTenGod": "Seven Killings",
        "branchTenGods": ["Shoulder", "Indirect Wealth", "Eating God"],
        "branchHiddenStems": ["己", "癸", "辛"],
        "startAge": 54,
        "endAge": 63
      },
      {
        "ganZhi": "丙寅",
        "startYear": 2061,
        "endYear": 2070,
        "stemTenGod": "Direct Seal",
        "branchTenGods": ["Direct Officer", "Direct Seal", "Friend"],
        "branchHiddenStems": ["甲", "丙", "戊"],
        "startAge": 64,
        "endAge": 73
      },
      {
        "ganZhi": "丁卯",
        "startYear": 2071,
        "endYear": 2080,
        "stemTenGod": "Indirect Seal",
        "branchTenGods": ["Seven Killings"],
        "branchHiddenStems": ["乙"],
        "startAge": 74,
        "endAge": 83
      },
      {
        "ganZhi": "戊辰",
        "startYear": 2081,
        "endYear": 2090,
        "stemTenGod": "Friend",
        "branchTenGods": ["Friend", "Seven Killings", "Indirect Wealth"],
        "branchHiddenStems": ["戊", "乙", "癸"],
        "startAge": 84,
        "endAge": 93
      },
      {
        "ganZhi": "己巳",
        "startYear": 2091,
        "endYear": 2100,
        "stemTenGod": "Shoulder",
        "branchTenGods": ["Direct Seal", "Hurting Officer", "Friend"],
        "branchHiddenStems": ["丙", "庚", "戊"],
        "startAge": 94,
        "endAge": 103
      }
    ]
  },
  "clashesCombinations": {
    "year": {"stem": {}, "branch": {}},
    "month": {
      "stem": {},
      "branch": {
        "halfCombination": [{"pillar": "Day", "note": "未卯半合木", "element": "Wood"}]
      }
    },
    "day": {
      "stem": {},
      "branch": {
        "halfCombination": [
          {"pillar": "Month", "note": "卯未半合木", "element": "Wood"},
          {"pillar": "Hour", "note": "卯未半合木", "element": "Wood"}
        ]
      }
    },
    "hour": {
      "stem": {},
      "branch": {
        "halfCombination": [{"pillar": "Day", "note": "未卯半合木", "element": "Wood"}]
      }
    }
  }
}
```

### getSolarTimes

> Return a list of possible solar calendar datetime based on the given Bazi.

#### Arguments

- bazi: `String`

  > Bazi, with each pillar separated by a space.

#### Result example

```json
["1758-07-29 14:00:00", "1818-07-15 14:00:00", "1998-07-31 14:00:00"]
```

### getChineseCalendar

> Get chinese calendar information for the specified solar calendar date (default is today).

#### Arguments

- solarDatetime

  > Solar datetime in ISO format. Example: `2000-05-15T12:00:00+08:00`.

#### Result example

```json
{
  "solar": "2025-05-07 Wednesday",
  "lunar": "Lunar Year Yisi, 4th month, 10th day",
  "ganZhi": "乙巳 辛巳 丙子",
  "zodiac": "Snake",
  "naYin": "Stream Water",
  "solarTerm": "Start of Summer",
  "constellation": "箕水豹吉",
  "pengZu": "丙不修灶必见灾殃 子不问卜自惹祸殃",
  "joyGodDirection": "Southwest",
  "yangNobleDirection": "West",
  "yinNobleDirection": "Northwest",
  "fortuneGodDirection": "East",
  "wealthGodDirection": "Southwest",
  "clash": "冲马(午)煞南",
  "suitable": "marriage, sacrifice, prayer, seeking descendants, opening light, travel, dismantling, earth-moving, beam-raising, fire-setting, adding people, moving in, moving, bed-settling, planting, livestock, herding, pillar-raising, door-fixing, repair, cleansing, meeting relatives",
  "avoid": ""
}
```

### buildBaziFromLunarDatetime (deprecated)

> Calculate the BaZi results based on the lunar datetime.

#### Arguments

- lunarDatetime: `String`

  > Lunar datetime. Example: `2000-05-15 12:00:00`.

- gender: `Number`

  > Gender. Optional. 0 for female, 1 for male. 1 by default.

- eightCharProviderSect: `Number`

  > Configuration for eight char provider. Optional. 1 for meaning the day stem of 23:00-23:59 is for tomorrow, 2 for meaning the day stem of 23:00-23:59 is for today. 2 by default.

### buildBaziFromSolarDatetime (deprecated)

> Calculate the BaZi results based on the solar datetime.

#### Arguments

- solarDatetime: `String`

  > Solar datetime in ISO format. Example: `2000-05-15T12:00:00+08:00`.

- gender: `Number`

  > Gender. Optional. 0 for female, 1 for male.

- eightCharProviderSect: `Number`

  > Configuration for eight char provider. Optional. 1 for meaning the day stem of 23:00-23:59 is for tomorrow, 2 for meaning the day stem of 23:00-23:59 is for today. 2 by default.

**Keywords**: Bazi MCP, Bazi AI Agent, Fengshui AI Agent, Bazi Calculator MCP, Bazi Calculator AI, Cantian AI

**Official site: ** [https://github.com/taurusduan/bazi-mcp](https://github.com/taurusduan/bazi-mcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `memory`
- Tags: `knowledge and memory`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `bazi-mcp`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/chevalblanc-cantian-baizi.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
