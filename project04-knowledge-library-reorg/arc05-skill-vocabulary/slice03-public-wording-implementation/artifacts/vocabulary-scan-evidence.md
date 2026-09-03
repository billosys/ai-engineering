# vocabulary scan evidence

## Source Scope

Scans covered public source surfaces under:

- `/Users/oubiwann/lab/billosys/ai-engineering/README.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs`
- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`

## Accepted Terms

Command:

```sh
rg -n "skill kind|domain/tooling|framework/operational|method skill|protocol distribution|protocol package|support material|support template|atomic skill|composite skill|knowledge substrate" README.md docs SKILL.md
```

Result: passed with matches in the authorized public surfaces.

Representative matches:

- `README.md` records skill packages, planned method material, support
  templates, protocol distributions, skill kind, topology, atomic skill,
  composite skill, Rust, `collaboration-framework`, CCDP, and planned
  `concept-card-method`.
- `docs/skill-library.md` records skill kind, topology, domain/tooling skill,
  composite framework/operational skill, atomic skill, and planned method
  skill.
- `docs/collaboration-framework.md` records the top-level composite
  framework/operational skill and daily-driver composer.
- `docs/knowledge-library-anatomy.md` records knowledge substrate, skill
  entrypoint, multi-entrypoint Biome behavior, and source-root/package-root
  distinction.
- `docs/building-and-installing.md` records domain/tooling skill zips,
  source-root/package-root distinction, protocol distribution, and protocol
  package.
- `SKILL.md` records composite framework/operational skill and separately
  loaded domain/tooling skills.

## Avoided Claims

Command:

```sh
rg -n "atomic means domain|composite means framework|method skills are composite|CCDP is a skill|concept-card-method is available|source root always equals package root|source-root/package-root equivalence|collaboration-framework.*deprecated|all knowledge lives in docs|all framework material is documentation|CCDP package is installed by make install" README.md docs SKILL.md
```

Result: no matches.

Contextual verdict: no unqualified prohibited claims were found in the edited
public source surfaces. The wording explicitly avoids these claims:

- atomic means domain;
- composite means framework;
- CCDP is a skill;
- concept-card-method is available;
- source-root/package-root equivalence;
- `collaboration-framework` is deprecated;
- all knowledge lives in docs;
- all framework material is documentation;
- CCDP package is installed by `make install`.

## Caveated Risky Wording

- `concept-card-method` appears only as planned method skill wording.
- CCDP appears as protocol distribution / protocol package wording and is kept
  separate from installable skill packages.
- Source roots and package roots are explicitly described as potentially
  different.
- Biome is described as a multi-entrypoint knowledge root, not as proof that
  every multi-entrypoint root is composite.
