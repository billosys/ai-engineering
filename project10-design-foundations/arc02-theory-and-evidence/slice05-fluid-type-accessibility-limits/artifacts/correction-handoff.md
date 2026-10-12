# Slice05 literal correction and Arc03 behavior handoff

CC-proposed. SOURCE is pinned to `dffa504e851b03b8e4746f1941068e4cc850b612`. This registry is the sole current action set: 15 assessed result IDs, each exactly once. `retain` has no replacement; `qualify`/`correct` carry a complete literal replacement; model-input retentions for C04–C07 point to, and do not replace, accepted Slice01 handoffs. Proposed text is not installed. Arc04 owns any source composition and mutation; Arc03 owns runtime behavior proof.

## Exact proposed actions

The JSON block is strict, closed, and complete. Each source pointer is one-based inclusive line bounds plus zero-based half-open byte bounds into the exact pinned file. Null replacement is required for `retain`. The consumer checks identities, hashes, bounds, original bytes, dispositions, unique result membership, replacement digests, non-overlap, and complete virtual composition.

```json
[
  {
    "action_id": "A-C01",
    "result_ids": [
      "C01"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      69,
      69
    ],
    "byte_offsets": [
      6013,
      6226
    ],
    "literal_original": "| II | **Perception Is the Only Coordinate System** | Use OKLCH for colour, `rem`/`ch`/`vi` for sizing — units that describe experience, not mechanism. | Hex colours, `px` for type sizes, `vw` instead of `vi`. |",
    "replacement": "| II | **Perception Is the Only Coordinate System** | Use OKLCH for colour; for sizing, choose `rem`, `ch` or `vi` by the relationship required, and check user and content outcomes. | Choosing a unit without checking its specified basis or behavior. |",
    "replacement_sha256": "c04c6ce433256180eafb4b719ea8d4ef13a360289973018aa5b74b2348a1fe3c",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      251
    ],
    "replacement_parts": [
      {
        "part_id": "A-C01.P1",
        "byte_bounds": [
          0,
          251
        ],
        "text": "| II | **Perception Is the Only Coordinate System** | Use OKLCH for colour; for sizing, choose `rem`, `ch` or `vi` by the relationship required, and check user and content outcomes. | Choosing a unit without checking its specified basis or behavior. |",
        "sha256": "c04c6ce433256180eafb4b719ea8d4ef13a360289973018aa5b74b2348a1fe3c"
      }
    ]
  },
  {
    "action_id": "A-C02",
    "result_ids": [
      "C02"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      186,
      187
    ],
    "byte_offsets": [
      12207,
      12340
    ],
    "literal_original": "- **@min**: 360px viewport, 16px base, ratio 1.200 (minor third)\n- **@max**: 1440px viewport, 20px base, ratio 1.333 (perfect fourth)",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 retains the declared baseline and reconciles source coefficients with the accepted Slice01 handoff.",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-C03",
    "result_ids": [
      "C03"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      191,
      191
    ],
    "byte_offsets": [
      12361,
      12548
    ],
    "literal_original": "Type, space, and grid are **one unified mathematical system**. The base space token equals the base type size. Space pairs (e.g., `--space-s-l`) interpolate steeply for component padding.",
    "replacement": "Type, space, and grid can share project-defined inputs. Check each generated value and its use; a shared mathematical system does not itself establish accessible or suitable results.",
    "replacement_sha256": "42f87a996ce9deb7e153082d68777a97a27a924c02311b63f51fcd7c7b9b64a4",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      182
    ],
    "replacement_parts": [
      {
        "part_id": "A-C03.P1",
        "byte_bounds": [
          0,
          182
        ],
        "text": "Type, space, and grid can share project-defined inputs. Check each generated value and its use; a shared mathematical system does not itself establish accessible or suitable results.",
        "sha256": "42f87a996ce9deb7e153082d68777a97a27a924c02311b63f51fcd7c7b9b64a4"
      }
    ]
  },
  {
    "action_id": "A-C04",
    "result_ids": [
      "C04"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      195,
      195
    ],
    "byte_offsets": [
      12574,
      12629
    ],
    "literal_original": "--step-0: clamp(1rem, 0.9015rem + 0.4924vi, 1.3337rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 composes the accepted Slice01 arithmetic/correction handoff; no source correction is installed by this evidence assignment.",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-C05",
    "result_ids": [
      "C05"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      196,
      196
    ],
    "byte_offsets": [
      12630,
      12687
    ],
    "literal_original": "--step-1: clamp(1.2rem, 1.0534rem + 0.7331vi, 1.7783rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 composes the accepted Slice01 arithmetic/correction handoff; no source correction is installed by this evidence assignment.",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-C06",
    "result_ids": [
      "C06"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      200,
      200
    ],
    "byte_offsets": [
      12753,
      12811
    ],
    "literal_original": "--space-m: clamp(1.5rem, 1.3523rem + 0.7385vi, 2.0006rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 composes the accepted Slice01 arithmetic/correction handoff; no source correction is installed by this evidence assignment.",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-C07",
    "result_ids": [
      "C07"
    ],
    "disposition": "retain",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "57833e7cecd5984bf1cd6c7b26def1194f7cbbdf83e24a4960bd739a6f26ff63",
    "path": "knowledge/design/SKILL.md",
    "line_span": [
      203,
      203
    ],
    "byte_offsets": [
      12855,
      12913
    ],
    "literal_original": "--space-s-l: clamp(1rem, 0.5038rem + 2.4808vi, 2.6674rem);",
    "replacement": null,
    "replacement_sha256": null,
    "owner": "Arc04 composes the accepted Slice01 arithmetic/correction handoff; no source correction is installed by this evidence assignment.",
    "replacement_bounds": null,
    "replacement_parts": []
  },
  {
    "action_id": "A-C08",
    "result_ids": [
      "C08"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      118,
      118
    ],
    "byte_offsets": [
      5031,
      5100
    ],
    "literal_original": "density. The `rem` unit anchors to the user\\'s chosen root font size,",
    "replacement": "The `rem` unit is based on the computed font-size of the root element. A user preference affects it only when it changes that computed root size; verify enlargement and reflow separately.",
    "replacement_sha256": "c90dfadafb22199416f080e1ac0a2af1bef495b82ba32c1fa764c88a6eb3aa13",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      187
    ],
    "replacement_parts": [
      {
        "part_id": "A-C08.P1",
        "byte_bounds": [
          0,
          187
        ],
        "text": "The `rem` unit is based on the computed font-size of the root element. A user preference affects it only when it changes that computed root size; verify enlargement and reflow separately.",
        "sha256": "c90dfadafb22199416f080e1ac0a2af1bef495b82ba32c1fa764c88a6eb3aa13"
      }
    ]
  },
  {
    "action_id": "A-C09",
    "result_ids": [
      "C09"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      937,
      940
    ],
    "byte_offsets": [
      44742,
      44999
    ],
    "literal_original": "values and `b` is the y-intercept. The `vi` unit (viewport inline) is\nused instead of `vw` because it respects writing direction and,\ncritically, does not prevent browser zoom from scaling\ntext --- satisfying WCAG SC 1.4.4. The modular scale itself is a",
    "replacement": "Use `vi` when viewport-relative sizing should follow the inline axis. In horizontal writing it follows the same axis as `vw`; neither unit alone establishes text-resize conformance. Preserve user preferences and verify actual enlargement without loss of content or functionality, separately from reflow. The modular scale itself is a",
    "replacement_sha256": "757d184a427edf14190bc4a0ea65a741ba6fc434700bea1712168600058f3e48",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      333
    ],
    "replacement_parts": [
      {
        "part_id": "A-C09.P1",
        "byte_bounds": [
          0,
          333
        ],
        "text": "Use `vi` when viewport-relative sizing should follow the inline axis. In horizontal writing it follows the same axis as `vw`; neither unit alone establishes text-resize conformance. Preserve user preferences and verify actual enlargement without loss of content or functionality, separately from reflow. The modular scale itself is a",
        "sha256": "757d184a427edf14190bc4a0ea65a741ba6fc434700bea1712168600058f3e48"
      }
    ]
  },
  {
    "action_id": "A-C10",
    "result_ids": [
      "C10"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "361ea7887a69870db6db7aa362455b00b5cf718d6c4ae0d49405785fd5c82aec",
    "path": "knowledge/design/guides/layout.md",
    "line_span": [
      941,
      945
    ],
    "byte_offsets": [
      45000,
      45314
    ],
    "literal_original": "geometric progression: `size(n) = base × ratio^n`. Interpolating between\ntwo geometric progressions produces a family of curves, each\nasymptotically approaching the higher progression as the viewport\nwidens. This is why the visual hierarchy intensifies on larger screens\nwithout any explicit instruction to do so.",
    "replacement": "Each `clamp()` interpolation is linear between its endpoint values and saturates at its bounds. Step-specific changes depend on the selected endpoints; they do not establish a universal hierarchy or an asymptotic approach.",
    "replacement_sha256": "4e3ef7a688e97a06ae28971a2a618f56fcb54a5d6bf98575793664ced71cf1f5",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      222
    ],
    "replacement_parts": [
      {
        "part_id": "A-C10.P1",
        "byte_bounds": [
          0,
          222
        ],
        "text": "Each `clamp()` interpolation is linear between its endpoint values and saturates at its bounds. Step-specific changes depend on the selected endpoints; they do not establish a universal hierarchy or an asymptotic approach.",
        "sha256": "4e3ef7a688e97a06ae28971a2a618f56fcb54a5d6bf98575793664ced71cf1f5"
      }
    ]
  },
  {
    "action_id": "A-C11",
    "result_ids": [
      "C11"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      198,
      204
    ],
    "byte_offsets": [
      7406,
      7845
    ],
    "literal_original": "Utopia (James Gilyead and Trys Mudford) defines type and space at\nminimum and maximum viewport widths with different modular scale ratios,\nthen interpolates between them via `clamp()` with mixed `rem` and `vi`\nunits. The result: smooth, continuous type and spacing transitions with\nno jarring layout shifts at any viewport size. The use of `vi` (viewport\ninline) rather than `vw` preserves zoom accessibility, satisfying WCAG\nrequirements.",
    "replacement": "Utopia examples can use `clamp()` with font-relative and viewport-relative units for fluid values. The result depends on chosen endpoints, coefficients, axis and content; no unit guarantees an absence of layout shifts or WCAG conformance. Verify text enlargement without loss and reflow in the actual content.",
    "replacement_sha256": "a23f29eade7aa7b5817729dbee7ee73c7936c9a06013ebfc581bd1ff392be693",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      309
    ],
    "replacement_parts": [
      {
        "part_id": "A-C11.P1",
        "byte_bounds": [
          0,
          309
        ],
        "text": "Utopia examples can use `clamp()` with font-relative and viewport-relative units for fluid values. The result depends on chosen endpoints, coefficients, axis and content; no unit guarantees an absence of layout shifts or WCAG conformance. Verify text enlargement without loss and reflow in the actual content.",
        "sha256": "a23f29eade7aa7b5817729dbee7ee73c7936c9a06013ebfc581bd1ff392be693"
      }
    ]
  },
  {
    "action_id": "A-C12",
    "result_ids": [
      "C12"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      206,
      211
    ],
    "byte_offsets": [
      7847,
      8218
    ],
    "literal_original": "Space tokens derived from the same modular scale as typography create\nwhat Massimo Vignelli called \\\"syntactical consistency\\\" --- spacing and\ntype as a unified mathematical system. When the type scale is built on\nmusical interval ratios (perfect fourth at 4:3, perfect fifth at 3:2,\nmajor third at 5:4), the space system inherits that proportional harmony\nautomatically.",
    "replacement": "Shared type and space tokens can express a project scale. Their proportions are a design convention; state the chosen inputs and review their suitability.",
    "replacement_sha256": "9bb4a9a005190566380245850953a47d3a484e420b098d18309027a69de1dfc7",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      154
    ],
    "replacement_parts": [
      {
        "part_id": "A-C12.P1",
        "byte_bounds": [
          0,
          154
        ],
        "text": "Shared type and space tokens can express a project scale. Their proportions are a design convention; state the chosen inputs and review their suitability.",
        "sha256": "9bb4a9a005190566380245850953a47d3a484e420b098d18309027a69de1dfc7"
      }
    ]
  },
  {
    "action_id": "A-C13",
    "result_ids": [
      "C13"
    ],
    "disposition": "correct",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "76d209306a8ade1da51f62ad86fb7f01f103f0f4d033e7235c3b4b023397b845",
    "path": "knowledge/design/guides/breaking-the-layout-monoculture.md",
    "line_span": [
      218,
      218
    ],
    "byte_offsets": [
      8481,
      8571
    ],
    "literal_original": "  Typography     Utopia fluid type scale              Breakpoint-free, modular, accessible",
    "replacement": "Typography | Utopia fluid type scale | Breakpoint-free, modular; accessibility requires separate text-resize, reflow and content/functionality checks.",
    "replacement_sha256": "ab9312365696e77024d59ca381a47d5d739f3a5de6e0369149373e0ad26f77cc",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      150
    ],
    "replacement_parts": [
      {
        "part_id": "A-C13.P1",
        "byte_bounds": [
          0,
          150
        ],
        "text": "Typography | Utopia fluid type scale | Breakpoint-free, modular; accessibility requires separate text-resize, reflow and content/functionality checks.",
        "sha256": "ab9312365696e77024d59ca381a47d5d739f3a5de6e0369149373e0ad26f77cc"
      }
    ]
  },
  {
    "action_id": "A-C14",
    "result_ids": [
      "C14"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "e4953fd1452102c98df6f0fcf33bc17bd3732f011180475daa8fd256e70e687b",
    "path": "knowledge/design/guides/design.md",
    "line_span": [
      148,
      152
    ],
    "byte_offsets": [
      5384,
      5727
    ],
    "literal_original": "The same principle applies beyond colour. Fluid type scales that\ninterpolate between viewport widths should use the `vi` unit (viewport\ninline), which respects writing direction. Spacing should be defined in\n`rem`, which scales with the user\\'s font size preference. Every unit of\nmeasurement should describe the experience, not the mechanism.",
    "replacement": "For fluid sizing, choose `vi` when the viewport inline axis is the intended input. `rem` follows the computed root font-size; user settings and author root rules can affect outcomes differently. Verify enlargement, no-loss behavior and reflow in the actual context.",
    "replacement_sha256": "46ca43eba95991e829896ab8d6fdda12a0e4ff4fd5939641b0f1dcc20de09a63",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      265
    ],
    "replacement_parts": [
      {
        "part_id": "A-C14.P1",
        "byte_bounds": [
          0,
          265
        ],
        "text": "For fluid sizing, choose `vi` when the viewport inline axis is the intended input. `rem` follows the computed root font-size; user settings and author root rules can affect outcomes differently. Verify enlargement, no-loss behavior and reflow in the actual context.",
        "sha256": "46ca43eba95991e829896ab8d6fdda12a0e4ff4fd5939641b0f1dcc20de09a63"
      }
    ]
  },
  {
    "action_id": "A-C15",
    "result_ids": [
      "C15"
    ],
    "disposition": "qualify",
    "source_revision": "dffa504e851b03b8e4746f1941068e4cc850b612",
    "source_sha256": "8a9f1ab35dee3373ebbf1460416e334adffcd908f095463fa015c6ef0a5f5d7c",
    "path": "knowledge/design/guides/type.md",
    "line_span": [
      472,
      478
    ],
    "byte_offsets": [
      17910,
      18356
    ],
    "literal_original": "The fluid interpolation uses `clamp(min, preferred, max)` where the\npreferred value is a linear function of `vi` (viewport inline size). At\n360px the effective ratio is 1.25 (major third); at 1440px it\\'s 1.333\n(perfect fourth). This means headings grow proportionally faster than\nbody text as the viewport widens --- Bringhurst\\'s principle that\ndisplay type needs more air, and text type needs more density,\nimplemented in pure CSS mathematics.",
    "replacement": "The preferred term can be a linear function of `vi`, bounded by the selected `clamp()` endpoints. The project baseline uses 1.2 at 360px and 1.333 (approximately 4/3) at 1440px; reconcile any differing table value to that declared configuration. Whether larger headings grow faster depends on each step’s endpoint differences. The CSS expresses calculations; it does not establish attribution or perceptual effect.",
    "replacement_sha256": "011321d4a86657f23dc0fd7694c83aeada6d7107eb89ecd47799695529f78922",
    "owner": "Arc04 application; Arc03 runtime proof",
    "replacement_bounds": [
      0,
      416
    ],
    "replacement_parts": [
      {
        "part_id": "A-C15.P1",
        "byte_bounds": [
          0,
          416
        ],
        "text": "The preferred term can be a linear function of `vi`, bounded by the selected `clamp()` endpoints. The project baseline uses 1.2 at 360px and 1.333 (approximately 4/3) at 1440px; reconcile any differing table value to that declared configuration. Whether larger headings grow faster depends on each step’s endpoint differences. The CSS expresses calculations; it does not establish attribution or perceptual effect.",
        "sha256": "011321d4a86657f23dc0fd7694c83aeada6d7107eb89ecd47799695529f78922"
      }
    ]
  }
]
```

## Composition and prior accepted handoffs

C02–C07 point to declarations and coefficients previously examined in Arc02/Slice01, not source edits. [Slice01’s accepted arithmetic](../../slice01-fluid-scale-arithmetic/artifacts/fluid-scale-proof.md) and [configuration reconciliation](../../slice01-fluid-scale-arithmetic/artifacts/configuration-reconciliation.md) already propose correcting the two type clamps and require owner confirmation before dependent space token regeneration. This assignment preserves those proposals as predecessors and adds root/zoom behavior observations. They are not installed by this packet.

C09 and C11 are repeated original guarantees in two files, each requiring its own literal action. C10 overlaps Slice01’s previously assessed arithmetic at layout.md:941–945; retain its accepted endpoint/clamp result at that historical scope, and apply the new action only as a proposal in the current source context. C15 overlaps Slice01 type.md:472–478; retain its numeric endpoint arithmetic, while the 1.25 versus Project10 1.2 narrow-input conflict and accessibility implications remain current here. Arc04 must compose these predecessor handoffs against the whole live section and report conflicts before any source edit. No replacement in this artifact is represented as applied.

## Arc03 bounded future test protocol

This is a proposed re-entry packet, not current conformance evidence. Run only after Arc04 identifies and pins the composed CSS and representative application content. Before execution record browser name/version, operating system, device scale factor, CSS viewport, browser zoom, root computed font-size, author root declarations, user minimum-font/text-size preferences, font load status, writing-mode/direction, and the exact tested revision. Preserve screenshots/computed-style/DOM measurements and manual content/functionality observations as future Arc03 evidence.

1. **Resize Text (WCAG 2.2 SC 1.4.4, AA):** from 100%, test at least one user-agent-supported enlargement mechanism to 200% (page zoom, text-only sizing, or configured text size), including intermediate offered steps. Include headings/body, text in controls and labels, long/unbreakable strings, and the actual page content. Record whether text enlarged and whether any content or functionality is lost. This is a distinct run from reflow; the informative guidance says one supported mechanism can suffice, not that all listed mechanisms are mandatory.
2. **Reflow (SC 1.4.10, AA):** test horizontal-language/vertical-scroll content at 320 CSS-pixel width and vertical-language/horizontal-scroll content at 256 CSS-pixel height. Record two-axis scrolling, clipping, overlap, hidden controls/content, reading order and operation. Exercise representative one-dimensional prose, controls, long tokens and a genuinely two-dimensional example (e.g. data table/map) while retaining the exception only for parts whose use or meaning requires two-dimensional layout. Inspect table cells for reflow.
3. **Root and preferences:** vary computed root font-size separately from user minimum-font/text-size settings and author `html` overrides. Record computed root and affected `rem` values. Do not call a root model change browser zoom; do not assume a user preference changes computed `rem` resolution.
4. **Axis:** use a declared 800×600 CSS-pixel viewport with horizontal and vertical writing modes. Record computed `vi`/`vw` values, viewport variant and inline axis. This checks axis selection only, not text resizing or accessibility.
5. **Clamp specimens:** include source’s four literal clamps, a pure viewport-unit control, and the toy mixed clamp in source-comparison.md. Capture actual computed and rendered results under page zoom and text-size settings. Compare them with the fixed-root rational model as a hypothesis check; report mismatches rather than altering coefficients or fitting the model after observation.

Re-entry requires: accepted Arc04 composed revision; representative content and controls from the application; named browser/OS/device and repeatable settings; a protocol approved by Arc03; separate results for enlargement and reflow, including exceptions and failures. Until those inputs exist, current status is **unrun**. No user-agent support matrix, assistive-technology test, application behavior or WCAG conformance is asserted here.
