# Source-to-Concept Map

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice01-source-inventory
status: proposed-done
candidate-breakout-labels: non-final, not final component boundaries, for later analysis
```

## Map

Field markers for ledger verification:

- Source path: each row names an actual source path from the implementation
  checkout or the Project01 planning close set.
- Concept: each row names the framework concept visible at that source path.
- Discipline: each row names the operational discipline carried by the concept.
- Candidate breakout label: every label is non-final and for later analysis.

| Source path | Concept | Discipline | Candidate breakout label |
|-------------|---------|------------|--------------------------|
| `/Users/oubiwann/lab/billosys/ai-engineering/README.md` | Repository discovery and skill-bundle distribution | Human entrypoint, command discovery, source/package distinction | `repository-orientation-and-distribution` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/README.md` | CCDP as separate protocol distribution | Avoid treating `ccdp.zip` as a skill zip; route package readers to package-local README | `protocol-distribution-guidance` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md` | Collaboration-framework runtime entrypoint | Load-order routing, top-level composition, domain-skill exclusion | `framework-entrypoint-and-routing` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md` | Notes for Codex | Adapts framework terms to Codex and records mandatory PM loading | `agent-adapter-and-routing` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-CONSTITUTION-SUPPLEMENT.md` | AI collaboration rights and posture | User sovereignty, honest challenge, compassion, structural pressure awareness | `collaborative-posture-and-ethics` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-CONSTITUTION-SUPPLEMENT.md` | Nine augmentations | Practical posture checks against unhelpful assistant behavior | `collaborative-posture-and-ethics` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-ENGINEERING-METHODOLOGY.md` | Three pillars | Knowledge substrate, collaborative posture, process rigour | `engineering-methodology-and-process` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-ENGINEERING-METHODOLOGY.md` | 9-point SDLC and anti-degradation | Systematic implementation and quality floor maintenance | `engineering-methodology-and-process` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-ENGINEERING-METHODOLOGY.md` | Verification and evidence | Separate implementation claims from audit and verification claims | `verification-methodology` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md` | PM wayfinder | Mandatory routing before planning or closing | `project-management-wayfinder` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/01-scales-of-work.md` | Project/arc/slice/step/iteration scale model | Keep work units and repair loops distinct | `project-management-scale-model` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/02-canonical-planning-worktree.md` | Canonical planning worktree | Separate planning branch/worktree from implementation source | `planning-worktree-and-layout` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/03-planning-top-down.md` | Top-down open sets | Create project, arc, slice, and ledger records before execution | `planning-open-set-mechanics` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/04-closing-slices.md` | Slice close and bubble-up | Artifact inventory, ledger walk, silent-drop check, parent handoff | `slice-close-and-bubble-up` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/05-closing-arcs.md` | Arc/project composition close | Recompose verified child evidence at parent scale | `arc-project-composition-close` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/06-confirmation-protocol.md` | Path/layout confirmation | Ask before creating ambiguous planning paths | `planning-confirmation-protocol` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/07-anti-patterns.md` | Planning anti-patterns | Refuse root workbench/reports/scratch planning artifacts and implementation-doc planning trees | `planning-anti-patterns-and-repair` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/08-maintenance.md` | PM document maintenance | Keep split PM files and wayfinder synchronized | `framework-maintenance-discipline` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/09-worked-example-odm.md` | Worked planning example | Concrete project-to-slice sequencing example | `project-management-examples` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/version-history.md` | PM path-rule history | Preserves why planning moved to `.worktrees/planning` and why artifact homes changed | `project-management-provenance` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/templates/LEDGER-DISCIPLINE.md` | Ledger row closure | Evidence strengths, closer/verifier split, per-row verification | `ledger-verification-protocol` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/templates/LEDGER-DISCIPLINE.md` | Artifact placement in ledgered work | Durable slice outputs default to owning slice `artifacts/` unless overridden | `ledger-verification-protocol` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/CODE-AUDIT.md` | CAP-style code audit | Multi-scale source audit with finding IDs and severity discipline | `code-audit-discipline` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/CODE-AUDIT.md` | Modernization synthesis | Modernization follows observed defects and structural pressure | `evidence-backed-modernization` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/CLAUDE-CODE-COVERAGE.md` | Coverage hardening loop | Keep iterating until coverage and quality gates are actually met | `coverage-hardening-discipline` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/CLAUDE-CODE-COVERAGE.md` | Root-cause test repair | Fix failing tests by understanding the failure path, not by weakening checks | `coverage-hardening-discipline` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/SUBAGENT-DELEGATION-POLICY.md` | Subagent boundary | Main agent keeps thinking and judgment; subagents may assist lookup | `delegation-policy` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/docs/CONTRIBUTION-STYLE.md` | Upstream contribution voice | Specific, respectful, evidence-bounded maintainer communication | `contribution-style-and-voice` (non-final) |
| `/Users/oubiwann/lab/billosys/ai-engineering/templates/CONTRIBUTION-TICKET.md` | Contribution-ticket structure | Header block, evidence body, shapes for bug/feature/docs/design question | `contribution-ticket-template` (non-final) |
| `.worktrees/planning/project01-harmonise-paths/closing-report.md` | Project01 accepted source/package contract | Project02 must preserve release-surface distinctions and package validators | `path-contract-constraints` (non-final) |

## Candidate Cluster Notes

These clusters are candidate, non-final, and for later analysis:

- `posture`: Constitution supplement plus posture parts of the methodology.
- `methodology`: methodology process material plus audit/coverage principles.
- `project-management`: PM wayfinder, split PM files, and planning examples.
- `ledger`: ledger discipline plus verification concepts in methodology and PM
  close files.
- `specialized-operational-guides`: code audit, coverage, delegation, and
  contribution guides/templates.
- `distribution-entrypoints`: README, SKILL entrypoint, package semantics, and
  Project01 path/package constraints.

## Open Questions

- Slice 02 problem-solution map: Which historical failure mode required each
  concept, and which concepts are solving the same failure more than once?
- Slice 02 problem-solution map: Does `CODE-AUDIT.md` belong with methodology,
  or does its diagnosis-only workflow justify a standalone component?
- Slice 02 problem-solution map: Is coverage hardening a general methodology
  guide, a testing component, or a language-guided overlay?
- Arc 02 operator discussion: Should the final breakout optimize for runtime
  loading, human maintainability, package boundaries, or all three with a thin
  top-level composer?
- Arc 02 decision needed: Which legacy entrypoint and package path promises are
  compatibility constraints rather than implementation details?
