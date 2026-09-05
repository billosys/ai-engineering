## Summary

AI Engineering 0.5.0 is the knowledge-library reorganization release. It moves
the repository from a mixed `docs/` tree toward a clearer public contract:
`docs/` explains the materials for readers, `knowledge/` stores the source and
derived substrate consumed by skills and packages, and `protocols/` carries
protocol distributions such as CCDP.

The release also carries the framework hardening work from the 0.5.0 cycle:
multi-scale code audits, per-scale ledger files, per-slice artifact homes,
package-context path validation, CCDP protocol packaging, the
collaboration-framework component map, the live scientific-methods skill, and
the planned concept-card method skill architecture.

Project04, the knowledge-library reorganization project, is acceptance-ready:
the planned reorganization arcs are closed, the Arc07 component-entrypoint
cleanup is reconciled, and final validation reproduced green source, package,
install, and CCDP checks. The remaining project-level gate is operator
acceptance of the end-user route from README into `docs/` for explanation and
into `knowledge/` for the actual material substrate.

## Knowledge Library Reorganization

The repository now has a durable split between user documentation and material
substrate:

- `README.md` is a concise orientation and command map.
- `docs/` contains focused end-user guides:
  - `docs/repository-overview.md`
  - `docs/skill-library.md`
  - `docs/collaboration-framework.md`
  - `docs/knowledge-library-anatomy.md`
  - `docs/building-and-installing.md`
  - `docs/protocols.md`
  - `docs/contributing.md`
  - `docs/ORIGINS.md`
- `knowledge/` contains skill source material, derived guides, framework
  substrate, verification templates, contribution templates, and
  domain/tooling knowledge packs.
- `templates/` remains only for cross-cutting support templates such as
  `templates/GUIDE.md`.
- `protocols/` remains separate for protocol distributions, with CCDP packaged
  as a protocol package rather than an installable assistant skill.

This closes the old ambiguity where `docs/` sometimes meant "documentation
about the repo" and sometimes meant "the material being packaged or loaded."
End users can now start from README, read `docs/` for explanation, and follow
links into `knowledge/` when they need the actual skill or framework material.

The public vocabulary was also settled. Skill kind and skill topology are
separate axes:

- Kind describes what the skill is about: domain/tooling,
  framework/operational, method, protocol distribution/package, or support
  material.
- Topology describes how it loads and composes: atomic skills have one bounded
  load reason, while composite skills select, sequence, route, govern, or
  compose multiple loadable parts.

Rust is now the public example of an atomic domain/tooling skill. The
top-level `collaboration-framework` remains the public example of a composite
framework/operational skill. `scientific-methods` is now the live method-skill
example for practical inquiry, controlled comparison, experiment planning,
evaluation rubrics, evidence capture, and regression analysis. CCDP is
explicitly a protocol distribution and protocol package, not an installable
skill package. `concept-card-method` remains a planned method skill until
source and package support are implemented.

Project04 closed six arcs to get there:

- source inventory and material-role classification;
- target directory contract and migration plan;
- directory reorganization implementation;
- README decomposition and focused end-user docs;
- public skill vocabulary and atomic/composite positioning;
- final validation, packaging, installability, CCDP package separation, and
  operator-acceptance readiness.

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

Generated package archives now land under `target/skills/` instead of the
repository root. The Makefile keeps the output path in a single
`ZIP_OUTPUT_DIR` variable, uses that path for skill and CCDP package archives,
and ignores `target/` as generated build output. This keeps repeated local
packaging runs from cluttering the source checkout root while preserving the
existing archive names and install behavior.

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

The current Project04 release-readiness baseline is:

- 13 generated skill zips scanned.
- 222 packaged Markdown files scanned.
- 0 hard failures.
- 366 visible warnings.
- 3 explicit exceptions.
- 656 external URLs skipped.

The final install smoke installed 13 `SKILL*.md` entrypoints into an isolated
temporary directory and confirmed that no `ccdp` install root was created.

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

The source checkout now carries this component contract directly:

- `knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md` has been split
  into `knowledge/contribution-style/guides/01-contribution-style.md` for
  maintainer-facing voice and calibrated contribution discipline, and
  `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md` for
  local draft, filing, line-reference, paste-boundary, cross-linking, and
  template workflow. The old path is not a live package route.
- `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md` remains the
  reusable package-local authoring template.

- `knowledge/collaboration-framework/SKILL.md` is the source entrypoint for
  the composed framework, while the generated package still exposes
  `collaboration-framework/SKILL.md`.
- Each component root listed above has a concise `SKILL.md` wayfinder for
  narrower use.
- Long component material lives under component-owned `guides/` directories.
- Contribution and verification forms remain under component-owned
  `templates/` directories.
- The generated `collaboration-framework.zip` package includes the composed
  entrypoint, component `SKILL.md` wayfinders, moved `guides/` material, and
  preserved `templates/` material without legacy component `docs/` entries.

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

`scientific-methods` is the first live method skill in this repository. It
captures the experiment-design pattern used during the framework comparison
trial: pin the independent variable, control contamination, bound the task,
predeclare outputs and measures, preserve evidence, compare against a rubric,
and report threats to validity. The package includes:

- `knowledge/scientific-methods/SKILL.md`
- nine focused guides under `knowledge/scientific-methods/guides/`
- experiment protocol, A/B comparison prompt, and evaluation rubric templates
  under `knowledge/scientific-methods/templates/`
- `knowledge/scientific-methods/version-history.md`

The generated package target is `scientific-methods.zip`, built by
`make scientific-methods` and included in `make skills`, `make all`, and
`make install`.

`concept-card-method` remains planned method material. Its planned package
name is still `concept-card-method.zip`, but this release does not implement
or ship that package.

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

- `knowledge/collaboration-framework/SKILL.md` is the source
  `collaboration-framework` skill entrypoint; generated packages stage it at
  `collaboration-framework/SKILL.md`.
- `knowledge/code-auditing/SKILL.md` routes to the split code-auditing guide
  set:
  `knowledge/code-auditing/guides/01-audit-scope-and-map.md`,
  `02-findings-and-severity.md`, `03-scale-aware-auditing.md`,
  `04-modernization-synthesis.md`, and
  `05-audit-to-hardening-handoff.md`. The old `CODE-AUDIT.md` path was renamed
  and is no longer a live package route.
- `knowledge/project-management/SKILL.md` routes to
  `knowledge/project-management/guides/README.md`, which carries the
  project -> arc -> slice lifecycle, Expedited Mode, and planning-worktree
  wayfinding.
- `knowledge/engineering-methods/SKILL.md` routes to
  `knowledge/engineering-methods/guides/01-engineering-methodology.md`, which
  carries the 9-point SDLC and methodology substrate.
- `knowledge/work-verification/SKILL.md` routes to five focused
  `knowledge/work-verification/guides/` files for ledger discipline, evidence
  strength, row closure, silent-drop checks, and independent verification; the
  retained full protocol remains under `templates/`.
- `knowledge/agent-coordination/SKILL.md` routes to the split
  agent-coordination guide set:
  `knowledge/agent-coordination/guides/01-when-to-delegate.md`,
  `02-context-packets.md`, `03-result-integration.md`, and
  `04-anti-patterns.md`. The old `SUBAGENT-DELEGATION-POLICY.md` path was
  renamed and is no longer a live package route.
- `knowledge/contribution-style/SKILL.md` routes to
  `knowledge/contribution-style/guides/01-contribution-style.md`,
  `knowledge/contribution-style/guides/02-upstream-ticket-workflow.md`, and
  `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`; the old
  `CONTRIBUTION-STYLE.md` path was split and is no longer a live package
  route.
- `knowledge/testing/SKILL.md` routes to
  `knowledge/testing/guides/01-testing-discipline.md`,
  `knowledge/testing/guides/02-coverage-hardening.md`, and
  `knowledge/testing/guides/03-validation-gates.md`; the old
  `CODE-COVERAGE.md` path was renamed into the coverage-hardening guide.
- `knowledge/project-management/version-history.md` records the
  project-management guide history, including per-scale ledger files and
  per-slice artifact homes.
