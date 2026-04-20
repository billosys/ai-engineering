---
# === CORE IDENTIFICATION ===
concept: Permissions System
slug: deno-permissions-system

# === CLASSIFICATION ===
category: security
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/security.md"
chapter_number: null
pdf_page: null
section: "Permissions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno permissions"
  - "permission flags"
  - "allow flags"
  - "deny flags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-security-model
extends:
  - deno-security-model
related:
  - deno
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Deno permissions system?"
  - "How do I configure permissions for a Deno script?"
---

# Quick Definition
Deno's permissions system uses `--allow-*` and `--deny-*` command-line flags to grant or restrict access to specific system resources (files, network, environment, subprocesses, FFI, system info), with deny flags taking precedence over allow flags.

# Core Definition
The permissions system is the concrete mechanism that enforces Deno's security model. It provides granular control over what system resources a program can access through a set of command-line flags. Each resource category has both an allow flag and a deny flag, and deny flags always take precedence over allow flags. Permissions can be granted at invocation time via flags, during execution via interactive prompts (when running in a TTY), or stored in a `deno.json` configuration file.

The permission categories are:
- **File system**: `--allow-read` (`-R`), `--allow-write` (`-W`), with optional path restrictions
- **Network**: `--allow-net` (`-N`), with optional hostname/port restrictions
- **Environment variables**: `--allow-env` (`-E`), with optional variable name restrictions and wildcard support
- **System information**: `--allow-sys` (`-S`), with optional API name restrictions
- **Subprocesses**: `--allow-run`, with optional executable name restrictions
- **FFI**: `--allow-ffi`, with optional path restrictions
- **Web imports**: `--allow-import`, with optional host restrictions
- **All permissions**: `--allow-all` (`-A`), disables the sandbox entirely

# Prerequisites
- deno-security-model: Understanding of Deno's secure-by-default philosophy

# Key Properties
1. **Granular path/host scoping** -- Allow flags accept comma-separated lists of paths, hostnames, variable names, or program names
2. **Deny takes precedence** -- `--deny-*` flags override `--allow-*` flags for specific resources
3. **Runtime prompts** -- When running in a TTY without `--no-prompt`, Deno interactively asks for permissions
4. **Short flags** -- Common permissions have single-letter shortcuts: `-R` (read), `-W` (write), `-N` (net), `-E` (env), `-S` (sys)
5. **Audit logging** -- `DENO_AUDIT_PERMISSIONS` environment variable enables JSONL permission audit logs
6. **Configuration file support** -- Permissions can be stored in `deno.json`/`deno.jsonc`
7. **Permission broker** -- Advanced feature that delegates all permission decisions to an external process via `DENO_PERMISSION_BROKER_PATH`

# Construction / Recognition
```sh
# Allow reading from specific paths
deno run --allow-read=foo.txt,bar.txt script.ts

# Allow all network but deny specific domain
deno run --allow-net --deny-net=evil.com script.ts

# Allow environment variables matching a prefix
deno run --allow-env="AWS_*" script.ts

# Allow only specific subprocesses
deno run --allow-run="curl,whoami" script.ts

# Allow everything (disables sandbox)
deno run -A script.ts
```

# Context & Application
The permissions system is the primary interface through which developers interact with Deno's security model. It applies to every `deno run` invocation and determines what the program can do. In CI/production environments, permissions are typically specified as flags. In development, interactive prompts provide a convenient way to grant permissions as needed.

The `--allow-run` flag is particularly sensitive because spawned subprocesses run independently of the Deno sandbox -- granting `--allow-run` essentially invalidates the security sandbox for those subprocesses. Similarly, `--allow-ffi` allows loading dynamic libraries that bypass the sandbox.

# Examples
From runtime/fundamentals/security.md:
- File access: `deno run --allow-read=/etc --deny-read=/etc/hosts script.ts` -- allows reading `/etc` but denies reading `/etc/hosts`
- Network access: `deno run --allow-net=github.com,jsr.io script.ts` -- allows network to specific hosts only
- Environment: `deno run --allow-env --deny-env=AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY script.ts` -- allows all env vars except AWS credentials

# Relationships
## Builds Upon
- deno-security-model (the permissions system implements the security model)

## Enables
- Secure execution of third-party code
- Granular access control for production deployments

## Related
- deno (the runtime that enforces permissions)

# Common Errors
1. Using `--allow-all` in production -- defeats the purpose of the security model
2. Granting `--allow-run=deno` -- allows spawning a new Deno process with full permissions, effectively bypassing the sandbox
3. Not realizing `--allow-run` subprocesses escape the sandbox -- child processes have their own unrestricted system access

# Common Confusions
1. **Allow vs. deny precedence** -- Deny flags always take precedence over allow flags, not the other way around
2. **Symlink permissions** -- Permissions are checked based on the symlink's location, not its target; but symlinks to sensitive paths like `/proc` require `--allow-all`
3. **Static vs. dynamic imports** -- Static module graph imports do not require `--allow-read`; dynamic imports do

# Source Reference
- runtime/fundamentals/security.md, section "Permissions": Complete description of all permission flags, scoping, and runtime behavior

# Verification Notes
- High confidence: Every permission flag and its behavior is explicitly documented with examples
- Deny-takes-precedence rule is explicitly stated in the source
