# Biome Formatting

Biome's formatter options, Prettier compatibility, intentional divergences, and format suppression. Formatting is a "configure once" topic — you set your indent style, line width, quotes, and semicolons once, then never discuss formatting in code review again. That's the goal. This is the shortest chapter in the guide series by design. Grounded in Biome documentation concept cards.

Target environment: **Deno** + **Biome**, **ESM-only**, **no TypeScript** (plain JS with JSDoc where needed).

---

## ID-01: Biome Is an Opinionated Formatter — Minimal Options by Design

**Strength**: SHOULD

**Summary**: Biome enforces one correct way to format code. The option set is intentionally small and frozen.

**The philosophy**: Biome functions as "its own automatic style guide, not a tool for implementing other style guides." Formatting debates vanish from code reviews. Requests for new formatting options are closed without discussion — this is a feature, not a limitation.

**Options that exist for Prettier migration** (not as first-class Biome features):
- `bracketSameLine`, `arrowParentheses`, `bracketSpacing` — these exist so teams migrating from Prettier can carry their config forward. Prettier's own documentation calls them options "we're not happy to have."

**Rationale**: Every formatting option is a formatting debate waiting to happen. Biome minimizes options to maximize the signal: "run the formatter, commit, move on." The formatter shares Prettier's Option Philosophy — both tools agree on minimalism even when their output differs in edge cases (Biome opinionated formatting docs).

---

## ID-02: Configure Once, Never Think About It

**Strength**: SHOULD

**Summary**: Set your formatter config once in `biome.json`. From then on, `biome format --write` and format-on-save handle everything.

```jsonc
// biome.json — the project's formatter config (configured once)
{
  "formatter": {
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double",
      "semicolons": "always",
      "trailingCommas": "all"
    }
  }
}
```

**The workflow**:
1. Set the options (this entry)
2. Enable format-on-save in VS Code (`13-biome/01-setup.md` ID-15)
3. Add `biome ci` to the check task (`12-deno/03-task-runner.md` ID-07)
4. Never discuss formatting in code review again

**Rationale**: Configuration is a one-time cost. Once the team agrees on indent style and line width, the formatter enforces it automatically on every save and CI run. Disagreements about formatting become impossible.

---

## ID-03: `indentStyle` — Spaces or Tabs

**Strength**: MUST

**Summary**: Choose `"space"` or `"tab"`. This is the one formatting decision that cannot be deferred.

```jsonc
{
  "formatter": {
    "indentStyle": "space"    // or "tab" — Biome defaults to "tab"
  }
}
```

**Note**: Biome defaults to `"tab"`, unlike Prettier which defaults to spaces. If migrating from Prettier, set `"indentStyle": "space"` explicitly.

**Rationale**: This is a project-level decision made once. Both are valid; the project uses spaces. The choice has no correctness implications — only consistency matters (Biome formatter options docs).

---

## ID-04: `indentWidth` — Spaces Per Level

**Strength**: SHOULD

**Summary**: Number of spaces (or tab-stop width) per indent level. Default is `2`.

```jsonc
{
  "formatter": {
    "indentWidth": 2    // default; 4 is also common
  }
}
```

**Rationale**: 2 is the JavaScript community standard and Biome's default. 4 is common in some codebases. Pick one, configure it, done (Biome formatter options docs).

---

## ID-05: `lineWidth` — Maximum Line Length

**Strength**: SHOULD

**Summary**: Maximum characters per line before Biome wraps. Default is `80`.

```jsonc
{
  "formatter": {
    "lineWidth": 100    // default is 80; 100 and 120 are common alternatives
  }
}
```

**Per-language override**: JS files can have a different line width from JSON:
```jsonc
{
  "formatter": { "lineWidth": 100 },
  "javascript": { "formatter": { "lineWidth": 120 } }
}
```

**Rationale**: 80 is the historical standard. 100 is a common modern choice that accommodates longer function signatures and template literals. 120 is for wide monitors. The formatter wraps when a line would exceed this width (Biome formatter options docs).

---

## ID-06: `lineEnding` — LF, CRLF, or CR

**Strength**: CONSIDER

**Summary**: Controls line endings in formatted output. Default is `"lf"`.

```jsonc
{
  "formatter": {
    "lineEnding": "lf"    // "lf" (Unix/Mac), "crlf" (Windows), "cr" (rare)
  }
}
```

**Rationale**: `"lf"` is the standard for all modern projects. Only change to `"crlf"` if the project must produce Windows-native line endings. Configure `core.autocrlf=false` and `core.eol=lf` in Git to prevent CRLF from entering the repo (Biome formatter options docs).

---

## ID-07: `quoteStyle` — Double or Single Quotes

**Strength**: SHOULD

**Summary**: Controls which quote character Biome uses for strings. Default is `"double"`.

```jsonc
{
  "javascript": {
    "formatter": {
      "quoteStyle": "double"    // or "single"
    }
  }
}
```

**Note**: This goes under `javascript.formatter`, not the top-level `formatter`. Placing JS-specific options at the wrong level is a common configuration mistake.

**Rationale**: Double quotes are Biome's default and match JSON (which only allows double quotes). Single quotes are preferred by some teams for visual distinction from HTML attributes. Either is fine — pick one (Biome formatter options docs).

---

## ID-08: `semicolons` — Always or As Needed

**Strength**: SHOULD

**Summary**: Controls whether Biome adds semicolons at the end of statements. Default is `"always"`.

```jsonc
{
  "javascript": {
    "formatter": {
      "semicolons": "always"    // or "asNeeded"
    }
  }
}
```

**`"always"`**: Adds semicolons everywhere. No ASI surprises.
**`"asNeeded"`**: Omits semicolons where ASI is safe. Adds defensive semicolons before `(`, `[`, and `` ` `` at the start of a line.

**Rationale**: `"always"` is the safer default — it eliminates all Automatic Semicolon Insertion edge cases. `"asNeeded"` is a valid style choice for teams comfortable with ASI rules. The project uses `"always"` (Biome formatter options docs).

---

## ID-09: `trailingCommas` — All, ES5, or None

**Strength**: SHOULD

**Summary**: Controls whether Biome adds trailing commas in multi-line structures. Default is `"all"`.

```jsonc
{
  "javascript": {
    "formatter": {
      "trailingCommas": "all"    // or "es5" or "none"
    }
  }
}
```

**`"all"`**: Trailing commas in function parameters, arguments, array/object literals — everywhere the language allows.
**`"es5"`**: Trailing commas in arrays and objects only (not function parameters).
**`"none"`**: No trailing commas anywhere.

**Rationale**: Trailing commas produce cleaner diffs — adding an element doesn't modify the previous line. `"all"` is the most diff-friendly option and Biome's default (Biome formatter options docs).

---

## ID-10: `arrowParentheses` — Always or As Needed

**Strength**: CONSIDER

**Summary**: Controls whether single-parameter arrow functions get parentheses. Default is `"always"`.

```jsonc
{
  "javascript": {
    "formatter": {
      "arrowParentheses": "always"    // (x) => x * 2
      // "asNeeded"                   //  x  => x * 2
    }
  }
}
```

**Rationale**: `"always"` is consistent — every arrow function looks the same regardless of parameter count. `"asNeeded"` saves two characters per single-param arrow. This is a Prettier-legacy option; Biome keeps it for migration compatibility (Biome formatter options docs).

---

## ID-11: `bracketSpacing` — Spaces Inside Object Braces

**Strength**: CONSIDER

**Summary**: Controls spaces between braces and content in object literals. Default is `true`.

```js
// bracketSpacing: true (default)
const obj = { a: 1, b: 2 };

// bracketSpacing: false
const obj = {a: 1, b: 2};
```

**Rationale**: `true` is the dominant convention. This is another Prettier-legacy option (Biome formatter options docs).

---

## ID-12: 97%+ Prettier Compatibility

**Strength**: SHOULD

**Summary**: Biome's output matches Prettier's in 97%+ of cases. Migration produces minimal diffs.

**Migration process**:
1. Run `biome migrate prettier --write` (see `13-biome/01-setup.md` ID-21)
2. Run `biome format --write`
3. Diff against the previous Prettier output
4. Review against the documented divergences (ID-13) — expected diffs are not bugs

**Important**: Differences that appear only with Prettier's `typescript` parser (not `babel` or `babel-ts`) are classified as Prettier bugs, not Biome incompatibilities.

**Rationale**: Biome achieved 97%+ compatibility through the formal Prettier Challenge. The remaining differences are intentional design decisions documented in ID-13 (Biome Prettier compatibility docs).

---

## ID-13: Intentional Divergences from Prettier

**Strength**: SHOULD

**Summary**: Biome intentionally differs from Prettier in a small number of documented cases. These are design decisions, not bugs.

**Divergence 1 — ES2015+ identifier unquoting**:
```js
// Prettier (keeps quotes — only unquotes ES5 identifiers):
const obj = { "𐊧": true };

// Biome (unquotes all valid ES2015+ identifiers):
const obj = { 𐊧: true };
```
*Biome's position*: The ES5 restriction in Prettier is a legacy limitation. All modern engines support ES2015+ property names.

**Divergence 2 — Computed key parenthesization**:
```js
// Prettier (inconsistent — parenthesizes in objects but not in classes):
a = { [(x = 0)]: 1 };
class C { [x = 0] = 1; }

// Biome (consistent — no parentheses in either):
a = { [x = 0]: 1 };
class C { [x = 0] = 1; }
```
*Biome's position*: Consistency across similar constructs.

Two additional divergences affect **TypeScript only** (trailing commas on arrow type parameters, non-null-asserted optional chains) — irrelevant for this plain-JS project. See the [Biome Prettier divergences docs](https://biomejs.dev/formatter/differences-with-prettier/) for details.

**Rationale**: These divergences are small, intentional, and documented. During migration, expect divergences 1 and 2 in JS diffs — they are not bugs (Biome Prettier divergences docs).

---

## ID-14: Format Suppression — `biome-ignore format: reason`

**Strength**: SHOULD

**Summary**: Suppress formatting for the next syntax node. A reason is required — same as lint suppressions.

```js
// Good — matrix data with intentional alignment
// biome-ignore format: projection matrix must maintain row/column alignment
const projection = [
  (2*n)/(r-l),  0,            (r+l)/(r-l),   0,
  0,            (2*n)/(t-b),  (t+b)/(t-b),   0,
  0,            0,            -(f+n)/(f-n),  -(2*f*n)/(f-n),
  0,            0,            -1,             0,
];

// Good — alignment table
// biome-ignore format: alignment conveys structure
const routes = [
  { path: "/",        handler: home,    auth: false },
  { path: "/login",   handler: login,   auth: false },
  { path: "/admin",   handler: admin,   auth: true  },
];

// Good — file-wide suppression for generated code
// biome-ignore-all format: auto-generated by codegen, do not edit
```

**Syntax**:
- `// biome-ignore format: reason` — suppresses the next syntax node
- `// biome-ignore-all format: reason` — suppresses the entire file (must be at top)

**Rationale**: Suppressed code is printed verbatim. Use for alignment tables, matrix data, ASCII art, and generated files where Biome's reformatting destroys meaningful structure. The mandatory reason connects to Guide 11's documentation discipline (Biome format suppression docs).

**See also**: `13-biome/02-lint-rules.md` ID-18 (lint suppression uses the same syntax)

---

## ID-15: Realistic Suppression Use Cases

**Strength**: CONSIDER

**Summary**: Suppress formatting when visual structure conveys meaning that reformatting would destroy.

**When to suppress**:
- **Matrix/tabular data**: Rows aligned by column for readability
- **Generated files**: Code produced by tools that should not be reformatted
- **Lookup tables**: Key-value pairs aligned for visual scanning
- **Test fixtures**: Intentionally formatted data literals

**When NOT to suppress**:
- Because you prefer a different indent style (configure the formatter instead)
- Because you disagree with how Biome wraps a particular expression (trust the formatter)
- Because the formatted output "looks weird" to you (it looks the same to everyone)

**For entire directories**: Use `files.includes` with `!!` exclusion in `biome.json` rather than per-file suppression:
```jsonc
{ "files": { "includes": ["**", "!!**/generated"] } }
```

**Rationale**: Suppression is for genuine structural meaning — not aesthetic preference. If you're suppressing frequently, the formatter config may need adjustment rather than individual suppressions.

---

## ID-16: Per-Language Formatter Overrides

**Strength**: CONSIDER

**Summary**: Override global formatter options for specific languages using the `<language>.formatter` section.

```jsonc
{
  "formatter": {
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  },
  "javascript": {
    "formatter": {
      "lineWidth": 120,         // wider for JS than global default
      "quoteStyle": "double",
      "semicolons": "always"
    }
  },
  "json": {
    "formatter": {
      "enabled": true,          // or false to skip JSON formatting
      "trailingCommas": "none"  // JSON doesn't support trailing commas
    }
  }
}
```

**Important**: JS-specific options (`quoteStyle`, `semicolons`, `trailingCommas`) must go under `javascript.formatter`, not the top-level `formatter`. Placing them at the wrong level is silently ignored.

**Rationale**: Global options set the project baseline. Language-specific sections override for cases where one language needs different settings — e.g., wider line width for JS, or disabled formatting for JSON (Biome configuration docs).

---

## Best Practices Summary

### Quick Reference Table

| ID | Pattern | Strength | Key Insight |
|----|---------|----------|-------------|
| 01 | Opinionated formatter | SHOULD | Minimal options; zero-debate goal |
| 02 | Configure once | SHOULD | Set options → format-on-save → done |
| 03 | `indentStyle` | MUST | `"space"` or `"tab"` — one decision |
| 04 | `indentWidth` | SHOULD | Default 2; 4 is also common |
| 05 | `lineWidth` | SHOULD | Default 80; 100 and 120 are common |
| 06 | `lineEnding` | CONSIDER | Default `"lf"`; rarely needs changing |
| 07 | `quoteStyle` | SHOULD | `"double"` (default) or `"single"` |
| 08 | `semicolons` | SHOULD | `"always"` (default, safest) or `"asNeeded"` |
| 09 | `trailingCommas` | SHOULD | `"all"` (default, cleanest diffs) |
| 10 | `arrowParentheses` | CONSIDER | `"always"` (default); legacy Prettier option |
| 11 | `bracketSpacing` | CONSIDER | `true` (default); legacy Prettier option |
| 12 | 97%+ Prettier compat | SHOULD | Migration produces minimal diffs |
| 13 | Prettier divergences | SHOULD | Small, intentional, documented |
| 14 | Format suppression | SHOULD | `// biome-ignore format: reason` — mandatory reason |
| 15 | When to suppress | CONSIDER | Structural meaning only; not aesthetic preference |
| 16 | Per-language overrides | CONSIDER | `javascript.formatter` overrides global `formatter` |

### Formatter Options Quick Reference

| Option | Location | Default | Values |
|--------|----------|---------|--------|
| `indentStyle` | `formatter` | `"tab"` | `"tab"` / `"space"` |
| `indentWidth` | `formatter` | `2` | number |
| `lineWidth` | `formatter` | `80` | number |
| `lineEnding` | `formatter` | `"lf"` | `"lf"` / `"crlf"` / `"cr"` |
| `quoteStyle` | `javascript.formatter` | `"double"` | `"double"` / `"single"` |
| `semicolons` | `javascript.formatter` | `"always"` | `"always"` / `"asNeeded"` |
| `trailingCommas` | `javascript.formatter` | `"all"` | `"all"` / `"es5"` / `"none"` |
| `arrowParentheses` | `javascript.formatter` | `"always"` | `"always"` / `"asNeeded"` |
| `bracketSpacing` | `javascript.formatter` | `true` | `true` / `false` |
| `bracketSameLine` | `javascript.formatter` | `false` | `true` / `false` |

---

## Related Guidelines

- **Biome Setup**: See `13-biome/01-setup.md` for `biome.json` creation (ID-06), `biome format` command (ID-13), editor format-on-save (ID-15), Prettier migration (ID-21)
- **Biome Lint Rules**: See `13-biome/02-lint-rules.md` for suppression syntax (ID-18–20) — same `biome-ignore` pattern
- **Task Runner**: See `12-deno/03-task-runner.md` for `biome ci` in the `check` task (ID-07, ID-08)
- **Documentation**: See `11-documentation.md` for "comments explain why" (ID-01) — connects to mandatory suppression reasons

---

## External References

- [Biome — Formatter](https://biomejs.dev/formatter/)
- [Biome — Formatter Options](https://biomejs.dev/reference/configuration/#formatter)
- [Biome — Prettier Differences](https://biomejs.dev/formatter/differences-with-prettier/)
- [Biome — Format Suppression](https://biomejs.dev/formatter/#ignoring-code)
