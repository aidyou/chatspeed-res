---
title: "kfc_v_me_50"
description: "A tag-based copywriting service built on MCP (Model Context Protocol), providing \"Crazy Thursday\" copy generation and search for AI applications. Designed for role-playing apps, chatbots, social media…"
---

# kfc_v_me_50

A tag-based copywriting service built on MCP (Model Context Protocol), providing "Crazy Thursday" copy generation and search for AI applications. Designed for role-playing apps, chatbots, social media…

# Crazy Thursday Copywriting MCP Service

A tag-based copywriting service built on the Model Context Protocol (MCP), providing Crazy Thursday copy generation and search for AI applications. Designed for role-playing apps, chatbots, social media tools, and similar scenarios.

## Core Features

### Tag-based Management
- **Multi-dimensional tag system**: five dimensions - occupation, group, scenario, emotion, and technique
- **Precise matching**: quickly filter the right copy by tags
- **Smart categorization**: 329 items of copy classified by writing style and use case

### MCP Service Interfaces
- `generate_random_content()` - random copy generation
- `search_targeted_content()` - tag-based targeted search
- **Standardized output**: unified data format for easy integration

### AI-Application Friendly
- **Role adaptation guide**: how to use the copy based on the AI character's traits
- **Scenario matching**: copy recommendations for different use cases
- **Creative references**: structure and technique analysis of the copy

## Service Positioning

### Empowering AI Applications
- **Role-playing apps** - copywriting capabilities for AI assistants and chatbots
- **Social media tools** - content creation and marketing copy
- **Entertainment and interactive apps** - enhance user interaction
- **Creative writing tools** - creative reference for copy

### Usage Principles
This service provides copy as **reference and creative inspiration**. App developers are advised to:
- Adjust tone and expression to fit the AI character's traits
- Weave the copy naturally into the conversation context rather than pasting it verbatim
- Check and update time-sensitive information in the copy
- Personalize while keeping the character consistent

## Installation & Configuration

### 1. Clone the project
```bash
git clone https://github.com/whoever01/crazy_v_me_50.git
cd crazy_v_me_50
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
# Or use pyproject.toml
pip install -e .
```

### 3. MCP client configuration

#### Claude Desktop configuration
Add the following to `~/.claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "crazy-thursday": {
      "command": "python",
      "args": ["app.py"],
      "cwd": "/path/to/crazy_v_me_50",
      "env": {
        "SILICONFLOW_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

#### Other MCP clients
Follow the format above and replace the path with your actual project path.

### 4. API key configuration (optional)

#### Getting an API key
- Visit the [SiliconFlow website](https://siliconflow.cn/)
- Register an account and get an API key
- Used to enable hybrid search (semantic + tag + content search)
- Uses the advanced BAAI/bge-m3 multilingual model for semantic understanding
- Without a key, tag + content search is used (still highly accurate)

#### Configuration methods
**Method 1: Set it in the MCP configuration**
```json
"env": {
  "SILICONFLOW_API_KEY": "sk-xxxxxxxxxxxxxxxx"
}
```

**Method 2: Environment variable**
```bash
export SILICONFLOW_API_KEY=sk-xxxxxxxxxxxxxxxx
```

**Method 3: .env file**
```bash
# Create a .env file
echo "SILICONFLOW_API_KEY=sk-xxxxxxxxxxxxxxxx" > .env
```

### 5. Verify the installation
```bash
# Test basic functionality
python -c "from tools import generate_random_content; print(generate_random_content(1))"

# Check the environment variable
python -c "import os; print(f'API Key: {os.getenv(\"SILICONFLOW_API_KEY\", \"not set\")}')"
```

## MCP Service Interfaces

### Available Features
- **`generate_random_content(count=3)`**: randomly generate copy (3 items by default)
- **`search_targeted_content(query, count=3, api_key="")`**: targeted search
  - `query`: search keyword
  - `count`: number of results (1-10)
  - `api_key`: SiliconFlow API key (optional)
    - When provided: uses hybrid search (semantic + tag + content search, with semantic results weighted higher)
    - When not provided: uses a two-stage tag + content search (fast and accurate)

### Output Format
Each call returns three parts:
1. **Usage notes**: how to use the copy based on the AI character
2. **Adaptation notes**: specific suggestions for personalized adaptation
3. **Original text**: title, category, content, and tag information
- **Batch generator**: generates multiple copy items at once for comparison

### Analysis & Learning Tools
- **Copy structure analyzer**: analyzes writing techniques and structural characteristics
- **Category info viewer**: learn the features and creation points of each category

## Copy Categories

### Role-play (89 items)
Copy delivered in a specific character's voice (e.g. Qin Shi Huang, Ultraman, a reborn young master), suited to AI role-playing apps.

### Long-form story (70 items)
Copy that uses a complete storyline and emotional buildup to lead into Crazy Thursday, suited to in-depth content creation.

### Current events (61 items)
Copy tied to trending events, internet memes, and social phenomena; it needs regular updates to stay timely.

### Mystery/suspense (51 items)
Copy that grabs attention through suspense, hidden information, and riddles to boost engagement.

### Uncategorized (49 items)
Copy not yet categorized, including short copy and creative pieces.

### Emo literature (5 items)
Literary copy that is emotionally intense, self-expressive, and melancholic, focused on inner monologue and emotional rendering.

### Abstract literature (4 items)
Creative copy with non-sequential logic, stream-of-consciousness, and surrealism, packed with imagination and absurdist flair.

## Targeted Search

### Search modes
- **Tag + content search**: a two-stage intelligent search that needs no API key - fast and precise
  - Stage 1: tag matching to filter candidate copy
  - Stage 2: full-text content matching for ranking
- **Semantic search**: based on the BAAI/bge-m3 model, requires a SiliconFlow API key, understands semantic relationships
- **Hybrid search**: combines semantic search with tag + content search for the best experience

### Getting an API key
1. Visit the [SiliconFlow website](https://siliconflow.cn)
2. Register an account and get an API key
3. Enter the key in the targeted search tool to enable semantic search

### Search tips
- **Concrete topics**: e.g. "work", "dating", "gaming", "studying"
- **Scenario descriptions**: e.g. "company notice", "friends gathering", "exam"
- **Emotional states**: e.g. "starving and freezing", "stressed", "happy"
- **Character identities**: e.g. "programmer", "student", "office worker"
- **Combined keywords**: e.g. "programmer code", "student exam", "sci-fi interstellar"

### Search examples
```
Search "sci-fi" -> finds "Interstellar Chief of Staff seeks help"
Search "starving and freezing" -> finds hardship-help copy containing that phrase
Search "work stress" -> finds workplace complaint copy
```

## Usage Suggestions

1. **Learn the categories first**: use the category info viewer to understand each type's characteristics
2. **Targeted search**: use the targeted search tool based on your specific needs
3. **Analyze and learn**: use the structure analyzer to study the writing techniques of good copy
4. **Create by reference**: adapt original copy based on the generated references
5. **Compare in batches**: use the batch generator to get multiple options for comparison

## Tech Architecture

- **Framework**: Gradio + MCP
- **Data management**: modular data files
- **Utility functions**: full type annotations and documentation
- **Project management**: modern Python project setup (pyproject.toml)

## Project Structure

### Folder + YAML architecture
```
crazy_v_me_50/
├── jokes/              # Core data folder (maintained independently)
│   ├── emo-literary/   # Emotionally intense, melancholic literary copy
│   ├── abstract-literary/ # Non-sequential, surreal creative copy
│   ├── current-events/ # Copy tied to trending events
│   ├── roleplay/       # Copy for various character identities
│   ├── suspense/       # Copy with riddles and hidden info
│   ├── long-story/     # Full storylines
│   └── uncategorized/  # Other creative copy
├── app.py             # MCP server main program
├── data.py            # YAML data loader
├── tools.py           # Core feature implementation
├── requirements.txt   # Dependencies
├── pyproject.toml     # Python project config
├── .gitignore         # Git ignore rules
└── README.md          # Project readme
```

### Data/code separation
- The `jokes` folder can be maintained and version-controlled independently
- Reusable across projects
- Enables team collaboration (content team vs. technical team)

## Troubleshooting

### Common issues

1. **Python path problems**
```bash
   # Check the Python version
   python --version

   # If using a virtual environment
   which python
```

2. **Dependency install failures**
```bash
   # Upgrade pip
   pip install --upgrade pip

   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
```

3. **MCP service won't start**
   - Check whether the path configuration is correct
   - Confirm the Python environment is correct
   - Check the client error logs

4. **Invalid API key**
   - Confirm the key format is correct (starts with sk-)
   - Verify key permissions

## Usage Notes

- This tool provides **reference content**; please create **original work**
- Keep the Crazy Thursday core theme; switching to another brand is not recommended
- Mind the context and audience appropriateness
- Respect others and avoid over-messaging

## Open-Source Collaboration

### How to contribute
- **Content** - submit new copy to the `jokes/` folder
- **Categorization** - improve the copy classification system and tags
- **Technical** - optimize MCP service performance
- **Documentation** - improve docs and examples

### Adding new copy
```yaml
# Create a new YAML file in the corresponding category folder
title: "New copy title"
content: "Copy content"
tags:
  occupation: ["programmer", "student"]
  group: ["young people", "struggling worker"]
  scenario: ["moments", "group chat"]
  emotion: ["funny", "self-deprecating"]
  technique: ["roleplay", "twist & contrast"]
category: "roleplay"
id: "roleplay_017"
```

## License

Apache-2.0 License - supports commercial and non-commercial use

## Acknowledgments

Thanks to all developers who contributed to the creation and implementation of Crazy Thursday copy!
The copy comes from various group chats and social media; please contact us for removal if any copyright issues arise.
Some copy was curated by Bilibili user Saobingmao, from the series about KFC Crazy Thursday copy: https://www.bilibili.com/opus/1012561406475632642?spm_id_from=333.1387.0.0

**Official site: ** [https://www.modelscope.cn/studios/modelscope_mp_460196816/V_me_50](https://www.modelscope.cn/studios/modelscope_mp_460196816/V_me_50)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `productivity`
- Tags: `other`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `mcp-remote https://modelscope-mp-460196816-v-me-50.ms.show/gradio_api/mcp/sse --transport sse-only`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/modelscope-mp-460196816-kfc-v-me-50.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
