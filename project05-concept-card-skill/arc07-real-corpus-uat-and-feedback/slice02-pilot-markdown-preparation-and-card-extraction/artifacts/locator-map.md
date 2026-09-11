# Pilot Locator Map

## Locator Convention

Each locator combines the immutable source snapshot, resource path, Markdown
heading anchor, and one-based inclusive source line range. Line numbers were
observed in the temporary checkout named in [source acquisition](./source-acquisition.md).
They resolve against the recorded file SHA-256; a changed file requires a new
locator revision rather than a presumed line-offset mapping.

| Locator ID | Resource | Anchor | Lines | Context hint |
| --- | --- | --- | ---: | --- |
| `loc-ch01-model-constraints` | `chapter-01.md` | `sec:ch-intro` / `The Computational Approach` | 37-45 | Data constraints, testable predictions, and simplification tradeoff |
| `loc-ch01-emergence` | `chapter-01.md` | `sec:ch-intro` / `Emergent Phenomena` | 53-57 | Reductionism, reconstructionism, and interacting gears |
| `loc-ch01-gears-figure` | `figures/fig_gears.png` | `fig:fig-gears` | n/a | PNG inspected directly; SHA-256 `f87dbaa675eb16da27c6a01fb349b075b8bf25cbcb5988f67275a53253d42138` |
| `loc-ch07-pattern-separation` | `chapter-07.md` | `sec:ch-memory` / `The Hippocampus and Pattern Separation / Pattern Completion` | 67-75 | Sparseness, overlap, and reduced interference |
| `loc-ch07-pattern-figure` | `figures/fig_patsep_clr.png` | `fig:fig-patsep-clr` | n/a | PNG inspected directly; SHA-256 `c7cc9ecb7ce06643388dfbec4984b2d1d444b270bbd8f0891bf9c8b0376dc035` |
| `loc-ch07-consolidation` | `chapter-07.md` | `sec:ch-memory` / `Memory Consolidation from Hippocampus to Neocortex` | 113-117 | Qualified consolidation account and limits |

The figure locators identify assets; their captions and claim interpretation
remain in the Markdown source-support comparison. No figure is used as an
independent, unreviewed substitute for the surrounding text.
