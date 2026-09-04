# CC Prompt: Project04 Arc07 Slice01

You are CC completing Project04 Arc07 Slice01:
`arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract`.

Project04 is in Expedited Mode. Commit your Slice01 planning packet before CDC
review, using an explicit file list for staging/commit. Include both required
commit trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Required Context

Read, in order:

1. `project04-knowledge-library-reorg/project-plan.md`
2. `project04-knowledge-library-reorg/ledger.md`
3. `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/arc-plan.md`
4. `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/ledger.md`
5. `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/slice-plan.md`
6. `project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/ledger.md`

Then inspect the live source checkout at
`/Users/oubiwann/lab/billosys/ai-engineering`.

## Mission

Produce a read-only component entrypoint contract and migration map. Do not
edit source files in this slice.

The operator surfaced these cleanup requirements:

- move root `SKILL.md` to `knowledge/collaboration-framework/`;
- update Make targets/files accordingly in a later implementation slice;
- remove stale `docs/` directory holdovers for:
  - `knowledge/agent-coordination/`;
  - `knowledge/code-auditing/`;
  - `knowledge/collaboration-framework/`;
  - `knowledge/contribution-style/`;
  - `knowledge/engineering-methods/`;
  - `knowledge/project-management/`;
- decide whether those components should instead have component-root
  `SKILL.md` entrypoints;
- migrate `knowledge/project-management/docs/pm/` to
  `knowledge/project-management/guides/`.

CDC's starting recommendation, which you should test rather than merely
repeat, is:

- `knowledge/collaboration-framework/SKILL.md` should become the canonical
  collaboration-framework entrypoint, while the generated package still exposes
  `collaboration-framework/SKILL.md`.
- Independently loadable framework components should get concise component-root
  `SKILL.md` wayfinders/contracts.
- Long current documents should usually become `guides/` material, not be
  blindly renamed to `SKILL.md`.
- Reusable forms should remain under `templates/`.
- `knowledge/project-management/docs/pm/` should become
  `knowledge/project-management/guides/`.
- Adjacent `knowledge/testing/docs/` and
  `knowledge/work-verification/templates/` should be inventoried and either
  included or excluded with explicit rationale.

## Required Artifacts

Create these files under this slice's `artifacts/` directory:

1. `current-component-layout-and-reference-map.md`
2. `component-entrypoint-decision-register.md`
3. `source-migration-impact-map.md`
4. `validation-command-inventory.md`
5. `implementation-slice-roadmap.md`

Update this slice's `ledger.md` with final statuses and attested evidence.
Create `closing-report.md` walking all six rows and bubbling findings up to
Arc07.

Do not create `cdc-verification.md`; CDC owns that.

## Required Validation

Run and record:

- source status before work;
- source status after work, confirming no source edits;
- planning `git diff --check`;
- all six Slice01 ledger verifier commands.

The artifacts should name later implementation validation gates, including:

- source `git diff --check`;
- README/docs/SKILL local-link validation;
- `make check-skills`;
- `make collab-framework`;
- `make all`;
- `make check-package-paths`;
- generated package inspection;
- isolated install smoke;
- CCDP validation disposition, even if no CCDP commands are required by the
  implementation slices.

## Commit Scope

Commit exactly the Slice01 planning packet:

```text
project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/artifacts/current-component-layout-and-reference-map.md
project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/artifacts/component-entrypoint-decision-register.md
project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/artifacts/source-migration-impact-map.md
project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/artifacts/validation-command-inventory.md
project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/artifacts/implementation-slice-roadmap.md
project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/ledger.md
project04-knowledge-library-reorg/arc07-knowledge-component-entrypoints/slice01-component-entrypoint-contract/closing-report.md
```

Suggested commit message:

```text
Complete Project04 Arc07 Slice01 component entrypoint contract
```
