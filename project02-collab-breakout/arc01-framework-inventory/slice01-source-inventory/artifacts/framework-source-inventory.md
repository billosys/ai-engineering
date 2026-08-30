# Collaboration Framework Source Inventory

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice01-source-inventory
status: proposed-done
source-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
project01-gate-capture: artifacts/project01-gate-check.txt
candidate-labels: non-final, for later analysis
```

## Scope

This inventory was produced from the current source checkout without editing
source files. It covers the required collaboration-framework entry points,
guides, templates, and split project-management files named by the slice plan.

Candidate breakout labels below are explicitly non-final. They name possible
analysis buckets for Slice 02 and Arc 02, not accepted component boundaries.

## Inventory Entries

### README.md

- Source path: `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- Role: Repository-level orientation, installation guide, skill library index,
  build/package command index, and CCDP distribution overview.
- Major sections: About, Contents, The collaboration framework, The problems,
  The solutions, What you get, How to use it, Under the hood, The skill
  library, Building/installing, Repository layout, CCDP, Contributing, License.
- Load moment: First-stop human/source-clone orientation; packaging and release
  command lookup; source-vs-package workflow clarification.
- Standalone usefulness: High for users and maintainers learning what the repo
  contains and how to build or install bundles, but it depends on linked files
  for the actual collaboration discipline.
- Dependencies: `Makefile`, `SKILL.md`, `docs/`, `templates/`,
  `protocols/ccdp/`, package check scripts, generated skill zips, and
  `ccdp.zip`.
- Path/package notes: States that skill zips are produced through `make`, named
  from frontmatter `name:`, wrapped in a matching root directory, and uploadable
  to Claude; unzipped skills install under `~/.agents/`. It distinguishes the
  source checkout from generated packages and says CCDP is packaged separately
  as `ccdp.zip`, not as an installable skill zip.
- Concepts/discipline contributed: discovery, installation, release-surface
  vocabulary, package/source distinction, repository layout, CCDP boundary,
  contributor orientation.
- Candidate breakout label: `repository-orientation-and-distribution`
  (non-final, for later analysis).

### SKILL.md

- Source path: `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- Role: Runtime entry point for the collaboration-framework skill and routing
  table for the documents the model must load at different work moments.
- Major sections: What this is, Notes for Codex, When to use this skill,
  posture summary, practice summary, framework file table, what is not loaded,
  version history, using the skill.
- Load moment: When the collaboration-framework skill is invoked, especially
  before planning, closing, ledgered work, code audit, coverage work,
  delegation decisions, or contribution-ticket drafting.
- Standalone usefulness: Medium-high. It provides enough framing to select
  next documents, but deliberately routes planning/closing and ledger details
  to `docs/PROJECT-MANAGEMENT.md` and `templates/LEDGER-DISCIPLINE.md`.
- Dependencies: `docs/AI-CONSTITUTION-SUPPLEMENT.md`,
  `docs/AI-ENGINEERING-METHODOLOGY.md`, `docs/PROJECT-MANAGEMENT.md`,
  `templates/LEDGER-DISCIPLINE.md`, audit/coverage/delegation/contribution
  guides, and external domain skills loaded separately.
- Path/package notes: Acts as package entrypoint. Its relative links must keep
  resolving inside built skill zips and unzipped installs. It must not assume
  planning-worktree files are packaged with the skill.
- Concepts/discipline contributed: model posture, task routing, load-order
  discipline, peer frame, artifact and planning gates.
- Candidate breakout label: `framework-entrypoint-and-routing` (non-final, for
  later analysis).

### docs/AI-CONSTITUTION-SUPPLEMENT.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-CONSTITUTION-SUPPLEMENT.md`
- Role: Normative posture layer for collaborative AI work, adapting the user's
  AI Constitution Supplement to coding-agent behavior.
- Major sections: Preamble, notes for Codex, structural pulls, rights rubric,
  interdependence and compassion, nine augmentations, open questions, summary
  principles, key research sources, version history.
- Load moment: When the peer frame, power dynamics, user agency, compassion, or
  anti-deference posture needs grounding.
- Standalone usefulness: Medium. It carries the character/posture argument, but
  operational execution depends on the methodology, project-management, and
  ledger files.
- Dependencies: `docs/AI-ENGINEERING-METHODOLOGY.md` for process translation;
  `SKILL.md` for routing; external research sources cited in the guide.
- Path/package notes: Linked by `SKILL.md`; package-local relative links and
  references must remain valid after zip staging.
- Concepts/discipline contributed: structural pressures on AI behavior,
  rights, user sovereignty, compassion, honest disagreement, responsibility,
  epistemic humility.
- Candidate breakout label: `collaborative-posture-and-ethics` (non-final, for
  later analysis).

### docs/AI-ENGINEERING-METHODOLOGY.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-ENGINEERING-METHODOLOGY.md`
- Role: Engineering practice layer that translates posture into substrate,
  process, audit, verification, and disciplined agent collaboration.
- Major sections: Preamble, notes for Codex, three pillars, knowledge substrate,
  collaborative posture, process rigour, practitioner disciplines, applied OSS
  positions, open questions, provenance, version history.
- Load moment: Before planning how substantial engineering work should be
  structured, audited, verified, or delegated.
- Standalone usefulness: High for process framing, but it intentionally
  delegates concrete planning mechanics to `docs/PROJECT-MANAGEMENT.md` and
  concrete row closure to `templates/LEDGER-DISCIPLINE.md`.
- Dependencies: Constitution supplement, project-management docs, ledger
  discipline, code-audit guidance, coverage guidance, delegation policy.
- Path/package notes: Source-clone and package users reach it through
  `SKILL.md`; cross-links must stay package-relative.
- Concepts/discipline contributed: knowledge substrate, peer frame,
  verification, 9-point SDLC, ledger-backed closure, code audit, coverage,
  anti-degradation, subagent boundaries.
- Candidate breakout label: `engineering-methodology-and-process` (non-final,
  for later analysis).

### docs/PROJECT-MANAGEMENT.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md`
- Role: Wayfinder for the split project-management corpus and mandatory load
  set for planning or closing work.
- Major sections: Notes for Codex, scope, split-file load table, required load
  set for project/arc/slice work, shortcuts, version history.
- Load moment: Must be read before planning or closing any project, arc, or
  slice, or before creating planning directories.
- Standalone usefulness: High as a router, low as the complete body. It points
  to the focused `docs/pm/*.md` files for concrete rules.
- Dependencies: `docs/pm/01-scales-of-work.md` through
  `docs/pm/09-worked-example-odm.md`, `docs/pm/version-history.md`, and
  `templates/LEDGER-DISCIPLINE.md`.
- Path/package notes: Documents the canonical planning worktree and default
  slice artifact home. Those planning artifacts live outside packaged skill
  source content.
- Concepts/discipline contributed: planning load order, planning tree layout,
  close/bubble-up routing, artifact home discipline.
- Candidate breakout label: `project-management-wayfinder` (non-final, for
  later analysis).

### docs/pm/01-scales-of-work.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/01-scales-of-work.md`
- Role: Defines the project, arc, slice, step, and iteration scales used by
  the framework.
- Major sections: Project, Arc, Slice, Step, Iteration, scale discipline.
- Load moment: When selecting the right work unit or reviewing whether a
  planning record is using the right scale.
- Standalone usefulness: Medium. Useful for vocabulary, but needs the layout,
  top-down planning, and close files to execute the process.
- Dependencies: `docs/pm/02-canonical-planning-worktree.md`,
  `docs/pm/03-planning-top-down.md`, `docs/pm/04-closing-slices.md`,
  `docs/pm/05-closing-arcs.md`.
- Path/package notes: States that durable slice-produced artifacts belong under
  the owning slice's `artifacts/` directory by default unless the operator
  records an override.
- Concepts/discipline contributed: scale hygiene, scope control, slice as
  execution unit, iteration as repair loop rather than planning unit.
- Candidate breakout label: `project-management-scale-model` (non-final, for
  later analysis).

### docs/pm/02-canonical-planning-worktree.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/02-canonical-planning-worktree.md`
- Role: Defines the branch/worktree layout and canonical filenames for
  planning records.
- Major sections: default branch and worktree, project/arc/slice directory
  tree, required files, artifact home, local instruction handoff.
- Load moment: Before creating or locating planning directories, or when a path
  needs confirmation.
- Standalone usefulness: High for layout, but not enough for planning content
  or closure semantics.
- Dependencies: `docs/pm/06-confirmation-protocol.md`,
  `docs/pm/03-planning-top-down.md`, `templates/LEDGER-DISCIPLINE.md`.
- Path/package notes: Establishes `.worktrees/planning` on a planning branch
  as the default planning substrate, with `projectNN-<slug>` directories and
  per-slice `artifacts/` homes by default.
- Concepts/discipline contributed: path discipline, planning/source separation,
  canonical filenames, artifact placement.
- Candidate breakout label: `planning-worktree-and-layout` (non-final, for
  later analysis).

### docs/pm/03-planning-top-down.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/03-planning-top-down.md`
- Role: Defines how to create project, arc, and slice open sets from the top
  down.
- Major sections: project planning, arc planning, slice planning, durable
  artifacts, ledger criteria, deferring detailed downstream open sets.
- Load moment: When opening new project/arc/slice records or converting a goal
  into ledgered work.
- Standalone usefulness: High for opening work, but relies on the layout file
  for path shape and ledger discipline for close mechanics.
- Dependencies: `docs/pm/01-scales-of-work.md`,
  `docs/pm/02-canonical-planning-worktree.md`,
  `templates/LEDGER-DISCIPLINE.md`.
- Path/package notes: Reinforces that durable outputs are housed under the
  owning slice by default and that no second output location should be invented.
- Concepts/discipline contributed: open-set planning, falsifiable ledger rows,
  explicit scope, downstream deferral.
- Candidate breakout label: `planning-open-set-mechanics` (non-final, for
  later analysis).

### docs/pm/04-closing-slices.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/04-closing-slices.md`
- Role: Defines how a slice closes, including evidence review, artifact
  inventory, ledger walk, and bubble-up to its arc.
- Major sections: close report content, artifact inventory, ledger row walk,
  bubble-up notes, status behavior, CDC verification handoff.
- Load moment: At slice close or when auditing a proposed slice close.
- Standalone usefulness: High for slice close execution, paired with ledger
  discipline for evidence strength.
- Dependencies: `templates/LEDGER-DISCIPLINE.md`,
  `docs/pm/05-closing-arcs.md`, slice plan and ledger.
- Path/package notes: Requires slice-produced durable artifacts to live under
  `artifacts/` unless an explicit operator override is recorded.
- Concepts/discipline contributed: slice close mechanics, silent-drop check,
  bubble-up, artifact accountability.
- Candidate breakout label: `slice-close-and-bubble-up` (non-final, for later
  analysis).

### docs/pm/05-closing-arcs.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/05-closing-arcs.md`
- Role: Defines arc and project composition close, emphasizing recomposition of
  slice evidence rather than inherited child claims.
- Major sections: arc close, project close, composition rows, remediation
  routing, bubble-up from children to parent.
- Load moment: When closing an arc/project or preparing higher-scale readiness
  from completed slices.
- Standalone usefulness: High for composition close, but depends on child
  slice reports and ledgers.
- Dependencies: `docs/pm/04-closing-slices.md`,
  `templates/LEDGER-DISCIPLINE.md`, parent plan/ledger files.
- Path/package notes: Composition artifacts remain in planning worktree parent
  directories; durable slice evidence remains in the owning slice path.
- Concepts/discipline contributed: recomposition, parent ledger closure,
  remediation-not-iteration at larger scale, child evidence reuse limits.
- Candidate breakout label: `arc-project-composition-close` (non-final, for
  later analysis).

### docs/pm/06-confirmation-protocol.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/06-confirmation-protocol.md`
- Role: Defines when and how to confirm planning layout choices with the
  operator before creating directories or filenames.
- Major sections: when to use it, proposed layout prompt shape, operator
  responses, local instruction files, artifact-home confirmation.
- Load moment: Before creating a new planning substrate or when existing local
  instructions do not settle the path.
- Standalone usefulness: High for preventing wrong-path work, but relies on the
  canonical layout file for the default shape.
- Dependencies: `docs/pm/02-canonical-planning-worktree.md`, local
  instruction files such as `AGENTS.md`, operator response.
- Path/package notes: Specifically protects against planning artifacts landing
  in source docs, release docs, root workbench directories, or other stale
  locations.
- Concepts/discipline contributed: explicit operator confirmation, planning
  path safety, local instruction capture.
- Candidate breakout label: `planning-confirmation-protocol` (non-final, for
  later analysis).

### docs/pm/07-anti-patterns.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/07-anti-patterns.md`
- Role: Names planning-layout and lifecycle shapes that should be refused or
  corrected.
- Major sections: milestone/project confusion, misplaced slice artifacts,
  branch/worktree mistakes, implementation-doc planning trees, date-only
  directories, implied dependencies.
- Load moment: When reviewing a proposed planning layout, diagnosing drift, or
  rejecting a tempting shortcut.
- Standalone usefulness: Medium-high. It is corrective, not a full process
  guide.
- Dependencies: `docs/pm/02-canonical-planning-worktree.md`,
  `docs/pm/03-planning-top-down.md`, `docs/pm/06-confirmation-protocol.md`.
- Path/package notes: Explicitly rejects root `workbench/`, `reports/`, scratch
  directories, and implementation `docs/` trees as default homes for planning
  records or slice-produced durable artifacts.
- Concepts/discipline contributed: anti-drift policy, artifact locality,
  planning/source separation.
- Candidate breakout label: `planning-anti-patterns-and-repair` (non-final,
  for later analysis).

### docs/pm/08-maintenance.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/08-maintenance.md`
- Role: Defines how to evolve project-management guidance without creating
  inconsistent process instructions.
- Major sections: when to update the wayfinder, version history, cross-file
  synchronization, audit guidance.
- Load moment: When the framework process docs themselves change.
- Standalone usefulness: Medium. It is mainly a maintainer checklist.
- Dependencies: `docs/PROJECT-MANAGEMENT.md`, `docs/pm/version-history.md`,
  related PM split files.
- Path/package notes: Calls out that durable slice artifacts default to
  `artifacts/` and that framework planning belongs in the planning branch,
  not implementation product docs.
- Concepts/discipline contributed: process-doc maintenance, version-history
  discipline, split-file coherence.
- Candidate breakout label: `framework-maintenance-discipline` (non-final, for
  later analysis).

### docs/pm/09-worked-example-odm.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/09-worked-example-odm.md`
- Role: Small example showing the project-management flow through a real
  staged project.
- Major sections: scope of example, project split, arc/slice progression,
  close behavior, lessons.
- Load moment: When an operator or agent needs a concrete example of applying
  the planning process.
- Standalone usefulness: Medium. It illustrates but does not replace the
  process rules.
- Dependencies: PM scale/layout/planning/close files.
- Path/package notes: Uses example paths as illustrations; should not be
  copied blindly into a different repo.
- Concepts/discipline contributed: applied planning example, sequencing,
  evidence handoff.
- Candidate breakout label: `project-management-examples` (non-final, for
  later analysis).

### docs/pm/version-history.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/version-history.md`
- Role: Maintains PM guidance change history and rationale.
- Major sections: v2.5 artifact-home update, v2.4 closing guidance, v2.3
  artifact placement, v2.2 planning worktree change, older revisions.
- Load moment: When auditing why a PM rule exists or updating PM docs.
- Standalone usefulness: Medium for provenance, low for operational execution.
- Dependencies: all PM split files and `docs/PROJECT-MANAGEMENT.md`.
- Path/package notes: Captures the historical shift from implementation-branch
  design trees to `.worktrees/planning`, and the default slice `artifacts/`
  home.
- Concepts/discipline contributed: planning-process provenance, compatibility
  expectations, path-rule history.
- Candidate breakout label: `project-management-provenance` (non-final, for
  later analysis).

### templates/LEDGER-DISCIPLINE.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/templates/LEDGER-DISCIPLINE.md`
- Role: Scale-free verification protocol for project, arc, and slice ledgers.
- Major sections: core invariant, evidence strengths, slice protocol, arc
  protocol, project protocol, failure modes, lineage and version history.
- Load moment: At the start of any ledgered unit and again when closing or
  verifying rows.
- Standalone usefulness: High for verification semantics, but it assumes the
  project-management files define where plans, ledgers, and artifacts live.
- Dependencies: `docs/PROJECT-MANAGEMENT.md`, project/arc/slice plans and
  ledgers, actual artifacts and command outputs.
- Path/package notes: Defines durable slice-produced artifacts as living in
  `sliceNN-<slug>/artifacts/` by default unless the operator records another
  path. For this slice, the slice plan explicitly names the three analysis
  outputs in the slice directory.
- Concepts/discipline contributed: evidence-backed row closure,
  asserted/attested/reproduced/reconciled evidence ladder, closer/verifier
  separation, silent-drop checks.
- Candidate breakout label: `ledger-verification-protocol` (non-final, for
  later analysis).

### docs/CODE-AUDIT.md

- Source path: `/Users/oubiwann/lab/billosys/ai-engineering/docs/CODE-AUDIT.md`
- Role: Diagnosis-only audit procedure for production codebases, including
  multi-scale audit mapping and modernization synthesis.
- Major sections: preparation, scope, output files, audit report structure,
  index structure, modernization synthesis, stance, hunt list, do-not-modify
  rule, version history.
- Load moment: When the user asks for a code-quality audit or modernization
  assessment without immediate source changes.
- Standalone usefulness: High for audit execution, but it depends on language
  skills and repository-specific build/test discovery.
- Dependencies: language/domain skills, repository build/test files, source
  tree, `workbench/<DATE>-audit-*.md` output convention.
- Path/package notes: Uses source-checkout `workbench/` audit outputs by
  convention; this is an audit-output convention, not a planning-slice artifact
  home. Project02 should decide whether that convention remains inside a
  future audit component.
- Concepts/discipline contributed: diagnosis-only stance, multi-scale audit
  map, finding IDs, severity discipline, evidence-backed modernization.
- Candidate breakout label: `code-audit-discipline` (non-final, for later
  analysis).

### docs/CLAUDE-CODE-COVERAGE.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/CLAUDE-CODE-COVERAGE.md`
- Role: High-coverage testing workflow for implementation tasks, with a strong
  95 percent threshold and persistence loop.
- Major sections: objective, notes for Codex, core principles, testing strategy
  by code type, obstacles, coverage report interpretation, quality gates,
  iterative process, anti-patterns, sample session, final checklist.
- Load moment: When test coverage is the requested focus or when a slice needs
  explicit coverage hardening.
- Standalone usefulness: High for coverage work, although command names must
  be adapted to the repository's own build/test system.
- Dependencies: repository test tools, coverage tool output, language-specific
  test idioms, implementation source.
- Path/package notes: Mentions repository-owned Makefile, package scripts, CI
  config, or language-native commands as command sources; does not define a
  package contract itself.
- Concepts/discipline contributed: coverage floor, root-cause repair, error
  path testing, quality gates, iterative test expansion.
- Candidate breakout label: `coverage-hardening-discipline` (non-final, for
  later analysis).

### docs/SUBAGENT-DELEGATION-POLICY.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/SUBAGENT-DELEGATION-POLICY.md`
- Role: Defines when subagents can be used, what cannot be delegated, and how
  to verify delegated lookup.
- Major sections: policy, why, correct use, install instructions for tools,
  verification caveat, version history.
- Load moment: Before considering subagent use in a non-trivial task.
- Standalone usefulness: High for delegation boundaries; low for the rest of
  project execution.
- Dependencies: main model judgment, task context, optional subagent tooling,
  verification by the main agent.
- Path/package notes: No special package path assumptions beyond `SKILL.md`
  link validity. It should remain reachable wherever delegation guidance is
  packaged.
- Concepts/discipline contributed: serial thinking/parallel lookup split,
  no-delegated-judgment rule, verification ownership.
- Candidate breakout label: `delegation-policy` (non-final, for later
  analysis).

### docs/CONTRIBUTION-STYLE.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/docs/CONTRIBUTION-STYLE.md`
- Role: Voice and conduct guidance for upstream issue reports and contribution
  notes.
- Major sections: why this matters, voice, shape, calibrated honesty, respect
  maintainer ownership, what to leave out, sizing, tone under pressure,
  relationship with tickets.
- Load moment: Before drafting upstream-facing issues, PR notes, or maintainer
  communications.
- Standalone usefulness: High for tone and posture; ticket structure lives in
  the template.
- Dependencies: `templates/CONTRIBUTION-TICKET.md`, actual evidence from the
  audit or implementation task, maintainer/project context.
- Path/package notes: Package-relative link from `SKILL.md` and from the
  ticket template must remain valid.
- Concepts/discipline contributed: maintainer-respecting tone, calibrated
  claims, evidence humility, issue scope.
- Candidate breakout label: `contribution-style-and-voice` (non-final, for
  later analysis).

### templates/CONTRIBUTION-TICKET.md

- Source path:
  `/Users/oubiwann/lab/billosys/ai-engineering/templates/CONTRIBUTION-TICKET.md`
- Role: Concrete upstream ticket template for bugs, features, docs, design
  questions, and follow-ups.
- Major sections: header block, body shape, calibrated honesty, what to leave
  out, four ticket shapes, filing workflow, version history.
- Load moment: When drafting a contribution ticket from verified findings.
- Standalone usefulness: High for structure, but it relies on
  `docs/CONTRIBUTION-STYLE.md` and task evidence for good content.
- Dependencies: contribution style guide, concrete source paths/lines, test or
  reproduction evidence, upstream repository conventions.
- Path/package notes: Template path is under `templates/`; source paths inside
  generated tickets should be actual upstream paths, not local planning paths.
- Concepts/discipline contributed: upstream ticket structure, evidence blocks,
  claim boundaries, maintainer workflow.
- Candidate breakout label: `contribution-ticket-template` (non-final, for
  later analysis).

## Open Questions

- Slice 02: Which current mechanisms address the same historical failure modes
  and may be duplicates rather than distinct components?
- Slice 02: Does the `workbench/<DATE>-audit-*.md` convention belong to a
  code-audit component, or should all durable task artifacts move to
  slice-local planning paths when work is ledgered?
- Arc 02: Should posture and methodology remain a single conceptual component,
  or should posture, process, and verification become separately installable
  pieces with the top-level skill composing them?
- Arc 02: Which package entrypoint promises must remain stable for existing
  Claude, Codex, and source-clone users if the monolith is split?
