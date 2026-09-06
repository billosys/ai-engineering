# Slice04 Plan: Templates And Examples

```yaml
project: project05-concept-card-skill
arc: arc02-document-extraction-skill
slice: slice04-templates-and-examples
status: open
opened: 2026-09-06
depends-on:
  - slice01-source-scaffold-and-load-contract
  - slice02-format-preparation-guides
  - slice03-structure-media-locators-and-reports
```

## Goal

Add sibling `templates/` and `examples/` support surfaces that make the
`document-extraction` skill usable for human-assisted and agent-direct
workflows. The support files must preserve the skill's standalone purpose while
also making downstream `concept-cards` handoff provenance clear.

## Scope

In scope:

- add sibling `knowledge/document-extraction/templates/` files for the core
  preparation outputs: manifest, structure map, media records, locator records,
  validation/readiness report, caveat records, and downstream concept-card
  handoff;
- add a non-executable per-extraction helper-script template as a Markdown
  template, informed by the operator-surfaced historical Neo-Riemannian helper
  scripts but not copied from them as canonical code;
- add sibling `knowledge/document-extraction/examples/` files showing worked
  or representative PDF/Marker, EPUB/pandoc, HTML/converted-Markdown, and
  downstream concept-card handoff records;
- update `knowledge/document-extraction/SKILL.md` so templates/examples are
  live source routes while package/install wiring remains future Arc05 work;
- update caller text in `knowledge/document-extraction/guides/01-load-contract.md`,
  `guides/04-pdf-source-preparation.md`, and
  `guides/05-epub-source-preparation.md` so shared reporting is no longer
  grouped with later templates/examples;
- inspect and update `guides/03-output-contract.md` and
  `guides/10-validation-and-reports.md` only where needed to route to the new
  templates/examples accurately;
- update `knowledge/document-extraction/version-history.md` and
  `metadata.version` in `SKILL.md` under the current source version contract.

Out of scope:

- adding executable conversion, splitting, validation, or helper scripts;
- adding package, Makefile, README, docs, generated zip, or install wiring;
  those remain Arc05;
- implementing `concept-cards`;
- recreating `source-preparation`;
- moving support material under `guides/` for packaging convenience.

## Required Design Pressure

Templates should be fillable records, not vague checklists. Examples should
demonstrate the records with realistic but non-source-specific values and make
uncertainty visible instead of presenting polished false certainty.

The per-extraction helper-script template must be a Markdown template for
creating source-specific helpers when needed. It should require source identity,
input/output paths, boundary rules, media rewrite rules, dry-run/report mode,
idempotence/regeneration behavior, validation checks, and caveat output. It
must warn against hard-coded assumptions becoming canonical behavior.

## Exit Criteria

Slice04 is complete when:

- sibling `templates/` and `examples/` directories exist under
  `knowledge/document-extraction/`;
- templates cover manifests, structure maps, media records, locator records,
  validation/readiness reports, caveat records, downstream concept-card
  handoffs, and per-extraction helper-script planning;
- examples cover PDF/Marker, EPUB/pandoc, HTML/converted Markdown, and
  downstream concept-card handoff use;
- entrypoint and guide routes to templates/examples are live and local links
  resolve;
- residual Slice03 caller-text cleanup is completed in the authorized guide
  files;
- version metadata and sibling history are updated with no guide-local version
  history;
- focused validators pass;
- source status is inspected before editing and after commit, and unrelated
  work remains excluded.

## Expected Artifacts

No separate durable planning artifacts are expected. Implementation output is
the source files listed above. Durable close evidence belongs in this slice's
`closing-report.md`, `ledger.md`, and later `cdc-verification.md`.
