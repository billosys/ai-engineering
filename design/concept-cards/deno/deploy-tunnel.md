---
# === CORE IDENTIFICATION ===
concept: Deploy Tunnel
slug: deploy-tunnel

# === CLASSIFICATION ===
category: deploy
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/tunnel.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "--tunnel"
  - "local tunnel"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - environment-variables-and-contexts
  - deploy-observability
  - deploy-databases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I expose my local dev server through Deno Deploy?"
  - "How do I connect to Deploy databases during local development?"
---

# Quick Definition
The `--tunnel` flag securely exposes a local Deno development server to the internet via a Deno Deploy public URL, while also pulling "Local" context environment variables, pushing OpenTelemetry data to the Deploy dashboard, and connecting to hosted development databases.

# Core Definition
Deno Deploy's tunnel feature allows developers to securely expose their local development server to the internet by passing the `--tunnel` flag when running Deno locally (`deno run --tunnel` or `deno task --tunnel`). On first use, it prompts for authentication and app selection. Once established, the tunnel provides a public URL forwarding traffic to the local server, pulls environment variables from the "Local" context, pushes OpenTelemetry traces/metrics/logs to the Deploy dashboard, and automatically connects to local development databases assigned to the app.

# Prerequisites
- deno-deploy -- Tunnels connect to a Deno Deploy application

# Key Properties
1. **Public URL** -- Secure HTTPS URL that forwards traffic to local development server
2. **Environment variable injection** -- "Local" context variables from Deploy pulled into the local Deno process
3. **Observability push** -- Local traces, metrics, and logs appear in the Deploy dashboard (filter with `context:local`)
4. **Database connection** -- Automatically injects hosted isolated local development database credentials
5. **Simple activation** -- `deno run --tunnel -A main.ts` or `deno task --tunnel dev`
6. **Active tunnel listing** -- "Tunnels" tab in app dashboard shows all connected tunnels with URLs and connection times
7. **Stop by terminating** -- Closing the Deno process closes the tunnel

# Construction / Recognition
```bash
# Run with tunnel
deno run --tunnel -A main.ts
# Or with tasks
deno task --tunnel dev
```
First run prompts for authentication and app selection.

# Context & Application
Tunnels are useful for testing webhooks from external services (Stripe, GitHub), sharing work with collaborators, and developing against production-like database environments. The observability integration means local development sessions appear in the same dashboard as production, enabling consistent debugging workflows. For teams not wanting the full tunnel feature set, a local database instance is an alternative.

# Examples
From deploy/reference/tunnel.md:
- "The first time you run this command, you'll be prompted to authenticate with Deno Deploy and choose which Deno Deploy app you want to connect the tunnel to."
- Filter local telemetry: `context:local` in the search bar
- "When using the tunnel feature, the 'Local' context environment variables from your Deno Deploy application are made available to your local Deno process."

# Relationships
## Builds Upon
- deno-deploy (tunnels connect to Deploy apps)

## Related
- environment-variables-and-contexts ("Local" context variables injected)
- deploy-observability (local traces/logs pushed to dashboard)
- deploy-databases (automatic connection to hosted dev databases)

# Common Errors
1. Expecting tunnel without authentication -- first run requires Deploy authentication and app selection

# Common Confusions
1. **Tunnel vs. deploy** -- Tunnel exposes your local server temporarily for development; deploying publishes code to Deploy's infrastructure permanently

# Source Reference
- deploy/reference/tunnel.md: Complete tunnel feature documentation

# Verification Notes
- High confidence: Feature explicitly documented with usage examples and capability list
