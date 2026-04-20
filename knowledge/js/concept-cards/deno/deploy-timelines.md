---
# === CORE IDENTIFICATION ===
concept: Deploy Timelines
slug: deploy-timelines

# === CLASSIFICATION ===
category: deploy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/timelines.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "deployment history"
  - "rollback"
  - "timeline locking"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
  - deploy-builds
extends: []
related:
  - environment-variables-and-contexts
  - deploy-cron
  - deploy-databases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I roll back a deployment on Deno Deploy?"
  - "What are timelines in Deno Deploy?"
---

# Quick Definition
A timeline is the deployment history of one branch of an application, with an active revision serving traffic, instant rollback to any previous revision, and optional timeline locking to prevent automatic promotion of new builds.

# Core Definition
A timeline represents the history of one branch of a Deno Deploy application. Each timeline contains a set of revisions, with one "active" revision currently serving traffic on all URLs assigned to that timeline. Timelines are associated with contexts (Production or Development), which determine environment variable availability. By default, apps have a Production timeline (default git branch, served at `<app>.<org>.deno.net` and custom domains), Git Branch timelines (per-branch, served at `<app>--<branch>.<org>.deno.net`), and per-revision Preview timelines (`<app>-<revision-id>.<org>.deno.net`).

# Prerequisites
- deno-deploy -- Timelines are a Deno Deploy concept
- deploy-builds -- Each build creates a revision on one or more timelines

# Key Properties
1. **Active revision** -- One revision per timeline serves traffic; usually the most recent build
2. **Instant rollback** -- Lock any previous revision as active to revert without building new code
3. **Timeline locking** -- Lock to a specific revision to prevent new builds from auto-promoting (useful during feature freezes)
4. **Unlock to resume** -- Unlocking reverts to default behavior where latest build becomes active
5. **Three timeline types** -- Production (`<app>.<org>.deno.net`), Git Branch (`<app>--<branch>.<org>.deno.net`), Preview (`<app>-<revision-id>.<org>.deno.net`)
6. **Context association** -- Production timeline uses Production context; all others use Development context
7. **Preview timelines hidden** -- Not visible in timeline pages; accessible via revision build page

# Construction / Recognition
- View timelines from the app's timelines page
- Lock a revision: click on it in the timeline page to make it active (locks the timeline)
- Unlock: revert to default behavior where latest revision becomes active
- Rolling back re-registers cron jobs and database connections from the rollback target revision

# Context & Application
Timelines enable safe deployment workflows. Instant rollback provides a safety net for failed deployments -- reverting to a known-good revision takes effect immediately without waiting for a new build. Timeline locking is valuable for high-stakes periods (product launches, events) where teams want to freeze deployments while still allowing code pushes to Git. Each git branch getting its own timeline enables isolated testing with dedicated URLs and database environments.

# Examples
From deploy/reference/timelines.md:
- Production URL pattern: `https://<app-name>.<org-name>.deno.net`
- Branch URL pattern: `https://<app-name>--<branch-name>.<org-name>.deno.net`
- Preview URL pattern: `https://<app-name>-<revision-id>.<org-name>.deno.net`
- "Timeline locking is useful if you are in a feature freeze situation, for example during a big event, and want to de-risk by not allowing new builds to be deployed."

# Relationships
## Builds Upon
- deno-deploy (timelines are a platform concept)
- deploy-builds (builds produce revisions placed on timelines)

## Related
- environment-variables-and-contexts (timelines map to contexts)
- deploy-cron (cron jobs execute per-timeline)
- deploy-databases (each timeline gets its own isolated database)

# Common Errors
1. Expecting locked timelines to block builds -- builds still run, they just do not become the active revision on locked timelines
2. Confusing preview timelines with branch timelines -- preview timelines are per-revision and not visible in the UI timeline pages

# Common Confusions
1. **Rollback vs. revert** -- Rollback in Deno Deploy means locking to an older revision (no new code needed); it is not a git revert

# Source Reference
- deploy/reference/timelines.md: Complete timelines documentation

# Verification Notes
- High confidence: Timeline types, rollback mechanism, and locking behavior explicitly documented
