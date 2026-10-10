# Correction handoff — token-system conventions

Proposed source text for CDC review; no live SOURCE edit is made. Original
C&B literals remain evidence while the portable proposal removes those defaults.

## Proposed architecture explanation

> A token system may keep reusable reference values, semantic aliases and
> component-specific bindings. Reference values hold reusable inputs; semantic
> aliases name roles that matter across consumers or themes; optional component
> bindings provide a place for component-specific choices and exceptions.
> Choose the number of layers according to consumers, theme variation,
> component-specific change and maintenance cost. A semantic alias changes a
> consumer only when it resolves through that alias and the relevant theme
> mapping covers it. Adding a site requires explicit mappings and component
> coverage. Direct component values can be appropriate when a value is genuinely
> local or an implementation documents that choice.
>
> This model can resemble separation of concerns: values, role names and
> component choices serve different purposes. The analogy is not a formal
> equivalence to programming-language types, interfaces or implementations.
> DTCG 2025.10 provides a JSON interchange format, token types, groups,
> references and composite values; it does not mandate this layer count or a
> universal semantic vocabulary. Validate an actual exported file against the
> selected DTCG version before describing it as conforming.

This retains semantic role naming and an optional component layer. It rejects
three tiers as format or industry law, and rejects a universal ban on direct
component values: Material Web permits them. Project guidance may still prefer
semantic aliases for reusable roles. Propagation requires working references,
theme mappings and covered component consumers.

## Occurrence-level disposition

| Inventory IDs / source | Proposed treatment | Reason and owner |
|---|---|---|
| U003, U013, U049, U050, U145 — SKILL.md:70, 114, 270; design.md:175–176 | Retain the local semantic-reference preference, qualified by intentional direct-value and component-binding exceptions. | Same local object/use rule; not universal. Design skill maintainer; CDC review. |
| U016, U041, U042, U043, U044, U045, U046, U047, U048 — SKILL.md:368; design.md:166–173 | Replace categorical identity with the bounded analogy above. | Useful analogy, but no formal type/interface/implementation equivalence or guaranteed propagation/refactoring. Design skill maintainer; T review for broader theory. |
| U017, U018, U020, U022, U023, U028, U032, U036, U037, U038, U039, U040, U055, U080, U081, U082, U109, U110, U111 — design.md:61–78, 160–165, 329; colour.md:565–567; foundations-of-design.md:471–474 | Replace convergence/necessity claims with: “These systems document different token models. Name the product, generation, page date and exact token category for each comparison; examples do not establish a universal layer count.” | Fluent's documented two layers and differences defeat universal wording. Material 3 and old Polaris passages remain blocked. Design maintainer; CDC re-entry. |
| U061, U062, U063 — design.md:371–373 | Replace with: “DTCG 2025.10 defines a JSON interchange format for design tokens. A design system may define stable semantic names for its own contexts; the format does not guarantee identical role meaning across systems, platforms or tools.” | DTCG directly describes a file format; system meaning is locally chosen. Design maintainer; CDC verifies attribution. |
| U067 — colour.md:14 | Keep the tag only as historical evidence; remove or qualify “DTCG-aligned” in a future edit until an actual export is validated. | No export or conformance test here. Colour guide maintainer; T/source validation owner. |
| U001, U051, U052, U053, U054, U069, U079, U080, U081, U082, U144 — SKILL.md:34, 249; design.md:178–180; colour.md:236, 249, 564–567 | Replace the “follows DTCG/converges” and unconditional site-propagation statements with the architecture explanation above. Retain examples only as local examples after mappings and site coverage are checked. | DTCG does not specify architecture; propagation and inheritance need explicit mappings and complete consumers. Colour guide maintainer; CDC review. |
| U099, U100, U128, U130, U131 — foundations-of-design.md:108–109, 495–498 | Replace status/type text with: “DTCG 2025.10 is a Community Group Final Report, not a W3C Standard or Standards Track document. It defines primitive and composite token types, including typography as a composite with specified child properties and types.” Validate exact type list against the chosen version before retaining it. | Correct status, format scope and composite structure. Foundations guide maintainer; T validates broader typography claims. |
| U108, U109, U110, U111 — foundations-of-design.md:471–474 | Replace “dominant pattern” and asserted universal convergence with the qualified architecture explanation. Remove industry-trend wording unless a separately scoped review supplies representative evidence. | Accessible systems do not establish universality; Material 3 and old Polaris passages remain gaps. Foundations maintainer; CDC review. |

## Gaps and boundaries

G-M3 and G-POLARIS-OLD-A/B block claims that depend on their historical
passages. CDC/Operator owns retrieval; re-entry requires readable official
bodies, exact generation/date and pinned text. Do not substitute snippets, a
live Material Web page, archive status or current Shopify web components.

Other selected context stays with its existing owners: typography scale
arithmetic and Utopia naming/clamp (T/L); spacing grids, naming and values
(T/L); OKLCH/browser support, hex interoperability, industry trends and
perception claims (T/L); documentation categories (L/Arc04); CSS cascade tiers
(L, separate subject); accessibility contrast (Arc03). The preview chip at
colour.md:245 remains an observed markup/value example pending whole-file
colour-guide review; it is not automatically a component-token binding.

No live edit, DTCG export, token implementation, Project08 metadata migration or
Project13 record is authorized by this handoff.
