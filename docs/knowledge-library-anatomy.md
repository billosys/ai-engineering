# Knowledge Library Anatomy

[`knowledge/`](../knowledge/) stores the source and derived material that
skills and packages consume. It is the repository's knowledge substrate: the
place for entrypoints, guides, source extracts, provenance, examples,
templates, and workbench material owned by a specific knowledge surface.

`docs/` explains this structure. It does not replace it.

## Common Shape

Many knowledge roots follow this shape, though not every root has every
directory:

```text
knowledge/<surface>/
├── SKILL.md or SKILL-*.md
├── guides/
├── concept-cards/
├── extraction-metadata/
├── sources/
├── templates/
├── examples/
├── tools/
└── workbench/
```

## What Each Part Means

| Part | Role |
|---|---|
| `SKILL.md` or `SKILL-*.md` | Skill entrypoint with the skill name, trigger guidance, scope, and routing. |
| `guides/` | Topic guides that carry the main reusable guidance. |
| `concept-cards/` | Atomic concept records where a surface has concept-card material. |
| `extraction-metadata/` | Provenance and transformation evidence for generated or synthesized material. |
| `sources/` | Original or normalized source material used to build the guides. |
| `templates/` | Templates owned by that knowledge surface. |
| `examples/` | Example artifacts used by that knowledge surface. |
| `tools/` | Local helper tools owned by that knowledge surface. |
| `workbench/` | Scratch, review, release, or transition material that is useful in source but not necessarily packaged. |

## Source Roots And Package Roots

Source roots can be larger than package roots. For installable skill zips, the
Makefile packages the skill entrypoint and guide surface needed by the loader.
Source-only material such as extraction metadata, source corpora, and
workbench notes usually stays out of the generated zip.

This distinction matters when checking links. A link can be valid for a source
reader but invalid inside a generated package, or valid inside a package but
not meaningful as a source maintenance route. Package validation should be run
against generated zips, not guessed from source paths alone.

## Current Exceptions

Some roots have multiple entrypoints. For example, [`knowledge/biome/`](../knowledge/biome/)
is a multi-entrypoint knowledge root that ships two lint skills, and
[`knowledge/deno/`](../knowledge/deno/)
uses a specific JavaScript linter entrypoint.

The top-level collaboration framework entrypoint remains [`SKILL.md`](../SKILL.md)
at the repository root while its supporting material lives under several
`knowledge/` component roots. It is the public example of a composite
framework/operational skill.

CCDP lives under [`protocols/ccdp/`](../protocols/ccdp/), not under
`knowledge/`, because it is packaged as a protocol distribution rather than as
an installable assistant skill.
