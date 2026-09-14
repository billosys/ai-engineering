# CC Proposed-Done: Arc06 Slice01

Status: CC proposed-done after Iteration 01, pending independent CDC review.
This is not operator acceptance and does not change the transition's 115
accepted pairs.

| ID | Attested result | Evidence |
| --- | --- | --- |
| S1-1 | Plan-derived exact 35 members are in the frozen remaining 440, disjoint from 115 accepted; 405 remain outside assignment. | semantic-membership.json; validation-evidence.md |
| S1-2 | Census of 2,054/31/2, named reads, both v3.2 prompts and registered contextual hashes repair R1. | semantic-membership.json; semantic-evidence.md |
| S1-3 | Legacy lists are retained as typed assertions while representation, resolution, revision and warrant remain distinct. | semantic-membership.json; semantic-evidence.md |
| S1-4 | Four bounded target outcomes distinguish found legacy slugs from missing synthetic requested targets. | semantic-evidence.md; query-cases.json |
| S1-5 | Four actual structured cases cover real prerequisite, empty extension, symmetry lookup and unsupported edge declaration. | query-cases.json |
| S1-6 | Handoff preserves assertion/warrant boundary and concrete CQ resolver questions. | handoff.md |
| S1-7 | Literal replay adds eligible-population and observed-result assertions to prior structural checks. | validation-evidence.md |

Artifact inventory: `semantic-membership.json`, `semantic-evidence.md`,
`query-cases.json`, `validation-evidence.md`, and `handoff.md`. Scope specified
and delivered is the exact 35-pair table only. No source, schema, extraction,
corpus, runtime, package, baseline, parent-plan or CDC artifacts were changed.

Key findings: legacy relation lists are reader-navigation inputs rather than
supported relationship edges; directed edge metadata separates meaning,
endpoints, support and closure; and the observed `relationship_type` versus
`relation_type`, `relationship_edge_refs` versus `relationship_refs`, target
anchor, and revision questions remain unresolved rather than normalized.
