---
# === CORE IDENTIFICATION ===
concept: Deploy Databases
slug: deploy-databases

# === CLASSIFICATION ===
category: infrastructure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/reference/databases.md"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "database integrations"
  - "Deno KV on Deploy"
  - "PostgreSQL on Deploy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-deploy
extends: []
related:
  - deploy-timelines
  - environment-variables-and-contexts
  - deploy-builds
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I connect a database to a Deno Deploy application?"
  - "What databases does Deno Deploy support?"
---

# Quick Definition
Deno Deploy's database feature automatically creates isolated databases per deployment environment (production, git branches, previews) for PostgreSQL and Deno KV, with auto-injected connection credentials and a built-in database explorer.

# Core Definition
Deno Deploy supports PostgreSQL and Deno KV database engines. Database instances can be linked (existing external database) or provisioned (managed by Deno Deploy via Prisma Postgres or Deno KV). After assignment to an app, Deno Deploy automatically creates isolated (logical) databases within the instance for each deployment timeline -- production uses `{app-id}-production`, git branches use `{app-id}--{branch-name}`, and previews use `{app-id}-preview`. Connection credentials (`DATABASE_URL`, `PGHOST`, etc.) are automatically injected as environment variables. For Deno KV, `Deno.openKv()` connects automatically with no configuration.

# Prerequisites
- deno-deploy -- Database feature is part of the Deno Deploy platform

# Key Properties
1. **Two engines** -- PostgreSQL (external or managed Prisma Postgres) and Deno KV (globally distributed key-value store)
2. **Per-environment isolation** -- Automatic isolated databases for production, git branches, and preview timelines
3. **Auto-injected credentials** -- `DATABASE_URL`, `PGHOST`, `PGPORT`, `PGDATABASE`, `PGUSER`, `PGPASSWORD` for PostgreSQL
4. **Zero-config Deno KV** -- `Deno.openKv()` connects to the correct instance automatically
5. **Pre-deploy migrations** -- Configure a pre-deploy command (e.g., `deno task migrate`) that runs before each deployment
6. **Database explorer** -- Built-in PostgreSQL database browser in the dashboard
7. **TLS/SSL support** -- Auto-detection for AWS RDS certificates; manual upload for other providers
8. **Local development** -- Use local database or connect to hosted isolated dev instance via `--tunnel`

# Construction / Recognition
- Link external PostgreSQL: provide hostname, port, username, password, optional CA certificate
- Provision managed: choose Deno KV or Prisma Postgres, select region
- Assign to app: one database instance per app (can serve multiple apps)
- Connect in code:
  ```typescript
  // Deno KV - zero config
  const kv = await Deno.openKv();
  // PostgreSQL - auto-detected env vars
  import { Pool } from "npm:pg";
  const pool = new Pool(); // reads DATABASE_URL automatically
  ```

# Context & Application
Database integration simplifies state management across deployment environments. The per-environment isolation ensures that development branches cannot corrupt production data. The pre-deploy command enables automated migrations using tools like node-pg-migrate, Prisma Migrate, Drizzle, or Kysely. The `--tunnel` flag provides access to hosted dev databases during local development.

# Examples
From deploy/reference/databases.md:
- Database naming: `{app-id}-production`, `{app-id}--{branch-name}`, `{app-id}-preview`
- Pre-deploy migration: set "Pre-Deploy Command" to `deno task migrate`
- "Because Deno Deploy creates isolated databases for each environment... ensure that the database user you provide has sufficient privileges to create new databases on the server."
- Prisma Postgres instances can be "claimed" into your own Prisma account for higher plan limits

# Relationships
## Builds Upon
- deno-deploy (database feature is a platform capability)

## Related
- deploy-timelines (each timeline gets its own isolated database)
- environment-variables-and-contexts (database credentials injected as env vars)
- deploy-builds (pre-deploy command runs migrations during build pipeline)

# Common Errors
1. Insufficient database user privileges -- the user must be able to create new databases for per-environment isolation
2. Only one database instance per app -- cannot link both Deno KV and PostgreSQL to the same app

# Common Confusions
1. **Instance vs. database** -- A database instance contains multiple isolated databases (one per timeline); multiple apps can share one instance
2. **Preview database sharing** -- Currently only one preview database per app, shared across all preview deployments

# Source Reference
- deploy/reference/databases.md: Complete database documentation including linking, provisioning, connection, migrations, explorer

# Verification Notes
- High confidence: Comprehensive source documentation with explicit API examples and configuration details
