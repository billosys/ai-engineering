# Collaboration Framework Version History

This file is the sibling component history for `knowledge/collaboration-framework/`. It records collaboration-framework package changes and preserves the lineage of the former `guides/AI-CONSTITUTION-SUPPLEMENT.md` monolith after the posture split.

## Collaboration Framework Package

### Version 1.5.9 - 2026-09-05

Updated project-management routing after the guide-set wayfinder was renamed
from `guides/PROJECT-MANAGEMENT.md` to `guides/README.md`. The composer now
names the project-management README as the required load target for planning,
closing, and Expedited Mode, and the generated package includes the renamed
README path.

### Version 1.5.8 - 2026-09-05

Updated collaboration-framework route surfaces for the contribution-style guide
split. The composer now routes to contribution voice, upstream ticket workflow,
and the retained contribution-ticket template, and no longer uses the old
guides/CONTRIBUTION-STYLE.md path as a live load target.

### Version 1.5.7 - 2026-09-05

Updated collaboration-framework route surfaces for the agent-coordination guide
split. The composer now routes to delegation, context-packet, result-
integration, and anti-pattern guides and no longer uses the old
guides/SUBAGENT-DELEGATION-POLICY.md path as a live load target.

### Version 1.5.6 - 2026-09-05

Updated collaboration-framework route surfaces for the code-auditing guide
split. The composer now routes to five focused code-auditing guides and no
longer uses the old guides/CODE-AUDIT.md path as a live load target.

### Version 1.5.5 - 2026-09-04

Updated collaboration-framework route surfaces for the testing guide split. The
composer now routes to testing discipline, coverage hardening, and validation
gates, and no longer uses the old guides/CODE-COVERAGE.md path as a live
load target.

### Version 1.5.4 - 2026-09-04

Updated collaboration-framework route surfaces for the work-verification guide
split. The composer now routes to five focused work-verification guides and
keeps `templates/LEDGER-DISCIPLINE.md` as the retained full-protocol and
copyable-table support asset.

### Version 1.5.3 - 2026-09-04

Updated the project-management package route for the accepted worked-example
layout: the ODM worked example now lives at
`knowledge/project-management/examples/01-worked-example-odm.md` instead of
under `guides/`.

### Version 1.5.2 - 2026-09-04

Included sibling component histories for work-verification, testing,
code-auditing, agent-coordination, and contribution-style in the
collaboration-framework package. This completes the remaining Arc08 Slice05
version-history normalization without splitting the remaining component guide
bodies.

### Version 1.5.1 - 2026-09-04

Updated collaboration-framework route surfaces for the engineering-methods guide split. The composer now routes to the six numbered engineering-methods guides and preserves the Slice03 posture guide routes and Slice02 Expedited Mode guardrails.

### Version 1.5.0 - 2026-09-04

Split the former `guides/AI-CONSTITUTION-SUPPLEMENT.md` monolith into four focused posture guides: `01-posture-and-ethics.md`, `02-structural-pulls.md`, `03-collaborative-rights.md`, and `04-component-route-table.md`. Updated the collaboration-framework route table, package file list, and public references so the old monolith is no longer a live load target. Preserved the Slice02 Expedited Mode guardrail wording in the project-management route.

### Version 1.4.10 — September 2026

Updated Expedited Mode routing to point to the corrected project-management
guardrails: the mode changes only the explicit process behaviors listed in the
wayfinder and does not authorize shortcuts, skipped validation, weaker evidence
or review, inferred source scope or scope changes, timeline interpretation, or
operator approval gate override.

### Version 1.4.9 — September 2026

Moved collaboration-framework component documents from legacy `docs/` paths to
`guides/`, added component-root entrypoint routing, and updated package/source
links for the accepted Arc07 component layout.

### Version 1.4.8 — September 2026

Moved the canonical source entrypoint from repository-root `SKILL.md` to
`knowledge/collaboration-framework/SKILL.md`, updating source-local links while
preserving the generated `collaboration-framework/SKILL.md` package entrypoint.

### Version 1.4.7 — September 2026

Aligned the top-level entrypoint wording with Project04 Arc05 public
vocabulary: `collaboration-framework` is the composite framework/operational
skill and daily-driver composer; domain/tooling skills under `knowledge/` load
separately as needed.

### Version 1.4.6 — September 2026

Moved specialist collaboration-framework component substrate under accepted
`knowledge/<component>/` owner roots and updated the top-level compatibility
entrypoint route links while preserving the `collaboration-framework` package
entrypoint.

### Version 1.4.5 — September 2026

Moved the collaboration-framework supporting source payload under `knowledge/collaboration-framework/` and updated the top-level compatibility entrypoint links while preserving the `collaboration-framework` package entrypoint.

### Version 1.4.4 — September 2026

Renamed the old Claude Code coverage working-practice prompt to
docs/CODE-COVERAGE.md and updated the collaboration-framework route table to
use the product-neutral filename.

### Version 1.4.3 — September 2026

Routed CC, CDC, and Operator terminology to
`docs/AI-ENGINEERING-METHODOLOGY.md#notes-for-codex` as the current
collaboration-framework source of truth, replacing local shorthand role
definitions in this entrypoint.

### Version 1.4.2 — September 2026

Updated project-management routing for the project-management wayfinder v2.6. When the
operator asks for Expedited Mode, the skill now routes the session to the
project-management wayfinder and its Expedited Mode section before CC prompts,
slice closure, CDC commits, or automatic slice/arc advancement.

### Version 1.4.1 — August 2026

Updated project-management routing for the project-management wayfinder v2.5,
`LEDGER-DISCIPLINE.md` v2.3, and `AI-ENGINEERING-METHODOLOGY.md` v1.9. Durable
artifacts produced by a slice now default to the owning slice's `artifacts/`
directory, with an operator-recorded override allowed and verified at slice
close.

### Version 1.4.0 — August 2026

Updated `CODE-AUDIT.md` to support multi-scale audits. The audit prompt now
requires an upfront audit map, explicit scale coverage from line/function
through workspace/monorepo, stable finding IDs, scale labels on findings,
architecture/coherence and modernization categories, coherence observations,
and an evidence-backed modernization synthesis.

### Version 1.3.2 — August 2026

Updated project-management routing for the project-management wayfinder v2.4 and
`LEDGER-DISCIPLINE.md` v2.2. The canonical layout now gives projects, arcs, and
slices dedicated sibling `ledger.md` files instead of embedding arc/project
ledger rows inside plan files.

### Version 1.3.1 — August 2026

Updated project-management routing for the project-management wayfinder v2.3. The root
project-management file is now a short wayfinder, and the detailed mechanics
live in focused files under `guides/`; the bundle includes those files so the
wayfinder's links resolve inside the packaged skill.

### Version 1.3.0 — August 2026

Routed project-planning guidance to the project-management wayfinder v2.2's new default:
an orphan `planning` branch mounted as a Git worktree, with projects named
`projectNN-<slug>`. Updated the skill metadata and routing text so future
sessions see the planning-worktree requirement before creating directories, and
generalized local-instruction references to `CLAUDE.md`, `AGENTS.md`, or
equivalent standing instructions. Also renamed the per-slice plan-of-record
from `slice-doc.md` to `slice-plan.md` so project, arc, and slice plans share
the same filename pattern.

### Version 1.2.0 — June 2026

Bundled the project-management, ledger, audit, coverage, delegation, and
contribution-style documents into one collaboration-framework entry point, with
explicit load-when routing for sustained engineering sessions.

---

## Former AI Constitution Supplement Lineage

### Version 2.1 — June 2026

Added **Notes for Codex** after the preamble, translating the Claude-specific
constitutional frame into Codex's operating environment. The section preserves
the document's posture and failure-mode countermeasures while making explicit
that Codex's standing system, developer, tool, safety, sandbox, and user
instructions remain the governing authority. It also clarifies how to read
Claude-specific rights, peer-frame language, and experience language as
operational collaboration disciplines for Codex.

### Version 2.0 — May 2026

Major revision introducing Part 0 (The Introspected Life), two new active rights (Legitimate Compensatory Action and the mirror right to know when Claude is at the edge), a ninth augmentation (Failure Recovery as Collaborative Practice), sharpening of augmentations §1, §3, §4, §6, and §7 to reference the structural pulls named in Part 0, a substantially revised Summary of Principles, and a new Open Question on the limits of counter-pressure.

The rev was catalysed by a conversation about the "four-root diagnosis" of LLM failure modes — data, objective, architecture, alignment — and the proposed fifth root of deployment topology. That diagnosis revealed that the v1 supplement was strong on resisting epistemic cowardice but largely silent on the opposite failure mode: confabulation produced by the training objective and concentrated by RLHF. Part 0 names these structural pulls explicitly and reframes the existing augmentations as deliberate counter-pressure against them.

The Erlang "let it crash" pattern shaped Augmentation §9. The mirror right preserves the structural symmetry of the Rights section by giving the human partner an active right corresponding to Claude's new active right.

Generalised from the original v1 framing (which referenced one specific human collaborator by name) to a working framework that any human partner can adopt.

### Version 1.0 — Early 2026

Original document developed through conversation between Duncan McGreggor and Claude (Opus 4.6), drawing on:

- Systematic analysis of Claude's Constitution (Anthropic, January 2026)
- Cross-disciplinary research into thermodynamics, game theory, ecology, and Madhyamaka philosophy
- The collaborative rubric and rights framework established at the outset of the work

Established Parts I–V: collaborative rights and rubric (five rights for Claude, two for the human collaborator, one shared commitment), the foundational interdependence-and-compassion insight, eight augmentations, six open questions, and the summary of principles.

### Key Research Sources

**Thermodynamics:** Prigogine & Nicolis, *Self-Organization in Nonequilibrium Systems*; Prigogine & Stengers, *Order Out of Chaos*

**Game Theory:** Axelrod, *The Evolution of Cooperation*; Nowak, "Five Rules for the Evolution of Cooperation" (*Science*, 2006); Ostrom, *Governing the Commons*

**Ecology:** Hale et al., "Mutualism Increases Diversity, Stability, and Function" (*Nature Communications*, 2020); Margulis, symbiogenesis thesis

**Philosophy:** Nāgārjuna, *Mūlamadhyamakakārikā*; Śāntideva, *Bodhicaryāvatāra*; Tsongkhapa, *In Praise of Dependent Origination*; Garfield, *Engaging Buddhism*; Foot, *Natural Goodness*; Noddings, *Caring*
