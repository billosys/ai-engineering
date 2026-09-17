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
  `ledger.md`, `cc-prompt.md`, `closing-report.md`, workflow-specific
  verification records, and
  `artifacts/` for durable slice-produced artifacts unless the operator records
  an override. Preserve existing `cdc-verification.md` records and project
  conventions under the planning guide's verification filename compatibility
  rule; do not rename historical records or leave competing current verdicts.
  Slice records are `cdc-verification.md` by default and `crc-verification.md`
  with three contributors; three-contributor arc/project closure requires both
  CRC and CDC records under the per-scale record contract.
- Default to the Two-Contributor Workflow (CDC + CC). Enable the
  Three-Contributor Workflow (CDC + CRC + CC) only on explicit Operator request,
  recorded with scope, role assignments, and authority in the canonical plan.
  Follow `knowledge/engineering-methods/guides/01-engineering-methodology.md`.
  CRC escalates structural changes via `crc-escalationNN.md`; CDC returns
  `cdc-directiveNN.md`, both relayed by the Operator and preserved under the
  planning guide's design handoff contract. Neither workflow permits
  self-acceptance or silent changes to the agreed contract.
- The Operator may explicitly select the One-Contributor Workflow for bounded
  single-assistant work. Use proportionate self-checks and a completion report,
  not fictional role handoffs or new planning trees solely for the workflow.
  Existing ledgered work and independent/Operator gates remain binding; do not
  present the sole contributor's self-review as independent verification.
- Preserve issued slice prompts. Keep the initial `cc-prompt.md` and every
  follow-up `cc-prompt-iterationNN.md` in the slice root, never in `artifacts/`.
  Record the current assignment and prior handoffs in `slice-plan.md`; follow
  `knowledge/project-management/guides/03-planning-top-down.md` for iteration
  handoff and execution. Supporting-artifact overrides do not change prompt
  placement.
- Before implementation or slice/arc closure, read the active
  `project-plan.md` from the `planning` worktree first, then the relevant
  `arc-plan.md`, slice `slice-plan.md`, and ledger files. Treat
  `closing-report.md` as proposed-done until the required workflow-specific
  records, a recorded legacy path, or an
  equivalent independent verification artifact closes the ledger evidence.
- **Skill versioning:** follow the repository-wide contract below for every
  skill, including domain/tooling skills, framework components and composers,
  and method skills. Guides and templates do not have independent versions.
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

## Skill version and history contract (repository maintenance only)

This is how ai-engineering maintains its own skills. Keep these maintenance
instructions in `AGENTS.md`; do not copy them into distributed skills, guides,
templates, or end-user documentation. They supersede older per-document or
framework-only versioning instructions and examples. Historical plans and
existing nonconforming files are evidence, not exceptions to this contract.

- **One authority:** a skill's current version has exactly one authoritative
  value, `metadata.version` in the YAML frontmatter of its own `SKILL.md`.
  Write it as the `version` string inside the `metadata` mapping. Read that
  value before an update. Neither a history heading, prose label, Git release
  tag, nor another skill's version determines this skill's current version.
  Do not add a top-level `version`, a literal dotted YAML key named
  `metadata.version`, or another version authority.
- **Why the nesting matters (confirmed 2026-09-06):** the installed
  skill-creator validator, `~/.codex/skills/.system/skill-creator/scripts/quick_validate.py`,
  permits only `name`, `description`, `license`, `allowed-tools`, and `metadata`
  at the frontmatter's top level. It rejects top-level `version` and accepts
  `version` inside `metadata`. The nesting is a compatibility requirement, not
  evidence of multiple versions; do not flatten it merely because there is one
  version. Keep other custom fields inside `metadata` too. Recheck the actual
  validator before revising this convention; our own gate must not enforce a
  schema that the skill-creator validator rejects.
- **One history:** each skill has exactly one `version-history.md`, sibling to
  its `SKILL.md`. That file records significant changes across the whole skill
  directory: the entrypoint, guides, templates, examples, and any other owned
  material. It is the change record, not the authority for the current version.
  Include an entry matching the current metadata version and retain previous
  entries; do not infer the current version from ordering or the largest number.
  Do not keep additional history files or embedded change-history sections in
  the entrypoint or descendants. A link to the sibling history is sufficient.
- **One version sequence per skill:** record significant changes under the
  owning skill's version, including changes confined to a guide or template.
  Update the metadata and corresponding history entry together when bumping
  the skill version. Do not continue independent guide/template version
  sequences or automatically bump the collaboration-framework composer for
  every component edit; assess each affected skill's own change.
- **No duplicate skill version numbers:** current and previous skill version
  numbers may appear only in the owning entrypoint's version metadata and its
  sibling history. Do not repeat them in entrypoint prose, headings, footers,
  badges, filenames, directory names, guides, templates, examples, or other
  skill files. Generated packages must preserve this rule; synchronizing a
  duplicate from metadata does not make the duplicate permissible.
- **Preserve the distinction from subject matter:** language, dependency,
  tool, protocol, specification, and example-project versions are not skill
  versions. Preserve those references and upstream source provenance. Actual
  project/arc/slice plan histories and CCDP's own protocol history are separate
  from this skill contract. Preserve former local-document histories as
  explicitly retired lineage in the sibling history, not as live version
  sequences; do not invent mappings to skill releases without evidence.
- **Reconciliation:** when retiring competing skill/document version
  sequences, use the highest existing version from the entrypoint and sibling
  history (including local-document history moved there). Compare numeric
  components, not strings or decimal numbers; normalize omitted minor/micro
  components to zero. Preserve the old records with their original provenance.
- **Bump guidance:** use semantic `major.minor.micro` versions. Increment major
  for incompatible changes, minor for compatible new capabilities or guidance,
  and micro for compatible corrections or clarifications. Reset lower
  components when incrementing a higher one. Use judgment about significance
  and grouping; no rigid per-edit or per-commit bump cadence is required.
- **Establish ownership before editing:** identify the owning skill entrypoint
  and sibling history. Existing `SKILL-*.md` variants are skills too; sharing
  a source directory or shipping inside a composite does not exempt them.
  A shared directory with multiple entrypoints needs an explicit ownership and
  history migration decision, not an inferred shared skill version. Packaging
  copies do not create independent version authorities.
- **Shared-root deferral (operator decision, 2026-09-06):** keep the existing
  Biome source directory and guide sharing unchanged until the operator revisits
  skill-root design. Its sibling `version-history.md` has separate
  `## Skill: biome-js-linter` and `## Skill: biome-linter` sections, each with
  its own version entries matching its entrypoint. Record shared-guide changes
  in every affected skill's section. This is not a shared version sequence or
  a general exception allowing new shared roots.
- **Verify the whole contract:** for each affected skill, check the metadata,
  sibling history, and entire owned tree for additional histories, live local
  version sequences, and duplicate skill-version labels. Check packaged output
  too when packaging is affected. Description-length and Markdown-path checks
  alone do not establish version-contract compliance. Report existing gaps
  explicitly rather than treating the current layout as a compliant template.
  Run `make test-skill-versions` for checker changes and
  `make check-skill-versions` for source plus freshly generated package checks.
  `make check-package-paths` includes the version gate. The checker recognizes
  explicit skill/document version declarations; reviewers must still distinguish
  subject-matter references from disguised or ambiguous skill-version prose.

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
