---
# === CORE IDENTIFICATION ===
concept: Deploy Cron
slug: deploy-cron

# === CLASSIFICATION ===
category: infrastructure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/cron.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno.cron"
  - "scheduled tasks"
  - "cron jobs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - deploy-timelines
  - deploy-observability
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I schedule recurring tasks on Deno Deploy?"
  - "How does Deno.cron work?"
---

# Quick Definition
Deploy Cron enables scheduled tasks defined in code via the `Deno.cron()` API, with automatic discovery at deployment time, per-timeline execution, retry support, and OpenTelemetry trace integration.

# Core Definition
Cron jobs in Deno Deploy are scheduled tasks defined using the `Deno.cron()` API. Each cron job takes a human-readable name, a schedule (5-field cron expression or structured object, all times UTC), and a handler function. The platform discovers cron definitions at deployment time by evaluating top-level module code, then schedules them for execution. Cron jobs run independently on each timeline where they are registered, with the handler from that timeline's active revision. Each execution is billed as one inbound HTTP request.

# Prerequisites
- deno-deploy -- Cron jobs run on the Deno Deploy platform

# Key Properties
1. **Code-defined** -- Register via `Deno.cron("name", "schedule", handler)` at the module top level
2. **Top-level registration only** -- Must be registered before `Deno.serve()` starts; not picked up inside request handlers or conditionals
3. **UTC scheduling** -- All times are UTC to avoid daylight saving ambiguity
4. **No overlapping executions** -- If a cron job is still running when the next invocation is due, that invocation is skipped
5. **Configurable retries** -- `backoffSchedule` array of delays in ms; max 5 retries, max 1-hour delay per retry
6. **Per-timeline execution** -- Each timeline (production, git branch) runs its own set of cron jobs from its active revision
7. **Limits** -- Max 256 characters for name; 10 cron jobs per revision on free plan
8. **OpenTelemetry traces** -- Each execution produces traces viewable in the observability dashboard

# Construction / Recognition
```typescript
// Register at top level, before Deno.serve()
Deno.cron("cleanup-old-data", "0 * * * *", () => {
  console.log("Cleaning up old data...");
});

Deno.cron("sync-data", "*/15 * * * *", {
  backoffSchedule: [1000, 5000, 10000],
}, async () => {
  await syncExternalData();
});
```
Common pattern: define crons in a dedicated `crons.ts` and import at the top of `main.ts`.

# Context & Application
Deploy Cron is useful for periodic maintenance tasks (data cleanup), synchronization jobs, report generation, and any recurring background work. Rolling back a deployment re-registers the cron jobs from that revision. The dashboard Cron tab shows all registered jobs, their schedules, execution history, and allows filtering by status and timeline.

# Examples
From deploy/reference/cron.md:
- Common schedules: `* * * * *` (every minute), `0 * * * *` (hourly), `0 1 * * *` (daily at 1 AM UTC)
- Organizing cron declarations: `import "./crons.ts";` in main.ts
- Dashboard filters: `status:ok`, `status:error`, `timeline:production`
- Trace filters: `kind:cron`, `cron.name:<name>`, `cron.schedule:<schedule>`

# Relationships
## Builds Upon
- deno-deploy (cron jobs run on the Deploy platform)

## Related
- deploy-timelines (cron jobs execute per-timeline)
- deploy-observability (executions produce OpenTelemetry traces)

# Common Errors
1. Registering cron jobs inside request handlers or after `Deno.serve()` -- the platform will not discover them
2. Expecting concurrent execution of the same cron job -- overlapping invocations are skipped

# Common Confusions
1. **Retries vs. scheduled runs** -- Retries do not affect the cron schedule; the next scheduled run fires on time even if retries are pending
2. **Per-timeline isolation** -- The same cron name on different timelines runs independently from each timeline's active revision

# Source Reference
- deploy/reference/cron.md: Full cron documentation including API, lifecycle, retries, dashboard, observability

# Verification Notes
- High confidence: API and behavior explicitly documented with code examples and schedule reference table
