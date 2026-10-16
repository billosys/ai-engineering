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

For text, evaluate each actual foreground/background pair after applying alpha, overlays and the rendered background. Under WCAG 2.2 SC 1.4.3 (AA), target at least 4.5:1 for normal text and 3:1 for large-scale text; SC 1.4.6 (AAA) uses 7:1 and 4.5:1 respectively. Do not round a failing value up. Check non-text controls and essential graphics against SC 1.4.11 separately (3:1 against adjacent colours), and do not use colour alone to convey information (SC 1.4.1). Exceptions and applicability depend on the criterion. Recheck hover, focus, disabled and other relevant states in the rendered context; a palette-level result does not establish whole-page accessibility.


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
