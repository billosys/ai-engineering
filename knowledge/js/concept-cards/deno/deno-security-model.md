---
# === CORE IDENTIFICATION ===
concept: Security Model
slug: deno-security-model

# === CLASSIFICATION ===
category: security
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/fundamentals/security.md"
chapter_number: null
pdf_page: null
section: "Key Principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno security model"
  - "secure by default"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-permissions-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Deno's security model?"
  - "What distinguishes Deno from Node.js?"
---

# Quick Definition
Deno is secure by default: programs have no access to sensitive APIs (file system, network, environment) unless explicitly granted, enforcing a principle of least privilege with no silent escalation.

# Core Definition
Deno's security model is built around the principle that code should have no access to sensitive system APIs by default. Unlike Node.js, where dependencies are automatically granted full access to all system I/O, Deno requires explicit permission grants for file system access, network connectivity, environment variables, subprocess spawning, and FFI. The model is enforced by the Deno runtime itself and is not dependent on the underlying operating system.

The security model rests on six key principles:

1. **No access to I/O by default** -- Code cannot read/write files, make network requests, access environment variables, or spawn subprocesses without explicit permission.
2. **No limits on code execution at the same privilege level** -- Code can use `eval`, `new Function`, dynamic imports, and web workers to execute arbitrary code at the same privilege level.
3. **Multiple invocations can share data** -- Through built-in caching and KV storage APIs, but different applications cannot see each other's data.
4. **All code on the same thread shares the same privilege level** -- It is not possible for different modules to have different privilege levels within the same thread.
5. **No privilege escalation without user consent** -- Code cannot escalate its privileges without the user agreeing via interactive prompt or invocation-time flag.
6. **Static module graph imports are unrestricted** -- Files in the initial static module graph can be imported without read permissions; dynamic imports require permissions.

# Prerequisites
- deno: Understanding of Deno as a runtime

# Key Properties
1. **No I/O by default** -- File system, network, environment, and subprocess access are all denied unless explicitly allowed
2. **Runtime enforcement** -- The security model is enforced by the Deno runtime, not by the operating system
3. **Same-thread privilege sharing** -- All code on one thread shares the same permissions; per-module permissions are not possible
4. **No silent escalation** -- Privileges can only increase through explicit user consent (flags or interactive prompts)
5. **Static imports unrestricted** -- The initial static module graph can import local files freely; dynamic imports require read permissions
6. **Major difference from Node.js** -- Node.js grants full system access to all dependencies by default

# Construction / Recognition
- Run code with no permissions: `deno run script.ts` (will be prompted or fail on I/O)
- Run code with all permissions disabled (equivalent to Node.js): `deno run -A script.ts`
- Deno's security is a runtime-level sandbox, not an OS-level sandbox

# Context & Application
The security model is the most fundamental architectural distinction between Deno and Node.js. It addresses the supply-chain security problem where npm dependencies can silently access the file system, network, and environment. The model is designed to be simple enough to understand while providing meaningful protection against malicious or compromised dependencies.

For running completely untrusted code, the documentation recommends layering Deno's permissions with OS-level sandboxing (chroot, cgroups, seccomp) and virtualization (gVisor, Firecracker).

# Examples
From runtime/fundamentals/security.md:
- "Unless you specifically enable it, a program run with Deno has no access to sensitive APIs, such as file system access, network connectivity, or environment access."
- "This is a major difference from Node, where dependencies are automatically granted full access to all system I/O, potentially introducing hidden vulnerabilities into your project."

# Relationships
## Builds Upon
- deno (the security model is a core design decision of the runtime)

## Enables
- deno-permissions-system (the concrete mechanism for granting/denying access)

## Related
- deno-architecture (ops enforce the permission boundary)

## Contrasts With
- Node.js security model (grants full system access to all code by default)

# Common Errors
1. Using `--allow-all` / `-A` carelessly -- this disables the security sandbox entirely and provides the same security as Node.js (i.e., none)
2. Granting `--allow-run` broadly -- spawned subprocesses run outside the Deno sandbox and can access system resources regardless of parent permissions

# Common Confusions
1. **Per-module permissions** -- Deno does NOT support different permission levels for different modules on the same thread; all code shares the same privileges
2. **OS-level sandbox** -- Deno's security model is a runtime-level sandbox, not a kernel-level sandbox; for untrusted code, additional OS-level sandboxing is recommended

# Source Reference
- runtime/fundamentals/security.md: Full description of security model, key principles, and permission system

# Verification Notes
- High confidence: All six key principles are explicitly enumerated in the source
- Security model is the primary differentiator highlighted across Deno documentation
