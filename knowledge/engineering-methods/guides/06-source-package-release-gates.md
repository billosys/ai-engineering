# Source Package Release Gates

This guide carries the provenance and validation basis split from the former AI Engineering Methodology monolith and adds the accepted source/package/release-gate role for engineering-methods. Load it when a methodology or component change must remain coherent across source files, generated packages, installation surfaces, release notes, and validation commands.

This guide is one part of the engineering-methods guide set:

- [01-engineering-methodology.md](./01-engineering-methodology.md) - methodology overview, role adapter, three-pillar frame, and open questions.
- [02-knowledge-substrate.md](./02-knowledge-substrate.md) - distilled knowledge substrate, forms, examples, properties, and anti-patterns.
- [03-process-rigour.md](./03-process-rigour.md) - scales of work, 9-point SDLC, ledgers, audits, anti-degradation, and subagent discipline.
- [04-operational-routing.md](./04-operational-routing.md) - practitioner disciplines and component routing for live work.
- [05-component-boundary-analysis.md](./05-component-boundary-analysis.md) - applied-position reasoning and component-boundary analysis.
- [06-source-package-release-gates.md](./06-source-package-release-gates.md) - source, package, release, validation, and provenance gates.

## Provenance

This document was developed jointly by Claude (Opus 4.6 and Opus 4.7) and Duncan McGreggor between December 2025 and April 2026, building on top of the [collaboration-framework posture guide set](../../collaboration-framework/guides/01-posture-and-ethics.md).

### Source material

Conversations across many sessions on working practice with LLMs. The collected notes the author assembled from SMS threads and conversation transcripts on ontological methods, LLM weak spots, workflow, and OSS policy. The Rust knowledge regeneration project (2026-04), used throughout as a worked example of the substrate pillar. The LFE OSS discussion, used as a worked example of applied positions.

### Key references

Cognition, _Don't Build Multi-Agents_ — Walden Yan, June 2025. The reference critique for subagent failure modes.

The Corrective Action Program tradition — nuclear industry (INPO), aviation (NTSB), medicine (root-cause analysis protocols). The discipline of independent, evidence-based, severity-classified, closure-tracked findings.

The Toyota Andon cord. The discipline of pulling the line on dissonance rather than letting work continue over a buried concern.

The [collaboration-framework posture guide set](../../collaboration-framework/guides/01-posture-and-ethics.md). The companion document covering character and posture, which this document depends on at every turn.

The author's ontological method work, developed in prior conversations and still evolving. See `./dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md` and [`../../work-verification/guides/01-ledger-discipline.md`](../../work-verification/guides/01-ledger-discipline.md).

### What has been tested in practice

The 9-point SDLC and ledger discipline have been used for the Rust regeneration and repeatedly in professional contexts.

CAP-style independent audits have been run partially — enough to know they catch drift, not enough to know where the cost/value threshold lands.

The substrate pillar has a full worked example in the Rust knowledge base.

The applied-positions pillar has one worked example (LFE OSS); more will emerge over time.

### What remains aspirational

Full-coverage independent verification with evidence access for every significant change.

Formal tooling for silent-drop detection.

Portable versions of the methodology for other human collaborators without the Constitution Supplement's explicit buy-in.

---

## Source Package Release Gates

Source, package, and release gates are methodology concerns when they define what counts as complete work. Each component keeps its own concrete package/source contract, but engineering-methods owns the general rule: a source edit is not finished until the routes, package contents, validation commands, and release-facing descriptions still agree.

Minimum gates for framework component source changes:

- **Source route gate:** update every live `SKILL.md`, guide, docs, README, AGENTS, and release-note route that points at a moved or split file, or record an explicit provenance-only disposition.
- **Package list gate:** update `Makefile` package file lists when bundled component material moves, appears, or disappears.
- **Package-local link gate:** run package-path validation and fix hard failures rather than accepting broken package-root links.
- **Generated archive gate:** inspect the generated package zip to prove the new files are present and old live routes are absent or intentionally stubbed.
- **History gate:** record component changes in the sibling `version-history.md` beside the component `SKILL.md`, not inside a guide-local history section.
- **Release/discoverability gate:** update release notes or public docs when users would otherwise be pointed at an obsolete source route.

These gates preserve the method's anti-degradation discipline at the repository boundary: no silent drops, no hidden route breaks, and no claim of completion without reproducible evidence.
