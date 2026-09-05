---
title: "newsnow"
description: "English | | [!NOTE] This is a demo version currently supporting Chinese only. A full-featured version with better customization and English content support will be released later."
---

# newsnow

English | | [!NOTE] This is a demo version currently supporting Chinese only. A full-featured version with better customization and English content support will be released later.

English | [简体中文](https://github.com/See-lo/newsnow/blob/HEAD/README.zh-CN.md) | [日本語](https://github.com/See-lo/newsnow/blob/HEAD/README.ja-JP.md)

> [!NOTE]
> This is a demo version currently supporting Chinese only. A full-featured version with better customization and English content support will be released later.

**_Elegant reading of real-time and hottest news_**

## Features

- Clean and elegant UI design for optimal reading experience
- Real-time updates on trending news
- GitHub OAuth login with data synchronization
- 30-minute default cache duration (logged-in users can force refresh)
- Adaptive scraping interval (minimum 2 minutes) based on source update frequency to optimize resource usage and prevent IP bans
- support MCP server

```json
{
  "mcpServers": {
    "newsnow": {
      "command": "npx",
      "args": [
        "-y",
        "newsnow-mcp-server"
      ],
      "env": {
        "BASE_URL": "https://newsnow.busiyi.world"
      }
    }
  }
}
```
You can change the `BASE_URL` to your own domain.

## Deployment

### Basic Deployment

For deployments without login and caching:

1. Fork this repository
2. Import to platforms like Cloudflare Page or Vercel

### Cloudflare Page Configuration

- Build command: `pnpm run build`
- Output directory: `dist/output/public`

### GitHub OAuth Setup

1. [Create a GitHub App](https://github.com/settings/applications/new)
2. No special permissions required
3. Set callback URL to: `https://your-domain.com/api/oauth/github` (replace `your-domain` with your actual domain)
4. Obtain Client ID and Client Secret

### Environment Variables

Refer to `example.env.server`. For local development, rename it to `.env.server` and configure:

```env
# Github Client ID
G_CLIENT_ID=
# Github Client Secret
G_CLIENT_SECRET=
# JWT Secret, usually the same as Client Secret
JWT_SECRET=
# Initialize database, must be set to true on first run, can be turned off afterward
INIT_TABLE=true
# Whether to enable cache
ENABLE_CACHE=true
```

### Database Support

Supported database connectors: https://db0.unjs.io/connectors
**Cloudflare D1 Database** is recommended.

1. Create D1 database in Cloudflare Worker dashboard
2. Configure database_id and database_name in wrangler.toml
3. If wrangler.toml doesn't exist, rename example.wrangler.toml and modify configurations
4. Changes will take effect on next deployment

### Docker Deployment

In project root directory:

```sh
docker compose up
```

You can also set Environment Variables in `docker-compose.yml`.

## Development

> [!Note]
> Requires Node.js >= 20

```sh
corepack enable
pnpm i
pnpm dev
```

### Adding Data Sources

Refer to `shared/sources` and `server/sources` directories. The project provides complete type definitions and a clean architecture.

For detailed instructions on how to add new sources, see [CONTRIBUTING.md](https://github.com/See-lo/newsnow/blob/HEAD/CONTRIBUTING.md).

## Roadmap

- Add **multi-language support** (English, Chinese, more to come).
- Improve **personalization options** (category-based news, saved preferences).
- Expand **data sources** to cover global news in multiple languages.

**_release when ready_**
![](/mcp-assets/2197d28504147a4aea26ca6d6a172b1b.gif)

## Contributing

Contributions are welcome! Feel free to submit pull requests or create issues for feature requests and bug reports.

See [CONTRIBUTING.md](https://github.com/See-lo/newsnow/blob/HEAD/CONTRIBUTING.md) for detailed guidelines on how to contribute, especially for adding new data sources.

## License

[MIT](https://github.com/See-lo/newsnow/blob/HEAD/LICENSE) © ourongxing

**Official site: ** [https://github.com/See-lo/newsnow](https://github.com/See-lo/newsnow)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `entertainment and media`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y newsnow-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/seeloqaq-newsnow.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
