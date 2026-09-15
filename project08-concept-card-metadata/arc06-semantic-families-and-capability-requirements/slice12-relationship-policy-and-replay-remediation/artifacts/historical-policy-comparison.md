# Historical Relationship Policy Comparison

## Scope And Inputs

This is the bounded Slice12 R5 comparison for the four legacy relationship
roots and their item lists: `prerequisites`, `extends`, `related` and
`contrasts_with`. It uses the already registered `v32Parallel` and `v32Howto`
authorities plus the frozen frontmatter inventory and its accepted census. It
does not add a membership pair, choose a future schema, or treat historical
instructions as proof that every frozen card followed them.

The historical sources have two rule scopes:

- `old/dev/concept-cards/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md:585-610`
  says every non-foundational concept needs prerequisites and its quality
  requirements call for all frontmatter fields, using `null` or an empty array
  where not applicable.
- The same source's Required Frontmatter Fields at `:877-893` marks
  `prerequisites` required and permits an empty list for foundational concepts.
- `old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md:573-592`
  lists all four legacy relationship keys among missing fields and requires
  conformance to the v3 template. This is broader template-conformance
  guidance, not four separately stated relationship-specific requiredness rules.

## Comparison Matrix

| Root and item list | Documented historical rule and scope | Observed frozen states and item values | Lineage and conformance limits | Future-policy question |
| --- | --- | --- | --- | --- |
| `prerequisites`, `prerequisites[]` | Non-foundational concepts need prerequisites. Foundational concepts may use an empty list. The broader all-frontmatter rule permits `null`/empty where not applicable. | Complete Musician: present 390, null 0, empty 5, populated 385; 620 string items and 183 distinct targets. Erlang: present 1,664, absent 0, null 1, empty 306, populated 1,357; 2,282 string items and 586 distinct targets. | The census cannot recover whether each card was generated under the rule or whether a concept was foundational. The `data-type-sizes.md` null witness still has body prerequisite prose; null is not proof of no conceptual dependency. | After P-15, decide how a future contract expresses foundational status, applicability, missing/null/empty states and migration without silently adopting v3.2. |
| `extends`, `extends[]` | The broader all-frontmatter/template-conformance guidance names this field. No separate relation-specific requiredness rule is stated in the registered passages. | Complete Musician: present 390, absent/null 0, empty 180, populated 210; 210 string items and 88 distinct targets. Erlang: present 1,598, absent 66, null 0, empty 1,289, populated 309; 314 string items and 162 distinct targets. | Absent Erlang keys may reflect lineage, applicability or nonconformance; the frozen records do not distinguish those causes. Legacy items remain slugs without edge support or revision. | Decide whether a future profile requires, omits, nulls or empties this relation by source/card applicability, and how migration preserves the distinction. |
| `related`, `related[]` | The broader all-frontmatter/template-conformance guidance names this field. Its historical meaning remains symmetric association without dependency implication. | Complete Musician: present 390, null 0, empty 16, populated 374; 752 string items and 331 distinct targets. Erlang: present 1,664, absent 0, null 1, empty 21, populated 1,642; 4,065 string items and 1,239 distinct targets. | Presence and item counts do not establish universal conformance, reciprocal storage requirements or edge truth. The null witness remains distinct from an empty list. | Decide future requiredness and reciprocal representation separately from the preserved symmetric reader behavior. |
| `contrasts_with`, `contrasts_with[]` | The broader all-frontmatter/template-conformance guidance names this field. The historical meaning is commonly confused concepts; it is not silently replaced by the current guide's broader qualified comparison. | Complete Musician: present 390, null 0, empty 262, populated 128; 148 string items and 107 distinct targets. Erlang: present 1,664, absent 0, null 3, empty 1,133, populated 528; 643 string items and 385 distinct targets. | Observed null/empty states do not prove absence of contrast or universal conformance. Legacy item slugs do not supply edge-scoped support. | Decide whether the future profile retains the common-confusion distinction, how qualified comparisons are represented, and which applicability/requiredness policy is accepted. |

## Bounded Conclusion

The explicit prerequisite rule must not be reported as absent. The broader
all-field/template instructions must also not be inflated into a claim that
every historical card conformed or that every relationship key was individually
required under the same conditions. Observed absent, null, empty and populated
states remain corpus facts with different meanings; they are not coerced into
one requiredness result.

The future policy remains open for the operator's P-15 schema/specification
discussion. This artifact records historical authority, observed behavior,
lineage limits and unresolved design questions; it does not adopt required
fields, a schema language, a migration rule or a specification format.
