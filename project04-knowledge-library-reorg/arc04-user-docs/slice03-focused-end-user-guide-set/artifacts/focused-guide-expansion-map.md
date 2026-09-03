# Focused Guide Expansion Map

focused guide expansion map for Arc04 Slice03.

Source commit: `bcfd986ca1a9078508bfb2628d574af69ddc1fe1`

## Expanded Guides

| Guide | Role now served | Source inputs |
|---|---|---|
| `docs/repository-overview.md` | Expanded orientation for top-level repository surfaces and user entrypoints. | Slice01 end-user docs decomposition, Slice02 README orientation, source `README.md`. |
| `docs/skill-library.md` | Expanded guide to current installable skill packages, source entrypoints, package/source distinction, and planned method boundary. | Slice01 decomposition, Slice02 stub register, source `Makefile`, source `knowledge/*/SKILL*.md`. |
| `docs/collaboration-framework.md` | Expanded guide to the framework composer, component source paths, and whole-framework versus narrower component use. | Slice01 decomposition, Slice02 README map, source `SKILL.md`, source framework component paths under `knowledge/`. |
| `docs/knowledge-library-anatomy.md` | Expanded guide to the `knowledge/` substrate shape, source/package roots, and current exceptions. | Slice01 decomposition, source `knowledge/` file inventory, source `Makefile` package behavior. |
| `docs/building-and-installing.md` | Expanded guide to skill package commands, validation commands, installation, CCDP commands, and generated zip handling. | Slice01 validation inventory, source `Makefile`, Slice02 source validation evidence. |
| `docs/protocols.md` | Expanded guide to CCDP source/package entrypoints and protocol distribution boundary. | Slice01 decomposition, source `protocols/ccdp/README.md`, source CCDP file inventory. |
| `docs/contributing.md` | Expanded guide to contribution routing for docs, skill material, new guide material, new skill surfaces, and protocol changes. | Slice01 decomposition, source `templates/GUIDE.md`, source `Makefile`, Slice02 README route repair evidence. |

## Expansion Outcome

All seven focused docs were expanded from minimal stubs into usable end-user
guides. The expansion explains routes and roles without copying large source
substrate from `knowledge/` or protocol chapters from `protocols/ccdp/`.
