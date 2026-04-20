---
# === CORE IDENTIFICATION ===
concept: Deno Deploy
slug: deno-deploy

# === CLASSIFICATION ===
category: deploy
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/index.md"
chapter_number: null
pdf_page: null
section: "What is Deno Deploy?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deploy"
  - "Deno Deploy v2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deploy-builds
  - deploy-observability
  - deploy-timelines
  - deploy-framework-support
  - deno-sandbox
contrasts_with:
  - deploy-classic

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Deno Deploy?"
  - "How do I deploy to Deno Deploy?"
  - "What distinguishes Deno Deploy from Deploy Classic?"
---

# Quick Definition
Deno Deploy is a serverless platform for running JavaScript and TypeScript applications in the cloud or self-hosted, with a built-in CI/CD pipeline, GitHub integration, and a management dashboard at console.deno.com.

# Core Definition
Deno Deploy is a serverless platform for deploying and running JavaScript and TypeScript applications at global scale. It provides a management plane with built-in CI, GitHub Actions integration, and a web dashboard at console.deno.com. Applications execute using a standard Deno 2.0 runtime in secure, isolated Linux environments. Deno Deploy is a complete rework of Deploy Classic, featuring a new dashboard, full Deno and Node.js support (including FFI, subprocesses, native addons), first-class framework support for Next.js/Astro/SvelteKit/Fresh, CDN caching, environment variable contexts (dev/prod), tracing, metrics, and self-hostable regions.

# Prerequisites
- deno -- Understanding of the Deno runtime is helpful for deploying applications

# Key Properties
1. **Serverless execution** -- Applications start on demand, scale automatically, and stop when idle; cold starts complete within 100ms for hello-world apps
2. **Full Deno 2.0 runtime** -- Runs with `--allow-all` permissions; supports FFI, subprocesses, file system writes, and full npm compatibility
3. **Built-in CI/CD** -- Integrated build system with live-streamed logs, automatic GitHub deployment on push, and CLI deployment via `deno deploy`
4. **Framework first-class support** -- Auto-detects and optimizes Next.js, Astro, SvelteKit, Fresh, Nuxt, and more
5. **CDN caching** -- Built-in HTTP edge caching with tag-based invalidation
6. **Environment contexts** -- Separate Production and Development variable sets with secret support
7. **Observability** -- Logs, distributed traces, and metrics via OpenTelemetry integration
8. **Instant rollback** -- Timeline-based deployment history with one-click rollback to any previous revision
9. **Self-hostable regions** -- Supported (not available in Deploy Classic)

# Construction / Recognition
- Access via console.deno.com
- Create an organization, then create applications within it
- Deploy from GitHub repository or via `deno deploy create` CLI
- Each app is identified by a slug, gets a default domain at `<app>.<org>.deno.net`
- Applications are web services with build history, environment variables, and custom domains

# Context & Application
Deno Deploy is the production hosting platform for Deno applications and compatible Node.js/framework applications. It is suitable for API servers, server-side rendered applications, static sites, and scheduled tasks. The platform manages the full lifecycle from code push through build, deployment, and monitoring. Organizations can host multiple applications, each with isolated environments for production and development.

# Examples
From deploy/index.md:
- "Deno Deploy is a serverless platform for running JavaScript and TypeScript applications in the cloud (or self-hosted on your own infrastructure)."
- "It provides a management plane for deploying and running applications with the built-in CI or through integrations such as GitHub actions."
- Deploy Classic sunsetting July 20, 2026; migration guide available

From deploy/getting_started.md:
- Build stages: Prepare, Install, Build, Warm up, Route
- App creation via dashboard or `deno deploy create` CLI with flags for org, app, source, framework preset

# Relationships
## Builds Upon
- deno (the runtime that executes deployed code)

## Enables
- deploy-builds
- deploy-timelines
- cdn-caching
- deploy-cron
- deploy-databases
- deploy-observability
- custom-domains
- deploy-framework-support

## Related
- deno-sandbox (complementary product sharing the same organization boundary)

## Contrasts With
- Deploy Classic (legacy platform at dash.deno.com; limited Deno/Node support, no CDN caching, no tracing/metrics, no self-hostable regions)

# Common Errors
1. Confusing Deploy Classic (dash.deno.com) with Deno Deploy (console.deno.com) -- they are separate platforms with different capabilities
2. Expecting custom Deno flags at runtime -- custom flags cannot be passed to the Deno runtime on Deploy

# Common Confusions
1. **Deploy vs. Sandbox** -- Deploy runs persistent serverless applications that serve HTTP traffic; Sandbox provides ephemeral microVMs for running arbitrary code
2. **Regions** -- Deno Deploy currently has 2 regions (vs. Deploy Classic's 6), but supports self-hostable regions

# Source Reference
- deploy/index.md: Platform overview, Deploy Classic comparison table
- deploy/getting_started.md: Step-by-step app creation, build stages, monitoring

# Verification Notes
- High confidence: Explicitly defined in source with detailed feature comparison
- All claims verified against the Deploy Classic comparison table and getting started guide
