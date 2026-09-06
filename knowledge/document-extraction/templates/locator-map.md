# Locator Record And Map Template

Use the [locator guide](../guides/09-locator-model.md). Repeat a typed record
for every distinct location; preserve original values alongside derived ones.
See the [PDF example](../examples/pdf-marker-handoff.md) for an unknown
converter basis that stays separate from a known physical-page location.

## Context

- Map ID / manifest: <id / reference>.
- Source / run / path resolution root: <IDs and root>.
- Snapshots covered: <raw, conversion, prepared IDs and inventory references>.
- Scope and observer: <full mapping or sample; actor and evidence kind>.

## Typed Locator Record

| Field | Value |
| --- | --- |
| Locator ID / source ID / snapshot ID | <IDs; snapshot of this endpoint> |
| Resource path or URI | <identified file or captured resource> |
| Kind | <page index, physical PDF page, displayed label, source resource, heading, anchor/ID, URI fragment, source lines, output lines> |
| Original value verbatim | <exact observed spelling or value> |
| Interpreted value or range | <value; unresolved if interpretation unverified> |
| Basis and scope | <zero/one-based; full document or subset; printed/viewer label system; line counting including headers; resource for anchors> |
| Endpoint convention | <inclusive/exclusive, single point, or not applicable> |
| Heading context when relevant | <parent chain, reading order, exact title; generated or source-authored> |
| Verification status | <verified within named scope, inferred, unresolved, unchecked> |
| Method / observer / coverage / evidence | <target existence/uniqueness and content comparison; direct versus report> |
| Caveat IDs | <references or explicit scoped none> |

## Source-To-Prepared Relations

| Mapping ID | From locator IDs | To locator IDs | Relation / transformation | Verification and evidence | Caveat IDs |
| --- | --- | --- | --- | --- | --- |
| <id> | <original and/or conversion endpoints> | <prepared endpoints> | <one-to-one, one-to-many, many-to-one; split, header, rewrite> | <observed matches, scope, status; do not imply exhaustive fidelity> | <IDs> |

Unresolved relation: <candidate endpoints, evidence needed, mapping withheld>.
Never default an unknown PDF page basis. Keep page labels separate from
physical ordinals, and never invent fixed pagination for EPUB or HTML.

## Lifecycle And Handoff

- Prior mapping / changed locations: <record references and reason, or first run>.
- Revalidation after regeneration: <new snapshot, checks/results; retained old IDs>.
- Readiness report: <reference and use-specific impact of unresolved mappings>.
- Available output navigation versus original-source traceability: <separate claims>.

Locators do not validate source claims or grade concept-card evidence.
