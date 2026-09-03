# Public Language Boundary Register

Date: 2026-09-02
Slice: Arc04 Slice01 README and docs decomposition map

## public language boundary

Arc04 may use practical, provisional wording to help users navigate current
repository docs. Arc05 owns final public skill kind and atomic/composite
vocabulary.

## Allowed Arc04 Wording

Arc04 may describe current surfaces with plain operational language:

- "skill library"
- "domain and tooling skills"
- "collaboration framework"
- "framework components"
- "method skills" when referring to planned or current method-oriented
  material with clear current/planned status
- "protocol distribution" for CCDP
- "support templates" for `templates/GUIDE.md` and owner-local template
  surfaces

Arc04 may say that `docs/` explains repository materials and `knowledge/`
stores the knowledge-library substrate.

## Arc05-Owned Vocabulary

Arc05 owns final public language for:

- skill kind
- atomic
- composite
- domain
- tooling
- framework
- operational
- method
- protocol
- support

Arc04 should not turn these into final taxonomy definitions. It may use them
only as provisional descriptive labels where current reader navigation needs
them.

## Boundary Rules

- Do not collapse skill kind into topology.
- Do not state that every domain/tooling skill is atomic.
- Do not state that every framework/operational skill is composite.
- Do not classify CCDP as an installable skill package.
- Do not present `concept-card-method` as live implemented source until a later
  implementation project lands it.
- Do not rewrite public taxonomy tables in README/docs beyond what is needed
  for navigation before Arc05.

## Re-entry Conditions

Re-enter this boundary in Arc04 if:

- a README/docs edit needs a final definition of atomic or composite;
- a source doc wants to publish a category table rather than a navigation
  description;
- CCDP or Biome wording risks changing package meaning;
- method-skill wording would imply `concept-card-method` is implemented now.

Operator gate: final public vocabulary belongs to Arc05 or explicit operator
authorization.
