# Correction handoff — layout and measure exceptions

CC-proposed evidence and dispositions; no source file is edited. Implementations require a fresh Arc04 assignment pinned to an accepted source state. Arc03 owns actual accessibility, typography and browser proof. The Operator/R owns original editions, capture identity and lineage under P10-11.

## Portable policy

Compose from intrinsic, content-responsive primitives first. Let content size prose, sections and grids where that works. Treat a prose measure such as `60ch` as a configurable starting value: CSS defines `ch` through the “0” glyph advance, so script, font, writing mode and fallback affect it. Do not apply a prose measure indiscriminately to controls, navigation, media, wide data, or structural containers.

Use discrete media or container adaptation when a component or task needs an actual mode change: grouping dense navigation/actions, preserving operation and reading order, choosing a presentation for print, or responding to a user preference. Each threshold needs a stated subject (viewport, output medium or named query container), an operational reason, the expected transition and a failure check. A relative unit can express a threshold; it cannot explain why that value is right. Keep the intrinsic mode as a usable fallback where possible.

Separate three rules that the current text merges: prose measure, interactive target size, and spacing-token preference. WCAG SC 1.4.8, 1.4.10, 2.5.5 and 2.5.8 have distinct levels, mechanisms, scopes and exceptions. None is certified by a CSS declaration or by a design-system default. A broad universal selector may be used only with a reviewed exception set and real component checks; direct semantic targeting may be safer when exceptions are unstable.

Preserve the compositional ethos. Primitives are useful tools, not proof that one finite primitive set composes every layout or that any untested composition is correct. Derivation reduces arbitrary values and repeated tuning; it does not remove the need to inspect representative outcomes.

## Worked cases and verification owners

| Case | Assumptions and expected behavior | Contrary interpretation to reject | Future check / owner |
|---|---|---|---|
| Global rule and local exception | A default measure applies to prose; wrappers, controls, media, tables and other wide content receive their own intentional sizing. | “Axiom” means every element must remain at 60ch; every selector exception is a defect. | Inspect computed measure and overflow for prose, navigation, controls, media and data-table examples; Arc04 implementation, Arc03 review. |
| Measure, characters and standards | `60ch` is 60 times the relevant CSS `ch` length. In the stipulated toy model, a zero advance of 10px gives 600px; glyph widths of 10px and 5px would fit 60 and 120 equal-width glyphs, respectively. | Every font/string yields exactly 60 characters; this CSS passes WCAG. | Record actual font, fallback, writing mode, zoom and representative scripts; separately test the named WCAG criteria and mechanisms. Arc03. The 60/120 arithmetic is not browser line wrapping. |
| Dense actions and prose | Base navigation/actions wrap intrinsically. If grouping or operability becomes unclear, a discrete container or media mode rearranges controls; a prose column still works without a query. | A justified discrete mode violates intrinsic-first design; `ch` alone justifies its threshold. | Test wide/narrow container, task sequence, keyboard/focus order, zoom, labels and print; Arc03 + Arc04. No run occurred here. |
| Outcomes and changing inputs | Rules reduce one-off tuning. Increased copy, a long unbreakable token, changed font metrics, and wide 2D content may trigger different outcomes or exceptions. | A well-chosen axiom guarantees correct unseen combinations, so manual review is unnecessary. | Browser matrix tests at normal/enlarged text, fallback/changed fonts, long content and wide table/media; record clipping, overflow, reading order and interaction. Arc03. Not run in this evidence slice. |

## Exact proposed actions

The JSON below maps every assessed occurrence to one original-source action. Offsets are zero-based Unicode character bounds within the inclusive joined line span; byte bounds locate the same original in the pinned UTF-8 file. Virtual composition replaces these non-overlapping whole-line spans only. Each `original` is reproduced from pinned Git bytes. See result IDs for separate five-dimension assessments and evidence.

```json
[
  {
    "action_id": "A-C01",
    "claim_ids": [
      "C01"
    ],
    "result_ids": [
      "C01"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      80,
      80
    ],
    "literal_offset_0based": [
      0,
      89
    ],
    "file_byte_offsets": [
      7340,
      7431
    ],
    "original": "Every layout is a composition of these. No bespoke CSS layouts — compose from primitives.",
    "disposition": "qualify",
    "replacement": "Use the listed primitives as a compositional starting vocabulary; add a justified layout rule when content or interaction requires it.",
    "rationale": "Composed action for C01; local layout-composition policy",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C27",
    "claim_ids": [
      "C27"
    ],
    "result_ids": [
      "C27"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      98,
      98
    ],
    "literal_offset_0based": [
      0,
      182
    ],
    "file_byte_offsets": [
      9052,
      9234
    ],
    "original": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow). A page header = Cover containing a Center containing a Stack. A navigation = Cluster inside a Box.",
    "disposition": "retain",
    "replacement": "Keep as an illustrative composition pattern; treat it as one useful example, not an exhaustive layout grammar.",
    "rationale": "Composed action for C27; primitive composition example",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C02",
    "claim_ids": [
      "C02"
    ],
    "result_ids": [
      "C02"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      86,
      86
    ],
    "literal_offset_0based": [
      0,
      135
    ],
    "file_byte_offsets": [
      7787,
      7922
    ],
    "original": "| **Center** | Max-width + horizontal centering | `max-inline-size: 60ch; margin-inline: auto` | Prose, any width-constrained content |",
    "disposition": "qualify",
    "replacement": "Use a configurable measure such as 60ch for prose; choose an appropriate unconstrained or wider container for non-prose layout.",
    "rationale": "Composed action for C02; measure default and scope",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C03",
    "claim_ids": [
      "C03"
    ],
    "result_ids": [
      "C03"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      89,
      89
    ],
    "literal_offset_0based": [
      0,
      146
    ],
    "file_byte_offsets": [
      8172,
      8320
    ],
    "original": "| **Switcher** | Multi-col → single-col based on space | `flex-wrap: wrap` with calculated `flex-basis` | Responsive columns without breakpoints |",
    "disposition": "retain",
    "replacement": "Retain Switcher as an intrinsic technique; assess each composition for content, operation and accessibility.",
    "rationale": "Composed action for C03; intrinsic switcher",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C04",
    "claim_ids": [
      "C04"
    ],
    "result_ids": [
      "C04"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      208,
      208
    ],
    "literal_offset_0based": [
      0,
      154
    ],
    "file_byte_offsets": [
      12941,
      13095
    ],
    "original": "No media queries for layout. Primitives + fluid tokens handle all responsiveness. The test: if you removed every media query, would the layout still work?",
    "disposition": "correct",
    "replacement": "Start with intrinsic layout. Add a content- or user-context-driven query when a tested need requires discrete adaptation.",
    "rationale": "Composed action for C04; zero-query rule and universal claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C05",
    "claim_ids": [
      "C05"
    ],
    "result_ids": [
      "C05"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      272,
      272
    ],
    "literal_offset_0based": [
      0,
      79
    ],
    "file_byte_offsets": [
      17011,
      17092
    ],
    "original": "5. **Breakpoint test**: Remove all media queries mentally — does it still work?",
    "disposition": "qualify",
    "replacement": "Ask whether intrinsic behavior suffices; where it does not, document the need and verify the chosen adaptation.",
    "rationale": "Composed action for C05; query-free review heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C06",
    "claim_ids": [
      "C06"
    ],
    "result_ids": [
      "C06"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      331,
      332
    ],
    "literal_offset_0based": [
      0,
      98
    ],
    "file_byte_offsets": [
      18516,
      18614
    ],
    "original": "* { max-inline-size: 60ch; }\nhtml, body, div, header, nav, main, footer { max-inline-size: none; }",
    "disposition": "qualify",
    "replacement": "Set a configurable prose measure and exempt or separately size controls, media, structural containers and wide content.",
    "rationale": "Composed action for C06; universal measure rule with structural exceptions",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C07",
    "claim_ids": [
      "C07"
    ],
    "result_ids": [
      "C07"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      144,
      147
    ],
    "literal_offset_0based": [
      0,
      279
    ],
    "file_byte_offsets": [
      6541,
      6824
    ],
    "original": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance. You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*. The consequences",
    "disposition": "qualify",
    "replacement": "Treat 60ch as a default for prose, implemented through a local token or component rule with explicit, reviewable exceptions.",
    "rationale": "Composed action for C07; exceptionless axiom and universal enforcement",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C08",
    "claim_ids": [
      "C08"
    ],
    "result_ids": [
      "C08"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      148,
      150
    ],
    "literal_offset_0based": [
      0,
      206
    ],
    "file_byte_offsets": [
      6825,
      7039
    ],
    "original": "that emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*. They are your CSS doing",
    "disposition": "qualify",
    "replacement": "A ch-based measure responds to the relevant font metrics, but verify representative fonts, scripts, content and containers.",
    "rationale": "Composed action for C08; font scaling and guaranteed sound outcomes",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C09-C10",
    "claim_ids": [
      "C09",
      "C10"
    ],
    "result_ids": [
      "C09",
      "C10"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      275,
      282
    ],
    "literal_offset_0based": [
      0,
      535
    ],
    "file_byte_offsets": [
      12944,
      13487
    ],
    "original": "The single most important principle. Every fixed value in your CSS is a\nplace where you have overridden the browser\\'s judgment with your own.\nSometimes this is necessary --- a maximum measure of `60ch`, a minimum\ntouch-target of `44px` --- but the default posture should always be to\n*suggest* rather than prescribe. Use `min-`, `max-`, and `clamp()`\ninstead of fixed values. Use `auto` instead of `100%`. Use `flex-basis`\ninstead of `width`. Each of these is an invitation for the browser to\nmake a contextually appropriate decision.",
    "disposition": "qualify",
    "replacement": "Prefer content-aware constraints and flexible sizing when suitable; choose and justify each measure or CSS sizing function for the actual content, component and user context, then verify the result.",
    "rationale": "Composed action for C09, C10; fixed values, measure and target examples CSS technique preference",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C11",
    "claim_ids": [
      "C11"
    ],
    "result_ids": [
      "C11"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      284,
      289
    ],
    "literal_offset_0based": [
      0,
      400
    ],
    "file_byte_offsets": [
      13489,
      13893
    ],
    "original": "This is not laziness. It is recognition that the browser knows things\nyou do not --- the user\\'s font size preferences, their zoom level,\ntheir screen dimensions, whether they are using a split-screen view,\nwhether they have a notch or a toolbar. Your CSS should provide\n*constraints within which good outcomes are inevitable*, not blueprints\nthat are correct in one context and broken in all others.",
    "disposition": "qualify",
    "replacement": "Use browser and user context as design inputs, then verify supported environments and representative content; no CSS constraint guarantees every outcome.",
    "rationale": "Composed action for C11; browser context and inevitable outcome",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C12",
    "claim_ids": [
      "C12"
    ],
    "result_ids": [
      "C12"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      291,
      293
    ],
    "literal_offset_0based": [
      0,
      159
    ],
    "file_byte_offsets": [
      13895,
      14054
    ],
    "original": "**The test:** if you removed every media query from your stylesheet,\nwould the layout still be usable? If not, your constraints are not yet\nwell enough chosen.",
    "disposition": "qualify",
    "replacement": "Use query removal as a diagnostic prompt, not a pass condition; explain any discrete adaptation that remains necessary.",
    "rationale": "Composed action for C12; query-free usability test",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C13",
    "claim_ids": [
      "C13"
    ],
    "result_ids": [
      "C13"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      328,
      334
    ],
    "literal_offset_0based": [
      0,
      449
    ],
    "file_byte_offsets": [
      15432,
      15881
    ],
    "original": "The web is a content-driven medium. The width of a paragraph should be\ndetermined by its measure (in `ch` units). The height of a section\nshould be determined by the amount of content it contains. The gap\nbetween elements should be determined by the typographic scale (in `rem`\nor Utopia space tokens). The number of columns in a grid should be\ndetermined by the minimum acceptable item width and the available space\n(via `auto-fit` and `minmax()`).",
    "disposition": "qualify",
    "replacement": "Derive dimensions from content and context; use ch as an approximate glyph-relative prose measure and verify with the actual scripts and fonts.",
    "rationale": "Composed action for C13; content-derived dimension principles",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C14",
    "claim_ids": [
      "C14"
    ],
    "result_ids": [
      "C14"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      336,
      341
    ],
    "literal_offset_0based": [
      0,
      401
    ],
    "file_byte_offsets": [
      15883,
      16284
    ],
    "original": "When you prescribe a height, you are declaring that you know how much\ncontent will be present. You almost certainly do not. When you prescribe\na width in pixels, you are declaring that you know the user\\'s viewport\nsize. You do not. When you prescribe a column count, you are declaring\nthat you know the container\\'s width. In a world of container queries\nand intrinsic design, you should not need to.",
    "disposition": "qualify",
    "replacement": "Avoid brittle fixed geometry, but use explicit sizes and column counts when justified; queries and intrinsic rules solve different needs.",
    "rationale": "Composed action for C14; fixed geometry assumptions and container-query claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C15",
    "claim_ids": [
      "C15"
    ],
    "result_ids": [
      "C15"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      343,
      345
    ],
    "literal_offset_0based": [
      0,
      146
    ],
    "file_byte_offsets": [
      16286,
      16432
    ],
    "original": "Content determines dimensions. Context determines arrangement. The\ndesigner\\'s job is to set the *rules of derivation*, not the values\nthemselves.",
    "disposition": "qualify",
    "replacement": "Prefer rules that respond to content and context, while allowing explicit values where the design requirement warrants them.",
    "rationale": "Composed action for C15; design rule of derivation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C16",
    "claim_ids": [
      "C16"
    ],
    "result_ids": [
      "C16"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      347,
      349
    ],
    "literal_offset_0based": [
      0,
      179
    ],
    "file_byte_offsets": [
      16434,
      16613
    ],
    "original": "**The test:** if the content doubles in length, does the layout still\nwork? If the viewport halves in width, does it still work? If both\nhappen simultaneously, does it still work?",
    "disposition": "retain",
    "replacement": "Retain as a test prompt and add changed-font metrics, unbreakable tokens, expanded labels and wide-content cases.",
    "rationale": "Composed action for C16; content and viewport stress heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C17",
    "claim_ids": [
      "C17"
    ],
    "result_ids": [
      "C17"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      387,
      391
    ],
    "literal_offset_0based": [
      0,
      340
    ],
    "file_byte_offsets": [
      18186,
      18526
    ],
    "original": "An axiom is a design rule that pervades the entire system without\nexception. \\\"The measure shall not exceed 60ch.\\\" \\\"The minimum touch\ntarget shall be 44px.\\\" \\\"Spacing between sibling elements shall use\nUtopia space tokens.\\\" These are not guidelines to remember; they are\n*CSS declarations* that are written once and enforced everywhere.",
    "disposition": "correct",
    "replacement": "Define prose measure, touch-target checks and spacing preferences as distinct scoped rules; state each exception and verification route.",
    "rationale": "Composed action for C17; universal size/spacing axioms",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C18",
    "claim_ids": [
      "C18"
    ],
    "result_ids": [
      "C18"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      393,
      400
    ],
    "literal_offset_0based": [
      0,
      490
    ],
    "file_byte_offsets": [
      18528,
      19018
    ],
    "original": "The crucial insight from Every Layout\\'s Axioms chapter is that\ndesigning by axiom means designing *without seeing*. You cannot predict\nevery visual consequence of a well-chosen axiom, and *you do not need\nto*. The axiom generates correct outcomes in contexts you never\nanticipated, because it encodes a *principle* rather than a *specific\narrangement*. This is what makes axiom-based design scale: it does not\nrequire a designer to manually verify every combination of content and\ncontext.",
    "disposition": "correct",
    "replacement": "Use rules to reduce repeated hand-tuning, while inspecting representative combinations and failures; attribute the cited source only after edition and passage are established.",
    "rationale": "Composed action for C18; attribution, correctness and verification guarantee",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C19",
    "claim_ids": [
      "C19"
    ],
    "result_ids": [
      "C19"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      402,
      406
    ],
    "literal_offset_0based": [
      0,
      335
    ],
    "file_byte_offsets": [
      19020,
      19355
    ],
    "original": "Axioms are best implemented using exception-based CSS: apply the rule to\neverything (`*`), then remove it from the specific elements that are\nlogical exceptions (containers, wrappers, structural elements). This\ninverted approach means you only need to *remember the exceptions*, not\nenumerate every element that should follow the rule.",
    "disposition": "qualify",
    "replacement": "Use a broad selector only when its inheritance and exception set are controlled and tested; otherwise target semantic components directly.",
    "rationale": "Composed action for C19; exception-based CSS approach",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C20",
    "claim_ids": [
      "C20"
    ],
    "result_ids": [
      "C20"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      408,
      410
    ],
    "literal_offset_0based": [
      0,
      212
    ],
    "file_byte_offsets": [
      19357,
      19569
    ],
    "original": "**The test:** can you state each design rule in a single sentence? Can\nthat sentence be translated into a single CSS declaration? If so, it is\nan axiom. If not, it may be a convention masquerading as a principle.",
    "disposition": "qualify",
    "replacement": "Use this as a clarity prompt; single-declaration form does not establish universality or correctness.",
    "rationale": "Composed action for C20; axiom classification heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C21",
    "claim_ids": [
      "C21"
    ],
    "result_ids": [
      "C21"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      599,
      607
    ],
    "literal_offset_0based": [
      0,
      384
    ],
    "file_byte_offsets": [
      26894,
      27278
    ],
    "original": "**Responsibility:** constraining content to a maximum width and centring\nit horizontally. The measure axiom is typically enforced here.\n\n**Mechanism:** `max-inline-size` with `margin-inline: auto`. Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.\n\n**Key parameter:** `--measure` (maximum width, typically `60ch` for\nprose, wider for layout containers).",
    "disposition": "retain",
    "replacement": "Keep a configurable measure: commonly around 60ch for prose, with values chosen for scripts, fonts, and wider layout containers.",
    "rationale": "Composed action for C21; scoped configurable measure",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C22",
    "claim_ids": [
      "C22"
    ],
    "result_ids": [
      "C22"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      670,
      678
    ],
    "literal_offset_0based": [
      0,
      373
    ],
    "file_byte_offsets": [
      28980,
      29353
    ],
    "original": "**Responsibility:** switching between a multi-column and a single-column\nlayout based on available space. No breakpoints.\n\n**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that\ncauses items to wrap at the threshold width. The threshold is defined by\nthe content, not the viewport.\n\n**Key parameter:** `--threshold` (the container width at which items\nstack).",
    "disposition": "qualify",
    "replacement": "Retain content-driven wrapping as the first option; make a discrete query or mode available when interaction needs a state change that wrapping cannot provide.",
    "rationale": "Composed action for C22; intrinsic Switcher threshold",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C23",
    "claim_ids": [
      "C23"
    ],
    "result_ids": [
      "C23"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      698,
      700
    ],
    "literal_offset_0based": [
      0,
      205
    ],
    "file_byte_offsets": [
      30128,
      30341
    ],
    "original": "Together, these thirteen primitives can compose any layout. They are the\n*atoms* of the system. Everything else --- cards, headers, navigation,\nforms, footers --- is a *molecule* composed from these atoms.",
    "disposition": "qualify",
    "replacement": "Treat the primitives as reusable composition tools, not an exhaustive guarantee that every layout or interaction is expressible without additional patterns.",
    "rationale": "Composed action for C23; complete-vocabulary guarantee and composition model",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C24",
    "claim_ids": [
      "C24"
    ],
    "result_ids": [
      "C24"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      973,
      975
    ],
    "literal_offset_0based": [
      0,
      193
    ],
    "file_byte_offsets": [
      46389,
      46582
    ],
    "original": "of layout needs. Set `max-inline-size: 60ch` on all text elements. Use\n`gap` with Utopia space tokens for all spacing. Write zero media\nqueries. You will be astonished at how far this gets you.",
    "disposition": "correct",
    "replacement": "Use a prose measure where appropriate; treat spacing tokens as local guidance and add justified context adaptation when required.",
    "rationale": "Composed action for C24; broad implementation prescription",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C25",
    "claim_ids": [
      "C25"
    ],
    "result_ids": [
      "C25"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "span": [
      107,
      108
    ],
    "literal_offset_0based": [
      0,
      135
    ],
    "file_byte_offsets": [
      4064,
      4199
    ],
    "original": "Shift responsive design from viewport to component. Using `ch` units in\ncontainer queries eliminates magic-number breakpoints entirely.",
    "disposition": "correct",
    "replacement": "Container queries can express content-context thresholds; justify each value from tested content and behavior, since ch only supplies a relative unit.",
    "rationale": "Composed action for C25; ch units eliminate magic-number thresholds",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  },
  {
    "action_id": "A-C26",
    "claim_ids": [
      "C26"
    ],
    "result_ids": [
      "C26"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "span": [
      109,
      111
    ],
    "literal_offset_0based": [
      0,
      174
    ],
    "file_byte_offsets": [
      4200,
      4374
    ],
    "original": "Components adapt based on the space they actually occupy, not the\nbrowser window size. Combined with container query units (`cqw`, `cqh`),\nsizing becomes relative to context.",
    "disposition": "qualify",
    "replacement": "Prefer container context for component-local adaptation when a suitable query container exists; verify axis, size containment and fallback behavior.",
    "rationale": "Composed action for C26; container-context adaptation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here."
  }
]
```

No source action is executed by this handoff. Original-source fidelity remains unassessed until P10-11 re-entry; actual behavior and accessibility remain untested until the named later owners run the appropriate checks.
