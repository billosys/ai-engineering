---
# === CORE IDENTIFICATION ===
concept: Deploy Builds
slug: deploy-builds

# === CLASSIFICATION ===
category: deploy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/builds.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "revisions"
  - "build system"
  - "Deploy build pipeline"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - deploy-timelines
  - deploy-framework-support
  - environment-variables-and-contexts
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I deploy to Deno Deploy?"
  - "What are the build stages in Deno Deploy?"
  - "How do builds get triggered?"
---

# Quick Definition
The Deploy build system converts source code into deployable revisions through a multi-stage pipeline (Queue, Prepare, Install, Build, Deploy) triggered automatically from GitHub, manually from the CLI, or from the dashboard.

# Core Definition
In Deno Deploy, each version of application code is represented as a revision (or build). When deploying from GitHub, revisions generally map one-to-one to Git commits. Builds progress through stages: Queuing, Preparing (downloading source and restoring caches), Install (running dependency installation), Build (executing the build command and uploading the artifact), and Deploy (creating databases, running pre-deploy commands, warming up, and routing traffic). Build configuration can be set in the dashboard or in `deno.json`/`deno.jsonc` source code (source code takes precedence).

# Prerequisites
- deno-deploy -- Builds are the deployment mechanism for Deno Deploy applications

# Key Properties
1. **Three trigger methods** -- Automatically from GitHub push, manually from CLI (`deno deploy`), or manually from UI ("Deploy Default Branch")
2. **Five-stage pipeline** -- Queuing, Preparing, Install, Build, Deploy (with sub-stages: create database, pre-deploy command, warmup, routing)
3. **Configurable from source** -- `deno.json` deploy key supports framework, install, build, predeploy, and runtime configuration
4. **Build caching** -- Automatic caching for framework presets and DENO_DIR dependency cache
5. **Live-streamed logs** -- Build logs stream to the dashboard in real time and persist after completion
6. **Build environment** -- Linux (x64 or ARM64), 2 vCPUs, 3 GB RAM (up to 4 GB on Pro), 8 GB storage, with deno/node/npm/yarn/pnpm/git available
7. **All JS runs through Deno** -- `node`, `npm`, `npx`, `yarn`, `pnpm` are shims that translate invocations to Deno
8. **Timeouts** -- Default 5 minutes, up to 15 minutes on Pro plan

# Construction / Recognition
- Configuration via dashboard: framework preset, install command, build command, pre-deploy command, runtime config (dynamic/static/automatic)
- Configuration via `deno.json`:
  ```json
  {
    "deploy": {
      "framework": "nextjs",
      "install": "npm install",
      "build": "npm run build",
      "predeploy": "deno run --allow-net --allow-env migrate.ts",
      "runtime": { "type": "dynamic", "entrypoint": "./server.js" }
    }
  }
  ```
- Runtime types: Dynamic (server-side code), Static (pre-rendered files), Automatic (framework preset)

# Context & Application
Builds are the core deployment mechanism. Every code change flows through the build pipeline before reaching production. The pre-deploy command enables automated database migrations. Build environment variables are isolated from runtime contexts (Production/Development). GitHub events integration dispatches `repository_dispatch` events for build status changes, enabling CI/CD workflow triggers.

# Examples
From deploy/reference/builds.md:
- "When deploying from GitHub, revisions generally map one-to-one to git commits in your repository."
- Build environment variables: `CI=true`, `DENO_DEPLOY=true`, `DENO_DEPLOY_APPLICATION_SLUG`, `DENO_DEPLOY_BUILD_ID`
- GitHub events: `deno_deploy.build.enqueued`, `deno_deploy.build.routed`, `deno_deploy.build.failed`, `deno_deploy.build.cancelled`

# Relationships
## Builds Upon
- deno-deploy (the platform that hosts and runs builds)

## Enables
- deploy-timelines (each build creates a revision that is deployed to timelines)
- deploy-framework-support (framework presets optimize the build pipeline)

## Related
- environment-variables-and-contexts (Build context has separate env vars)
- deploy-databases (pre-deploy command can run migrations)

# Common Errors
1. Expecting dashboard config to override source code config -- when `deno.json` has deploy settings, dashboard configuration is ignored
2. Placing the pre-deploy command in the build step -- pre-deploy runs after build but before routing, with runtime database env vars

# Common Confusions
1. **Build vs. runtime environment** -- Build context env vars are separate from Production/Development runtime env vars
2. **node command in build** -- `node` is actually a Deno shim; all JavaScript execution uses Deno during builds

# Source Reference
- deploy/reference/builds.md: Full build pipeline documentation, stages, configuration, environment
- deploy/reference/apps.md: App creation, GitHub integration, build triggers

# Verification Notes
- High confidence: Build stages, configuration options, and environment details are explicitly documented
- GitHub events payload structure verified from apps.md TypeScript interface
