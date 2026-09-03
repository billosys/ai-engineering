# public wording implementation map

## Scope

Slice03 implemented the accepted Arc05 public vocabulary in authorized public
source surfaces only.

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

Source commit:
`9b948da065534d0c58c7140a18ab6f9cd34dedf4`

## Edited Source Files

| Source file | Before | After |
|---|---|---|
| `README.md` | Described "Markdown skills, guides, methods, templates, and protocol material" and left skill-category/topology language as provisional Arc05 work. | Describes skill packages, planned method material, support templates, protocol distributions, skill kind, topology, atomic skill, composite skill, Rust, `collaboration-framework`, CCDP, and planned `concept-card-method`. |
| `docs/repository-overview.md` | Described installable Markdown skills, reusable templates, and top-level `collaboration-framework` as a skill entrypoint. | Uses skill package, support template, knowledge substrate, composite framework/operational skill entrypoint, skill kind, topology, Rust atomic example, and `collaboration-framework` composite example. |
| `docs/skill-library.md` | Stated the category words were practical wayfinding until Arc05 settled final vocabulary. | Introduces the accepted kind/topology split, domain/tooling skills, composite framework/operational `collaboration-framework`, Rust as atomic example, and planned `concept-card-method` as a planned method skill. |
| `docs/collaboration-framework.md` | Described the framework as top-level skill and retained provisional Arc05 category-language caveat. | Describes `collaboration-framework` as the top-level composite framework/operational skill and daily-driver composer; states component roots do not deprecate the composer. |
| `docs/knowledge-library-anatomy.md` | Used loader-entrypoint wording, source/package distinction, Biome and collaboration-framework exceptions. | Uses skill entrypoint, source-root/package-root distinction, Biome as a multi-entrypoint knowledge root, and `collaboration-framework` as the composite framework/operational example. |
| `docs/contributing.md` | Told contributors to keep category/topology wording provisional until Arc05. | Uses skill entrypoint, skill kind, topology, and confirms CCDP remains a protocol distribution rather than an installable skill package. |
| `docs/building-and-installing.md` | Used per-domain/tooling wording and explained generated zips and CCDP separately. | Uses domain/tooling skill zips, explicit source-root/package-root distinction, and CCDP as protocol distribution and protocol package. |
| `SKILL.md` | Top-level `collaboration-framework` entrypoint described the house framework and omitted accepted Arc05 kind/topology wording in metadata prose. | Version bumped from `1.4.6` to `1.4.7`; description and version history identify `collaboration-framework` as the composite framework/operational skill and domain/tooling skills as separately loaded. |

## Inspected But Unchanged

| Source file | Disposition |
|---|---|
| `docs/protocols.md` | Inspected and left unchanged in the final source commit. The page already uses protocol distribution language for CCDP and avoids calling CCDP a skill. A provisional edit was backed out after `make ccdp-package` exposed a stale assembled CCDP spec that Slice03 is not authorized to refresh under `protocols/ccdp/**`. |

## Accepted Vocabulary Applied

- `skill package`
- `skill entrypoint`
- `knowledge substrate`
- `skill kind`
- `domain/tooling skill`
- `framework/operational skill`
- `method skill`, with planned availability qualifier for `concept-card-method`
- `protocol distribution`
- `protocol package`
- `support material`
- `support template`
- `atomic skill`
- `composite skill`

## Axis Preservation

The public wording keeps skill kind separate from topology:

- kind: what the skill is about, such as domain/tooling, framework/operational,
  or method work;
- topology: how the skill composes, such as atomic or composite.

No edited public source file states that domain/tooling means atomic,
framework/operational means composite, or method skills are composite.
