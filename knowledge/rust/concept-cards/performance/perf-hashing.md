---
concept: Hashing Performance
slug: perf-hashing
category: performance
subcategory: data-structures
tier: intermediate
source: "The Rust Performance Book"
source_slug: performance
authors: "Nicholas Nethercote et al."
chapter: "Hashing"
chapter_number: 6
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "hash map performance"
  - "FxHashMap"
  - "FxHashSet"
  - "rustc-hash"
  - "ahash"
  - "alternative hasher"
  - "SipHash"
  - "byte-wise hashing"
prerequisites:
  - perf-profiling
extends: []
related:
  - perf-overview
  - perf-stdlib-types
  - perf-heap-allocations
contrasts_with: []
answers_questions:
  - "How do I make HashMap and HashSet faster in Rust?"
  - "What are FxHashMap and FxHashSet?"
  - "When should I replace the default hasher?"
  - "What is the difference between rustc-hash, fnv, and ahash?"
  - "What is byte-wise hashing and when should I use it?"
  - "How do I use nohash_hasher for random integer keys?"
---

# Quick Definition

The default Rust hash algorithm (SipHash 1-3) prioritizes collision resistance over speed. When profiling shows hashing is hot and HashDoS attacks are not a concern, switching to a faster hasher like `rustc-hash` (FxHashMap/FxHashSet), `fnv`, or `ahash` can provide large speed wins. Byte-wise hashing via `zerocopy` or `bytemuck` is an advanced technique for further optimization.

# Core Definition

"The default hashing algorithm is not specified, but at the time of writing the default is an algorithm called SipHash 1-3. This algorithm is high quality -- it provides high protection against collisions -- but is relatively slow, particularly for short keys such as integers." (Ch. 6, Alternative Hashers)

Three alternative hasher crates are presented:
- **`rustc-hash`**: Provides `FxHashSet` and `FxHashMap` as drop-in replacements. "Its hashing algorithm is low-quality but very fast, especially for integer keys, and has been found to out-perform all other hash algorithms within rustc."
- **`fnv`**: Provides `FnvHashSet` and `FnvHashMap`. "Its hashing algorithm is higher quality than `rustc-hash`'s but a little slower."
- **`ahash`**: Provides `AHashSet` and `AHashMap`. "Its hashing algorithm can take advantage of AES instruction support that is available on some processors."

(Ch. 6, Alternative Hashers)

# Prerequisites

- **perf-profiling** -- "If profiling shows that hashing is hot" is the stated trigger for considering alternative hashers

# Key Properties

1. The default SipHash 1-3 is high-quality (collision-resistant) but relatively slow, especially for short keys like integers
2. Alternative hashers are appropriate when profiling shows hashing is hot AND HashDoS attacks are not a concern
3. `rustc-hash` (FxHash) is the fastest option tested within rustc, especially for integer keys
4. `fnv` is higher quality than FxHash but slightly slower
5. `ahash` can leverage AES hardware instructions on supported processors
6. Performance varies by application -- the book reports switching from fnv to fxhash gave up to 6% speedups in rustc, while switching from fxhash to ahash caused 1-4% slowdowns
7. Switching from fxhash back to the default hasher in rustc caused 4-84% slowdowns
8. For types wrapping random or near-random integers, `nohash_hasher` can skip hashing entirely since the distribution is already adequate
9. Byte-wise hashing (via `zerocopy`, `bytemuck`, or `derive_hash_fast`) can be faster than field-by-field hashing for types with no padding bytes
10. Use Clippy's `disallowed_types` to prevent accidental use of standard HashMap/HashSet after switching to alternatives

# Construction / Recognition

## To Evaluate Alternative Hashers:
1. Profile your program to confirm hashing is a hot spot
2. Assess whether HashDoS resistance is needed for your application
3. Try multiple alternatives -- performance varies by application:
   - `rustc-hash` for fastest integer hashing
   - `fnv` for better quality with modest speed gain
   - `ahash` if AES instructions are available
4. Benchmark each alternative against your workloads
5. If switching universally, add `disallowed_types` to `clippy.toml` to prevent accidental use of standard types

## To Use Byte-wise Hashing:
1. Verify your type satisfies requirements (e.g., no padding bytes)
2. Use `#[derive(ByteHash)]` from `zerocopy` or `bytemuck`
3. Measure carefully -- effects depend on the hash function and type structure

# Context & Application

Hash performance is one of the most impactful data-structure-level optimizations in Rust. The book's evidence from the Rust compiler itself is compelling: switching from the default hasher to fxhash prevented 4-84% slowdowns, demonstrating how significant the choice of hash function can be for programs that use hash maps extensively.

The trade-off is security vs. speed. SipHash was chosen as the default specifically because it protects against HashDoS attacks -- carefully crafted inputs that cause pathological hash collisions, degrading HashMap to O(n) lookup. Applications that process untrusted input (web servers, parsers accepting external data) should carefully evaluate whether switching away from SipHash is safe.

`nohash_hasher` is a niche but clever optimization: if keys are already well-distributed (random integers, hash values, UUIDs), there is no benefit to hashing them further. The "hash function" simply returns the value unchanged.

# Examples

**Example 1** (Ch. 6, Alternative Hashers): Performance results from rustc:
- Switching from `fnv` to `fxhash`: speedups of up to 6%
- Attempting `fxhash` to `ahash`: slowdowns of 1-4%
- Attempting `fxhash` back to default: slowdowns of 4-84%

**Example 2** (Ch. 6, Alternative Hashers): "If you decide to universally use one of the alternatives, such as `FxHashSet`/`FxHashMap`, it is easy to accidentally use `HashSet`/`HashMap` in some places. You can use Clippy to avoid this problem." -- via `disallowed_types` in `clippy.toml`.

**Example 3** (Ch. 6, Byte-wise Hashing): "When you annotate a type with `#[derive(Hash)]` the generated `hash` method will hash each field separately. For some hash functions it may be faster to convert the type to raw bytes and hash the bytes as a stream." The `zerocopy`, `bytemuck`, and `derive_hash_fast` crates support this.

# Relationships

## Builds Upon
- **perf-profiling** -- profiling is explicitly required before switching hashers

## Enables
- Faster hash table lookups and insertions throughout the program

## Related
- **perf-overview** -- Clippy's `disallowed_types` lint is used to enforce alternative hasher usage
- **perf-stdlib-types** -- HashMap/HashSet are standard library types with performance considerations
- **perf-heap-allocations** -- hash tables have allocation patterns similar to Vec

## Contrasts With
- None explicitly stated

# Common Errors

- **Error**: Switching to a fast hasher without profiling first.
  **Correction**: "If profiling shows that hashing is hot" is the prerequisite. If hashing is not a hot spot, switching hashers adds complexity without benefit.

- **Error**: Assuming one alternative hasher is universally best.
  **Correction**: "If hashing performance is important in your program, it is worth trying more than one of these alternatives." Results from rustc show ahash was slower than fxhash despite being theoretically more advanced.

- **Error**: Using byte-wise hashing on types with padding bytes.
  **Correction**: "This is possible for types that satisfy certain properties such as having no padding bytes." Applying it to types with padding produces incorrect hash values.

# Common Confusions

- **Confusion**: Thinking FxHash/fnv/ahash are always safe to use.
  **Clarification**: These hashers trade collision resistance for speed. If your application processes untrusted input, the weaker collision resistance may enable HashDoS attacks where an attacker crafts inputs causing O(n) hash table behavior.

- **Confusion**: Thinking `#[derive(Hash)]` already produces optimal hash implementations.
  **Clarification**: The derived `Hash` hashes each field separately. For some hash functions and type layouts, byte-wise hashing (converting the entire struct to raw bytes) is faster, but this is an advanced technique requiring types with no padding.

# Source Reference

Chapter 6: Hashing -- all sections: Alternative Hashers (SipHash, rustc-hash, fnv, ahash, nohash_hasher, hash function design), Byte-wise Hashing (zerocopy, bytemuck, derive_hash_fast).

# Verification Notes

- Definition source: Direct quotations from Ch. 6 introduction and Alternative Hashers section
- Performance data: Directly from rustc benchmarks cited in the chapter with links to PRs/issues
- Alternative hasher descriptions: Directly from the chapter's enumeration
- Byte-wise hashing: Directly from the Byte-wise Hashing section
- Confidence rationale: HIGH -- the chapter provides explicit guidance with concrete performance data from a major Rust project
- Uncertainties: None
