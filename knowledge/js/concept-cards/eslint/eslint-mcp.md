---
# === CORE IDENTIFICATION ===
concept: ESLint MCP Server
slug: eslint-mcp

# === CLASSIFICATION ===
category: integration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "ESLint Documentation"
source_slug: eslint
authors: "ESLint Contributors"
chapter: "use/mcp.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ESLint Model Context Protocol"
  - "ESLint AI integration"
  - "@eslint/mcp"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - eslint-getting-started
extends: []
related:
  - eslint-cli
  - eslint-editor-integrations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the ESLint MCP server and how does it work?"
  - "How do I configure ESLint MCP in VS Code, Cursor, or Windsurf?"
  - "How can AI agents use ESLint via MCP?"
---

# Quick Definition
The ESLint MCP (Model Context Protocol) server enables AI models and agents to interact with ESLint through a standardized interface, allowing LLMs to lint, fix, and explain ESLint issues directly within supported editors.

# Core Definition
MCP (Model Context Protocol) is an open standard enabling AI models to interact with external tools through a unified interface. ESLint includes a built-in MCP server, started via `npx @eslint/mcp@latest` or the `--mcp` CLI flag. The server uses stdio transport and can be registered with AI-enabled editors (VS Code with Copilot Chat, Cursor, Windsurf) to allow LLMs to invoke ESLint directly. In VS Code, configuration is placed in `.vscode/mcp.json`; in Cursor, in `.cursor/mcp.json`; in Windsurf, in `~/.codeium/windsurf/mcp_config.json`. Once configured, users can prompt the AI to lint files, fix issues, and explain rule violations through natural language.

# Prerequisites
- eslint-getting-started -- ESLint must be installed in the project

# Key Properties
1. **@eslint/mcp** -- The MCP server package; invoked via `npx @eslint/mcp@latest`
2. **stdio transport** -- Communication between editor and server uses standard input/output
3. **VS Code setup** -- `.vscode/mcp.json` with `{ "servers": { "ESLint": { "type": "stdio", "command": "npx", "args": ["@eslint/mcp@latest"] } } }`
4. **Cursor setup** -- `.cursor/mcp.json` with `{ "mcpServers": { "eslint": { "command": "npx", "args": ["@eslint/mcp@latest"] } } }`
5. **Windsurf setup** -- `~/.codeium/windsurf/mcp_config.json` with same mcpServers structure
6. **Agent mode required** -- In VS Code, requires Copilot Chat with agent mode enabled
7. **Workspace or user scope** -- Can be configured per-workspace or globally in user settings
8. **--mcp CLI flag** -- Alternative way to start the MCP server from the ESLint CLI

# Construction / Recognition
VS Code `.vscode/mcp.json`:
```json
{
  "servers": {
    "ESLint": {
      "type": "stdio",
      "command": "npx",
      "args": ["@eslint/mcp@latest"]
    }
  }
}
```

Example AI prompts:
- "Check this file for linting errors"
- "Fix all ESLint issues in the current file"
- "Show me what ESLint rules are being violated"
- "Lint and fix #file:index.js"

# Context & Application
The MCP server bridges ESLint and the emerging AI-assisted development workflow. Rather than running ESLint manually or relying on editor extension highlights, developers can ask AI agents to lint, explain, and fix code in natural language. This is particularly useful for understanding unfamiliar rule violations and performing bulk fixes across files.

# Examples
From use/mcp.md:
- VS Code: Create `.vscode/mcp.json`, enable agent mode in Copilot Chat, toggle ESLint MCP tools
- Cursor: Create `.cursor/mcp.json`, verify tools appear in MCP settings
- Windsurf: Configure via Advanced Settings, add server to `mcp_config.json`
- Troubleshooting: Run `MCP: List Servers` from VS Code Command Palette to check status

# Relationships
## Builds Upon
- eslint-getting-started (ESLint must be installed and configured)
## Related
- eslint-cli (MCP server can be started via `--mcp` flag)
- eslint-editor-integrations (MCP complements traditional editor extensions)

# Common Errors
1. Not having Copilot Chat extension installed in VS Code -- required for MCP support
2. Forgetting to toggle on ESLint MCP tools in the editor's tool selector

# Common Confusions
1. **MCP vs ESLint extension** -- The ESLint extension provides traditional highlighting; MCP enables AI-agent interaction with ESLint
2. **@eslint/mcp vs --mcp** -- `@eslint/mcp` is the dedicated package; `--mcp` is a CLI flag that starts the server

# Source Reference
- use/mcp.md: Complete MCP server setup for VS Code, Cursor, and Windsurf with troubleshooting

# Verification Notes
Directly documented with configuration examples for three editors. High confidence.
