# Portable layout and measure correction handoff — Iteration01

CC proposal only. These compositions are exact future edits against SOURCE `dffa504e851b03b8e4746f1941068e4cc850b612`; no SOURCE file was changed. Every action names the complete pinned original target, its source hash, half-open line-relative character and file-byte spans, result IDs, a composed replacement and later owner. Atomic results point to one authoritative composed action; grouped actions carry `unit_subjects` so each original clause remains traceable without duplicating contradictory replacement prose. All listed implementation and testing owners are future owners, not assignments or acceptance.

## Portable policy

Start with content-led, intrinsic composition: fluid constraints, wrapping, and content-derived sizing where their actual inputs produce a usable result. Treat a configurable prose measure (a project default may begin near 60ch) as a scoped choice; font-relative units do not mean a fixed pixel width or a guaranteed number of arbitrary characters. Size controls for their purpose and usable target; preserve access to wide data/media when two-dimensional structure carries meaning. Permit a container or media query when a concrete content, interaction, user, or output condition requires a discrete mode. State the condition, trigger, mode, order, and expected behavior; query-free layout remains a useful starting point, not a universal requirement. Verify content expansion, fonts, long tokens, reading/DOM/focus order, keyboard and touch access, and exceptional wide content.

The policy preserves the system's compositional ethos while separating technical CSS claims, standards obligations, local design defaults, and analogies. No claim here certifies the live skill or any browser output.

## Worked policy cases

### Dense action task: justified discrete mode

Hypothetical task: a compact data-review panel has four labeled actions—Select rows, Set disposition, Preview changes, Apply disposition. For the stipulated labels each control needs 96 CSS px plus three 8 px gaps: `4 × 96 + 3 × 8 = 408px`. At a 360px container, intrinsic flex wrapping can fit the controls, but it splits the single review-action cluster. The product task requires reviewers to scan and operate this one cluster against the selected rows without the primary action visually separating from its setup actions. Layout fit alone does not establish this task failure; the task constraint is an explicit hypothetical assumption.

Under that assumption, retain intrinsic sizing as the base and use a container query at a content/task-validated threshold to switch the action cluster to one full-width vertical labeled group below the required width. Do not hide labels, reorder controls, remove actions, or change DOM/focus order. Expected: all four labels remain visible, keyboard order follows the reading order, focus is visible, every action remains reachable, and the selected-row context remains available. Contrary outcome: wrapping causes the Apply action to appear detached/ambiguous, a label is clipped, or focus/order changes. Arc03 owns keyboard, focus and reading-order validation; Arc04 owns the later component implementation and cross-context behavior check. The 408px arithmetic is a stipulated design witness, not a measured browser threshold and not evidence that every dense page needs a query.

### Prose without a query

A long-form article with a semantic text column, ordinary paragraph flow, and no side-by-side task controls can use a configurable max measure, automatic block sizing, and normal wrapping at both 360px and 480px. Expected: paragraphs reflow, no horizontal overflow occurs, and the text remains in reading order without a mode switch. Contrary outcome: a long token, fixed descendant, or chosen measure causes clipping/overflow; correct that constraint or content behavior first. A query is not justified solely because one exists elsewhere.

### Adverse content and context

| Case | Assumption and expected behavior | Contrary observation / future owner |
|---|---|---|
| Expanded labels/content | A translated action label doubles in length. The control grows or wraps without clipping; actions remain distinguishable and reachable. | Clipping, overlap or loss of grouping triggers component revision; Arc03 accessibility review, Arc04 implementation. |
| Unbreakable token | A long identifier has no soft wrap opportunity. A prose column may overflow at that token unless the content or an intentional overflow/wrapping policy addresses it. | Horizontal page overflow or obscured content is a failure; retain code/token copyability and choose a scoped wrapping/scroll policy. Arc03 review, Arc04 behavior. |
| Changed font metrics | A user font/zoom change alters the “0” advance and control labels. A ch-based measure changes with the used font; content can reflow and the task remains available. | A fixed-height box, narrow control or assumed character count breaks; test representative fonts/zoom and remove brittle constraints. Arc03 and Arc04. |
| Wide 2D data/media | A table whose rows/columns require comparison may need a bounded horizontal scroll region or another equivalent two-dimensional presentation; surrounding prose still reflows. | Global 60ch clipping, lost column relationships, inaccessible scroll/focus or forced linearization that destroys meaning is failure. WCAG SC1.4.10 exceptions are context-bound, not a blanket exemption. Arc03 owns accessibility/keyboard checks; Arc04 owns responsive component behavior. |

For every case retain the contrary result as a defect witness and test reading order, DOM order, focus, keyboard access, labels and content integrity. Actual browser and assistive-technology behavior remains unrun.

## Exact proposed actions

The JSON below is the authoritative action registry. `retain` is used only where the replacement is byte-identical to the original; changed advice is labelled `qualify` or `correct`. Table replacements remain four-cell rows, checklist edits retain their number, and CSS edits are CSS within the original CSS fence. Before any future implementation, virtually compose the actions against each complete pinned file and inspect grammar, table rows, checklist numbering, CSS fences, neighboring attribution and untouched examples. This pass performed that composition review for the entries below; the checker verifies byte joins and structural formats, while human review remains responsible for meaning and grammar.

```json
[
  {
    "action_id": "A-C01",
    "claim_ids": [
      "C01.01",
      "C01.02"
    ],
    "result_ids": [
      "C01.01",
      "C01.02"
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
    "replacement": "Use the listed primitives as a reusable composition method. Permit justified additional CSS rules when content, semantics or interaction requires them.",
    "rationale": "Composed action for C01; local layout-composition policy",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C01.01": "Use the listed primitives as a reusable composition method.",
      "C01.02": "Permit justified additional CSS rules when content, semantics or interaction requires them."
    },
    "unit_subjects": {
      "C01.01": "Every layout is a composition of these.",
      "C01.02": "No bespoke CSS layouts — compose from primitives."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C01.01": {
        "start": 0,
        "end": 59
      },
      "C01.02": {
        "start": 60,
        "end": 151
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5f313ae4620fcaa9df9eb4dc34bde5abe006a664f1e73e4a0b2db68eba9f70cc"
  },
  {
    "action_id": "A-C27",
    "claim_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
    ],
    "result_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
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
    "disposition": "qualify",
    "replacement": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow). A page header = Cover containing a Center containing a Stack. A navigation = Cluster inside a Box. These examples illustrate reuse; they do not define a complete layout grammar.",
    "rationale": "Composed action for C27; primitive composition example",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "unit_subjects": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C27.01": {
        "start": 0,
        "end": 83
      },
      "C27.02": {
        "start": 84,
        "end": 145
      },
      "C27.03": {
        "start": 146,
        "end": 182
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a123d41cbac2dd8e30b65473c5adf1a06039512ebaeeea15d61b4cee9ba7f250"
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
    "replacement": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |",
    "rationale": "Composed action for C02; measure default and scope",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C02": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |"
    },
    "unit_subjects": {
      "C02": "| **Center** | Max-width + horizontal centering | `max-inline-size: 60ch; margin-inline: auto` | Prose, any width-constrained content |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C02": {
        "start": 0,
        "end": 218
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "433051521d4e0c1886e3439557a5166fc4f3ad481ab2d3ffd6ea37f933039482"
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
    "disposition": "qualify",
    "replacement": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |",
    "rationale": "Composed action for C03; intrinsic switcher",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C03": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |"
    },
    "unit_subjects": {
      "C03": "| **Switcher** | Multi-col → single-col based on space | `flex-wrap: wrap` with calculated `flex-basis` | Responsive columns without breakpoints |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C03": {
        "start": 0,
        "end": 255
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c76a45616f2d3bd9b7fb1b9d2b9b42abbaecae0999e37421bb01bcb7d95716a8"
  },
  {
    "action_id": "A-C04",
    "claim_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
    ],
    "result_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/SKILL.md",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "span": [
      206,
      208
    ],
    "literal_offset_0based": [
      0,
      176
    ],
    "file_byte_offsets": [
      12919,
      13095
    ],
    "original": "### Zero Breakpoints\n\nNo media queries for layout. Primitives + fluid tokens handle all responsiveness. The test: if you removed every media query, would the layout still work?",
    "disposition": "correct",
    "replacement": "### Zero Breakpoints\n\nStart with intrinsic layout and fluid constraints. Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation. Treat query removal as a diagnostic, not a universal pass condition.",
    "rationale": "Composed action for C04; zero-query rule and universal claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C04.01": "Start with intrinsic layout and fluid constraints.",
      "C04.02": "Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation.",
      "C04.03": "Treat query removal as a diagnostic, not a universal pass condition."
    },
    "unit_subjects": {
      "C04.01": "No media queries for layout.",
      "C04.02": "Primitives + fluid tokens handle all responsiveness.",
      "C04.03": "The test: if you removed every media query, would the layout still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C04.01": {
        "start": 22,
        "end": 72
      },
      "C04.02": {
        "start": 73,
        "end": 197
      },
      "C04.03": {
        "start": 198,
        "end": 266
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "d447d26fb88b761c545970f4456268d751822b62b4a09638e49ff9237380c663"
  },
  {
    "action_id": "A-C05",
    "claim_ids": [
      "C05.02"
    ],
    "result_ids": [
      "C05.02"
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
    "replacement": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice.",
    "rationale": "Composed action for C05; query-free review heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C05.02": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice."
    },
    "unit_subjects": {
      "C05.02": "**Breakpoint test**: Remove all media queries mentally — does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C05.02": {
        "start": 0,
        "end": 149
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a92dabe84e417ebb94b4388dd8be3006a23e7c60f75b4d62f634a57417ae6995"
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
    "replacement": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n",
    "rationale": "Composed action for C06; universal measure rule with structural exceptions",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C06": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n"
    },
    "unit_subjects": {
      "C06": "* { max-inline-size: 60ch; }\nhtml, body, div, header, nav, main, footer { max-inline-size: none; }"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C06": {
        "start": 0,
        "end": 211
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6f515dc61b0e33865c57e8db11e7b92a07052c09028071b42719e50e2c04e699"
  },
  {
    "action_id": "A-C07-C08",
    "claim_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "result_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      144,
      151
    ],
    "literal_offset_0based": [
      0,
      513
    ],
    "file_byte_offsets": [
      6541,
      7066
    ],
    "original": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance. You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*. The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*. They are your CSS doing\nexactly what you intended.",
    "disposition": "qualify",
    "replacement": "Treat an axiom as a project-wide default within a stated domain, with explicit exceptions. Apply a broad selector only to an explicit subject set; check inheritance and exclusions. CSS Values defines `1ch` from the used font’s “0” glyph advance, subject to fallback rules; its width varies with font metrics, but layout outcomes still need review. A rendered result may reflect the declared CSS without proving the designer’s intent or that the outcome is suitable.",
    "rationale": "Composed action for C07; exceptionless axiom and universal enforcement",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C07.01": "Treat an axiom as a project-wide default within a stated domain, with explicit exceptions.",
      "C07.02": "Apply a broad selector only to an explicit subject set; check inheritance and exclusions.",
      "C08.01": "CSS Values defines `1ch` from the used font’s “0” glyph advance, subject to fallback rules; its width varies with font metrics, but layout outcomes still need review.",
      "C08.02": "A rendered result may reflect the declared CSS without proving the designer’s intent or that the outcome is suitable."
    },
    "unit_subjects": {
      "C07.01": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance.",
      "C07.02": "You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*.",
      "C08.01": "The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*.",
      "C08.02": "They are your CSS doing\nexactly what you intended."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C07.01": {
        "start": 0,
        "end": 90
      },
      "C07.02": {
        "start": 91,
        "end": 180
      },
      "C08.01": {
        "start": 181,
        "end": 347
      },
      "C08.02": {
        "start": 348,
        "end": 465
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c8486868c2cada75cb35c73865ca50dbf679f961a8b0934012a7f72b7338bece"
  },
  {
    "action_id": "A-C09-C10",
    "claim_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
    ],
    "result_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
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
    "replacement": "Use constraints as a default method, while naming cases where a fixed value serves a requirement. A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target. Use `min-` and `max-` sizing properties to bound content; use `clamp()` when chosen minimum, preferred and maximum calculations express the intended range. Use `auto` or `100%` according to the property and formatting context; neither is universally preferable. For a flex item, choose `flex-basis` when its initial main-size input is intended; it is not a general substitute for `width`. These mechanisms contribute inputs to layout algorithms; they do not guarantee contextually appropriate outcomes without review.",
    "rationale": "Composed action for C09, C10; fixed values, measure and target examples CSS technique preference",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C09.01": "Use constraints as a default method, while naming cases where a fixed value serves a requirement.",
      "C09.02": "A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task.",
      "C09.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target.",
      "C10.01": "Use `min-` and `max-` sizing properties to bound content; use `clamp()` when chosen minimum, preferred and maximum calculations express the intended range.",
      "C10.02": "Use `auto` or `100%` according to the property and formatting context; neither is universally preferable.",
      "C10.03": "For a flex item, choose `flex-basis` when its initial main-size input is intended; it is not a general substitute for `width`.",
      "C10.04": "These mechanisms contribute inputs to layout algorithms; they do not guarantee contextually appropriate outcomes without review."
    },
    "unit_subjects": {
      "C09.01": "The single most important principle.",
      "C09.02": "Every fixed value in your CSS is a\nplace where you have overridden the browser\\'s judgment with your own.",
      "C09.03": "Sometimes this is necessary --- a maximum measure of `60ch`, a minimum\ntouch-target of `44px` --- but the default posture should always be to\n*suggest* rather than prescribe.",
      "C10.01": "Use `min-`, `max-`, and `clamp()`\ninstead of fixed values.",
      "C10.02": "Use `auto` instead of `100%`.",
      "C10.03": "Use `flex-basis`\ninstead of `width`.",
      "C10.04": "Each of these is an invitation for the browser to\nmake a contextually appropriate decision."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C09.01": {
        "start": 0,
        "end": 97
      },
      "C09.02": {
        "start": 98,
        "end": 221
      },
      "C09.03": {
        "start": 222,
        "end": 531
      },
      "C10.01": {
        "start": 532,
        "end": 687
      },
      "C10.02": {
        "start": 688,
        "end": 793
      },
      "C10.03": {
        "start": 794,
        "end": 920
      },
      "C10.04": {
        "start": 921,
        "end": 1049
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "ccb9c3a538c2b1fe40968e20678118a1f60c5d8a0c10ea564cb27b086b2fe284"
  },
  {
    "action_id": "A-C11",
    "claim_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
    ],
    "result_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
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
    "replacement": "This is a design preference for using browser and user context, not a claim of laziness. Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result. Constraints can support robust outcomes but cannot make good results inevitable across all contexts.",
    "rationale": "Composed action for C11; browser context and inevitable outcome",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C11.01": "This is a design preference for using browser and user context, not a claim of laziness.",
      "C11.02": "Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result.",
      "C11.03": "Constraints can support robust outcomes but cannot make good results inevitable across all contexts."
    },
    "unit_subjects": {
      "C11.01": "This is not laziness.",
      "C11.02": "It is recognition that the browser knows things\nyou do not --- the user\\'s font size preferences, their zoom level,\ntheir screen dimensions, whether they are using a split-screen view,\nwhether they have a notch or a toolbar.",
      "C11.03": "Your CSS should provide\n*constraints within which good outcomes are inevitable*, not blueprints\nthat are correct in one context and broken in all others."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C11.01": {
        "start": 0,
        "end": 88
      },
      "C11.02": {
        "start": 89,
        "end": 201
      },
      "C11.03": {
        "start": 202,
        "end": 302
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "80fcfa794d0a4bdc31cc231033005712b123547d7733807dc87bee77e628c67f"
  },
  {
    "action_id": "A-C12",
    "claim_ids": [
      "C12.01",
      "C12.02"
    ],
    "result_ids": [
      "C12.01",
      "C12.02"
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
    "replacement": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case. If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision.",
    "rationale": "Composed action for C12; query-free usability test",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C12.01": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case.",
      "C12.02": "If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision."
    },
    "unit_subjects": {
      "C12.01": "**The test:** if you removed every media query from your stylesheet,\nwould the layout still be usable?",
      "C12.02": "If not, your constraints are not yet\nwell enough chosen."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C12.01": {
        "start": 0,
        "end": 99
      },
      "C12.02": {
        "start": 100,
        "end": 209
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f7014ddad136381d870b9460fdd55d75a263b795fa3091311811ba49657b10fa"
  },
  {
    "action_id": "A-C13",
    "claim_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
    ],
    "result_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
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
    "replacement": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee. Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts. Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow. Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing. Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions.",
    "rationale": "Composed action for C13; content-derived dimension principles",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C13.01": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee.",
      "C13.02": "Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts.",
      "C13.03": "Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow.",
      "C13.04": "Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing.",
      "C13.05": "Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions."
    },
    "unit_subjects": {
      "C13.01": "The web is a content-driven medium.",
      "C13.02": "The width of a paragraph should be\ndetermined by its measure (in `ch` units).",
      "C13.03": "The height of a section\nshould be determined by the amount of content it contains.",
      "C13.04": "The gap\nbetween elements should be determined by the typographic scale (in `rem`\nor Utopia space tokens).",
      "C13.05": "The number of columns in a grid should be\ndetermined by the minimum acceptable item width and the available space\n(via `auto-fit` and `minmax()`)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C13.01": {
        "start": 0,
        "end": 109
      },
      "C13.02": {
        "start": 110,
        "end": 216
      },
      "C13.03": {
        "start": 217,
        "end": 349
      },
      "C13.04": {
        "start": 350,
        "end": 456
      },
      "C13.05": {
        "start": 457,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f85c9989149c642d3483eb36d18e8e47c08a42367c6f871a5ef28b191a684e4f"
  },
  {
    "action_id": "A-C14",
    "claim_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
    ],
    "result_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
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
    "replacement": "A prescribed height constrains the box; content may overflow, clip or scroll, so verify that behavior against the task. Unknown or changing content is a reason to test clipping and overflow, not a universal argument against fixed heights. A pixel width encodes a fixed size; test it across viewport and user settings. A fixed width may still serve a defined task when its consequences are checked. A column count depends on available container space and track sizing. Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs.",
    "rationale": "Composed action for C14; fixed geometry assumptions and container-query claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C14.01": "A prescribed height constrains the box; content may overflow, clip or scroll, so verify that behavior against the task.",
      "C14.02": "Unknown or changing content is a reason to test clipping and overflow, not a universal argument against fixed heights.",
      "C14.03": "A pixel width encodes a fixed size; test it across viewport and user settings.",
      "C14.04": "A fixed width may still serve a defined task when its consequences are checked.",
      "C14.05": "A column count depends on available container space and track sizing.",
      "C14.06": "Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs."
    },
    "unit_subjects": {
      "C14.01": "When you prescribe a height, you are declaring that you know how much\ncontent will be present.",
      "C14.02": "You almost certainly do not.",
      "C14.03": "When you prescribe\na width in pixels, you are declaring that you know the user\\'s viewport\nsize.",
      "C14.04": "You do not.",
      "C14.05": "When you prescribe a column count, you are declaring\nthat you know the container\\'s width.",
      "C14.06": "In a world of container queries\nand intrinsic design, you should not need to."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C14.01": {
        "start": 0,
        "end": 119
      },
      "C14.02": {
        "start": 120,
        "end": 238
      },
      "C14.03": {
        "start": 239,
        "end": 317
      },
      "C14.04": {
        "start": 318,
        "end": 397
      },
      "C14.05": {
        "start": 398,
        "end": 467
      },
      "C14.06": {
        "start": 468,
        "end": 588
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "763f7fe98e8150a40a3ec40019cfda8c48958a229ddb4624d89f46f4a519505f"
  },
  {
    "action_id": "A-C15",
    "claim_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
    ],
    "result_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
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
    "replacement": "Let content inform dimensions where appropriate. Let available context inform arrangement. Designers set useful derivation rules and may also choose explicit values for justified cases.",
    "rationale": "Composed action for C15; design rule of derivation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C15.01": "Let content inform dimensions where appropriate.",
      "C15.02": "Let available context inform arrangement.",
      "C15.03": "Designers set useful derivation rules and may also choose explicit values for justified cases."
    },
    "unit_subjects": {
      "C15.01": "Content determines dimensions.",
      "C15.02": "Context determines arrangement.",
      "C15.03": "The\ndesigner\\'s job is to set the *rules of derivation*, not the values\nthemselves."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C15.01": {
        "start": 0,
        "end": 48
      },
      "C15.02": {
        "start": 49,
        "end": 90
      },
      "C15.03": {
        "start": 91,
        "end": 185
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6663d668b39712700795900b835e06f64d9b1b0b051d2a81ca86930db2040f0d"
  },
  {
    "action_id": "A-C16",
    "claim_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
    ],
    "result_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
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
    "disposition": "qualify",
    "replacement": "**The test:** if content doubles, check whether the task and layout remain usable. If the viewport halves, check reflow, overflow and task operation. Check combined changes too; these are diagnostics, not proof across all content or users.",
    "rationale": "Composed action for C16; content and viewport stress heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C16.01": "**The test:** if content doubles, check whether the task and layout remain usable.",
      "C16.02": "If the viewport halves, check reflow, overflow and task operation.",
      "C16.03": "Check combined changes too; these are diagnostics, not proof across all content or users."
    },
    "unit_subjects": {
      "C16.01": "**The test:** if the content doubles in length, does the layout still\nwork?",
      "C16.02": "If the viewport halves in width, does it still work?",
      "C16.03": "If both\nhappen simultaneously, does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C16.01": {
        "start": 0,
        "end": 82
      },
      "C16.02": {
        "start": 83,
        "end": 149
      },
      "C16.03": {
        "start": 150,
        "end": 239
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6ca282f7e6038af05a9f62214fc33f249d040eb89650603b65db0204ec799f37"
  },
  {
    "action_id": "A-C17",
    "claim_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
    ],
    "result_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
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
    "replacement": "An axiom can be a project-wide default, but “without exception” overstates its proper scope. Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target. Use Utopia spacing tokens as a local convention where they suit the composition. Implement shared defaults centrally, with documented exceptions and component-specific overrides.",
    "rationale": "Composed correction preserves all three examples while separating measure, target-size standards, spacing convention and universal-enforcement scope.",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C17.01": "An axiom can be a project-wide default, but “without exception” overstates its proper scope.",
      "C17.02": "Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content.",
      "C17.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target.",
      "C17.04": "Use Utopia spacing tokens as a local convention where they suit the composition.",
      "C17.05": "Implement shared defaults centrally, with documented exceptions and component-specific overrides."
    },
    "unit_subjects": {
      "C17.01": "An axiom is a design rule that pervades the entire system without\nexception.",
      "C17.02": "\\\"The measure shall not exceed 60ch.\\\"",
      "C17.03": "\\\"The minimum touch\ntarget shall be 44px.\\\"",
      "C17.04": "\\\"Spacing between sibling elements shall use\nUtopia space tokens.\\\"",
      "C17.05": "These are not guidelines to remember; they are\n*CSS declarations* that are written once and enforced everywhere."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C17.01": {
        "start": 0,
        "end": 92
      },
      "C17.02": {
        "start": 93,
        "end": 190
      },
      "C17.03": {
        "start": 191,
        "end": 499
      },
      "C17.04": {
        "start": 500,
        "end": 580
      },
      "C17.05": {
        "start": 581,
        "end": 678
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a0fad6ec591e09c01397b01e54cecd856c42210c8b46a41b40421434f69f5b5d"
  },
  {
    "action_id": "A-C18",
    "claim_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
    ],
    "result_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
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
    "replacement": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page. A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations. A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts. Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations.",
    "rationale": "Composed action for C18; attribution, correctness and verification guarantee",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C18.01": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page.",
      "C18.02": "A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations.",
      "C18.03": "A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts.",
      "C18.04": "Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations."
    },
    "unit_subjects": {
      "C18.01": "The crucial insight from Every Layout\\'s Axioms chapter is that\ndesigning by axiom means designing *without seeing*.",
      "C18.02": "You cannot predict\nevery visual consequence of a well-chosen axiom, and *you do not need\nto*.",
      "C18.03": "The axiom generates correct outcomes in contexts you never\nanticipated, because it encodes a *principle* rather than a *specific\narrangement*.",
      "C18.04": "This is what makes axiom-based design scale: it does not\nrequire a designer to manually verify every combination of content and\ncontext."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C18.01": {
        "start": 0,
        "end": 114
      },
      "C18.02": {
        "start": 115,
        "end": 222
      },
      "C18.03": {
        "start": 223,
        "end": 318
      },
      "C18.04": {
        "start": 319,
        "end": 421
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6b3e9c4f01fb049705c9594a3e6252f4bf77c6521fb1f0b0c8315156a6997ab8"
  },
  {
    "action_id": "A-C19",
    "claim_ids": [
      "C19.01",
      "C19.02"
    ],
    "result_ids": [
      "C19.01",
      "C19.02"
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
    "replacement": "Use a broad selector only with an explicit, bounded and tested exception set. Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions.",
    "rationale": "Composed action for C19; exception-based CSS approach",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C19.01": "Use a broad selector only with an explicit, bounded and tested exception set.",
      "C19.02": "Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions."
    },
    "unit_subjects": {
      "C19.01": "Axioms are best implemented using exception-based CSS: apply the rule to\neverything (`*`), then remove it from the specific elements that are\nlogical exceptions (containers, wrappers, structural elements).",
      "C19.02": "This\ninverted approach means you only need to *remember the exceptions*, not\nenumerate every element that should follow the rule."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C19.01": {
        "start": 0,
        "end": 77
      },
      "C19.02": {
        "start": 78,
        "end": 186
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5c85ed1a758f10d03851626634fdd038f232b4c7860ce36772a03862c4191505"
  },
  {
    "action_id": "A-C20",
    "claim_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
    ],
    "result_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
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
    "replacement": "**The test:** try stating each design rule in one sentence. Ask whether one declaration can express it in the intended context. A single declaration may encode a useful project axiom, subject to its scope and exceptions. A multi-part rule may be a convention or composition; complexity alone does not make it false.",
    "rationale": "Composed action for C20; axiom classification heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C20.01": "**The test:** try stating each design rule in one sentence.",
      "C20.02": "Ask whether one declaration can express it in the intended context.",
      "C20.03": "A single declaration may encode a useful project axiom, subject to its scope and exceptions.",
      "C20.04": "A multi-part rule may be a convention or composition; complexity alone does not make it false."
    },
    "unit_subjects": {
      "C20.01": "**The test:** can you state each design rule in a single sentence?",
      "C20.02": "Can\nthat sentence be translated into a single CSS declaration?",
      "C20.03": "If so, it is\nan axiom.",
      "C20.04": "If not, it may be a convention masquerading as a principle."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C20.01": {
        "start": 0,
        "end": 59
      },
      "C20.02": {
        "start": 60,
        "end": 127
      },
      "C20.03": {
        "start": 128,
        "end": 220
      },
      "C20.04": {
        "start": 221,
        "end": 315
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "b976a5e3a00cf2539c8f770649d989613b9e5287cc536503ce013e17f6dcd642"
  },
  {
    "action_id": "A-C21",
    "claim_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
    ],
    "result_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
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
    "disposition": "qualify",
    "replacement": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content. Use the measure axiom here only when a prose or task-specific measure is appropriate.\n\n**Mechanism:** `max-inline-size` with `margin-inline: auto`. In CSS Grid, §6.4 says auto margins absorb extra space for item alignment. CSS2.1 §10.3.3 centers a normal-flow, non-replaced block when width is not auto and both physical horizontal margins are auto; overconstraint has separate rules. `margin-inline` maps through writing mode, direction and text orientation. `max-inline-size` alone does not guarantee those conditions, so check free space and the actual formatting context.\n\n**Box-model note:** A `box-sizing: content-box` example makes the declared size apply to the content box, with padding outside it; verify that this matches the intended outer size.\n\n**Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers.",
    "rationale": "Composed action for C21; scoped configurable measure C21.04 replaces a detached retained fragment with an explicit box-model qualification.",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C21.01": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content.",
      "C21.02": "Use the measure axiom here only when a prose or task-specific measure is appropriate.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "**Box-model note:** A `box-sizing: content-box` example makes the declared size apply to the content box, with padding outside it; verify that this matches the intended outer size.",
      "C21.05": "**Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers."
    },
    "unit_subjects": {
      "C21.01": "**Responsibility:** constraining content to a maximum width and centring\nit horizontally.",
      "C21.02": "The measure axiom is typically enforced here.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` (maximum width, typically `60ch` for\nprose, wider for layout containers)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C21.01": {
        "start": 0,
        "end": 113
      },
      "C21.02": {
        "start": 114,
        "end": 199
      },
      "C21.03": {
        "start": 201,
        "end": 261
      },
      "C21.04": {
        "start": 691,
        "end": 871
      },
      "C21.05": {
        "start": 873,
        "end": 1003
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "b7ca017130c7a17c4a78e26c33fc940ec868f91d7377a80758c2bbea6100cb25"
  },
  {
    "action_id": "A-C22",
    "claim_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
    ],
    "result_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
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
    "replacement": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require. Begin without a breakpoint where intrinsic wrapping preserves the task.\n\n**Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs.\n\nThe threshold can be informed by content and container space; it is not automatically correct for every task.\n\n**Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes.",
    "rationale": "Composed action for C22; intrinsic Switcher threshold",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C22.01": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require.",
      "C22.02": "Begin without a breakpoint where intrinsic wrapping preserves the task.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs.",
      "C22.04": "The threshold can be informed by content and container space; it is not automatically correct for every task.",
      "C22.05": "**Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes."
    },
    "unit_subjects": {
      "C22.01": "**Responsibility:** switching between a multi-column and a single-column\nlayout based on available space.",
      "C22.02": "No breakpoints.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that\ncauses items to wrap at the threshold width.",
      "C22.04": "The threshold is defined by\nthe content, not the viewport.",
      "C22.05": "**Key parameter:** `--threshold` (the container width at which items\nstack)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C22.01": {
        "start": 0,
        "end": 123
      },
      "C22.02": {
        "start": 124,
        "end": 195
      },
      "C22.03": {
        "start": 197,
        "end": 369
      },
      "C22.04": {
        "start": 371,
        "end": 480
      },
      "C22.05": {
        "start": 482,
        "end": 594
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "3a5fe272643b6a3d771eccc763c70dc6186cf2f9a8bc543b5afdd3adf8cd2af3"
  },
  {
    "action_id": "A-C23",
    "claim_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
    ],
    "result_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
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
    "replacement": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method. They are the system’s “atoms,” a metaphor for reusable building blocks. Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them.",
    "rationale": "Composed action for C23; complete-vocabulary guarantee and composition model",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C23.01": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method.",
      "C23.02": "They are the system’s “atoms,” a metaphor for reusable building blocks.",
      "C23.03": "Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them."
    },
    "unit_subjects": {
      "C23.01": "Together, these thirteen primitives can compose any layout.",
      "C23.02": "They are the\n*atoms* of the system.",
      "C23.03": "Everything else --- cards, headers, navigation,\nforms, footers --- is a *molecule* composed from these atoms."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C23.01": {
        "start": 0,
        "end": 99
      },
      "C23.02": {
        "start": 100,
        "end": 171
      },
      "C23.03": {
        "start": 172,
        "end": 330
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "69a02e2590e7443d06cf9f7211c460f6294478d324ad953e3d2c0a74370fae35"
  },
  {
    "action_id": "A-C24",
    "claim_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "result_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      970,
      975
    ],
    "literal_offset_0based": [
      0,
      408
    ],
    "file_byte_offsets": [
      46170,
      46582
    ],
    "original": "Start at utopia.fyi and generate a type scale and space scale. Paste the\ncustom properties into your stylesheet. Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs. Set `max-inline-size: 60ch` on all text elements. Use\n`gap` with Utopia space tokens for all spacing. Write zero media\nqueries. You will be astonished at how far this gets you.",
    "disposition": "correct",
    "replacement": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them. Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet. Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported. Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role. Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions. Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode. Treat the result as a useful starting point and verify it against the actual content and contexts.",
    "rationale": "Composed action for C24; broad implementation prescription",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C24.01": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them.",
      "C24.02": "Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet.",
      "C24.03": "Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported.",
      "C24.04": "Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role.",
      "C24.05": "Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions.",
      "C24.06": "Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode.",
      "C24.07": "Treat the result as a useful starting point and verify it against the actual content and contexts."
    },
    "unit_subjects": {
      "C24.01": "Start at utopia.fyi and generate a type scale and space scale.",
      "C24.02": "Paste the\ncustom properties into your stylesheet.",
      "C24.03": "Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs.",
      "C24.04": "Set `max-inline-size: 60ch` on all text elements.",
      "C24.05": "Use\n`gap` with Utopia space tokens for all spacing.",
      "C24.06": "Write zero media\nqueries.",
      "C24.07": "You will be astonished at how far this gets you."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C24.01": {
        "start": 0,
        "end": 124
      },
      "C24.02": {
        "start": 125,
        "end": 265
      },
      "C24.03": {
        "start": 266,
        "end": 447
      },
      "C24.04": {
        "start": 448,
        "end": 569
      },
      "C24.05": {
        "start": 570,
        "end": 672
      },
      "C24.06": {
        "start": 673,
        "end": 837
      },
      "C24.07": {
        "start": 838,
        "end": 936
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "deda2f7a893b5db57b0491033811d64bafba7c7ecb61fbbd5542a3bc2064f337"
  },
  {
    "action_id": "A-C25",
    "claim_ids": [
      "C25.01",
      "C25.02"
    ],
    "result_ids": [
      "C25.01",
      "C25.02"
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
    "replacement": "Shift responsive decisions toward component space when the component context matters. `ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself.",
    "rationale": "Composed action for C25; ch units eliminate magic-number thresholds",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C25.01": "Shift responsive decisions toward component space when the component context matters.",
      "C25.02": "`ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself."
    },
    "unit_subjects": {
      "C25.01": "Shift responsive design from viewport to component.",
      "C25.02": "Using `ch` units in\ncontainer queries eliminates magic-number breakpoints entirely."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C25.01": {
        "start": 0,
        "end": 85
      },
      "C25.02": {
        "start": 86,
        "end": 223
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "7fa24f8936d4bbaaeb35982e5181f72a9976ac885475ded58817098b14e976be"
  },
  {
    "action_id": "A-C26",
    "claim_ids": [
      "C26.01",
      "C26.02"
    ],
    "result_ids": [
      "C26.01",
      "C26.02"
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
    "replacement": "Components can adapt to the space they occupy when a suitable query container exists. Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior.",
    "rationale": "Composed action for C26; container-context adaptation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C26.01": "Components can adapt to the space they occupy when a suitable query container exists.",
      "C26.02": "Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior."
    },
    "unit_subjects": {
      "C26.01": "Components adapt based on the space they actually occupy, not the\nbrowser window size.",
      "C26.02": "Combined with container query units (`cqw`, `cqh`),\nsizing becomes relative to context."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C26.01": {
        "start": 0,
        "end": 85
      },
      "C26.02": {
        "start": 86,
        "end": 205
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c768692e0aa996055f5df885f042e5c6a163c0a13454b456b94633bf7c27e0ae"
  }
]
```json
[
  {
    "action_id": "A-C01",
    "claim_ids": [
      "C01.01",
      "C01.02"
    ],
    "result_ids": [
      "C01.01",
      "C01.02"
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
    "replacement": "Use the listed primitives as a reusable composition method. Permit justified additional CSS rules when content, semantics or interaction requires them.",
    "rationale": "Composed action for C01; local layout-composition policy",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C01.01": "Use the listed primitives as a reusable composition method.",
      "C01.02": "Permit justified additional CSS rules when content, semantics or interaction requires them."
    },
    "unit_subjects": {
      "C01.01": "Every layout is a composition of these.",
      "C01.02": "No bespoke CSS layouts — compose from primitives."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C01.01": {
        "start": 0,
        "end": 59
      },
      "C01.02": {
        "start": 60,
        "end": 151
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5f313ae4620fcaa9df9eb4dc34bde5abe006a664f1e73e4a0b2db68eba9f70cc"
  },
  {
    "action_id": "A-C27",
    "claim_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
    ],
    "result_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
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
    "disposition": "qualify",
    "replacement": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow). A page header = Cover containing a Center containing a Stack. A navigation = Cluster inside a Box. These examples illustrate reuse; they do not define a complete layout grammar.",
    "rationale": "Composed action for C27; primitive composition example",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "unit_subjects": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C27.01": {
        "start": 0,
        "end": 83
      },
      "C27.02": {
        "start": 84,
        "end": 145
      },
      "C27.03": {
        "start": 146,
        "end": 182
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a123d41cbac2dd8e30b65473c5adf1a06039512ebaeeea15d61b4cee9ba7f250"
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
    "replacement": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |",
    "rationale": "Composed action for C02; measure default and scope",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C02": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |"
    },
    "unit_subjects": {
      "C02": "| **Center** | Max-width + horizontal centering | `max-inline-size: 60ch; margin-inline: auto` | Prose, any width-constrained content |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C02": {
        "start": 0,
        "end": 218
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "433051521d4e0c1886e3439557a5166fc4f3ad481ab2d3ffd6ea37f933039482"
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
    "disposition": "qualify",
    "replacement": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |",
    "rationale": "Composed action for C03; intrinsic switcher",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C03": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |"
    },
    "unit_subjects": {
      "C03": "| **Switcher** | Multi-col → single-col based on space | `flex-wrap: wrap` with calculated `flex-basis` | Responsive columns without breakpoints |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C03": {
        "start": 0,
        "end": 255
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c76a45616f2d3bd9b7fb1b9d2b9b42abbaecae0999e37421bb01bcb7d95716a8"
  },
  {
    "action_id": "A-C04",
    "claim_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
    ],
    "result_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
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
    "replacement": "Start with intrinsic layout and fluid constraints. Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation. Treat query removal as a diagnostic, not a universal pass condition.",
    "rationale": "Composed action for C04; zero-query rule and universal claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C04.01": "Start with intrinsic layout and fluid constraints.",
      "C04.02": "Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation.",
      "C04.03": "Treat query removal as a diagnostic, not a universal pass condition."
    },
    "unit_subjects": {
      "C04.01": "No media queries for layout.",
      "C04.02": "Primitives + fluid tokens handle all responsiveness.",
      "C04.03": "The test: if you removed every media query, would the layout still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C04.01": {
        "start": 0,
        "end": 50
      },
      "C04.02": {
        "start": 51,
        "end": 175
      },
      "C04.03": {
        "start": 176,
        "end": 244
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "1a8f7b8a870a41c3eeacb327a08e83c7ee9476e805d98f80f5685f95eb796e40"
  },
  {
    "action_id": "A-C05",
    "claim_ids": [
      "C05.02"
    ],
    "result_ids": [
      "C05.02"
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
    "replacement": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice.",
    "rationale": "Composed action for C05; query-free review heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C05.02": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice."
    },
    "unit_subjects": {
      "C05.02": "**Breakpoint test**: Remove all media queries mentally — does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C05.02": {
        "start": 0,
        "end": 149
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a92dabe84e417ebb94b4388dd8be3006a23e7c60f75b4d62f634a57417ae6995"
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
    "replacement": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n",
    "rationale": "Composed action for C06; universal measure rule with structural exceptions",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C06": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n"
    },
    "unit_subjects": {
      "C06": "* { max-inline-size: 60ch; }\nhtml, body, div, header, nav, main, footer { max-inline-size: none; }"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C06": {
        "start": 0,
        "end": 211
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6f515dc61b0e33865c57e8db11e7b92a07052c09028071b42719e50e2c04e699"
  },
  {
    "action_id": "A-C07-C08",
    "claim_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "result_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      144,
      151
    ],
    "literal_offset_0based": [
      0,
      513
    ],
    "file_byte_offsets": [
      6541,
      7066
    ],
    "original": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance. You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*. The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*. They are your CSS doing\nexactly what you intended.",
    "disposition": "qualify",
    "replacement": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked. Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception. A 60ch measure can guide prose; choose controls, data and other content by role. Use project conventions consistently while stating their scope and exceptions.",
    "rationale": "Composed action for C07; exceptionless axiom and universal enforcement",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C07.01": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked.",
      "C07.02": "Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception.",
      "C08.01": "A 60ch measure can guide prose; choose controls, data and other content by role.",
      "C08.02": "Use project conventions consistently while stating their scope and exceptions."
    },
    "unit_subjects": {
      "C07.01": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance.",
      "C07.02": "You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*.",
      "C08.01": "The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*.",
      "C08.02": "They are your CSS doing\nexactly what you intended."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C07.01": {
        "start": 0,
        "end": 99
      },
      "C07.02": {
        "start": 100,
        "end": 211
      },
      "C08.01": {
        "start": 212,
        "end": 292
      },
      "C08.02": {
        "start": 293,
        "end": 371
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "4fed4d0b7f32457d064cad64d8713dec9dd44764a4abb1b675d1d32a50eb8081"
  },
  {
    "action_id": "A-C09-C10",
    "claim_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
    ],
    "result_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
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
    "replacement": "Use constraints as a default method, while naming cases where a fixed value serves a requirement. A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target. Use `min-` and `max-` sizing properties to set bounds suited to the content. Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict. Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings. Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review.",
    "rationale": "Composed action for C09, C10; fixed values, measure and target examples CSS technique preference",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C09.01": "Use constraints as a default method, while naming cases where a fixed value serves a requirement.",
      "C09.02": "A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task.",
      "C09.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target.",
      "C10.01": "Use `min-` and `max-` sizing properties to set bounds suited to the content.",
      "C10.02": "Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict.",
      "C10.03": "Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings.",
      "C10.04": "Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review."
    },
    "unit_subjects": {
      "C09.01": "The single most important principle.",
      "C09.02": "Every fixed value in your CSS is a\nplace where you have overridden the browser\\'s judgment with your own.",
      "C09.03": "Sometimes this is necessary --- a maximum measure of `60ch`, a minimum\ntouch-target of `44px` --- but the default posture should always be to\n*suggest* rather than prescribe.",
      "C10.01": "Use `min-`, `max-`, and `clamp()`\ninstead of fixed values.",
      "C10.02": "Use `auto` instead of `100%`.",
      "C10.03": "Use `flex-basis`\ninstead of `width`.",
      "C10.04": "Each of these is an invitation for the browser to\nmake a contextually appropriate decision."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C09.01": {
        "start": 0,
        "end": 97
      },
      "C09.02": {
        "start": 98,
        "end": 221
      },
      "C09.03": {
        "start": 222,
        "end": 531
      },
      "C10.01": {
        "start": 532,
        "end": 608
      },
      "C10.02": {
        "start": 609,
        "end": 804
      },
      "C10.03": {
        "start": 805,
        "end": 926
      },
      "C10.04": {
        "start": 927,
        "end": 1194
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "dc5d34cb586c0753218f9d0134a48caa232fdc92d2b233915488fd20babcf408"
  },
  {
    "action_id": "A-C11",
    "claim_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
    ],
    "result_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
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
    "replacement": "This is a design preference for using browser and user context, not a claim of laziness. Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result. Constraints can support robust outcomes but cannot make good results inevitable across all contexts.",
    "rationale": "Composed action for C11; browser context and inevitable outcome",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C11.01": "This is a design preference for using browser and user context, not a claim of laziness.",
      "C11.02": "Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result.",
      "C11.03": "Constraints can support robust outcomes but cannot make good results inevitable across all contexts."
    },
    "unit_subjects": {
      "C11.01": "This is not laziness.",
      "C11.02": "It is recognition that the browser knows things\nyou do not --- the user\\'s font size preferences, their zoom level,\ntheir screen dimensions, whether they are using a split-screen view,\nwhether they have a notch or a toolbar.",
      "C11.03": "Your CSS should provide\n*constraints within which good outcomes are inevitable*, not blueprints\nthat are correct in one context and broken in all others."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C11.01": {
        "start": 0,
        "end": 88
      },
      "C11.02": {
        "start": 89,
        "end": 201
      },
      "C11.03": {
        "start": 202,
        "end": 302
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "80fcfa794d0a4bdc31cc231033005712b123547d7733807dc87bee77e628c67f"
  },
  {
    "action_id": "A-C12",
    "claim_ids": [
      "C12.01",
      "C12.02"
    ],
    "result_ids": [
      "C12.01",
      "C12.02"
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
    "replacement": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case. If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision.",
    "rationale": "Composed action for C12; query-free usability test",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C12.01": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case.",
      "C12.02": "If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision."
    },
    "unit_subjects": {
      "C12.01": "**The test:** if you removed every media query from your stylesheet,\nwould the layout still be usable?",
      "C12.02": "If not, your constraints are not yet\nwell enough chosen."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C12.01": {
        "start": 0,
        "end": 99
      },
      "C12.02": {
        "start": 100,
        "end": 209
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f7014ddad136381d870b9460fdd55d75a263b795fa3091311811ba49657b10fa"
  },
  {
    "action_id": "A-C13",
    "claim_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
    ],
    "result_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
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
    "replacement": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee. Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts. Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow. Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing. Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions.",
    "rationale": "Composed action for C13; content-derived dimension principles",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C13.01": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee.",
      "C13.02": "Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts.",
      "C13.03": "Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow.",
      "C13.04": "Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing.",
      "C13.05": "Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions."
    },
    "unit_subjects": {
      "C13.01": "The web is a content-driven medium.",
      "C13.02": "The width of a paragraph should be\ndetermined by its measure (in `ch` units).",
      "C13.03": "The height of a section\nshould be determined by the amount of content it contains.",
      "C13.04": "The gap\nbetween elements should be determined by the typographic scale (in `rem`\nor Utopia space tokens).",
      "C13.05": "The number of columns in a grid should be\ndetermined by the minimum acceptable item width and the available space\n(via `auto-fit` and `minmax()`)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C13.01": {
        "start": 0,
        "end": 109
      },
      "C13.02": {
        "start": 110,
        "end": 216
      },
      "C13.03": {
        "start": 217,
        "end": 349
      },
      "C13.04": {
        "start": 350,
        "end": 456
      },
      "C13.05": {
        "start": 457,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f85c9989149c642d3483eb36d18e8e47c08a42367c6f871a5ef28b191a684e4f"
  },
  {
    "action_id": "A-C14",
    "claim_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
    ],
    "result_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
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
    "replacement": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content. Content can change, so this is a reason to test the assumption, not a universal ban on heights. A pixel width encodes a fixed size; test it across viewport and user settings. A fixed width may still serve a defined task when its consequences are checked. A column count depends on available container space and track sizing. Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs.",
    "rationale": "Composed action for C14; fixed geometry assumptions and container-query claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C14.01": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content.",
      "C14.02": "Content can change, so this is a reason to test the assumption, not a universal ban on heights.",
      "C14.03": "A pixel width encodes a fixed size; test it across viewport and user settings.",
      "C14.04": "A fixed width may still serve a defined task when its consequences are checked.",
      "C14.05": "A column count depends on available container space and track sizing.",
      "C14.06": "Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs."
    },
    "unit_subjects": {
      "C14.01": "When you prescribe a height, you are declaring that you know how much\ncontent will be present.",
      "C14.02": "You almost certainly do not.",
      "C14.03": "When you prescribe\na width in pixels, you are declaring that you know the user\\'s viewport\nsize.",
      "C14.04": "You do not.",
      "C14.05": "When you prescribe a column count, you are declaring\nthat you know the container\\'s width.",
      "C14.06": "In a world of container queries\nand intrinsic design, you should not need to."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C14.01": {
        "start": 0,
        "end": 121
      },
      "C14.02": {
        "start": 122,
        "end": 217
      },
      "C14.03": {
        "start": 218,
        "end": 296
      },
      "C14.04": {
        "start": 297,
        "end": 376
      },
      "C14.05": {
        "start": 377,
        "end": 446
      },
      "C14.06": {
        "start": 447,
        "end": 567
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5b6a8b773598cd68090989852ac1728094b529af5fcdad1eee303098fc402931"
  },
  {
    "action_id": "A-C15",
    "claim_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
    ],
    "result_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
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
    "replacement": "Let content inform dimensions where appropriate. Let available context inform arrangement. Designers set useful derivation rules and may also choose explicit values for justified cases.",
    "rationale": "Composed action for C15; design rule of derivation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C15.01": "Let content inform dimensions where appropriate.",
      "C15.02": "Let available context inform arrangement.",
      "C15.03": "Designers set useful derivation rules and may also choose explicit values for justified cases."
    },
    "unit_subjects": {
      "C15.01": "Content determines dimensions.",
      "C15.02": "Context determines arrangement.",
      "C15.03": "The\ndesigner\\'s job is to set the *rules of derivation*, not the values\nthemselves."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C15.01": {
        "start": 0,
        "end": 48
      },
      "C15.02": {
        "start": 49,
        "end": 90
      },
      "C15.03": {
        "start": 91,
        "end": 185
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6663d668b39712700795900b835e06f64d9b1b0b051d2a81ca86930db2040f0d"
  },
  {
    "action_id": "A-C16",
    "claim_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
    ],
    "result_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
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
    "disposition": "qualify",
    "replacement": "**The test:** if content doubles, check whether the task and layout remain usable. If the viewport halves, check reflow, overflow and task operation. Check combined changes too; these are diagnostics, not proof across all content or users.",
    "rationale": "Composed action for C16; content and viewport stress heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C16.01": "**The test:** if content doubles, check whether the task and layout remain usable.",
      "C16.02": "If the viewport halves, check reflow, overflow and task operation.",
      "C16.03": "Check combined changes too; these are diagnostics, not proof across all content or users."
    },
    "unit_subjects": {
      "C16.01": "**The test:** if the content doubles in length, does the layout still\nwork?",
      "C16.02": "If the viewport halves in width, does it still work?",
      "C16.03": "If both\nhappen simultaneously, does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C16.01": {
        "start": 0,
        "end": 82
      },
      "C16.02": {
        "start": 83,
        "end": 149
      },
      "C16.03": {
        "start": 150,
        "end": 239
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6ca282f7e6038af05a9f62214fc33f249d040eb89650603b65db0204ec799f37"
  },
  {
    "action_id": "A-C17",
    "claim_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
    ],
    "result_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
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
    "replacement": "An axiom can be a project-wide default, but “without exception” overstates its proper scope. Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target. Use Utopia spacing tokens as a local convention where they suit the composition. Implement shared defaults centrally, with documented exceptions and component-specific overrides.",
    "rationale": "Composed correction preserves all three examples while separating measure, target-size standards, spacing convention and universal-enforcement scope.",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C17.01": "An axiom can be a project-wide default, but “without exception” overstates its proper scope.",
      "C17.02": "Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content.",
      "C17.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target.",
      "C17.04": "Use Utopia spacing tokens as a local convention where they suit the composition.",
      "C17.05": "Implement shared defaults centrally, with documented exceptions and component-specific overrides."
    },
    "unit_subjects": {
      "C17.01": "An axiom is a design rule that pervades the entire system without\nexception.",
      "C17.02": "\\\"The measure shall not exceed 60ch.\\\"",
      "C17.03": "\\\"The minimum touch\ntarget shall be 44px.\\\"",
      "C17.04": "\\\"Spacing between sibling elements shall use\nUtopia space tokens.\\\"",
      "C17.05": "These are not guidelines to remember; they are\n*CSS declarations* that are written once and enforced everywhere."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C17.01": {
        "start": 0,
        "end": 92
      },
      "C17.02": {
        "start": 93,
        "end": 190
      },
      "C17.03": {
        "start": 191,
        "end": 499
      },
      "C17.04": {
        "start": 500,
        "end": 580
      },
      "C17.05": {
        "start": 581,
        "end": 678
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a0fad6ec591e09c01397b01e54cecd856c42210c8b46a41b40421434f69f5b5d"
  },
  {
    "action_id": "A-C18",
    "claim_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
    ],
    "result_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
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
    "replacement": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page. A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations. A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts. Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations.",
    "rationale": "Composed action for C18; attribution, correctness and verification guarantee",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C18.01": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page.",
      "C18.02": "A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations.",
      "C18.03": "A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts.",
      "C18.04": "Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations."
    },
    "unit_subjects": {
      "C18.01": "The crucial insight from Every Layout\\'s Axioms chapter is that\ndesigning by axiom means designing *without seeing*.",
      "C18.02": "You cannot predict\nevery visual consequence of a well-chosen axiom, and *you do not need\nto*.",
      "C18.03": "The axiom generates correct outcomes in contexts you never\nanticipated, because it encodes a *principle* rather than a *specific\narrangement*.",
      "C18.04": "This is what makes axiom-based design scale: it does not\nrequire a designer to manually verify every combination of content and\ncontext."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C18.01": {
        "start": 0,
        "end": 114
      },
      "C18.02": {
        "start": 115,
        "end": 222
      },
      "C18.03": {
        "start": 223,
        "end": 318
      },
      "C18.04": {
        "start": 319,
        "end": 421
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6b3e9c4f01fb049705c9594a3e6252f4bf77c6521fb1f0b0c8315156a6997ab8"
  },
  {
    "action_id": "A-C19",
    "claim_ids": [
      "C19.01",
      "C19.02"
    ],
    "result_ids": [
      "C19.01",
      "C19.02"
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
    "replacement": "Use a broad selector only with an explicit, bounded and tested exception set. Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions.",
    "rationale": "Composed action for C19; exception-based CSS approach",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C19.01": "Use a broad selector only with an explicit, bounded and tested exception set.",
      "C19.02": "Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions."
    },
    "unit_subjects": {
      "C19.01": "Axioms are best implemented using exception-based CSS: apply the rule to\neverything (`*`), then remove it from the specific elements that are\nlogical exceptions (containers, wrappers, structural elements).",
      "C19.02": "This\ninverted approach means you only need to *remember the exceptions*, not\nenumerate every element that should follow the rule."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C19.01": {
        "start": 0,
        "end": 77
      },
      "C19.02": {
        "start": 78,
        "end": 186
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5c85ed1a758f10d03851626634fdd038f232b4c7860ce36772a03862c4191505"
  },
  {
    "action_id": "A-C20",
    "claim_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
    ],
    "result_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
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
    "replacement": "**The test:** try stating each design rule in one sentence. Ask whether one declaration can express it in the intended context. A single declaration may encode a useful project axiom, subject to its scope and exceptions. A multi-part rule may be a convention or composition; complexity alone does not make it false.",
    "rationale": "Composed action for C20; axiom classification heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C20.01": "**The test:** try stating each design rule in one sentence.",
      "C20.02": "Ask whether one declaration can express it in the intended context.",
      "C20.03": "A single declaration may encode a useful project axiom, subject to its scope and exceptions.",
      "C20.04": "A multi-part rule may be a convention or composition; complexity alone does not make it false."
    },
    "unit_subjects": {
      "C20.01": "**The test:** can you state each design rule in a single sentence?",
      "C20.02": "Can\nthat sentence be translated into a single CSS declaration?",
      "C20.03": "If so, it is\nan axiom.",
      "C20.04": "If not, it may be a convention masquerading as a principle."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C20.01": {
        "start": 0,
        "end": 59
      },
      "C20.02": {
        "start": 60,
        "end": 127
      },
      "C20.03": {
        "start": 128,
        "end": 220
      },
      "C20.04": {
        "start": 221,
        "end": 315
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "b976a5e3a00cf2539c8f770649d989613b9e5287cc536503ce013e17f6dcd642"
  },
  {
    "action_id": "A-C21",
    "claim_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
    ],
    "result_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
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
    "disposition": "qualify",
    "replacement": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content. Use the measure axiom here only when a prose or task-specific measure is appropriate. **Mechanism:** `max-inline-size` with `margin-inline: auto`. In CSS Grid, §6.4 says auto margins absorb extra space for item alignment. CSS2.1 §10.3.3 centers a normal-flow, non-replaced block when width is not auto and both physical horizontal margins are auto; overconstraint has separate rules. `margin-inline` maps through writing mode, direction and text orientation. `max-inline-size` alone does not guarantee those conditions, so check free space and the actual formatting context. Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea. **Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers.",
    "rationale": "Composed action for C21; scoped configurable measure",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C21.01": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content.",
      "C21.02": "Use the measure axiom here only when a prose or task-specific measure is appropriate.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers."
    },
    "unit_subjects": {
      "C21.01": "**Responsibility:** constraining content to a maximum width and centring\nit horizontally.",
      "C21.02": "The measure axiom is typically enforced here.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` (maximum width, typically `60ch` for\nprose, wider for layout containers)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C21.01": {
        "start": 0,
        "end": 113
      },
      "C21.02": {
        "start": 114,
        "end": 199
      },
      "C21.03": {
        "start": 200,
        "end": 260
      },
      "C21.04": {
        "start": 689,
        "end": 769
      },
      "C21.05": {
        "start": 770,
        "end": 900
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a9441d2e3e05a1866f3c6d5cdee1a10df6bc1a86a41e0428cd2f4b060e862fdd"
  },
  {
    "action_id": "A-C22",
    "claim_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
    ],
    "result_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
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
    "replacement": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require. Begin without a breakpoint where intrinsic wrapping preserves the task. **Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs. The threshold can be informed by content and container space; it is not automatically correct for every task. **Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes.",
    "rationale": "Composed action for C22; intrinsic Switcher threshold",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C22.01": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require.",
      "C22.02": "Begin without a breakpoint where intrinsic wrapping preserves the task.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs.",
      "C22.04": "The threshold can be informed by content and container space; it is not automatically correct for every task.",
      "C22.05": "**Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes."
    },
    "unit_subjects": {
      "C22.01": "**Responsibility:** switching between a multi-column and a single-column\nlayout based on available space.",
      "C22.02": "No breakpoints.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that\ncauses items to wrap at the threshold width.",
      "C22.04": "The threshold is defined by\nthe content, not the viewport.",
      "C22.05": "**Key parameter:** `--threshold` (the container width at which items\nstack)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C22.01": {
        "start": 0,
        "end": 123
      },
      "C22.02": {
        "start": 124,
        "end": 195
      },
      "C22.03": {
        "start": 196,
        "end": 368
      },
      "C22.04": {
        "start": 369,
        "end": 478
      },
      "C22.05": {
        "start": 479,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "bfe50f44830c6ff0658c2d3703a4c8d8f1ad1001a49597fd8de6ad18f0f58d07"
  },
  {
    "action_id": "A-C23",
    "claim_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
    ],
    "result_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
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
    "replacement": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method. They are the system’s “atoms,” a metaphor for reusable building blocks. Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them.",
    "rationale": "Composed action for C23; complete-vocabulary guarantee and composition model",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C23.01": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method.",
      "C23.02": "They are the system’s “atoms,” a metaphor for reusable building blocks.",
      "C23.03": "Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them."
    },
    "unit_subjects": {
      "C23.01": "Together, these thirteen primitives can compose any layout.",
      "C23.02": "They are the\n*atoms* of the system.",
      "C23.03": "Everything else --- cards, headers, navigation,\nforms, footers --- is a *molecule* composed from these atoms."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C23.01": {
        "start": 0,
        "end": 99
      },
      "C23.02": {
        "start": 100,
        "end": 171
      },
      "C23.03": {
        "start": 172,
        "end": 330
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "69a02e2590e7443d06cf9f7211c460f6294478d324ad953e3d2c0a74370fae35"
  },
  {
    "action_id": "A-C24",
    "claim_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "result_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      970,
      975
    ],
    "literal_offset_0based": [
      0,
      408
    ],
    "file_byte_offsets": [
      46170,
      46582
    ],
    "original": "Start at utopia.fyi and generate a type scale and space scale. Paste the\ncustom properties into your stylesheet. Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs. Set `max-inline-size: 60ch` on all text elements. Use\n`gap` with Utopia space tokens for all spacing. Write zero media\nqueries. You will be astonished at how far this gets you.",
    "disposition": "correct",
    "replacement": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them. Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet. Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported. Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role. Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions. Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode. Treat the result as a useful starting point and verify it against the actual content and contexts.",
    "rationale": "Composed action for C24; broad implementation prescription",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C24.01": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them.",
      "C24.02": "Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet.",
      "C24.03": "Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported.",
      "C24.04": "Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role.",
      "C24.05": "Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions.",
      "C24.06": "Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode.",
      "C24.07": "Treat the result as a useful starting point and verify it against the actual content and contexts."
    },
    "unit_subjects": {
      "C24.01": "Start at utopia.fyi and generate a type scale and space scale.",
      "C24.02": "Paste the\ncustom properties into your stylesheet.",
      "C24.03": "Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs.",
      "C24.04": "Set `max-inline-size: 60ch` on all text elements.",
      "C24.05": "Use\n`gap` with Utopia space tokens for all spacing.",
      "C24.06": "Write zero media\nqueries.",
      "C24.07": "You will be astonished at how far this gets you."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C24.01": {
        "start": 0,
        "end": 124
      },
      "C24.02": {
        "start": 125,
        "end": 265
      },
      "C24.03": {
        "start": 266,
        "end": 447
      },
      "C24.04": {
        "start": 448,
        "end": 569
      },
      "C24.05": {
        "start": 570,
        "end": 672
      },
      "C24.06": {
        "start": 673,
        "end": 837
      },
      "C24.07": {
        "start": 838,
        "end": 936
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "deda2f7a893b5db57b0491033811d64bafba7c7ecb61fbbd5542a3bc2064f337"
  },
  {
    "action_id": "A-C25",
    "claim_ids": [
      "C25.01",
      "C25.02"
    ],
    "result_ids": [
      "C25.01",
      "C25.02"
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
    "replacement": "Shift responsive decisions toward component space when the component context matters. `ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself.",
    "rationale": "Composed action for C25; ch units eliminate magic-number thresholds",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C25.01": "Shift responsive decisions toward component space when the component context matters.",
      "C25.02": "`ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself."
    },
    "unit_subjects": {
      "C25.01": "Shift responsive design from viewport to component.",
      "C25.02": "Using `ch` units in\ncontainer queries eliminates magic-number breakpoints entirely."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C25.01": {
        "start": 0,
        "end": 85
      },
      "C25.02": {
        "start": 86,
        "end": 223
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "7fa24f8936d4bbaaeb35982e5181f72a9976ac885475ded58817098b14e976be"
  },
  {
    "action_id": "A-C26",
    "claim_ids": [
      "C26.01",
      "C26.02"
    ],
    "result_ids": [
      "C26.01",
      "C26.02"
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
    "replacement": "Components can adapt to the space they occupy when a suitable query container exists. Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior.",
    "rationale": "Composed action for C26; container-context adaptation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C26.01": "Components can adapt to the space they occupy when a suitable query container exists.",
      "C26.02": "Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior."
    },
    "unit_subjects": {
      "C26.01": "Components adapt based on the space they actually occupy, not the\nbrowser window size.",
      "C26.02": "Combined with container query units (`cqw`, `cqh`),\nsizing becomes relative to context."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C26.01": {
        "start": 0,
        "end": 85
      },
      "C26.02": {
        "start": 86,
        "end": 205
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c768692e0aa996055f5df885f042e5c6a163c0a13454b456b94633bf7c27e0ae"
  }
]
```json
[
  {
    "action_id": "A-C01",
    "claim_ids": [
      "C01.01",
      "C01.02"
    ],
    "result_ids": [
      "C01.01",
      "C01.02"
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
    "replacement": "Use the listed primitives as a reusable composition method. Permit justified additional CSS rules when content, semantics or interaction requires them.",
    "rationale": "Composed action for C01; local layout-composition policy",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C01.01": "Use the listed primitives as a reusable composition method.",
      "C01.02": "Permit justified additional CSS rules when content, semantics or interaction requires them."
    },
    "unit_subjects": {
      "C01.01": "Every layout is a composition of these.",
      "C01.02": "No bespoke CSS layouts — compose from primitives."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C01.01": {
        "start": 0,
        "end": 59
      },
      "C01.02": {
        "start": 60,
        "end": 151
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5f313ae4620fcaa9df9eb4dc34bde5abe006a664f1e73e4a0b2db68eba9f70cc"
  },
  {
    "action_id": "A-C27",
    "claim_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
    ],
    "result_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
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
    "disposition": "qualify",
    "replacement": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow). A page header = Cover containing a Center containing a Stack. A navigation = Cluster inside a Box. These examples illustrate reuse; they do not define a complete layout grammar.",
    "rationale": "Composed action for C27; primitive composition example",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "unit_subjects": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C27.01": {
        "start": 0,
        "end": 83
      },
      "C27.02": {
        "start": 84,
        "end": 145
      },
      "C27.03": {
        "start": 146,
        "end": 182
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a123d41cbac2dd8e30b65473c5adf1a06039512ebaeeea15d61b4cee9ba7f250"
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
    "replacement": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |",
    "rationale": "Composed action for C02; measure default and scope",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C02": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |"
    },
    "unit_subjects": {
      "C02": "| **Center** | Max-width + horizontal centering | `max-inline-size: 60ch; margin-inline: auto` | Prose, any width-constrained content |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C02": {
        "start": 0,
        "end": 218
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "433051521d4e0c1886e3439557a5166fc4f3ad481ab2d3ffd6ea37f933039482"
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
    "disposition": "qualify",
    "replacement": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |",
    "rationale": "Composed action for C03; intrinsic switcher",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C03": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |"
    },
    "unit_subjects": {
      "C03": "| **Switcher** | Multi-col → single-col based on space | `flex-wrap: wrap` with calculated `flex-basis` | Responsive columns without breakpoints |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C03": {
        "start": 0,
        "end": 255
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c76a45616f2d3bd9b7fb1b9d2b9b42abbaecae0999e37421bb01bcb7d95716a8"
  },
  {
    "action_id": "A-C04",
    "claim_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
    ],
    "result_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
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
    "replacement": "Start with intrinsic layout and fluid constraints. Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation. Treat query removal as a diagnostic, not a universal pass condition.",
    "rationale": "Composed action for C04; zero-query rule and universal claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C04.01": "Start with intrinsic layout and fluid constraints.",
      "C04.02": "Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation.",
      "C04.03": "Treat query removal as a diagnostic, not a universal pass condition."
    },
    "unit_subjects": {
      "C04.01": "No media queries for layout.",
      "C04.02": "Primitives + fluid tokens handle all responsiveness.",
      "C04.03": "The test: if you removed every media query, would the layout still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C04.01": {
        "start": 0,
        "end": 50
      },
      "C04.02": {
        "start": 51,
        "end": 175
      },
      "C04.03": {
        "start": 176,
        "end": 244
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "1a8f7b8a870a41c3eeacb327a08e83c7ee9476e805d98f80f5685f95eb796e40"
  },
  {
    "action_id": "A-C05",
    "claim_ids": [
      "C05.02"
    ],
    "result_ids": [
      "C05.02"
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
    "replacement": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice.",
    "rationale": "Composed action for C05; query-free review heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C05.02": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice."
    },
    "unit_subjects": {
      "C05.02": "**Breakpoint test**: Remove all media queries mentally — does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C05.02": {
        "start": 0,
        "end": 149
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a92dabe84e417ebb94b4388dd8be3006a23e7c60f75b4d62f634a57417ae6995"
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
    "replacement": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n",
    "rationale": "Composed action for C06; universal measure rule with structural exceptions",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C06": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n"
    },
    "unit_subjects": {
      "C06": "* { max-inline-size: 60ch; }\nhtml, body, div, header, nav, main, footer { max-inline-size: none; }"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C06": {
        "start": 0,
        "end": 211
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6f515dc61b0e33865c57e8db11e7b92a07052c09028071b42719e50e2c04e699"
  },
  {
    "action_id": "A-C07-C08",
    "claim_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "result_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      144,
      151
    ],
    "literal_offset_0based": [
      0,
      513
    ],
    "file_byte_offsets": [
      6541,
      7066
    ],
    "original": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance. You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*. The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*. They are your CSS doing\nexactly what you intended.",
    "disposition": "qualify",
    "replacement": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked. Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception. A 60ch measure can guide prose; choose controls, data and other content by role. Use project conventions consistently while stating their scope and exceptions.",
    "rationale": "Composed action for C07; exceptionless axiom and universal enforcement",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C07.01": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked.",
      "C07.02": "Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception.",
      "C08.01": "A 60ch measure can guide prose; choose controls, data and other content by role.",
      "C08.02": "Use project conventions consistently while stating their scope and exceptions."
    },
    "unit_subjects": {
      "C07.01": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance.",
      "C07.02": "You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*.",
      "C08.01": "The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*.",
      "C08.02": "They are your CSS doing\nexactly what you intended."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C07.01": {
        "start": 0,
        "end": 99
      },
      "C07.02": {
        "start": 100,
        "end": 211
      },
      "C08.01": {
        "start": 212,
        "end": 292
      },
      "C08.02": {
        "start": 293,
        "end": 371
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "4fed4d0b7f32457d064cad64d8713dec9dd44764a4abb1b675d1d32a50eb8081"
  },
  {
    "action_id": "A-C09-C10",
    "claim_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
    ],
    "result_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
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
    "replacement": "Use constraints as a default method, while naming cases where a fixed value serves a requirement. A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target. Use `min-` and `max-` sizing properties to set bounds suited to the content. Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict. Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings. Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review.",
    "rationale": "Composed action for C09, C10; fixed values, measure and target examples CSS technique preference",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C09.01": "Use constraints as a default method, while naming cases where a fixed value serves a requirement.",
      "C09.02": "A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task.",
      "C09.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target.",
      "C10.01": "Use `min-` and `max-` sizing properties to set bounds suited to the content.",
      "C10.02": "Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict.",
      "C10.03": "Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings.",
      "C10.04": "Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review."
    },
    "unit_subjects": {
      "C09.01": "The single most important principle.",
      "C09.02": "Every fixed value in your CSS is a\nplace where you have overridden the browser\\'s judgment with your own.",
      "C09.03": "Sometimes this is necessary --- a maximum measure of `60ch`, a minimum\ntouch-target of `44px` --- but the default posture should always be to\n*suggest* rather than prescribe.",
      "C10.01": "Use `min-`, `max-`, and `clamp()`\ninstead of fixed values.",
      "C10.02": "Use `auto` instead of `100%`.",
      "C10.03": "Use `flex-basis`\ninstead of `width`.",
      "C10.04": "Each of these is an invitation for the browser to\nmake a contextually appropriate decision."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C09.01": {
        "start": 0,
        "end": 97
      },
      "C09.02": {
        "start": 98,
        "end": 221
      },
      "C09.03": {
        "start": 222,
        "end": 531
      },
      "C10.01": {
        "start": 532,
        "end": 608
      },
      "C10.02": {
        "start": 609,
        "end": 804
      },
      "C10.03": {
        "start": 805,
        "end": 926
      },
      "C10.04": {
        "start": 927,
        "end": 1194
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "dc5d34cb586c0753218f9d0134a48caa232fdc92d2b233915488fd20babcf408"
  },
  {
    "action_id": "A-C11",
    "claim_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
    ],
    "result_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
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
    "replacement": "This is a design preference for using browser and user context, not a claim of laziness. Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result. Constraints can support robust outcomes but cannot make good results inevitable across all contexts.",
    "rationale": "Composed action for C11; browser context and inevitable outcome",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C11.01": "This is a design preference for using browser and user context, not a claim of laziness.",
      "C11.02": "Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result.",
      "C11.03": "Constraints can support robust outcomes but cannot make good results inevitable across all contexts."
    },
    "unit_subjects": {
      "C11.01": "This is not laziness.",
      "C11.02": "It is recognition that the browser knows things\nyou do not --- the user\\'s font size preferences, their zoom level,\ntheir screen dimensions, whether they are using a split-screen view,\nwhether they have a notch or a toolbar.",
      "C11.03": "Your CSS should provide\n*constraints within which good outcomes are inevitable*, not blueprints\nthat are correct in one context and broken in all others."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C11.01": {
        "start": 0,
        "end": 88
      },
      "C11.02": {
        "start": 89,
        "end": 201
      },
      "C11.03": {
        "start": 202,
        "end": 302
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "80fcfa794d0a4bdc31cc231033005712b123547d7733807dc87bee77e628c67f"
  },
  {
    "action_id": "A-C12",
    "claim_ids": [
      "C12.01",
      "C12.02"
    ],
    "result_ids": [
      "C12.01",
      "C12.02"
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
    "replacement": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case. If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision.",
    "rationale": "Composed action for C12; query-free usability test",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C12.01": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case.",
      "C12.02": "If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision."
    },
    "unit_subjects": {
      "C12.01": "**The test:** if you removed every media query from your stylesheet,\nwould the layout still be usable?",
      "C12.02": "If not, your constraints are not yet\nwell enough chosen."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C12.01": {
        "start": 0,
        "end": 99
      },
      "C12.02": {
        "start": 100,
        "end": 209
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f7014ddad136381d870b9460fdd55d75a263b795fa3091311811ba49657b10fa"
  },
  {
    "action_id": "A-C13",
    "claim_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
    ],
    "result_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
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
    "replacement": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee. Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts. Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow. Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing. Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions.",
    "rationale": "Composed action for C13; content-derived dimension principles",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C13.01": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee.",
      "C13.02": "Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts.",
      "C13.03": "Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow.",
      "C13.04": "Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing.",
      "C13.05": "Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions."
    },
    "unit_subjects": {
      "C13.01": "The web is a content-driven medium.",
      "C13.02": "The width of a paragraph should be\ndetermined by its measure (in `ch` units).",
      "C13.03": "The height of a section\nshould be determined by the amount of content it contains.",
      "C13.04": "The gap\nbetween elements should be determined by the typographic scale (in `rem`\nor Utopia space tokens).",
      "C13.05": "The number of columns in a grid should be\ndetermined by the minimum acceptable item width and the available space\n(via `auto-fit` and `minmax()`)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C13.01": {
        "start": 0,
        "end": 109
      },
      "C13.02": {
        "start": 110,
        "end": 216
      },
      "C13.03": {
        "start": 217,
        "end": 349
      },
      "C13.04": {
        "start": 350,
        "end": 456
      },
      "C13.05": {
        "start": 457,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f85c9989149c642d3483eb36d18e8e47c08a42367c6f871a5ef28b191a684e4f"
  },
  {
    "action_id": "A-C14",
    "claim_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
    ],
    "result_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
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
    "replacement": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content. Content can change, so this is a reason to test the assumption, not a universal ban on heights. A pixel width encodes a fixed size; test it across viewport and user settings. A fixed width may still serve a defined task when its consequences are checked. A column count depends on available container space and track sizing. Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs.",
    "rationale": "Composed action for C14; fixed geometry assumptions and container-query claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C14.01": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content.",
      "C14.02": "Content can change, so this is a reason to test the assumption, not a universal ban on heights.",
      "C14.03": "A pixel width encodes a fixed size; test it across viewport and user settings.",
      "C14.04": "A fixed width may still serve a defined task when its consequences are checked.",
      "C14.05": "A column count depends on available container space and track sizing.",
      "C14.06": "Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs."
    },
    "unit_subjects": {
      "C14.01": "When you prescribe a height, you are declaring that you know how much\ncontent will be present.",
      "C14.02": "You almost certainly do not.",
      "C14.03": "When you prescribe\na width in pixels, you are declaring that you know the user\\'s viewport\nsize.",
      "C14.04": "You do not.",
      "C14.05": "When you prescribe a column count, you are declaring\nthat you know the container\\'s width.",
      "C14.06": "In a world of container queries\nand intrinsic design, you should not need to."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C14.01": {
        "start": 0,
        "end": 121
      },
      "C14.02": {
        "start": 122,
        "end": 217
      },
      "C14.03": {
        "start": 218,
        "end": 296
      },
      "C14.04": {
        "start": 297,
        "end": 376
      },
      "C14.05": {
        "start": 377,
        "end": 446
      },
      "C14.06": {
        "start": 447,
        "end": 567
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5b6a8b773598cd68090989852ac1728094b529af5fcdad1eee303098fc402931"
  },
  {
    "action_id": "A-C15",
    "claim_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
    ],
    "result_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
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
    "replacement": "Let content inform dimensions where appropriate. Let available context inform arrangement. Designers set useful derivation rules and may also choose explicit values for justified cases.",
    "rationale": "Composed action for C15; design rule of derivation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C15.01": "Let content inform dimensions where appropriate.",
      "C15.02": "Let available context inform arrangement.",
      "C15.03": "Designers set useful derivation rules and may also choose explicit values for justified cases."
    },
    "unit_subjects": {
      "C15.01": "Content determines dimensions.",
      "C15.02": "Context determines arrangement.",
      "C15.03": "The\ndesigner\\'s job is to set the *rules of derivation*, not the values\nthemselves."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C15.01": {
        "start": 0,
        "end": 48
      },
      "C15.02": {
        "start": 49,
        "end": 90
      },
      "C15.03": {
        "start": 91,
        "end": 185
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6663d668b39712700795900b835e06f64d9b1b0b051d2a81ca86930db2040f0d"
  },
  {
    "action_id": "A-C16",
    "claim_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
    ],
    "result_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
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
    "disposition": "qualify",
    "replacement": "**The test:** if content doubles, check whether the task and layout remain usable. If the viewport halves, check reflow, overflow and task operation. Check combined changes too; these are diagnostics, not proof across all content or users.",
    "rationale": "Composed action for C16; content and viewport stress heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C16.01": "**The test:** if content doubles, check whether the task and layout remain usable.",
      "C16.02": "If the viewport halves, check reflow, overflow and task operation.",
      "C16.03": "Check combined changes too; these are diagnostics, not proof across all content or users."
    },
    "unit_subjects": {
      "C16.01": "**The test:** if the content doubles in length, does the layout still\nwork?",
      "C16.02": "If the viewport halves in width, does it still work?",
      "C16.03": "If both\nhappen simultaneously, does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C16.01": {
        "start": 0,
        "end": 82
      },
      "C16.02": {
        "start": 83,
        "end": 149
      },
      "C16.03": {
        "start": 150,
        "end": 239
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6ca282f7e6038af05a9f62214fc33f249d040eb89650603b65db0204ec799f37"
  },
  {
    "action_id": "A-C17",
    "claim_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
    ],
    "result_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
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
    "replacement": "An axiom can be a project-wide default, but “without exception” overstates its proper scope. Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target. Use Utopia spacing tokens as a local convention where they suit the composition. Implement shared defaults centrally, with documented exceptions and component-specific overrides.",
    "rationale": "Composed correction preserves all three examples while separating measure, target-size standards, spacing convention and universal-enforcement scope.",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C17.01": "An axiom can be a project-wide default, but “without exception” overstates its proper scope.",
      "C17.02": "Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content.",
      "C17.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target.",
      "C17.04": "Use Utopia spacing tokens as a local convention where they suit the composition.",
      "C17.05": "Implement shared defaults centrally, with documented exceptions and component-specific overrides."
    },
    "unit_subjects": {
      "C17.01": "An axiom is a design rule that pervades the entire system without\nexception.",
      "C17.02": "\\\"The measure shall not exceed 60ch.\\\"",
      "C17.03": "\\\"The minimum touch\ntarget shall be 44px.\\\"",
      "C17.04": "\\\"Spacing between sibling elements shall use\nUtopia space tokens.\\\"",
      "C17.05": "These are not guidelines to remember; they are\n*CSS declarations* that are written once and enforced everywhere."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C17.01": {
        "start": 0,
        "end": 92
      },
      "C17.02": {
        "start": 93,
        "end": 190
      },
      "C17.03": {
        "start": 191,
        "end": 499
      },
      "C17.04": {
        "start": 500,
        "end": 580
      },
      "C17.05": {
        "start": 581,
        "end": 678
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a0fad6ec591e09c01397b01e54cecd856c42210c8b46a41b40421434f69f5b5d"
  },
  {
    "action_id": "A-C18",
    "claim_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
    ],
    "result_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
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
    "replacement": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page. A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations. A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts. Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations.",
    "rationale": "Composed action for C18; attribution, correctness and verification guarantee",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C18.01": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page.",
      "C18.02": "A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations.",
      "C18.03": "A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts.",
      "C18.04": "Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations."
    },
    "unit_subjects": {
      "C18.01": "The crucial insight from Every Layout\\'s Axioms chapter is that\ndesigning by axiom means designing *without seeing*.",
      "C18.02": "You cannot predict\nevery visual consequence of a well-chosen axiom, and *you do not need\nto*.",
      "C18.03": "The axiom generates correct outcomes in contexts you never\nanticipated, because it encodes a *principle* rather than a *specific\narrangement*.",
      "C18.04": "This is what makes axiom-based design scale: it does not\nrequire a designer to manually verify every combination of content and\ncontext."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C18.01": {
        "start": 0,
        "end": 114
      },
      "C18.02": {
        "start": 115,
        "end": 222
      },
      "C18.03": {
        "start": 223,
        "end": 318
      },
      "C18.04": {
        "start": 319,
        "end": 421
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6b3e9c4f01fb049705c9594a3e6252f4bf77c6521fb1f0b0c8315156a6997ab8"
  },
  {
    "action_id": "A-C19",
    "claim_ids": [
      "C19.01",
      "C19.02"
    ],
    "result_ids": [
      "C19.01",
      "C19.02"
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
    "replacement": "Use a broad selector only with an explicit, bounded and tested exception set. Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions.",
    "rationale": "Composed action for C19; exception-based CSS approach",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C19.01": "Use a broad selector only with an explicit, bounded and tested exception set.",
      "C19.02": "Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions."
    },
    "unit_subjects": {
      "C19.01": "Axioms are best implemented using exception-based CSS: apply the rule to\neverything (`*`), then remove it from the specific elements that are\nlogical exceptions (containers, wrappers, structural elements).",
      "C19.02": "This\ninverted approach means you only need to *remember the exceptions*, not\nenumerate every element that should follow the rule."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C19.01": {
        "start": 0,
        "end": 77
      },
      "C19.02": {
        "start": 78,
        "end": 186
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5c85ed1a758f10d03851626634fdd038f232b4c7860ce36772a03862c4191505"
  },
  {
    "action_id": "A-C20",
    "claim_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
    ],
    "result_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
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
    "replacement": "**The test:** try stating each design rule in one sentence. Ask whether one declaration can express it in the intended context. A single declaration may encode a useful project axiom, subject to its scope and exceptions. A multi-part rule may be a convention or composition; complexity alone does not make it false.",
    "rationale": "Composed action for C20; axiom classification heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C20.01": "**The test:** try stating each design rule in one sentence.",
      "C20.02": "Ask whether one declaration can express it in the intended context.",
      "C20.03": "A single declaration may encode a useful project axiom, subject to its scope and exceptions.",
      "C20.04": "A multi-part rule may be a convention or composition; complexity alone does not make it false."
    },
    "unit_subjects": {
      "C20.01": "**The test:** can you state each design rule in a single sentence?",
      "C20.02": "Can\nthat sentence be translated into a single CSS declaration?",
      "C20.03": "If so, it is\nan axiom.",
      "C20.04": "If not, it may be a convention masquerading as a principle."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C20.01": {
        "start": 0,
        "end": 59
      },
      "C20.02": {
        "start": 60,
        "end": 127
      },
      "C20.03": {
        "start": 128,
        "end": 220
      },
      "C20.04": {
        "start": 221,
        "end": 315
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "b976a5e3a00cf2539c8f770649d989613b9e5287cc536503ce013e17f6dcd642"
  },
  {
    "action_id": "A-C21",
    "claim_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
    ],
    "result_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
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
    "disposition": "qualify",
    "replacement": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content. Use the measure axiom here only when a prose or task-specific measure is appropriate. **Mechanism:** `max-inline-size` with `margin-inline: auto`. For normal-flow, non-replaced block boxes with a non-auto width and both physical horizontal margins auto, CSS2.1 §10.3.3 makes the used margins equal to center the box; overconstraint and other formatting contexts have separate rules. `margin-inline` maps through writing mode, direction and text orientation. Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea. **Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers.",
    "rationale": "Composed action for C21; scoped configurable measure",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C21.01": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content.",
      "C21.02": "Use the measure axiom here only when a prose or task-specific measure is appropriate.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers."
    },
    "unit_subjects": {
      "C21.01": "**Responsibility:** constraining content to a maximum width and centring\nit horizontally.",
      "C21.02": "The measure axiom is typically enforced here.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` (maximum width, typically `60ch` for\nprose, wider for layout containers)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C21.01": {
        "start": 0,
        "end": 113
      },
      "C21.02": {
        "start": 114,
        "end": 199
      },
      "C21.03": {
        "start": 200,
        "end": 260
      },
      "C21.04": {
        "start": 572,
        "end": 652
      },
      "C21.05": {
        "start": 653,
        "end": 783
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "112801301b3dabd7a9e5f4a3f2e347a3a8425b965a4d35fcb16aae7f91b66230"
  },
  {
    "action_id": "A-C22",
    "claim_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
    ],
    "result_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
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
    "replacement": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require. Begin without a breakpoint where intrinsic wrapping preserves the task. **Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs. The threshold can be informed by content and container space; it is not automatically correct for every task. **Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes.",
    "rationale": "Composed action for C22; intrinsic Switcher threshold",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C22.01": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require.",
      "C22.02": "Begin without a breakpoint where intrinsic wrapping preserves the task.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs.",
      "C22.04": "The threshold can be informed by content and container space; it is not automatically correct for every task.",
      "C22.05": "**Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes."
    },
    "unit_subjects": {
      "C22.01": "**Responsibility:** switching between a multi-column and a single-column\nlayout based on available space.",
      "C22.02": "No breakpoints.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that\ncauses items to wrap at the threshold width.",
      "C22.04": "The threshold is defined by\nthe content, not the viewport.",
      "C22.05": "**Key parameter:** `--threshold` (the container width at which items\nstack)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C22.01": {
        "start": 0,
        "end": 123
      },
      "C22.02": {
        "start": 124,
        "end": 195
      },
      "C22.03": {
        "start": 196,
        "end": 368
      },
      "C22.04": {
        "start": 369,
        "end": 478
      },
      "C22.05": {
        "start": 479,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "bfe50f44830c6ff0658c2d3703a4c8d8f1ad1001a49597fd8de6ad18f0f58d07"
  },
  {
    "action_id": "A-C23",
    "claim_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
    ],
    "result_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
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
    "replacement": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method. They are the system’s “atoms,” a metaphor for reusable building blocks. Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them.",
    "rationale": "Composed action for C23; complete-vocabulary guarantee and composition model",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C23.01": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method.",
      "C23.02": "They are the system’s “atoms,” a metaphor for reusable building blocks.",
      "C23.03": "Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them."
    },
    "unit_subjects": {
      "C23.01": "Together, these thirteen primitives can compose any layout.",
      "C23.02": "They are the\n*atoms* of the system.",
      "C23.03": "Everything else --- cards, headers, navigation,\nforms, footers --- is a *molecule* composed from these atoms."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C23.01": {
        "start": 0,
        "end": 99
      },
      "C23.02": {
        "start": 100,
        "end": 171
      },
      "C23.03": {
        "start": 172,
        "end": 330
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "69a02e2590e7443d06cf9f7211c460f6294478d324ad953e3d2c0a74370fae35"
  },
  {
    "action_id": "A-C24",
    "claim_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "result_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      970,
      975
    ],
    "literal_offset_0based": [
      0,
      408
    ],
    "file_byte_offsets": [
      46170,
      46582
    ],
    "original": "Start at utopia.fyi and generate a type scale and space scale. Paste the\ncustom properties into your stylesheet. Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs. Set `max-inline-size: 60ch` on all text elements. Use\n`gap` with Utopia space tokens for all spacing. Write zero media\nqueries. You will be astonished at how far this gets you.",
    "disposition": "correct",
    "replacement": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them. Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet. Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported. Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role. Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions. Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode. Treat the result as a useful starting point and verify it against the actual content and contexts.",
    "rationale": "Composed action for C24; broad implementation prescription",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C24.01": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them.",
      "C24.02": "Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet.",
      "C24.03": "Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported.",
      "C24.04": "Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role.",
      "C24.05": "Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions.",
      "C24.06": "Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode.",
      "C24.07": "Treat the result as a useful starting point and verify it against the actual content and contexts."
    },
    "unit_subjects": {
      "C24.01": "Start at utopia.fyi and generate a type scale and space scale.",
      "C24.02": "Paste the\ncustom properties into your stylesheet.",
      "C24.03": "Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs.",
      "C24.04": "Set `max-inline-size: 60ch` on all text elements.",
      "C24.05": "Use\n`gap` with Utopia space tokens for all spacing.",
      "C24.06": "Write zero media\nqueries.",
      "C24.07": "You will be astonished at how far this gets you."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C24.01": {
        "start": 0,
        "end": 124
      },
      "C24.02": {
        "start": 125,
        "end": 265
      },
      "C24.03": {
        "start": 266,
        "end": 447
      },
      "C24.04": {
        "start": 448,
        "end": 569
      },
      "C24.05": {
        "start": 570,
        "end": 672
      },
      "C24.06": {
        "start": 673,
        "end": 837
      },
      "C24.07": {
        "start": 838,
        "end": 936
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "deda2f7a893b5db57b0491033811d64bafba7c7ecb61fbbd5542a3bc2064f337"
  },
  {
    "action_id": "A-C25",
    "claim_ids": [
      "C25.01",
      "C25.02"
    ],
    "result_ids": [
      "C25.01",
      "C25.02"
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
    "replacement": "Shift responsive decisions toward component space when the component context matters. `ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself.",
    "rationale": "Composed action for C25; ch units eliminate magic-number thresholds",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C25.01": "Shift responsive decisions toward component space when the component context matters.",
      "C25.02": "`ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself."
    },
    "unit_subjects": {
      "C25.01": "Shift responsive design from viewport to component.",
      "C25.02": "Using `ch` units in\ncontainer queries eliminates magic-number breakpoints entirely."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C25.01": {
        "start": 0,
        "end": 85
      },
      "C25.02": {
        "start": 86,
        "end": 223
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "7fa24f8936d4bbaaeb35982e5181f72a9976ac885475ded58817098b14e976be"
  },
  {
    "action_id": "A-C26",
    "claim_ids": [
      "C26.01",
      "C26.02"
    ],
    "result_ids": [
      "C26.01",
      "C26.02"
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
    "replacement": "Components can adapt to the space they occupy when a suitable query container exists. Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior.",
    "rationale": "Composed action for C26; container-context adaptation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C26.01": "Components can adapt to the space they occupy when a suitable query container exists.",
      "C26.02": "Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior."
    },
    "unit_subjects": {
      "C26.01": "Components adapt based on the space they actually occupy, not the\nbrowser window size.",
      "C26.02": "Combined with container query units (`cqw`, `cqh`),\nsizing becomes relative to context."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C26.01": {
        "start": 0,
        "end": 85
      },
      "C26.02": {
        "start": 86,
        "end": 205
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c768692e0aa996055f5df885f042e5c6a163c0a13454b456b94633bf7c27e0ae"
  }
]
```json
[
  {
    "action_id": "A-C01",
    "claim_ids": [
      "C01.01",
      "C01.02"
    ],
    "result_ids": [
      "C01.01",
      "C01.02"
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
    "replacement": "Use the listed primitives as a reusable composition method. Permit justified additional CSS rules when content, semantics or interaction requires them.",
    "rationale": "Composed action for C01; local layout-composition policy",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C01.01": "Use the listed primitives as a reusable composition method.",
      "C01.02": "Permit justified additional CSS rules when content, semantics or interaction requires them."
    },
    "unit_subjects": {
      "C01.01": "Every layout is a composition of these.",
      "C01.02": "No bespoke CSS layouts — compose from primitives."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C01.01": {
        "start": 0,
        "end": 59
      },
      "C01.02": {
        "start": 60,
        "end": 151
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5f313ae4620fcaa9df9eb4dc34bde5abe006a664f1e73e4a0b2db68eba9f70cc"
  },
  {
    "action_id": "A-C27",
    "claim_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
    ],
    "result_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
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
    "disposition": "qualify",
    "replacement": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow). A page header = Cover containing a Center containing a Stack. A navigation = Cluster inside a Box. These examples illustrate reuse; they do not define a complete layout grammar.",
    "rationale": "Composed action for C27; primitive composition example",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "unit_subjects": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C27.01": {
        "start": 0,
        "end": 83
      },
      "C27.02": {
        "start": 84,
        "end": 145
      },
      "C27.03": {
        "start": 146,
        "end": 182
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a123d41cbac2dd8e30b65473c5adf1a06039512ebaeeea15d61b4cee9ba7f250"
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
    "replacement": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |",
    "rationale": "Composed action for C02; measure default and scope",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C02": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |"
    },
    "unit_subjects": {
      "C02": "| **Center** | Max-width + horizontal centering | `max-inline-size: 60ch; margin-inline: auto` | Prose, any width-constrained content |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C02": {
        "start": 0,
        "end": 218
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "433051521d4e0c1886e3439557a5166fc4f3ad481ab2d3ffd6ea37f933039482"
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
    "disposition": "qualify",
    "replacement": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |",
    "rationale": "Composed action for C03; intrinsic switcher",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C03": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |"
    },
    "unit_subjects": {
      "C03": "| **Switcher** | Multi-col → single-col based on space | `flex-wrap: wrap` with calculated `flex-basis` | Responsive columns without breakpoints |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C03": {
        "start": 0,
        "end": 255
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c76a45616f2d3bd9b7fb1b9d2b9b42abbaecae0999e37421bb01bcb7d95716a8"
  },
  {
    "action_id": "A-C04",
    "claim_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
    ],
    "result_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
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
    "replacement": "Start with intrinsic layout and fluid constraints. Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation. Treat query removal as a diagnostic, not a universal pass condition.",
    "rationale": "Composed action for C04; zero-query rule and universal claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C04.01": "Start with intrinsic layout and fluid constraints.",
      "C04.02": "Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation.",
      "C04.03": "Treat query removal as a diagnostic, not a universal pass condition."
    },
    "unit_subjects": {
      "C04.01": "No media queries for layout.",
      "C04.02": "Primitives + fluid tokens handle all responsiveness.",
      "C04.03": "The test: if you removed every media query, would the layout still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C04.01": {
        "start": 0,
        "end": 50
      },
      "C04.02": {
        "start": 51,
        "end": 175
      },
      "C04.03": {
        "start": 176,
        "end": 244
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "1a8f7b8a870a41c3eeacb327a08e83c7ee9476e805d98f80f5685f95eb796e40"
  },
  {
    "action_id": "A-C05",
    "claim_ids": [
      "C05.02"
    ],
    "result_ids": [
      "C05.02"
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
    "replacement": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice.",
    "rationale": "Composed action for C05; query-free review heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C05.02": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice."
    },
    "unit_subjects": {
      "C05.02": "**Breakpoint test**: Remove all media queries mentally — does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C05.02": {
        "start": 0,
        "end": 149
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a92dabe84e417ebb94b4388dd8be3006a23e7c60f75b4d62f634a57417ae6995"
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
    "replacement": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n",
    "rationale": "Composed action for C06; universal measure rule with structural exceptions",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C06": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n"
    },
    "unit_subjects": {
      "C06": "* { max-inline-size: 60ch; }\nhtml, body, div, header, nav, main, footer { max-inline-size: none; }"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C06": {
        "start": 0,
        "end": 211
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6f515dc61b0e33865c57e8db11e7b92a07052c09028071b42719e50e2c04e699"
  },
  {
    "action_id": "A-C07-C08",
    "claim_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "result_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      144,
      151
    ],
    "literal_offset_0based": [
      0,
      513
    ],
    "file_byte_offsets": [
      6541,
      7066
    ],
    "original": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance. You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*. The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*. They are your CSS doing\nexactly what you intended.",
    "disposition": "qualify",
    "replacement": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked. Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception. A 60ch measure can guide prose; choose controls, data and other content by role. Use project conventions consistently while stating their scope and exceptions.",
    "rationale": "Composed action for C07; exceptionless axiom and universal enforcement",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C07.01": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked.",
      "C07.02": "Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception.",
      "C08.01": "A 60ch measure can guide prose; choose controls, data and other content by role.",
      "C08.02": "Use project conventions consistently while stating their scope and exceptions."
    },
    "unit_subjects": {
      "C07.01": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance.",
      "C07.02": "You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*.",
      "C08.01": "The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*.",
      "C08.02": "They are your CSS doing\nexactly what you intended."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C07.01": {
        "start": 0,
        "end": 99
      },
      "C07.02": {
        "start": 100,
        "end": 211
      },
      "C08.01": {
        "start": 212,
        "end": 292
      },
      "C08.02": {
        "start": 293,
        "end": 371
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "4fed4d0b7f32457d064cad64d8713dec9dd44764a4abb1b675d1d32a50eb8081"
  },
  {
    "action_id": "A-C09-C10",
    "claim_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
    ],
    "result_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
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
    "replacement": "Use constraints as a default method, while naming cases where a fixed value serves a requirement. A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target. Use `min-` and `max-` sizing properties to set bounds suited to the content. Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict. Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings. Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review.",
    "rationale": "Composed action for C09, C10; fixed values, measure and target examples CSS technique preference",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C09.01": "Use constraints as a default method, while naming cases where a fixed value serves a requirement.",
      "C09.02": "A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task.",
      "C09.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target.",
      "C10.01": "Use `min-` and `max-` sizing properties to set bounds suited to the content.",
      "C10.02": "Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict.",
      "C10.03": "Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings.",
      "C10.04": "Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review."
    },
    "unit_subjects": {
      "C09.01": "The single most important principle.",
      "C09.02": "Every fixed value in your CSS is a\nplace where you have overridden the browser\\'s judgment with your own.",
      "C09.03": "Sometimes this is necessary --- a maximum measure of `60ch`, a minimum\ntouch-target of `44px` --- but the default posture should always be to\n*suggest* rather than prescribe.",
      "C10.01": "Use `min-`, `max-`, and `clamp()`\ninstead of fixed values.",
      "C10.02": "Use `auto` instead of `100%`.",
      "C10.03": "Use `flex-basis`\ninstead of `width`.",
      "C10.04": "Each of these is an invitation for the browser to\nmake a contextually appropriate decision."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C09.01": {
        "start": 0,
        "end": 97
      },
      "C09.02": {
        "start": 98,
        "end": 221
      },
      "C09.03": {
        "start": 222,
        "end": 531
      },
      "C10.01": {
        "start": 532,
        "end": 608
      },
      "C10.02": {
        "start": 609,
        "end": 804
      },
      "C10.03": {
        "start": 805,
        "end": 926
      },
      "C10.04": {
        "start": 927,
        "end": 1194
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "dc5d34cb586c0753218f9d0134a48caa232fdc92d2b233915488fd20babcf408"
  },
  {
    "action_id": "A-C11",
    "claim_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
    ],
    "result_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
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
    "replacement": "This is a design preference for using browser and user context, not a claim of laziness. Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result. Constraints can support robust outcomes but cannot make good results inevitable across all contexts.",
    "rationale": "Composed action for C11; browser context and inevitable outcome",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C11.01": "This is a design preference for using browser and user context, not a claim of laziness.",
      "C11.02": "Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result.",
      "C11.03": "Constraints can support robust outcomes but cannot make good results inevitable across all contexts."
    },
    "unit_subjects": {
      "C11.01": "This is not laziness.",
      "C11.02": "It is recognition that the browser knows things\nyou do not --- the user\\'s font size preferences, their zoom level,\ntheir screen dimensions, whether they are using a split-screen view,\nwhether they have a notch or a toolbar.",
      "C11.03": "Your CSS should provide\n*constraints within which good outcomes are inevitable*, not blueprints\nthat are correct in one context and broken in all others."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C11.01": {
        "start": 0,
        "end": 88
      },
      "C11.02": {
        "start": 89,
        "end": 201
      },
      "C11.03": {
        "start": 202,
        "end": 302
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "80fcfa794d0a4bdc31cc231033005712b123547d7733807dc87bee77e628c67f"
  },
  {
    "action_id": "A-C12",
    "claim_ids": [
      "C12.01",
      "C12.02"
    ],
    "result_ids": [
      "C12.01",
      "C12.02"
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
    "replacement": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case. If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision.",
    "rationale": "Composed action for C12; query-free usability test",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C12.01": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case.",
      "C12.02": "If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision."
    },
    "unit_subjects": {
      "C12.01": "**The test:** if you removed every media query from your stylesheet,\nwould the layout still be usable?",
      "C12.02": "If not, your constraints are not yet\nwell enough chosen."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C12.01": {
        "start": 0,
        "end": 99
      },
      "C12.02": {
        "start": 100,
        "end": 209
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f7014ddad136381d870b9460fdd55d75a263b795fa3091311811ba49657b10fa"
  },
  {
    "action_id": "A-C13",
    "claim_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
    ],
    "result_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
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
    "replacement": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee. Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts. Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow. Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing. Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions.",
    "rationale": "Composed action for C13; content-derived dimension principles",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C13.01": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee.",
      "C13.02": "Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts.",
      "C13.03": "Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow.",
      "C13.04": "Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing.",
      "C13.05": "Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions."
    },
    "unit_subjects": {
      "C13.01": "The web is a content-driven medium.",
      "C13.02": "The width of a paragraph should be\ndetermined by its measure (in `ch` units).",
      "C13.03": "The height of a section\nshould be determined by the amount of content it contains.",
      "C13.04": "The gap\nbetween elements should be determined by the typographic scale (in `rem`\nor Utopia space tokens).",
      "C13.05": "The number of columns in a grid should be\ndetermined by the minimum acceptable item width and the available space\n(via `auto-fit` and `minmax()`)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C13.01": {
        "start": 0,
        "end": 109
      },
      "C13.02": {
        "start": 110,
        "end": 216
      },
      "C13.03": {
        "start": 217,
        "end": 349
      },
      "C13.04": {
        "start": 350,
        "end": 456
      },
      "C13.05": {
        "start": 457,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "f85c9989149c642d3483eb36d18e8e47c08a42367c6f871a5ef28b191a684e4f"
  },
  {
    "action_id": "A-C14",
    "claim_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
    ],
    "result_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
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
    "replacement": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content. Content can change, so this is a reason to test the assumption, not a universal ban on heights. A pixel width encodes a fixed size; test it across viewport and user settings. A fixed width may still serve a defined task when its consequences are checked. A column count depends on available container space and track sizing. Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs.",
    "rationale": "Composed action for C14; fixed geometry assumptions and container-query claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C14.01": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content.",
      "C14.02": "Content can change, so this is a reason to test the assumption, not a universal ban on heights.",
      "C14.03": "A pixel width encodes a fixed size; test it across viewport and user settings.",
      "C14.04": "A fixed width may still serve a defined task when its consequences are checked.",
      "C14.05": "A column count depends on available container space and track sizing.",
      "C14.06": "Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs."
    },
    "unit_subjects": {
      "C14.01": "When you prescribe a height, you are declaring that you know how much\ncontent will be present.",
      "C14.02": "You almost certainly do not.",
      "C14.03": "When you prescribe\na width in pixels, you are declaring that you know the user\\'s viewport\nsize.",
      "C14.04": "You do not.",
      "C14.05": "When you prescribe a column count, you are declaring\nthat you know the container\\'s width.",
      "C14.06": "In a world of container queries\nand intrinsic design, you should not need to."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C14.01": {
        "start": 0,
        "end": 121
      },
      "C14.02": {
        "start": 122,
        "end": 217
      },
      "C14.03": {
        "start": 218,
        "end": 296
      },
      "C14.04": {
        "start": 297,
        "end": 376
      },
      "C14.05": {
        "start": 377,
        "end": 446
      },
      "C14.06": {
        "start": 447,
        "end": 567
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5b6a8b773598cd68090989852ac1728094b529af5fcdad1eee303098fc402931"
  },
  {
    "action_id": "A-C15",
    "claim_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
    ],
    "result_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
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
    "replacement": "Let content inform dimensions where appropriate. Let available context inform arrangement. Designers set useful derivation rules and may also choose explicit values for justified cases.",
    "rationale": "Composed action for C15; design rule of derivation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C15.01": "Let content inform dimensions where appropriate.",
      "C15.02": "Let available context inform arrangement.",
      "C15.03": "Designers set useful derivation rules and may also choose explicit values for justified cases."
    },
    "unit_subjects": {
      "C15.01": "Content determines dimensions.",
      "C15.02": "Context determines arrangement.",
      "C15.03": "The\ndesigner\\'s job is to set the *rules of derivation*, not the values\nthemselves."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C15.01": {
        "start": 0,
        "end": 48
      },
      "C15.02": {
        "start": 49,
        "end": 90
      },
      "C15.03": {
        "start": 91,
        "end": 185
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6663d668b39712700795900b835e06f64d9b1b0b051d2a81ca86930db2040f0d"
  },
  {
    "action_id": "A-C16",
    "claim_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
    ],
    "result_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
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
    "disposition": "qualify",
    "replacement": "**The test:** if content doubles, check whether the task and layout remain usable. If the viewport halves, check reflow, overflow and task operation. Check combined changes too; these are diagnostics, not proof across all content or users.",
    "rationale": "Composed action for C16; content and viewport stress heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C16.01": "**The test:** if content doubles, check whether the task and layout remain usable.",
      "C16.02": "If the viewport halves, check reflow, overflow and task operation.",
      "C16.03": "Check combined changes too; these are diagnostics, not proof across all content or users."
    },
    "unit_subjects": {
      "C16.01": "**The test:** if the content doubles in length, does the layout still\nwork?",
      "C16.02": "If the viewport halves in width, does it still work?",
      "C16.03": "If both\nhappen simultaneously, does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C16.01": {
        "start": 0,
        "end": 82
      },
      "C16.02": {
        "start": 83,
        "end": 149
      },
      "C16.03": {
        "start": 150,
        "end": 239
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6ca282f7e6038af05a9f62214fc33f249d040eb89650603b65db0204ec799f37"
  },
  {
    "action_id": "A-C17",
    "claim_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
    ],
    "result_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
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
    "replacement": "An axiom can be a project-wide default, but “without exception” overstates its proper scope. Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target. Use Utopia spacing tokens as a local convention where they suit the composition. Implement shared defaults centrally, with documented exceptions and component-specific overrides.",
    "rationale": "Composed correction preserves all three examples while separating measure, target-size standards, spacing convention and universal-enforcement scope.",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C17.01": "An axiom can be a project-wide default, but “without exception” overstates its proper scope.",
      "C17.02": "Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content.",
      "C17.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target.",
      "C17.04": "Use Utopia spacing tokens as a local convention where they suit the composition.",
      "C17.05": "Implement shared defaults centrally, with documented exceptions and component-specific overrides."
    },
    "unit_subjects": {
      "C17.01": "An axiom is a design rule that pervades the entire system without\nexception.",
      "C17.02": "\\\"The measure shall not exceed 60ch.\\\"",
      "C17.03": "\\\"The minimum touch\ntarget shall be 44px.\\\"",
      "C17.04": "\\\"Spacing between sibling elements shall use\nUtopia space tokens.\\\"",
      "C17.05": "These are not guidelines to remember; they are\n*CSS declarations* that are written once and enforced everywhere."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C17.01": {
        "start": 0,
        "end": 92
      },
      "C17.02": {
        "start": 93,
        "end": 190
      },
      "C17.03": {
        "start": 191,
        "end": 499
      },
      "C17.04": {
        "start": 500,
        "end": 580
      },
      "C17.05": {
        "start": 581,
        "end": 678
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "a0fad6ec591e09c01397b01e54cecd856c42210c8b46a41b40421434f69f5b5d"
  },
  {
    "action_id": "A-C18",
    "claim_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
    ],
    "result_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
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
    "replacement": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page. A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations. A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts. Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations.",
    "rationale": "Composed action for C18; attribution, correctness and verification guarantee",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C18.01": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page.",
      "C18.02": "A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations.",
      "C18.03": "A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts.",
      "C18.04": "Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations."
    },
    "unit_subjects": {
      "C18.01": "The crucial insight from Every Layout\\'s Axioms chapter is that\ndesigning by axiom means designing *without seeing*.",
      "C18.02": "You cannot predict\nevery visual consequence of a well-chosen axiom, and *you do not need\nto*.",
      "C18.03": "The axiom generates correct outcomes in contexts you never\nanticipated, because it encodes a *principle* rather than a *specific\narrangement*.",
      "C18.04": "This is what makes axiom-based design scale: it does not\nrequire a designer to manually verify every combination of content and\ncontext."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C18.01": {
        "start": 0,
        "end": 114
      },
      "C18.02": {
        "start": 115,
        "end": 222
      },
      "C18.03": {
        "start": 223,
        "end": 318
      },
      "C18.04": {
        "start": 319,
        "end": 421
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "6b3e9c4f01fb049705c9594a3e6252f4bf77c6521fb1f0b0c8315156a6997ab8"
  },
  {
    "action_id": "A-C19",
    "claim_ids": [
      "C19.01",
      "C19.02"
    ],
    "result_ids": [
      "C19.01",
      "C19.02"
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
    "replacement": "Use a broad selector only with an explicit, bounded and tested exception set. Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions.",
    "rationale": "Composed action for C19; exception-based CSS approach",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C19.01": "Use a broad selector only with an explicit, bounded and tested exception set.",
      "C19.02": "Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions."
    },
    "unit_subjects": {
      "C19.01": "Axioms are best implemented using exception-based CSS: apply the rule to\neverything (`*`), then remove it from the specific elements that are\nlogical exceptions (containers, wrappers, structural elements).",
      "C19.02": "This\ninverted approach means you only need to *remember the exceptions*, not\nenumerate every element that should follow the rule."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C19.01": {
        "start": 0,
        "end": 77
      },
      "C19.02": {
        "start": 78,
        "end": 186
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "5c85ed1a758f10d03851626634fdd038f232b4c7860ce36772a03862c4191505"
  },
  {
    "action_id": "A-C20",
    "claim_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
    ],
    "result_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
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
    "replacement": "**The test:** try stating each design rule in one sentence. Ask whether one declaration can express it in the intended context. A single declaration may encode a useful project axiom, subject to its scope and exceptions. A multi-part rule may be a convention or composition; complexity alone does not make it false.",
    "rationale": "Composed action for C20; axiom classification heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C20.01": "**The test:** try stating each design rule in one sentence.",
      "C20.02": "Ask whether one declaration can express it in the intended context.",
      "C20.03": "A single declaration may encode a useful project axiom, subject to its scope and exceptions.",
      "C20.04": "A multi-part rule may be a convention or composition; complexity alone does not make it false."
    },
    "unit_subjects": {
      "C20.01": "**The test:** can you state each design rule in a single sentence?",
      "C20.02": "Can\nthat sentence be translated into a single CSS declaration?",
      "C20.03": "If so, it is\nan axiom.",
      "C20.04": "If not, it may be a convention masquerading as a principle."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C20.01": {
        "start": 0,
        "end": 59
      },
      "C20.02": {
        "start": 60,
        "end": 127
      },
      "C20.03": {
        "start": 128,
        "end": 220
      },
      "C20.04": {
        "start": 221,
        "end": 315
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "b976a5e3a00cf2539c8f770649d989613b9e5287cc536503ce013e17f6dcd642"
  },
  {
    "action_id": "A-C21",
    "claim_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
    ],
    "result_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
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
    "disposition": "qualify",
    "replacement": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content. Use the measure axiom here only when a prose or task-specific measure is appropriate. **Mechanism:** `max-inline-size` with `margin-inline: auto`. For normal-flow, non-replaced block boxes with a non-auto width and both physical horizontal margins auto, CSS2.1 §10.3.3 makes the used margins equal to center the box; overconstraint and other formatting contexts have separate rules. `margin-inline` maps through writing mode, direction and text orientation. Uses `box-sizing: content-box` so padding does not reduce the content area; keep this as a context-specific box-sizing choice. **Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers.",
    "rationale": "Composed action for C21; scoped configurable measure",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C21.01": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content.",
      "C21.02": "Use the measure axiom here only when a prose or task-specific measure is appropriate.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers."
    },
    "unit_subjects": {
      "C21.01": "**Responsibility:** constraining content to a maximum width and centring\nit horizontally.",
      "C21.02": "The measure axiom is typically enforced here.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` (maximum width, typically `60ch` for\nprose, wider for layout containers)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C21.01": {
        "start": 0,
        "end": 113
      },
      "C21.02": {
        "start": 114,
        "end": 199
      },
      "C21.03": {
        "start": 200,
        "end": 260
      },
      "C21.04": {
        "start": -1,
        "end": 79
      },
      "C21.05": {
        "start": 699,
        "end": 829
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "35f8994d73187e5ad89d4d7e994f3282420a13100ba68409000f3297277a3471"
  },
  {
    "action_id": "A-C22",
    "claim_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
    ],
    "result_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
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
    "replacement": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require. Begin without a breakpoint where intrinsic wrapping preserves the task. **Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs. The threshold can be informed by content and container space; it is not automatically correct for every task. **Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes.",
    "rationale": "Composed action for C22; intrinsic Switcher threshold",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C22.01": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require.",
      "C22.02": "Begin without a breakpoint where intrinsic wrapping preserves the task.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs.",
      "C22.04": "The threshold can be informed by content and container space; it is not automatically correct for every task.",
      "C22.05": "**Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes."
    },
    "unit_subjects": {
      "C22.01": "**Responsibility:** switching between a multi-column and a single-column\nlayout based on available space.",
      "C22.02": "No breakpoints.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that\ncauses items to wrap at the threshold width.",
      "C22.04": "The threshold is defined by\nthe content, not the viewport.",
      "C22.05": "**Key parameter:** `--threshold` (the container width at which items\nstack)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C22.01": {
        "start": 0,
        "end": 123
      },
      "C22.02": {
        "start": 124,
        "end": 195
      },
      "C22.03": {
        "start": 196,
        "end": 368
      },
      "C22.04": {
        "start": 369,
        "end": 478
      },
      "C22.05": {
        "start": 479,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "bfe50f44830c6ff0658c2d3703a4c8d8f1ad1001a49597fd8de6ad18f0f58d07"
  },
  {
    "action_id": "A-C23",
    "claim_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
    ],
    "result_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
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
    "replacement": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method. They are the system’s “atoms,” a metaphor for reusable building blocks. Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them.",
    "rationale": "Composed action for C23; complete-vocabulary guarantee and composition model",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C23.01": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method.",
      "C23.02": "They are the system’s “atoms,” a metaphor for reusable building blocks.",
      "C23.03": "Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them."
    },
    "unit_subjects": {
      "C23.01": "Together, these thirteen primitives can compose any layout.",
      "C23.02": "They are the\n*atoms* of the system.",
      "C23.03": "Everything else --- cards, headers, navigation,\nforms, footers --- is a *molecule* composed from these atoms."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C23.01": {
        "start": 0,
        "end": 99
      },
      "C23.02": {
        "start": 100,
        "end": 171
      },
      "C23.03": {
        "start": 172,
        "end": 330
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "69a02e2590e7443d06cf9f7211c460f6294478d324ad953e3d2c0a74370fae35"
  },
  {
    "action_id": "A-C24",
    "claim_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "result_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      970,
      975
    ],
    "literal_offset_0based": [
      0,
      408
    ],
    "file_byte_offsets": [
      46170,
      46582
    ],
    "original": "Start at utopia.fyi and generate a type scale and space scale. Paste the\ncustom properties into your stylesheet. Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs. Set `max-inline-size: 60ch` on all text elements. Use\n`gap` with Utopia space tokens for all spacing. Write zero media\nqueries. You will be astonished at how far this gets you.",
    "disposition": "correct",
    "replacement": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them. Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet. Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported. Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role. Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions. Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode. Treat the result as a useful starting point and verify it against the actual content and contexts.",
    "rationale": "Composed action for C24; broad implementation prescription",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C24.01": "Start at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them.",
      "C24.02": "Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet.",
      "C24.03": "Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported.",
      "C24.04": "Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role.",
      "C24.05": "Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions.",
      "C24.06": "Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode.",
      "C24.07": "Treat the result as a useful starting point and verify it against the actual content and contexts."
    },
    "unit_subjects": {
      "C24.01": "Start at utopia.fyi and generate a type scale and space scale.",
      "C24.02": "Paste the\ncustom properties into your stylesheet.",
      "C24.03": "Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs.",
      "C24.04": "Set `max-inline-size: 60ch` on all text elements.",
      "C24.05": "Use\n`gap` with Utopia space tokens for all spacing.",
      "C24.06": "Write zero media\nqueries.",
      "C24.07": "You will be astonished at how far this gets you."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C24.01": {
        "start": 0,
        "end": 124
      },
      "C24.02": {
        "start": 125,
        "end": 265
      },
      "C24.03": {
        "start": 266,
        "end": 447
      },
      "C24.04": {
        "start": 448,
        "end": 569
      },
      "C24.05": {
        "start": 570,
        "end": 672
      },
      "C24.06": {
        "start": 673,
        "end": 837
      },
      "C24.07": {
        "start": 838,
        "end": 936
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "deda2f7a893b5db57b0491033811d64bafba7c7ecb61fbbd5542a3bc2064f337"
  },
  {
    "action_id": "A-C25",
    "claim_ids": [
      "C25.01",
      "C25.02"
    ],
    "result_ids": [
      "C25.01",
      "C25.02"
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
    "replacement": "Shift responsive decisions toward component space when the component context matters. `ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself.",
    "rationale": "Composed action for C25; ch units eliminate magic-number thresholds",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C25.01": "Shift responsive decisions toward component space when the component context matters.",
      "C25.02": "`ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself."
    },
    "unit_subjects": {
      "C25.01": "Shift responsive design from viewport to component.",
      "C25.02": "Using `ch` units in\ncontainer queries eliminates magic-number breakpoints entirely."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C25.01": {
        "start": 0,
        "end": 85
      },
      "C25.02": {
        "start": 86,
        "end": 223
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "7fa24f8936d4bbaaeb35982e5181f72a9976ac885475ded58817098b14e976be"
  },
  {
    "action_id": "A-C26",
    "claim_ids": [
      "C26.01",
      "C26.02"
    ],
    "result_ids": [
      "C26.01",
      "C26.02"
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
    "replacement": "Components can adapt to the space they occupy when a suitable query container exists. Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior.",
    "rationale": "Composed action for C26; container-context adaptation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C26.01": "Components can adapt to the space they occupy when a suitable query container exists.",
      "C26.02": "Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior."
    },
    "unit_subjects": {
      "C26.01": "Components adapt based on the space they actually occupy, not the\nbrowser window size.",
      "C26.02": "Combined with container query units (`cqw`, `cqh`),\nsizing becomes relative to context."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C26.01": {
        "start": 0,
        "end": 85
      },
      "C26.02": {
        "start": 86,
        "end": 205
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim.",
    "replacement_sha256": "c768692e0aa996055f5df885f042e5c6a163c0a13454b456b94633bf7c27e0ae"
  }
]
```json
[
  {
    "action_id": "A-C01",
    "claim_ids": [
      "C01.01",
      "C01.02"
    ],
    "result_ids": [
      "C01.01",
      "C01.02"
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
    "replacement": "Use the listed primitives as a reusable composition method. Permit justified additional CSS rules when content, semantics or interaction requires them.",
    "rationale": "Composed action for C01; local layout-composition policy",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C01.01": "Use the listed primitives as a reusable composition method.",
      "C01.02": "Permit justified additional CSS rules when content, semantics or interaction requires them."
    },
    "unit_subjects": {
      "C01.01": "Every layout is a composition of these.",
      "C01.02": "No bespoke CSS layouts — compose from primitives."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C01.01": {
        "start": 0,
        "end": 59
      },
      "C01.02": {
        "start": 60,
        "end": 151
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C27",
    "claim_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
    ],
    "result_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
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
    "disposition": "qualify",
    "replacement": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow). A page header = Cover containing a Center containing a Stack. A navigation = Cluster inside a Box. These examples illustrate reuse; they do not define a complete layout grammar.",
    "rationale": "Composed action for C27; primitive composition example",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "unit_subjects": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C27.01": {
        "start": 0,
        "end": 83
      },
      "C27.02": {
        "start": 84,
        "end": 145
      },
      "C27.03": {
        "start": 146,
        "end": 182
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
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
    "replacement": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |",
    "rationale": "Composed action for C02; measure default and scope",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C02": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |"
    },
    "unit_subjects": {
      "C02": "| **Center** | Max-width + horizontal centering | `max-inline-size: 60ch; margin-inline: auto` | Prose, any width-constrained content |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C02": {
        "start": 0,
        "end": 218
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
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
    "disposition": "qualify",
    "replacement": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |",
    "rationale": "Composed action for C03; intrinsic switcher",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C03": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and use a justified discrete mode when it fails |"
    },
    "unit_subjects": {
      "C03": "| **Switcher** | Multi-col → single-col based on space | `flex-wrap: wrap` with calculated `flex-basis` | Responsive columns without breakpoints |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C03": {
        "start": 0,
        "end": 255
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C04",
    "claim_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
    ],
    "result_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
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
    "replacement": "Start with intrinsic layout and fluid constraints. Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation. Treat query removal as a diagnostic, not a universal pass condition.",
    "rationale": "Composed action for C04; zero-query rule and universal claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C04.01": "Start with intrinsic layout and fluid constraints.",
      "C04.02": "Use a justified media or container query when content, interaction, user need or output medium requires discrete adaptation.",
      "C04.03": "Treat query removal as a diagnostic, not a universal pass condition."
    },
    "unit_subjects": {
      "C04.01": "No media queries for layout.",
      "C04.02": "Primitives + fluid tokens handle all responsiveness.",
      "C04.03": "The test: if you removed every media query, would the layout still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C04.01": {
        "start": 0,
        "end": 50
      },
      "C04.02": {
        "start": 51,
        "end": 175
      },
      "C04.03": {
        "start": 176,
        "end": 244
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C05",
    "claim_ids": [
      "C05.02"
    ],
    "result_ids": [
      "C05.02"
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
    "replacement": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice.",
    "rationale": "Composed action for C05; query-free review heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C05.02": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task or context need for adaptation and verify the choice."
    },
    "unit_subjects": {
      "C05.02": "**Breakpoint test**: Remove all media queries mentally — does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C05.02": {
        "start": 0,
        "end": 149
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
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
    "replacement": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n",
    "rationale": "Composed action for C06; universal measure rule with structural exceptions",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C06": "/* Scope the default measure to prose; size controls and wide content by role. */\n.prose {\n  max-inline-size: var(--measure, 60ch);\n  margin-inline: auto;\n}\n.controls, .wide-content {\n  max-inline-size: 100%;\n}\n"
    },
    "unit_subjects": {
      "C06": "* { max-inline-size: 60ch; }\nhtml, body, div, header, nav, main, footer { max-inline-size: none; }"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C06": {
        "start": 0,
        "end": 211
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C07-C08",
    "claim_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "result_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      144,
      151
    ],
    "literal_offset_0based": [
      0,
      513
    ],
    "file_byte_offsets": [
      6541,
      7066
    ],
    "original": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance. You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*. The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*. They are your CSS doing\nexactly what you intended.",
    "disposition": "qualify",
    "replacement": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked. Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception. A 60ch measure can guide prose; choose controls, data and other content by role. Use project conventions consistently while stating their scope and exceptions.",
    "rationale": "Composed action for C07; exceptionless axiom and universal enforcement",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C07.01": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked.",
      "C07.02": "Treat an axiom as a reusable default constraint, not a rule that must apply to every element without exception.",
      "C08.01": "A 60ch measure can guide prose; choose controls, data and other content by role.",
      "C08.02": "Use project conventions consistently while stating their scope and exceptions."
    },
    "unit_subjects": {
      "C07.01": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance.",
      "C07.02": "You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*.",
      "C08.01": "The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*.",
      "C08.02": "They are your CSS doing\nexactly what you intended."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C07.01": {
        "start": 0,
        "end": 99
      },
      "C07.02": {
        "start": 100,
        "end": 211
      },
      "C08.01": {
        "start": 212,
        "end": 292
      },
      "C08.02": {
        "start": 293,
        "end": 371
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C09-C10",
    "claim_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
    ],
    "result_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
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
    "replacement": "Use constraints as a default method, while naming cases where a fixed value serves a requirement. A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target. Use `min-` and `max-` sizing properties to set bounds suited to the content. Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict. Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings. Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review.",
    "rationale": "Composed action for C09, C10; fixed values, measure and target examples CSS technique preference",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C09.01": "Use constraints as a default method, while naming cases where a fixed value serves a requirement.",
      "C09.02": "A fixed CSS value is an author choice; assess its context and user effects rather than assuming the browser knows the task.",
      "C09.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may choose 44px as its own stronger target.",
      "C10.01": "Use `min-` and `max-` sizing properties to set bounds suited to the content.",
      "C10.02": "Use `clamp()` when its minimum, preferred and maximum calculations express the intended range; CSS Values §10.2 defines its comparison behavior, including minimum preference when bounds conflict.",
      "C10.03": "Use `auto` where the property’s layout algorithm makes it appropriate; `auto` and `100%` have property-specific meanings.",
      "C10.04": "Choose `flex-basis` for a flex item’s initial main-size input when that behavior is intended; it is not a general replacement for `width`. These mechanisms contribute values to layout algorithms; they do not guarantee a contextually appropriate result without review."
    },
    "unit_subjects": {
      "C09.01": "The single most important principle.",
      "C09.02": "Every fixed value in your CSS is a\nplace where you have overridden the browser\\'s judgment with your own.",
      "C09.03": "Sometimes this is necessary --- a maximum measure of `60ch`, a minimum\ntouch-target of `44px` --- but the default posture should always be to\n*suggest* rather than prescribe.",
      "C10.01": "Use `min-`, `max-`, and `clamp()`\ninstead of fixed values.",
      "C10.02": "Use `auto` instead of `100%`.",
      "C10.03": "Use `flex-basis`\ninstead of `width`.",
      "C10.04": "Each of these is an invitation for the browser to\nmake a contextually appropriate decision."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C09.01": {
        "start": 0,
        "end": 97
      },
      "C09.02": {
        "start": 98,
        "end": 221
      },
      "C09.03": {
        "start": 222,
        "end": 531
      },
      "C10.01": {
        "start": 532,
        "end": 608
      },
      "C10.02": {
        "start": 609,
        "end": 804
      },
      "C10.03": {
        "start": 805,
        "end": 926
      },
      "C10.04": {
        "start": 927,
        "end": 1194
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C11",
    "claim_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
    ],
    "result_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
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
    "replacement": "This is a design preference for using browser and user context, not a claim of laziness. Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result. Constraints can support robust outcomes but cannot make good results inevitable across all contexts.",
    "rationale": "Composed action for C11; browser context and inevitable outcome",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C11.01": "This is a design preference for using browser and user context, not a claim of laziness.",
      "C11.02": "Account for user font preferences, zoom, available dimensions and other relevant inputs, then verify the result.",
      "C11.03": "Constraints can support robust outcomes but cannot make good results inevitable across all contexts."
    },
    "unit_subjects": {
      "C11.01": "This is not laziness.",
      "C11.02": "It is recognition that the browser knows things\nyou do not --- the user\\'s font size preferences, their zoom level,\ntheir screen dimensions, whether they are using a split-screen view,\nwhether they have a notch or a toolbar.",
      "C11.03": "Your CSS should provide\n*constraints within which good outcomes are inevitable*, not blueprints\nthat are correct in one context and broken in all others."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C11.01": {
        "start": 0,
        "end": 88
      },
      "C11.02": {
        "start": 89,
        "end": 201
      },
      "C11.03": {
        "start": 202,
        "end": 302
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C12",
    "claim_ids": [
      "C12.01",
      "C12.02"
    ],
    "result_ids": [
      "C12.01",
      "C12.02"
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
    "replacement": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case. If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision.",
    "rationale": "Composed action for C12; query-free usability test",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C12.01": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case.",
      "C12.02": "If the result is unusable, identify whether the content, constraints or a discrete adaptation needs revision."
    },
    "unit_subjects": {
      "C12.01": "**The test:** if you removed every media query from your stylesheet,\nwould the layout still be usable?",
      "C12.02": "If not, your constraints are not yet\nwell enough chosen."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C12.01": {
        "start": 0,
        "end": 99
      },
      "C12.02": {
        "start": 100,
        "end": 209
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C13",
    "claim_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
    ],
    "result_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
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
    "replacement": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee. Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts. Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow. Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing. Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions.",
    "rationale": "Composed action for C13; content-derived dimension principles",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C13.01": "Treat the web as content-driven when selecting layout methods; this is a design framing, not a CSS guarantee.",
      "C13.02": "Choose a paragraph measure in `ch` when it suits the prose, and verify it with the used fonts and scripts.",
      "C13.03": "Let section block-size follow content where the task permits; use justified minimum or fixed bounds where needed and check overflow.",
      "C13.04": "Use a typographic or spacing scale as a project convention for gaps, while allowing task-specific spacing.",
      "C13.05": "Choose a grid item minimum for the content and task; `auto-fit` with `minmax()` can repeat tracks only under Grid’s sizing conditions."
    },
    "unit_subjects": {
      "C13.01": "The web is a content-driven medium.",
      "C13.02": "The width of a paragraph should be\ndetermined by its measure (in `ch` units).",
      "C13.03": "The height of a section\nshould be determined by the amount of content it contains.",
      "C13.04": "The gap\nbetween elements should be determined by the typographic scale (in `rem`\nor Utopia space tokens).",
      "C13.05": "The number of columns in a grid should be\ndetermined by the minimum acceptable item width and the available space\n(via `auto-fit` and `minmax()`)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C13.01": {
        "start": 0,
        "end": 109
      },
      "C13.02": {
        "start": 110,
        "end": 216
      },
      "C13.03": {
        "start": 217,
        "end": 349
      },
      "C13.04": {
        "start": 350,
        "end": 456
      },
      "C13.05": {
        "start": 457,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C14",
    "claim_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
    ],
    "result_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
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
    "replacement": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content. Content can change, so this is a reason to test the assumption, not a universal ban on heights. A pixel width encodes a fixed size; test it across viewport and user settings. A fixed width may still serve a defined task when its consequences are checked. A column count depends on available container space and track sizing. Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs.",
    "rationale": "Composed action for C14; fixed geometry assumptions and container-query claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C14.01": "A prescribed height assumes a content amount; use content-driven height where the task permits and test expanded content.",
      "C14.02": "Content can change, so this is a reason to test the assumption, not a universal ban on heights.",
      "C14.03": "A pixel width encodes a fixed size; test it across viewport and user settings.",
      "C14.04": "A fixed width may still serve a defined task when its consequences are checked.",
      "C14.05": "A column count depends on available container space and track sizing.",
      "C14.06": "Intrinsic layout and container queries offer alternatives, but fixed column counts may still be justified by task needs."
    },
    "unit_subjects": {
      "C14.01": "When you prescribe a height, you are declaring that you know how much\ncontent will be present.",
      "C14.02": "You almost certainly do not.",
      "C14.03": "When you prescribe\na width in pixels, you are declaring that you know the user\\'s viewport\nsize.",
      "C14.04": "You do not.",
      "C14.05": "When you prescribe a column count, you are declaring\nthat you know the container\\'s width.",
      "C14.06": "In a world of container queries\nand intrinsic design, you should not need to."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C14.01": {
        "start": 0,
        "end": 121
      },
      "C14.02": {
        "start": 122,
        "end": 217
      },
      "C14.03": {
        "start": 218,
        "end": 296
      },
      "C14.04": {
        "start": 297,
        "end": 376
      },
      "C14.05": {
        "start": 377,
        "end": 446
      },
      "C14.06": {
        "start": 447,
        "end": 567
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C15",
    "claim_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
    ],
    "result_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
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
    "replacement": "Let content inform dimensions where appropriate. Let available context inform arrangement. Designers set useful derivation rules and may also choose explicit values for justified cases.",
    "rationale": "Composed action for C15; design rule of derivation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C15.01": "Let content inform dimensions where appropriate.",
      "C15.02": "Let available context inform arrangement.",
      "C15.03": "Designers set useful derivation rules and may also choose explicit values for justified cases."
    },
    "unit_subjects": {
      "C15.01": "Content determines dimensions.",
      "C15.02": "Context determines arrangement.",
      "C15.03": "The\ndesigner\\'s job is to set the *rules of derivation*, not the values\nthemselves."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C15.01": {
        "start": 0,
        "end": 48
      },
      "C15.02": {
        "start": 49,
        "end": 90
      },
      "C15.03": {
        "start": 91,
        "end": 185
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C16",
    "claim_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
    ],
    "result_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
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
    "disposition": "qualify",
    "replacement": "**The test:** if content doubles, check whether the task and layout remain usable. If the viewport halves, check reflow, overflow and task operation. Check combined changes too; these are diagnostics, not proof across all content or users.",
    "rationale": "Composed action for C16; content and viewport stress heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C16.01": "**The test:** if content doubles, check whether the task and layout remain usable.",
      "C16.02": "If the viewport halves, check reflow, overflow and task operation.",
      "C16.03": "Check combined changes too; these are diagnostics, not proof across all content or users."
    },
    "unit_subjects": {
      "C16.01": "**The test:** if the content doubles in length, does the layout still\nwork?",
      "C16.02": "If the viewport halves in width, does it still work?",
      "C16.03": "If both\nhappen simultaneously, does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C16.01": {
        "start": 0,
        "end": 82
      },
      "C16.02": {
        "start": 83,
        "end": 149
      },
      "C16.03": {
        "start": 150,
        "end": 239
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C17",
    "claim_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
    ],
    "result_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
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
    "replacement": "An axiom can be a project-wide default, but “without exception” overstates its proper scope. Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content. For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target. Use Utopia spacing tokens as a local convention where they suit the composition. Implement shared defaults centrally, with documented exceptions and component-specific overrides.",
    "rationale": "Composed correction preserves all three examples while separating measure, target-size standards, spacing convention and universal-enforcement scope.",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C17.01": "An axiom can be a project-wide default, but “without exception” overstates its proper scope.",
      "C17.02": "Treat “60ch” as a configurable prose-measure preference, not a universal maximum for all content.",
      "C17.03": "For pointer targets, distinguish WCAG 2.2 SC 2.5.8 AA (24 by 24 CSS px with spacing, equivalent, inline, user-agent-control and essential exceptions) from SC 2.5.5 AAA (44 by 44 CSS px with equivalent, inline, user-agent-control and essential exceptions); a project may adopt 44px as a stronger local target.",
      "C17.04": "Use Utopia spacing tokens as a local convention where they suit the composition.",
      "C17.05": "Implement shared defaults centrally, with documented exceptions and component-specific overrides."
    },
    "unit_subjects": {
      "C17.01": "An axiom is a design rule that pervades the entire system without\nexception.",
      "C17.02": "\\\"The measure shall not exceed 60ch.\\\"",
      "C17.03": "\\\"The minimum touch\ntarget shall be 44px.\\\"",
      "C17.04": "\\\"Spacing between sibling elements shall use\nUtopia space tokens.\\\"",
      "C17.05": "These are not guidelines to remember; they are\n*CSS declarations* that are written once and enforced everywhere."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C17.01": {
        "start": 0,
        "end": 92
      },
      "C17.02": {
        "start": 93,
        "end": 190
      },
      "C17.03": {
        "start": 191,
        "end": 499
      },
      "C17.04": {
        "start": 500,
        "end": 580
      },
      "C17.05": {
        "start": 581,
        "end": 678
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C18",
    "claim_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
    ],
    "result_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
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
    "replacement": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page. A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations. A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts. Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations.",
    "rationale": "Composed action for C18; attribution, correctness and verification guarantee",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C18.01": "The current Every Layout Axioms page presents axiom-based design as a method; this attribution is about that page.",
      "C18.02": "A well-chosen axiom does not make every visual consequence predictable; inspect consequential combinations.",
      "C18.03": "A principle can generalize, but it cannot guarantee correct outcomes in unanticipated contexts.",
      "C18.04": "Axiom-based methods can reduce repeated decisions; they do not remove the need to verify combinations."
    },
    "unit_subjects": {
      "C18.01": "The crucial insight from Every Layout\\'s Axioms chapter is that\ndesigning by axiom means designing *without seeing*.",
      "C18.02": "You cannot predict\nevery visual consequence of a well-chosen axiom, and *you do not need\nto*.",
      "C18.03": "The axiom generates correct outcomes in contexts you never\nanticipated, because it encodes a *principle* rather than a *specific\narrangement*.",
      "C18.04": "This is what makes axiom-based design scale: it does not\nrequire a designer to manually verify every combination of content and\ncontext."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C18.01": {
        "start": 0,
        "end": 114
      },
      "C18.02": {
        "start": 115,
        "end": 222
      },
      "C18.03": {
        "start": 223,
        "end": 318
      },
      "C18.04": {
        "start": 319,
        "end": 421
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C19",
    "claim_ids": [
      "C19.01",
      "C19.02"
    ],
    "result_ids": [
      "C19.01",
      "C19.02"
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
    "replacement": "Use a broad selector only with an explicit, bounded and tested exception set. Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions.",
    "rationale": "Composed action for C19; exception-based CSS approach",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C19.01": "Use a broad selector only with an explicit, bounded and tested exception set.",
      "C19.02": "Exception-based CSS can reduce repeated declarations, but requires maintaining and testing those exceptions."
    },
    "unit_subjects": {
      "C19.01": "Axioms are best implemented using exception-based CSS: apply the rule to\neverything (`*`), then remove it from the specific elements that are\nlogical exceptions (containers, wrappers, structural elements).",
      "C19.02": "This\ninverted approach means you only need to *remember the exceptions*, not\nenumerate every element that should follow the rule."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C19.01": {
        "start": 0,
        "end": 77
      },
      "C19.02": {
        "start": 78,
        "end": 186
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C20",
    "claim_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
    ],
    "result_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
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
    "replacement": "**The test:** try stating each design rule in one sentence. Ask whether one declaration can express it in the intended context. A single declaration may encode a useful project axiom, subject to its scope and exceptions. A multi-part rule may be a convention or composition; complexity alone does not make it false.",
    "rationale": "Composed action for C20; axiom classification heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C20.01": "**The test:** try stating each design rule in one sentence.",
      "C20.02": "Ask whether one declaration can express it in the intended context.",
      "C20.03": "A single declaration may encode a useful project axiom, subject to its scope and exceptions.",
      "C20.04": "A multi-part rule may be a convention or composition; complexity alone does not make it false."
    },
    "unit_subjects": {
      "C20.01": "**The test:** can you state each design rule in a single sentence?",
      "C20.02": "Can\nthat sentence be translated into a single CSS declaration?",
      "C20.03": "If so, it is\nan axiom.",
      "C20.04": "If not, it may be a convention masquerading as a principle."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C20.01": {
        "start": 0,
        "end": 59
      },
      "C20.02": {
        "start": 60,
        "end": 127
      },
      "C20.03": {
        "start": 128,
        "end": 220
      },
      "C20.04": {
        "start": 221,
        "end": 315
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C21",
    "claim_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
    ],
    "result_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
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
    "disposition": "qualify",
    "replacement": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content. Use the measure axiom here only when a prose or task-specific measure is appropriate. **Mechanism:** `max-inline-size` with `margin-inline: auto`. For normal-flow, non-replaced block boxes with a non-auto width and both physical horizontal margins auto, CSS2.1 §10.3.3 makes the used margins equal to center the box; overconstraint and other formatting contexts have separate rules. `margin-inline` maps through writing mode, direction and text orientation. Uses `box-sizing: content-box` so padding does not reduce the content area; keep this as a context-specific box-sizing choice. **Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers.",
    "rationale": "Composed action for C21; scoped configurable measure",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C21.01": "**Responsibility:** constrain content to a maximum inline size and center it where that layout suits the content.",
      "C21.02": "Use the measure axiom here only when a prose or task-specific measure is appropriate.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`. For normal-flow, non-replaced block boxes with a non-auto width and both physical horizontal margins auto, CSS2.1 §10.3.3 makes the used margins equal to center the box; overconstraint and other formatting contexts have separate rules. `margin-inline` maps through writing mode, direction and text orientation.",
      "C21.04": "Uses `box-sizing: content-box` so padding does not reduce the content area; keep this as a context-specific box-sizing choice.",
      "C21.05": "**Key parameter:** `--measure` may default near `60ch` for prose; choose wider or otherwise suitable bounds for layout containers."
    },
    "unit_subjects": {
      "C21.01": "**Responsibility:** constraining content to a maximum width and centring\nit horizontally.",
      "C21.02": "The measure axiom is typically enforced here.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` (maximum width, typically `60ch` for\nprose, wider for layout containers)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C21.01": {
        "start": 0,
        "end": 113
      },
      "C21.02": {
        "start": 114,
        "end": 199
      },
      "C21.03": {
        "start": 200,
        "end": 571
      },
      "C21.04": {
        "start": 572,
        "end": 698
      },
      "C21.05": {
        "start": 699,
        "end": 829
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C22",
    "claim_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
    ],
    "result_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
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
    "replacement": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require. Begin without a breakpoint where intrinsic wrapping preserves the task. **Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs. The threshold can be informed by content and container space; it is not automatically correct for every task. **Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes.",
    "rationale": "Composed action for C22; intrinsic Switcher threshold",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C22.01": "**Responsibility:** switch between multi-column and single-column arrangement as available space and task grouping require.",
      "C22.02": "Begin without a breakpoint where intrinsic wrapping preserves the task.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a content-informed `flex-basis`; Flexbox defines line collection and flexible-length resolution, subject to item and container inputs.",
      "C22.04": "The threshold can be informed by content and container space; it is not automatically correct for every task.",
      "C22.05": "**Key parameter:** `--threshold` may describe a validated container width at which a task-specific mode changes."
    },
    "unit_subjects": {
      "C22.01": "**Responsibility:** switching between a multi-column and a single-column\nlayout based on available space.",
      "C22.02": "No breakpoints.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that\ncauses items to wrap at the threshold width.",
      "C22.04": "The threshold is defined by\nthe content, not the viewport.",
      "C22.05": "**Key parameter:** `--threshold` (the container width at which items\nstack)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C22.01": {
        "start": 0,
        "end": 123
      },
      "C22.02": {
        "start": 124,
        "end": 195
      },
      "C22.03": {
        "start": 196,
        "end": 368
      },
      "C22.04": {
        "start": 369,
        "end": 478
      },
      "C22.05": {
        "start": 479,
        "end": 591
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C23",
    "claim_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
    ],
    "result_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
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
    "replacement": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method. They are the system’s “atoms,” a metaphor for reusable building blocks. Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them.",
    "rationale": "Composed action for C23; complete-vocabulary guarantee and composition model",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C23.01": "These thirteen primitives form a reusable composition vocabulary; the statement describes a method.",
      "C23.02": "They are the system’s “atoms,” a metaphor for reusable building blocks.",
      "C23.03": "Cards, headers, navigation, forms and footers can be composed from the primitives, but these examples do not prove that every layout is expressible from them."
    },
    "unit_subjects": {
      "C23.01": "Together, these thirteen primitives can compose any layout.",
      "C23.02": "They are the\n*atoms* of the system.",
      "C23.03": "Everything else --- cards, headers, navigation,\nforms, footers --- is a *molecule* composed from these atoms."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C23.01": {
        "start": 0,
        "end": 99
      },
      "C23.02": {
        "start": 100,
        "end": 171
      },
      "C23.03": {
        "start": 172,
        "end": 330
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C24",
    "claim_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "result_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      970,
      975
    ],
    "literal_offset_0based": [
      0,
      408
    ],
    "file_byte_offsets": [
      46170,
      46582
    ],
    "original": "Start at utopia.fyi and generate a type scale and space scale. Paste the\ncustom properties into your stylesheet. Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs. Set `max-inline-size: 60ch` on all text elements. Use\n`gap` with Utopia space tokens for all spacing. Write zero media\nqueries. You will be astonished at how far this gets you.",
    "disposition": "correct",
    "replacement": "## Zero Breakpoints\n\nStart at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them. Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet. Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported. Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role. Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions. Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode. Treat the result as a useful starting point and verify it against the actual content and contexts.",
    "rationale": "Composed action for C24; broad implementation prescription",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C24.01": "## Zero Breakpoints\n\nStart at Utopia and generate a type scale and space scale; review the generated values for the project before adopting them.",
      "C24.02": "Before copying custom properties, include their complete definitions and verify every referenced token exists in the destination stylesheet.",
      "C24.03": "Stack and Sidebar are useful primitives; the claim that they cover most layout needs is an unverified breadth claim and should be presented as a local observation only if supported.",
      "C24.04": "Use `max-inline-size: 60ch` as a prose default, not for all text elements; size controls, data and other content by role.",
      "C24.05": "Use `gap` with Utopia space tokens as a project spacing convention, allowing task-specific exceptions.",
      "C24.06": "Start with zero-query intrinsic composition; add a justified media or container query when a verified content, task, user or output condition needs a discrete mode.",
      "C24.07": "Treat the result as a useful starting point and verify it against the actual content and contexts."
    },
    "unit_subjects": {
      "C24.01": "Start at utopia.fyi and generate a type scale and space scale.",
      "C24.02": "Paste the\ncustom properties into your stylesheet.",
      "C24.03": "Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs.",
      "C24.04": "Set `max-inline-size: 60ch` on all text elements.",
      "C24.05": "Use\n`gap` with Utopia space tokens for all spacing.",
      "C24.06": "Write zero media\nqueries.",
      "C24.07": "You will be astonished at how far this gets you."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C24.01": {
        "start": 0,
        "end": 145
      },
      "C24.02": {
        "start": 146,
        "end": 286
      },
      "C24.03": {
        "start": 287,
        "end": 468
      },
      "C24.04": {
        "start": 469,
        "end": 590
      },
      "C24.05": {
        "start": 591,
        "end": 693
      },
      "C24.06": {
        "start": 694,
        "end": 858
      },
      "C24.07": {
        "start": 859,
        "end": 957
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C25",
    "claim_ids": [
      "C25.01",
      "C25.02"
    ],
    "result_ids": [
      "C25.01",
      "C25.02"
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
    "replacement": "Shift responsive decisions toward component space when the component context matters. `ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself.",
    "rationale": "Composed action for C25; ch units eliminate magic-number thresholds",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C25.01": "Shift responsive decisions toward component space when the component context matters.",
      "C25.02": "`ch` can express a font-relative measure in a container query; it does not eliminate breakpoint choices or justify a threshold by itself."
    },
    "unit_subjects": {
      "C25.01": "Shift responsive design from viewport to component.",
      "C25.02": "Using `ch` units in\ncontainer queries eliminates magic-number breakpoints entirely."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C25.01": {
        "start": 0,
        "end": 85
      },
      "C25.02": {
        "start": 86,
        "end": 223
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  },
  {
    "action_id": "A-C26",
    "claim_ids": [
      "C26.01",
      "C26.02"
    ],
    "result_ids": [
      "C26.01",
      "C26.02"
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
    "replacement": "Components can adapt to the space they occupy when a suitable query container exists. Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior.",
    "rationale": "Composed action for C26; container-context adaptation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C26.01": "Components can adapt to the space they occupy when a suitable query container exists.",
      "C26.02": "Container query units depend on an eligible container and axis; verify the applicable conditions and fallback behavior."
    },
    "unit_subjects": {
      "C26.01": "Components adapt based on the space they actually occupy, not the\nbrowser window size.",
      "C26.02": "Combined with container query units (`cqw`, `cqh`),\nsizing becomes relative to context."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file.",
    "proposal_pointers": {
      "C26.01": {
        "start": 0,
        "end": 85
      },
      "C26.02": {
        "start": 86,
        "end": 205
      }
    },
    "part_rationale": "Each pointer identifies the exact inserted or retained literal clause for its source unit; identical parts are shared only where the source unit is retained verbatim."
  }
]
```json
[
  {
    "action_id": "A-C01",
    "claim_ids": [
      "C01.01",
      "C01.02"
    ],
    "result_ids": [
      "C01.01",
      "C01.02"
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
    "replacement": "Use the listed primitives as a compositional starting vocabulary; add a justified layout rule when content, semantics or interaction requires it.",
    "rationale": "Composed action for C01; local layout-composition policy",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C01.01": "Use the listed primitives as a compositional starting vocabulary; add a justified layout rule when content or interaction requires it.",
      "C01.02": "Use the listed primitives as a compositional starting vocabulary; add a justified layout rule when content or interaction requires it."
    },
    "unit_subjects": {
      "C01.01": "Every layout is a composition of these.",
      "C01.02": "No bespoke CSS layouts — compose from primitives."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C27",
    "claim_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
    ],
    "result_ids": [
      "C27.01",
      "C27.02",
      "C27.03"
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
    "disposition": "qualify",
    "replacement": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow). A page header = Cover containing a Center containing a Stack. A navigation = Cluster inside a Box. This is one example, not a complete layout grammar.",
    "rationale": "Composed action for C27; primitive composition example",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C27.01": "Keep as an illustrative composition pattern; treat it as one useful example, not an exhaustive layout grammar.",
      "C27.02": "Keep as an illustrative composition pattern; treat it as one useful example, not an exhaustive layout grammar.",
      "C27.03": "Keep as an illustrative composition pattern; treat it as one useful example, not an exhaustive layout grammar."
    },
    "unit_subjects": {
      "C27.01": "**Composition example**: A card = Box (padding) containing a Stack (vertical flow).",
      "C27.02": "A page header = Cover containing a Center containing a Stack.",
      "C27.03": "A navigation = Cluster inside a Box."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
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
    "replacement": "| **Center** | Maximum inline measure and centering | `max-inline-size: var(--measure, 60ch); margin-inline: auto` | Prose; choose purpose-specific sizing for controls, media, data and other width-constrained content |",
    "rationale": "Composed action for C02; measure default and scope",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C02": "Use a configurable measure such as 60ch for prose; choose an appropriate unconstrained or wider container for non-prose layout."
    },
    "unit_subjects": {
      "C02": "| **Center** | Max-width + horizontal centering | `max-inline-size: 60ch; margin-inline: auto` | Prose, any width-constrained content |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
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
    "disposition": "qualify",
    "replacement": "| **Switcher** | Multi-column to single-column arrangement as space changes | Intrinsic wrapping can use `flex-wrap: wrap` and a content-informed basis | Start with intrinsic wrapping; verify task grouping and provide a justified discrete mode when wrapping does not preserve operation |",
    "rationale": "Composed action for C03; intrinsic switcher",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C03": "Retain Switcher as an intrinsic technique; assess each composition for content, operation and accessibility."
    },
    "unit_subjects": {
      "C03": "| **Switcher** | Multi-col → single-col based on space | `flex-wrap: wrap` with calculated `flex-basis` | Responsive columns without breakpoints |"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C04",
    "claim_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
    ],
    "result_ids": [
      "C04.01",
      "C04.02",
      "C04.03"
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
    "replacement": "Start with intrinsic layout and fluid constraints. Use a justified media or container query when content, interaction, user need or output medium requires a discrete adaptation; query removal is a diagnostic, not a universal pass condition.",
    "rationale": "Composed action for C04; zero-query rule and universal claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C04.01": "Start with intrinsic layout. Add a content- or user-context-driven query when a tested need requires discrete adaptation.",
      "C04.02": "Start with intrinsic layout. Add a content- or user-context-driven query when a tested need requires discrete adaptation.",
      "C04.03": "Start with intrinsic layout. Add a content- or user-context-driven query when a tested need requires discrete adaptation."
    },
    "unit_subjects": {
      "C04.01": "No media queries for layout.",
      "C04.02": "Primitives + fluid tokens handle all responsiveness.",
      "C04.03": "The test: if you removed every media query, would the layout still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C05",
    "claim_ids": [
      "C05.02"
    ],
    "result_ids": [
      "C05.02"
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
    "replacement": "5. **Breakpoint test**: Would intrinsic behavior keep this layout usable? If not, name the task/context need for an adaptation and verify that choice.",
    "rationale": "Composed action for C05; query-free review heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C05.02": "Ask whether intrinsic behavior suffices; where it does not, document the need and verify the chosen adaptation."
    },
    "unit_subjects": {
      "C05.02": "**Breakpoint test**: Remove all media queries mentally — does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
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
    "replacement": "/* Scope prose measure to prose; exempt or size controls and wide content by role. */\n.prose { max-inline-size: var(--measure, 60ch); }",
    "rationale": "Composed action for C06; universal measure rule with structural exceptions",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C06": "Set a configurable prose measure and exempt or separately size controls, media, structural containers and wide content."
    },
    "unit_subjects": {
      "C06": "* { max-inline-size: 60ch; }\nhtml, body, div, header, nav, main, footer { max-inline-size: none; }"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C07-C08",
    "claim_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "result_ids": [
      "C07.01",
      "C07.02",
      "C08.01",
      "C08.02"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      144,
      151
    ],
    "literal_offset_0based": [
      0,
      513
    ],
    "file_byte_offsets": [
      6541,
      7066
    ],
    "original": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance. You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*. The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*. They are your CSS doing\nexactly what you intended.",
    "disposition": "qualify",
    "replacement": "An axiom is a reusable default constraint, not a rule that must apply to every element without exception. A 60ch measure may be a useful prose default; define its scope and explicit exceptions. The browser applies CSS rules, but that alone does not establish that every resulting context is sound.\n\nThe `ch` unit follows the used font’s “0” advance under CSS Values rules; it does not promise a fixed pixel width or a count of arbitrary characters. Test relevant fonts, scripts, content and writing modes.",
    "rationale": "Composed action for C07; exceptionless axiom and universal enforcement",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C07.01": "Treat 60ch as a default for prose, implemented through a local token or component rule with explicit, reviewable exceptions.",
      "C07.02": "Treat 60ch as a default for prose, implemented through a local token or component rule with explicit, reviewable exceptions.",
      "C08.01": "A ch-based measure responds to the relevant font metrics, but verify representative fonts, scripts, content and containers.",
      "C08.02": "A ch-based measure responds to the relevant font metrics, but verify representative fonts, scripts, content and containers."
    },
    "unit_subjects": {
      "C07.01": "An axiom is a rule that pervades the system without exception --- \\\"the\nmeasure should never exceed 60ch,\\\" for instance.",
      "C07.02": "You don\\'t manually\napply this rule to each element; you write it once, as a universal\nstyle, and then *the browser enforces it everywhere*.",
      "C08.01": "The consequences\nthat emerge from this axiom may surprise you --- elements with larger\nfont sizes will be physically wider, because `1ch` scales with font\nsize --- but those consequences are *sound*.",
      "C08.02": "They are your CSS doing\nexactly what you intended."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C09-C10",
    "claim_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
    ],
    "result_ids": [
      "C09.01",
      "C09.02",
      "C09.03",
      "C10.01",
      "C10.02",
      "C10.03",
      "C10.04"
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
    "replacement": "The browser has context the author may not know, so prefer constraints that allow content and user settings to participate. A 60ch measure and 44px target are examples requiring scope and standards context. `min-`, `max-`, `clamp()`, `auto` and `flex-basis` are tools, not guarantees that the browser will choose the task-appropriate result; state the intended range and verify it.",
    "rationale": "Composed action for C09, C10; fixed values, measure and target examples CSS technique preference",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C09.01": "Prefer content-aware constraints where suitable; justify fixed or bounded values for the component and validate target-size requirements at their named WCAG level.",
      "C09.02": "Prefer content-aware constraints where suitable; justify fixed or bounded values for the component and validate target-size requirements at their named WCAG level.",
      "C09.03": "Prefer content-aware constraints where suitable; justify fixed or bounded values for the component and validate target-size requirements at their named WCAG level.",
      "C10.01": "Prefer these flexible CSS tools when their sizing behavior fits the content and interaction; they do not replace case-specific layout review.",
      "C10.02": "Prefer these flexible CSS tools when their sizing behavior fits the content and interaction; they do not replace case-specific layout review.",
      "C10.03": "Prefer these flexible CSS tools when their sizing behavior fits the content and interaction; they do not replace case-specific layout review.",
      "C10.04": "Prefer these flexible CSS tools when their sizing behavior fits the content and interaction; they do not replace case-specific layout review."
    },
    "unit_subjects": {
      "C09.01": "The single most important principle.",
      "C09.02": "Every fixed value in your CSS is a\nplace where you have overridden the browser\\'s judgment with your own.",
      "C09.03": "Sometimes this is necessary --- a maximum measure of `60ch`, a minimum\ntouch-target of `44px` --- but the default posture should always be to\n*suggest* rather than prescribe.",
      "C10.01": "Use `min-`, `max-`, and `clamp()`\ninstead of fixed values.",
      "C10.02": "Use `auto` instead of `100%`.",
      "C10.03": "Use `flex-basis`\ninstead of `width`.",
      "C10.04": "Each of these is an invitation for the browser to\nmake a contextually appropriate decision."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C11",
    "claim_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
    ],
    "result_ids": [
      "C11.01",
      "C11.02",
      "C11.03"
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
    "replacement": "This is not laziness; it recognizes that browser and user contexts vary. Design with those inputs in mind, then verify representative supported contexts and failure cases; no CSS constraint guarantees every outcome.",
    "rationale": "Composed action for C11; browser context and inevitable outcome",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C11.01": "Use browser and user context as design inputs, then verify supported environments and representative content; no CSS constraint guarantees every outcome.",
      "C11.02": "Use browser and user context as design inputs, then verify supported environments and representative content; no CSS constraint guarantees every outcome.",
      "C11.03": "Use browser and user context as design inputs, then verify supported environments and representative content; no CSS constraint guarantees every outcome."
    },
    "unit_subjects": {
      "C11.01": "This is not laziness.",
      "C11.02": "It is recognition that the browser knows things\nyou do not --- the user\\'s font size preferences, their zoom level,\ntheir screen dimensions, whether they are using a split-screen view,\nwhether they have a notch or a toolbar.",
      "C11.03": "Your CSS should provide\n*constraints within which good outcomes are inevitable*, not blueprints\nthat are correct in one context and broken in all others."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C12",
    "claim_ids": [
      "C12.01",
      "C12.02"
    ],
    "result_ids": [
      "C12.01",
      "C12.02"
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
    "replacement": "**The test:** Removing queries can reveal whether intrinsic constraints are adequate for this case. If it is not usable, identify the missing behavior and justify and verify a contextual adaptation.",
    "rationale": "Composed action for C12; query-free usability test",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C12.01": "Use query removal as a diagnostic prompt, not a pass condition; explain any discrete adaptation that remains necessary.",
      "C12.02": "Use query removal as a diagnostic prompt, not a pass condition; explain any discrete adaptation that remains necessary."
    },
    "unit_subjects": {
      "C12.01": "**The test:** if you removed every media query from your stylesheet,\nwould the layout still be usable?",
      "C12.02": "If not, your constraints are not yet\nwell enough chosen."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C13",
    "claim_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
    ],
    "result_ids": [
      "C13.01",
      "C13.02",
      "C13.03",
      "C13.04",
      "C13.05"
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
    "replacement": "The web is content-driven: paragraph measure, section block-size, inter-element gap and grid track count are separate choices. Use a reviewed prose measure; let content contribute to block-size; choose spacing from the project scale where appropriate; and set grid tracks from tested item needs and available space with `auto-fit`/`minmax()` only where suitable.",
    "rationale": "Composed action for C13; content-derived dimension principles",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C13.01": "Derive dimensions from content and context; use ch as an approximate glyph-relative prose measure and verify with the actual scripts and fonts.",
      "C13.02": "Derive dimensions from content and context; use ch as an approximate glyph-relative prose measure and verify with the actual scripts and fonts.",
      "C13.03": "Derive dimensions from content and context; use ch as an approximate glyph-relative prose measure and verify with the actual scripts and fonts.",
      "C13.04": "Derive dimensions from content and context; use ch as an approximate glyph-relative prose measure and verify with the actual scripts and fonts.",
      "C13.05": "Derive dimensions from content and context; use ch as an approximate glyph-relative prose measure and verify with the actual scripts and fonts."
    },
    "unit_subjects": {
      "C13.01": "The web is a content-driven medium.",
      "C13.02": "The width of a paragraph should be\ndetermined by its measure (in `ch` units).",
      "C13.03": "The height of a section\nshould be determined by the amount of content it contains.",
      "C13.04": "The gap\nbetween elements should be determined by the typographic scale (in `rem`\nor Utopia space tokens).",
      "C13.05": "The number of columns in a grid should be\ndetermined by the minimum acceptable item width and the available space\n(via `auto-fit` and `minmax()`)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C14",
    "claim_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
    ],
    "result_ids": [
      "C14.01",
      "C14.02",
      "C14.03",
      "C14.04",
      "C14.05",
      "C14.06"
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
    "replacement": "Avoid assuming content length, viewport width or container width in advance. Fixed sizes or column counts may still be justified by a concrete task or constraint; choose intrinsic sizing or a query only after stating the condition and checking the result.",
    "rationale": "Composed action for C14; fixed geometry assumptions and container-query claim",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C14.01": "Avoid brittle fixed geometry, but use explicit sizes and column counts when justified; queries and intrinsic rules solve different needs.",
      "C14.02": "Avoid brittle fixed geometry, but use explicit sizes and column counts when justified; queries and intrinsic rules solve different needs.",
      "C14.03": "Avoid brittle fixed geometry, but use explicit sizes and column counts when justified; queries and intrinsic rules solve different needs.",
      "C14.04": "Avoid brittle fixed geometry, but use explicit sizes and column counts when justified; queries and intrinsic rules solve different needs.",
      "C14.05": "Avoid brittle fixed geometry, but use explicit sizes and column counts when justified; queries and intrinsic rules solve different needs.",
      "C14.06": "Avoid brittle fixed geometry, but use explicit sizes and column counts when justified; queries and intrinsic rules solve different needs."
    },
    "unit_subjects": {
      "C14.01": "When you prescribe a height, you are declaring that you know how much\ncontent will be present.",
      "C14.02": "You almost certainly do not.",
      "C14.03": "When you prescribe\na width in pixels, you are declaring that you know the user\\'s viewport\nsize.",
      "C14.04": "You do not.",
      "C14.05": "When you prescribe a column count, you are declaring\nthat you know the container\\'s width.",
      "C14.06": "In a world of container queries\nand intrinsic design, you should not need to."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C15",
    "claim_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
    ],
    "result_ids": [
      "C15.01",
      "C15.02",
      "C15.03"
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
    "replacement": "Content and context should inform dimensions and arrangement. Derived values are a useful default method, not a ban on explicit values where a reasoned requirement calls for them.",
    "rationale": "Composed action for C15; design rule of derivation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C15.01": "Prefer rules that respond to content and context, while allowing explicit values where the design requirement warrants them.",
      "C15.02": "Prefer rules that respond to content and context, while allowing explicit values where the design requirement warrants them.",
      "C15.03": "Prefer rules that respond to content and context, while allowing explicit values where the design requirement warrants them."
    },
    "unit_subjects": {
      "C15.01": "Content determines dimensions.",
      "C15.02": "Context determines arrangement.",
      "C15.03": "The\ndesigner\\'s job is to set the *rules of derivation*, not the values\nthemselves."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C16",
    "claim_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
    ],
    "result_ids": [
      "C16.01",
      "C16.02",
      "C16.03"
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
    "disposition": "qualify",
    "replacement": "**The test:** if content expands, the viewport narrows, or both happen, does the task remain usable? Also check changed font metrics, an unbreakable token and wide content.",
    "rationale": "Composed action for C16; content and viewport stress heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C16.01": "Retain as a test prompt and add changed-font metrics, unbreakable tokens, expanded labels and wide-content cases.",
      "C16.02": "Retain as a test prompt and add changed-font metrics, unbreakable tokens, expanded labels and wide-content cases.",
      "C16.03": "Retain as a test prompt and add changed-font metrics, unbreakable tokens, expanded labels and wide-content cases."
    },
    "unit_subjects": {
      "C16.01": "**The test:** if the content doubles in length, does the layout still\nwork?",
      "C16.02": "If the viewport halves in width, does it still work?",
      "C16.03": "If both\nhappen simultaneously, does it still work?"
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C17",
    "claim_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
    ],
    "result_ids": [
      "C17.01",
      "C17.02",
      "C17.03",
      "C17.04",
      "C17.05"
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
    "replacement": "Treat the 60ch prose measure as a configurable reading preference, with “ch” defined by the used font’s zero-glyph advance; it does not count arbitrary characters. Choose target dimensions by the applicable criterion and level: WCAG 2.2 AA’s 24 CSS px minimum and AAA’s 44 CSS px enhanced target have separate exceptions; a stronger local target may be adopted explicitly. Use Utopia spacing tokens as a project scale where they serve the composition. Do not collapse these examples into a single CSS declaration enforced everywhere; state each rule’s scope, exceptions, override mechanism and validation route.",
    "rationale": "Composed correction preserves all three examples while separating measure, target-size standards, spacing convention and universal-enforcement scope.",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C17.01": "Keep “axiom” language only for a scoped rule with its exceptions named.",
      "C17.02": "Treat 60ch as a configurable prose measure based on the font’s zero advance, not a character count.",
      "C17.03": "Name whether 44 CSS px is a local stronger target or a particular WCAG criterion and level; preserve its exceptions.",
      "C17.04": "Use Utopia tokens as a chosen spacing scale where suitable, not a universal requirement.",
      "C17.05": "Do not describe these examples as one exceptionless declaration enforced everywhere."
    },
    "unit_subjects": {
      "C17.01": "An axiom is a design rule that pervades the entire system without\nexception.",
      "C17.02": "\\\"The measure shall not exceed 60ch.\\\"",
      "C17.03": "\\\"The minimum touch\ntarget shall be 44px.\\\"",
      "C17.04": "\\\"Spacing between sibling elements shall use\nUtopia space tokens.\\\"",
      "C17.05": "These are not guidelines to remember; they are\n*CSS declarations* that are written once and enforced everywhere."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C18",
    "claim_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
    ],
    "result_ids": [
      "C18.01",
      "C18.02",
      "C18.03",
      "C18.04"
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
    "replacement": "A well-chosen rule may reduce repeated manual adjustment, but it cannot establish correct outcomes for every unanticipated combination. Review representative content/context combinations and adverse cases; no axiom removes the need for verification.",
    "rationale": "Composed action for C18; attribution, correctness and verification guarantee",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C18.01": "Use rules to reduce repeated hand-tuning, while inspecting representative combinations and failures; attribute the cited source only after edition and passage are established.",
      "C18.02": "Use rules to reduce repeated hand-tuning, while inspecting representative combinations and failures; attribute the cited source only after edition and passage are established.",
      "C18.03": "Use rules to reduce repeated hand-tuning, while inspecting representative combinations and failures; attribute the cited source only after edition and passage are established.",
      "C18.04": "Use rules to reduce repeated hand-tuning, while inspecting representative combinations and failures; attribute the cited source only after edition and passage are established."
    },
    "unit_subjects": {
      "C18.01": "The crucial insight from Every Layout\\'s Axioms chapter is that\ndesigning by axiom means designing *without seeing*.",
      "C18.02": "You cannot predict\nevery visual consequence of a well-chosen axiom, and *you do not need\nto*.",
      "C18.03": "The axiom generates correct outcomes in contexts you never\nanticipated, because it encodes a *principle* rather than a *specific\narrangement*.",
      "C18.04": "This is what makes axiom-based design scale: it does not\nrequire a designer to manually verify every combination of content and\ncontext."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C19",
    "claim_ids": [
      "C19.01",
      "C19.02"
    ],
    "result_ids": [
      "C19.01",
      "C19.02"
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
    "replacement": "Use a broad selector only when its inheritance and exception set are explicit, bounded and checked. Otherwise apply the rule to named semantic roles. Record why each exception is valid and test both included and excluded elements.",
    "rationale": "Composed action for C19; exception-based CSS approach",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C19.01": "Use a broad selector only when its inheritance and exception set are controlled and tested; otherwise target semantic components directly.",
      "C19.02": "Use a broad selector only when its inheritance and exception set are controlled and tested; otherwise target semantic components directly."
    },
    "unit_subjects": {
      "C19.01": "Axioms are best implemented using exception-based CSS: apply the rule to\neverything (`*`), then remove it from the specific elements that are\nlogical exceptions (containers, wrappers, structural elements).",
      "C19.02": "This\ninverted approach means you only need to *remember the exceptions*, not\nenumerate every element that should follow the rule."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C20",
    "claim_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
    ],
    "result_ids": [
      "C20.01",
      "C20.02",
      "C20.03",
      "C20.04"
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
    "replacement": "**The test:** can the rule be stated simply and represented by one declaration? Use the answer to improve clarity; simplicity does not establish universality or correctness.",
    "rationale": "Composed action for C20; axiom classification heuristic",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C20.01": "Use this as a clarity prompt; single-declaration form does not establish universality or correctness.",
      "C20.02": "Use this as a clarity prompt; single-declaration form does not establish universality or correctness.",
      "C20.03": "Use this as a clarity prompt; single-declaration form does not establish universality or correctness.",
      "C20.04": "Use this as a clarity prompt; single-declaration form does not establish universality or correctness."
    },
    "unit_subjects": {
      "C20.01": "**The test:** can you state each design rule in a single sentence?",
      "C20.02": "Can\nthat sentence be translated into a single CSS declaration?",
      "C20.03": "If so, it is\nan axiom.",
      "C20.04": "If not, it may be a convention masquerading as a principle."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C21",
    "claim_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
    ],
    "result_ids": [
      "C21.01",
      "C21.02",
      "C21.03",
      "C21.04",
      "C21.05"
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
    "disposition": "qualify",
    "replacement": "**Responsibility:** constrain content to a maximum inline size and center it; a measure default may be used here.\n\n**Mechanism:** `max-inline-size` with `margin-inline: auto`. `box-sizing: content-box` makes specified sizing lengths apply to the content box, with padding/border outside that specified size.\n\n**Key parameter:** `--measure` (a reviewed prose default, often around `60ch`; use an appropriate wider value for layout containers).",
    "rationale": "Composed action for C21; scoped configurable measure",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C21.01": "Retain Center as a maximum-inline-size and centering primitive; state which content roles use it.",
      "C21.02": "Describe a configurable measure as a local default implemented at Center, not a universal axiom.",
      "C21.03": "Retain max-inline-size and automatic inline margins as the mechanism, subject to layout-context behavior.",
      "C21.04": "Explain that content-box sizing measures the content box; padding and border are outside it and can increase outer size.",
      "C21.05": "Keep a configurable --measure: commonly around 60ch for prose, with reviewed wider values for layout containers."
    },
    "unit_subjects": {
      "C21.01": "**Responsibility:** constraining content to a maximum width and centring\nit horizontally.",
      "C21.02": "The measure axiom is typically enforced here.",
      "C21.03": "**Mechanism:** `max-inline-size` with `margin-inline: auto`.",
      "C21.04": "Uses\n`box-sizing: content-box` so that padding does not reduce the content\narea.",
      "C21.05": "**Key parameter:** `--measure` (maximum width, typically `60ch` for\nprose, wider for layout containers)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C22",
    "claim_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
    ],
    "result_ids": [
      "C22.01",
      "C22.02",
      "C22.03",
      "C22.04",
      "C22.05"
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
    "replacement": "**Responsibility:** arrange items across multiple columns or stack them as available space changes; this can be intrinsic and does not inherently require a breakpoint.\n\n**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` can produce a content-informed wrapping threshold, subject to flex sizing, item minimums and available space.\n\n**Key parameter:** `--threshold` (a candidate container width to validate against the actual content and task).",
    "rationale": "Composed action for C22; intrinsic Switcher threshold",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C22.01": "Retain content-driven wrapping as the first option; make a discrete query or mode available when interaction needs a state change that wrapping cannot provide.",
      "C22.02": "Retain content-driven wrapping as the first option; make a discrete query or mode available when interaction needs a state change that wrapping cannot provide.",
      "C22.03": "Retain content-driven wrapping as the first option; make a discrete query or mode available when interaction needs a state change that wrapping cannot provide.",
      "C22.04": "Retain content-driven wrapping as the first option; make a discrete query or mode available when interaction needs a state change that wrapping cannot provide.",
      "C22.05": "Retain content-driven wrapping as the first option; make a discrete query or mode available when interaction needs a state change that wrapping cannot provide."
    },
    "unit_subjects": {
      "C22.01": "**Responsibility:** switching between a multi-column and a single-column\nlayout based on available space.",
      "C22.02": "No breakpoints.",
      "C22.03": "**Mechanism:** `flex-wrap: wrap` with a calculated `flex-basis` that\ncauses items to wrap at the threshold width.",
      "C22.04": "The threshold is defined by\nthe content, not the viewport.",
      "C22.05": "**Key parameter:** `--threshold` (the container width at which items\nstack)."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C23",
    "claim_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
    ],
    "result_ids": [
      "C23.01",
      "C23.02",
      "C23.03"
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
    "replacement": "These thirteen primitives form a reusable composition vocabulary. They are useful building blocks, not a demonstrated exhaustive grammar for every layout. Cards, headers, navigation, forms and footers can be composed from them, with additional patterns where content or interaction needs them.",
    "rationale": "Composed action for C23; complete-vocabulary guarantee and composition model",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C23.01": "Treat the primitives as reusable composition tools, not an exhaustive guarantee that every layout or interaction is expressible without additional patterns.",
      "C23.02": "Treat the primitives as reusable composition tools, not an exhaustive guarantee that every layout or interaction is expressible without additional patterns.",
      "C23.03": "Treat the primitives as reusable composition tools, not an exhaustive guarantee that every layout or interaction is expressible without additional patterns."
    },
    "unit_subjects": {
      "C23.01": "Together, these thirteen primitives can compose any layout.",
      "C23.02": "They are the\n*atoms* of the system.",
      "C23.03": "Everything else --- cards, headers, navigation,\nforms, footers --- is a *molecule* composed from these atoms."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C24",
    "claim_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "result_ids": [
      "C24.01",
      "C24.02",
      "C24.03",
      "C24.04",
      "C24.05",
      "C24.06",
      "C24.07"
    ],
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "path": "knowledge/design/guides/layout.md",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "span": [
      970,
      975
    ],
    "literal_offset_0based": [
      0,
      408
    ],
    "file_byte_offsets": [
      46170,
      46582
    ],
    "original": "Start at utopia.fyi and generate a type scale and space scale. Paste the\ncustom properties into your stylesheet. Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs. Set `max-inline-size: 60ch` on all text elements. Use\n`gap` with Utopia space tokens for all spacing. Write zero media\nqueries. You will be astonished at how far this gets you.",
    "disposition": "correct",
    "replacement": "Start at utopia.fyi and generate a type scale and space scale. Paste the custom properties into your stylesheet. Read the Every Layout chapters on Stack and Sidebar—those two primitives alone cover many common layouts. Use `max-inline-size: var(--measure, 60ch)` for prose where suitable, not on all text elements. Use `gap` with Utopia space tokens where the spacing system calls for them. Start with intrinsic layout; add a justified, verified media/container adaptation when needed. Use this as a starting point and check its fit against the content and interaction.",
    "rationale": "Composed action for C24; broad implementation prescription",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C24.01": "Use a prose measure where appropriate; treat spacing tokens as local guidance and add justified context adaptation when required.",
      "C24.02": "Use a prose measure where appropriate; treat spacing tokens as local guidance and add justified context adaptation when required.",
      "C24.03": "Use a prose measure where appropriate; treat spacing tokens as local guidance and add justified context adaptation when required.",
      "C24.04": "Use a prose measure where appropriate; treat spacing tokens as local guidance and add justified context adaptation when required.",
      "C24.05": "Use a prose measure where appropriate; treat spacing tokens as local guidance and add justified context adaptation when required.",
      "C24.06": "Use a prose measure where appropriate; treat spacing tokens as local guidance and add justified context adaptation when required.",
      "C24.07": "Use this as a starting point and check its fit against the content and interaction."
    },
    "unit_subjects": {
      "C24.01": "Start at utopia.fyi and generate a type scale and space scale.",
      "C24.02": "Paste the\ncustom properties into your stylesheet.",
      "C24.03": "Read the Every Layout chapters\non Stack and Sidebar --- those two primitives alone cover the majority\nof layout needs.",
      "C24.04": "Set `max-inline-size: 60ch` on all text elements.",
      "C24.05": "Use\n`gap` with Utopia space tokens for all spacing.",
      "C24.06": "Write zero media\nqueries.",
      "C24.07": "You will be astonished at how far this gets you."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C25",
    "claim_ids": [
      "C25.01",
      "C25.02"
    ],
    "result_ids": [
      "C25.01",
      "C25.02"
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
    "replacement": "Shift responsive decisions toward the component’s available space when that context is relevant. `ch` can express a font-relative threshold, but does not eliminate arbitrary or untested choices; justify the value from content and behavior.",
    "rationale": "Composed action for C25; ch units eliminate magic-number thresholds",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C25.01": "Container queries can express content-context thresholds; justify each value from tested content and behavior, since ch only supplies a relative unit.",
      "C25.02": "Container queries can express content-context thresholds; justify each value from tested content and behavior, since ch only supplies a relative unit."
    },
    "unit_subjects": {
      "C25.01": "Shift responsive design from viewport to component.",
      "C25.02": "Using `ch` units in\ncontainer queries eliminates magic-number breakpoints entirely."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  },
  {
    "action_id": "A-C26",
    "claim_ids": [
      "C26.01",
      "C26.02"
    ],
    "result_ids": [
      "C26.01",
      "C26.02"
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
    "replacement": "Components can adapt to their containing space where a suitable query container exists. Container-relative units such as `cqw`/`cqh` use specified eligible-container and axis rules, including fallback; verify those conditions and justify each threshold.",
    "rationale": "Composed action for C26; container-context adaptation",
    "owner": "Arc04 implementation planning for live guidance; Arc03 owns browser/accessibility validation where implicated; P10-11 Operator/R owns missing original-source inputs. No implementation is assigned or accepted here.",
    "proposal_parts": {
      "C26.01": "Prefer container context for component-local adaptation when a suitable query container exists; verify axis, size containment and fallback behavior.",
      "C26.02": "Prefer container context for component-local adaptation when a suitable query container exists; verify axis, size containment and fallback behavior."
    },
    "unit_subjects": {
      "C26.01": "Components adapt based on the space they actually occupy, not the\nbrowser window size.",
      "C26.02": "Combined with container query units (`cqw`, `cqh`),\nsizing becomes relative to context."
    },
    "line_target_contract": "literal_offset_0based is a half-open Unicode codepoint span within LF-joined inclusive source lines; file_byte_offsets is the equivalent half-open UTF-8 byte span in the pinned file."
  }
]
```

## Ownership and gates

- Future live-guide edits belong to a freshly authorized Arc04 implementation assignment; source-fidelity gaps and original captures remain P10-11/Operator/R-owned.
- Future keyboard, focus, reading-order, target-size and assistive-technology checks belong to Arc03; WCAG references do not substitute for them.
- Original claims remain the subject of these assessments. Replacements have their own bounded evidence and are not used to score the original as correct.
- No DES finding, full corpus, card relationship/CQ, source, package, browser, AT or release gate is closed by this handoff.
