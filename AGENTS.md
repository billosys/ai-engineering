# ai-engineering - standing session instructions

**ai-engineering**: public Billosys repository for AI-optimized engineering
skills, the collaboration framework, domain knowledge packs, and the Composite
Cognition Dispatch Protocol (CCDP). The repo is both a source tree for
framework documents and a packaging surface for installable assistant skills.

- Planning artifacts live on the dedicated `planning` branch/worktree, not on
  the implementation branch. Use `git worktree list` to locate it. If it is not
  present locally, inspect or create the canonical `.worktrees/planning`
  checkout only after confirming that the repository does not already have a
  different worktree convention. Do not recreate planning docs on `main`.
- Use the current `collaboration-framework` skill at session start. For
  planning work, read `knowledge/project-management/SKILL.md`, then
  `knowledge/project-management/guides/README.md` as the
  wayfinder, and then load the relevant
  `knowledge/project-management/guides/` files. The current canonical layout
  is `projectNN-<slug>/project-plan.md` plus project `ledger.md`,
  `arcNN-<slug>/arc-plan.md` plus arc `ledger.md`, and per-slice `slice-plan.md`,
  `ledger.md`, `cc-prompt.md`, `closing-report.md`, `cdc-verification.md`, and
  `artifacts/` for durable slice-produced artifacts unless the operator records
  an override.
- Before implementation or slice/arc closure, read the active
  `project-plan.md` from the `planning` worktree first, then the relevant
  `arc-plan.md`, slice `slice-plan.md`, and ledger files. Treat
  `closing-report.md` as proposed-done until `cdc-verification.md` or an
  equivalent independent verification artifact closes the ledger evidence.
- When changing framework or project-management documents, update each affected
  file's `Version History` section and bump its version if it has one. If a
  touched file has no local version, update the conceptually enclosing
  versioned file, at minimum the top-level `SKILL.md` for framework behavior.
- **Framework component version-history management:** each framework component
  root keeps its component version in `SKILL.md` and its component change log
  in a sibling `version-history.md`. Changes to that component's `SKILL.md`,
  `guides/`, `templates/`, or `examples/` are recorded in the sibling
  version-history file; do not add or keep component histories under `guides/`
  merely because a guide was edited.
- **Work-verification routes:** use
  `knowledge/work-verification/guides/01-ledger-discipline.md` as the primary
  ledger-discipline load path, then load the focused evidence-strength,
  row-closure, silent-drop, or independent-verification guides as needed.
  `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md` remains a
  package-local full-protocol and copyable-table support asset.
- **Testing routes:** use
  `knowledge/testing/guides/01-testing-discipline.md` as the primary testing
  load path. Load `02-coverage-hardening.md` for hard coverage-threshold work
  and `03-validation-gates.md` for repository-native test/lint/format/package
  validation gates. The old `CODE-COVERAGE.md` path is not a live route.
- **Code-auditing routes:** use
  `knowledge/code-auditing/guides/01-audit-scope-and-map.md` as the primary
  diagnosis-only audit load path. Load `02-findings-and-severity.md` for report
  and finding format, `03-scale-aware-auditing.md` for all-scale review,
  `04-modernization-synthesis.md` for evidence-backed modernization pressure,
  and `05-audit-to-hardening-handoff.md` for follow-up testing or hardening
  work. The old `CODE-AUDIT.md` path is not a live route.
- **Agent-coordination routes:** use
  `knowledge/agent-coordination/guides/01-when-to-delegate.md` as the primary
  delegation-boundary load path. Load `02-context-packets.md` for self-contained
  lookup packets, `03-result-integration.md` for parent-context evidence
  integration, and `04-anti-patterns.md` for delegation failure modes. The old
  `SUBAGENT-DELEGATION-POLICY.md` path is not a live route.
- **Contribution-style routes:** use
  `knowledge/contribution-style/guides/01-contribution-style.md` as the primary
  maintainer-facing voice and calibrated-claim guidance. Load
  `02-upstream-ticket-workflow.md` for local draft, filing, line-reference,
  blockquote-header, paste-boundary, cross-linking, and template-use mechanics.
  `knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md` remains a
  package-local authoring template, not a guide. The old
  `CONTRIBUTION-STYLE.md` path is not a live route.
- Load the relevant domain skill before writing or reviewing domain material:
  Rust, Go, Erlang/OTP, C++, JavaScript/Deno, Cobalt, Tailwind CSS, Visual
  Design, Biome, or Deno lint. Preserve source material under
  `knowledge/<domain>/sources/` as provenance; write derived guidance in the
  domain `SKILL.md` and `guides/` unless a local plan says otherwise.

## Workflow

- **Repo home:** `billosys` org, public, default branch `main`.
- **Branching:** direct-to-main is normal for this repo unless the operator
  asks for a branch, PR, or separate worktree. Keep planning work on the
  `planning` worktree and implementation/release changes on `main`.
- **Compatibility instructions:** keep `CLAUDE.md` as a symlink to `AGENTS.md`
  for tools that still look for the older filename. Edit `AGENTS.md`, not the
  symlink target via a separate copy.
- **Commit footer convention (operator override, 2026-08-07):** every future
  assistant-authored commit message includes these trailers:
  `Co-authored-by: Codex <noreply@openai.com>` and
  `Co-authored-by: Billo AI <ai-engineering@billo.systems>`.
- **Build entrypoint:** start with `make help`. Use Make-backed targets instead
  of hand-running packaging scripts when a target exists.
- **Skill packaging:** `make all` builds every zip; `make collab-framework`
  builds the framework bundle; `make skills` builds the per-domain bundles;
  `make install` installs into `$(HOME)/.agents/skills` unless `INSTALL_DIR`
  is overridden. Generated zips land under `target/skills/`; `target/` and
  `build/` are ignored release artifacts, not ordinary source changes.
- **Validation:** run `make check-skills` after any `SKILL.md` description or
  packaged-skill metadata change. Run `make check-package-paths` after changing
  packaged Markdown links, bundle contents, `Makefile` packaging lists, or
  `assets/packaging/path-exceptions.tsv`. The package-path gate may report
  accepted warnings; hard failures must be fixed or explicitly dispositioned.
- **Packaging lists:** when adding, removing, or renaming a skill or bundled
  document, update the relevant `Makefile` lists/targets, README skill-library
  documentation, and package-path exceptions in the same slice.
- **CCDP:** source chapters live under `protocols/ccdp/src/`; the assembled
  protocol is `protocols/ccdp/composite-cognition-dispatch-protocol.md`. Use
  `make ccdp` from the repo root, or `make ccdp-rfc-strict` inside
  `protocols/ccdp`, before treating protocol edits as complete.
- **Ignored workbench outputs:** `workbench/` is ignored. For intended release
  notes, review packets, or durable analysis artifacts, inspect them directly
  and use `git add -f` only for the specific file(s) the operator wants
  committed.
