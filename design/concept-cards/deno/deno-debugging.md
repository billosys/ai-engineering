---
concept: Debugging
slug: deno-debugging
category: development
subcategory: debugging
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/debugging.md"
chapter_number: null
pdf_page: null
section: "Debugging"
extraction_confidence: high
aliases:
  - "--inspect"
  - "--inspect-brk"
  - "--inspect-wait"
  - "Deno debugging"
  - "Deno DevTools"
prerequisites:
  - deno-configuration
extends: []
related:
  - deno-opentelemetry-support
  - deno-test-runner
contrasts_with: []
answers_questions:
  - "How do I debug Deno code?"
  - "How do I use Chrome DevTools with Deno?"
  - "How do I debug Deno in VS Code?"
---

# Quick Definition

Deno supports the V8 Inspector Protocol for debugging via Chrome DevTools, VS Code, and JetBrains IDEs, activated with `--inspect`, `--inspect-wait`, or `--inspect-brk` flags, plus built-in CPU profiling, op tracing, and TLS session debugging.

# Core Definition

Deno implements the V8 Inspector Protocol used by Chrome, Edge, and Node.js, enabling debugging with any compatible client. Three flags control debugging behavior:

- **`--inspect`** — Starts the inspector server; code begins executing immediately. Connect via `chrome://inspect` in a Chromium browser.
- **`--inspect-wait`** — Waits for a debugger to connect before executing code.
- **`--inspect-brk`** — Waits for a debugger to connect, then pauses at the first line. This is the most commonly used flag and the default for JetBrains and VS Code IDEs.

Additional debugging tools:

- **`--log-level=debug`** — Shows module resolution, network requests, and permission checks.
- **`--strace-ops`** — Prints all Deno ops (RPC between JavaScript and Rust) with timings, useful for performance profiling and debugging hanging programs.
- **CPU profiling** — `--cpu-prof` captures a V8 CPU profile (`.cpuprofile`), loadable in Chrome DevTools. Additional flags: `--cpu-prof-dir`, `--cpu-prof-name`, `--cpu-prof-interval`, `--cpu-prof-md` (Markdown report), `--cpu-prof-flamegraph` (interactive SVG).
- **TLS debugging** — `SSLKEYLOGFILE=./keys.log` logs TLS session keys for Wireshark decryption.

# Prerequisites

- `deno-configuration` — debugging may use permissions configured in `deno.json`

# Key Properties

1. **V8 Inspector Protocol**: Compatible with Chrome DevTools, VS Code, and JetBrains IDEs.
2. **Source maps**: DevTools displays both compiled JavaScript and original TypeScript source maps, allowing stepping through TypeScript directly.
3. **`--inspect-brk` is most common**: Pauses at the first line, giving time to set breakpoints before execution proceeds.
4. **CPU profiling output formats**: `.cpuprofile` (loadable in Chrome DevTools), Markdown summary tables, and interactive SVG flamegraphs.
5. **Op tracing**: `--strace-ops` shows `Dispatch`/`Complete` events for every Deno op with timings.
6. **VS Code integration**: The official `vscode_deno` extension provides built-in debugging support.
7. **JetBrains support**: The Deno plugin enables right-click debugging.

# Construction / Recognition

Basic debugging:
```sh
deno run --inspect-brk your_script.ts
```
Then open `chrome://inspect` in Chrome and click "Inspect" next to the target.

CPU profiling:
```sh
deno run --cpu-prof your_script.ts
deno run --cpu-prof --cpu-prof-md server.js          # With Markdown report
deno run --cpu-prof --cpu-prof-flamegraph script.ts   # With SVG flamegraph
```

Op tracing:
```sh
deno run --strace-ops your_script.ts
```

# Context & Application

Debugging in Deno works similarly to Node.js debugging, using the same V8 Inspector Protocol. The `--inspect-brk` flag is essential for debugging short-lived scripts or test files. For production applications, OpenTelemetry integration provides ongoing observability that complements development-time debugging.

# Examples

**Chrome DevTools workflow** (from `runtime/fundamentals/debugging.md`):
```sh
deno run --inspect-brk -RN jsr:@std/http/file-server
# Debugger listening on ws://127.0.0.1:9229/ws/...
```

1. Open `chrome://inspect` in Chrome
2. Click "Inspect" next to the Deno target
3. Navigate to "Sources" pane, expand the file tree
4. Set breakpoints in the source-mapped TypeScript files
5. Resume execution to hit breakpoints

**Markdown CPU profile report** includes summary table, top 10 expensive functions, hot functions by self time, call tree, and per-function details.

**Interactive flamegraph** (from `runtime/fundamentals/debugging.md`):
- Click frames to zoom in
- Ctrl+F for regex search with highlighting
- Invert checkbox for icicle graph view

# Relationships

- **Related**: `deno-opentelemetry-support` — production observability complements development debugging
- **Related**: `deno-test-runner` — tests can be debugged with the same inspect flags

# Common Errors

1. **Using `--inspect` with short scripts**: The program may finish before the debugger connects. Use `--inspect-wait` or `--inspect-brk` instead.
2. **TypeScript line numbers in CPU profiles**: V8's profiler reports line numbers from transpiled JavaScript, not original TypeScript source.

# Common Confusions

- **`--inspect` vs `--inspect-brk` vs `--inspect-wait`**: `--inspect` starts immediately (may miss breakpoints), `--inspect-wait` waits for connection then runs, `--inspect-brk` waits and pauses at first line.
- **Source map duplicates**: In DevTools, files appear twice — the regular entry is compiled JavaScript, the italic entry is the source map for stepping through TypeScript.

# Source Reference

Source: "Deno Documentation", file `runtime/fundamentals/debugging.md`, all sections.

# Verification Notes

All flags, workflows, and profiling features are explicitly documented in the source file. Extraction confidence is high.
