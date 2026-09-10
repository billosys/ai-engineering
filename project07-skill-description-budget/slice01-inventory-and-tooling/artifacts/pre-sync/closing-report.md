# Proposed Completion

Source baseline: `177f1a6` on main. Source and planning changes remain uncommitted;
the user did not request commits. The project is ready for operator review.

## Changes

Implementation files:

- `scripts/skill_descriptions.py`
- `scripts/skill-descriptions`
- `scripts/requirements-skill-tools.txt`
- `scripts/check-skill-description.sh`
- `tests/test_skill_descriptions.py`
- `docs/skill-description-tooling.md`
- `Makefile`, `README.md`, `.gitignore`
- `.github/workflows/ci.yml`, `.github/workflows/release-skill-zips.yml`

Planning files: planning-root AGENTS.md; project plan and ledger; slice plan,
ledger, cc-prompt, this report, cdc-verification; artifacts listed below.

## Row Walk

- S1 done: source inventory covers 20 packaged entrypoints, 9,868 characters;
  installed inventory covers 82 files; actual Codex catalog exposes 55 skills,
  with 21 changed descriptions and 5,710 characters removed. All source
  comparisons succeeded. Evaluation covers each packaged source skill and
  identifies active duplicate standalone/plugin copies.
- S2 done: YAML-aware parsing, normalized Unicode and UTF-8 counts, optional
  per-file and description-total gates, JSON reports, Make targets, and a real
  CLI diagnostic. Source and installed catalogs are explicitly distinguished.
- S3 done: generated prompt/template, 13 concrete candidates with rationale,
  complete preflight validation, read-only default preview, terminal per-file
  approval, stale-file rejection, and isolated description replacement.
  Approved yes/no/quit behavior was exercised through a real PTY on temporary
  files. No repository or installed skill descriptions were changed.
- S4 done: usage/setup documentation, dependency manifest, CI integration,
  evaluation and validation artifacts. Existing packaging gate preserved.

## Verification

- `make test-skill-tools`: 17 tests pass; independently rerun.
- `make check-skills`: all 20 source descriptions pass; independently rerun.
- Proposal review without `--apply`: 13 valid candidates, 0 unresolved,
  0 applied; independently rerun.
- `make check-package-paths`: 20 zips, 287 Markdown files, zero hard failures,
  534 warnings in existing documented categories. Full output in artifact log.
- `git diff --check`: passes; independently rerun before final CI edits and
  repeated by the parent afterward.
- Both edited workflow YAML files parse locally. Remote CI not run.

Independent evidence collection is documented in cdc-verification.md. This is
not a claim of an independent architecture review or a behavioral skill-routing
evaluation. Those limits are explicit in the report and proposal rationales.

## Artifact Inventory

All durable outputs live in `artifacts/`: evaluation.md, source-inventory.json,
all-source-inventory.json, installed-inventory.json, live-catalog.json,
package-check.log, rewrites/prompt.md, rewrites/proposal.json, and the exploratory
research-inclusive-template prompt/proposal. The latter is retained as evidence
of why nested research workbenches were excluded, not as an approval packet.

## Bubble-Up to Project

There is no arc wrapper. This slice delivers all three requested outcomes.
No requested scope was dropped. Discovery needed to distinguish packaged
entrypoints from research clones, and the YAML dependency needed CI/release
installation. Both were incorporated. No further implementation slice is needed
for the agreed tooling scope.

Application and installation of shortened descriptions are a subsequent user
decision. The proposed set saves 4,781 characters (48.4%) in source descriptions;
no claim is made that this alone eliminates warning pressure in every model or
installed catalog. Skill-selection equivalence has not been tested.

## What Worked

The version-matched Codex source clarified which metadata is rendered; the real
prompt diagnostic exposed actual clipping without emulating the allocator.
Real parser and PTY tests verified the approval and preservation contracts.
