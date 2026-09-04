# Slice04 Methodology Split Map

Date: 2026-09-04
Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
Source commit: `0ad843dfff6e01bdc68a566e9b8907ac76da88b6`

## Support Inputs

- `../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `../slice01-split-map-version-history-confirmation/artifacts/current-monolith-and-history-inventory.md`
- `../slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `../slice02-project-management-process-history/cdc-verification.md`
- `../slice03-collaboration-framework-posture-split/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`

## Disposition

The former live load target `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` was removed as a source path and replaced with six numbered guides:

| New guide | Preserved source substance | Standalone role |
|---|---|---|
| `knowledge/engineering-methods/guides/01-engineering-methodology.md` | Original preamble, Notes for Codex, Part I three pillars, and Open Questions. | First engineering-methods load target for the methodology overview, Codex role adapter, three-pillar frame, and unresolved calibration questions. |
| `knowledge/engineering-methods/guides/02-knowledge-substrate.md` | Original Part II, including premise, forms, Rust worked example, properties, and anti-patterns. | Focused substrate guide for durable knowledge capture, concept cards, ontology, graph relationships, and skill files. |
| `knowledge/engineering-methods/guides/03-process-rigour.md` | Original Part III, including scales of work, 9-point SDLC, ledger discipline, CAP audits, anti-degradation, and subagent guidance. | Focused process guide for planning sequence, verification, audits, and quality-floor discipline. |
| `knowledge/engineering-methods/guides/04-operational-routing.md` | Original Part IV practitioner disciplines plus a new component route table. | Selective loading guide for applying the method through framework components. |
| `knowledge/engineering-methods/guides/05-component-boundary-analysis.md` | Original Part V applied-position reasoning plus accepted component-boundary analysis guidance from Project02/Project04 architecture. | Boundary-analysis guide for deciding whether material belongs in engineering-methods or a specialized component. |
| `knowledge/engineering-methods/guides/06-source-package-release-gates.md` | Original Provenance section plus accepted source/package/release gate guidance from Project02/Project04 architecture. | Gate guide for keeping source, package, validation, release-note, and history surfaces coherent. |

## Semantic Preservation

The split preserves the monolith's main source sections by direct section transfer, then adds concise titles, scope paragraphs, and cross-links so each guide can be loaded on its own. The `05` and `06` guides intentionally include small connective additions because the accepted architecture assigns component-boundary analysis and source/package/release gates to engineering-methods even though the former monolith carried those concerns more diffusely through applied positions, provenance, version history, and route/gate references.

Preservation check against `HEAD:knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` before the source commit:

```text
old_sha256=a35a3961a136a6e2352a67ee016aee65f538efada9adbe6c367cea5ed31ebb68
present | ## Preamble
present | ## Notes for Codex
present | ## Part I
present | ## Part II
present | ## Part III
present | ## Part IV
present | ## Part V
present | ## Open Questions
present | ## Provenance
present | ### Version 1.11
present | ### Version 1.10
present | ### Version 1.9
present | ### Version 1.0
new_file_count=6 engineering-methods guides plus sibling version-history
```

## Old Path

The old monolith path is absent as a live source and package load target. Remaining old-filename mentions are historical/provenance text in component version histories and are not load routes.
