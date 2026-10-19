---
concept: "Binocular Disparity and Stereoscopy"
slug: "binocular-disparity"
category: "visual-perception"
subcategory: "depth-cues"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Help From Physical Space"
extraction_confidence: "medium"
aliases:
  - "stereoscopy"
  - "stereoscopic depth"
  - "spatial parallax"
  - "binocular depth cue"
prerequisites:
  - "pictorial-space"
extends: []
related:
  - "overlap-depth-cue"
  - "size-gradient"
  - "depth-gradient-principle"
contrasts_with:
  - "monocular-depth-cues"
answers_questions: []
rosetta_stone:
  -
    domain: "engineering"
    concept: "Stereoscopic 3D displays, VR headsets, anaglyph rendering"
    rating: "rigorous"
    note: "Rigorous only for routing defined distinct views to the eyes. Actual fusion, comfort, accommodation and device performance remain untested."
  -
    domain: "mathematics"
    concept: "Trigonometric parallax — angular difference as function of depth and interocular distance"
    rating: "rigorous"
    note: "For symmetric midline geometry θ(Z)=2atan(b/(2Z)); signed δ=θ(Z)−θ(Zf). The bd/D² expression is a small-baseline, small-offset approximation, not an exact universal retinal formula."
css_implementation: []
---

# Quick Definition

Binocular disparity describes differences between left- and right-eye images. Stereo delivery can use such differences to support a depth percept, but delivery geometry, actual fusion and comfortable viewing are separate questions.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim reports two-eye image differences, eye-alternation demonstrations and Julesz random-dot stereograms. He explains fusion through his simplicity account; that explanation is not newly verified physiology. Spatial/binocular parallax and temporal/motion parallax are related changes of viewpoint, not identical cues. An ordinary single-view image on a flat screen differs from a flat substrate delivering distinct eye views through stereoscopic arrangements. No result here establishes that a particular device supplies accurate or comfortable stereopsis or varying accommodation.

Retained wording from the represented account (original fidelity unassessed):

"When the two eyes look at the same objects, they will receive different images. The two spots will be farther apart for the left eye than for the right eye"

"Confronted by two different images, the sense of sight faces a dilemma. The stimulus pattern recorded by the retinas is invariable, but here again the third dimension offers an avenue of freedom, which permits the fusion of the two flat images into one three-dimensional image. Thus once again, three-dimensionality is brought about by the tendency toward simplification and tension reduction"

# Prerequisites

- **Pictorial Space** — Pictorial spatial readings supply the vocabulary for this particular cue or convention.

# Key Properties

1. Distinct eye views are needed for disparity-based stereo delivery.
2. A fixed physical screen can deliver separated views using suitable optics or viewing arrangements.
3. The sign and reference convention for disparity must be defined.
4. A large unsigned disparity is not a universal nearer rule.
5. Random-dot depth and eye-alternation demonstrations remain source reports.

# Construction / Recognition

## To Construct/Create (for stereoscopic media):

1. Specify left/right eye positions, fixation and projection model.
2. Deliver the intended view to each eye with the actual display arrangement.
3. Evaluate actual fusion, comfort and task performance separately; these checks are unrun here.

## To Identify/Recognise:

1. Distinguish single-view presentation from per-eye delivery.
2. An eye-alternation demonstration can reveal relative angular changes, without measuring fusion.
3. Name the fixation depth and signed convention before interpreting disparity.

# Context & Application

VR, stereoscopes, anaglyphs, 3D cinema and autostereoscopic displays provide delivery examples. There is no CSS feature status for binocular perception itself. CSS can participate in authoring content, but optics/delivery determine which eye receives it. Neither a flat substrate nor a VR label settles the actual percept.

## Cross-Domain Connections

**Engineering → RIGOROUS**, limited to the defined delivery construction: separate specified views can be routed to separate eyes, without guaranteeing observer fusion. **Mathematics → RIGOROUS**, limited to a symmetric midline model: eye baseline b>0, axial target Z>0 and fixation Zf>0 give θ(Z)=2atan(b/(2Z)), signed disparity δ=θ(Z)−θ(Zf). For b=.065m, Zf=1m, Z=.5m gives +.0648402503rad; Z=2m gives −.0324799893rad. For small b/D and a small nearer offset d from fixation D, δ≈bd/D², with sign reversed for a farther offset. This is an approximation, not universal atan(d/D) or a model of all off-axis retinal disparities.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 484): "When the two eyes look at the same objects, they will receive different images. In the present case the two spots will be farther apart for the left eye than for the right eye." — Arnheim

**Example 2** (p. 486): "Confronted by two different images, the sense of sight faces a dilemma... the third dimension offers an avenue of freedom, which permits the fusion of the two flat images into one three-dimensional image." — Arnheim

**Example 3** (p. 152): Citing Bela Julesz: "Stereoscopy also will make a figure-ground effect visible even when it is not seen in the two images singly and when, as Bela Julesz has shown, no contour but merely a slight displacement of texture distinguishes the two areas." — Arnheim

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Pictorial Space** — Compare single-view pictorial cues with per-eye image differences; no all-scene dominance follows.
- **Simplicity Principle** — The represented simplicity explanation is not independently established physiology.

## Enables

- **VR/Stereoscopic Design** — Separate eye views supply a stereo-delivery construction; actual fusion and comfort remain untested.
- **Stereoscopic Depth without Monocular Cues** — Julesz’s random-dot cases remain reported examples requiring original conditions.

## Related

- **Motion Parallax** — Motion parallax changes views over time; it is related, not identical, to eye-separated delivery.
- **Monocular Depth Cues** — The local enumerated monocular family includes overlap, size, atmosphere, perspective, texture and deformation.

## Contrasts With

- **Monocular Depth Cues** (overlap, size gradient, atmospheric perspective, linear perspective, texture gradient, deformation) — That family works without separated eye images; flat substrates can nevertheless deliver stereo using an appropriate arrangement.

# Common Errors

- **Error**: Assuming a flat screen cannot supply stereo, or that every stereo device guarantees depth comfort.
  **Correction**: Inspect per-eye delivery and then the actual observer/device outcome.

- **Error**: Treating VR as a guarantee of accommodation cues or stronger depth.
  **Correction**: Identify what the particular display actually delivers; do not transfer the geometric construction to physiology.

# Common Confusions

- **Confusion**: Blur or motion parallax is binocular disparity.
  **Clarification**: Defocus and temporal viewpoint change are distinct; ordinary single-view pictorial cues do not require separated eye images.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 474–496 (Help From Physical Space section).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from discussion in Chapter V (Space), pp. 474–496
- Confidence rationale: Medium — Arnheim discusses binocular disparity as part of a broader discussion of physiological depth cues; coverage is less extended than for pictorial depth cues
- Uncertainties: Page numbers approximate
- Cross-reference status: Verified
- Rosetta Stone check: Mappings added — VR engineering is rigorous; trigonometric parallax is rigorous
- OCR issues: None significant
