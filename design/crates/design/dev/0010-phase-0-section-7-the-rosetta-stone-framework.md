# Phase 0 - Section 7 - The Rosetta Stone Framework

## 7. The Rosetta Stone Framework

### 7.1 Purpose

The Rosetta Stone is not a separate section of the knowledge base — it is a *dimension* woven into every relevant concept card. When a concept has a rigorous analogue in mathematics, music theory, or software engineering, the concept card should note this in its Context & Application section and use `related` links to concept cards in those other domains (where they exist in the user's other knowledge bases).

### 7.2 Rigour Classification

Every cross-domain mapping MUST be classified:

| Rating | Meaning | Criteria |
|--------|---------|----------|
| **RIGOROUS** | Identical mathematical structure or direct implementation | The same equations, data structures, or formal properties apply in both domains. Not an analogy — an isomorphism or implementation. |
| **STRUCTURAL** | Meaningful parallel with practical value | Similar structural relationships operating through different mechanisms. Useful for building intuition but not formally equivalent. |
| **LOOSE** | Suggestive but not formally grounded | Metaphorical connection that may aid memory but should not be relied upon for reasoning. |

### 7.3 Known Cross-Domain Mappings

#### Software Engineering → Design (RIGOROUS — implementations, not analogies)

| Engineering Concept | Design Concept | Rating | Notes |
|-------------------|----------------|--------|-------|
| Abstraction / named constants | Design tokens | RIGOROUS | Identical concept: name a decision, reference the name |
| DRY / single source of truth | Token repository (JSON/YAML) → Style Dictionary | RIGOROUS | Same architecture: one definition, multiple outputs |
| API design (types, defaults, contracts) | Component props interface | RIGOROUS | `<Button variant="primary" size="lg">` IS an API |
| Composition over inheritance | Every Layout's CSS approach; component composition | RIGOROUS | GoF principle applied to CSS and component architecture |
| Dependency injection / IoC | CSS custom properties (cascade) | RIGOROUS | Properties injected at root, consumed by children |
| Semantic versioning | Design system versioning and breaking changes | RIGOROUS | Same governance problem, same solution pattern |
| Linting / static analysis | Design linting (Figma plugins, Stylelint) | RIGOROUS | Automated enforcement of conventions |
| Type systems / interfaces | Token types (DTCG spec: colour, dimension, etc.) | RIGOROUS | Tokens have types, constraints, and composition rules |
| Refactoring | Design system migration / token consolidation | STRUCTURAL | Similar intent (improve without changing behaviour) but different verification methods |

#### Music Theory → Design (Mixed — some rigorous, some structural)

| Music Concept | Design Concept | Rating | Notes |
|--------------|----------------|--------|-------|
| Musical intervals (4:3, 3:2) | Modular type scale ratios | RIGOROUS | Identical mathematics. Tim Brown explicitly adopted these ratios. |
| Equal temperament (12-TET: 2^(1/12)) | Perceptual uniformity in colour spaces (CIELAB, OKLAB) | RIGOROUS | Solving the identical problem: uniformising a perceptually non-uniform space. The deepest bridge. |
| Linear algebra in audio (DFT, spectral analysis) | Linear algebra in colour (3×3 matrix transforms between colour spaces) | RIGOROUS | Both are linear algebra over perceptual spaces. |
| Rhythm (temporal patterns of strong/weak beats) | Visual rhythm (spatial patterns of emphasis/rest) | STRUCTURAL | Same structural concept, different perceptual modalities (temporal vs. spatial). |
| Tension-resolution (dominant → tonic) | Visual tension-resolution (problem → CTA, scroll → reveal) | STRUCTURAL | Analogous narrative/emotional arc, different mechanisms. |
| Dynamics (pp to ff as expressive range) | Visual emphasis scale (whisper to shout in visual weight) | STRUCTURAL | Similar concept of expressive range within a system. |
| Counterpoint (independent voices in relationship) | Typographic counterpoint (independent type elements creating a unified composition) | STRUCTURAL | Similar structural ideal, very different implementation. |
| Harmonic relationships (consonance/dissonance) | Colour harmony (complementary/analogous/triadic) | LOOSE | 12-hue wheel / 12-semitone parallel is suggestive but trichromatic vs. frequency-analytic perception means the mathematics diverge. Useful for intuition, not for rigorous reasoning. |
| Key/tonality (tonal centre organising other pitches) | Colour palette anchor (primary colour organising other palette colours) | LOOSE | Suggestive organisational parallel but no formal equivalence. |

#### Mathematics → Design (RIGOROUS where applicable)

| Math Concept | Design Concept | Rating | Notes |
|-------------|----------------|--------|-------|
| Group theory: 17 wallpaper groups | Classification of all possible 2D repeating patterns | RIGOROUS | Mathematical theorem (Fedorov, 1891). Any `background-repeat` pattern is in one of these groups. |
| Group theory: 7 frieze groups | Classification of all possible border/strip patterns | RIGOROUS | Same theorem applied to 1D periodicity. |
| Crystallographic restriction | Only 2-, 3-, 4-, 6-fold rotational symmetries in periodic lattices | RIGOROUS | Explains why 5-fold symmetry requires aperiodic structures (Penrose tilings). |
| Geometric sequences | Modular type scales and spacing scales | RIGOROUS | Scale = base × ratio^step. |
| Linear interpolation | CSS `clamp()` for fluid responsive values | RIGOROUS | `clamp()` literally computes lerp between viewport bounds. |
| 3×3 matrix multiplication | Colour space conversions (sRGB↔XYZ↔LMS↔Oklab) | RIGOROUS | Grassmann's additivity law means the chain collapses to a single matrix. |
| Exponential decay | Gestalt proximity grouping (Kubovy & Wagemans) | RIGOROUS | Pure Distance Law: log[p(b)/p(a)] = -α × (|b|/|a| - 1). |
| Persistent homology (algebraic topology) | Unified computational framework for proximity + closure | RIGOROUS | Chen et al. (2024): Vietoris-Rips filtrations. 0-dim = proximity, 1-dim = closure. |
| Information theory (Shannon entropy) | Hick's Law (decision time as function of choice entropy) | RIGOROUS | RT = a + b × H, where H = -Σ pᵢ log₂(pᵢ). Fitts's Law derives from Shannon channel capacity. |
| Power laws (Stevens) | Perceptual scaling of visual properties | RIGOROUS | ψ = k × Iⁿ. Visual area: n ≈ 0.7. Brightness: n ≈ 0.33. |
| Weber fractions | Just-noticeable differences in design (spacing, sizing) | RIGOROUS | ΔI/I = k. Line length k ≈ 0.03. |

### 7.4 Implementation in Concept Cards

When a concept card has a Rosetta Stone mapping, include it in the **Context & Application** section using this format:

```markdown
## Cross-Domain Connections

**[Source Domain] → [Rating]**: [Description of the mapping].
[1-2 sentences explaining why this mapping holds (if RIGOROUS) or where it breaks down (if STRUCTURAL/LOOSE).]
```

Example for a `modular-type-scale` concept card:

```markdown
## Cross-Domain Connections

**Music Theory → RIGOROUS**: Modular type scale ratios are identical to musical intervals.
A perfect fourth type scale (ratio 1.333) means each step is exactly 4:3 of the previous,
the same ratio that defines the musical perfect fourth. Tim Brown explicitly adopted these
ratios from Bringhurst, who drew from centuries of typographic proportion. A music theorist
immediately understands that a perfect-fourth type scale produces perceived proportional
harmony for the same reason the interval does — small-integer ratios.

**Mathematics → RIGOROUS**: A modular scale is a geometric sequence: size = base × ratio^step.
The entire scale is determined by two parameters (base size and ratio), just as a geometric
series is determined by its first term and common ratio.
```
