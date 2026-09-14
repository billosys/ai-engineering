# CC Proposed-Done: Arc06 Slice01

Status: CC proposed-done, pending independent CDC review. This is not operator
acceptance and does not change the transition's 115 accepted pairs.

| ID | Attested result | Evidence |
| --- | --- | --- |
| S1-1 | Plan-derived exact 35 members are in the frozen remaining 440, disjoint from 115 accepted; 405 remain outside assignment. | semantic-membership.json; validation-evidence.md |
| S1-2 | Frozen census, both full v3.2 prompts, current template/guide, synthetic edge and card contexts are registered with hashes. | semantic-membership.json; semantic-evidence.md |
| S1-3 | Three coherent meanings retain predicate-specific orientation and name/context exceptions. | semantic-membership.json |
| S1-4 | Endpoint, card-edge, support and closure boundaries are explicit; no revision or support inheritance is inferred. | semantic-evidence.md; query-cases.json |
| S1-5 | Four expected/observed diagnostic cases cover prerequisite, extension, symmetry and unresolved synthetic support. | query-cases.json |
| S1-6 | Handoff preserves reader/query/extraction consequences and bounded design questions. | handoff.md |
| S1-7 | Literal replay checks validate membership, transition accounting, hashes, JSON, preservation and whitespace. | validation-evidence.md |

Artifact inventory: `semantic-membership.json`, `semantic-evidence.md`,
`query-cases.json`, `validation-evidence.md`, and `handoff.md`. Scope specified
and delivered is the exact 35-pair table only. No source, schema, extraction,
corpus, runtime, package, baseline, parent-plan or CDC artifacts were changed.

Key findings: legacy relation lists are reader-navigation inputs rather than
supported relationship edges; directed edge metadata separates meaning,
endpoints, support and closure; and the observed `relationship_type` versus
`relation_type`, `relationship_edge_refs` versus `relationship_refs`, target
anchor, and revision questions remain unresolved rather than normalized.
