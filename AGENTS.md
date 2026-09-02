# ai-engineering planning - standing session instructions

**ai-engineering planning**: the dedicated planning branch/worktree for the
Billosys AI Engineering repository. This worktree stores project, arc, slice,
ledger, prompt, closing, verification, and planning-analysis artifacts. It is
not the implementation checkout and should not be used for source/package edits.

- This branch is the planning source of truth. Do not recreate these planning
  docs on `main`, and do not move implementation/release artifacts into this
  worktree unless a plan explicitly defines them as planning evidence.
- The implementation/source checkout is
  `<git-clone-path>/billosys/ai-engineering` on `main`. Read source files
  from that checkout when a plan needs evidence; make source, packaging,
  README, protocol, and release-note edits there unless the operator says
  otherwise.
- Use the current `collaboration-framework` skill at session start. Because
  this orphan planning branch does not carry the framework source docs, load
  them from the installed skill or from the main checkout. For planning work,
  read `docs/PROJECT-MANAGEMENT.md` as the wayfinder and then load the
  relevant `docs/pm/` files before creating or closing project, arc, or slice
  artifacts.
- The current canonical layout is
  `projectNN-<slug>/project-plan.md` plus project `ledger.md`,
  `arcNN-<slug>/arc-plan.md` plus arc `ledger.md`, and per-slice
  `slice-plan.md`, `ledger.md`, `cc-prompt.md`, `closing-report.md`,
  `cdc-verification.md`, and `artifacts/` for durable slice-produced
  artifacts unless the operator records an override.
- Slice-generated durable artifacts default to that slice's `artifacts/`
  directory. Planning-analysis artifacts that predate the default may live as
  named files in the slice directory; do not relocate historical evidence
  unless the operator asks.
- Treat `closing-report.md` as proposed-done until `cdc-verification.md` or an
  equivalent independent verification artifact closes the ledger evidence.
  Project and arc closure require composition checks against their own
  `ledger.md` files, not just all child slices being green.

## Workflow

- **Repo home:** `billosys` org, public, default implementation branch `main`;
  dedicated planning branch `planning`.
- **Worktree identity:** this checkout should report branch `planning`. Use
  `git worktree list` before assuming paths, and use `git -C
  <git-clone-path>/billosys/ai-engineering ...` for implementation-branch
  Git commands.
- **Compatibility instructions:** keep `CLAUDE.md` as a symlink to `AGENTS.md`
  for tools that still look for the older filename. Edit `AGENTS.md`, not the
  symlink target via a separate copy.
- **Commit footer convention (operator override, 2026-08-07):** every future
  assistant-authored commit message includes these trailers:
  `Co-authored-by: Codex <noreply@openai.com>` and
  `Co-authored-by: Billo AI <ai-engineering@billo.systems>`.
- **Plan first, implement elsewhere:** write `slice-plan.md`, `ledger.md`, and
  `cc-prompt.md` here; implement source changes in the main checkout after the
  operator accepts the slice prompt.
- **Versioning source docs:** if a plan changes framework or
  project-management source docs, the implementation slice must update each
  affected file's `Version History` section and bump its version if it has one.
  If a touched file has no local version, update the conceptually enclosing
  versioned file, at minimum the top-level `SKILL.md` for framework behavior.
- **Evidence discipline:** preserve command outputs, audits, synthesis reports,
  and other durable evidence in the owning slice directory, preferably under
  `artifacts/`. Every ledger row needs an evidence pointer with a strength
  claim; do not close by summary alone.
- **Project ordering:** as of 2026-09-01, `project01-harmonise-paths` and
  `project03-concept-card-method` are closed. `project02-collab-breakout` is
  ready for project-level closure and/or explicit source implementation
  authorization. `project04-knowledge-library-reorg` is planned for the
  docs/knowledge-library reorganization.
- **Project01 status:** closed; Arc 01, Arc 02, Arc 03, and Arc 04 are closed
  with Project 01 DoD verdict met.
- **Project02 status:** Arc 01 through Arc 05 are closed/composed with a
  source implementation roadmap, validation matrix, acceptance gates, and
  implementation handoff packet. The project is ready for project-level closure
  and/or explicit source implementation authorization.
- **Project03 status:** closed; Arc 01 through Arc 05 are closed with the
  Project03 DoD verdict met.
- **Project04 status:** active and operating in Expedited Mode as of
  2026-09-02. Arc01 `arc01-material-inventory` is closed. Arc02
  `arc02-directory-contract` is active; Slice01
  `slice01-decision-surface-inventory` and Slice02
  `slice02-accepted-directory-contract` are verified-closed, and Slice03
  `slice03-migration-validation-plan` is open for CC. In Expedited Mode, CC and
  CDC both commit their own changes with explicit commit scope; after each
  slice closes, immediately open the next slice and report the relative
  `cc-prompt.md` path. No source edits, file moves, README rewrites, package
  updates, or generated artifacts are authorized by Arc01 or Arc02 planning
  unless a later implementation arc explicitly says so.
- **Source checkout validation references:** implementation plans may require
  `make help`, `make check-skills`, `make check-package-paths`, `make all`,
  `make collab-framework`, or `make ccdp` in the main checkout. Record these
  as source-checkout commands; do not expect this planning branch to contain
  the Makefile or source tree.
- **CCDP planning:** CCDP source lives in the main checkout under
  `protocols/ccdp/src/`, and the assembled protocol lives at
  `protocols/ccdp/composite-cognition-dispatch-protocol.md`. Plans that touch
  CCDP should require `make ccdp` from the main checkout or
  `make ccdp-rfc-strict` inside `protocols/ccdp`.
