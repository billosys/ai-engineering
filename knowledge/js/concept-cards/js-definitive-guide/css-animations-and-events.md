---
concept: CSS Animations and Events
slug: css-animations-and-events
category: browser-apis
subcategory: CSS scripting
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 475
section: "15.4.5 CSS Animations and Events"
extraction_confidence: high
aliases:
  - CSS transitions
  - transitionend event
prerequisites:
  - classlist
  - addeventlistener
extends: []
related:
  - element-style-property
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

CSS transitions and animations can be triggered by JavaScript (typically by adding/removing classes), and their progress can be monitored through events like "transitionend", "transitionstart", "animationstart", "animationend", and "animationiteration".

# Core Definition

CSS transitions animate property changes over time (e.g., opacity changing over 0.5 seconds). JavaScript triggers these by adding/removing CSS classes via `classList`. Transition events include "transitionrun", "transitionstart", and "transitionend" with `propertyName` and `elapsedTime` properties. CSS animations (using @keyframes) fire "animationstart", "animationend", and "animationiteration" events with `animationName` and `elapsedTime` properties (Flanagan, Ch. 15, pp. 475-476).

# Prerequisites

- **classlist** — Triggering animations by adding/removing CSS classes.
- **addeventlistener** — Listening for animation events.

# Key Properties

1. `transition` CSS property defines which properties to animate and their duration.
2. Adding/removing classes with `classList` triggers transitions on changed properties.
3. "transitionend" fires when a CSS transition completes.
4. "animationend" fires when a CSS animation completes.
5. Event objects include `propertyName` (transitions) or `animationName` (animations) and `elapsedTime`.

# Construction / Recognition

```css
.fadeable { transition: opacity .5s ease-in; }
.transparent { opacity: 0; }
```
```javascript
document.querySelector("#subscribe").classList.add("transparent");
// Element fades out over 0.5 seconds
```

# Context & Application

CSS handles the animation; JavaScript triggers it and monitors completion. This separation keeps animation logic in CSS while JavaScript controls timing and state.

# Examples

From the source (p. 475): Adding the "transparent" class to a "fadeable" element triggers a smooth opacity transition. Removing it fades the element back in.

# Relationships

## Builds Upon
- **classlist** — Triggers animations by class changes
- **addeventlistener** — Monitors animation events

## Enables
- Smooth UI transitions without JavaScript animation loops

## Related
- **element-style-property** — Alternative for per-element inline style changes

## Contrasts With
- (None)

# Common Errors

- **Error**: Expecting JavaScript to drive the animation frame-by-frame.
  **Correction**: CSS transitions handle the animation natively; JavaScript only triggers and monitors them.

# Common Confusions

- **Confusion**: CSS transitions and CSS animations are the same thing.
  **Clarification**: Transitions animate between two states on property change. Animations use @keyframes for complex multi-step sequences.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.4.5, pages 475-476.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear examples of both transitions and animations
- Uncertainties: None
- Cross-reference status: Verified
