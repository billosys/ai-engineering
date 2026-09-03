# vocabulary reconciliation report

## Scope

Slice04 reconciled the public vocabulary after Slice03 source implementation.
No source edits were needed and no source commit was created.

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

## README/docs/SKILL Consistency

| Surface | Result |
|---|---|
| `README.md` | Consistent. It introduces skill packages, support templates, protocol distributions, `docs/` versus `knowledge/`, skill kind, topology, atomic skill, composite skill, Rust, `collaboration-framework`, CCDP, and planned `concept-card-method`. |
| `docs/` | Consistent. Focused docs explain repository navigation, skill loading, collaboration-framework composition, knowledge substrate shape, build/install behavior, CCDP protocol boundaries, and contribution rules without duplicating the knowledge substrate. |
| `SKILL.md` | Consistent. The top-level entrypoint identifies `collaboration-framework` as the composite framework/operational skill and states that domain/tooling skills under `knowledge/` load separately. |

## Accepted Kind and Topology Wording

The public wording keeps the two axes separate:

- skill kind: what a skill is about, including domain/tooling,
  framework/operational, and method work;
- topology: how a skill composes, including atomic skill and composite skill.

The public examples remain consistent:

- Rust is the public example of an atomic domain/tooling skill.
- `collaboration-framework` is the public example of a composite
  framework/operational skill and remains the daily-driver composer.
- `concept-card-method` is a planned method skill until source and package
  support exist.
- CCDP is a protocol distribution / protocol package, not an installable skill
  package.
- `templates/GUIDE.md` is support material / support template.
- Biome remains a multi-entrypoint knowledge root.

## docs/ and knowledge/ Boundary

The docs/ and knowledge/ boundary remains intact:

- `docs/` explains repository materials, routes, build/install behavior,
  protocol packaging, and contribution expectations for human readers.
- `knowledge/` stores the actual raw and derived knowledge substrate consumed
  by skills and generated packages.

No public wording says all knowledge lives in docs or that all framework
material is documentation.

## Accepted Vocabulary Scan

Command:

```sh
rg -n "skill kind|domain/tooling|framework/operational|method skill|protocol distribution|protocol package|support material|support template|atomic skill|composite skill|knowledge substrate" README.md docs SKILL.md
```

Result: accepted vocabulary scan passed with matches across `README.md`,
`docs/`, and `SKILL.md`.

## Avoided Claim Scan

Command:

```sh
rg -n "atomic means domain|composite means framework|method skills are composite|CCDP is a skill|concept-card-method is available|source root always equals package root|source-root/package-root equivalence|collaboration-framework.*deprecated|all knowledge lives in docs|all framework material is documentation|CCDP package is installed by make install" README.md docs SKILL.md
```

Result: avoided claim scan passed with no matches.

Verdict: no unqualified prohibited claims were found.

## Reconciliation Result

Arc05 public wording is reconciled for README/docs/SKILL consistency. No
source repair is required for vocabulary wording.
