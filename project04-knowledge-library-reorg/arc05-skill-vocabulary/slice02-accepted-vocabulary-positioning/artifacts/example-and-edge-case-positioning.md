# example and edge-case positioning

## Accepted Examples

Arc05 accepts these examples for public wording, with the caveats below.

| Surface | Accepted positioning | Caveat |
|---|---|---|
| Rust / `knowledge/rust/SKILL.md` | Rust is the public example of an atomic domain/tooling skill. | Say "example" rather than universal rule. Broad does not mean composite. |
| `collaboration-framework` / top-level `SKILL.md` | `collaboration-framework` is the accepted public example of a composite framework/operational skill and daily-driver composer. | Component roots do not deprecate the top-level composer. |
| CCDP / `protocols/ccdp/` | CCDP is a protocol distribution and protocol package, not an installable skill package. | It may be described as related assistant-engineering material, but not as a skill. |
| Biome / `knowledge/biome/` | Biome is the public package-root edge case: one knowledge root has multiple skill entrypoints and packages. | Public docs should explain this as a multi-entrypoint source root or current exception, not as proof that every multi-file root is composite. |
| `templates/GUIDE.md` | `templates/GUIDE.md` is a support template and cross-cutting support material. | Do not call it a standalone skill unless it gains an accepted skill entrypoint and package behavior. |
| planned `concept-card-method` | `concept-card-method` may be described as a planned method skill. | It is planned, not live source, not installable, and not package-validated. |

## Atomic Skill Caveat

Atomic means one bounded load reason and a coherent vocabulary, activities,
constraints, and failure model. Rust is the public anchor example because the
load reason "work in Rust" is coherent even though the domain is broad.

Do not say atomic means small, simple, isolated, or domain-only.

## Composite Skill Caveat

Composite means composition is identity-defining: the skill selects,
sequences, routes, governs, or composes multiple loadable components. The
collaboration-framework daily-driver composer is the accepted public anchor.

Do not say composite means framework, large, messy, or overgrown.

## CCDP Caveat

CCDP should be positioned as a protocol package / protocol distribution with
its own source root, package, and validation commands. Public wording should
pair CCDP with:

- `protocols/ccdp/`
- `ccdp.zip`
- `make ccdp-package`
- `make check-ccdp-package`

CCDP is a bridge/integration edge case in maintainer-facing classification,
but public docs should lead with protocol distribution language.

## Biome Caveat

Biome should be positioned as a multi-entrypoint knowledge root. Public docs
may say:

- `knowledge/biome/SKILL-js-linter.md` builds `biome-js-linter.zip`
- `knowledge/biome/SKILL-web-linter.md` builds `biome-linter.zip`

Use multi-entrypoint wording before topology jargon. The source root can be
larger than one package root.

## Planned Concept-Card Method Caveat

concept-card-method remains planned. Public wording may say:

- planned method skill
- future method material
- not yet a live installable skill

Public wording must not say:

- concept-card-method is available
- load concept-card-method now
- concept-card-method.zip exists
- knowledge/concept-card-method is current source unless a later source slice
  implements it

## Template Caveat

templates/GUIDE.md is accepted as support material. Public wording may explain
that it helps start new guides and that finished guide material usually belongs
under an owning knowledge root.

Do not use `templates/GUIDE.md` as evidence that templates are standalone
skills.
