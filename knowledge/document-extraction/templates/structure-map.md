# Structure Map Template

Fill under the [structure guide](../guides/08-structure-mapping-and-splitting.md).
Use the [manifest](./manifest.md) for shared identity and
[typed locators](./locator-map.md) for every span. This record may describe an
unsplit monolith. See the [EPUB example](../examples/epub-pandoc-handoff.md).

## Map Context

- Map ID / manifest reference: <id / path or section>.
- Source / input snapshot / prepared snapshot / run: <IDs>.
- Full requested scope / inspected scope: <content and inspection coverage>.
- Path root / numbering and range conventions: <root; bases; inclusive or exclusive>.
- Observer / evidence kind: <actor; direct, operator-reported, or inferred>.
- Sources compared: <body, navigation, metadata; file/snapshot and evidence>.
- Decision: <split accepted units, larger groups, or retain monolith; reason>.

## Ordered Section Records

Repeat one record per section, including front matter, unnumbered sections,
notes, references, and back matter. Use IDs, hierarchy and order to distinguish
duplicate titles and TOC occurrences from body targets.

| Field | Value |
| --- | --- |
| Section ID / parent ID / reading order | <id / parent or root / ordinal> |
| Original title / original label / original anchor | <verbatim values or absent> |
| Kind | <front matter, TOC, part, body, appendix, notes, back matter, etc.> |
| Input resource / start and end locator IDs | <preserved snapshot path / typed endpoints> |
| Boundary evidence / status | <observed surrounding content and evidence; verified within scope, inferred, unresolved, or unchecked> |
| Destination / output locator IDs | <prepared file and span, or unsplit mapping> |
| Metadata placement / generated fields | <sidecar or header; original versus generated; line offset effect> |
| Containers / dependencies | <fences, divs, tables, notes, definitions, anchors and cross-links; handling> |
| Caveat IDs | <IDs or explicit none found within scope> |

## Reconciliation And Regeneration

| Check | Scope and evidence | Outcome / caveat |
| --- | --- | --- |
| Every input span accounted for in order | <retained spans and destinations; excluded spans and justification> | <pass, fail, not checked, not applicable with reason> |
| No unintended gap, overlap, or duplication | <span comparison; intentional repeats distinguished> | <outcome> |
| Navigation versus body | <unmatched entries, additional sections, TOC duplicates> | <outcome> |
| Complete containers and shared definitions | <both sides of every cut; dependency destinations> | <outcome> |
| Names unique and stable | <ID-to-path map; case folding/truncation collisions> | <outcome> |
| Content after splits matches mapped input | <normalizations accounted for; body comparisons> | <outcome> |
| Regeneration | <fresh destination; preserved map reuse; comparison result or untested> | <outcome> |

Unresolved boundary: <alternatives, retained representation, affected uses,
next inspection>. Send these findings to [readiness](./validation-readiness.md);
matching section counts alone does not establish preservation.
