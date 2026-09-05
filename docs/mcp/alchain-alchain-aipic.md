---
title: "alchain_aipic"
description: "AI Image Generation MCP Server An AI image generation server based on the Model Context Protocol (MCP), specifically designed for automatically analyzing web pages and article content to generate corr…"
---

# alchain_aipic

AI Image Generation MCP Server An AI image generation server based on the Model Context Protocol (MCP), specifically designed for automatically analyzing web pages and article content to generate corr…

# AI Image Generation MCP Server

An AI image generation server based on the Model Context Protocol (MCP), specifically designed for automatically analyzing web pages and article content to generate corresponding AI images.

## Features

### 🎯 Core Features
1. **Intelligent Web Page Analysis**: Automatically analyzes HTML content to identify areas that require images.
2. **Article Illustration Generation**: Analyzes the content of articles to generate illustrations for key paragraphs.
3. **AI Image Generation**: Uses the FLUX model to generate high-quality images.
4. **English Prompt Optimization**: Automatically converts Chinese descriptions into English prompts suitable for AI generation.
5. **HTML Enhancement**: Automatically embeds generated images into the original web page.

### 🛠️ Provided Tools

#### 1. analyze-and-generate-webpage-images
- **Function**: Analyzes the HTML content of a web page and generates corresponding images.
- **Parameters**:
  - `html`: The HTML content of the web page.
  - `generateImages`: Whether to immediately generate images (default: true).

#### 2. analyze-and-generate-article-images
- **Function**: Analyzes the content of an article and generates illustrations.
- **Parameters**:
  - `content`: The content of the article.
  - `title`: The title of the article (optional).
  - `generateImages`: Whether to immediately generate images (default: true).

#### 3. generate-single-image
- **Function**: Generates a single image based on a prompt.
- **Parameters**:
  - `prompt`: The English prompt.
  - `width`: The width of the image (default: 1024).
  - `height`: The height of the image (default: 1024).
  - `model`: The name of the model to use (optional).

#### 4. generate-enhanced-webpage
- **Function**: Embeds generated images into the original HTML.
- **Parameters**:
  - `originalHtml`: The original HTML content.
  - `imageMapping`: A mapping from image IDs to URLs.

#### 5. translate-prompt-to-english
- **Function**: Translates Chinese descriptions into English prompts.
- **Parameters**:
  - `chinesePrompt`: The Chinese prompt or description.
  - `style`: The style of the image (optional).

### 📊 Provided Resources

#### 1. generated-images
- **URI**: `generated://images`
- **Function**: Retrieves information about all generated AI images.

#### 2. generation-stats
- **URI**: `stats://generation`
- **Function**: Retrieves statistical information about image generation.

## Installation and Usage

### 1. Install Dependencies
```bash
npm install
```
### 2. Compile TypeScript
```bash
npm run build
```
### 3. Run the Server
```bash
npm start
```
### 4. Development Mode
```bash
npm run dev
```
## Configuring MCP Client

### Claude Desktop Configuration
Add the following to the configuration file of Claude Desktop:

```json

{

  "mcpServers": {

    "ai-image-generator": {

      "command": "node",

      "args": ["/path/to/your/ai-image-generator-mcp-server/dist/index.js"],

      "env": {

        "MODELSCOPE_API_KEY": "your-modelscope-api-key-here"

      }

    }

  }

}

```
**Important**: Replace `"your-modelscope-api-key-here"` with your actual ModelScope API key.

### Other MCP Clients
Configure this server according to the method used by your MCP client, and set the API key in the environment variables.

## API Key Configuration

### 1. Obtain ModelScope API Key
1. Visit [ModelScope](https://modelscope.cn/)
2. Register and log in to your account
3. Go to Personal Center → API Management
4. Create a new API key
5. Copy the API key (format: `ms-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`)

### 2. Configure Environment Variables
Set the API key in the `env` section of the MCP client configuration file. This configuration is long-term and similar to how Google Maps is configured.

## Usage Examples

After configuring the API key, you can directly use the tools in the MCP client without passing the API key again:

### 1. Analyze Web Page and Generate Images
```typescript
// Call via the MCP client
const result = await mcpClient.callTool("analyze-and-generate-webpage-images", {
  html: "

My website
 alt='Homepage image'>
",
  generateImages: true
});
```
### 2. Generate Illustrations for an Article
```typescript
const result = await mcpClient.callTool("analyze-and-generate-article-images", {
  content: "AI technology is developing rapidly...",
  title: "AI technology development trends"
});
```
### 3. Generate a Single Image
```typescript
const result = await mcpClient.callTool("generate-single-image", {
  prompt: "A beautiful landscape with mountains and lake, photorealistic, high quality",
  width: 1024,
  height: 768
});
```
## Technical Architecture

### Core Components
- **ImageGenerator**: Responsible for interacting with the ModelScope API to generate AI images.
- **ContentAnalyzer**: Analyzes web page and article content to identify image requirements.
- **AIImageGeneratorMCPServer**: The main server class that handles MCP protocol communication.

### Supported Image Formats
- Width: 200-1200 pixels
- Height: 200-1200 pixels
- Format: JPEG, PNG

### AI Models Used
- Default Model: `MusePublic/489_ckpt_FLUX_1`
- Custom models are supported (must be available on the ModelScope platform)

## Advanced Features

### Intelligent Content Analysis
- Automatically identifies image placeholders in web pages.
- Generates relevant image descriptions based on context.
- Infers image dimensions and styles intelligently.

### Prompt Optimization
- Automatically converts Chinese descriptions into English.
- Adds quality and style descriptors.
- Optimizes prompts based on the content context.

### Batch Processing
- Supports generating multiple images simultaneously.- Asynchronous processing to improve efficiency
- Error handling and retry mechanism

## Error Handling

The server includes a comprehensive error handling mechanism:
- Error messages when API calls fail
- Handling of network connection issues
- Validation for invalid parameters
- Detailed error logging

## Performance Optimization

- Asynchronous image generation
- Caching generated image information in memory
- Batch processing optimization
- Retry mechanism for errors

## Scalability

### Adding New Image Generation Models
Add support for new models in the `ImageGenerator` class:

```typescript

const newModel = 'your-new-model-id';

const response = await this.generateImage({

  prompt: "your prompt",

  model: newModel

});

```
### Adding New Analysis Algorithms
Extend analysis capabilities in the `ContentAnalyzer` class:

```typescript

private customAnalyzer(content: string): AnalysisResult {

  // implement custom analysis logic

}

```
## Contribution Guidelines

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Contact

If you have any questions or suggestions, please contact us through the following methods:
- Create an Issue
- Submit a Pull Request

## Changelog

### v1.0.0
- Initial version release
- Support for web page and article analysis
- Integration of the FLUX image generation model
- Full MCP protocol support provided

**Official site: ** [https://github.com/alchaincyf/AIpic](https://github.com/alchaincyf/AIpic)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `browser`
- Tags: `browser automation`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `node`
- Args: `/path/to/your/ai-image-generator-mcp-server/dist/index.js`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/alchain-alchain-aipic.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
