# Deno Task Runner

The commands you type every day and how to wire them together: `deno task` definitions, `--watch` mode, common task recipes, CLI command reference, task composition, and CI workflows. This is a practical, recipe-oriented chapter — less "why" and more "here's the command." Grounded in Deno documentation concept cards.

Target environment: **Deno**, **Biome** for linting/formatting, **ESM-only**, **no TypeScript** (plain JS with JSDoc where needed). No `npm run`, no Makefile.

---

## ID-01: Define Tasks in `deno.json` — Replaces `npm run`

**Strength**: MUST

**Summary**: Tasks are defined in the `tasks` field of `deno.json`. Run them with `deno task <name>`.

```jsonc
// deno.json
{
  "tasks": {
    "dev": "deno run --watch --allow-net --allow-read main.js",
    "start": "deno run --allow-net=:8080 --allow-read=./static main.js",
    "test": "deno test --allow-all",
    "check": "biome ci && deno check **/*.js && deno test --allow-all",
    "build": "deno compile -o dist/myapp --allow-net --allow-read main.js"
  }
}
```

```sh
# Run a task
deno task dev

# List all available tasks
deno task
```

**Rationale**: `deno task` is the direct replacement for `npm run`. Tasks are shell command strings — they can invoke any program, not just `deno` commands. No `package.json`, no `node_modules`, no `npx` (Deno task docs).

**See also**: `10-project-structure.md` ID-15

---

## ID-02: `deno task` With No Arguments Lists Available Tasks

**Strength**: SHOULD

**Summary**: Running `deno task` with no arguments prints all defined tasks — a quick reference without opening `deno.json`.

```sh
$ deno task
Available tasks:
  dev    deno run --watch --allow-net --allow-read main.js
  start  deno run --allow-net=:8080 --allow-read=./static main.js
  test   deno test --allow-all
  check  biome ci && deno check **/*.js && deno test --allow-all
  build  deno compile -o dist/myapp --allow-net --allow-read main.js
```

**Rationale**: Self-documenting tasks. New team members can discover the available workflows without reading config files.

---

## ID-03: Task Shell — Cross-Platform Built-In Shell

**Strength**: SHOULD

**Summary**: `deno task` uses a built-in cross-platform shell, not the system shell. Supported operators work identically on macOS, Linux, and Windows.

**Supported operators**:

| Operator | Meaning | Example |
|----------|---------|---------|
| `&&` | Sequential, stop on error | `deno lint && deno test` |
| `x \|\| y` | Fallback on error | Run y if x fails |
| `;` | Sequential, always continue | `cmd1 ; cmd2` |
| `x \| y` | Pipe stdout | Pipe x's output to y |
| `&` | Background execution | `cmd1 & cmd2` |
| `>` / `>>` | Redirect stdout | `deno coverage --lcov > cov.lcov` |
| `2>` | Redirect stderr | `cmd 2> errors.log` |
| `$VAR` | Environment variable expansion | `echo $HOME` |
| `$(cmd)` | Command substitution | `echo $(date)` |
| `*.js` | Glob expansion | `deno check **/*.js` |

**What does NOT work** (Bash-specific features not supported):
- `[[ ]]` conditionals, `source`, heredocs, process substitution `<()`
- Brace expansion `{a,b,c}`
- Shell functions and `alias`
- Windows `cmd.exe` syntax (`%VAR%`, `set`, `if exist`)

**Escape hatch**: For complex shell scripting, invoke the system shell explicitly: `"task": "bash -c 'your bash script here'"`.

**Rationale**: The cross-platform shell ensures tasks work identically on all OSes — no more "works on my Mac but fails on CI Linux." The trade-off is a subset of POSIX shell features (Deno task docs).

---

## ID-04: Passing Arguments to Tasks

**Strength**: SHOULD

**Summary**: Arguments after `deno task <name>` are appended to the task command string.

```sh
# deno.json: "dev": "deno run --watch --allow-net main.js"
deno task dev --port 8080
# Executes: deno run --watch --allow-net main.js --port 8080
# --port 8080 becomes part of Deno.args

# Flag ordering matters for deno run
deno task start -- --verbose
# The -- separates deno flags from script arguments
```

**Rationale**: Arguments are positionally appended. For `deno run`, permission flags must appear before the script name — arguments after the script name go to `Deno.args`, not to Deno itself.

---

## ID-05: `dev` Task — `--watch` for Live Reload

**Strength**: SHOULD

**Summary**: `--watch` restarts the process automatically when files change. Essential for development.

```jsonc
{
  "tasks": {
    "dev": "deno run --watch --allow-net --allow-read main.js",
    "dev:exclude": "deno run --watch --watch-exclude='*.log,tmp/' --allow-net main.js"
  }
}
```

```sh
deno task dev
# Watcher File change detected! Restarting!
```

**Key flags**:
- `--watch` — restart on file changes
- `--watch-hmr` — attempt hot module replacement instead of full restart (dispatches `hmr` CustomEvent)
- `--watch-exclude=<glob>` — exclude paths/patterns from triggering restart

**Rationale**: `--watch` eliminates the manual restart cycle. Exclude log files, temp directories, and generated output to avoid restart loops (Deno run docs).

---

## ID-06: `test` Task — `deno test` with Appropriate Permissions

**Strength**: SHOULD

**Summary**: Define a test task with the permissions your test suite needs.

```jsonc
{
  "tasks": {
    "test": "deno test --allow-all",
    "test:watch": "deno test --allow-all --watch",
    "test:coverage": "deno test --allow-all --coverage=cov/ && deno coverage --lcov cov/ > cov.lcov",
    "test:ci": "deno test --allow-all --parallel --reporter=junit > results.xml"
  }
}
```

**Rationale**: Tests commonly use `--allow-all` because test suites touch files, network, and env vars across many tests. This is acceptable since tests are not production code. For tighter control, use per-test `permissions` to restrict access within individual tests — see `12-deno/02-testing.md` ID-03. For production `run` tasks, always use granular permissions (ID-01). `--watch` for continuous testing during development; `--coverage` for CI (Deno test runner docs).

**See also**: `12-deno/02-testing.md` ID-01, ID-14, ID-21

---

## ID-07: `check` Task — The Combined Quality Gate

**Strength**: SHOULD

**Summary**: A single task that runs lint, format check, type check, and tests. Run this before committing.

```jsonc
{
  "tasks": {
    "check": "biome ci && deno check **/*.js && deno test --allow-all"
  }
}
```

```sh
# One command to verify everything
deno task check
```

**What each step does**:
1. `biome ci` — lint + format check in one pass (exits nonzero on violations)
2. `deno check **/*.js` — type-check all JS files with JSDoc annotations
3. `deno test --allow-all` — run the full test suite

**Using `&&`** ensures the pipeline stops at the first failure — no point running tests if lint fails.

**If using Deno's built-in lint/fmt instead of Biome**:
```jsonc
{
  "tasks": {
    "check": "deno fmt --check && deno lint && deno check **/*.js && deno test --allow-all"
  }
}
```

**Rationale**: This is the single most valuable task in any project. It answers "is the code ready to commit?" in one command. Use it as a pre-commit check, a CI entry point, or a habit before pushing.

**See also**: `12-deno/01-runtime-basics.md` ID-20, `13-biome/01-setup.md`

---

## ID-08: `lint` and `fmt` Tasks — Biome Integration

**Strength**: SHOULD

**Summary**: Since the project uses Biome, lint and format tasks should call Biome. Show both Biome and Deno options.

```jsonc
{
  "tasks": {
    // Biome (project preference)
    "lint": "biome check ./",
    "fmt": "biome format --write ./",
    "lint:fix": "biome check --write ./",

    // Deno built-in (alternative if not using Biome)
    "lint:deno": "deno lint",
    "fmt:deno": "deno fmt",
    "fmt:check:deno": "deno fmt --check"
  }
}
```

**Biome commands**:
- `biome check` — lint + format check combined (the default quality gate)
- `biome ci` — same as `check` but optimized for CI (no fixes, formatter errors)
- `biome check --write` — lint with auto-fix + format
- `biome format --write` — format only

**Rationale**: Biome combines linting and formatting in one tool and is significantly faster than Prettier (an order of magnitude in most benchmarks). The project uses Biome via `biome.json` — `deno lint`/`deno fmt` sections in `deno.json` should be omitted to avoid confusion. See `13-biome/01-setup.md` for Biome configuration.

---

## ID-09: `build` Task — `deno compile` for Production

**Strength**: CONSIDER

**Summary**: Compile the application into a standalone binary with embedded permissions.

```jsonc
{
  "tasks": {
    "build": "deno compile -o dist/myapp --allow-net=:8080 --allow-read=./static main.js",
    "build:linux": "deno compile --target x86_64-unknown-linux-gnu -o dist/myapp main.js"
  }
}
```

**Rationale**: `deno compile` produces a single binary that runs without Deno installed. Permissions are baked in at compile time. Cross-compilation targets let you build for different platforms from one machine (Deno compile docs).

**See also**: `12-deno/01-runtime-basics.md` ID-24

---

## ID-10: `deno test --watch` for Continuous Testing

**Strength**: SHOULD

**Summary**: `--watch` reruns tests automatically when files change.

```jsonc
{
  "tasks": {
    "test:watch": "deno test --allow-all --watch"
  }
}
```

```sh
deno task test:watch
# Tests rerun on every file save
```

**Rationale**: Continuous testing provides immediate feedback during development. Pair with `--fail-fast` to stop on the first failure: `deno test --allow-all --watch --fail-fast` (Deno test runner docs).

---

## ID-11: `deno run` — Execute a Script with Permissions

**Strength**: MUST

**Summary**: `deno run` is the primary execution command. Permission flags go before the script name.

```sh
# Basic execution
deno run main.js

# With permissions (flags BEFORE the script name)
deno run --allow-net --allow-read main.js

# With type checking
deno run --check main.js

# Watch mode
deno run --watch --allow-net main.js

# Bypass module cache
deno run --reload main.js
```

**Flag ordering rule**: Everything before the script name is a Deno flag. Everything after is passed to the script as `Deno.args`.

```sh
# CORRECT: --allow-net is a Deno flag
deno run --allow-net main.js --port 8080

# WRONG: --allow-net goes to Deno.args, not to the runtime
deno run main.js --allow-net --port 8080
```

**Rationale**: Flag ordering is the most common mistake when running Deno scripts. Permission flags after the script name are silently ignored by the runtime and passed as arguments to the script (Deno run docs).

---

## ID-12: `deno fmt` and `deno lint` — Built-In Formatting and Linting

**Strength**: SHOULD

**Summary**: Deno includes a formatter (dprint-based) and linter (ESLint-derived). Use them if not using Biome.

```sh
# Format all files
deno fmt

# Check formatting without modifying (CI mode)
deno fmt --check

# Lint all files
deno lint

# Format/lint specific directories
deno fmt src/
deno lint src/
```

**Note**: If the project uses **Biome** for linting and formatting (as this project does), omit `lint` and `fmt` from `deno.json` and use `biome check` / `biome format` tasks instead (ID-08). `deno fmt` and `deno lint` are still useful as fallbacks or for projects that don't use Biome.

**Rationale**: `deno fmt --check` exits nonzero if any file is unformatted — the correct CI gate. `deno lint` uses ESLint-derived recommended rules. Both are configured in `deno.json` (Deno linter docs; Deno formatter docs).

**See also**: `12-deno/01-runtime-basics.md` ID-13

---

## ID-13: `deno check` — Type-Check Without Executing

**Strength**: SHOULD

**Summary**: Separate type-checking from execution. Use `deno check` in CI as a gate.

```sh
# Type-check a specific entry point
deno check main.js

# Type-check all JS files (with checkJs enabled in deno.json)
deno check **/*.js

# Type-check including remote/npm modules
deno check --all main.js
```

```jsonc
{
  "tasks": {
    "typecheck": "deno check **/*.js"
  }
}
```

**Rationale**: `deno run` skips type-checking for performance. `deno check` catches type errors before deployment without executing the code. Run it in CI alongside lint and test (Deno TypeScript docs).

**See also**: `12-deno/01-runtime-basics.md` ID-20, `05-type-discipline.md` ID-20

---

## ID-14: `deno info` — Dependency Tree Inspection

**Strength**: CONSIDER

**Summary**: Inspect a module's full dependency graph without executing it.

```sh
# Show dependency tree for a local file
deno info main.js

# Inspect a remote module
deno info jsr:@std/assert

# JSON output for tooling
deno info --json main.js
```

**Rationale**: `deno info` shows every module in the dependency graph with its URL, local cache path, and module type. Useful for auditing dependencies, debugging resolution issues, and understanding what a script pulls in (Deno CLI docs).

---

## ID-15: `deno install` — Two Distinct Uses

**Strength**: CONSIDER

**Summary**: `deno install` has two different modes: dependency caching and global script installation.

**Use 1: Dependency caching** (project-level)

```sh
# Pre-cache all dependencies for an entry point (no execution)
deno install --entrypoint main.js

# Install dependencies listed in deno.json
deno install
```

**Docker pattern**: Copy `deno.json` and `deno.lock` first, run `deno install --entrypoint main.js` to cache deps as a Docker layer, then copy source — dep caching survives source changes.

**Use 2: Global script installation** (CLI tools)

```sh
# Install a remote script as a global CLI command
deno install -g -n serve https://deno.land/std/http/file_server.ts

# The script is now available as: serve
```

Permission flags passed at install time (`--allow-net`, etc.) are embedded into the generated wrapper command.

**Rationale**: These are two unrelated operations sharing a command name. Use 1 (`deno install --entrypoint`) pre-populates the module cache for faster startup and Docker layer caching. Use 2 (`deno install -g`) creates a global executable wrapper (Deno install docs; Deno Docker docs).

---

## ID-16: Task Chaining — `&&` for Sequential, `&` for Parallel

**Strength**: SHOULD

**Summary**: Chain tasks with shell operators for sequential or parallel execution.

```jsonc
{
  "tasks": {
    // Sequential — stops on first failure
    "check": "biome ci && deno check **/*.js && deno test --allow-all",

    // Sequential — always runs all (use ; instead of &&)
    "clean-and-test": "rm -rf cov/ ; deno test --allow-all --coverage=cov/",

    // Parallel — both run simultaneously
    "dev:all": "deno task dev & deno task test:watch"
  }
}
```

| Operator | Behavior |
|----------|----------|
| `&&` | Run next only if previous succeeded (exit 0) |
| `x \|\| y` | Run y only if x failed (non-zero exit) |
| `;` | Always run next, regardless of previous exit code |
| `&` | Run in background (both commands execute in parallel) |

**Rationale**: `&&` is the correct operator for quality gates — if lint fails, don't bother type-checking or testing. `&` is useful for running a dev server and a test watcher simultaneously (Deno task docs).

---

## ID-17: Environment Variables in Tasks

**Strength**: SHOULD

**Summary**: Set environment variables inline in task definitions using `VAR=value cmd` syntax.

```jsonc
{
  "tasks": {
    "start:prod": "PORT=8080 LOG_LEVEL=info deno run --allow-net --allow-env main.js",
    "test:verbose": "DEBUG=true deno test --allow-all"
  }
}
```

**Rationale**: Inline env vars are scoped to the command — they don't persist beyond the task. This is cleaner than `export` (which modifies the shell session) and works cross-platform in Deno's built-in shell (Deno task docs).

---

## ID-18: Composing Tasks — Calling Other Tasks

**Strength**: CONSIDER

**Summary**: Tasks can call `deno task` within their definition to compose from other tasks.

```jsonc
{
  "tasks": {
    "test": "deno test --allow-all",
    "typecheck": "deno check **/*.js",
    "lint": "biome ci",
    "check": "deno task lint && deno task typecheck && deno task test"
  }
}
```

**Rationale**: Composing from named tasks keeps each task focused and reusable. The `check` task chains three independent tasks — each can also be run individually. The trade-off is subprocess overhead: each `deno task` invocation spawns a child process. For CI where speed matters, the inline version (ID-07: `"check": "biome ci && deno check **/*.js && deno test --allow-all"`) is faster because it avoids three extra process spawns (Deno task docs).

---

## ID-19: CI Task Recipe — Single Entry Point

**Strength**: SHOULD

**Summary**: Define a `ci` task that runs the full quality pipeline. Use it as the single CI step.

```jsonc
{
  "tasks": {
    "ci": "biome ci && deno check **/*.js && deno test --allow-all --parallel --coverage=cov/"
  }
}
```

**GitHub Actions example**:
```yaml
- uses: denoland/setup-deno@v2
  with:
    deno-version: v2.x
    cache: true
- run: deno task ci
- run: deno coverage --lcov cov/ > cov.lcov
  if: matrix.os == 'ubuntu-latest'
```

**Rationale**: A single `deno task ci` keeps CI pipeline YAML minimal and ensures local and CI environments run identical checks. Dependency caching (`cache: true`) is keyed by `deno.lock` (Deno CI docs).

---

## ID-20: Workspace Tasks — Scoping to Members

**Strength**: CONSIDER

**Summary**: In workspaces, run tasks scoped to a specific member with `--cwd`.

```sh
# Run a task in a specific workspace member
deno task --cwd=packages/core build

# Commands run across all members from the root
deno test        # discovers tests in all workspace members
deno lint        # lints all members
deno fmt         # formats all members
```

**Rationale**: Root-level commands (`deno test`, `deno lint`, `deno fmt`) automatically traverse all workspace members. Use `--cwd` to target a specific member for member-specific tasks. Member task configurations take priority over root (Deno workspace docs).

**See also**: `10-project-structure.md` ID-25

---

## ID-21: `deno eval` — Quick One-Liners

**Strength**: CONSIDER

**Summary**: Execute inline JavaScript without a file. Useful for quick checks and CI assertions.

```sh
# Quick one-liner
deno eval 'console.log(2 ** 53)'

# Health check in Docker
deno eval "try { await fetch('http://localhost:8000/health'); } catch { Deno.exit(1); }"

# Verify feature availability
deno eval "[1,2,3].values().map(x=>x*2).toArray()"
```

**Rationale**: `deno eval` runs a snippet without creating a file. Useful for Docker health checks, CI assertions, and verifying API availability. Does not type-check by default (Deno eval docs).

---

## ID-22: `--watch-exclude` — Prevent Restart Loops

**Strength**: CONSIDER

**Summary**: Without `--watch-exclude`, generated files trigger an infinite restart loop.

```sh
# The problem: server writes to access.log → watcher detects change → restart →
# server writes to access.log again → watcher detects change → restart → ...

# Bad — no exclusions, restart loop if server generates output files
deno run --watch --allow-net --allow-write server.js

# Good — exclude generated files
deno run --watch --watch-exclude='*.log,tmp/,cov/,dist/' --allow-net --allow-write server.js
```

**Common exclusions**: Log files (`*.log`), temp directories (`tmp/`), coverage output (`cov/`), build output (`dist/`), and `.git/`.

**Rationale**: `--watch` monitors all files in the project. If the running program writes files (logs, temp files, build output), those writes trigger a restart, which writes again — an infinite loop. `--watch-exclude` accepts glob patterns to break the cycle. See also ID-05 which shows `--watch-exclude` in a task definition (Deno run docs).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Tasks in `deno.json` | MUST | Replaces `npm run` / `package.json` scripts |
| 02 | `deno task` lists tasks | SHOULD | Self-documenting; no config file needed |
| 03 | Cross-platform shell | SHOULD | Built-in; no Bash/cmd dependency |
| 04 | Argument passing | SHOULD | Appended to command; flag order matters |
| 05 | `dev` with `--watch` | SHOULD | Auto-restart on file changes |
| 06 | `test` task | SHOULD | `--watch` for dev; `--coverage` for CI |
| 07 | `check` — quality gate | SHOULD | lint + fmt + typecheck + test in one command |
| 08 | Biome integration | SHOULD | `biome ci` replaces `deno lint` + `deno fmt` |
| 09 | `build` with `deno compile` | CONSIDER | Standalone binary; embedded permissions |
| 10 | `deno test --watch` | SHOULD | Continuous testing during development |
| 11 | `deno run` flag ordering | MUST | Permissions before script; args after |
| 12 | `deno fmt` / `deno lint` | SHOULD | Built-in; use if not using Biome |
| 13 | `deno check` | SHOULD | Type-check without executing; CI gate |
| 14 | `deno info` | CONSIDER | Dependency tree inspection |
| 15 | `deno install` | CONSIDER | Pre-cache deps; global script install |
| 16 | `&&` / `;` / `&` chaining | SHOULD | Sequential-stop / always / parallel |
| 17 | Inline env vars | SHOULD | `VAR=value cmd`; scoped to command |
| 18 | Composing tasks | CONSIDER | `deno task` inside a task |
| 19 | CI single entry point | SHOULD | `deno task ci`; minimal pipeline YAML |
| 20 | Workspace `--cwd` | CONSIDER | Scope tasks to a specific member |
| 21 | `deno eval` | CONSIDER | One-liners; Docker health checks |
| 22 | `--watch-exclude` | CONSIDER | Prevent restart loops from generated files |

### CLI Quick Reference

| Command | Purpose |
|---------|---------|
| `deno run main.js` | Execute a script |
| `deno run --watch main.js` | Execute with live reload |
| `deno test` | Run tests |
| `deno test --watch` | Continuous testing |
| `deno check main.js` | Type-check without executing |
| `deno fmt` | Format code |
| `deno fmt --check` | Verify formatting (CI) |
| `deno lint` | Lint code |
| `deno compile -o app main.js` | Build standalone binary |
| `deno info main.js` | Show dependency tree |
| `deno install` | Cache dependencies |
| `deno eval 'code'` | Run inline code |
| `deno task <name>` | Run a defined task |
| `deno task` | List all tasks |

---

## Related Guidelines

- **Project Structure**: See `10-project-structure.md` for `deno.json` placement (ID-15), import maps (ID-16), workspaces (ID-25)
- **Type Discipline**: See `05-type-discipline.md` for `deno check` integration (ID-20)
- **Runtime Basics**: See `12-deno/01-runtime-basics.md` for permissions (ID-01–04), `deno.json` config (ID-13), `deno compile` (ID-24)
- **Testing**: See `12-deno/02-testing.md` for `Deno.test()` API (ID-01), assertions (ID-06–11), coverage (ID-21)
- **Publishing**: See `12-deno/04-publishing.md` for `deno publish` workflow
- **Biome**: See `13-biome/01-setup.md` for Biome configuration (lint rules, format options)

---

## External References

- [Deno — Task Runner](https://docs.deno.com/runtime/fundamentals/configuration/#tasks)
- [Deno — CLI Reference](https://docs.deno.com/runtime/reference/cli/)
- [Deno — Continuous Integration](https://docs.deno.com/runtime/fundamentals/testing/#continuous-integration)
- [Deno — Docker](https://docs.deno.com/runtime/tutorials/docker/)
