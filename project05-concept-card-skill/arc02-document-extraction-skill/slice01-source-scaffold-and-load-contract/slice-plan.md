# Slice01 Plan: Source Scaffold And Load Contract

```yaml
project: project05-concept-card-skill
arc: arc02-document-extraction-skill
slice: slice01-source-scaffold-and-load-contract
status: open
opened: 2026-09-06
artifact-home: none expected
```

## Goal

Create the live `document-extraction` source scaffold and the core contracts
that later Arc02 slices will deepen: skill entrypoint, version history, load
contract, workflow guide, and output contract.

## In Scope

- Create `knowledge/document-extraction/`.
- Add `SKILL.md` with frontmatter `name: document-extraction`, concise
  description, positive triggers, negative triggers, ownership boundary,
  routing to `concept-cards`, guide map, and version-history pointer.
- Add sibling `version-history.md`.
- Add `guides/01-load-contract.md`.
- Add `guides/02-workflow.md` covering human-assisted and agent-direct flow.
- Add `guides/03-output-contract.md` covering prepared Markdown, structure
  maps, locators, media references, manifests, readiness reports, and caveats.
- Preserve the standalone nature of the skill: indexing, reading, source
  review, analysis, and concept-card inputs are all valid downstream uses.
- Keep PDF/EPUB/HTML/converter-specific deep guidance for later Arc02 slices,
  but route to the future guide names from the entrypoint when useful.

## Out Of Scope

- Detailed PDF/Marker and EPUB/pandoc procedural guides.
- Detailed HTML/converted-Markdown, media normalization, structure splitting,
  locator, validation, readiness, and caveat guides beyond the core output
  contract.
- Templates and examples.
- Makefile targets, docs/skill-library entries, generated zips, install
  smoke, or release notes.
- Creating `knowledge/source-preparation/`.
- Creating or editing `knowledge/concept-cards/`.

## Durable Artifacts

No planning artifacts are expected beyond the slice close set. Source files
created in `knowledge/document-extraction/` are the implementation output.

## Verification Approach

Use direct source inspection and focused validation:

- confirm source checkout status before edits;
- inspect the new files after edits;
- run `scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md`;
- run `git diff --check` in the source checkout;
- confirm the planning checkout receives only Slice01 ledger and close-report
  updates;
- do not run package gates unless this slice changes package machinery.

## Exit Criteria

- `knowledge/document-extraction/SKILL.md` exists and describes the correct
  standalone skill.
- `knowledge/document-extraction/version-history.md` exists.
- `guides/01-load-contract.md`, `guides/02-workflow.md`, and
  `guides/03-output-contract.md` exist.
- The scaffold names future PDF, EPUB, HTML/converted Markdown, media,
  structure, locator, validation/readiness, and template/example work without
  claiming those later files already exist.
- No superseded `knowledge/source-preparation/` root is created.
