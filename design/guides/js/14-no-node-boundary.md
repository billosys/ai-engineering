# No-Node Boundary

The consolidated reference for every Node.js pattern this project avoids and its Deno replacement. This is not a Deno vs Node.js debate — it's a practical boundary specification: "In this project, here's what we use instead." Each entry is brief: state the Node.js pattern, name the Deno replacement, cross-reference the guide that covers it in detail. When Claude Code encounters a Node.js pattern and is about to emit it, this guide catches the mistake. Grounded in Deno documentation concept cards and *JavaScript: The Definitive Guide* (Flanagan).

Target environment: **Deno**, **ESM-only**, **Biome** for linting/formatting, **no TypeScript** (plain JS with JSDoc where needed).

---

## ID-01: No `require()` — ESM `import` Only

**Strength**: MUST-AVOID

**Summary**: `require()` is CommonJS. It does not exist in Deno ESM modules.

```js
// Node.js (avoid)
const { readFile } = require("fs");
const utils = require("./utils");

// Deno (use instead)
const text = await Deno.readTextFile("./data.txt");  // preferred
import { transform } from "./utils.js";  // extension required

// Compat only (when migrating incrementally):
import { readFile } from "node:fs/promises";
```

**Why not Node.js**: `require()` is synchronous, runtime-evaluated, prevents tree shaking, and is not available in ESM. Deno uses ESM exclusively.

**Deno replacement**: `import` statements with explicit file extensions.

**See also**: `01-core-idioms.md` ID-08, `09-anti-patterns.md` ID-33, `12-deno/01-runtime-basics.md` ID-26

---

## ID-02: No `module.exports` — Use `export`

**Strength**: MUST-AVOID

**Summary**: `module.exports` is CommonJS. Use ESM `export` for all module exports.

```js
// Node.js (avoid)
module.exports = { parse, stringify };
exports.parse = parse;

// Deno (use instead)
export function parse(input) { /* ... */ }
export function stringify(data) { /* ... */ }
```

**Why not Node.js**: `module.exports` is CommonJS syntax. ESM `export` is static, enables tree shaking, and is the JavaScript standard.

**Deno replacement**: `export` (named) or `export default` (single primary export).

**See also**: `01-core-idioms.md` ID-07, ID-08

---

## ID-03: No Extensionless Imports — File Extensions Required

**Strength**: MUST-AVOID

**Summary**: Deno resolves imports like a browser — no extension guessing, no `index.js` resolution.

```js
// Node.js (avoid)
import { parse } from "./parser";      // guesses .js, .ts, .json
import { utils } from "./lib";         // resolves to ./lib/index.js

// Deno (use instead)
import { parse } from "./parser.js";   // explicit extension
import { utils } from "./lib/mod.js";  // explicit entry point
```

**Why not Node.js**: Node's multi-step resolution (try `.js`, `.ts`, `.json`, then `index.js`) is implicit and slow. Deno's explicit resolution is predictable and matches browser behavior.

**Deno replacement**: Always include the file extension. Use `mod.js` instead of `index.js`.

**See also**: `12-deno/01-runtime-basics.md` ID-16, `10-project-structure.md` ID-08

---

## ID-04: No `index.js` Convention — Use `mod.js`

**Strength**: SHOULD-AVOID

**Summary**: Deno uses `mod.js` (or `mod.ts`) as the entry point convention, not `index.js`.

```
// Node.js (avoid)
my-lib/
├── index.js        # Node convention
└── src/

// Deno (use instead)
my-lib/
├── mod.js          # Deno convention
└── src/
```

**Why not Node.js**: `index.js` is tied to Node's directory-as-module resolution (importing `"./lib"` resolves to `"./lib/index.js"`). Deno does not support this implicit resolution.

**Deno replacement**: `mod.js` for entry points. The `exports` field in `deno.json` is the actual mechanism.

**See also**: `10-project-structure.md` ID-08, `12-deno/04-publishing.md` ID-03

---

## ID-05: No `package.json` — Use `deno.json`

**Strength**: MUST-AVOID

**Summary**: `deno.json` replaces `package.json`, `tsconfig.json`, `.eslintrc`, and `.prettierrc` in one file.

```jsonc
// Node.js (avoid)
// package.json + tsconfig.json + .eslintrc + .prettierrc = 4 files

// Deno (use instead) — one file
{
  "imports": { "@std/assert": "jsr:@std/assert@^1.0.0" },
  "tasks": { "dev": "deno run --watch --allow-net main.js" },
  "compilerOptions": { "checkJs": true, "strict": true }
}
```

**Why not Node.js**: `package.json` requires `npm install` to populate `node_modules`. It scatters configuration across multiple files.

**Deno replacement**: `deno.json` with `imports`, `tasks`, and `compilerOptions`. Biome config goes in `biome.json`.

**See also**: `10-project-structure.md` ID-15, `12-deno/01-runtime-basics.md` ID-13

---

## ID-06: No `node_modules` — Deno Uses a Global Cache

**Strength**: MUST-AVOID

**Summary**: `jsr:` and `npm:` specifiers resolve on demand. No `npm install`, no `node_modules` directory.

```sh
# Node.js (avoid)
npm install chalk
# Creates node_modules/ with hundreds of nested directories

# Deno (use instead)
# Just import it — no install step
import chalk from "npm:chalk@5";
# Or add to import map: deno add npm:chalk@5
```

**Why not Node.js**: `node_modules` is a heavyweight, often duplicated dependency tree. Deno's global cache eliminates it for most packages.

**Deno replacement**: `jsr:` and `npm:` specifiers with import maps in `deno.json`. Use `deno add` to manage the import map.

**See also**: `12-deno/01-runtime-basics.md` ID-17, ID-23

---

## ID-07: No `npm install` / `npm run` — Use `deno add` / `deno task`

**Strength**: MUST-AVOID

**Summary**: Deno has built-in equivalents for npm's install and script runner.

```sh
# Node.js (avoid)
npm install chalk
npm run dev
npx create-vite

# Deno (use instead)
deno add npm:chalk@5
deno task dev
deno run -A npm:create-vite@latest
```

**Deno replacement**: `deno add` manages the import map. `deno task` runs scripts from `deno.json`. `deno run npm:tool` replaces `npx`.

**See also**: `12-deno/03-task-runner.md` ID-01

---

## ID-08: No `.eslintrc` / `.prettierrc` — Use `biome.json`

**Strength**: MUST-AVOID

**Summary**: Biome replaces ESLint + Prettier with one tool and one config file.

```
// Node.js (avoid)
.eslintrc.json + .prettierrc + eslint-config-* + prettier-plugin-*

// Deno (use instead)
biome.json    # lint + format in one file
```

**Deno replacement**: `biome.json` for lint and format. Omit `lint` and `fmt` from `deno.json` when using Biome.

**See also**: `13-biome/01-setup.md` ID-06, ID-16

---

## ID-09: No `tsconfig.json` — Use `compilerOptions` in `deno.json`

**Strength**: MUST-AVOID

**Summary**: TypeScript/JSDoc compiler options go in `deno.json`, not a separate `tsconfig.json`.

```jsonc
// Node.js (avoid) — tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "target": "ES2022",
    "module": "ESNext",
    "checkJs": true
  }
}

// Deno (use instead) — deno.json
{
  "compilerOptions": {
    "checkJs": true,
    "strict": true
    // target and module are handled by the Deno runtime — no need to specify
  }
}
```

**Key mappings**: `strict`, `checkJs`, `lib`, `jsx`, `jsxImportSource` transfer directly. `target`, `module`, `moduleResolution`, and `outDir` are not needed — Deno handles these at runtime.

**See also**: `12-deno/01-runtime-basics.md` ID-15

---

## ID-10: No `process.env` — Use `Deno.env.get()`

**Strength**: SHOULD-AVOID

**Summary**: `process` is not a Deno global. Use the `Deno` namespace for environment access.

```js
// Node.js (avoid)
const port = process.env.PORT || 3000;

// Deno (use instead) — also uses ?? instead of || to preserve 0 as valid
const port = Number(Deno.env.get("PORT") ?? "8080");
```

**Two improvements in one**: The Deno version replaces `process.env` with `Deno.env.get()` AND replaces `||` with `??` to preserve falsy-but-valid values like `0`. See `01-core-idioms.md` ID-03.

**Requires**: `--allow-env` (or `--allow-env=PORT` for granular access).

**See also**: `12-deno/01-runtime-basics.md` ID-08

---

## ID-11: No `process.argv` — Use `Deno.args`

**Strength**: SHOULD-AVOID

**Summary**: `Deno.args` contains only user arguments — no runtime or script path prefix.

```js
// Node.js (avoid)
const args = process.argv.slice(2);

// Deno (use instead)
const args = Deno.args;  // already just the user arguments
```

**See also**: `12-deno/01-runtime-basics.md` ID-09

---

## ID-12: No `__dirname` / `__filename` — Use `import.meta`

**Strength**: SHOULD-AVOID

**Summary**: ESM has no `__dirname` or `__filename`. Use `import.meta.dirname` and `import.meta.filename`.

```js
// Node.js (avoid)
const configPath = path.join(__dirname, "config.json");

// Deno (use instead)
const configPath = `${import.meta.dirname}/config.json`;
// Or for URL-based resolution (works with remote modules too):
const configUrl = new URL("./config.json", import.meta.url);
```

**See also**: `12-deno/01-runtime-basics.md` ID-12

---

## ID-13: No `Buffer` — Use `Uint8Array` + `TextEncoder`/`TextDecoder`

**Strength**: SHOULD-AVOID

**Summary**: `Buffer` is Node-specific. The Web Platform uses `Uint8Array` for binary data.

```js
// Node.js (avoid)
const buf = Buffer.from("hello", "utf8");
const str = buf.toString("utf8");

// Deno (use instead)
const bytes = new TextEncoder().encode("hello");
const str = new TextDecoder().decode(bytes);
```

**See also**: `12-deno/01-runtime-basics.md` ID-29

---

## ID-14: No `fs.readFile` / `fs.writeFile` — Use `Deno.readTextFile` / `Deno.writeTextFile`

**Strength**: SHOULD-AVOID

**Summary**: Deno has its own async file I/O that integrates with the permission system.

```js
// Node.js (avoid)
import { readFile, writeFile } from "node:fs/promises";
const text = await readFile("./data.txt", "utf8");
await writeFile("./output.txt", result);

// Deno (use instead)
const text = await Deno.readTextFile("./data.txt");
await Deno.writeTextFile("./output.txt", result);
```

**Requires**: `--allow-read`, `--allow-write`.

**See also**: `12-deno/01-runtime-basics.md` ID-05

---

## ID-15: No `http.createServer` — Use `Deno.serve()`

**Strength**: SHOULD-AVOID

**Summary**: `Deno.serve()` uses standard Web API `Request`/`Response` types — the same as `fetch()`.

```js
// Node.js (avoid)
import http from "node:http";
http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Hello");
}).listen(8000);

// Deno (use instead)
Deno.serve(() => new Response("Hello"));
```

**Requires**: `--allow-net`.

**See also**: `12-deno/01-runtime-basics.md` ID-06

---

## ID-16: No `child_process.exec` — Use `Deno.Command`

**Strength**: SHOULD-AVOID

**Summary**: `Deno.Command` is a single, unified subprocess API. It does not invoke a shell by default.

```js
// Node.js (avoid)
import { execSync } from "node:child_process";
const output = execSync("git log --oneline", { encoding: "utf8" });

// Deno (use instead)
const cmd = new Deno.Command("git", { args: ["log", "--oneline"] });
const { stdout } = await cmd.output();
console.log(new TextDecoder().decode(stdout));
```

**Requires**: `--allow-run`.

**See also**: `12-deno/01-runtime-basics.md` ID-07

---

## ID-17: No Node Streams — Use Web Streams API

**Strength**: SHOULD-AVOID

**Summary**: Deno uses WHATWG `ReadableStream`/`WritableStream`/`TransformStream` — the web standard.

```js
// Node.js (avoid)
import { createReadStream } from "node:fs";
const stream = createReadStream("large-file.txt");
stream.on("data", (chunk) => process(chunk));

// Deno (use instead)
const file = await Deno.open("large-file.txt");
for await (const chunk of file.readable) {
  process(chunk);
}
file.close();
```

**See also**: `07-async-concurrency.md` ID-27, ID-28, ID-29

---

## ID-18: No `EventEmitter` — Use `EventTarget` or Explicit Callbacks

**Strength**: SHOULD-AVOID

**Summary**: `EventTarget` is the web-standard event system. It works identically in Deno and browsers.

```js
// Node.js (avoid)
import { EventEmitter } from "node:events";
const emitter = new EventEmitter();
emitter.on("data", (payload) => handle(payload));
emitter.emit("data", { id: 1 });

// Deno (use instead)
const target = new EventTarget();
target.addEventListener("data", (e) => handle(e.detail));
target.dispatchEvent(new CustomEvent("data", { detail: { id: 1 } }));
```

**Why not Node.js**: `EventEmitter` is Node-specific. `EventTarget` is the web standard, available in Deno, browsers, and modern Node.js.

---

## ID-19: No Error-First Callbacks — Use `async`/`await`

**Strength**: MUST-AVOID

**Summary**: Deno's entire API surface is Promise-based. Never use the `(err, result)` callback pattern.

```js
// Node.js (avoid)
fs.readFile("data.txt", "utf8", (err, text) => {
  if (err) throw err;
  process(text);
});

// Deno (use instead)
const text = await Deno.readTextFile("data.txt");
process(text);
```

**See also**: `07-async-concurrency.md` ID-09

---

## ID-20: No `process.nextTick` — Use `queueMicrotask()`

**Strength**: SHOULD-AVOID

**Summary**: `queueMicrotask()` is the web-standard microtask scheduler.

```js
// Node.js (avoid)
process.nextTick(() => doWork());

// Deno (use instead)
queueMicrotask(() => doWork());
```

**See also**: `07-async-concurrency.md` ID-04

---

## ID-21: No Jest / Mocha / Vitest — Use `Deno.test()` + `@std/assert`

**Strength**: MUST-AVOID

**Summary**: Deno has a built-in test runner. No framework installation needed.

```js
// Node.js (avoid)
import { test, expect } from "vitest";
test("adds correctly", () => { expect(1 + 2).toBe(3); });

// Deno (use instead)
import { assertEquals } from "@std/assert";
Deno.test("adds correctly", () => { assertEquals(1 + 2, 3); });
```

**See also**: `12-deno/02-testing.md` ID-01, ID-06

---

## ID-22: No ESLint / No Prettier — Use Biome

**Strength**: MUST-AVOID

**Summary**: Biome replaces both ESLint and Prettier with a single tool — faster, unified, one config.

```sh
# Node.js (avoid)
eslint --fix src/ && prettier --write src/    # two tools, two configs, two passes

# Deno (use instead)
biome check --write                           # one tool, one config, one pass
```

**See also**: `13-biome/01-setup.md` ID-01, ID-02, `13-biome/03-formatting.md` ID-12

---

## ID-23: No `npx` — Use `deno run` with Specifiers

**Strength**: SHOULD-AVOID

**Summary**: `deno run npm:tool@version` replaces `npx tool`.

```sh
# Node.js (avoid)
npx create-vite@latest

# Deno (use instead)
deno run -A npm:create-vite@latest
```

**See also**: `12-deno/03-task-runner.md` ID-11

---

## ID-24: `npm:` Specifier — The Acceptable Escape Hatch

**Strength**: CONSIDER-AVOIDING

**Summary**: Use `npm:` specifiers for npm packages that have no JSR equivalent. This is a legitimate use case, not a failure.

```js
// Acceptable — no JSR equivalent exists
import chalk from "npm:chalk@5";
import express from "npm:express@4";

// Preferred — JSR package available
import { assertEquals } from "jsr:@std/assert@^1.0.0";
```

**When `npm:` is fine**: Consuming established npm packages. Running npm CLI tools. Gradual migration from Node.js.

**When to prefer alternatives**: If a JSR (`jsr:`) equivalent exists, use it — JSR packages are TypeScript-native, auto-documented, and designed for Deno.

**See also**: `12-deno/01-runtime-basics.md` ID-17

---

## ID-25: `node:` Specifier — Available but Not Preferred

**Strength**: CONSIDER-AVOIDING

**Summary**: Deno provides `node:` built-in shims for compatibility. Prefer Deno/Web APIs for new code.

```js
// Available but not preferred
import { readFile } from "node:fs/promises";
import { join } from "node:path";

// Preferred
const text = await Deno.readTextFile("./data.txt");
const url = new URL("./data.txt", import.meta.url);
```

**Common `node:` modules**: `fs`, `path`, `http`, `https`, `net`, `crypto`, `stream`, `buffer`, `os`, `process`, `child_process`, `events`, `url`, `util`, `assert`, `zlib`.

**When `node:` is acceptable**: Inside npm package dependencies (they need it). When migrating incrementally and the Deno equivalent requires significant refactoring.

**See also**: `12-deno/01-runtime-basics.md` ID-18

---

## ID-26: `nodeModulesDir` — Last Resort for Compat

**Strength**: CONSIDER-AVOIDING

**Summary**: Set `"nodeModulesDir": "auto"` only when a framework or native addon requires a local `node_modules` directory.

```jsonc
// deno.json — only when needed
{
  "nodeModulesDir": "auto"
}
```

**When needed**: Frameworks that resolve modules from `node_modules` (Vite, Next.js). Node-API native addons (`--allow-ffi`). IDE tooling that expects `node_modules`.

**When NOT needed**: Pure Deno code with `jsr:` and `npm:` specifiers. The global cache handles everything.

**See also**: `12-deno/01-runtime-basics.md` ID-23

---

## Best Practices Summary

### Quick Reference Table

| ID | Avoid | Strength | Replacement |
|----|-------|----------|-------------|
| 01 | `require()` | MUST-AVOID | ESM `import` |
| 02 | `module.exports` | MUST-AVOID | ESM `export` |
| 03 | Extensionless imports | MUST-AVOID | Explicit `.js` extension |
| 04 | `index.js` | SHOULD-AVOID | `mod.js` |
| 05 | `package.json` | MUST-AVOID | `deno.json` |
| 06 | `node_modules` | MUST-AVOID | Global cache (`jsr:`/`npm:`) |
| 07 | `npm install`/`npm run` | MUST-AVOID | `deno add`/`deno task` |
| 08 | `.eslintrc`/`.prettierrc` | MUST-AVOID | `biome.json` |
| 09 | `tsconfig.json` | MUST-AVOID | `deno.json` `compilerOptions` |
| 10 | `process.env` | SHOULD-AVOID | `Deno.env.get()` |
| 11 | `process.argv` | SHOULD-AVOID | `Deno.args` |
| 12 | `__dirname`/`__filename` | SHOULD-AVOID | `import.meta.dirname`/`.filename` |
| 13 | `Buffer` | SHOULD-AVOID | `Uint8Array` + `TextEncoder`/`TextDecoder` |
| 14 | `fs.readFile`/`writeFile` | SHOULD-AVOID | `Deno.readTextFile`/`writeTextFile` |
| 15 | `http.createServer` | SHOULD-AVOID | `Deno.serve()` |
| 16 | `child_process` | SHOULD-AVOID | `Deno.Command` |
| 17 | Node streams | SHOULD-AVOID | Web Streams API |
| 18 | `EventEmitter` | SHOULD-AVOID | `EventTarget` + `CustomEvent` |
| 19 | Error-first callbacks | MUST-AVOID | `async`/`await` |
| 20 | `process.nextTick` | SHOULD-AVOID | `queueMicrotask()` |
| 21 | Jest/Mocha/Vitest | MUST-AVOID | `Deno.test()` + `@std/assert` |
| 22 | ESLint + Prettier | MUST-AVOID | Biome (`biome check --write`) |
| 23 | `npx` | SHOULD-AVOID | `deno run npm:tool` |
| 24 | `npm:` (when JSR exists) | CONSIDER-AVOIDING | `jsr:` specifiers |
| 25 | `node:` built-ins | CONSIDER-AVOIDING | Deno/Web APIs |
| 26 | `nodeModulesDir` | CONSIDER-AVOIDING | Global cache (default) |

### Comprehensive Node.js → Deno Replacement Table

| Category | Node.js | Deno | Guide Reference |
|----------|---------|------|-----------------|
| **Modules** | `require("./mod")` | `import from "./mod.js"` | 01 ID-08 |
| | `module.exports` | `export` | 01 ID-07 |
| | `index.js` | `mod.js` | 10 ID-08 |
| **Config** | `package.json` | `deno.json` | 10 ID-15, 12-01 ID-13 |
| | `tsconfig.json` | `deno.json` `compilerOptions` | 12-01 ID-15 |
| | `.eslintrc` + `.prettierrc` | `biome.json` | 13-01 ID-06 |
| | `node_modules` | Global cache | 12-01 ID-23 |
| | `npm install` | `deno add` | 12-03 ID-01 |
| | `npm run` | `deno task` | 12-03 ID-01 |
| | `npx tool` | `deno run npm:tool` | 12-03 ID-11 |
| **Globals** | `process.env.X` | `Deno.env.get("X")` | 12-01 ID-08 |
| | `process.argv.slice(2)` | `Deno.args` | 12-01 ID-09 |
| | `process.exit(n)` | `Deno.exit(n)` | 12-01 ID-09 |
| | `__dirname` | `import.meta.dirname` | 12-01 ID-12 |
| | `__filename` | `import.meta.filename` | 12-01 ID-12 |
| | `Buffer.from(str)` | `new TextEncoder().encode(str)` | 12-01 ID-29 |
| | `Buffer.alloc(n)` | `new Uint8Array(n)` | 12-01 ID-29 |
| **I/O** | `fs.readFile` | `Deno.readTextFile` | 12-01 ID-05 |
| | `fs.writeFile` | `Deno.writeTextFile` | 12-01 ID-05 |
| | `fs.stat` | `Deno.stat` | 12-01 ID-05 |
| | `fs.mkdir` | `Deno.mkdir` | 12-01 ID-05 |
| **Network** | `http.createServer` | `Deno.serve()` | 12-01 ID-06 |
| | `child_process.exec` | `Deno.Command` | 12-01 ID-07 |
| | `child_process.fork` | Deno Workers | 07 ID-30 |
| **Streams** | Node `Readable`/`Writable` | `ReadableStream`/`WritableStream` | 07 ID-27 |
| | Node `Transform` | `TransformStream` | 07 ID-28 |
| | `.pipe()` | `.pipeThrough()`/`.pipeTo()` | 07 ID-28 |
| **Events** | `EventEmitter` | `EventTarget` + `CustomEvent` | 12-01 ID-11 |
| | `process.nextTick` | `queueMicrotask()` | 07 ID-04 |
| **Patterns** | Error-first callbacks | `async`/`await` | 07 ID-09 |
| | `callback(err, result)` | `try { await fn() }` | 03 ID-14 |
| **Testing** | Jest / Mocha / Vitest | `Deno.test()` + `@std/assert` | 12-02 ID-01 |
| **Linting** | ESLint | Biome | 13-01 ID-01 |
| **Formatting** | Prettier | Biome | 13-01 ID-01 |
| **Registry** | npm | JSR (`jsr:`) preferred; `npm:` for compat | 12-01 ID-17, 12-04 |

---

## Related Guidelines

- **Core Idioms**: See `01-core-idioms.md` for ESM-only (ID-08), named exports (ID-07), Deno-first (ID-20)
- **Error Handling**: See `03-error-handling.md` for async/await patterns (ID-14, ID-19) replacing callbacks
- **Async & Concurrency**: See `07-async-concurrency.md` for Web Streams (ID-27–29), `queueMicrotask` (ID-04), promisification (ID-09)
- **Anti-Patterns**: See `09-anti-patterns.md` for `require()` (ID-33), `var` (ID-28), `for...in` (ID-29) — automated catches
- **Project Structure**: See `10-project-structure.md` for `deno.json` (ID-15), `mod.js` (ID-08), import maps (ID-16)
- **Runtime Basics**: See `12-deno/01-runtime-basics.md` for every Deno API replacement (ID-05–09, ID-12, ID-17, ID-23, ID-26–29)
- **Testing**: See `12-deno/02-testing.md` for `Deno.test()` replacing Jest (ID-01, ID-06–08)
- **Task Runner**: See `12-deno/03-task-runner.md` for `deno task` replacing `npm run` (ID-01, ID-07)
- **Publishing**: See `12-deno/04-publishing.md` for JSR replacing npm (ID-03, ID-07)
- **Biome Setup**: See `13-biome/01-setup.md` for Biome replacing ESLint + Prettier (ID-01, ID-06, ID-16)

---

## External References

- [Deno — Node.js Compatibility](https://docs.deno.com/runtime/fundamentals/node/)
- [Deno — npm Specifiers](https://docs.deno.com/runtime/fundamentals/node/#using-npm-packages)
- [Deno — Configuration](https://docs.deno.com/runtime/fundamentals/configuration/)
- [JSR Registry](https://jsr.io/)
- *JavaScript: The Definitive Guide* (7th ed.) — David Flanagan (Node.js chapters)
