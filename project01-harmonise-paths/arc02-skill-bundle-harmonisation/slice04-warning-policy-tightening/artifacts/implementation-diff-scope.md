# Implementation Diff Scope

`git status --short --untracked-files=all` in the implementation checkout shows
one modified implementation file:

```text
 M package-path-exceptions.tsv
```

The diff converts five stale transitional policy rows:

- Rust missing CLI pitfalls guide references now expire as `later-rust-guide-maintenance`.
- C++ missing parameter-passing image references now expire as `later-cpp-asset-maintenance`.
- JavaScript/Deno guide shorthand references now expire as `later-js-guide-harmonisation`.

The implementation checkout has no source-package, guide-prose, checker-code, or
generated bundle edits from Slice 04.
