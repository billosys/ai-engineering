# Modernization Synthesis

Use this guide after the per-language audit reports exist. It preserves the
evidence-backed modernization contract from the original audit guide: synthesis
follows findings, not novelty.

For the audit map, load [`01-audit-scope-and-map.md`](./01-audit-scope-and-map.md).
For finding IDs and severity, load
[`02-findings-and-severity.md`](./02-findings-and-severity.md). For handoff
boundaries, load
[`05-audit-to-hardening-handoff.md`](./05-audit-to-hardening-handoff.md).

## Synthesis File

Write the modernization synthesis to:

```text
workbench/<DATE>-audit-modernization-synthesis.md
```

It comes after the per-language reports. It is not a substitute for evidence
and must cite the report finding IDs it relies on.

## Structure

1. **Executive summary** - what modernization pressure is real, what can wait,
   and what should not be changed until evidence improves.
2. **System themes** - recurring findings across files, packages, crates, apps,
   or languages. Distinguish isolated defects from architectural drift.
3. **Consolidation opportunities** - duplicated concepts, overlapping
   utilities, competing abstractions, shared schemas, repeated parser or
   protocol logic, copy-pasted tests, and places where one supported
   implementation should replace several local variants.
4. **Modernization moves** - ordered recommendations such as dependency
   replacement, API redesign, language-edition migration, build-system cleanup,
   test harness changes, error-model unification, or workspace restructuring.
   Each move cites audit findings and says whether it is safe as a local
   refactor, requires a compatibility layer, or needs an explicit behavior
   change.
5. **Defer / do not touch yet** - areas where modernization would be
   speculative, where public contracts are unclear, or where tests are too weak
   to support safe change.

## Evidence Rules

Modernization follows evidence. Do not start with the newest library, edition,
framework, or rewrite shape. Start with observed defects and structural
pressure, then recommend the smallest modernization move that resolves the real
problem while preserving supported behavior.

Every modernization move cites one or more finding IDs from the audit reports.
If a recommendation cannot cite a finding, it belongs in "defer / do not touch
yet" or in an open question, not in the ordered moves.

## Compatibility Classification

Classify each move:

- **Local refactor:** behavior is preserved and current tests should remain
  valid.
- **Compatibility layer required:** public behavior or storage/protocol shape
  must be bridged while the implementation changes.
- **Explicit behavior change:** the move changes a user-visible contract and
  needs operator or maintainer acceptance before implementation.

## Defer Aggressively

Defer modernization when:

- The public contract is unclear.
- Tests are too weak to protect the change.
- The change is mostly aesthetic.
- The new dependency or pattern would add more policy than it removes.
- The audit produced no concrete failure mode.

The synthesis should make modernization pressure legible without turning an
audit into a rewrite plan.
