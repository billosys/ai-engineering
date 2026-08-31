# Implementation Prompt Packet

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice04-implementation-sequence-synthesis
status: proposed-done
artifact-status: implementation prompt packet
source-files-edited: false
```

## Boundary

This is a compact handoff for future CC and CDC source implementation work.
This Slice04 packet made no source edits, did not authorize source
implementation, and did not change generated zip artifacts.

## Context Packet

Future CC should read, at minimum:

- Project02 `project-plan.md` and `ledger.md`.
- Arc05 `arc-plan.md`, `ledger.md`, and closing report if present.
- Slice01 CDC verification and artifacts:
  implementation surface inventory and release validation surface map.
- Slice02 CDC verification and artifacts: component contract matrix,
  component file layout plan, source-to-component migration plan,
  package-source contract register, and support adapter dependency plan.
- Slice03 CDC verification and artifacts: package target plan, README
  wayfinding plan, skill entrypoint validation plan, package-path link
  exception plan, migration compatibility plan, and Slice04 implementation
  sequence inputs.
- Slice04 artifacts: implementation sequence roadmap, source-edit risk
  register, validation matrix, acceptance gate plan, and Arc05
  close-readiness.
- Arc04 `operator-accepted-architecture.md`.
- Source checkout `AGENTS.md`, `Makefile`, `README.md`, root `SKILL.md`,
  `package-path-exceptions.tsv`, and current package scripts.

## Source-Edit Sequence

1. Component skeletons and source compatibility baseline.
2. Mechanical move of direct-mapping components:
   `project-management`, `work-verification`, and `contribution-style`.
3. Composer posture extraction and `collaboration-framework` route table.
4. `engineering-methods` methodology, component-boundary, and
   source/package/release gate guides.
5. `testing` and `code-auditing` guide splits.
6. `agent-coordination` expansion for CC/CDC/operator terminology,
   delegation, context packets, and result integration.
7. Makefile component package targets, `COMPONENT_ZIPS`, `INSTALL_ZIPS`,
   `ALL_SKILL_FILES`, `CF_FILES`, help text, and aggregate behavior.
8. README composed/standalone wayfinding, source checkout, generated zip,
   unzipped/install, installed skill, migration, and CCDP separation routes.
9. Package-local link repair and bounded `package-path-exceptions.tsv`
   updates.
10. Generated package acceptance sweep and final validation.

## Explicit File-List Commit Rules

Each implementation commit should stage an explicit file list, not a broad
directory add, unless the operator explicitly asks for a bulk stage. Keep one
concern per commit:

- Skeleton/compatibility files.
- Direct mechanical move/copy files.
- Composer/posture files.
- `engineering-methods` files.
- `testing` and `code-auditing` files, split if the diff is large.
- `agent-coordination` files.
- Makefile/package mechanics.
- README/migration guidance.
- Package-path repairs and exception rows.
- Validation fixes, if any.

Generated root-level `*.zip` files and `build/` remain ignored release
artifacts and should not be committed unless the operator changes release
policy.

Every assistant-authored source implementation commit message must include:

```text
Co-authored-by: Codex <noreply@openai.com>

Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Validation Packet For Each Source Slice

Each source implementation close should report:

- What component or surface changed.
- Exact files staged and committed.
- Commands run and outputs summarized.
- `git diff --check`.
- Source checkout cleanliness before starting and after cleanup where
  relevant.
- Component package target output once Makefile targets exist.
- `make check-skills`, `make collab-framework`, `make all`, and `make
  check-package-paths` at the gates named in the validation matrix.
- Conditional CCDP proof if CCDP surfaces changed.

## CDC Review Packet

CDC should independently reproduce command evidence, inspect generated package
roots, verify package-local links, confirm accepted warnings and exceptions are
bounded, check source/provenance preservation, verify all eight accepted
components are covered, and confirm no source implementation claim relies on
this planning slice as source-edit authorization.
