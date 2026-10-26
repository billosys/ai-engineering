# Purposeful motion

Use motion only when a task or piece of content benefits from a visible change through time. State the purpose, the property that changes, the state that starts it, and what a person can still understand and do at rest. A movement is optional when labels, focus, order or a persistent marker already communicate the same information; keep that complete resting equivalent.

## Decide whether movement belongs

Begin with the transition, not an effect catalog:

- **Purpose:** What change should the movement help someone notice or relate? If there is no answer beyond “make it lively,” keep the state change immediate.
- **Property:** Does the transition change position, size, shape or bounds, or only a non-spatial effect such as color? A property can look small in code and still create perceptible movement. Do not treat a color or opacity change without perceived movement as the same issue as motion.
- **State and trigger:** Which user action starts the change? Is it a one-time arrival, a repeated step, or an automatic update? Keep the trigger and affected object clear.
- **Rest:** What shows the current state when the animation is absent, unsupported, interrupted or completed? Keep names, essential content, navigation and focus available without waiting for a transition.

A transition can suggest a relation or draw attention, but its presence alone does not establish comprehension, comfort or wayfinding benefit. If immediate focus, reading order, a selected state or a stable accent already serves the task, an added movement may be decorative distraction.

## Keep optional motion finite and controllable

For a non-essential interaction cue, prefer a bounded transition with one clear start and rest state. Avoid perpetual loops, automatic movement, parallax and animated page scrolling when the task works without them. Do not reveal essential copy or controls only during an animation. Content and the next action must remain available at rest and when motion is reduced.

When an effect is optional, provide an understandable way to leave it off. A native control can provide a direct, reversible choice without script or saved preference. Also honor the user agent's `prefers-reduced-motion` result: when it is `reduce`, keep the cue off even if a local opt-in control is selected. The system preference takes priority. Explain the choice beside the control in ordinary language. Avoid implying that a particular duration is comfortable for everyone.

Interruption and reversal need deliberate behavior. Decide whether a new state cancels, replaces or completes an in-flight cue; whether the cue restarts on a new target; and whether reversing direction has a meaningful reverse transition. If an effect is only a one-way arrival accent, say so in the design and keep the final state legible if it is cancelled. Do not promise replay for repeated activation of an unchanged state unless it is actually implemented and checked.

Retain native input and focus. A CSS effect should not intercept links, change focus order, add a delay before the destination works, or make pointer input the only path. If a selector or animation is unsupported, hide any control that would otherwise do nothing and preserve the complete static navigation.

## Example: an optional story-arrival marker

The [image-composition text case](using-the-skill.md#image-composition) records the LFE collection's motion decision. In the earlier runtime, native fragment links and focus stayed immediate. Each story number reserved a small marker before any target state; the selected story received a persistent static gold marker, so the destination remained identifiable without movement. An unchecked “Allow a brief arrival cue” checkbox optionally animated only that marker once as it scaled into its resting size; it did not move the article, photograph or document. The choice was local to the page and was not saved. Unchecking removed the animation immediately while the static target marker remained. The Markdown case does not claim a new runtime execution.

This specimen uses a locally chosen 450 ms ease-out. It is an example parameter, not a timing rule or a comfort guarantee. Motion is available only when the system reports `no-preference`; the control does not override `reduce`. Enabling the checkbox while a story is already the target can start its cue. Moving from one story to another and back rematches the target and cues it again. Re-selecting the same already-active fragment is not promised to replay. Native Back-to-index and the persistent target/focus state continue to work independently.

The AndroidX [Material 3 Compose `MotionScheme.kt` snapshot](https://android.googlesource.com/platform/frameworks/support/+/383a96e0e6e21b2155de1ff320ef3c78f4c288f7/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/MotionScheme.kt) distinguishes spatial specs, which may change a component's shape or bounds, from effects specs that do not, and permits customization at theme or component scope. This is experimental Android Compose Material 3 guidance at a pinned source revision, not a web API. The specimen adapts the property distinction and contextual choice; it does not import the Kotlin API, spring defaults, Material appearance or a universal motion scheme.

[WCAG 2.2 Understanding SC 2.3.3, Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) is a Level AAA criterion about disabling non-essential motion animation triggered by interaction. Its explanation distinguishes this from automatically started animation addressed by SC 2.2.2 Pause, Stop, Hide. It defines motion animation in terms of added steps that create apparent movement; color or opacity changes that do not change perceived size, shape or position are outside that definition. The [CSS Media Queries Level 5 `prefers-reduced-motion` feature](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion) describes the user preference as `no-preference` or `reduce`. These sources inform the local decision; citing or applying them here is not evidence that this specimen or another page conforms.

## Check the actual transition and resting path

Inspect the real target at the sizes, text settings, input paths and preference conditions relevant to the page. Check the transition's first and final frames, its finite end, a changed target, same-target activation, manual interruption, and the persistent rest state. Verify that text, image geometry, focus and native navigation do not depend on animation. Inspect the reduced-motion rule in source and, if useful, use a clearly labelled authored preference fixture; do not describe that as changing the operating system setting.

For this collection, the browser checkpoint observed the actual user agent at `no-preference`. Root exercised the unchecked default, native Space opt-in, fragment arrivals, A→B→A return, Back-to-index focus, immediate manual off and the finite marker state. At 390px and authored 32px text/spacing, the control, stories and navigation remained within the document and the existing images/layout retained their accepted projection. The CSS gate was source-inspected; no native OS `reduce` change was made. Other browser engines, assistive technology, native zoom, participant comfort, repeated same-fragment replay and accessibility conformance were not tested. These bounded observations are not a universal motion recommendation.
