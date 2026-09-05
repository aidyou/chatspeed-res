---
title: "HealthCalculator"
description: "This project is a web application for calculating health parameters based on Gradio. Users can input basic information such as gender, age, height, and weight (required), as well as optional health da…"
---

# HealthCalculator

This project is a web application for calculating health parameters based on Gradio. Users can input basic information such as gender, age, height, and weight (required), as well as optional health da…

## Project Introduction

Origin of the idea: Sometimes I really want to know what simple parameters or health indicators mean for my body. Many online calculators are not very accurate, so I confirmed the calculation formulas with hospital doctors. I then wanted to build this on large models, in MCP form, to facilitate my body assessments.

Currently, users only need to input basic information such as gender, age, height, and weight (required), as well as optional health data like waist circumference, triglycerides, and HDL cholesterol, to instantly calculate multiple commonly used health indicators, including BMI, BSA, waist-to-height ratio, CI, CMI, CVAI, LAP, BFR, RFM, etc., and receive health assessment recommendations.

## Deployment Guide

#### What is SSE?

Server-Sent Events (SSE) is an HTTP-based technology that allows the server to push data to clients unidirectionally and in real time. In SSE mode, developers can create an EventSource object on the client to establish a persistent connection with the server; the server then continuously sends a data stream through this connection without the client having to make repeated requests.

#### Product Features

* Easy to use: suitable for everyday users via the MCP (SSE) approach - no local deployment needed, simply configure a URL address.
* Automatic upgrades: we continuously iterate and update; no extra actions are required from users.
* Easier for LLMs to understand: we convert the raw JSON results into a semantic form that is easier for large models to understand.
* Zero operations cost: fully managed cloud architecture - users don't need to worry about server maintenance, resource scaling, or other underlying ops issues.
* Protocol compatibility: supports SSE long connections, adapting to the technical needs of different business scenarios.

```json
{
    "mcpServers": {
        "gradio": {
            "command": "npx",
            "args": [
                "mcp-remote",
                "https://dudu007-healthcalculator.ms.show/gradio_api/mcp/sse",
                "--transport",
                "sse-only"
            ]
        }
    }
}
```

## Usage Example

### Input
This is an MCP that can retrieve health information. Calculate health parameters based on the following information:
Gender: Male
Age: 30.0 years
Height: 175.0 cm
Weight: 70.0 kg
Waist circumference: 85.0 cm
Triglycerides: 150.0 mg/dL
HDL cholesterol: 45.0 mg/dL

### Output
The user needs to have health parameters calculated.
For this request, I need to call the health calculator tool, which calculates health parameters based on the provided personal information. These parameters may include BMI, metabolic syndrome risk, and more.

First, I should select the dudu007/HealthCalculator:predict tool, since it is dedicated to calculating health parameters and provides the required parameter interface. The tool requires age, gender, HDL cholesterol level (optional), height, triglyceride level (optional), waist circumference (optional), and weight as inputs.

I need to prepare the input data:
- Age: 30.0 years
- Gender: Male
- Height: 175.0 cm
- Weight: 70.0 kg
- Waist circumference: 85.0 cm
- Triglycerides: 150.0 mg/dL
- HDL cholesterol: 45.0 mg/dL

After calling the tool, it will return the calculated health parameters. I need to parse the returned results and report the key information to the user.

The health parameter calculation is complete. Here are the detailed results:

#### Basic Information:
- **Gender**: Male
- **Age**: 30.0 years
- **Height**: 175.0 cm
- **Weight**: 70.0 kg

#### Health Calculation Parameters:
1. **BMI (Body Mass Index)**: 22.86 -> **Normal weight**
   - BMI is an important indicator of whether your weight is normal; the healthy range is 18.5-24.9.

2. **BSA (Body Surface Area)**: 1.81 m²
   - Represents the total body surface area; commonly used in medical calculations.

3. **Waist circumference**: 85.0 cm
   - The normal range for male waist circumference is below 90 cm; the current value is within normal range.

4. **Waist-to-height ratio**: 0.486 -> **Normal waist-to-height ratio**
   - A waist-to-height ratio below 0.5 is normal, indicating a lower risk of central obesity.

5. **CI (Conicity Index)**: 1.23
   - Reflects the shape of fat distribution; lower values are healthier.

6. **Triglycerides**: 150.0 mg/dL
   - The normal range is below 150 mg/dL; the current value is at the borderline.

7. **HDL cholesterol**: 45.0 mg/dL
   - The ideal value for men is above 40 mg/dL; the current value meets the target.

8. **CMI (Cardiometabolic Index)**: 1.62
   - Used to assess cardiovascular disease risk; the lower the value, the lower the risk.

9. **CVAI (Chinese Visceral Adiposity Index)**: -531.01
   - Reflects visceral fat accumulation; a negative value indicates less visceral fat.

10. **LAP (Lipid Accumulation Product)**: 3000.00
    - Used to predict metabolic risk; the current value is in the lower-risk range.

11. **BFR (Body Fat Rate)**: 18.13%
    - The normal body fat range for adult men is 15%-20%; the current value is within the healthy range.

12. **RFM (Relative Fat Mass)**: 22.82%
    - A newer measure of body fat; lower values are better.

### Health Assessment:
- **BMI status**: Normal weight
- **Waist-to-height ratio status**: Normal
- **Overall assessment**: Current health is good, with no obvious metabolic or obesity-related risks.

If you need further analysis, such as dietary advice or exercise plans, feel free to continue with specific requests.

**Official site: ** [https://www.modelscope.cn/studios/dudu007/HealthCalculator](https://www.modelscope.cn/studios/dudu007/HealthCalculator)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `search`, `data`
- Tags: `developer tools`, `research and data`, `search`, `健康`, `bmi`, `ci`, `bfr`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://dudu007-healthcalculator.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/dudu007-healthcalculator.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
