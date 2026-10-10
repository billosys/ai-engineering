# Primary-source comparison — token-system conventions

Observation date: 2026-10-10. These are live-page observations, not immutable
captures; no source snapshot hash or original publication lineage was supplied.
They support bounded technical comparison only. They do not close P10-11,
establish historical author verification, or validate an export.

## Register

| ID | Source and version | Read extent and status | Observation and limit |
|---|---|---|---|
| E-DTCG | [Design Tokens Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/), Final Community Group Report dated 2025-10-28 | Abstract/Status, §§1, 3.6–3.9, 4, 5.2.2, 6.1, type headings, §§9.2 and 9.8 plus needed definitions. Not a W3C Standard or Standards Track. | Defines JSON interchange and token structure. Types classify values; groups are arbitrary; aliases reference tokens; composites are typed structured values. No universal semantic-role vocabulary or three-layer architecture. |
| E-MW | [Material Web theming](https://material-web.dev/theming/material-theming/), documentation/package version unknown | Full short page: Reference, System, Component. Explanatory implementation guidance. | Reference tokens hold concrete values; system tokens name roles; component tokens can be system tokens or concrete values. Bounded to Material Web, not every Material Design generation. |
| E-FLUENT | [Fluent 2 tokens](https://fluent2.microsoft.design/design-tokens), publication/version unknown | Full short page: global, alias and theming. Explanatory guidance. | Explicitly documents two layers. This counters “every system requires three”; it does not prove all Fluent internals lack component-level choices. |
| E-CARBON | [Carbon color overview](https://www.carbondesignsystem.com/building-blocks/foundations/color/overview), updated 2026-09-25; references v11 design kit; package version unknown | Definitions, themes, token names, core/component tokens and layering model. Explanatory guidance. | Separates theme-dependent values, role-based token identifiers, core/component categories and visual layering. |
| E-UTOPIA | [Utopia type calculator](https://utopia.fyi/type/calculator/), publication/version unknown | Full CSS generator configuration and example. | Default sample uses numbered step properties and clamp; method and prefix are configurable. Not universal typography policy. |
| E-POLARIS | [Shopify Polaris React archive](https://github.com/Shopify/polaris-react-archive), exact old package version not inspected | README archive and deprecation notice. | Establishes archived/unmaintained/deprecated status, not historical token layering. |
| E-SHOPIFY | [Polaris React to web components migration](https://shopify.dev/docs/apps/build/app-home/migrate-from-polaris-react), page version unknown | Introduction and Requirements, including comparison baseline. | Names Polaris React 13.9.5 as comparison baseline and current web components as migration target. |
| G-M3 | [Material Design 3 token overview](https://m3.material.io/foundations/design-tokens/overview), version/date unknown | Direct open returned a one-line JavaScript-required shell; no body passage read. | Unavailable; no snippet substituted. Material Web cannot stand in for all Material Design 3 documentation. Owner: CDC/Operator. Re-entry: obtain readable official body at a pinned revision/date and check exact token-layer and component-value claims. |
| G-POLARIS-OLD-A | [Polaris React color tokens](https://polaris-react.shopify.com/tokens/color), version/date unknown | Direct open returned an internal error; no body passage read. | Historical comparison blocked. Owner: CDC/Operator. Re-entry: recover official archived page body or pinned repository document directly stating the model; inspect generation and publication identity. |
| G-POLARIS-OLD-B | [Archived Polaris React color tokens](https://shopify.github.io/polaris-react-archive/tokens/color), version/date unknown | Direct open returned an internal error; no body passage read. | Do not infer hierarchy from names or archive status. Owner: CDC/Operator. Re-entry: recover page bytes and verify against a pinned archived source revision. |

## Comparative findings

DTCG §4 calls token files JSON files that follow the module structure. Its type
rules require an unambiguous type, set directly or inherited from a group or
reference; tools must not guess from the value. Groups are organizational
containers; composites are individual typed tokens with structured child
values. Typography is a composite whose required children are fontFamily,
fontSize, fontWeight, letterSpacing and lineHeight, each with specified value
type/reference requirements. These syntax rules do not define every system's
semantic names.

The sources show useful roles without a universal count. Material Web documents
reference/system/component and permits concrete component values. Fluent 2
documents global/alias. Carbon documents core/component color tokens, roles and
theme-assigned values alongside a visual layering model. These differences
prevent treating “industry convergence” as proof of a three-tier law. They
support values, role aliases and optional component-local control as design
choices.

Theme propagation is conditional. A role alias changes consumers only where
their references resolve through it and theme mappings cover the consumer. A
new site needs explicit role/value mapping and component coverage. Carbon
illustrates that a token role can persist while its assigned value changes.
Material Web's concrete component values show that an alias at every component
binding is not universal.

The local pair is internally consistent at its stated scope: SOURCE
knowledge/design/SKILL.md:114 says components reference semantic tokens, and
knowledge/design/guides/design.md:175–177 says to use the semantic example rather
than the primitive example. Both address component references. This is local
policy, not a universal industry rule. Material Web's concrete-value allowance
counters universalizing the ban but does not conflict with the local pair. The
colour guide's colour.md:245 .sem-chip is preview markup using a primitive
value; it does not establish that the chip is a product component binding.

Polaris evidence is asymmetric: archive status and current migration boundary
are known; historical color-token details are unavailable. No Polaris agreement
or disagreement is inferred. Utopia's configurable example does not warrant a
universal clamp rule.

## Decision boundary

Portable guidance can keep reference/value tokens for reusable source values,
use semantic aliases where role meaning, reuse or theme variation benefits from
a stable mapping, and add component bindings when local control or component
exceptions justify their maintenance. A two-layer or direct component-value
arrangement can be valid where scope and tradeoffs are explicit. More layers
add indirection, names and maintenance; fewer can couple components to values
and make cross-theme changes harder. Choice depends on consumers, change
patterns, theme count, component-specific variation and tooling.

The software separation-of-concerns analogy can remain illustrative: values
hold inputs, aliases name roles, optional component bindings localize choices.
It is not a formal type/interface/implementation mapping and does not guarantee
automatic propagation, effortless site onboarding or independent comprehension.
Those outcomes depend on references, resolution, theme maps, component coverage
and validation.

No export, implementation, browser check, accessibility test, empirical
palette study or historical-source capture was performed.
