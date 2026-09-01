# Phase 0 - Section 10 - Validation Criteria

## 10. Validation Criteria

### 10.1 Taxonomy Coverage

After each extraction wave, verify:

- [ ] Every taxonomy category has at least 5 concept cards
- [ ] Every tier (foundational/intermediate/advanced) has cards in every category
- [ ] Cross-cutting concepts in `design-principles` link to domain-specific manifestations
- [ ] `accessibility` concepts exist both as standalone cards AND as facets within other categories

### 10.2 Competency Question Coverage

- [ ] Every CQ in Section 4 has at least one concept card listing it in `answers_questions`
- [ ] High-priority CQs (Section 4.4) have MULTIPLE cards contributing to the answer
- [ ] No CQ requires concepts that haven't been extracted yet (or flag as "Wave N dependency")

Note: CQ coverage is validated **across sources**, not within a single source. No single source is expected to cover all 56 CQs. After each extraction, generate a CQ coverage report showing which CQs are now answered. Maintain a cumulative tracker at `concept-cards/cq-coverage-tracker.md` that maps each CQ to the cards (across all sources) that answer it.

### 10.2.1 CQ Phrasing Consistency

After each extraction, verify that all `answers_questions` entries use canonical CQ phrasing:

```bash
# Extract all CQ strings from this source's cards
grep -h "answers_questions:" -A 20 concept-cards/$SOURCE_SLUG/*.md \
  | grep "^  - " | sed 's/^  - //' | sort | uniq -c | sort -rn

# Compare against canonical CQ list
# Each unique string should match a CQ in 0007 exactly
# Flag any string that doesn't match — likely a paraphrase that needs correction
```

CQ strings must be copied exactly from Section 4, not paraphrased. Paraphrased CQs break aggregation in the CQ coverage tracker.

### 10.3 Rosetta Stone Coverage

- [ ] Every RIGOROUS mapping in Section 7.3 is reflected in at least one concept card's `rosetta_stone` field
- [ ] No mapping is claimed as RIGOROUS without mathematical justification
- [ ] STRUCTURAL mappings include explicit "where it breaks down" notes

### 10.4 Layer Integrity

- [ ] Layer 0 concepts have no prerequisites from higher layers
- [ ] Layer 1 concepts depend only on Layer 0
- [ ] Layer 2 concepts may depend on Layers 0 and 1
- [ ] Layer 3 concepts may depend on any layer
- [ ] No circular dependencies exist within a layer

### 10.5 Cross-Source Slug Tracking

After each extraction, update `concept-cards/slug-registry.txt` — a flat file listing every slug, its source, and whether it's generic or source-prefixed:

```
hue                     munsell-source    generic
value                   munsell-source    generic
chroma                  munsell-source    generic
munsell-hue-circle      munsell-source    source-prefixed
munsell-notation        munsell-source    source-prefixed
```

This registry enables the harmonisation phase to quickly identify which concepts appear across multiple sources and need reconciliation.
