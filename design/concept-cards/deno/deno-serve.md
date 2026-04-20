---
concept: deno serve
slug: deno-serve
category: cli
subcategory: execution commands
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/cli/index.md"
chapter_number: null
pdf_page: null
section: "Execution"
extraction_confidence: medium
aliases:
  - "deno serve command"
prerequisites:
  - deno-cli
  - web-platform-apis
extends:
  - deno-cli
related:
  - deno-run
  - deno-in-docker
contrasts_with:
  - deno-run
answers_questions:
  - "What distinguishes `deno run` from `deno serve`?"
  - "How do I run an HTTP server in Deno?"
---

# Quick Definition

`deno serve` runs a web server from a module that exports a `fetch` handler, with built-in support for automatic parallel scaling across CPU cores.

# Core Definition

The `deno serve` subcommand is a specialized execution command for running HTTP servers in Deno. Unlike `deno run`, which executes arbitrary scripts, `deno serve` expects the entry module to export a `fetch` function (following the Web standard Request/Response pattern). It is listed in the CLI reference as the command to "run a web server."

`deno serve` is designed for production HTTP workloads and can automatically scale across multiple CPU cores, unlike manually calling `Deno.serve()` via `deno run`, which runs single-threaded by default.

# Prerequisites

- **deno-cli** -- `deno serve` is a subcommand of the Deno CLI.
- **web-platform-apis** -- The `fetch` handler uses standard Web Platform Request and Response objects.

# Key Properties

1. **Convention-based entry** -- Expects the module to export a `fetch(request: Request): Response` handler function.
2. **Automatic scaling** -- Can parallelize HTTP handling across multiple CPU cores.
3. **Web-standard interface** -- Uses the standard Request/Response API pattern from the Web Platform.
4. **Separate from `deno run`** -- Purpose-built for HTTP server workloads.

# Construction / Recognition

## To Use:
1. Create a module exporting a `fetch` handler:
```ts
export default {
  fetch(request: Request): Response {
    return new Response("Hello, world!");
  }
};
```
2. Run: `deno serve main.ts`

## To Identify:
- Invocation: `deno serve [flags] <module>`
- Module must export a `fetch` function.

# Context & Application

- **Web servers**: The recommended way to run HTTP servers in production Deno deployments.
- **Deno Deploy**: Aligns with the Deno Deploy model where modules export a `fetch` handler.
- **Docker containers**: Commonly used as the `CMD` in Dockerfiles for Deno web applications.

# Examples

**Example 1** (synthesized from CLI reference): Running a web server.
```shell
deno serve main.ts
```

# Relationships

## Builds Upon
- **deno-cli** -- Subcommand of the CLI.
- **web-platform-apis** -- Uses standard Request/Response.

## Enables
- Production HTTP server deployments with automatic scaling.

## Related
- **deno-run** -- General-purpose execution; can also run servers via `Deno.serve()`.
- **deno-in-docker** -- `deno serve` is commonly the CMD in Docker images.

## Contrasts With
- **deno run** -- `deno run` is general-purpose and single-threaded by default; `deno serve` is specialized for HTTP with automatic multi-core scaling.

# Common Errors

- **Error**: Using `deno serve` with a script that does not export a `fetch` handler.
  **Correction**: The entry module must export a default object with a `fetch` method or a `fetch` function.

# Common Confusions

- **Confusion**: `deno serve` and `deno run` with `Deno.serve()` are identical.
  **Clarification**: `deno serve` adds automatic parallel scaling and expects a convention-based module export; `deno run` with `Deno.serve()` is manual and single-threaded by default.

# Source Reference

- runtime/reference/cli/index.md: "deno serve - run a web server" listing.

# Verification Notes

- Medium confidence: The CLI reference confirms `deno serve` exists and its purpose, but detailed documentation on scaling behavior is referenced indirectly. The convention-based `fetch` handler pattern is well-established in Deno ecosystem documentation.
