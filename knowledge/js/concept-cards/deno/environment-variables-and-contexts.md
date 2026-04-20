---
# === CORE IDENTIFICATION ===
concept: Environment Variables and Contexts
slug: environment-variables-and-contexts

# === CLASSIFICATION ===
category: deploy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/env_vars_and_contexts.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "env vars"
  - "contexts"
  - "secrets"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - deploy-timelines
  - deploy-builds
  - deploy-databases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure environment variables on Deno Deploy?"
  - "What are contexts in Deno Deploy?"
---

# Quick Definition
Deno Deploy environment variables are scoped to contexts (Production, Development, Build) at application or organization level, supporting plain text and secret types, with predefined platform variables automatically available.

# Core Definition
Environment variables in Deno Deploy configure applications with static values such as API keys or connection strings. Variables can be plain text (visible in UI) or secrets (write-only after creation). They are scoped to contexts -- Production (production timeline), Development (preview/branch URLs), and Build (build process only). Variables can be set at application level or organization level (organization variables apply to all apps but can be overridden). The same variable name cannot appear twice in the same context, but can exist in different non-overlapping contexts. Access in code via `Deno.env.get("MY_ENV_VAR")`.

# Prerequisites
- deno-deploy -- Environment variables are a Deno Deploy platform feature

# Key Properties
1. **Two types** -- Plain text (visible in UI) and secrets (never visible after creation)
2. **Three contexts** -- Production, Development, Build (Build context is isolated from runtime contexts)
3. **Two levels** -- Application-level and organization-level (app overrides org)
4. **Bulk import** -- Import from `.env` file format (lines starting with `#` are comments)
5. **Key limits** -- Max 128 bytes; cannot start with `DENO_` (with exceptions), `LD_`, or `OTEL_`; max 16 KB value size
6. **Predefined variables** -- `DENO_DEPLOY=true`, `DENO_DEPLOY_ORGANIZATION_SLUG`, `DENO_DEPLOY_APPLICATION_SLUG`, `DENO_DEPLOYMENT_ID`, `DENO_TIMELINE`
7. **Reserved keys** -- Cloud connection keys (AWS_ROLE_ARN, GCP_*, AZURE_*) must use Cloud Connections feature

# Construction / Recognition
- Manage from app creation page, app settings, or organization settings
- Add: name, value, secret toggle, context selection
- Access: `Deno.env.get("MY_ENV_VAR")`
- `DENO_TIMELINE` values: `production`, `git-branch/<branch-name>`, `preview/<revision-id>`

# Context & Application
Environment variables enable configuration separation between development and production environments. Secrets protect sensitive values like API keys. The Build context isolation ensures that build-time configuration (e.g., npm tokens) does not leak into runtime, and vice versa. Organization-level variables enable shared configuration across all applications.

# Examples
From deploy/reference/env_vars_and_contexts.md:
- "Environment variables in the Build context are only available during builds and aren't accessible in Production or Development contexts (and vice versa)."
- Predefined: `DENO_DEPLOY=true`, `DENO_TIMELINE=production`
- During builds: `CI=1` is additionally set

# Relationships
## Builds Upon
- deno-deploy (env vars are a platform feature)

## Related
- deploy-timelines (contexts correspond to timelines)
- deploy-builds (Build context provides build-time configuration)
- deploy-databases (database credentials auto-injected as env vars)

# Common Errors
1. Using reserved key prefixes (`DENO_`, `LD_`, `OTEL_`) -- these are blocked with specific exceptions
2. Expecting Build context vars at runtime or vice versa -- contexts are strictly isolated

# Common Confusions
1. **Context vs. timeline** -- Contexts are logical groupings for env vars; timelines are deployment history tracks. Production context maps to the production timeline; Development context maps to all non-production timelines.

# Source Reference
- deploy/reference/env_vars_and_contexts.md: Complete environment variables and contexts documentation

# Verification Notes
- High confidence: Explicitly documented with limits, predefined variables, and context model
