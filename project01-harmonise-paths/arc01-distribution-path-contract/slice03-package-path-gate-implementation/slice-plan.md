# Slice 03: Package Path Gate Implementation

```yaml
project: project01-harmonise-paths
arc: arc01-distribution-path-contract
slice: slice03-package-path-gate-implementation
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
artifact-home: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/artifacts
```

## Capability Statement

This slice implements the accepted Slice 02 package path gate.

By the end of the slice, the source checkout should have a repeatable
Make-owned validation target that rebuilds or verifies the generated skill zip
set, scans Markdown references from the package context, classifies findings,
applies explicit exceptions, and reports hard failures separately from
warnings, explicit exceptions, skipped external URLs, and parser-suppressed
material.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/2026.08.29-package-path-audit.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice01-package-path-audit/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/2026.08.29-contract-gate-design.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice02-contract-gate-design/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/.gitignore`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/02-canonical-planning-worktree.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/03-planning-top-down.md`

## Artifact Home

Durable slice-produced evidence belongs here:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc01-distribution-path-contract/slice03-package-path-gate-implementation/artifacts/`

Expected artifacts include command transcripts or reports that prove the
current generated-zip scan, malformed exception handling, and parser fixture
behavior. Implementation source files, permanent test fixtures, and Makefile
changes belong in the implementation checkout, not in `artifacts/`.

## Scope

In scope:

- add `make check-package-paths`;
- add `scripts/check-package-paths` as a checked-in, executable, no-suffix
  Python 3 checker;
- add `package-path-exceptions.tsv` if current known misses need an explicit
  transitional policy for a non-breaking initial gate;
- scan generated zip archives named by `INSTALL_ZIPS`;
- parse Markdown links with enough structure to avoid the Slice 01 raw-regex
  false-positive pattern;
- classify emitted findings with the Slice 01 vocabulary plus hard
  `unclassified` internal failure behavior;
- return stable exit codes for pass, hard failures, and invocation/schema
  errors;
- create reproducible parser/schema/current-package evidence under the slice
  `artifacts/` directory;
- update this slice's ledger with attested evidence and write a close report.

Out of scope:

- harmonising the 145 current actionable misses except as needed to make the
  gate runnable under an explicit transitional policy;
- editing mature language guide prose;
- changing package layouts;
- adding CCDP package targets;
- checking URL liveness;
- turning the temporary Slice 01 scanner into a hard-fail raw regex gate;
- changing the collaboration-framework planning methodology.

## Implementation Notes

Follow the Slice 02 design unless implementation proves a concrete defect in
the design. If the design must change, record that explicitly in the close
report bubble-up rather than silently softening the ledger.

`scripts/check-package-paths` should use only the Python standard library if
feasible. If a third-party parser becomes necessary, treat that as a dependency
decision and explain it before closing the slice.

The Make target should be the public interface. Teach users and CI to run
`make check-package-paths`, not the script path directly, except for narrow
debugging or self-test evidence.

The checker should preserve source/package distinctions:

- generated zips are the authoritative surface;
- external URLs do not require network access;
- exceptions require a classification, disposition, reason, source, and
  expiration/re-entry condition;
- malformed exception data exits with code 2;
- hard unresolved package-path failures exit with code 1;
- warnings and explicit exceptions are visible in the summary.

## Verification Approach

The close set must include evidence for:

- `make check-package-paths` over the current generated zip set;
- parser behavior for Markdown links, images, reference definitions, anchors,
  code fences, conservative code spans, placeholders, and external URLs;
- malformed exception file handling;
- stable report buckets and exit codes;
- artifact placement under this slice's `artifacts/` directory;
- implementation diff scope.

## Close Conditions

This slice closes when the implementation diff is complete, the package path
gate runs repeatably, all ledger rows are marked done with attested evidence,
durable evidence artifacts live under `artifacts/`, and the closing report
walks every row with Bubble-up to Arc 01.
