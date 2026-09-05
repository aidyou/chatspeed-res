---
title: "IntelliVNG_mcp-server"
description: "@intellivng/mcp-server IntelliVNG Visual Novel Game Script Analysis MCP Server This is a service based on the Model Context Protocol (MCP), providing tools for analyzing visual novel game scripts. It…"
---

# IntelliVNG_mcp-server

@intellivng/mcp-server IntelliVNG Visual Novel Game Script Analysis MCP Server This is a service based on the Model Context Protocol (MCP), providing tools for analyzing visual novel game scripts. It…

# @intellivng/mcp-server

> IntelliVNG Visual Novel Game Script Analysis MCP Server

This is a service based on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), providing tools for analyzing visual novel game scripts. It can be invoked by any AI assistant that supports MCP, for validating and analyzing non-linear narrative structures.

## Features

- **Structure Validation**: Detects isolated nodes, dead ends, and invalid links to ensure there are no hard errors in the story graph.
- **Path Analysis**: Enumerates all story paths, evaluating the degree of non-linearity and diversity.
- **Dialogue Quality**: Analyzes dialogue distribution, character appearances, and emotional richness to assist in pacing and style optimization.
- **Branch Distribution**: Detects "pseudo non-linearity" issues, ensuring key branches are not concentrated only before the endings.
- **Constraint Compliance**: Compares against the creator's set goals for number of nodes, endings, path depth, and branching, outputting a compliance score and list of violations.
- **Non-linearity Composite Score**: Merges multiple analysis dimensions into a single 0–100 score, making it easy for front-end display and work ranking.
- **Unified Output Protocol**: All tools return `{ ok: boolean, data | error }`, allowing the host to reuse all capabilities with a single JSON parse.

---

## Tool List

### 1. `validate_story_structure` —— Story Structure Validation

**Purpose:**

- Ensures that all important nodes can be reached from the starting node, avoiding "island content".
- Checks if non-ending nodes have "dead ends", preventing players from getting stuck.
- Verifies that `nextNodeId` and branch-targeted node IDs are all valid.

**Typical Scenario:**

- After a Story Planner/Node Writer generates a version of the story graph, the Reviewer Agent first calls this tool for static structure checks, identifying hard errors before proceeding to higher-level narrative review processes.

**Output Example:**

```json

{

  "ok": true,

  "data": {

    "valid": true,

    "orphans": [],

    "deadEnds": [],

    "invalidLinks": [],

    "reachableCount": 12,

    "totalCount": 12

  }

}

```
---

### 2. `analyze_story_paths` —— Path and Diversity Analysis

**Purpose:**

- Counts the total number of complete paths from the start to all endings.
- Calculates the average path length and length variance to measure experience richness.
- Counts the number of branch points and endings as basic indicators of "non-linearity".

**Output Example:**

```json

{

  "ok": true,

  "data": {

    "totalPaths": 5,

    "diversityScore": 0.75,

    "avgPathLength": 8.2,

    "lengthVariance": 4.5,

    "endingCount": 3,

    "branchPointCount": 4,

    "nonLinearityScore": 72

  }

}

```
---

### 3. `analyze_dialogue_quality` —— Dialogue Quality and Pacing Analysis

**Purpose:**

- Counts the number of dialogues per node and whether there is narration.
- Identifies nodes with severely insufficient ( 8) dialogues to aid in pacing control.
- Analyzes the distribution of character speeches and emotions, providing quantitative references for style consistency and character development.

**Applicable Scenarios:**

- Used in conjunction with CharacterDB and StyleGuide, where upper-level agents determine "who speaks too little/too much" and "whether a certain character lacks presence".

---

### 4. `analyze_branch_distribution` —— Branch Distribution and "Pseudo Non-linearity" Detection

**Purpose:**

- Counts the number of branches at each stage based on the `functionTag` (setup/rising/conflict/climax/resolution) dimension.
- Categorizes and counts branches by `branchType` (route/relationship/information/ending).
- Detects if branches are heavily concentrated in the climax/ending stages, thus determining the presence of "pseudo non-linearity".

**Output Example:**

```json

{

  "ok": true,

  "data": {

    "isPseudoNonLinear": false,

    "distributionScore": 85,

    "branchByPhase": {

      "setup": 1,

      "rising": 2,

      "conflict": 1,

      "climax": 1,

      "resolution": 0

    },

    "branchTypeStats": {

      "route": 3,

      "relationship": 1,

      "information": 1,

      "ending": 0

    },

    "earlyBranchRatio": 0.6,

    "suggestions": [

      "分支分布良好！故事具有较好的非线性叙事结构。"

    ]

  }

}

```
---

### 5. `check_constraints_compliance` —— Constraint Compliance Check

**Purpose:**

- Converts the "target specifications" (e.g., 12 nodes, 3 endings, maximum depth of 10, up to 4 branches per node) from the creator or front-end form into hard constraints.
- Automatically tallies the actual generated story graph and outputs a list of violations and a compliance score.

**This step directly demonstrates "AI logic following capability":**

- Upper-level Agents can explicitly write these constraints in the Prompt, and then this tool makes a "factual judgment". If the criteria are not met, it triggers a rewrite or supplementation process.

**Output Example:**

```json

{

  "ok": true,

  "data": {

    "nodeCount": 12,

    "endingCount": 3,

    "branchPointCount": 4,

    "maxDepthFound": 9,

    "maxBranchingFound": 3,

    "hasStart": true,

    "violations": [],

    "complianceScore": 100

  }

}

```
---

### 6. `score_nonlinearity` —— Non-linearity Composite Score

**Purpose:**

- Combines results from path analysis, branch distribution analysis, and more into a single 0–100 non-linearity score.
- Facilitates direct front-end display of a "non-linearity score radar chart/progress bar" or sorting in a work list.

**Output Example:**

```json

{

  "ok": true,

  "data": {

    "overallScore": 82,

    "components": {

      "pathNonLinearity": 78,

      "distributionScore": 86,

      "diversityScore": 70

    },

    "endingCount": 3,

    "branchPointCount": 4,

    "earlyBranchRatio": 0.55,

    "notes": [

      "非线性结构良好，可直接呈现。"

    ]

  }

}

```
---

## Integration with IntelliVNG Multi-Agent WorkflowIn the overall system, this MCP server mainly collaborates with the following Agents:

- **Story Planner Agent**: Generates the `NarrativePlan` and `PlanNode` skeleton.
- **Node Writer Agent**: Fills in dialogues, narrations, and option texts for each PlanNode, producing a `NodeDraft`.
- **Story Reviewer Agent (ReAct mode)**:
  - During the ReAct reasoning process, multiple tools of this service are called through MCP:
    - First, use `validate_story_structure` and `analyze_story_paths` to ensure the structure is correct and sufficiently non-linear;
    - Then, use `analyze_dialogue_quality` to check the pacing and character distribution;
    - Use `analyze_branch_distribution` to detect if there is "pseudo non-linearity";
    - Finally, use `check_constraints_compliance` and `score_nonlinearity` to provide machine-readable decision bases.
  - The Reviewer decides whether to trigger rewrites on certain nodes (returning to Node Writer) based on the structured results returned by the tools, forming an automatic closed loop.

This design demonstrates:

- **AI Logical Follow-up Capability**:
  - The model does not "score based on feeling" but makes decisions based on objective metrics (number of nodes, path depth, early branch ratio, constraint compliance) returned by the tools.
- **Modularity and Reusability**:
  - Even if the implementation of Story Planner/Node Writer is changed, this MCP module can still be reused as is.

---

## Installation

```bash

# 在 IntelliVNG monorepo 根目录

pnpm install

# 或单独安装本包

cd packages/mcp-server

pnpm install

# 首次安装后会通过 prepare 自动编译 dist

```
---

## Usage

### Method One: Running as an MCP Server

```bash

# 开发模式（便于调试）

pnpm dev

# 或构建后运行

pnpm build

pnpm start

```
### Method Two: Configuring in Host Clients like Claude Desktop / Cursor

Add the following to `claude_desktop_config.json`:

```json

{

  "mcpServers": {

    "intellivng": {

      "command": "node",

      "args": ["/path/to/intellivng/packages/mcp-server/dist/index.js"]

    }

  }

}

```
### Method Three: Running Source Code Directly in Cursor

Configure in `.cursor/mcp.json`:

```json

{

  "mcpServers": {

    "intellivng": {

      "command": "npx",

      "args": ["tsx", "/path/to/intellivng/packages/mcp-server/src/index.ts"]

    }

  }

}

```
> All text content returned by the tools is in JSON string format. Please perform a JSON.parse on the host side and then read the `ok`, `data`, or `error` fields.

---

## Node Data Format Convention

Example of the minimum node format accepted by the tools (the more complete the fields, the more accurate the analysis):

```typescript

interface StoryNode {

  id: string;                          // 节点唯一标识

  type?: "scene" | "branch" | "ending"; // 节点类型

  isStart?: boolean;                   // 是否为起始节点

  isEnding?: boolean;                  // 是否为结局节点

  functionTag?:

    | "setup"

    | "rising"

    | "conflict"

    | "twist"

    | "climax"

    | "falling"

    | "resolution";                   // 叙事阶段标签（用于分支分布分析）

  nextNodeId?: string;                 // 线性推进下一个节点

  choices?: {                          // 分支选项（用于非线性和分支分析）

    targetNodeId: string;

    branchType?: "route" | "relationship" | "information" | "ending";

  }[];

  dialogues?: {                        // 对话列表（用于对话质量分析）

    characterName?: string;

    text: string;

    emotion?: string;

  }[];

  narration?: string;                  // 旁白

}

```
---

## Architecture Explanation

```text

packages/mcp-server/

├── src/

│   ├── index.ts                    # MCP Server 入口，注册所有 MCP 工具

│   └── tools/

│       ├── validate-structure.ts   # 结构校验工具

│       ├── analyze-paths.ts        # 路径分析工具

│       ├── analyze-dialogue.ts     # 对话质量工具

│       ├── analyze-branch-distribution.ts  # 分支分布工具

│       ├── check-constraints.ts    # 约束合规工具

│       ├── score-nonlinearity.ts   # 非线性综合评分工具

│       └── index.ts                # 工具导出统一入口

├── package.json

├── tsconfig.json

└── README.md

```
## Design Philosophy

### 1. "Left Brain + Right Brain"

Borrowing from the *Neuro-Symbolic Architecture* theory, this MCP service is not just a toolbox but serves as the 'left brain' (rational layer) of IntelliVNG, while LLMs serve as the 'right brain' (generative layer). Through deterministic graph algorithms, it corrects logical flaws in probabilistic models.

What we do can be simply understood as:

- **Right Brain: Let the large model focus on "writing stories"**
  - Story Planner / Node Writer is responsible for using imagination to write dialogues, narrations, and branches based on the settings.

- **Left Brain: Let a small "code module" specifically find errors**
  - This MCP Server only solidifies a few very specific tasks:
    - Use graph algorithms to check for dead ends or isolated nodes;
    - Perform constraint checks based on the user's target number of nodes / endings / maximum depth;
    - Return these check results in a unified JSON structure to the upper-level Agent.

The entire process is more like a collaboration of "AI writes the first draft → engineering validator finds errors → rewrite another version":

**Creativity is handled by the LLM, while rigor is ensured by deterministic tools, each performing their own roles.**

### 2. Cognitive Accessibility

In the `score_nonlinearity` tool, we introduce the **"Cognitive Friendly"** metric.

- Detects if the number of branches per node exceeds the player's short-term memory load (>5 or >7).
- We deeply consider how to improve **accessibility design** and **user experience** in both the main application and tool design, focusing not only on technical implementation but also on the final cognitive burden on players.

### 3. Internationalization (i18n)

All tools have built-in `i18n` support for multilingual internationalization, automatically switching via input parameters.
This allows AI Agents to receive accurate native language feedback in different language environments.

### 4. Self-Correction Loop

To achieve AI logical follow-up capability, we designed the following self-correction workflow:

```typescript

// 伪代码演示：自修正闭环

async function generatePerfectStory() {

  let story = await writerAgent.generate();

  let attempts = 0;

  while (attempts < 3) {

    // 调用 MCP 工具进行"左脑"检查

    const compliance = await mcp.check_constraints_compliance({

      nodes: story.nodes,

      constraints: { maxBranching: 4, targetEndingCount: 3 }

    });

    // 如果合规分 100，直接通过

    if (compliance.data.complianceScore === 100) break;

    // 否则，将违规项喂回给 Agent 进行针对性重写

    // 这就是"逻辑跟随"的具体体现

    const feedback = `检测到违规：${compliance.data.violations.join(", ")}。请修正这些问题。`;

    story = await writerAgent.regenerate(story, feedback);

    attempts++;

  }

  return story;

}

```
## Future Plans:To further implement the design philosophy of **"toolchain reuse"**, we have planned future expansions for MCP services, aiming to further decouple IntelliVNG's generation and format conversion capabilities, turning them into a general-purpose creation infrastructure.

### 1. `asset-generator` MCP — General Asset Generation Service

Currently, asset generation (Character Sprites, Backgrounds, BGM) is tightly coupled with business services. In the future, we will encapsulate these as independent MCP tools, available for any Agent to call upon.

**Planned Tools:**
- `generate_character_sprite(prompt, style, pose)`: Generates character sprites with transparency.
- `generate_background_image(prompt, style, mood)`: Generates background images that match the scene's atmosphere.
- `generate_bgm(mood, genre, duration)`: Generates background music.

**Value:**
- **Modularity**: Other game projects or Agents can directly reuse this service to generate materials without worrying about whether the underlying system is connected to SD or Midjourney.
- **Immediate Feedback**: After a Node Writer completes a segment of the story, they can directly use this tool to provide illustrations for that node, achieving a "rich text and image" creation flow.

### 2. `format-converter` MCP — Game Engine Bridge

To break the isolation of creation tools, we will provide format conversion services, supporting the translation of generic JSON scripts into source code for various game engines.

**Planned Tools:**
- `convert_to_renpy_script(node_json)`: Converts script nodes into Ren'Py `.rpy` script code.
- `convert_to_unity_csharp(node_json)`: Generates C# data classes or ScriptableObjects compatible with Unity's dialogue system.
- `export_full_project(target_engine)`: Packages all assets and scripts, generating engine project files.

**Value:**
- **Toolchain Closure**: Completes the last mile from "AI generation" to "engine execution".
- **Ecosystem Expansion**: Not only serves IntelliVNG's own web player but also empowers professional game developers to use traditional engines for further development.

**Official site: ** [https://github.com/FE-square/IntelliVNG](https://github.com/FE-square/IntelliVNG)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @intellivng/mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/melxy1997-intellivng.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
