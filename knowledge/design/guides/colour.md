# Colour Choices from Context

Choose colours for the adopting project's content, identity, interface roles and
rendering conditions. This guide supplies a method, not a palette or prescribed
token names. Keep supplied values and semantics unless a specific task or
verified issue calls for a change.

## Start with the supplied context

Identify the task and content, the surfaces users will see, the supplied
identity and tokens, the platform and display conditions, and relevant user
preferences or accessibility targets. Record unknowns. Ask only questions that
could change a consequential choice; otherwise label a task-specific proposal
and its assumptions.

If the project already has semantic tokens, reuse their names and mappings.
A brown palette, a single hue or an existing palette structure can be a valid
choice when the adopting project selects it. Do not infer one from an example.

## Define the roles the task needs

List the actual roles before assigning values. Depending on the interface these
may include:

| Role | Questions to resolve |
|---|---|
| Surfaces | Which page, panel, raised, selected, inverse or overlay surfaces occur? |
| Text and icons | Which foregrounds sit on each surface, and which meaning or state do they carry? |
| Actions and links | Which choices are actionable? How do default, hover, focus, active, visited and unavailable states appear? |
| Boundaries and focus | Which borders, separators, outlines or focus indicators carry information? |
| Themes | Which light, dark, forced-colour or other modes are actually required? |

These names describe questions, not a mandatory semantic vocabulary. Do not
create unused roles or layers merely to match this table.

## Choose candidate values

For text, evaluate each actual foreground/background pair after applying alpha, overlays and the rendered background. Under WCAG 2.2 SC 1.4.3 (AA), target at least 4.5:1 for normal text and 3:1 for large-scale text; SC 1.4.6 (AAA) uses 7:1 and 4.5:1 respectively. For an opaque rendered sRGB pair, normalize each 8-bit channel as `u = channel / 255`, then decode it to linear light: use `u / 12.92` when `u <= 0.04045`, otherwise `((u + 0.055) / 1.055)^2.4`. Calculate relative luminance as `L = 0.2126R + 0.7152G + 0.0722B`, then calculate `(Llighter + 0.05) / (Ldarker + 0.05)`. For example, `#000` against `#fff` is 21:1; `#777` against `#fff` is about 4.4780894536:1 and fails the 4.5:1 normal-text AA threshold without rounding up. WCAG 2.2 defines large-scale text as at least 18 pt or 14 pt bold (with equivalent CJK sizing); AA is 3:1 for it and AAA is 4.5:1, while normal-text AA/AAA are 4.5:1/7:1. See [SC 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum), [SC 1.4.6](https://www.w3.org/TR/WCAG22/#contrast-enhanced), and the WCAG [relative-luminance and contrast-ratio definitions](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). Criterion exceptions still apply. This calculation is for an opaque rendered sRGB pair; resolve alpha, overlays and the actual background first. It does not establish page conformance and does not replace the separate SC 1.4.11 non-text contrast and SC 1.4.1 use-of-colour checks. Do not round a failing value up. Check non-text controls and essential graphics against SC 1.4.11 separately (3:1 against adjacent colours), and do not use colour alone to convey information (SC 1.4.1). Exceptions and applicability depend on the criterion. Recheck hover, focus, disabled and other relevant states in the rendered context; a palette-level result does not establish whole-page accessibility.


Start with supplied tokens and accepted guidance. When values are absent, propose
candidates that fit the identified task, content and identity; state why and
what remains uncertain. OKLCH can help explore lightness, chroma and hue, but
perceived differences depend on context and gamut. A numeric lightness step is
not an exact brightness scale and does not establish contrast.

Check actual rendered foreground/background pairs for text, icons, controls,
focus indicators and each relevant state. Include transparency, gradients,
overlays, blending, compositing and target-device gamut mapping. Check the
result against the project's chosen accessibility target and inspect the
rendered interface; token names and source values alone do not prove legibility
or conformance. Do not claim support for untested displays, themes or user
settings.

## Preserve existing tokens; add aliases only when useful

A token architecture is optional. If the project already has meaningful
semantics, preserve them. If an extra alias would clarify a real boundary, name
the role for its purpose and map it to a supplied value without changing the
underlying identity.

For example, an existing interface might map its supplied `--client-surface`,
`--client-ink` and `--client-action` values to the actual surface, text and
action roles it uses. The action value still needs its supplied foreground and
state values checked as complete pairs. Do not force token renaming or add
primitive, semantic and component layers without a project need.

## Review themes and state pairs

For each theme or mode, enumerate the rendered combinations users encounter:
normal, hover, focus, active, visited, selected and unavailable as applicable.
Check both text and non-text information against the actual surface beneath it,
including nested surfaces and transparency. Recheck after a theme switch,
overlay, animation, image background or gamut conversion changes the pair.
Record the target, method, results, failed pairs and untested cases. A design
tool preview or OKLCH coordinate is not a substitute for these checks.
