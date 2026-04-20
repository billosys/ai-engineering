# Phase 0 - Section 9 - Extraction-Specific Instructions

## 9. Extraction-Specific Instructions

### 9.1 Concept Card Template Additions

In addition to the standard v3 template fields, visual design concept cards should include:

```yaml
# === VISUAL DESIGN EXTENSIONS ===
layer: [0-perception/1-principles/2-domain/3-implementation]

rosetta_stone:
  - domain: [engineering/music/mathematics/art]
    concept: [concept name in source domain]
    rating: [rigorous/structural/loose]
    note: [brief description of the mapping]

css_implementation:
  - property: [CSS property or technique]
    example: "property: value;"
    support: [baseline/partial/experimental]
```

These extensions are OPTIONAL — not every card will have cross-domain mappings or CSS implementations. But when they exist, capturing them in structured frontmatter enables graph queries like "show me all concepts with rigorous music theory mappings" or "show me all concepts with CSS implementation."

The Cross-Domain Connections subsection appears in Context & Application ONLY when the concept has `rosetta_stone` entries in the frontmatter. Structure each mapping as:

```
**[Source Domain] → [RIGOROUS/STRUCTURAL/LOOSE]**: [1-2 sentence description of the mapping.]
[1-2 sentences explaining WHY the mapping holds (RIGOROUS), what structural parallel exists
(STRUCTURAL), or where the analogy breaks down (LOOSE).]
```

For RIGOROUS mappings: state the shared mathematical structure or identical implementation.
For STRUCTURAL mappings: state the parallel and its limits.
For LOOSE mappings: state what's suggestive and what doesn't hold.

If no `rosetta_stone` entries exist, omit this subsection entirely.

### 9.2 Agent Instructions: Domain-Specific Guidance

When compiling agent instructions for parallel extraction, include:

1. **Always note the mathematical formulation** when one exists. Don't simplify it. This user wants the equations.

2. **Always note the CSS implementation** when the concept has one. Include the property, syntax, and browser support status. This user will implement what they learn.

3. **Always check for Rosetta Stone mappings** against the tables in Section 7.3. If a concept maps to engineering, music, or mathematics, note it.

4. **Distinguish "errors" from "confusions" with extra care.** For this user, procedural errors (Common Errors) will often manifest as CSS that doesn't do what they expect. Conceptual confusions (Common Confusions) will often involve applying an engineering mental model where a design mental model is needed (e.g., treating visual alignment as pixel-perfect mathematical alignment when optical alignment is required).

5. **When a concept has a perceptual science foundation**, cite it. Don't just say "use consistent spacing" — say "consistent spacing works because of gestalt proximity grouping (Kubovy & Wagemans: exponential decay function of relative inter-element distance)."

6. **For diagnostic competency questions**, always include both the symptom (what looks wrong) and the principle (why it's wrong). The target user can see the symptom — they need the principle to fix it and prevent it.

7. **Subagent file permissions.** Due to current permission constraints, subagents cannot write files directly. Use the return-and-write pattern: agents draft complete card content in their context windows and return it as text to the coordinator, who writes the files from the main conversation. For serial extraction (under 25 cards), write directly from the main conversation.

8. **Two-pass extraction order.** Within each agent's scope (or for serial extraction), extract in two passes. Pass 1: all foundational-tier concepts (no prerequisites within the source). Verify these are complete. Pass 2: intermediate and advanced concepts, verifying that all prerequisite slugs from Pass 1 exist.

9. **Small-source scaling.** The 5-agent parallel architecture is designed for 100+ card extractions. Scale down for smaller sources: under 25 cards → serial; 25-50 → 2-3 agents; 50-100 → 3-4 agents; 100+ → 5 agents.

10. **Typed relationship semantics.** Apply these definitions when populating the four relationship fields:
    - **`prerequisites`**: B requires understanding A to make sense. This is a dependency: "you need A first." If a reader hasn't encountered A, the Core Definition of B will be unclear. Example: `line-height` has prerequisite `type-anatomy` (you need to know what ascenders and descenders are).
    - **`extends`**: B is a specialisation or refinement of A. B inherits A's properties and adds constraints or specificity. This is an IS-A relationship: "B is a kind of A." Example: `small-caps` extends `typographic-emphasis` (small caps are a specific form of emphasis). `all-caps` extends `typographic-emphasis`. `triadic-harmony` extends `colour-harmony`.
    - **`related`**: A and B inform each other without dependency or specialisation. Neither requires the other, but understanding one enriches understanding of the other. Example: `whitespace` is related to `visual-hierarchy` (they interact, but neither is a prerequisite or specialisation of the other).
    - **`contrasts_with`**: A and B are easily confused, represent opposing approaches, or are frequently compared. Example: `optical-alignment` contrasts with `mathematical-alignment`. `serif` contrasts with `sans-serif`.

    The test: if removing A would make B's definition nonsensical → `prerequisites`. If B is "a kind of A" → `extends`. If they're lateral peers → `related`. If they're commonly mixed up or opposed → `contrasts_with`.

11. **Prescription-heavy sources.** When the source defines concepts through rules and best practices rather than formal definitions (common in practitioner-oriented sources like Refactoring UI, Practical Typography, Don't Make Me Think), synthesise the Core Definition by combining: (a) what the rule prescribes, (b) why the source says it matters, and (c) what design principle it serves. Set `extraction_confidence: medium` and note "Synthesised from prescriptive guidance on [topic], pp. X-Y" in Verification Notes. Do not invent theoretical justifications the source doesn't provide — if the source says "do X because it looks better" without citing a principle, record that honestly.

12. **Tier assignment is absolute, not source-relative.** Tiers reflect the concept's position in the knowledge base as a whole, not its difficulty relative to the source's audience. A general-audience source may produce mostly foundational and intermediate cards — this is expected and correct. Do not inflate tiers to achieve a balanced distribution within a single source. The validation criteria (Section 10.1) check tier coverage *across the full knowledge base*, not per-source.
