# Source Acquisition

## Acquired Snapshot

| Field | Observation |
| --- | --- |
| Upstream repository | `https://github.com/compcogneuro/book.git` |
| Temporary checkout | `/private/tmp/project05-compcogneuro-book-e0c697b4` |
| Requested commit | `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` |
| Checked-out `HEAD` | `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` |
| Tree | `894b3e10baa38e9d9c29a2e52b64f4d0ffb1378a` |
| Checkout state | Detached `HEAD`; clean immediately after checkout |
| Acquisition date | 2026-09-11 |
| License basis | Repository `LICENSE`: Creative Commons Attribution 4.0 International (`CC-BY-4.0`) |

The checkout is outside the source and planning worktrees. It is an
inspectable, temporary input for this bounded pilot and is not part of the
committed Slice02 artifact set.

## Sampled File Identity

| Resource | SHA-256 | Lines |
| --- | --- | ---: |
| `chapter-01.md` | `6a72d20260ba3fdac1f90b2bd8b99d0ed9d3acc7664e7d3d7b79070d7b2cba48` | 113 |
| `chapter-07.md` | `075b907fb4b8dfae6457b324ccc71f6f95f12f86e13f07df64584a35fb0e2b9d` | 184 |

## Non-Vendoring And Reproduction

No upstream chapter, figure, bibliography, or full-corpus copy appears under
the planning worktree. A future reproduction must clone or otherwise acquire
this exact commit outside planning, verify `HEAD` and the tree identity, and
recheck the sampled-file hashes before comparing results.
