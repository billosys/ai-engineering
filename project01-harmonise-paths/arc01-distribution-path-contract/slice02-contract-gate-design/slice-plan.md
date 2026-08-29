# Slice 02: Contract Gate Design

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
slice: slice02-contract-gate-design
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Capability Statement

This slice turns the verified Slice 01 package path contract into an
implementation-ready validation design for the packaging workflow.

By the end of the slice, Arc 01 should have a design artifact that a later
implementation slice can follow without rediscovering path semantics: what is
scanned, how Markdown references are parsed, which classifications fail or
warn, where exceptions live, how Make invokes the gate, and what remains out
of scope until later arcs.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/2026.08.29-package-path-audit.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`

## Deliverables

Create a slice-local design report:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md`

The report must include:

- the final validation surface: generated zips, staging directories, or both;
- the chosen Makefile target and checker entry point names;
- the package-path classification policy for all Slice 01 classes;
- the hard-fail, warning, pass, and explicit-exception behavior;
- Markdown parsing requirements that avoid the Slice 01 false-positive trap;
- an allowlist or exception schema, including its proposed repository path;
- guidance on source edits versus staging-time transforms;
- package-layout-change boundaries;
- CCDP/protocol reservation or deferral language;
- Slice 03 implementation scope and non-goals.

Update this slice's `ledger.md` with attested evidence, then write:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/closing-report.md`

## Scope

In scope:

- design only, based on the verified Slice 01 audit and CDC verification;
- concrete Make/Bash-friendly integration requirements;
- naming the checker script or scripts and Make target;
- choosing whether a small parser script is acceptable where Bash would be too
  brittle;
- a repeatable exception/allowlist contract;
- an implementation handoff for Slice 03.

Out of scope:

- implementing the checker;
- changing `Makefile`;
- editing package source Markdown;
- changing mature Rust, Go, Erlang, C++, JavaScript/Deno, Tailwind, Cobalt, or
  visual-design guide prose;
- adding a CCDP package target;
- changing the zip layout beyond design recommendations.

## Design Constraints

The design must preserve both primary use cases:

- source-clone users can keep using repo-root-oriented material for project
  management, SDLC planning/execution, language-specific best practices, and
  CCDP protocol processing;
- zip/unzipped users see references that resolve from the bundle context or
  are explicitly marked as repo-only/provenance/example/external.

The Slice 01 CDC verification adds two non-negotiable constraints:

- do not turn the temporary broad regex scanner into the final hard-fail gate;
- do not report skipped or filtered classes as if they were emitted by the same
  evidence stream.

## Suggested Direction

Prefer a Make-facing target named `check-package-paths` or similarly explicit,
with implementation delegated to a checked-in script if structured Markdown and
zip inspection make pure shell brittle.

The design should be friendly to Make/Bash orchestration but honest about the
parser boundary. A small checked-in Python validator may be a better
implementation detail than a shell regex gate, as long as Make owns the target
and the report format remains simple enough for humans and LLMs to consume.

The likely policy shape is:

- unresolved bundled references become hard failures once harmonisation lands;
- known current misses may start as warnings or allowlisted transitional rows
  if Slice 03 runs before Arc 02 rewrites;
- repo-only/provenance and example-project references pass only with explicit
  classification and reason;
- external URLs are skipped for package path resolution and never require
  network access;
- parser false positives should be prevented by Markdown structure, not hidden
  through a broad allowlist.

## Close Conditions

This slice closes when the design report exists, every ledger row is marked
done with evidence, the close report walks every row, and the Bubble-up to Arc
01 states whether the arc is ready for a gate implementation slice or needs a
contract revision first.
