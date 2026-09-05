---
title: "gaokaomcp"
description: "Gaokao (College Entrance Exam) volunteer recommendation system. An intelligent volunteer-filling recommendation system based on historical admission data over the years, helping students choose school…"
---

# gaokaomcp

Gaokao (College Entrance Exam) volunteer recommendation system. An intelligent volunteer-filling recommendation system based on historical admission data over the years, helping students choose school…

# Gaokao Volunteer Recommendation System

An intelligent volunteer-filling recommendation system based on historical college admission data, helping students choose schools and majors scientifically.

## Features

- **Smart recommendation**: based on 2024 and historical admission data, combined with major popularity trend analysis
- **Four-tier classification**: automatically computes four recommendation types - Reach, Safety, Stable, and Other - to prevent clustering and gaps
- **Historical data estimation**: when no historical data exists, automatically estimates using data from other majors at the same school, batch, and subject category
- **Subject requirement matching**: automatically checks subject selection requirements to ensure eligibility
- **Major trend analysis**: analyzes popularity trends of majors for more precise recommendations

## Installation and Running

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the service
```bash
uvicorn main:app --reload
```

### 3. Access the API docs
Open your browser and visit: http://127.0.0.1:8888/docs

## API Endpoints

### Basic recommendations
- **POST** `/recommend` - get the recommendation list
- **POST** `/recommend/summary` - get the recommendation summary
- **POST** `/recommend/by-type` - recommendations grouped by type

### Helper endpoints
- **GET** `/schools` - get the list of all schools
- **GET** `/majors` - get the list of all majors
- **GET** `/subjects` - get the list of subject requirements

## Usage Examples

### Basic recommendation request
```json
{
  "user": {
    "score": 600,
    "rank": 1200,
    "subjects": ["Physics", "Chemistry"],
    "preferred_majors": ["Computer Science", "Electronic Information"],
    "preferred_schools": ["Peking University", "Tsinghua University"],
    "risk_preference": "balanced"
  },
  "top_n": 30
}
```

### Recommendation result fields
- `yxmc`: school name
- `sbzydhmc`: major name
- `zszymc`: major code
- `zsjhs`: planned enrollment count
- `kskmyqzw`: subject requirements
- `last_year_rank`: lowest admission rank in 2024
- `last_year_score`: lowest admission score in 2024
- `trend`: major popularity trend (rising/stable/declining)
- `recommendation_type`: recommendation type (Reach/Safety/Stable/Other)
- `recommendation_score`: recommendation score
- `pcmc`: batch name
- `sfbz`: tuition standard

## Recommendation Algorithm

### 1. Historical data processing
- Prioritizes 2024 admission data
- When no data exists, estimates using other majors at the same school, batch, and subject category
- Supports multi-year trend analysis

### 2. Recommendation type calculation
- **Safe (Bao)**: student's rank has a clear advantage (rank gap > -1500), very high admission probability
- **Stable (Wen)**: ranks are close (rank gap from -1500 to -500), high admission probability
- **Reach (Chong)**: larger rank gap (rank gap > 1500), requires a stretch
- **Other**: other situations or insufficient data

### 3. Composite scoring algorithm
- Rank gap weight: 40%
- Major popularity trend: 20%
- Enrollment size: 20%
- Recommendation type: 20%

### 4. Subject requirement matching
- Automatically checks subject requirements for physics, chemistry, biology, politics, etc.
- Supports majors with "no subject requirements"
- Ensures the student's subject selection matches the eligibility criteria

## Recommendation Types

### Safe schools (Bao)
- Student's rank is clearly better than the school's admission rank
- Very high admission probability, recommended as a safety option
- Suitable as the last few choices in the volunteer list

### Stable schools (Wen)
- Student's rank is close to the school's admission rank
- High admission probability, relatively safe
- Suitable as the main volunteer choices

### Reach schools (Chong)
- Student's rank is lower than the school's admission rank
- Some risk, but there is a chance of admission
- Suitable as the first few choices in the volunteer list

### Other types
- Insufficient data or special situations
- Requires further understanding and analysis

## Notes

1. The data source is the 2025 Gansu Province enrollment plan and applies to candidates in Gansu Province only
2. Recommendations are for reference only; final volunteer filling should follow official policies
3. Consider personal interests, career planning, and other factors comprehensively
4. Monitor enrollment policy changes and school information updates regularly

## Tech Stack

- **Backend**: FastAPI + Python
- **Data processing**: Pandas + NumPy
- **Data source**: Excel files (openpyxl)
- **API docs**: Swagger UI (auto-generated)

## Development Plan

- [ ] Add a frontend interface
- [ ] Support data for more provinces
- [ ] Add major employment outlook analysis
- [ ] Support personalized recommendation preferences
- [ ] Add volunteer-filling simulation functionality

**Official site: ** [https://www.modelscope.cn/studios/YYplayer/gaokaomcp](https://www.modelscope.cn/studios/YYplayer/gaokaomcp)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://yyplayer-gaokaomcp.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/yyplayer-gaokaomcp.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
