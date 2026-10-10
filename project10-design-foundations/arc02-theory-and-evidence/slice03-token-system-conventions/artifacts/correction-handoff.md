# Correction handoff — complete token assertions

Proposed source text and exact occurrence actions for CDC review. No live SOURCE edit is made. The original C&B examples remain historical evidence; the portable proposal removes C&B defaults. Each action below is authoritative for one non-overlapping source block; unit membership is explicit.

## ACT-01 — knowledge/design/SKILL.md:34–34

Units: A001

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`; inclusive lines `34–34`.

Complete old target:
```text
| **Colour System** | `colour.md` | The actual token architecture — OKLCH scales for brand, neutrals, and per-site accents; semantic layer (surfaces, text, borders, interactive); three-site theming. | When writing CSS colour values, building palettes, creating themes, mapping primitives to semantic tokens, or choosing any colour. |
```

Proposed replacement (verbatim):
```text
| **Colour System** | `colour.md` | Repository colour guidance for palette examples, role mappings and themes; product-specific examples and scope should be checked in context. | When writing CSS colour values, building palettes, creating themes, mapping values to semantic tokens, or choosing any colour. |
```

Rationale: The original row says “actual token architecture,” which overstates what a route description can establish. The table remains a route into local colour guidance.

Owners: Design skill maintainer; CDC review.


## ACT-02 — knowledge/design/SKILL.md:70–70

Units: A003

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`; inclusive lines `70–70`.

Complete old target:
```text
| III | **Name the Role, Not the Value** | Three-tier tokens: primitive → semantic → component. Never use `var(--brand-700)` in a component. | `background: var(--brand-700)` instead of `background: var(--interactive-primary)`. |
```

Proposed replacement (verbatim):
```text
| III | **Name the Role, Not the Value** | Prefer semantic aliases for reusable component roles; use direct values or component-specific bindings when a value is genuinely local or an exception needs local control. | `background: var(--role-action)` for a shared role; use a local value when no shared role applies. |
```

Rationale: This preserves the local preference and removes the universal direct-value prohibition and C&B-specific example.

Owners: Design skill maintainer; CDC review.


## ACT-03 — knowledge/design/SKILL.md:104–104

Units: A006

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`; inclusive lines `104–104`.

Complete old target:
```text
### Three-Tier Tokens
```

Proposed replacement (verbatim):
```text
### A Three-Tier Example
```

Rationale: The diagram remains useful as a named local example; it is not a format requirement.

Owners: Design skill maintainer; CDC review.


## ACT-04 — knowledge/design/SKILL.md:114–114

Units: A012

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`; inclusive lines `114–114`.

Complete old target:
```text
**Rule**: Components reference semantic tokens, never primitives.
```

Proposed replacement (verbatim):
```text
**Guideline**: Prefer semantic role tokens when they name a reusable component role. Use a direct value or component-specific token when the value is genuinely local or an exception requires local control.
```

Rationale: The exact local pair supports consistency only; Material Web’s direct-value option limits universality.

Owners: Design skill maintainer; CDC review.


## ACT-05 — knowledge/design/SKILL.md:249–249

Units: A014
Boundary units: B001 — retain the palette decision for T/L review; portable recommendations honor the recorded C&B removal decision.

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`; inclusive lines `249–249`.

Complete old target:
```text
| 3 | **Unconstrained colour** — too many unrelated hues | One accent hue per site + brand browns + warm neutrals. Semantic tokens only. |
```

Proposed replacement (verbatim):
```text
| 3 | **Unconstrained colour** — too many unrelated hues | Use a deliberate palette to constrain unrelated hues. Prefer semantic tokens for shared roles, with documented local exceptions. |
```

Rationale: The palette clause belongs to T/L review and the Operator’s C&B removal decision; semantic-token preference remains local and qualified.

Owners: Design skill maintainer; T/L palette review; CDC review.


## ACT-06 — knowledge/design/SKILL.md:368–368

Units: A016

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63`; inclusive lines `368–368`.

Complete old target:
```text
- **The token architecture IS the separation of concerns** — primitives are type definitions, semantic tokens are interfaces, component tokens are implementations.
```

Proposed replacement (verbatim):
```text
A token architecture can illustrate separation of concerns: reusable values, role names, and component choices serve different purposes. This is an analogy only; it is not a formal equivalence to types, interfaces, or implementations and does not guarantee propagation or legibility.
```

Rationale: The source claims formal equivalence and guaranteed outcomes. The replacement retains the analogy with its limits.

Owners: Design skill maintainer; T review for broader theory.


## ACT-07 — knowledge/design/guides/colour.md:14–14

Units: A017

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `7187dabc5ca00d5d7c48c2a70dd2155731cbf68716c7cb8b1a0d3579285a0aea`; inclusive lines `14–14`.

Complete old target:
```text
[OKLCH]{.tag} [DTCG-aligned]{.tag} [3 sites, 1 system]{.tag}
```

Proposed replacement (verbatim):
```text
[OKLCH]{.tag}
```

Rationale: Remove the unsupported DTCG-alignment and C&B site/system status tags. Keep the OKLCH tag only while the local guide’s content supports it.

Owners: Colour guide maintainer; T/source validation owner.


## ACT-08 — knowledge/design/guides/colour.md:236–238

Units: A020, A022

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `7187dabc5ca00d5d7c48c2a70dd2155731cbf68716c7cb8b1a0d3579285a0aea`; inclusive lines `236–238`.

Complete old target:
```text
Role-based aliases that all three sites share. The primitive tokens
(brand-700, neutral-200) get mapped to purpose-based names. This is the
DRY layer --- change one mapping, every site updates.
```

Proposed replacement (verbatim):
```text
Role-based aliases can map reusable values to shared roles. Map each site’s values to the roles its consumers use. A change propagates only to consumers whose references resolve through that mapping; check theme mappings and component coverage for each site.
```

Rationale: The old “every site updates” promise omitted reference resolution and complete consumer coverage.

Owners: Colour guide maintainer; CDC review; Arc03 if accessibility claims are added.


## ACT-09 — knowledge/design/guides/colour.md:564–567

Units: A034, T001

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `7187dabc5ca00d5d7c48c2a70dd2155731cbf68716c7cb8b1a0d3579285a0aea`; inclusive lines `564–567`.

Complete old target:
```text
**The token architecture follows DTCG:** Primitive tokens (`brand-700`)
→ semantic tokens (`interactive-primary`) → component tokens (to come,
e.g. `button-primary-bg`). This three-tier stack is what Material
Design, Carbon, and Polaris converge on.
```

Proposed replacement (verbatim):
```text
This guide chooses reusable primitive values, semantic aliases for shared roles, and optional component bindings for local control. DTCG 2025.10 specifies interchange structure and token types; it does not require this layer count. Name the exact product generation and token category before claiming that Material, Carbon, or Polaris converges on this model.
```

Rationale: The old sentence attributes a local choice to DTCG and asserts convergence without the needed generation-specific primary passages.

Owners: Colour guide maintainer; CDC review; Arc03 if accessibility claims are added.


## ACT-10 — knowledge/design/guides/design.md:61–65

Units: T002, T003, A035

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `61–65`.

Complete old target:
```text
The three most influential design systems of the current era ---
Google\'s Material Design, IBM\'s Carbon, and Shopify\'s Polaris ---
were built independently, by different teams, for different products,
serving different users. And yet they converged on the same fundamental
architecture.
```

Proposed replacement (verbatim):
```text
Material Design, Carbon, and Polaris refer to distinct products and generations. Compare their token models only after naming the product, generation, page date, and exact token category; the examples do not establish a universal layer count.
```

Rationale: This removes unsupported influence ranking, historical independence and named-trio convergence while retaining a bounded comparison route.

Owners: Design guide maintainer; CDC re-entry for Material 3 and historical Polaris evidence.


## ACT-11 — knowledge/design/guides/design.md:67–68

Units: A037

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `67–68`.

Complete old target:
```text
All three define a layered token system: primitive values at the base,
semantic aliases in the middle, component-specific bindings at the top.
```

Proposed replacement (verbatim):
```text
Token systems can arrange reusable values, semantic aliases, and component bindings in different ways. These examples do not establish that every system uses all three layers.
```

Rationale: The named trio remains unestablished; Fluent 2 does not decide it.

Owners: Design guide maintainer; CDC re-entry for Material 3 and historical Polaris evidence.


## ACT-12 — knowledge/design/guides/design.md:74–78

Units: A042, A043
Boundary units: A044, A045 — preserve typography and colour propositions for T/L review.

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `74–80`.

Complete old target:
```text
This convergence is not coincidence. It is the signature of underlying
mathematical structure asserting itself through independent discovery
--- the same way calculus was discovered independently by Newton and
Leibniz, because the problems they were solving demanded it. The
problems of visual consistency at scale demand token architecture. The
problems of typographic hierarchy demand geometric progression. The
problems of colour harmony demand perceptually uniform spaces.
```

Proposed replacement (verbatim):
```text
Token architecture is one way to manage visual consistency at scale; these examples do not establish that it is necessary. The problems of typographic hierarchy demand geometric progression. The problems of colour harmony demand perceptually uniform spaces.
```

Rationale: This replaces the token-necessity and calculus analogy while retaining the typography and colour sentences verbatim for their T/L owners.

Owners: Design guide maintainer; CDC re-entry for Material 3 and historical Polaris evidence.


## ACT-13 — knowledge/design/guides/design.md:160–163

Units: A048, A049, A050

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `160–163`.

Complete old target:
```text
A colour called `brand-700` describes what it is. A colour called
`interactive-primary` describes what it does. Both are necessary, but
they serve different functions in the system, and conflating them is the
single most common architectural error in design token systems.
```

Proposed replacement (verbatim):
```text
Primitive-value names and semantic-role names can serve different purposes. Use a role alias when shared meaning, reuse, or theme variation warrants it; retain a direct value when it is genuinely local. Do not call either pattern necessary or the most common error without scoped evidence.
```

Rationale: The source’s “both are necessary” and frequency superlative lack general evidence; the replacement states a conditional local choice.

Owners: Design guide maintainer; CDC review; T review for theory claims.


## ACT-14 — knowledge/design/guides/design.md:165–173

Units: A052, A053, A054, A055, A056, A057

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `165–173`.

Complete old target:
```text
The three-tier token architecture --- primitive, semantic, component ---
is not a convention. It is the design equivalent of the separation of
concerns that every competent software architecture enforces. Primitives
are your type definitions. Semantic tokens are your interfaces.
Component tokens are your implementations. Changing a primitive\'s value
propagates automatically. Renaming a semantic token requires deliberate
refactoring. This is not a limitation; it is a feature. It means the
system is legible in the same way that well-structured code is legible:
you can understand any part of it without understanding all of it.
```

Proposed replacement (verbatim):
```text
A token system may use reusable reference values, semantic aliases, and optional component-specific bindings. The number of layers depends on consumers, theme variation, local exceptions, tooling, and maintenance cost. This can illustrate separation of concerns: values, roles, and component choices serve different purposes. The analogy does not equate these categories with programming-language types, interfaces, or implementations. A value change reaches consumers only when their references resolve through it; renaming requires updating affected references and tools. These choices can aid legibility, but layering alone does not guarantee it.
```

Rationale: This keeps the useful policy and analogy while removing mandatory architecture, unconditional propagation, and untested legibility guarantees.

Owners: Design guide maintainer; CDC review; T review for theory claims.


## ACT-15 — knowledge/design/guides/design.md:175–180

Units: A059, A060, A061, A062

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `175–180`.

Complete old target:
```text
**The practical implication:** never write
`background: var(--brand-700)` in a component. Write
`background: var(--interactive-primary)`. When the brand evolves, the
interactive colour changes in one place. When a new site joins the
system, it maps its own primitives to the same semantic tokens and
inherits every component for free.
```

Proposed replacement (verbatim):
```text
For components, prefer a semantic alias when it names a shared role. A direct component value can be appropriate for a genuinely local choice. A semantic mapping affects consumers that resolve through it; a new site needs explicit role mappings and component coverage. Check consumers before claiming inheritance or propagation.
```

Rationale: This preserves the practical guidance but removes “never,” “in one place,” and “for free” guarantees.

Owners: Design guide maintainer; CDC review; T review for theory claims.


## ACT-16 — knowledge/design/guides/design.md:329–332

Units: A063, A064

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `329–332`.

Complete old target:
```text
This is also why the convergence of Material Design, Carbon, and Polaris
is significant. These systems were built by teams with different
aesthetic preferences, different brand requirements, different technical
constraints. What they share is not style but structure. The structure
```

Proposed replacement (verbatim):
```text
Material Design, Carbon, and Polaris cover different products and generations. Any token-structure comparison must name the version and token category; the available examples do not establish that the systems share one architecture.
```

Rationale: The source’s named-system convergence and “structure, not style” claim is not supported by the accessible generation-specific evidence.

Owners: Design guide maintainer; T/L for perception; CDC re-entry for unavailable generations.


## ACT-17 — knowledge/design/guides/design.md:371–376

Units: A067, A068, A070

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b`; inclusive lines `371–376`.

Complete old target:
```text
**The design token specification (DTCG)** is not a file format. It is a
contract --- an agreement that the same semantic name means the same
thing in every context, on every platform, in every tool. A token file
is to a design system what a type signature is to a function: a
guarantee about the shape of the input and the shape of the output,
independent of implementation.
```

Proposed replacement (verbatim):
```text
DTCG 2025.10 defines a JSON interchange format for design tokens. It specifies token structure and types; design systems define semantic names for their own contexts. The format does not guarantee identical role meaning or input/output behavior across platforms and tools. Validate an actual exported file against the selected DTCG version before claiming conformance.
```

Rationale: DTCG defines file format and typing, not cross-platform semantic equivalence or a type-signature guarantee.

Owners: Design guide maintainer; CDC reviews attribution; T/source owner validates any future export.


## ACT-18 — knowledge/design/guides/foundations-of-design.md:107–111

Units: A081, A082
Boundary unit: A080 — retain the documentation-category statement for L/Arc04 review.

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `f4cff1c1edc0ece2a368ff81f3bb1909db9b50c1767281300223f88b83f54aa4`; inclusive lines `106–111`.

Complete old target:
```text
**Universal visual style categories** across all five systems: colour,
typography, spacing/layout, motion, icons, and elevation/depth. The W3C
Design Tokens Community Group published its first stable specification
(October 2025) defining seven primitive types (colour, dimension,
fontFamily, fontWeight, duration, cubicBezier, number) and six composite
types (shadow, typography, border, gradient, transition, strokeStyle).
```

Proposed replacement (verbatim):
```text
**Universal visual style categories** across all five systems: colour, typography, spacing/layout, motion, icons, and elevation/depth. DTCG 2025.10 is a Final Community Group Report; its Status section calls it stable and intended for implementation and says it is not a W3C Standard or Standards Track document. It defines primitive and composite token types, including typography. “First” requires historical evidence beyond this report.
```

Rationale: The existing documentation-category sentence remains intact for L/Arc04. The DTCG status and type claim are corrected without conflating stability with W3C standards status.

Owners: Foundations guide maintainer; CDC/T for historical priority and type-list verification.


## ACT-19 — knowledge/design/guides/foundations-of-design.md:465–465

Units: A085

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `f4cff1c1edc0ece2a368ff81f3bb1909db9b50c1767281300223f88b83f54aa4`; inclusive lines `465–465`.

Complete old target:
```text
## Notation Conventions Converge on Three-Tier Token Architecture
```

Proposed replacement (verbatim):
```text
## Token architecture choices
```

Rationale: The prior heading asserts convergence before the section supplies evidence; the replacement names the subject without implying a population result.

Owners: Design guide maintainer; CDC reviews attribution; T/source owner validates any future export.


## ACT-20 — knowledge/design/guides/foundations-of-design.md:471–475

Units: A092

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `f4cff1c1edc0ece2a368ff81f3bb1909db9b50c1767281300223f88b83f54aa4`; inclusive lines `471–475`, literal offsets [52, 271].

Complete old target:
```text
The dominant pattern
is a **three-tier token architecture**: primitive tokens
(`color.blue.500`) → semantic tokens (`color.primary`,
`color.surface.default`) → component tokens
(`color.button.primary.background.hover`).
```

Proposed replacement (verbatim):
```text
One possible token notation uses primitive values (`color.blue.500`), semantic aliases (`color.primary`, `color.surface.default`), and component bindings (`color.button.primary.background.hover`). These examples do not establish that three tiers are the dominant industry pattern.
```

Rationale: The complete naming example is retained, but selected examples cannot establish the “dominant” frequency claim. The adjacent OKLCH/CSS support claims remain with T/L.

Owners: Design guide maintainer; CDC reviews attribution; T/source owner validates any future export.


## ACT-21 — knowledge/design/guides/foundations-of-design.md:495–500

Units: A106, A107, A108

Old source: SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; SHA-256 `f4cff1c1edc0ece2a368ff81f3bb1909db9b50c1767281300223f88b83f54aa4`; inclusive lines `495–500`.

Complete old target:
```text
The DTCG specification defines typography as a composite token type
combining fontFamily, fontSize, fontWeight, lineHeight, and
letterSpacing. Material Design 3 uses category × size naming:
`typescale-display-large`. Utopia names scale steps numerically
(`--step--2` through `--step-5`) with each step getting its own
`clamp()` declaration.
```

Proposed replacement (verbatim):
```text
The DTCG 2025.10 specification defines typography as a composite token type combining fontFamily, fontSize, fontWeight, lineHeight, and letterSpacing. Utopia’s calculator example uses numbered scale-step names such as `--step--2` and `--step-5`; its method and prefix are configurable. The Material Design 3 category-by-size example is omitted until its primary page is readable and pinned.
```

Rationale: This preserves the DTCG composite and bounded Utopia example, separates their subjects, and does not substitute Material Web for unavailable Material 3 evidence or add arithmetic.

Owners: Design guide maintainer; CDC reviews attribution; T/source owner validates any future export.

## Retained gaps and dependencies

Material 3 overview and both historical Polaris colour passages remain inaccessible. The current Fluent 2 two-layer example does not decide the specific Material/Carbon/Polaris trio. CDC/Operator owns readable, versioned primary bodies and must verify generation and token category before reopening dependent claims. The current DTCG composite statement does not establish original fidelity or a validated export. Utopia step names are assigned only as a configurable example; typography arithmetic remains T/L.

Actions preserve the accepted choices: reference values for reusable inputs, semantic aliases when role meaning/reuse/theme variation justify them, and optional component bindings for local control or exceptions. Propagation requires references, mappings and covered consumers. Direct component values remain a scoped exception where the implementation documents that choice. No source edit, export validation or release claim is authorized here.

## Declared colour-guide context extension

SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`, `knowledge/design/guides/colour.md`, SHA-256 `7187dabc5ca00d5d7c48c2a70dd2155731cbf68716c7cb8b1a0d3579285a0aea`, line `[249,249]`, exact literal `::: sem-name` (context unit A033). This one-line extension resolves the former handoff reference beyond the prepared colour window `[234,248]`. It is block markup, not an assertion or correction target; retain unchanged. The line is separately represented in the inventory as the only context extension.
