---
# === CORE IDENTIFICATION ===
concept: Deno Sandbox
slug: deno-sandbox

# === CLASSIFICATION ===
category: sandbox
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "sandbox/index.md"
chapter_number: null
pdf_page: null
section: "What is a Deno Sandbox?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Sandbox"
  - "microVM"
  - "@deno/sandbox"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - sandbox-security
  - sandbox-volumes
  - deploy-observability
contrasts_with:
  - deno-deploy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Deno Sandbox?"
  - "What distinguishes Deno Sandbox from Deno Deploy?"
  - "How does Deno Sandbox relate to Deno Deploy?"
---

# Quick Definition
Deno Sandbox provides instant, ephemeral Linux microVMs orchestrated by Deno Deploy, designed for running untrusted or AI-generated code with API-driven creation, sub-second boot times, and production-grade isolation.

# Core Definition
Deno Sandbox brings instant Linux microVMs to Deno Deploy. Each sandbox boots in under a second, is API-driven from the `@deno/sandbox` SDK (JavaScript/Python), and is torn down when no longer needed. Sandboxes provide full Linux environments with files, processes, package managers, and background services. They are designed for running untrusted code with hypervisor-level isolation and strict outbound network policies. Sandboxes share the same organization boundary as Deno Deploy apps, reusing members, tokens, and observability settings.

# Prerequisites
- deno-deploy -- Sandboxes are orchestrated by Deno Deploy and share its organization model

# Key Properties
1. **Sub-second boot** -- Boot times measured in milliseconds, no warm pool to manage
2. **Full Linux environment** -- Files, processes, package managers, background services available
3. **API-driven** -- Create, run commands, and tear down from code via `@deno/sandbox` SDK
4. **Ephemeral by default** -- Destroyed when script finishes (timeout: "session"), but can persist with explicit timeout durations
5. **Hypervisor-level isolation** -- Each sandbox is an individual microVM, not a container
6. **Network policies** -- `allowNet` restricts outbound traffic to approved hosts
7. **Secret substitution** -- Secrets never enter the sandbox env vars; substituted only on approved outbound requests
8. **Expose HTTP** -- Run dev servers and expose them via secure HTTPS URLs under `*.sandbox.deno.net`
9. **Deploy from sandbox** -- `sandbox.deno.deploy()` pushes compiled artifacts to Deno Deploy
10. **Multi-runtime SDK** -- Deno (latest), Node.js 24+, Python 3.10+

# Construction / Recognition
```typescript
import { Sandbox } from "@deno/sandbox";
// Create and auto-cleanup
await using sandbox = await Sandbox.create({
  region: "ams",        // ams or ord
  memoryMb: 1024,       // 768-4096 MB
  allowNet: ["api.openai.com"],
});
await sandbox.sh`ls -lh /`;
// Upload and run files
await sandbox.fs.upload("./local.ts", "./remote.ts");
await sandbox.spawn("deno", { args: ["run", "remote.ts"] });
```
Authentication: `DENO_DEPLOY_TOKEN` environment variable from organization tokens.

# Context & Application
Deno Sandbox specializes in workloads where code needs to be generated, evaluated, or safely executed on behalf of untrusted users. Ideal use cases include AI agents/copilots that run code as they reason, secure plugin systems, vibe-coding and collaborative IDE experiences, ephemeral CI runners, customer-supplied code paths, and instant dev server previews. Together with Deno Deploy, it forms a workflow where code is created and proved safe in a sandbox, then deployed globally.

# Examples
From sandbox/index.md:
- "Deno Sandbox brings instant Linux microVMs to Deno Deploy. Each sandbox boots in under a second."
- "Secrets never enter the sandbox environment. The real value is substituted only when the sandbox makes outbound requests to approved hosts."
- Limits: 768-4096 MB memory, 2 vCPU, up to 30-minute lifetime, 10 GB ephemeral disk, 5 concurrent sandboxes per org (default)

From sandbox/getting_started.md:
- SDK install: `deno add jsr:@deno/sandbox` or `npm install @deno/sandbox` or `pip install deno-sandbox`
- Timeout modes: `"session"` (destroy on script finish), duration like `"5m"` (keep alive, reconnect via `Sandbox.connect({ id })`)
- Deploy from sandbox: scaffold Next.js, build, then `sandbox.deno.deploy(app.slug, { path, production: true, build: { entrypoint, args } })`

# Relationships
## Builds Upon
- deno-deploy (sandboxes are orchestrated by Deploy infrastructure)

## Enables
- sandbox-security (network policies and secret substitution)
- sandbox-volumes (persistent storage for ephemeral VMs)

## Related
- deploy-observability (sandbox logs, traces, metrics visible in Deploy dashboard)

## Contrasts With
- deno-deploy (Deploy runs persistent serverless apps serving HTTP; Sandbox provides ephemeral microVMs for arbitrary code execution)

# Common Errors
1. Forgetting `--allow-net` and `--allow-env` flags when running the SDK locally -- the SDK needs network access to Deploy API and env vars for authentication
2. Not setting `DENO_DEPLOY_TOKEN` -- SDK authentication requires this environment variable

# Common Confusions
1. **Sandbox vs. Deploy** -- Deploy is for persistent web applications; Sandbox is for ephemeral compute and code execution. They share the same organization and observability.
2. **`await using` syntax** -- Requires Node.js 24+; use try/finally with `sandbox.close()` on earlier versions
3. **Regions** -- Currently only `ams` (Amsterdam) and `ord` (Chicago); sandbox and volume must be in the same region

# Source Reference
- sandbox/index.md: Platform overview, capabilities, limits, regions
- sandbox/getting_started.md: SDK installation, first sandbox, configuration, deploying from sandbox

# Verification Notes
- High confidence: Core concept explicitly defined with detailed capabilities, limits, and SDK examples
