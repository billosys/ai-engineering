# accepted public vocabulary

## Decision Boundary

This artifact accepts Arc05 public vocabulary for current README/docs/SKILL
wording work. It does not edit source files. It keeps skill kind separate from
topology and does not infer taxonomy from folder placement alone.

source-files-edited: false

## Accepted Public Terms

| Term | Status | Public use |
|---|---|---|
| skill package | public | Use for generated installable assistant-skill zips such as `rust-guidelines.zip` and `collaboration-framework.zip`. |
| skill entrypoint | public | Use for `SKILL.md` or `SKILL-*.md` files that define when a skill should load. |
| knowledge substrate | public | Use for the source and derived material under `knowledge/` that skills and packages consume. |
| skill kind | public | Use when explaining the "what is this skill about?" axis. Keep it separate from topology. |
| domain/tooling skill | public | Use for skills about a language, toolchain, linter, design discipline, platform, or professional practice area. |
| framework/operational skill | public | Use for the collaboration framework and operational components that coordinate planning, verification, review, testing, auditing, delegation, contribution, or collaboration posture. |
| method skill | public with availability qualifier | Use for reusable knowledge-work methods. When naming `concept-card-method`, say planned method skill until source and package support exist. |
| protocol distribution | public | Preferred public wording for CCDP. It distinguishes CCDP from installable skill packages. |
| protocol package | public | Use when discussing `ccdp.zip`, package shape, package-local rebuild, or validation. |
| support material | public | Use for reusable materials that help create or operate skills, docs, frameworks, or protocols. |
| support template | public | Use for templates such as `templates/GUIDE.md` when the template is support material rather than a standalone skill. |
| atomic skill | public | Use for a skill with one bounded load reason and a coherent vocabulary, activities, constraints, and failure model. |
| composite skill | public | Use for a skill whose identity is selecting, sequencing, routing, governing, or composing multiple loadable components. |

## Maintainer-Facing Terms

| Term | Status | Use |
|---|---|---|
| bridge/integration layer | maintainer-facing | Use in planning, architecture, and maintainer docs when a surface connects domains, tasks, protocols, package surfaces, or governance layers. Avoid making it a first-level end-user category unless the page is explaining an edge case. |
| application/task bundle | maintainer-facing | Use for planning and maintainer analysis of local recipes or workflows. Avoid presenting it as a primary public skill category now. |
| source/provenance | maintainer-facing | Use when discussing original sources, extracted material, transformation records, historical evidence, workbench material, or package-excluded substrate. |
| source root | maintainer-facing | Use for repository-maintenance and package-validation discussion. |
| package root | maintainer-facing | Use for package-validation discussion, especially where it differs from source root. |

## Deferred Terms

| Term or decision | Status | Re-entry |
|---|---|---|
| metadata category alignment | deferred | Reopen when Slice03 or Arc06 decides whether frontmatter categories should match accepted public skill kind names. |
| package root renames | deferred | Reopen only with explicit source/package authorization and package validation evidence. |
| `concept-card-method` availability wording | deferred until implementation | Public docs may say planned method skill; they must not say available or installable. |
| bridge/integration and application/task as public category headings | deferred | Reopen if a public docs page needs those labels for user comprehension rather than maintainer classification. |

## Avoided Terms

Avoided status applies to claims, not just literal strings:

- "atomic means domain"
- "composite means framework"
- "method skills are composite"
- "CCDP is a skill"
- "`concept-card-method` is available"
- "source root always equals package root"
- "`collaboration-framework` is deprecated"
- "all knowledge lives in docs"
- "all framework material is documentation"

## Explicit Answers to Slice01 Questions

- Public docs should use "domain/tooling skill" where category language is
  useful, while README may use the simpler phrase "programming and tooling
  skill packages" for first-pass orientation.
- "framework/operational skill" is accepted public vocabulary, but pages may
  prefer concrete collaboration-framework wording when that is clearer.
- "method skill" is accepted public vocabulary with an availability qualifier.
- "protocol distribution" is the preferred public term for CCDP; "protocol
  package" is public for ccdp.zip/package validation contexts.
- "support material" and "support template" are public; "support/template" as
  slash taxonomy is not required in user-facing prose.
- "source/provenance" remains maintainer-facing.
- "atomic skill" and "composite skill" are public, but should be introduced
  with short definitions and examples rather than used as unexplained labels.
