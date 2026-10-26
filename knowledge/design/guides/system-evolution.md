# Evolve a Semantic Design System in Context

Change a design system from its adopting project's real roles, consumers and
mode behavior. Treat another system as evidence to adapt, not a replacement
contract. Keep every change attributable to an owner and useful rendered
state.

## Start with the adopting contract

Read the project's existing token definitions, state selectors, component
styles and actual rendered consumers before choosing values. Record the exact
role, property, value, owner, mode scope and consuming elements. Distinguish a
base value from a semantic alias and from a component-specific role. Trace the
alias to rendered controls and content; a declaration with a familiar name
does not prove that the target UI uses it.

Treat a mode as a visual-state choice within the same product profile. A user
or system profile can select a different product context or identity; a light
or dark mode changes the presentation contract for the current context. Keep
the source of the choice explicit and do not infer locale, language or writing
direction from a visual mode. Preserve `lang` and `dir` in markup, and use
logical properties such as `margin-inline-start` when layout should follow
writing direction. CSS should not set the document's base direction. See the
W3C [HTML direction and logical-properties guidance](https://www.w3.org/International/questions/qa-html-dir.en.html).

Build a small ownership map before editing:

| Item | Record |
|---|---|
| Semantic role | What user-facing purpose does this value serve? |
| Type and value | Which CSS property consumes it, and what value is expected in each mode? |
| Owner and scope | Which component or system layer may change it, and where is it defined? |
| Alias and consumers | Which semantic name resolves to it, and which rendered elements use that name? |
| Exception | Which component keeps a distinct value, why, and what impact would changing it have? |

Add a role or alias only when it names a real purpose and has identified
consumers. Preserve established names where they already express the contract.
For an intentional exception, record its owner, reason, affected consumers,
review condition and rollback. Avoid replacing matching literals globally:
equal values can belong to different roles and owners.

## Learn from another system without importing its contract

State which part of the source system applies to the adopting task and which
part does not. Fluent 2 describes global, context-agnostic values and alias
tokens that name a purpose; it also describes theming support as part of its
own design system. An adopting project can reuse that distinction between raw
values and role aliases without imposing Fluent's two-layer structure on the
adopting project,
corporate values or accessibility claims. The project's existing structure,
identity and acceptance target remain authoritative. See [Fluent 2's token
model](https://fluent2.microsoft.design/design-tokens).

## Define mode scopes and propagation

List the required visual modes and the existing mechanism that selects each
one. Change only values owned by the mode contract. Define an alias in each
mode scope where its consumers resolve it; do not rely on a parent alias to
re-resolve against a descendant's changed base value. CSS custom properties
are substituted at computed-value time before inheritance, so an inherited
alias can carry the value resolved in its defining scope. Inspect the actual
consumer after each mode switch.

Keep appearance modes separate from other rendering conditions. Forced-colour
settings, increased contrast, reduced motion, user zoom and input modality
need their own implementation and checks when the product supports them.
Never treat a dark class as evidence that these settings have been handled.
Preserve native controls, keyboard operation and visible focus; show state with
labels, underlines, shape or another suitable signal as well as colour.

## Respect CSS value and cascade behavior

CSS custom properties accept token streams without validating whether they
match the type required by a later property. A missing reference without a
usable fallback, or a dependency cycle, invalidates the dependent custom
property. A wrong-typed value can
survive as a custom property, then invalidate the consuming property at
computed-value time. When that happens, an earlier cascaded declaration is not
restored. A `var()` fallback handles an unavailable reference; it does not
validate a type. Validate both that the custom property resolved and that the
consuming property has the expected computed value. See the W3C [CSS Custom
Properties specification](https://www.w3.org/TR/css-variables-1/), especially
[dependency cycles](https://www.w3.org/TR/css-variables-1/#cycles) and
[invalid variables](https://www.w3.org/TR/css-variables-1/#invalid-variables).

When a utility framework exposes CSS variables, inspect its mapping semantics.
For example, Tailwind's `@theme inline` inlines a referenced variable's value
into generated utilities so a utility can use a value from the local scope.
Preserve a working mapping unless the consumer proves it needs to change; see
[Tailwind's variable-reference guidance](https://tailwindcss.com/docs/theme#referencing-other-variables).

## Compare actual rendered pairs and states

Choose each foreground and background from the real rendered context. Resolve
alpha and overlay layers first. Calculate opaque sRGB text pairs independently;
inspect focus and essential boundaries as non-text information separately.
Record the element, role, state, computed colors, resolved surface, ratio,
rendering assumptions and result. Include ordinary, hover, focus, visited,
active and disabled states where present. Compare before and after values and
check that unrelated semantic roles stay unchanged.

The [supplied-identity text case](using-the-skill.md#supplied-identity) records
the small LFE mode-study witness for this method. The original runtime projected
four before/after light/dark states with panel-local aliases, native links and
controls, and an unchanged code-component exception; it was not a full site copy
or generic palette. In the LFE change, only the
ordinary interactive accent moves from `#705406` to `#624900` in light mode and
from `#e9ca66` to `#f0d477` in dark mode. The existing `--lfe-link` and
`--lfe-focus` roles refer to that alias in both scopes. Code links and focus
remain explicit `#e9ca66` on `#1e293b` because the code surface has a separate
component owner.

When a team needs to carry a semantic role change to another owner or
implementation, continue with [Migrate a Semantic Design System Between
Owners](system-migration.md) and its [filled LFE handoff](examples/lfe-system-handoff.md).
Use that route to preserve compatible names, make mode-resolved values and
component exceptions explicit, and bound the receiving team's first use and
rollback.

The proposed opaque pairs calculate to 8.14279:1 (`#624900` on `#fcfaf5`),
8.49394:1 (`#624900` on `#ffffff`), 11.76074:1 (`#f0d477` on `#151c24`),
10.36280:1 (`#f0d477` on `#1d2732`) and 9.12888:1 for the unchanged code pair
(`#e9ca66` on `#1e293b`). These are pair calculations, not whole-page
conformance. The native browser checkpoint verified the current LFE link and
focus colors in both modes, the unchanged code outline, keyboard use and a
temporary English `dir="rtl"` layout diagnostic at 390px. That layout check is
not Arabic-language, shaping, IME or script validation. It did not test forced colours,
assistive technology, native zoom, other browser engines, user research or
conformance. Existing Arabic wording was unchanged; this work adds no
translation or language review.

## Review, document and roll back

Review the source diff and rendered result together. Confirm that only intended
owners changed, aliases resolve in every required scope, the exception remains
separate, and relevant keyboard states still work. Check a narrow layout and
one direction change when logical layout is part of the contract; these checks
do not stand in for language or script review. Record unknown modes and
untested conditions plainly.

Keep the rollback local and explicit: restore the previous semantic value and
its prior alias mapping while preserving component exceptions and unrelated
tokens. Link the decision method to its runnable witness and route it from the
existing colour and design entrypoints so future changes can repeat the same
consumer, ownership and state checks.
