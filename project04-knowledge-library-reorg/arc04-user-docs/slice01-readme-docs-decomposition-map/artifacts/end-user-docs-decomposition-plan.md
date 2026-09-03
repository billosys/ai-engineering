# End-User Docs Decomposition Plan

Date: 2026-09-02
Slice: Arc04 Slice01 README and docs decomposition map

## end-user docs decomposition

Arc04 should turn `docs/` into focused end-user documentation about repository
materials while keeping `knowledge/` as the actual knowledge-library substrate.
The audience is a repository reader, skill user, contributor, or maintainer who
needs orientation without loading the full knowledge substrate.

## Proposed Focused Docs

| Target doc | audience | purpose | source inputs | Boundary |
| --- | --- | --- | --- | --- |
| `docs/repository-overview.md` | New reader, maintainer, contributor | Explain what the repository contains, how `README.md`, `docs/`, `knowledge/`, `protocols/`, `templates/`, and `scripts/` fit together. | Current `README.md` About, Contents, Repository layout; Arc03 close report. | Keep explanation in `docs/`; do not move source substrate. |
| `docs/skill-library.md` | Skill user choosing a package | Explain current skill library contents, installable package names, source roots, and how to navigate `knowledge/`. | README skill library, domain/tooling table, method skills section, Makefile package list. | Use provisional category language only; Arc05 owns final skill kind and topology vocabulary. |
| `docs/collaboration-framework.md` | User considering or invoking the framework | Explain the collaboration framework, components, when to use the whole composer, and where component source lives. | README collaboration framework sections, top-level `SKILL.md`, Arc03 moved roots. | Explain component use without finalizing Arc05 public taxonomy. |
| `docs/knowledge-library-anatomy.md` | Maintainer or advanced contributor | Explain `knowledge/<skill>/` anatomy, guides, concept-cards, extraction-metadata, sources, and current exceptions. | README anatomy tree, Arc01 inventory, Arc02 directory contract, post-Arc03 source tree. | Keep substrate in `knowledge/`; doc is descriptive wrapper only. |
| `docs/building-and-installing.md` | Skill user, maintainer, release operator | Explain `make all`, `make skills`, per-package targets, `make install`, `make check-skills`, `make check-package-paths`, and generated zip handling. | README Building and installing, Makefile help output, Slice06 validation evidence. | Do not change package roots or generated zips. |
| `docs/protocols.md` | Protocol reader, integration designer | Explain that CCDP is a protocol/package distribution under `protocols/ccdp`, separate from installable skills. | README CCDP section, `protocols/ccdp/README.md`, Arc03 CCDP separation evidence. | Do not fold CCDP into skill package language. |
| `docs/contributing.md` | Contributor | Explain how to propose new patterns, new domains, and doc/source changes after the reorganization. | README Contributing, `templates/GUIDE.md`, relevant component guides. | Avoid promising unimplemented method-skill surfaces. |
| `docs/ORIGINS.md` | Reader wanting history and rationale | Preserve origin narrative and repair links to moved framework materials. | Existing `docs/ORIGINS.md`; Arc03 moved paths. | Remain historical/rationale documentation, not current operating instructions. |

## README.md Target Shape

After decomposition, `README.md` should be a concise orientation document:

- one-paragraph identity and scope;
- quick links to focused `docs/`;
- compact list of available skills/packages;
- shortest build/install commands;
- pointer to CCDP and contribution guide;
- license.

The README should not carry the full collaboration-framework origin story,
component explanation, package command table, skill anatomy guide, or CCDP
protocol overview once focused docs exist.

## docs/ versus knowledge/ Boundary

`docs/` should explain what a human reader needs to know about the repository.
`knowledge/` should remain the source and derived material substrate consumed
by skills and packages. Arc04 may add wrapper or explanatory docs under
`docs/`, but should not duplicate or relocate the full knowledge substrate.
