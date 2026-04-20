# Deno Runtime Basics

The foundational Deno reference: security model, permissions, namespace APIs, Web Platform APIs, configuration, module resolution, type checking, Node.js compatibility, compilation, and the standard library. This is the "Deno cheat sheet" chapter that five other guides reference. Grounded in Deno documentation concept cards, supplemented by *Exploring JavaScript* (Rauschmayer) for ESM semantics.

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (plain JS with JSDoc where needed).

---

## ID-01: Deno Is Secure by Default — No Access Without Explicit Permission

**Strength**: MUST

**Summary**: Deno denies all file, network, environment, and subprocess access unless you explicitly grant it with permission flags.

```sh
# Bad — full access, no sandbox
deno run -A server.js

# Good — minimal permissions for what the program needs
deno run --allow-net=api.example.com --allow-read=./data --allow-env=PORT server.js

# Good — deny specific resources within a broad grant
deno run --allow-net --deny-net=evil.com server.js
```

**Rationale**: Deno's security model is the inverse of Node.js — programs start with zero access and must request what they need. This prevents dependency supply-chain attacks from exfiltrating data or writing to the filesystem. `--allow-all` / `-A` disables the sandbox entirely — use it only for development, never in production (Deno security model docs).

---

## ID-02: Use Granular Permissions — Scope to Specific Paths, Hosts, and Variables

**Strength**: SHOULD

**Summary**: Permission flags accept comma-separated lists of specific paths, hostnames, or variable names. Prefer narrow grants over broad ones.

```sh
# Good — granular permissions
deno run \
  --allow-read=./config,./data \
  --allow-write=./output \
  --allow-net=api.example.com:443,db.internal:5432 \
  --allow-env=PORT,DATABASE_URL \
  server.js

# Bad — overly broad
deno run --allow-read --allow-write --allow-net --allow-env server.js
```

**Permission flags reference**:

| Flag | Short | Scoping | Requires |
|------|-------|---------|----------|
| `--allow-read` | `-R` | Comma-separated paths | File system reads |
| `--allow-write` | `-W` | Comma-separated paths | File system writes |
| `--allow-net` | `-N` | Comma-separated host:port | Network access |
| `--allow-env` | `-E` | Comma-separated names (wildcards: `"AWS_*"`) | Env variables |
| `--allow-run` | — | Comma-separated executables | Subprocesses |
| `--allow-sys` | `-S` | — | System info APIs |
| `--allow-ffi` | — | — | Native code (FFI) |
| `--allow-all` | `-A` | — | Everything (dev only) |

**Deny flags always override allow**: `--allow-net --deny-net=evil.com` permits all network except `evil.com`.

**Special caution**: `--allow-run` is the most dangerous permission — spawned subprocesses escape the Deno sandbox entirely and run with full system access. `--allow-ffi` is similarly dangerous (native code runs at full process privilege). Both should be scoped to specific executables/libraries when possible.

**Rationale**: Broad permissions (`--allow-read` with no path) grant access to the entire filesystem. Narrow permissions limit blast radius — a compromised dependency can only access what the program was granted (Deno permissions docs).

---

## ID-03: Request Permissions at Runtime

**Strength**: CONSIDER

**Summary**: Use `Deno.permissions.request()` to prompt for permissions interactively rather than requiring them upfront.

```js
// Good — request permission at the point of need
const status = await Deno.permissions.request({ name: "read", path: "./data" });
if (status.state === "granted") {
  const data = await Deno.readTextFile("./data/config.json");
}

// Query without prompting
const netStatus = await Deno.permissions.query({ name: "net", host: "api.example.com" });
if (netStatus.state === "granted") {
  await fetch("https://api.example.com/health");
}
```

**Rationale**: Runtime permission requests enable progressive permission escalation — the program starts with minimal access and asks for more only when needed. In TTY mode, Deno prompts the user interactively. In non-interactive environments (CI), use `--no-prompt` and pre-grant all needed permissions via flags (Deno permissions docs).

---

## ID-04: `--allow-all` Only for Development — Never in Production

**Strength**: MUST

**Summary**: `-A` disables the entire security sandbox. It is equivalent to Node.js's default behavior.

```sh
# Acceptable — development/prototyping
deno run -A main.js

# Required — production
deno run --allow-net=:8080 --allow-read=./static --allow-env=PORT main.js
```

**Rationale**: `-A` grants file, network, env, subprocess, and FFI access to the program and all of its dependencies. A malicious or compromised npm package with `-A` has full system access. Production deployments should use the minimal permission set — define it in a `deno task` or a named permission set in `deno.json` (Deno security model docs).

---

## ID-05: File I/O — `Deno.readTextFile`, `Deno.writeTextFile`, `Deno.open`

**Strength**: SHOULD

**Summary**: Use the `Deno` namespace for file operations. All are async by default and require `--allow-read` / `--allow-write`.

```js
// Good — async file operations
const text = await Deno.readTextFile("./config.json");
const config = JSON.parse(text);

await Deno.writeTextFile("./output.json", JSON.stringify(result, null, 2));

// Binary files
const bytes = await Deno.readFile("./image.png");

// Low-level: open, read, write, close
const file = await Deno.open("./data.csv", { read: true });
// ... use file.readable (a ReadableStream) ...
file.close();

// Directory operations
await Deno.mkdir("./output", { recursive: true });
for await (const entry of Deno.readDir("./data")) {
  console.log(entry.name, entry.isFile);
}

const info = await Deno.stat("./data.csv");
console.log(info.size, info.mtime);
```

**Rationale**: `Deno.readTextFile()` and `Deno.writeTextFile()` are the high-level convenience APIs. For streaming, use `Deno.open()` which returns a file with `.readable` and `.writable` properties (Web Streams). Sync variants exist (`Deno.readTextFileSync`) but should be avoided — see `07-async-concurrency.md` ID-03 (Deno namespace API docs).

---

## ID-06: `Deno.serve()` for HTTP Servers

**Strength**: SHOULD

**Summary**: `Deno.serve()` is the modern HTTP server API. It uses standard Web API `Request`/`Response` types.

```js
// Good — minimal server (handler only, defaults to port 8000)
Deno.serve((_req) => new Response("Hello, World!"));

// Good — with options (options first, handler second)
Deno.serve({ port: 8080, hostname: "0.0.0.0" }, (req) => {
  const url = new URL(req.url);
  if (url.pathname === "/api/health") {
    return new Response(JSON.stringify({ status: "ok" }), {
      headers: { "content-type": "application/json" },
    });
  }
  return new Response("Not Found", { status: 404 });
});

// Good — streaming response
Deno.serve((_req) => {
  const body = new ReadableStream({
    start(controller) {
      controller.enqueue(new TextEncoder().encode("chunk 1\n"));
      controller.enqueue(new TextEncoder().encode("chunk 2\n"));
      controller.close();
    },
  });
  return new Response(body, {
    headers: { "content-type": "text/plain" },
  });
});
```

**Signatures**: `Deno.serve(handler)` or `Deno.serve(options, handler)`. Options first, handler second.

**Key features**: HTTP/1.1 and HTTP/2 automatic, auto-compression (gzip/brotli), HTTPS via `cert`/`key` options, streaming bodies, WebSocket upgrade via `Deno.upgradeWebSocket(req)`. Requires `--allow-net`.

**Rationale**: `Deno.serve()` replaces the older `Deno.listen()` + manual request handling pattern. It uses the same `Request`/`Response` types as `fetch()`, making server and client code symmetrical (Deno HTTP server docs).

---

## ID-07: `Deno.Command` for Subprocesses

**Strength**: SHOULD

**Summary**: Use `Deno.Command` to spawn subprocesses. Requires `--allow-run`.

```js
// Good — run a command and capture output
const cmd = new Deno.Command("git", { args: ["log", "--oneline", "-5"] });
const { code, stdout, stderr } = await cmd.output();
console.log(new TextDecoder().decode(stdout));

// Good — streaming output
const child = new Deno.Command("find", { args: [".", "-name", "*.js"], stdout: "piped" }).spawn();
for await (const chunk of child.stdout) {
  console.log(new TextDecoder().decode(chunk));
}

// Good — piped stdin
const proc = new Deno.Command("wc", { args: ["-l"], stdin: "piped", stdout: "piped" }).spawn();
const writer = proc.stdin.getWriter();
await writer.write(new TextEncoder().encode("line 1\nline 2\nline 3\n"));
await writer.close();
const { stdout: out } = await proc.output();
console.log(new TextDecoder().decode(out).trim()); // "3"
```

**Rationale**: `Deno.Command` replaces the deprecated `Deno.run()`. It uses Web Streams for I/O (`.stdout` is a `ReadableStream`). Note: `--allow-run` subprocesses escape the sandbox — the spawned process has full system access regardless of Deno's permissions (Deno namespace API docs).

---

## ID-08: `Deno.env` for Environment Variables

**Strength**: SHOULD

**Summary**: Use `Deno.env` to read and write environment variables. Requires `--allow-env`.

```js
// Good — read with fallback
const port = Number(Deno.env.get("PORT") ?? "8080");
const dbUrl = Deno.env.get("DATABASE_URL");
if (!dbUrl) throw new Error("DATABASE_URL is required");

// Good — set for child processes
Deno.env.set("NODE_ENV", "production");

// Good — get all env vars as an object
const allEnv = Deno.env.toObject();
```

**Rationale**: `Deno.env.get()` returns `string | undefined`. There is no `process.env` global in Deno-native code — `process` is only available in npm package scope. Scope permissions narrowly: `--allow-env=PORT,DATABASE_URL` (Deno namespace API docs).

**See also**: `10-project-structure.md` ID-17

---

## ID-09: `Deno.cwd()`, `Deno.args`, and Runtime Introspection

**Strength**: CONSIDER

**Summary**: The `Deno` namespace provides process-level introspection without a `process` global.

```js
// Current working directory
const cwd = Deno.cwd();

// Command-line arguments (after the script name)
const args = Deno.args; // e.g., ["--verbose", "input.txt"]

// Deno version and build info
console.log(Deno.version.deno);    // "2.1.0"
console.log(Deno.version.v8);     // "13.0.245.12"
console.log(Deno.build.os);       // "darwin" | "linux" | "windows"
console.log(Deno.build.arch);     // "x86_64" | "aarch64"

// Exit (prefer letting the event loop drain naturally)
Deno.exit(0);
```

**Rationale**: `Deno.args` replaces Node's `process.argv.slice(2)`. `Deno.build.os` replaces `process.platform`. Avoid `Deno.exit()` when possible — it prevents cleanup in `finally` blocks and `unload` event handlers (Deno namespace API docs).

---

## ID-10: `fetch()` Is Built-In — No Import Needed

**Strength**: MUST

**Summary**: `fetch()` is a global in Deno, just like in browsers. No import or polyfill required.

```js
// Good — fetch is always available
const response = await fetch("https://api.github.com/users/denoland");
const data = await response.json();

// Good — with signal for cancellation
const controller = new AbortController();
const response = await fetch("https://api.example.com/data", {
  signal: AbortSignal.timeout(5000),
});

// Good — POST with JSON body
const response = await fetch("https://api.example.com/users", {
  method: "POST",
  headers: { "content-type": "application/json" },
  body: JSON.stringify({ name: "Alice" }),
});
```

**Deno-specific `fetch()` behaviors**:
- Supports `file:` URLs for local file reading
- No cookie jar, no CORS enforcement, no same-origin policy (server-side, intentionally)
- Supports duplex streaming

**Rationale**: Deno implements the WHATWG Fetch standard. Using `fetch()` produces code that is portable between Deno and browsers. Requires `--allow-net` for network requests (Deno Web Platform API docs).

**See also**: `07-async-concurrency.md` ID-24

---

## ID-11: Web Platform APIs Available in Deno

**Strength**: SHOULD

**Summary**: Deno implements a wide range of WHATWG/W3C standards, enabling isomorphic code that works in both Deno and browsers.

**Available globally (no import needed)**:

| Category | APIs |
|----------|------|
| HTTP | `fetch`, `Request`, `Response`, `Headers`, `FormData` |
| URLs | `URL`, `URLSearchParams` |
| Encoding | `TextEncoder`, `TextDecoder`, `atob`, `btoa` |
| Crypto | `crypto.subtle`, `crypto.randomUUID()`, `crypto.getRandomValues()` |
| Streams | `ReadableStream`, `WritableStream`, `TransformStream`, `CompressionStream`, `DecompressionStream` |
| Timers | `setTimeout`, `setInterval`, `queueMicrotask`, `performance.now()` |
| Abort | `AbortController`, `AbortSignal` |
| Events | `EventTarget`, `Event`, `CustomEvent` |
| Structured data | `structuredClone`, `JSON` |
| Workers | `Worker` (module type only) |
| WebSocket | `WebSocket` |
| Console | `console.log/warn/error/table/time/timeEnd` |
| Storage | `localStorage`*, `sessionStorage`* |
| Cache | `CacheStorage`, `Cache` (partial) |
| Channel | `BroadcastChannel` |

*`localStorage` in Deno differs from browsers: it is persisted to disk (not in-memory), scoped by the main module path (not by origin), and has a 10 MB limit. `sessionStorage` is per-execution (cleared when the process exits). Neither requires `--allow-read`/`--allow-write`.

**Rationale**: Using Web Platform APIs makes code portable between Deno and browsers. Deno deviates from browser behavior only where server-side semantics require it (no DOM, no CORS, `localStorage` scoped by module path) (Deno Web Platform API docs).

---

## ID-12: `import.meta` — Module Identity and Utilities

**Strength**: SHOULD

**Summary**: `import.meta` provides URL-based module identity, entry-point detection, and path resolution.

```js
// Module URL
console.log(import.meta.url);
// "file:///home/user/project/main.js"

// Entry-point detection (replaces Node's require.main === module)
if (import.meta.main) {
  console.log("Running as the main module");
  main();
}

// File path and directory (Deno-specific, undefined for remote modules)
console.log(import.meta.filename);  // "/home/user/project/main.js"
console.log(import.meta.dirname);   // "/home/user/project"

// Resolve sibling resources
const configUrl = new URL("./config.json", import.meta.url);
const config = JSON.parse(await Deno.readTextFile(configUrl));

// Resolve module specifiers
const workerUrl = import.meta.resolve("./worker.js");
```

**Note**: `import.meta.dirname` and `import.meta.filename` are `undefined` for remote modules. Use `new URL("./path", import.meta.url)` for portable resolution that works with both local and remote modules.

**Replaces Node.js**: `import.meta.main` → `require.main === module`, `import.meta.dirname` → `__dirname`, `import.meta.filename` → `__filename`.

**Rationale**: `import.meta.main` is Deno's way to detect whether a module is the entry point. `import.meta.dirname` and `import.meta.filename` replace Node's `__dirname` and `__filename`. `import.meta.resolve()` resolves specifiers relative to the current module (Deno namespace docs; Exploring JS Ch. 29).

---

## ID-13: `deno.json` — Configuration Overview

**Strength**: SHOULD

**Summary**: `deno.json` is auto-detected and consolidates imports, compiler options, tasks, and permissions in one file.

```jsonc
// deno.json (or deno.jsonc for comments)
{
  // Import map — centralized dependency versions
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0",
    "@std/path": "jsr:@std/path@^1.0.0",
    "chalk": "npm:chalk@5",
    "@shared/": "./shared/"
  },

  // TypeScript/JSDoc compiler options
  "compilerOptions": {
    "checkJs": true,
    "strict": true
  },

  // Task runner scripts
  "tasks": {
    "dev": "deno run --watch --allow-net --allow-read main.js",
    "start": "deno run --allow-net=:8080 --allow-read=./static main.js",
    "check": "deno check **/*.js"
  },

  // Exclude from all subcommands
  "exclude": ["vendor/", "node_modules/"]
}
```

**Key fields**: `imports` (import map), `compilerOptions`, `tasks`, `lint`, `fmt`, `lock`, `nodeModulesDir`, `unstable`, `permissions`, `exports`, `workspace`, `exclude`.

**Note**: If using Biome for linting/formatting, omit the `lint` and `fmt` fields — those are configured in `biome.json`. See `13-biome/01-setup.md`.

**Rationale**: `deno.json` replaces `package.json` + `tsconfig.json`. Accepts `.jsonc` (comments allowed). Auto-detected by walking up the directory tree. `deno add` and `deno remove` manage the `imports` field (Deno configuration docs).

**See also**: `10-project-structure.md` ID-15, ID-16

---

## ID-14: Import Maps — Bare Specifier Resolution

**Strength**: SHOULD

**Summary**: The `imports` field in `deno.json` maps bare specifiers to full specifiers. Versions are declared once.

```json
{
  "imports": {
    "@std/assert": "jsr:@std/assert@^1.0.0",
    "@std/path": "jsr:@std/path@^1.0.0",
    "@shared/": "./shared/",
    "@auth/": "./auth/"
  }
}
```

```js
// Source files use clean bare specifiers — no version strings
import { assertEquals } from "@std/assert";
import { join } from "@std/path";
import { login } from "@auth/mod.js";
```

**Managing imports**: `deno add jsr:@std/assert` adds to the import map. `deno remove @std/assert` removes it. Directory mappings (`@shared/`) enable project-internal path aliases.

**Rationale**: Import maps centralize version management — update once in `deno.json`, not in every source file. They implement the Web Import Maps Standard with Deno extensions (Deno import map docs).

**See also**: `10-project-structure.md` ID-16

---

## ID-15: `compilerOptions` for JSDoc Type Checking

**Strength**: SHOULD

**Summary**: Enable `checkJs` in `deno.json` to type-check plain JS files using JSDoc annotations.

```json
{
  "compilerOptions": {
    "checkJs": true,
    "strict": true
  }
}
```

```js
// @ts-check — per-file opt-in (use this when checkJs is NOT set globally in deno.json)

/**
 * @param {string} name
 * @returns {string}
 */
export function greet(name) {
  return `Hello, ${name}!`;
}

greet(42); // Type error: Argument of type 'number' is not assignable to parameter of type 'string'
```

**Type-checking commands**:
- `deno check main.js` — type-check without executing
- `deno run --check main.js` — type-check then execute
- `deno check --all main.js` — include remote modules and npm packages

**Wiring types to untyped JS**: Use `// @ts-types="./types.d.ts"` before an import to tell the compiler where to find type declarations for an untyped module.

**Rationale**: `deno run` does NOT type-check by default (for performance). `deno check` is separate and should be run in CI. Strict mode is Deno's default — the TypeScript core team's recommendation (Deno TypeScript docs).

**See also**: `05-type-discipline.md` ID-16, ID-20

---

## ID-16: Module Resolution — File Extensions Required

**Strength**: MUST

**Summary**: Deno requires explicit file extensions on all local import specifiers. No extension guessing.

```js
// Good — explicit extension
import { parse } from "./parser.js";
import { Config } from "./types.js";

// Bad — extensionless (error in Deno)
import { parse } from "./parser";
import { Config } from "./types";
```

**Rationale**: Deno resolves modules the way browsers do — directly to files without a `node_modules` tree or extension guessing. This is simpler, more predictable, and faster than Node.js's multi-step resolution algorithm (Deno ESM docs).

---

## ID-17: `jsr:` and `npm:` Specifiers — No Install Step

**Strength**: SHOULD

**Summary**: Import from JSR and npm registries by URL specifier. No `npm install` or `node_modules` required.

```js
// Good — JSR (Deno-native, TypeScript-native)
import { assertEquals } from "jsr:@std/assert@^1.0.0";
import { ulid } from "jsr:@std/ulid";

// Good — npm (for packages not on JSR)
import chalk from "npm:chalk@5";
import express from "npm:express@4";

// Good — via import map (preferred for application code)
// deno.json: { "imports": { "@std/assert": "jsr:@std/assert@^1.0.0" } }
import { assertEquals } from "@std/assert";
```

**Rationale**: Both `jsr:` and `npm:` specifiers are resolved on import — no install step, no lockfile management for development. `jsr:` packages support TypeScript natively and are Deno's preferred registry. Use `npm:` for packages that only exist on npm (Deno module resolution docs).

**See also**: `10-project-structure.md` ID-23

---

## ID-18: `node:` Specifiers for Node.js Built-In Compatibility

**Strength**: CONSIDER

**Summary**: Deno provides Node.js built-in modules via `node:` specifiers. Prefer Deno/Web APIs when equivalent.

```js
// Available but not preferred — Node.js built-in shims
import { readFile } from "node:fs/promises";
import { join } from "node:path";

// Preferred — Deno/Web equivalents
const text = await Deno.readTextFile("./data.txt");
const url = new URL("./data.txt", import.meta.url);
```

**Covered `node:` modules**: `fs`, `path`, `http`, `https`, `net`, `crypto`, `stream`, `buffer`, `os`, `process`, `child_process`, `events`, `url`, `util`, `assert`, `zlib`, and more.

**Rationale**: Deno implements Node.js built-in APIs for compatibility with the npm ecosystem. However, Deno's native APIs (`Deno.readTextFile`, `Deno.serve`, `fetch`) and Web Platform APIs (`URL`, `crypto.subtle`) are preferred because they are more portable (work in browsers too) and integrate with Deno's permission system. Use `node:` only when an npm dependency requires it (Deno Node compat docs).

---

## ID-19: HTTPS URL Imports

**Strength**: CONSIDER

**Summary**: Deno can import modules directly from HTTPS URLs. They are cached locally after first fetch.

```js
// Good — pinned URL import (version in URL)
import { Application } from "https://deno.land/x/oak@v17.0.0/mod.ts";

// Prefer — JSR or npm specifiers with import maps for most code
import { Application } from "jsr:@oak/oak@17";
```

**Rationale**: URL imports were Deno's original module resolution mechanism. They still work and are useful for quick scripts and CDN-hosted libraries. For project code, prefer `jsr:` / `npm:` specifiers with import maps for version management and reproducibility (Deno ESM docs).

---

## ID-20: `deno check` for Type Checking

**Strength**: SHOULD

**Summary**: `deno check` type-checks without executing. Use it in CI to catch type errors.

```sh
# Type-check a specific file
deno check main.js

# Type-check including remote/npm modules
deno check --all main.js

# Type-check then run
deno run --check main.js
```

**Commands that type-check by default**: `deno compile`, `deno publish`. `deno test` and `deno bench` type-checked by default in Deno 1.x but may skip type-checking in Deno 2.x for performance parity with `deno run` — check your Deno version's behavior.
**Commands that do NOT type-check**: `deno run` (for performance), `deno eval`, `deno repl`.

**Rationale**: Separating type-checking from execution is a deliberate performance decision. Run `deno check` in CI as a gate; use `deno run` (no check) for fast development iteration. For JS files, enable `"checkJs": true` in `deno.json` or add `// @ts-check` per file (Deno TypeScript docs).

**See also**: `05-type-discipline.md` ID-20

---

## ID-21: `deno doc` for API Documentation

**Strength**: SHOULD

**Summary**: `deno doc` extracts and displays JSDoc documentation from module exports.

```sh
# View docs for a local module
deno doc ./auth/mod.js

# View docs for a JSR package
deno doc jsr:@std/assert

# Generate JSON output for tooling
deno doc --json ./auth/mod.js
```

**Rationale**: `deno doc` reads JSDoc comments on exported symbols and produces formatted output. JSR auto-generates documentation pages from the same source. Write JSDoc for tooling, not just humans — see `11-documentation.md` ID-12 (Deno docs command).

**See also**: `11-documentation.md` ID-05, ID-11, ID-12

---

## ID-22: Deno LSP — Editor Integration

**Strength**: SHOULD

**Summary**: Deno's built-in Language Server Protocol provides autocomplete, hover docs, type errors, and go-to-definition in editors.

```jsonc
// .vscode/settings.json (for VS Code)
{
  "deno.enable": true,
  "deno.lint": true,
  "editor.defaultFormatter": "biomejs.biome"  // Biome for formatting
}
```

**What the LSP provides**: Autocomplete from JSDoc types, hover documentation, inline type errors, go-to-definition (including into `.d.ts` files), auto-import suggestions, and integration with `deno.json` import maps.

**Rationale**: The LSP is `tsc` under the hood — it reads JSDoc annotations the same way it reads TypeScript types. Combined with `checkJs`, plain JS files get most of TypeScript's static analysis (Deno TypeScript docs).

**See also**: `05-type-discipline.md` ID-20

---

## ID-23: `npm:` Packages Without `node_modules`

**Strength**: SHOULD

**Summary**: `npm:` specifiers resolve packages from the npm registry and cache them globally — no `node_modules` directory by default.

```js
// Good — npm package, no install step
import chalk from "npm:chalk@5";
import express from "npm:express@4";

// Run npm CLI tools directly
// deno run -A npm:create-vite@latest

// Subpath imports
import { say } from "npm:cowsay@1.6.0/cowthink";
```

**When `node_modules` is needed**: Some npm packages with native addons or specific file-system assumptions require a local `node_modules`. Set `"nodeModulesDir": "auto"` in `deno.json` for these cases.

**Rationale**: Deno resolves npm packages on-demand from the registry and caches them globally, avoiding the `node_modules` directory entirely for most packages. npm packages run inside Deno's permission sandbox (Deno npm specifier docs).

---

## ID-24: `deno compile` — Standalone Executables

**Strength**: CONSIDER

**Summary**: Compile a program and all dependencies into a single self-contained binary. No Deno installation needed on the target.

```sh
# Compile with embedded permissions
deno compile --allow-net=:8080 --allow-read=./static -o myserver main.js

# Cross-compile for a different target
deno compile --target x86_64-unknown-linux-gnu -o myserver main.js

# Run the compiled binary (no Deno needed)
./myserver
```

**Key facts**:
- Embeds the Deno runtime, all dependencies, and permission grants
- Type-checks by default (unlike `deno run`)
- Supports cross-compilation to different OS/architecture targets

**Rationale**: `deno compile` produces a single binary that can be distributed to any machine without requiring Deno. Permissions are baked in at compile time — the binary runs with exactly the grants specified in the compile command (Deno compile docs).

---

## ID-25: Standard Library — `@std/` on JSR

**Strength**: SHOULD

**Summary**: Deno's standard library is published as `@std/*` packages on JSR. Import explicitly — nothing is bundled into the runtime.

```js
// Good — import from standard library
import { assertEquals, assertThrows } from "@std/assert";
import { join, dirname } from "@std/path";
import { delay } from "@std/async";

// Add to project: deno add jsr:@std/assert jsr:@std/path
```

**Selected `@std` packages**:

| Package | Purpose |
|---------|---------|
| `@std/assert` | Test assertions |
| `@std/testing` | Test utilities (BDD, mocking, snapshots) |
| `@std/path` | Path manipulation |
| `@std/fs` | File system utilities |
| `@std/http` | HTTP utilities |
| `@std/streams` | Stream utilities |
| `@std/encoding` | Base64, hex, etc. |
| `@std/async` | Delay, debounce, retry |
| `@std/ulid` | ULID generation |

**Rationale**: Unlike Node.js, Deno's standard library is not bundled into the runtime — it's a set of independently versioned packages on JSR. This enables faster runtime releases and lets you pin library versions independently. All `@std` packages are officially maintained (Deno standard library docs).

---

## ID-26: No `require()`, No `module.exports` — ESM Only

**Strength**: MUST

**Summary**: Deno uses ESM exclusively. There is no `require()`, no `module.exports`, no CommonJS.

```js
// Good — ESM with Deno APIs
const data = await Deno.readTextFile("./input.txt");
export function process(data) { /* ... */ }

// Bad — CommonJS (does not work in Deno modules)
const fs = require("fs"); // ReferenceError: require is not defined
module.exports = { process }; // ReferenceError: module is not defined
```

**Rationale**: Deno is ESM-native. CommonJS is only available inside `.cjs` files or npm packages that use CommonJS internally. All Deno-native code uses `import`/`export` (Deno ESM docs).

**See also**: `01-core-idioms.md` ID-08, `09-anti-patterns.md` ID-33

---

## ID-27: No `__dirname` / `__filename` — Use `import.meta`

**Strength**: SHOULD

**Summary**: `__dirname` and `__filename` are CommonJS globals that don't exist in Deno. See ID-12 for the `import.meta` replacements.

```js
// Node.js (does not work in Deno)
const dir = __dirname;      // ReferenceError
const file = __filename;    // ReferenceError

// Deno — see ID-12 for full examples
const dir = import.meta.dirname;
const file = import.meta.filename;
```

**See also**: ID-12 for the complete `import.meta` reference including `.main`, `.url`, `.resolve()`, and the remote-module caveat.

---

## ID-28: No `process` Global — Use `Deno.env`, `Deno.args`, `Deno.exit()`

**Strength**: SHOULD

**Summary**: Deno has no `process` global. Use the `Deno` namespace for equivalent functionality.

| Node.js (`process.*`) | Deno equivalent |
|----------------------|-----------------|
| `process.env.PORT` | `Deno.env.get("PORT")` |
| `process.argv.slice(2)` | `Deno.args` |
| `process.exit(1)` | `Deno.exit(1)` |
| `process.cwd()` | `Deno.cwd()` |
| `process.platform` | `Deno.build.os` |
| `process.pid` | `Deno.pid` |
| `process.on("SIGINT", fn)` | `Deno.addSignalListener("SIGINT", fn)` |

**Rationale**: `process` is a Node.js global that doesn't exist in Deno-native code. It is available inside npm packages (for compat), but Deno-native code should use the `Deno` namespace (Deno Node compat docs).

---

## ID-29: No `Buffer` — Use `Uint8Array` and `TextEncoder`/`TextDecoder`

**Strength**: SHOULD

**Summary**: Deno uses the Web Platform's `Uint8Array` for binary data. Node's `Buffer` is not a global.

```js
// Good — Web Platform APIs
const encoder = new TextEncoder();
const decoder = new TextDecoder();

const bytes = encoder.encode("Hello, World!");  // Uint8Array
const text = decoder.decode(bytes);              // string

// Read binary file as Uint8Array
const data = await Deno.readFile("./image.png"); // returns Uint8Array

// Good — base64 encoding/decoding
const base64 = btoa(String.fromCharCode(...bytes));
// Or use @std/encoding for more options
import { encodeBase64 } from "@std/encoding/base64";
const b64 = encodeBase64(bytes);
```

**Rationale**: `Buffer` is Node.js-specific. `Uint8Array` is the Web Platform standard for binary data and is used throughout Deno's APIs. `TextEncoder`/`TextDecoder` handle the string ↔ bytes conversion (Deno Web Platform API docs).

---

## ID-30: Deno Error Classes — Structured Error Types

**Strength**: CONSIDER

**Summary**: Deno provides structured error types under `Deno.errors` for common failure modes.

```js
try {
  await Deno.readTextFile("./missing.txt");
} catch (err) {
  if (err instanceof Deno.errors.NotFound) {
    console.error("File not found");
  } else if (err instanceof Deno.errors.PermissionDenied) {
    console.error("Missing --allow-read permission");
  } else {
    throw err;
  }
}
```

**Available error classes**: `Deno.errors.NotFound`, `Deno.errors.PermissionDenied`, `Deno.errors.ConnectionRefused`, `Deno.errors.ConnectionReset`, `Deno.errors.AddrInUse`, `Deno.errors.BadResource`, and ~15 more.

**Rationale**: Deno's structured error classes enable precise `instanceof` checks for error handling — more reliable than checking `err.code` strings (Deno namespace API docs).

**See also**: `03-error-handling.md` ID-05, ID-09

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Secure by default | MUST | No access without explicit permission flags |
| 02 | Granular permissions | SHOULD | Scope to specific paths, hosts, variables |
| 03 | Runtime permission requests | CONSIDER | Progressive escalation with `Deno.permissions` |
| 04 | `-A` only for dev | MUST | Never in production — disables sandbox entirely |
| 05 | File I/O via `Deno.*` | SHOULD | Async by default; `readTextFile`, `writeTextFile`, `open` |
| 06 | `Deno.serve()` for HTTP | SHOULD | Web API Request/Response; HTTP/2; auto-compress |
| 07 | `Deno.Command` for subprocesses | SHOULD | Replaces deprecated `Deno.run`; Web Streams I/O |
| 08 | `Deno.env` for env vars | SHOULD | No `process.env`; requires `--allow-env` |
| 09 | Runtime introspection | CONSIDER | `Deno.args`, `Deno.cwd()`, `Deno.build` |
| 10 | `fetch()` is global | MUST | No import needed; WHATWG standard |
| 11 | Web Platform APIs | SHOULD | URL, crypto, streams, timers, AbortController |
| 12 | `import.meta` | SHOULD | `.main`, `.url`, `.dirname`, `.filename`, `.resolve()` |
| 13 | `deno.json` config | SHOULD | Imports, compiler options, tasks, excludes |
| 14 | Import maps | SHOULD | Bare specifiers, centralized versions |
| 15 | `compilerOptions.checkJs` | SHOULD | Type-check JS with JSDoc |
| 16 | File extensions required | MUST | No extension guessing on local imports |
| 17 | `jsr:` and `npm:` specifiers | SHOULD | No install step; JSR preferred |
| 18 | `node:` for Node compat | CONSIDER | Prefer Deno/Web APIs when equivalent |
| 19 | HTTPS URL imports | CONSIDER | Cached locally; prefer JSR/npm for projects |
| 20 | `deno check` in CI | SHOULD | Type-check separately from execution |
| 21 | `deno doc` for docs | SHOULD | JSDoc extraction; JSR auto-generates docs |
| 22 | Deno LSP for editors | SHOULD | Autocomplete, hover, type errors from JSDoc |
| 23 | `npm:` without `node_modules` | SHOULD | Global cache; `nodeModulesDir` for edge cases |
| 24 | `deno compile` | CONSIDER | Single binary; cross-compile; embedded permissions |
| 25 | `@std/*` standard library | SHOULD | On JSR; independently versioned; not bundled |
| 26 | No `require()` | MUST | ESM only; CJS only in .cjs or npm packages |
| 27 | No `__dirname`/`__filename` | SHOULD | Use `import.meta` — see ID-12 |
| 28 | No `process` global | SHOULD | Use `Deno.env`, `Deno.args`, `Deno.exit()` |
| 29 | No `Buffer` | SHOULD | Use `Uint8Array` + `TextEncoder`/`TextDecoder` |
| 30 | `Deno.errors.*` | CONSIDER | Structured error classes for `instanceof` checks |

### Node.js → Deno Quick Reference

| Node.js | Deno |
|---------|------|
| `require("fs")` | `import from "node:fs"` or `Deno.readTextFile()` |
| `process.env.X` | `Deno.env.get("X")` |
| `process.argv` | `Deno.args` |
| `__dirname` | `import.meta.dirname` |
| `__filename` | `import.meta.filename` |
| `Buffer.from()` | `new TextEncoder().encode()` |
| `http.createServer()` | `Deno.serve()` |
| `child_process.exec()` | `new Deno.Command()` |
| `npm install` | `deno add` (or just import `jsr:`/`npm:`) |
| `npm test` | `deno test` |
| `eslint + prettier` | `deno lint + deno fmt` (or Biome) |
| `package.json` | `deno.json` |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for ESM-only (ID-08), named exports (ID-07), Deno-first (ID-20)
- **API Design**: See `02-api-design.md` for async function conventions (ID-25), module design (ID-06–10)
- **Error Handling**: See `03-error-handling.md` for `Deno.errors.*` usage (ID-05, ID-09), AbortSignal (references `07-async-concurrency.md` ID-23–26)
- **Type Discipline**: See `05-type-discipline.md` for JSDoc annotations (ID-16–20), `deno check` integration (ID-20)
- **Async & Concurrency**: See `07-async-concurrency.md` for `fetch()` with signals (ID-24), `Deno.serve()` streaming (ID-27–29)
- **Anti-Patterns**: See `09-anti-patterns.md` for CommonJS (ID-33), `for...in` (ID-29)
- **Project Structure**: See `10-project-structure.md` for `deno.json` placement (ID-15), import maps (ID-16), workspaces (ID-25)
- **Documentation**: See `11-documentation.md` for `deno doc` usage (ID-12), JSDoc prose (ID-05–09)
- **Testing**: See `12-deno/02-testing.md` for `Deno.test()`, assertions, and mocking
- **Task Runner**: See `12-deno/03-task-runner.md` for `deno task` patterns
- **Publishing**: See `12-deno/04-publishing.md` for JSR publishing

---

## External References

- [Deno Manual](https://docs.deno.com/)
- [Deno — Permissions](https://docs.deno.com/runtime/fundamentals/security/)
- [Deno — Configuration](https://docs.deno.com/runtime/fundamentals/configuration/)
- [Deno — Node.js Compatibility](https://docs.deno.com/runtime/fundamentals/node/)
- [Deno — Standard Library](https://jsr.io/@std)
- [Deno — TypeScript Support](https://docs.deno.com/runtime/fundamentals/typescript/)
- *Exploring JavaScript* (ES2025) — Axel Rauschmayer
