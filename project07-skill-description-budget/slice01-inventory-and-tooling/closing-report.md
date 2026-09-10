# Proposed Completion After Upstream Integration

Main baseline `c8909905`; planning baseline `361cdc6f`; updated 2026-09-10.
The user's local tooling was restored from stash without committing. Planning
was restored only under `project07-skill-description-budget`; upstream planning
AGENTS.md and projects01 through06 were preserved. Both stashes remain backups.
The user's unrelated LFE taxonomy was also restored, without modification.

## Row Walk

- S1 done: measured 22 source skills (10,598 chars), 20 packaged entrypoints
  (9,868 chars), and 70 installed/cache files (22,970 chars). The real current
  CLI diagnostic reports 43 skills with no shortened descriptions. Source,
  installed filesystem and runtime scopes are explicitly separate.
- S2 done: restored YAML-aware inventory, optional per-file/aggregate policies,
  JSON reports and Make targets. Preserved upstream version/history and package
  gates. Both test targets use the selected Python environment. Added a
  metadata-version-only stale proposal regression and updated preservation
  fixtures to nested metadata.version. Eighteen description tests pass.
- S3 done: refreshed all hashes and the prompt; 15 proposed candidates pass
  read-only review, zero unresolved and zero applied. The original 13 candidates
  were reused only after matching unchanged names/descriptions; two source-only
  skills were read and added. No SKILL.md descriptions were modified or installed.
- S4 done: updated usage documentation and project evidence, retained pre-sync
  artifacts, integrated dependency setup without losing upstream CI gates,
  and recorded the transient installed-validator failure honestly.

## Verification

`artifacts/test-checks.log` records the final combined run: 18 description tests,
18 version tests and the 20-entry source gate pass. `proposal-review.log` records
15 valid, zero unresolved, zero applied. `package-check.log` records 22 source
skills and 20 packages with zero version errors, plus zero hard path failures
and 529 warnings in the existing warning categories. Both workflow YAML files
parse locally; remote CI was not run. Independent reproduction is limited to
the evidence explicitly listed in cdc-verification.md.

The first version-test run failed its installed-validator output assertion;
the standalone rerun and final combined run passed. Its cause is unknown.
The test now checks the expected rejection status and exposes stderr. The
original failure remains in `artifacts/initial-test-checks.log`.

## Artifact Inventory

Current artifacts: evaluation.md, source-inventory.json, all-source-inventory.json,
installed-inventory.json, live-catalog.json, test-checks.log, initial-test-checks.log,
proposal-review.log, package-check.log, rewrites/prompt.md and rewrites/proposal.json.
`pre-sync/` preserves the original evidence and old closing/verification records,
including the research-inclusive exploratory prompt. Those old proposals have
stale hashes and are not the current approval packet.

Implementation changes are in the description scripts, requirements, focused
tests, Makefile, README, usage guide, gitignore and CI/release workflows, plus
the two-line diagnostic assertion improvement in scripts/tests/test_skill_versions.py.
No framework or domain skill documents changed, so no skill version bumps or
histories were modified. Project/slice plan histories record this integration.

## Bubble-Up to Project

The single-slice plan has no arc wrapper. All three requested outcomes remain
delivered; no scope was dropped. Upstream added two source-only skills and a
version/history contract. This slice accommodates both without taking over
Project05 packaging work. Renumbering to07 follows the user's explicit request.

Actual rewrite approval, installation and semantic routing evaluation remain
separate user decisions, not implied by mechanical validation. All 15 proposed
edits would save 5,008 characters (47.3%) across the 22 source descriptions.
The currently absent warning follows plugin removal; it is not evidence that
these unapplied rewrites improved model behavior. Operator acceptance remains
pending; no further implementation slice is proposed for the agreed scope.

## What Worked

Whole-file proposal hashes exposed upstream metadata changes even where routing
text was unchanged. Separate filesystem and runtime measurements prevented
cached plugins and source-only skills from being mistaken for active entries.
