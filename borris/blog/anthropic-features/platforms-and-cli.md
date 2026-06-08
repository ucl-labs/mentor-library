<!-- source: claude-platform-on-aws, claude-in-microsoft-foundry, cli quickstart, data-residency — synced 2026-06-09 -->

# Platforms, Deployment & the `ant` CLI

Where you can run Claude and how to deploy it.

## Surfaces
- **Claude API (1P)** — the default. Full feature set, fastest to new features.
- **Claude Platform on AWS** — Claude API on Anthropic-managed infra accessed through AWS, with AWS billing + IAM auth. Same Messages API, Files, Batches, Managed Agents, Skills, code execution. Uses 1P-style model IDs.
- **Amazon Bedrock** — open to all Bedrock customers; global + regional endpoints.
- **Microsoft Foundry** — Claude on Azure with Azure billing + OAuth. Extended thinking, caching, PDF, Files, Skills, tool use. (Opus 4.8 capped at 200k context here.)
- **Google Vertex AI** — global, multi-region, and regional endpoints.

## `ant` CLI
Command-line client for the Claude API: faster interaction, native Claude Code integration, and **versioning of API resources in YAML files** (agents, sessions, memory stores all manageable via `ant beta:*`). Good for scripting Managed Agents.

## Governance / compliance dials (mention when relevant)
- **Data residency** — `inference_geo` controls where inference runs (US-only at 1.1x for newer models).
- **CMEK, Zero Data Retention, compliance API, WIF** — enterprise controls; most live in `_reference/`. Note: Managed Agents is NOT ZDR/HIPAA-eligible (stateful by design).

**Advise like this:** default to the Claude API. Recommend AWS/Foundry/Vertex only when Kristine's client already lives in that cloud or has billing/compliance constraints there. Use the `ant` CLI to script and version Managed Agent setups.
