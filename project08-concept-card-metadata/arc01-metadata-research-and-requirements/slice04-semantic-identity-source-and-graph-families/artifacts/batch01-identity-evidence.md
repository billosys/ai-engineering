# Batch01 Identity Evidence

## Inputs and observations

Planning prompts: v3.2 extraction `0009` SHA-256
`56eb092cfed206edf588748e041df9ed53448f941f1dee43684f96994a898cbd`
and re-extraction `0010` SHA-256
`b942d34237391d7a8d84ad463cd2c25aa72196adbc98797877dabc26a5ba337c`;
v3.1 predecessors `0007`/`0008` are retained comparison inputs. `0010` lines
351, 613-14 and 653-58 require legacy `slug` to match the lower-case hyphenated
filename and use it for cross-reference. `0010` lines 374-75 and 890 require
an aliases list (empty when none), while the current concept-card template has
`id`, `revision`, `title`, `concept_slug`, and `aliases` in frontmatter.

Representative observed values: Complete Musician `accent-types.md`
(`c5af9d16b099430d15d6a6fab2beaa00aea73704021a0c224056a271ffe07fde`)
uses `concept: Accent Types`, `slug: accent-types`, and populated aliases;
Arc07 `cc-emergent-explanation.md`
(`a7b5b387434bc82885ad013b36ed65d354cdb7687d4d3fa1daaffcebadbcbead`)
uses current `id`/`revision`/`concept_slug`. The Slice01 inventory registers
the corresponding Erlang and captured-rerun populations; malformed rich YAML
cannot establish populated identity values.

## Authored meanings and dispositions

`legacy-slug`: a filename-coupled, source-local lookup key; preserved as a
historical value but not demonstrated as the current record-ID authority.
`legacy-concept`: displayed concept label, not stable identity. `current-id`:
record identity; `revision`: that record's revision, not source edition;
`concept-slug`: current concept lookup label; `title`: display label; `aliases`:
alternate lookup labels. Alias key presence is preserved, but the inspected
scope does not prove authority-control equivalence or a completed migration.
Null placeholders are unfilled template values; absence and invalid YAML are
separate observations.

Lookup consequence: legacy filename references cannot safely be rewritten to
current IDs without an explicit mapping; titles/concepts require a stable ID or
slug to avoid collision. Bodies may display labels but do not supply this
machine lookup contract.

## Artifact shape and checks

`batch01-identity-membership.json` has one explicit observed path/kind pair,
an authored meaning ID, contextual evidence class, and disposition. `jq` parses
it and its unique path/kind projection is exactly the ten prompted pairs.
This is structural validation, not source-book verification. Remaining 545
pairs and full alias-authority comparison remain open.
