<!-- source: tool-use overview, tool-search, programmatic-tool-calling, code-execution, web-search, web-fetch, batch — synced 2026-06-09 -->

# Tools Overview (server tools + scaling tool use)

Claude's tool use is GA across all models. Beyond your own custom tools, Anthropic ships server-side tools and scaling features.

## Server tools (Anthropic-hosted, no infra)
- **Web search** — live web data with citations. GA. Returns rich SEC filing data for financial research.
- **Web fetch** — pull full content from a URL or PDF.
- **Code execution** — Claude runs Bash/Python in a sandbox, manipulates files. **Free when used with web search or web fetch.** Required for Skills.
- **Computer use** — Claude controls a screen (click, type, scroll). Supported on Opus 4.8.
- **Memory tool**, **text editor**, **bash** — GA building blocks.

## Tool search tool (for big tool catalogs)
When you have 10+ tools (or a multi-server MCP setup that eats 50k+ tokens), don't load all definitions upfront. Mark tools `defer_loading: true`; Claude searches the catalog (regex or BM25 variant) and loads only the 3–5 it needs.
- Cuts tool-definition context **85%+**; keeps selection accuracy high past 30–50 tools (up to 10,000).
- Preserves prompt caching (deferred tools aren't in the prefix).
- Keep your 3–5 most-used tools non-deferred.

## Programmatic tool calling
Claude calls tools from *within* code execution instead of one-at-a-time round trips — cuts latency and tokens in multi-tool workflows. GA.

## Other
- **Parallel tool use** — multiple tools in one turn (default on; disable with `disable_parallel_tool_use`).
- **Fine-grained tool streaming**, **strict tool use** (schema-validated inputs) — GA.
- **Message Batches API** — process huge volume async at **50% off**; up to 300k output tokens with a beta header.

**Advise like this:** "Use web search + code execution (free together) for research." "You have 40 MCP tools — turn on the tool search tool with defer_loading so they don't eat your context." "Batch it" for high-volume non-realtime jobs.
