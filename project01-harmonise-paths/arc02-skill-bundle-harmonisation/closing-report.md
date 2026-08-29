# Arc 02 Closing Report: Skill Bundle Harmonisation

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
status: closed
closed-by: CDC
closed-on: 2026-08-29
composition-verdict: delivered
```

## Capability Restated

Arc 02 exists to burn down package-path warnings in generated skill bundles
while preserving source-clone usefulness and the Arc 01 path contract.

The arc applies the source/package path strategy selected in Arc 01: use source
edits where one spelling works in both contexts, use staging-time transforms
where source-root prose should remain source-rooted, avoid broad mature guide
rewrites, keep package layout expansion rare and justified, and leave CCDP
distribution work to Arc 03.

## Composition Verdict

Composition verdict: delivered.

The four slices compose into the promised capability:

- Slice 01 harmonised low-risk tooling/simple skill entrypoints.
- Slice 02 harmonised collaboration-framework package-internal links.
- Slice 03 added narrow mature-entrypoint staging transforms for Rust and
  JavaScript/Deno.
- Slice 04 retired stale Arc 02 transitional policy and left unresolved package
  usability issues visible as later maintenance/backlog.

The final arc-scale package-path demonstration scans all 12 generated skill
zips and exits 0 with 0 hard failures, 295 warnings, 3 explicit exceptions,
and no stale `after-arc02` transitional rows. The warning count is not zero by
design: remaining warnings are classified or visible later work rather than
ambiguous hard package failures.

## Slice Walk

### Slice 01: Tooling Entrypoint Links

Outcome: delivered and CDC-verified.

Evidence:

- `slice01-tooling-entrypoint-links/cdc-verification.md`

The slice burned targeted tooling/simple entrypoint `bundled-reference`
warnings from 20 to 0 and moved total package-path warnings from 426 to 406.

### Slice 02: Collaboration Framework Links

Outcome: delivered and CDC-verified.

Evidence:

- `slice02-collaboration-framework-links/cdc-verification.md`

The slice burned collaboration-framework package-internal
`bundled-reference` warnings from 4 to 0 and moved total package-path warnings
from 406 to 402 while preserving source/provenance examples as classified
warnings.

### Slice 03: Mature Entrypoint Staging Transforms

Outcome: delivered and CDC-verified.

Evidence:

- `slice03-mature-entrypoint-staging-transforms/cdc-verification.md`

The slice burned targeted mature entrypoint `bundled-reference` warnings from
107 to 0, moved total package-path warnings from 402 to 295, and kept mature
guide prose out of scope.

### Slice 04: Warning Policy Tightening

Outcome: delivered and CDC-verified.

Evidence:

- `slice04-warning-policy-tightening/cdc-verification.md`

The slice converted five stale `transitional-warning` / `after-arc02` rows into
ordinary visible warnings with concrete later-maintenance dispositions. No new
explicit exceptions or broad suppressions were added.

## Arc Ledger Walk

### A-1

Status: done.

Slice 01 has CDC verification at
`slice01-tooling-entrypoint-links/cdc-verification.md`.

### A-2

Status: done.

The package-path warning count for targeted tooling/simple entrypoints
decreased from 20 to 0 without introducing hard failures. The arc-scale final
gate still exits 0.

### A-3

Status: done.

Source-clone skill entrypoints remain usable after edits and transforms.
`make check-skills` passes, and the final package-path gate validates the
generated zips.

### A-4

Status: done.

No mature guide prose, CCDP package target, or package layout expansion landed
without later-slice approval. Slice 03 used a constrained entrypoint staging
helper instead of guide rewrites.

### A-5

Status: done.

Slice 02 was opened from Slice 01 findings and recorded in the arc-plan Version
History.

### A-6

Status: done.

Slice 02 has CDC verification at
`slice02-collaboration-framework-links/cdc-verification.md`.

### A-7

Status: done.

Collaboration-framework package-internal `bundled-reference` warnings moved
from 4 to 0 without introducing hard failures.

### A-8

Status: done.

Collaboration-framework methodology and provenance examples were not
mechanically rewritten into misleading package paths. Remaining framework
warnings stay visible or explicitly narrow.

### A-9

Status: done.

Slice 03 was opened from Slice 02 findings and recorded in the arc-plan Version
History.

### A-10

Status: done.

Slice 03 has CDC verification at
`slice03-mature-entrypoint-staging-transforms/cdc-verification.md`.

### A-11

Status: done.

Mature entrypoint `bundled-reference` warnings moved from 107 to 0 without
introducing hard failures.

### A-12

Status: done.

Mature language source entrypoints remain useful and broad mature guide prose
remains untouched. Implementation scope stayed in Makefile staging,
`scripts/stage-skill-entrypoint`, and exception retirement.

### A-13

Status: done.

Slice 04 was opened from Slice 03 findings and recorded in the arc-plan Version
History.

### A-14

Status: done.

Slice 04 has CDC verification at
`slice04-warning-policy-tightening/cdc-verification.md`.

### A-15

Status: done.

Warning policy tightening is complete for Arc 02: no `after-arc02` or
`transitional-warning` rows remain in `package-path-exceptions.tsv`, and the
final package-path gate exits 0.

### A-16

Status: done.

The final skill-bundle path surface composes at arc scale. `make all` and
`make check-package-paths` pass serially against all generated skill zips with
0 hard failures.

### A-17

Status: done.

Remaining warning backlog is routed rather than hidden. Slice 04 records later
maintenance dispositions for Rust guide references, C++ assets,
JavaScript/Deno guide shorthand, source-clone/provenance references, example
paths, and parser false positives.

## Arc-Scale Evidence

From `/Users/oubiwann/lab/billosys/ai-engineering`:

- `make all`
  - passes and regenerates all 12 generated skill zips
- `make check-package-paths`
  - `zips scanned: 12`
  - `markdown files scanned: 171`
  - `hard failures: 0`
  - `warnings: 295`
  - `explicit exceptions: 3`
  - `skipped external URLs: 656`
- `scripts/check-package-paths --check-exceptions-only`
  - passes
- `make check-skills`
  - passes
- `git diff --check`
  - passes
- `rg -n "after-arc02|transitional-warning" package-path-exceptions.tsv`
  - no matches

From `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`:

- `git diff --check`
  - passes

## Accumulated Arc-Plan Change Log

Arc 02 changed as the slices closed:

- v1.1: Slice 01 verified/closed; targeted tooling/simple entrypoint warnings
  burned down from 20 to 0.
- v1.2: Slice 02 opened with a classification-first requirement for framework
  warnings.
- v1.3: Slice 02 verified/closed; framework `bundled-reference` warnings
  burned down from 4 to 0.
- v1.4: Slice 03 opened with mature-language entrypoint staging-transform
  boundaries.
- v1.5: Slice 03 verified/closed; mature entrypoint warnings burned down from
  107 to 0.
- v1.6: Slice 04 opened to tighten warning policy after entrypoint burn-down.
- v1.7: Slice 04 verified/closed; stale transitional rows converted into
  visible later-maintenance warnings.

## Silent-Drop Diff

Scope as specified:

- burn down package-path warnings in generated skill bundles;
- preserve source-clone usefulness;
- apply source edits where one path spelling works in both contexts;
- use staging transforms where source-root prose should remain source-rooted;
- avoid broad mature guide rewrites;
- avoid unapproved package layout expansion;
- keep CCDP package work out of Arc 02 and route it to Arc 03;
- tighten warning policy before close.

Scope delivered:

- all specified Arc 02 pieces delivered.

Silent drops: none found.

Deferred/routed:

- CCDP package target and protocol distribution story move to Arc 03.
- Release-facing source/zip workflow documentation moves to Arc 04.
- Remaining skill warning backlog is visible for later guide/package
  maintenance rather than blocking Arc 02 close.

## Bubble-up to Project 01

Arc 02 delivers the skill-bundle harmonisation capability promised in the
project roadmap.

The project plan should now move Arc 03 from stub to active detailed planning.
Arc 03 should focus on CCDP as a first-class distribution package: inventory
the protocol source, assembled spec, canonical JSON, examples, visual guide,
and existing Make targets before designing or implementing a package target.

No project scope change is required. The original sequencing remains valid:
distribution path contract, skill bundle harmonisation, CCDP distribution
package, then release and adoption hardening.

## What Worked / What Recurred

What worked:

- small warning-class slices made the package-path burn-down reviewable;
- staging transforms preserved mature source-root entrypoint prose without
  mature guide rewrites;
- warning policy stayed honest by keeping unresolved usability work visible.

What recurred:

- package-writing Make targets must be run serially during verification because
  generated zip files are shared outputs;
- remaining skill-bundle warnings need future maintenance, but they are no
  longer ambiguous Arc 02 transitional debt.

## Closure

Composition verdict: delivered. Gate reviewed by: CDC. Slices: 4, matching the
arc-plan breakdown. Arc-scale composition demonstrated by serial `make all` and
`make check-package-paths` over all generated skill zips. Findings
dispositioned: 4. Deferred: 3, routed to Arc 03, Arc 04, or later
guide/package maintenance.
