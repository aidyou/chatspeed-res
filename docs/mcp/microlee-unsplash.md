---
title: "unsplash-server"
description: "Unsplash MCP Server An Unsplash tool server based on the Model Context Protocol, providing 15 tools for search, photo details, random photos, collections, topics, and users. Feature List Photo-related…"
---

# unsplash-server

Unsplash MCP Server An Unsplash tool server based on the Model Context Protocol, providing 15 tools for search, photo details, random photos, collections, topics, and users. Feature List Photo-related…

# Unsplash MCP Server

An Unsplash tool server based on the Model Context Protocol, providing 15 tools for search, photo details, random photos, collections, topics, and users.

## Feature List

### Photo-related Tools (Photos)
- **search_photos** - Search Unsplash photos by keyword, supporting pagination, sorting, color filtering, and orientation filtering
- **get_photo** - Get detailed information of a single photo by its ID, including author, dimensions, download link, etc.
- **list_photos** - List the latest, most popular, or oldest photos on Unsplash, supporting pagination
- **get_random_photo** - Get a random photo, with options to filter by keyword, collection, topic, user, etc.
- **track_download** - Track photo download events (required by the Unsplash API), must be called when a user downloads a photo

### Collection-related Tools (Collections)
- **list_collections** - List photo collections on Unsplash, supporting paginated browsing
- **get_collection** - Get detailed information of a collection by its ID, including title, description, number of photos, etc.
- **get_collection_photos** - Get all photos in a specified collection, supporting pagination and orientation filtering

### Topic-related Tools (Topics)
- **list_topics** - List all topic categories on Unsplash, supporting sorting by newest, oldest, or location
- **get_topic** - Get detailed information of a topic by its ID or slug
- **get_topic_photos** - Get photos under a specified topic, supporting pagination, sorting, and orientation filtering

### User-related Tools (Users)
- **get_user** - Get public information of an Unsplash user by username, including bio, number of works, etc.
- **get_user_photos** - Get all photos uploaded by a specified user, supporting pagination, sorting, and orientation filtering
- **get_user_likes** - Get a list of photos liked (favorited) by a specified user, supporting pagination, sorting, and orientation filtering
- **get_user_collections** - Get a list of photo collections created by a specified user, supporting pagination

## Installation and Build
```bash
npm install
npm run build
```
## Running
```bash
UNSPLASH_ACCESS_KEY=your_key node build/index.js
```
## MCP Configuration Example
```json
{
    "mcpServers": {
        "unsplash": {
            "command": "npx",
            "args": [
                "-y",
                "@microlee666/unsplash-mcp-server"
            ],
            "env": {
                "UNSPLASH_ACCESS_KEY": ""
            },
            "disabled": false,
            "alwaysAllow": [],
            "disabledTools": []
        }
    }
}
```
## Publishing to npm
You need to log in to npm and ensure that the package name is not already taken:
```bash
npm login
npm publish --registry https://registry.npmjs.org
```

**Official site: ** [https://unsplash.com/](https://unsplash.com/)
**Status: ** `active`　**Last verified: ** `2026-08-30`

## Categories & Tags

- Categories: `media`
- Tags: `search`, `art and culture`, `chinese`

## MCP Configuration

- Transport: `stdio`
- Command: `npx`
- Args: `-y @microlee666/unsplash-mcp-server`

This config can be imported into ChatSpeed from the resource index. Verify the command, arguments, and permission source are trustworthy before importing.

## Data source

Resource file: `resources/mcp/microlee-unsplash.json`. Content last verified on `2026-08-30`; free quotas and service limits may change with official policies.
