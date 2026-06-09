# brave/brave-search-mcp-server

## Metadata
- Stars: 1166
- Primary language: TypeScript
- Default branch: main
- Latest release: v2.0.83 (2026-06-01)
- License: MIT License
- Homepage: (none)
- Fetched: 2026-06-09
- Final URL: https://github.com/brave/brave-search-mcp-server

## Description

An MCP server implementation that integrates the Brave Search API, providing comprehensive search capabilities including web search, local business search, place search, image search, video search, news search, LLM context, and AI-powered summarization. Supports both STDIO and HTTP transports, with STDIO as the default mode.

## README

# Brave Search MCP Server

An MCP server implementation that integrates the Brave Search API, providing comprehensive search capabilities including web search, local business search, place search, image search, video search, news search, LLM context, and AI-powered summarization. This project supports both STDIO and HTTP transports, with STDIO as the default mode.

## Migration

### 1.x to 2.x

#### Default transport now STDIO

To follow established MCP conventions, the server now defaults to STDIO. If you would like to continue using HTTP, you will need to set the `BRAVE_MCP_TRANSPORT` environment variable to `http`, or provide the runtime argument `--transport http` when launching the server.

#### Response structure of `brave_image_search`

Version 1.x of the MCP server would return base64-encoded image data along with image URLs. Version 2.x removes the base64-encoded data and returns a response object that more closely reflects the original Brave Search API response.

## Tools

### Web Search (`brave_web_search`)
Performs comprehensive web searches with rich result types and advanced filtering options.

**Parameters:**
- `query` (string, required): Search terms (max 400 chars, 50 words)
- `country` (string, optional): Country code (default: "US")
- `search_lang` (string, optional): Search language (default: "en")
- `ui_lang` (string, optional): UI language (default: "en-US")
- `count` (number, optional): Results per page (1-20, default: 10)
- `offset` (number, optional): Pagination offset (max 9, default: 0)
- `safesearch` (string, optional): Content filtering ("off", "moderate", "strict", default: "moderate")
- `freshness` (string, optional): Time filter ("pd", "pw", "pm", "py", or date range)
- `text_decorations` (boolean, optional): Include highlighting markers (default: true)
- `spellcheck` (boolean, optional): Enable spell checking (default: true)
- `result_filter` (array, optional): Filter result types
- `goggles` (array, optional): Custom re-ranking definitions
- `units` (string, optional): Measurement units ("metric" or "imperial")
- `extra_snippets` (boolean, optional): Get additional excerpts (Pro plans only)
- `summary` (boolean, optional): Enable summary key generation for AI summarization

### Local Search (`brave_local_search`)
Searches for local businesses and places with detailed information including ratings, hours, and AI-generated descriptions. Requires Pro plan for full capabilities; falls back to web search otherwise.

### Video Search (`brave_video_search`)
Searches for videos with comprehensive metadata and thumbnail information. Count up to 50, offset max 9.

### Image Search (`brave_image_search`)
Searches for images. Count 1-200, default 50. Returns URL-based references (v2.x removed base64 encoding).

### News Search (`brave_news_search`)
Searches for current news articles with freshness controls and breaking news indicators. Defaults to `freshness: "pd"` (last 24 hours).

### Summarizer Search (`brave_summarizer`)
Generates AI-powered summaries from web search results. Requires a summary key from a prior web search with `summary: true`.

### Place Search (`brave_place_search`)
Searches for points of interest in a geographic area. Parameters include `query`, `latitude`, `longitude`, `location` string, `radius`, `count` (1-50), country, language, units, safesearch.

### LLM Context (`brave_llm_context`)
Retrieves pre-extracted web content optimized for AI agents, LLM grounding, and RAG pipelines.

**Parameters:**
- `query` (string, required): Search query (max 400 chars, 50 words)
- `count` (number, optional): Maximum results considered (1-50)
- `maximum_number_of_urls` (number, optional): Max URLs (1-50)
- `maximum_number_of_tokens` (number, optional): Approx max context tokens (1024-32768)
- `maximum_number_of_snippets` (number, optional): Max snippets (1-256)
- `context_threshold_mode` (string, optional): "disabled", "strict", "lenient", "balanced"
- `maximum_number_of_tokens_per_url` (number, optional): Max tokens per URL (512-8192)
- `goggles` (string or array, optional): Custom re-ranking
- `freshness` (string, optional): Time filter
- `enable_local` (boolean, optional): Enable local recall
- `enable_source_metadata` (boolean, optional): Include source metadata enrichment

## Configuration

### Environment Variables
- `BRAVE_API_KEY`: Your Brave Search API key (required)
- `BRAVE_MCP_TRANSPORT`: Transport mode ("http" or "stdio", default: "stdio")
- `BRAVE_MCP_PORT`: HTTP server port (default: 8000)
- `BRAVE_MCP_HOST`: HTTP server host (default: "0.0.0.0")
- `BRAVE_MCP_LOG_LEVEL`: Logging level
- `BRAVE_MCP_ENABLED_TOOLS`: Space-separated whitelist for tools
- `BRAVE_MCP_DISABLED_TOOLS`: Space-separated blacklist for tools
- `BRAVE_MCP_STATELESS`: HTTP stateless mode (set to "true" for Amazon Bedrock AgentCore)

### Installation with Claude Desktop

#### Docker
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "BRAVE_API_KEY", "docker.io/mcp/brave-search"],
      "env": { "BRAVE_API_KEY": "YOUR_API_KEY_HERE" }
    }
  }
}
```

#### NPX
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server", "--transport", "http"],
      "env": { "BRAVE_API_KEY": "YOUR_API_KEY_HERE" }
    }
  }
}
```

### Build
```bash
npm install
npm run build
```

## Top-level structure
- dir .github
- file .gitignore, .prettierignore, .prettierrc
- file Dockerfile, docker-compose.yml
- file LICENSE, README.md
- file glama.json, marketplace-revision-release.json
- file package-lock.json, package.json, server.json, tsconfig.json
- dir src (TypeScript source)
