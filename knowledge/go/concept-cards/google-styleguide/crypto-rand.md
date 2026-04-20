---
# === CORE IDENTIFICATION ===
concept: Use crypto/rand for Keys
slug: crypto-rand

# === CLASSIFICATION ===
category: libraries
subcategory: security
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "crypto/rand"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cryptographic randomness"
  - "secure random generation"
  - "crypto/rand vs math/rand"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which random number package should I use for generating keys in Go?"
  - "Why is math/rand unsuitable for key generation?"
  - "How do I generate a random key in Go?"
  - "Is math/rand predictable even when seeded?"
---

# Quick Definition

Use `crypto/rand` instead of `math/rand` for generating keys or any security-sensitive random values. `math/rand` is predictable even when seeded -- unseeded it is completely predictable, and seeded with `time.Nanoseconds()` it has only a few bits of entropy.

# Core Definition

Do not use `math/rand` to generate keys, even throwaway ones. If unseeded, the generator is completely predictable. Seeded with `time.Nanoseconds()`, there are just a few bits of entropy. Instead, use `crypto/rand`'s `Reader` for cryptographically secure randomness, and if you need text output, encode the bytes as hexadecimal or base64.

# Prerequisites

- **Go crypto/rand package** -- Basic familiarity with `crypto/rand.Read`
- **Encoding packages** -- `encoding/hex` or `encoding/base64` for text output

# Key Properties

1. **math/rand is predictable**: Completely predictable when unseeded; only a few bits of entropy when seeded with time
2. **crypto/rand is secure**: Uses the operating system's cryptographic random number generator
3. **Text encoding**: Convert random bytes to hex or base64 for string representation
4. **Even throwaway keys**: The rule applies to all keys, not just production secrets

# Construction / Recognition

## To Apply:
1. Use `crypto/rand.Read(buf)` to fill a byte slice with random data
2. Encode the bytes with `fmt.Sprintf("%x", buf)`, `hex.EncodeToString`, or `base64.StdEncoding.EncodeToString`
3. Handle the (extremely unlikely) error from `rand.Read`

## To Recognize:
1. Code using `math/rand` for key generation is a security issue
2. Code seeding `math/rand` with time for "random" keys is insufficient

# Context & Application

This is a security-critical guideline. Even keys that seem temporary or low-value should use cryptographic randomness because "throwaway" keys can end up persisted, shared, or used in contexts where predictability creates vulnerabilities. The cost of using `crypto/rand` over `math/rand` is negligible for key generation.

# Examples

**Example 1 -- Correct key generation**:

```go
// Good:
import (
    "crypto/rand"
    "fmt"
)

func Key() string {
    buf := make([]byte, 16)
    if _, err := rand.Read(buf); err != nil {
        log.Fatalf("Out of randomness, should never happen: %v", err)
    }
    return fmt.Sprintf("%x", buf)
    // or hex.EncodeToString(buf)
    // or base64.StdEncoding.EncodeToString(buf)
}
```

# Relationships

(No specific related cards in this extraction batch.)

# Common Errors

- **Error**: Using `math/rand` for key generation because it is "fast enough"
  **Correction**: Speed is not the concern; predictability is. Always use `crypto/rand` for keys.

- **Error**: Seeding `math/rand` with time and assuming it is "random enough"
  **Correction**: Time-based seeds provide only a few bits of entropy. Use `crypto/rand`.

# Common Confusions

- **Confusion**: Thinking `math/rand` is acceptable for non-production or test keys
  **Clarification**: The guidance applies even to throwaway keys. Use `crypto/rand` for all key generation.

# Source Reference

Chapter 3: Style Decisions, Section "crypto/rand" under "Common libraries".

# Verification Notes

- Definition source: Directly from the "crypto/rand" section of the Style Decisions document
- Confidence rationale: HIGH -- the guidance is explicit and unambiguous
- Uncertainties: None
- Cross-reference status: Standalone security concept
