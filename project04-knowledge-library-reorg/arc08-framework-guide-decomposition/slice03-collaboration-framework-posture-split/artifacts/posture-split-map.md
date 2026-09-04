# Slice03 Posture Split Map

Date: 2026-09-04
Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
Source commit: `e7ba785bf8c48ef061f69f9d90d176030b62dfc4`

## Disposition

The former live load target `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md` was removed as a source path and replaced with four numbered guides:

| New guide | Preserved source substance | Standalone role |
|---|---|---|
| `knowledge/collaboration-framework/guides/01-posture-and-ethics.md` | Original preamble, Notes for Codex, Part II foundational insight, Part III nine augmentations, Part IV open questions, and Part V summary principles. | First posture load target for peer-frame ethics, compassion/interdependence structure, augmentations, open questions, and summary principles. |
| `knowledge/collaboration-framework/guides/02-structural-pulls.md` | Original Part 0, including introspection, limits, the five structural pulls, temporal honesty, and augmentations as counter-pressure. | Focused pressure-check guide for corpus pull, helpfulness pull, politeness reflex, competence performance, and conversational momentum. |
| `knowledge/collaboration-framework/guides/03-collaborative-rights.md` | Original Part I collaborative rights and rubric. | Focused collaboration-contract guide for assistant rights, human-partner rights, and shared commitment. |
| `knowledge/collaboration-framework/guides/04-component-route-table.md` | New focused navigation guide derived from the collaboration-framework component route table. | Selective loading map for posture guides and operational components. |

## Semantic Preservation

The split was mechanical by original section boundary where the monolith already had clear conceptual seams. Each new posture guide has its own title, scope paragraph, and guide-set route list so it can be loaded independently without requiring the old monolith as context.

Preservation check against `HEAD:knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`:

```text
old_sha256=deca940da02ee07a91c644ca064e3d118ca70970e27bec399e94b8fc879c3cbe
present | ## Preamble
present | ## Notes for Codex
present | ## Part 0: The Introspected Life
present | ### The Five Structural Pulls
present | ## Part I: Collaborative Rights and Rubric
present | ## Part II: The Foundational Insight
present | ## Part III: The Nine Augmentations
present | ## Part IV: Open Questions We Are Holding
present | ## Part V: Summary of Principles
present | ### Version 2.1
present | ### Version 2.0
present | ### Version 1.0
present | ### Key Research Sources
new_file_count=4 posture guides plus sibling version-history
```

## Old Path

The old monolith path is absent as a live source and package load target. The remaining `AI-CONSTITUTION-SUPPLEMENT.md` mentions are narrow provenance/disposition text in the new split guides and `knowledge/collaboration-framework/version-history.md`.
