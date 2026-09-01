## Summary

Collaboration Framework v1.4.1 — a framework hardening release that expands
audits from whole-repo language checks into explicit multi-scale reviews,
settles ledger files at every planning scale, gives slice-produced artifacts a
default home, and harmonizes source-clone, skill-bundle, and CCDP package
path behaviour. The README was refreshed on 2026-09-01 with a clearer
collaboration-framework component map for whole-framework and standalone use,
plus a new method-skill category for reusable knowledge-work methods.

## Harmonise Paths

Fixed the packaging-path mismatch that made finding the full paths of files in the
bundled Markdown awkward for humans and LLMs. The release now supports two first-class
reading contexts: the cloned `ai-engineering` source tree, and generated zip artifacts
either read directly or after unpacking.

Part of this work included adding a checked path contract instead of relying on prose
discipline alone. Skill zips now have a package-aware Markdown gate, targeted
entrypoints were rewritten or staged so bundled readers see bundled paths, and
the remaining warning surface is explicit rather than accidental.

CCDP also gained its own distribution surface: `ccdp.zip`, rooted at `ccdp/`,
with a package README and a dedicated package validator. Source-only provenance
material remains in the repo, while package consumers get entrypoints and
references that are meaningful from the package itself.

## Multi-Scale Code Audits

The code-audit prompt now treats an audit as a scale climb, not a context-window
sampling pass. Auditors must build an audit map and move from local code details
up through file/module, logical unit, package or crate, application/service,
whole codebase, and workspace/monorepo where present.

The updated prompt adds:

- An explicit audit map before findings are written.
- Scale coverage requirements for every audited language.
- Stable finding IDs and a `Scale` field on each finding.
- Architecture/coherence and modernization finding categories.
- Coherence observations for cross-file or cross-package drift.
- A new modernization synthesis at
  `workbench/<DATE>-audit-modernization-synthesis.md`.

This closes the old failure mode where "whole repo audit" could still collapse
into "whatever files fit in the current context."

## Per-Scale Ledger Files

Project management now gives every scale its own sibling `ledger.md` file.
Project, arc, and slice ledgers no longer live as embedded sections inside
their plan files.

The canonical shape is now:

- `projectNN-<slug>/project-plan.md`
- `projectNN-<slug>/ledger.md`
- `arcNN-<slug>/arc-plan.md`
- `arcNN-<slug>/ledger.md`
- `sliceNN-<slug>/slice-plan.md`
- `sliceNN-<slug>/ledger.md`

This keeps plan files focused on scope and sequencing while ledger files carry
the acceptance and composition rows that make closure checkable.

## Per-Slice Artifact Homes

Durable artifacts produced by a slice now have a default home:

```text
sliceNN-<slug>/artifacts/
```

The operator can override the location, but the override must be explicit in
`slice-plan.md`, repeated in `cc-prompt.md`, and verified at slice close through
the artifact inventory in `closing-report.md` and `cdc-verification.md`.

This matters because slice work often produces transcripts, captures, reports,
generated examples, or other durable evidence. The new default keeps those
artifacts attached to the slice that produced them instead of scattering them
through root `workbench/`, `reports/`, scratch directories, or implementation
docs.

## Package Path Gate

The repo now includes `scripts/check-package-paths`, a package-context Markdown
path validator for generated skill zips, plus a Make target:

```sh
make check-package-paths
```

The check builds the skill zips and scans Markdown links, reference
definitions, and path-like code spans in the packaged context. It distinguishes
bundled references, source-clone references, repo-only/provenance paths,
example-project paths, external URLs, and parser false positives.

`package-path-exceptions.tsv` records accepted exceptions and transitional
warnings, so path problems are visible without forcing every historical or
source-only reference to be rewritten in one release.

Several skill entry points and bundled documents were harmonized so package
consumers see package-valid paths rather than source-tree-only paths:

- Biome JS linter
- Biome web linter
- Deno JS linter
- Tailwind CSS
- Cobalt
- Collaboration framework package-internal references
- Mature Rust and JavaScript entrypoints staged through package-only transforms

The final Project01 acceptance baseline is:

- 12 generated skill zips scanned.
- 171 packaged Markdown files scanned.
- 0 hard failures.
- 295 visible warnings.
- 3 explicit exceptions.
- 656 external URLs skipped.

## Collaboration Framework Component Map

The README now describes the collaboration framework as both a composed whole
and a set of independently useful component disciplines. The daily-driver
entry point remains `/collaboration-framework`; the component names below are
the stable contract for narrower use, route tables, package planning, and
future standalone skill packaging.

| Component | Role in the composed framework | Independent use case |
|-----------|--------------------------------|----------------------|
| `collaboration-framework` | Daily-driver composer with the collaboration posture, quality floor, and route table. | Start broad work, establish the peer frame, and decide which specialist discipline to load next. |
| `engineering-methods` | Process layer for the knowledge substrate, 9-point SDLC, process rigour, component-boundary analysis, and source/package/release gates. | Plan how work should proceed, evaluate boundaries, or set validation and release gates. |
| `project-management` | Project -> arc -> slice planning and close lifecycle, including worktree layout, bubble-up, confirmation protocol, and anti-patterns. | Open, inspect, revise, or close planning work without loading the entire framework. |
| `work-verification` | Ledger discipline, evidence strength, row closure, independent reproduction, and silent-drop checks. | Define or verify acceptance rows and distinguish asserted, attested, reproduced, and reconciled evidence. |
| `testing` | Testing discipline, coverage hardening, and validation gates. | Drive tests, coverage, reproducible failures, and hardening after findings. |
| `code-auditing` | Diagnosis-only audits with audit maps, severity, scale coverage, modernization synthesis, and remediation handoff. | Review or audit code without making changes. |
| `agent-coordination` | CC/CDC/operator role language, delegation decisions, context packets, result integration, and multi-assistant coordination. | Prepare handoffs, delegate lookup work, or integrate subagent output. |
| `contribution-style` | Upstream contribution voice, calibrated claims, issue/PR framing, and contribution-ticket workflow. | Draft maintainer-facing bug reports, feature requests, documentation fixes, questions, or handoffs. |

This release note records the documentation update only. The source checkout's
current release surface still preserves the existing `/collaboration-framework`
entry path while component packaging is handled by the follow-on source
implementation work.

## Concept Card Method Planning

This release records the completion of Project03, the planning project that
turns the earlier v3.2 concept-card extraction methodology into a v4.0
method-skill architecture and implementation plan.

The project preserved the v3.2 workbench source documents as the baseline,
assessed the method on its own merits, identified the v4.0 gaps, and then
planned the next version as a repo knowledge skill rather than a language-skill
clone. The resulting architecture treats concept-card extraction as a
provenance-bearing knowledge-work method with explicit support for concept
extraction, ontology critique, competency questions, graph-ready
relationships, evidence grading, reconciliation, verification, and
memory-admission boundaries.

Project03 closed with five planned and verified arcs:

- method positioning and initial boundary aid;
- v3.2 source inventory and v4.0 gap analysis;
- v4.0 conceptual model;
- v4.0 skill architecture;
- implementation plan and project-close input.

The accepted source shape for future implementation is
`knowledge/concept-card-method/`: a thin `SKILL.md` wayfinder plus focused
`guides/`, templates, examples, validation documentation, and reference
material. The planned package name is `concept-card-method.zip`, but this
release does not implement or ship that package.

The README now names **method skills** as a distinct skill-library category:
skills that teach an assistant how to perform a durable knowledge-work method,
not just how to work in a specific programming, tooling, or design domain.
`concept-card-method` is listed as the first planned method skill and remains
framed as planned, not already packaged.

## CCDP Package

The release adds a CCDP protocol package workflow without folding CCDP into the
skill `INSTALL_ZIPS` set:

```sh
make ccdp-package
make check-ccdp-package
```

`make ccdp-package` builds `ccdp.zip` with a single `ccdp/` root. The package
contains the assembled protocol specification, source materials needed for
rebuild-capable use, and a generated `ccdp/README.md` oriented around package
readers.

`scripts/check-ccdp-package` verifies the zip shape, package README, and
Markdown path references in the extracted package context. The final acceptance
run scanned 42 Markdown files and 14 Markdown path references with 0 shape,
README, or path failures.

## Worktree Housekeeping

`.worktrees` is now ignored. This matches the project-management default that
planning worktrees live under the repository's worktree convention without
turning local planning checkouts into implementation-branch changes.

## Framework Document Updates

The release updates the collaboration-framework entry point and the operational
documents that carry its planning, audit, and verification mechanics:

- `SKILL.md` bumped to `1.4.1`.
- `docs/CODE-AUDIT.md` added version `1.1` for multi-scale audits and
  modernization synthesis.
- `docs/PROJECT-MANAGEMENT.md` bumped to `2.5`.
- `docs/AI-ENGINEERING-METHODOLOGY.md` bumped to `1.9`.
- `templates/LEDGER-DISCIPLINE.md` bumped to `2.3`.
- `docs/pm/version-history.md` now records both the per-scale ledger layout
  update and the per-slice artifact-home default.
