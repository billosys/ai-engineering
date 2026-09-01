# Phase 0 - Section 5 - Notation Conventions

## 5. Notation Conventions

### 5.1 Colour Notation

```
# Primary notation: OKLCH for perceptual work, hex for interchange
oklch(72% 0.15 240)          # Preferred: perceptually meaningful
#3B82F6                       # Acceptable: universal interchange
rgb(59, 130, 246)             # Acceptable: when RGB context matters
hsl(217, 91%, 60%)            # Acceptable: when explaining HSL specifically

# Colour relationships: use descriptive labels
complementary(#3B82F6)        # Informal — describe the relationship, show the result
oklch(from var(--base) l c calc(h + 180))  # CSS relative colour syntax

# Contrast ratios
4.5:1 (WCAG AA normal text)   # Always specify the standard
3:1 (WCAG AA large text)
7:1 (WCAG AAA normal text)

# Colour tokens
color.blue.500                # Primitive token (scale position)
color.primary                 # Semantic token (role-based)
color.button.primary.bg       # Component token (specific use)
```

**Convention**: When a concept card discusses colour, always provide the OKLCH representation alongside hex. When discussing colour manipulation (lightening, darkening, shifting hue), use OKLCH because the operations are perceptually meaningful in that space.

### 5.2 Typography Notation

```
# Type properties
font-family: "Inter Variable", system-ui, sans-serif
font-size: 1rem (16px base)
font-weight: 400 (regular) / 500 (medium) / 600 (semibold) / 700 (bold)
line-height: 1.5 (unitless preferred)
letter-spacing: -0.01em (tracking, relative to font size)
measure: 45-75ch (optimal line length)

# Modular scale ratios — always note the musical interval
1.067 (minor second, 15:16)
1.125 (major second, 8:9)
1.200 (minor third, 5:6)
1.250 (major third, 4:5)
1.333 (perfect fourth, 3:4)
1.500 (perfect fifth, 2:3)
1.618 (golden ratio, φ)

# Fluid type (Utopia notation)
clamp(1rem, 0.5rem + 1.5vi, 1.5rem)    # min, preferred, max
--step-0: clamp(...)                     # Base size
--step-1: clamp(...)                     # One step up
--step--1: clamp(...)                    # One step down

# Typography tokens (DTCG composite)
typescale.display.large:
  fontFamily: "Inter Variable"
  fontSize: "--step-4"
  fontWeight: 700
  lineHeight: 1.1
  letterSpacing: "-0.02em"
```

### 5.3 Spacing Notation

```
# Base unit: 4px (0.25rem)
# Primary rhythm: 8px (0.5rem)
# Scale: geometric progression or constrained set

# Constrained scale (Refactoring UI approach)
4px / 8px / 12px / 16px / 24px / 32px / 48px / 64px / 96px / 128px

# Token naming: t-shirt sizing
space-2xs: 4px    (0.25rem)
space-xs:  8px    (0.5rem)
space-s:   12px   (0.75rem)
space-m:   16px   (1rem)
space-l:   24px   (1.5rem)
space-xl:  32px   (2rem)
space-2xl: 48px   (3rem)
space-3xl: 64px   (4rem)

# Semantic aliases
spacing.inset.sm:     8px     # Internal padding, all sides
spacing.inset.md:     16px
spacing.inline.sm:    8px     # Horizontal spacing between inline elements
spacing.stack.md:     16px    # Vertical spacing between stacked elements
spacing.section:      64px    # Between major page sections

# Nathan Curtis inset variants
inset:                16px all sides
inset-squish:         8px top/bottom, 16px left/right
inset-stretch:        16px top/bottom, 8px left/right
```

### 5.4 Responsive Notation

```
# Breakpoint naming (when breakpoints are used)
sm:   640px
md:   768px
lg:   1024px
xl:   1280px
2xl:  1536px

# Fluid ranges (Utopia approach — preferred)
clamp(min-value, preferred-calc, max-value)
# where preferred-calc = intercept + slope × 100vi

# Container queries
@container (min-width: 400px) { ... }
# Container units: cqw, cqh, cqi, cqb

# Cascade layers
@layer reset, base, components, utilities;
```

### 5.5 Mathematical Notation

When concept cards include mathematical formulations (and they should, for this user), use these conventions:

```
# Fitts's Law
MT = a + b × log₂(1 + D/W)
  where MT = movement time, D = distance, W = target width
  ID = log₂(1 + D/W) [bits]
  TP = ID/MT [bits/s]

# Hick's Law
RT = a + b × log₂(n + 1)
  General: RT = a + b × H where H = -Σ pᵢ log₂(pᵢ)

# Stevens's Power Law
ψ = k × Iⁿ
  Visual area: n ≈ 0.7 (compressive)
  Brightness: n ≈ 0.33
  Line length: n ≈ 1.0 (nearly veridical)

# Weber-Fechner
ΔI/I = k (Weber fraction)
  Line length: k ≈ 0.03
  Weight: k ≈ 0.02

# Gestalt proximity (Kubovy & Wagemans Pure Distance Law)
log[p(b)/p(a)] = -α × (|b|/|a| - 1)
  where α ≈ 3 (attraction constant)

# Colour space transforms
[X,Y,Z]ᵀ = M₁ × [R,G,B]ᵀ     # sRGB to XYZ (3×3 matrix multiply)
[L,M,S]ᵀ = M₂ × [X,Y,Z]ᵀ     # XYZ to LMS
[l,a,b]  = f(∛L, ∛M, ∛S)       # LMS to Oklab (cube root + matrix)
```

### 5.6 Slug Naming Conventions

```
# Generic slugs — for universal concepts
hue                        # The concept of hue exists across all colour systems
chroma                     # Munsell uses it, OKLCH uses it, it's universal
complementary-colours      # Universal relationship
visual-hierarchy           # Universal design principle
modular-type-scale         # Universal typographic technique

# Source-prefixed slugs — for system-specific constructs
munsell-hue-circle         # Munsell's specific 5-principal-hue, 100-step circle
munsell-notation           # The H V/C notation system
munsell-colour-solid       # The specific 3D model
itten-seven-contrasts      # Itten's specific classification
albers-transparency        # Albers's specific exercise/principle

# The test
# Ask: "Would this concept exist with the same definition outside this system?"
# YES → generic slug
# NO  → source-prefixed slug

# Boundary case: when a source gives a specific definition to a universal concept
# Use the generic slug, document the source-specific definition in the card body
# The harmonisation phase reconciles multiple definitions
```
