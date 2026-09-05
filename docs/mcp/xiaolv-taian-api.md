---
title: "Taian_API"
description: "Enterprise Recruitment Data Processing System Overview This system is designed to handle data related to enterprise recruitment, primarily providing two core functionalities: 1. Recruitment Position D…"
---

# Taian_API

Enterprise Recruitment Data Processing System Overview This system is designed to handle data related to enterprise recruitment, primarily providing two core functionalities: 1. Recruitment Position D…

# Enterprise Recruitment Data Processing System

## Overview

This system is designed to handle data related to enterprise recruitment, primarily providing two core functionalities:
1. **Recruitment Position Data Cleaning** - Extract complete recruitment entity information from job postings.
2. **Position Alias Data Cleaning** - Standardize job titles and unify naming conventions.

---

## Functional Modules

### 1. Recruitment Position Data Cleaning

#### Function Description
Comprehensively extract entities from the input corporate recruitment data, extracting key fields from the job postings to support subsequent data analysis and management.

#### Task Parameters
 
task_l: "1-Recruitment Position Data Cleaning"

#### Field Extraction List

| Field Name | Description | Example |
|------------|-------------|---------|
| Original Job Title | The original job title in the job posting | "Java Development Engineer (Senior)" |
| Standardized Job Title | The standardized job title | "Java Development Engineer" |
| Number of Hires | The planned number of hires | "2 people", "several" |
| Hiring Company | The name of the company posting the job | "XX Technology Co., Ltd." |
| Work Location | The city/region where the work is located | "Chaoyang District, Beijing" |
| Professional Requirements | Required professional background | "Computer-related major" |
| Gender Requirement | Gender restrictions | "Unlimited", "Male", "Female" |
| Education Requirement | Minimum education requirement | "Bachelor's degree or above" |
| Work Experience Requirement | Work experience requirement | "3-5 years" |
| Age Requirement | Age range requirement | "25-35 years old" |
| Salary Range | Salary range | "15K-25K" |
| Skill Requirements | Essential/preferred skills | "Familiar with Spring framework, MySQL" |
| Benefits | Benefits provided by the company | "Five insurances and one fund, year-end bonus, paid annual leave" |
| Candidate Characteristics | Other requirements for candidates | "Strong sense of responsibility, good teamwork ability" |
| Contact Person | Name of the recruitment contact | "Manager Zhang" |
| Contact Information | Contact phone/email, etc. | "138****8000", "hr@*****.com" |

#### Output Format

json
{
  "Original Job Title": ["Java Development Engineer (Senior)"],
  "Standardized Job Title": ["Java Development Engineer"],
  "Number of Hires": ["2 people"],
  "Hiring Company": ["XX Technology Co., Ltd."],
  "Work Location": ["Chaoyang District, Beijing"],
  "Professional Requirements": ["Computer-related major"],
  "Gender Requirement": ["Unlimited"],
  "Education Requirement": ["Bachelor's degree or above"],
  "Work Experience Requirement": ["3-5 years"],
  "Age Requirement": ["No requirement"],
  "Salary Range": ["15K-25K"],
  "Skill Requirements": ["Familiar with Spring framework", "MySQL database", "Microservices architecture"],
  "Benefits": ["Five insurances and one fund", "Year-end bonus", "Paid annual leave"],
  "Candidate Characteristics": ["Strong sense of responsibility", "Good teamwork ability"],
  "Contact Person": ["Manager Zhang"],
  "Contact Information": ["138****8000"]
}

#### Field Explanation
- All fields are returned in **list form**, supporting multiple value extraction.
- When a field is not mentioned or has no clear information in the original text, it returns `["No requirement"]`.
- Fields such as skill requirements and benefits can contain multiple values.

#### Usage Example

**Input Example:**

Recruiting 2 Java Development Engineers, requiring a bachelor's degree or above, more than 3 years of work experience,
familiar with Spring Boot, MySQL, salary 15-25K, work location: Chaoyang District, Beijing,
contact person: Manager Zhang, phone: 138****8000

**Output Example:**
json
{
  "Original Job Title": ["Java Development Engineer"],
  "Standardized Job Title": ["Java Development Engineer"],
  "Number of Hires": ["2 people"],
  "Hiring Company": ["No requirement"],
  "Work Location": ["Chaoyang District, Beijing"],
  "Professional Requirements": ["No requirement"],
  "Gender Requirement": ["No requirement"],
  "Education Requirement": ["Bachelor's degree or above"],
  "Work Experience Requirement": ["More than 3 years"],
  "Age Requirement": ["No requirement"],
  "Salary Range": ["15-25K"],
  "Skill Requirements": ["Spring Boot", "MySQL"],
  "Benefits": ["No requirement"],
  "Candidate Characteristics": ["No requirement"],
  "Contact Person": ["Manager Zhang"],
  "Contact Information": ["138****8000"]
}

---

### 2. Position Alias Data Cleaning

#### Function Description
Standardize the input job titles, identify and clean various variants of job titles, and output uniformly standardized job titles and their related information.

#### Task Parameters
 
task_l: "2-Position Alias Data Cleaning"#### Field Extraction List

| Field Name | Description | Example |
|------------|-------------|---------|
| Original Job Title | The original job title from the recruitment information | "Senior JAVA Engineer (P6)" |
| Standardized Job Title | The standardized and normalized job title | "Java Development Engineer" |
| English Job Title | The standard English name of the position | "Java Development Engineer" |
| Chinese Alternative Names | Other common Chinese names for the position | ["Java Engineer", "Java Programmer", "Java Developer"] |

#### Output Format

json
{
  "Original Job Title": ["Senior JAVA Engineer (P6)"],
  "Standardized Job Title": ["Java Development Engineer"],
  "English Job Title": ["Java Development Engineer"],
  "Chinese Alternative Names": ["Java Engineer", "Java Programmer", "Java Developer"]
}

#### Field Explanation
- All fields are returned in **list form**.
- **Original Job Title**: Retains the original input format without modification.
- **Standardized Job Title**: Removes modifiers such as levels or numbers, unifying the expression.
- **English Job Title**: Provides the corresponding standard English name.
- **Chinese Alternative Names**: Lists other common names for the position, supporting multiple aliases.
- When a field cannot be identified or is not applicable, return `["No Requirement"]`.

#### Usage Examples

**Example Input 1:**
 
Senior JAVA Engineer (P6)

**Example Output 1:**
json
{
  "Original Job Title": ["Senior JAVA Engineer (P6)"],
  "Standardized Job Title": ["Java Development Engineer"],
  "English Job Title": ["Java Development Engineer"],
  "Chinese Alternative Names": ["Java Engineer", "Java Programmer", "Java Developer"]
}

**Example Input 2:**
 
Product Manager PM/Product Designer

**Example Output 2:**
json
{
  "Original Job Title": ["Product Manager PM/Product Designer"],
  "Standardized Job Title": ["Product Manager"],
  "English Job Title": ["Product Manager"],
  "Chinese Alternative Names": ["PM", "Product Planner", "Product Designer"]
}

**Example Input 3:**
 
UI/UX Design

**Example Output 3:**
json
{
  "Original Job Title": ["UI/UX Design"],
  "Standardized Job Title": ["UI Designer"],
  "English Job Title": ["UI Designer"],
  "Chinese Alternative Names": ["Interface Designer", "User Interface Designer", "UX Designer", "Interaction Designer"]
}

---

## Data Processing Flow

### Overall Flowchart

Input Recruitment Data
     ↓
Identify Task Type (task_l)
     ↓
  ┌──────────────┐
  │              │
  ↓              ↓
Task 1        Task 2
Recruitment  Position
Data Cleaning  Alias
  │              │
  ↓              ↓
Entity Extraction  Name Standardization
(16 Fields)    (4 Fields)
  │              │
  └──────┬───────┘
         ↓
   Return JSON Result

### Processing Principles

1. **Completeness**: Extract all relevant information as much as possible.
2. **Accuracy**: Ensure that the extracted information matches the original text.
3. **Standardization**: Unify data formats and naming conventions.
4. **Fault Tolerance**: Return "No Requirement" for missing information, do not throw errors.

---

## API Call Specifications

### Request Parameters

| Parameter Name | Type | Required | Description |
|----------------|------|----------|-------------|
| task_l | string | Yes | Task type: "1-Recruitment Position Data Cleaning" or "2-Position Alias Data Cleaning" |
| content | string | Yes | The recruitment data text to be processed |

### Request Examples

**Task 1 - Recruitment Position Data Cleaning:**
json
{
  "task_l": "1-Recruitment Position Data Cleaning",
  "content": "Hiring 2 Java Development Engineers, requires bachelor's degree or above, 3+ years of experience, familiar with Spring Boot, MySQL, salary 15-25K, location: Chaoyang District, Beijing"
}

**Task 2 - Position Alias Data Cleaning:**
json
{
  "task_l": "2-Position Alias Data Cleaning",
  "content": "Senior JAVA Engineer (P6)"
}

### Response Format

Responses are uniformly in JSON format, returning the corresponding field structure based on the task type.

---

## Frequently Asked Questions (FAQ)

### Q1: What if some fields are missing in the recruitment information?**A:** The system will automatically identify and return `["无要求"]` for missing fields, which will not affect the normal extraction of other fields.

### Q2: How to handle multiple values for the same field?
**A:** The system will return multiple values in list form, for example, skill requirements might return `["Java", "Python", "MySQL"]`.

### Q3: What is the basis for standardizing job titles?
**A:** The system standardizes job titles based on commonly used industry standards, removing modifiers such as levels and numbers, and extracting the core job title.

### Q4: How to distinguish between using Task 1 or Task 2?
**A:** 
- If you need to extract **complete job information** (company, location, salary, etc.), use Task 1.
- If you only need to **standardize the job title**, use Task 2.

### Q5: Which languages of job titles does the system support?
**A:** Currently, the system mainly supports processing Chinese job titles and can output the corresponding standardized English names.

---

## Data Example Set

### Example 1: Complete Job Information

**Input:**
 
An internet company is hiring a Senior Product Manager with the following requirements:
1. Bachelor's degree or above, major in Marketing or Computer Science preferred
2. 5+ years of product management experience, e-commerce experience preferred
3. Age 30-40, gender not specified
4. Familiar with product design processes, proficient in Axure, Xmind, etc.
5. Salary range: 25K-35K, 13 months' salary
6. Benefits: Five insurances and one fund, supplementary medical, annual health check, team building activities
7. Work location: Pudong New Area, Shanghai
8. Contact: Ms. Li, email: hr@*****.com

**Task 1 Output:**
json
{
  "原始岗位名称": ["高级产品经理"],
  "标准岗位名称": ["产品经理"],
  "招聘人数": ["无要求"],
  "招聘公司": ["某互联网公司"],
  "工作地点": ["上海市浦东新区"],
  "专业要求": ["市场营销", "计算机相关专业"],
  "性别要求": ["不限"],
  "学历要求": ["本科及以上"],
  "工作年限要求": ["5年以上"],
  "年龄要求": ["30-40岁"],
  "薪资区间": ["25K-35K", "13薪"],
  "技能要求": ["熟悉产品设计流程", "精通Axure", "Xmind"],
  "福利待遇": ["五险一金", "补充医疗", "年度体检", "团建活动"],
  "求职者特性": ["有电商行业经验者优先"],
  "联系人": ["李女士"],
  "联系方式": ["hr@*****.com"]
}

### Example 2: Brief Job Information

**Input:**

Urgently hiring front-end developers, proficiency in Vue required, 8-12K

**Task 1 Output:**
json
{
  "原始岗位名称": ["前端开发"],
  "标准岗位名称": ["前端开发工程师"],
  "招聘人数": ["无要求"],
  "招聘公司": ["无要求"],
  "工作地点": ["无要求"],
  "专业要求": ["无要求"],
  "性别要求": ["无要求"],
  "学历要求": ["无要求"],
  "工作年限要求": ["无要求"],
  "年龄要求": ["无要求"],
  "薪资区间": ["8-12K"],
  "技能要求": ["Vue"],
  "福利待遇": ["无要求"],
  "求职者特性": ["无要求"],
  "联系人": ["无要求"],
  "联系方式": ["无要求"]
}

### Example 3: Multiple Variants of Job Titles

**Input List:**
- "资深Java工程师（P7-P8）"
- "JAVA后端研发专家"
- "Java开发"
- "后端工程师-Java方向"

**Task 2 Output (Example One):**
json
{
  "原始岗位名称": ["资深Java工程师（P7-P8）"],
  "标准岗位名称": ["Java开发工程师"],
  "岗位英文名称": ["Java Development Engineer"],
  "岗位中文别名": ["Java工程师", "Java程序员", "Java后端开发", "后端工程师"]
}

---

## Technical Notes

### Data Format
- All input and output use **UTF-8** encoding
- Return format is **JSON**
- All field values are of **List** type

### Performance Metrics
- Processing time for a single data entry: < 500ms
- Supports batch processing
- Concurrent processing capability: Depends on server configuration

### Version Information
- Current version: v1.0
- Last updated: 2025-11-10

---

## Contact and Support

If you have any questions or suggestions, please contact the technical support team.

---

## Update Log

### v1.0 (2025-11-10)
- Initial version release- Support job posting data cleaning function
- Support job alias data cleaning function
- Provide entity extraction for 16 recruitment fields
- Provide 4 standardized job title fields

---

**End of Document**

**Official site: ** [https://modelscope.cn/models/xiaolv/security_testing_model/summary](https://modelscope.cn/models/xiaolv/security_testing_model/summary)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `communication`
- Tags: `knowledge and memory`, `communication`, `实体抽取`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y mcp-remote https://taian-mcp-1.rencaidanao.com --transport http-only --auth-timeout 500000 --timeout 500000`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/xiaolv-taian-api.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
