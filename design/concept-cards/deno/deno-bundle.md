---
concept: deno bundle
slug: deno-bundle
category: cli
subcategory: tooling commands
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/bundling.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "deno bundle command"
  - "Deno bundler"
prerequisites:
  - deno-cli
extends:
  - deno-cli
related:
  - deno-compile
  - jsx-support
contrasts_with:
  - deno-compile
answers_questions:
  - "How do I bundle a Deno project into a single JavaScript file?"
  - "Can Deno bundle for the browser?"
---

# Quick Definition

`deno bundle` outputs a single JavaScript file with all dependencies inlined, powered by ESBuild, supporting JSX/TSX, TypeScript, CSS, HTML entrypoints, minification, code splitting, and browser/Deno platform targeting.

# Core Definition

The `deno bundle` command "outputs a single JavaScript file with all dependencies." It is an experimental feature (Deno 2.4+) powered by ESBuild under the hood. It resolves and inlines all dependencies (JSR, npm, HTTPS, local), supports JSX/TSX and TypeScript, and can target either the Deno or browser platform.

Starting in Deno 2.5, `deno bundle` also supports HTML files as entrypoints, automatically finding script references, bundling their dependencies, and injecting CSS.

A runtime API (`Deno.bundle()`) is also available (experimental, requires `--unstable-bundle`) for programmatic bundling.

# Prerequisites

- **deno-cli** -- `deno bundle` is a subcommand of the Deno CLI.

# Key Properties

1. **ESBuild-powered** -- Uses ESBuild for fast bundling.
2. **Dependency inlining** -- Resolves and inlines JSR, npm, HTTPS, and local imports.
3. **Platform targeting** -- `--platform` flag supports `deno` (default) and `browser`.
4. **Minification** -- `--minify` flag for production builds.
5. **Source maps** -- `--sourcemap` supports linked, inline, and external formats.
6. **Code splitting** -- `--code-splitting` flag for multi-chunk output.
7. **HTML entrypoints** -- Deno 2.5+ can bundle from HTML files, processing script tags and CSS.
8. **Experimental** -- Requires Deno 2.4.0 or newer; subject to changes.

# Construction / Recognition

## To Use:
1. Bundle to stdout: `deno bundle main.ts > bundle.js`
2. Bundle with explicit output: `deno bundle -o bundle.js main.ts`
3. Bundle for browser with minification: `deno bundle --platform=browser --minify -o bundle.js main.ts`
4. Bundle from HTML: `deno bundle --outdir dist index.html`
5. Programmatic API:
```ts
const result = await Deno.bundle({
  entrypoints: ["./index.tsx"],
  outputDir: "dist",
  platform: "browser",
  minify: true,
});
```

## To Identify:
- Invocation: `deno bundle [flags] <entrypoint>`
- Produces `.js` output file(s) or modified HTML with hashed asset references.

# Context & Application

- **Deployment**: Produce a single optimized JS file for distribution.
- **Browser apps**: Bundle Deno-authored code for browser consumption with `--platform=browser`.
- **Static sites**: HTML entrypoint support enables bundling small static apps with CSS injection.

# Examples

**Example 1** (from source): Basic bundling.
```bash
$ deno bundle main.ts > bundle.js
```
(Section: "Basic example")

**Example 2** (from source): Bundling a React page for the browser.
```bash
$ deno bundle --platform=browser app.jsx -o bundle.js
```
(Section: "Bundle a React page for the web")

**Example 3** (from source): HTML entrypoint bundling.
```bash
deno bundle --outdir dist index.html
```
(Section: "HTML entrypoint support")

# Relationships

## Builds Upon
- **deno-cli** -- Subcommand of the CLI.

## Enables
- Single-file JavaScript distribution.
- Browser-targeted builds from Deno projects.

## Related
- **deno-compile** -- Compiles to standalone binary (different output format).
- **jsx-support** -- JSX/TSX is supported in bundled output.

## Contrasts With
- **deno-compile** -- `deno compile` embeds the runtime into a binary; `deno bundle` produces plain JavaScript that still needs a runtime.
- **Vite** -- For complex projects, Vite offers a wider ecosystem; `deno bundle` is better for small, quick builds.

# Common Errors

- **Error**: Using `deno bundle` on Deno versions before 2.4.0.
  **Correction**: `deno bundle` requires Deno 2.4.0 or newer.

- **Error**: Using `Deno.bundle()` API without the `--unstable-bundle` flag.
  **Correction**: The runtime API requires `--unstable-bundle` (added in Deno 2.5).

# Common Confusions

- **Confusion**: `deno bundle` produces an executable.
  **Clarification**: It produces JavaScript file(s), not a standalone binary. Use `deno compile` for executables.

# Source Reference

- runtime/reference/bundling.md: Full documentation of `deno bundle`, options, HTML entrypoints, runtime API, and React example.

# Verification Notes

- High confidence: Detailed documentation with examples directly in the source file.
- Experimental status explicitly noted in source.
- Options table reproduced from source.
