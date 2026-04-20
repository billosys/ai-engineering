---
# === CORE IDENTIFICATION ===
concept: Deploy Observability
slug: deploy-observability

# === CLASSIFICATION ===
category: infrastructure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/observability.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "logs"
  - "traces"
  - "metrics"
  - "monitoring"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - deploy-cron
  - deploy-timelines
  - deploy-tunnel
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I monitor my Deno Deploy application?"
  - "What observability features does Deno Deploy provide?"
---

# Quick Definition
Deno Deploy provides three observability pillars -- logs (via `console` API), traces (automatic and custom OpenTelemetry spans), and metrics (automatic time-series data) -- all filterable by revision, context, trace ID, and time range.

# Core Definition
Deno Deploy's observability features leverage OpenTelemetry and Deno's built-in OTel integration. Logs are captured from the standard `console` API and correlated with traces when emitted within an active span. Traces are captured automatically for incoming HTTP requests, outbound fetch calls, and supported framework operations (Next.js, Fresh, Astro), plus manually via the OpenTelemetry API. Metrics are automatically captured for incoming requests and outbound calls, displayed as time-series graphs. All three can be filtered by revision, context (Production/Development), trace ID, HTTP method/path/status, and custom time ranges using Grafana-compatible syntax.

# Prerequisites
- deno-deploy -- Observability is a built-in platform feature

# Key Properties
1. **Three pillars** -- Logs (unstructured debug output), Traces (structured request handling with span timing), Metrics (time-series performance data)
2. **Automatic tracing** -- Incoming HTTP requests, outbound fetch calls, and framework operations traced without configuration
3. **Framework instrumentation** -- Next.js, Fresh, Astro include built-in trace spans
4. **Custom instrumentation** -- Application code can create spans via the OpenTelemetry API
5. **Log-trace correlation** -- Logs emitted within a trace have a "View trace" button; traces have a "View logs" button
6. **Waterfall visualization** -- Trace overlay shows all spans with timing, attributes, and nested parent-child relationships
7. **Grafana-style time ranges** -- `now-1h`, `now/d`, `now-1d/d` syntax for custom ranges
8. **Cannot be disabled** -- Automatic capture for HTTP requests and fetch calls is always on

# Construction / Recognition
- Logs page: filter with `context:production`, `revision:<id>`, full-text search
- Traces page: filter with `context:production`, HTTP method/path/status
- Metrics page: time-series graphs with attribute filters
- Cron-specific trace filters: `kind:cron`, `cron.name:<name>`, `cron.schedule:<schedule>`
- Local development traces: filter with `context:local` when using `--tunnel`

# Context & Application
Observability is essential for debugging production issues, understanding application performance, and monitoring deployment health. The automatic tracing provides immediate visibility without code changes. Log-trace correlation enables efficient debugging by connecting error messages to specific request traces. Metrics enable capacity planning and alerting.

# Examples
From deploy/reference/observability.md:
- "Traces in Deno Deploy are captured in three ways: automatically for built-in operations, automatically for supported frameworks, manually through custom instrumentation."
- Time range examples: `now-1h` (1 hour ago), `now/h` (start of current hour), `now/d+3h` (3 hours from start of today)
- "Metrics in Deno Deploy are automatically captured for various operations such as incoming HTTP requests and outbound fetch calls."

# Relationships
## Builds Upon
- deno-deploy (observability is a platform feature)

## Related
- deploy-cron (cron executions produce OpenTelemetry traces)
- deploy-timelines (filter by context/revision)
- deploy-tunnel (local dev traces pushed to dashboard via `--tunnel`)

# Common Errors
1. Expecting to disable automatic tracing -- it cannot be turned off for built-in operations

# Common Confusions
1. **Logs vs. traces** -- Logs are unstructured text from `console.*`; traces are structured spans with timing and attributes representing request lifecycle

# Source Reference
- deploy/reference/observability.md: Complete observability documentation
- deploy/getting_started.md: Log and trace UI walkthrough

# Verification Notes
- High confidence: Three observability pillars explicitly defined with filtering syntax and visualization details
