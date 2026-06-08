<!-- source: mcp-connector, remote-mcp-servers, mcp-tunnels — synced 2026-06-09 -->

# MCP (Model Context Protocol) — connect external tools

**What it is:** The open standard for plugging Claude into external systems (CRMs, GitHub, Slack, databases, your own services). An MCP server exposes tools/resources; Claude calls them.

**When to recommend it:** any time the build needs to touch a real outside system. "Connect it via MCP" is the answer for tool/data integration.

## Ways to use it
- **MCP connector (Messages API)** — connect to remote MCP servers directly from a `/v1/messages` call. GA/beta depending on surface.
- **Remote MCP servers** — Anthropic-hosted and third-party servers you point Claude at by URL.
- **MCP in Claude Code** — add servers locally; tools appear as `mcp__<server>__*`.
- **MCP tunnels** (research preview) — reach MCP servers inside your private network without exposing them publicly.
- **In Managed Agents** — MCP servers are agent-scoped; pair with vault credentials (session-scoped) for auth.

## Scaling
Big MCP setups (200+ tools) blow the context budget. Combine with the **tool search tool** + `defer_loading` (see `tools-overview.md`) so only the needed tools load.

**Advise like this:** "Expose your CRM/warehouse as an MCP server and connect it." "You've got many MCP servers — add tool search so definitions don't eat 55k tokens before any work happens." For private networks, mention MCP tunnels.
