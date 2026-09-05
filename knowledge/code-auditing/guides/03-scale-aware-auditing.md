# Scale-Aware Auditing

Use this guide to keep a code audit from collapsing into whichever files fit in
context. It preserves the original all-scale review contract and the
cross-language hunt list.

For setup and source mapping, load
[`01-audit-scope-and-map.md`](./01-audit-scope-and-map.md). For findings and
severity, load [`02-findings-and-severity.md`](./02-findings-and-severity.md).

## Scope

Per language, review all source files in idiomatic locations for that language:
source tree, test modules, and integration tests. Skip only generated,
vendored, dependency, and build-output trees identified in the audit map.

Every scale does not need the same number of findings, but every scale must be
examined. Treat the codebase as if a senior reviewer in that language will ship
it to users next week.

## Required Scales

Review each audited language at these scales:

1. **Line / expression / function** - correctness, soundness, lifetimes,
   ownership, nullability, error propagation, panic/throw behavior, input
   validation, resource management, and local idiom.
2. **File / module** - cohesive responsibilities, explicit invariants,
   consistent names, meaningful tests, and private helpers that do not leak
   architectural decisions.
3. **Logical unit** - neighboring files that implement one concept: submodule,
   feature folder, parser phase, CLI surface, protocol handler, persistence
   layer, renderer, or equivalent. Check shared vocabulary, error model,
   dependency posture, and abstraction level.
4. **Package / crate / library / target** - public API design, dependency
   direction, feature flags, build targets, binary/library split, test
   boundaries, integration points, and coherent reason to exist.
5. **Application / service / executable** - startup/shutdown behavior,
   configuration, observability, process contracts, exit/status behavior,
   stdin/stdout/stderr semantics, persistence, upgrades, and user-facing
   failure modes.
6. **Whole codebase** - architectural through-line, naming and layout
   coherence, duplicate concepts, scattered policy, inconsistent abstractions,
   test pyramid shape, CI coverage, release posture, and modernization pressure.
7. **Workspace / monorepo / system-of-systems**, when present - shared crates
   or packages, internal dependency graph, versioning and feature compatibility,
   shared schemas, repo-wide tooling, ownership boundaries, and whether local
   conventions scale across members.

## Scale Coverage Evidence

Each per-language report must include a scale coverage section. It is not
filler; it is the reviewer showing that the audit climbed the ladder.

If a scale is absent, say so. If a scale cannot be assessed because repository
structure or documentation is missing, record that as an architecture or
coherence issue.

## Cross-Language Hunt List

Apply these checks to every audited language, adapting the local syntax and
runtime model:

- Silently dropped errors: swallowed results/exceptions, catch blocks that log
  and continue, missing propagation, `.unwrap()` / `.expect()` / non-null
  assertions on user-reachable library paths.
- Panics or exceptions on code paths a library caller can hit that should be
  recoverable errors.
- Test doubles that diverge from production code paths and hide integration
  bugs.
- Wildcard or catch-all patterns that suppress compile-time or lint-time
  exhaustiveness checks.
- Assertions that accept ranges where exact values are computable.
- Shared mutable state accessed without the synchronization required by the
  language's concurrency model.
- Resource leaks: unclosed handles, listeners not removed, timers not cleared,
  connections not released on error paths.
- Untrusted input reaching trusted code without validation, canonicalization, or
  escaping.
- Implicit assumptions about time, locale, encoding, file-system case
  sensitivity, or line endings.
- Missing or misconfigured CI gates that would have caught the issue.
- Inconsistent naming, layering, logging, error handling, configuration,
  serialization, or dependency direction across files that implement the same
  concept.
- Two or more local abstractions solving the same problem without a documented
  reason for coexistence.
- Policy scattered through call sites instead of held in one tested boundary.
- Public entrypoints whose behavior is not exercised through the same boundary
  real users or supervised processes use.
- Workspace or monorepo members that silently diverge in toolchain, edition,
  dependency policy, CI gates, release assumptions, or shared schema versions.

## Per-Language Hunt Lists

For each language, derive the hunt list from the loaded skill and guides. The
anti-patterns guide, where one exists, is the canonical starting point. Work
through its items and grep the codebase for each.

Do not fall back to generic knowledge when a guide exists. The guide is the
contract.
