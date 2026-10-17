# Independent final audit — Fennel skill

Reviewer: **fresh fennel_final_audit context** (`/root/fennel_final_audit`), 2026-10-17. Diagnosis only; this reviewer did not author or edit the candidate, change retained upstream files, stage, commit, or close ledgers. Scratch programs and check logs were created only under `/private/tmp/fennel-final-audit/`; this report is the sole planning artifact written by the reviewer.

## Verdict

The candidate substantially fulfills the scoped request: a useful, task-routed Fennel skill with eleven teaching chapters, retained official documentation and meaningful Git history, working packaging, and executable examples. The Fennel/Lua distinctions are generally careful and useful; the Rust influence is structural rather than an imported runtime model. **Complete the three corrections below before reporting the work finished:** distinguish native `__close` cleanup from ordinary `:close`, correct the general upstream copyright attribution, and repair the misleading chapter-map labels. There are **0 Blocker, 0 High, 2 Medium and 1 Low findings**. Passing checks support specific promises; they do not establish universal correctness.

The canonical project and slice plans supplied the design/scope context. The project plan was read first, then the slice plan, both ledgers, project AGENTS.md and root AGENTS.md; collaboration-framework and code-auditing entrypoints plus audit scope/severity guides informed this review. The explicit single-contributor workflow and separately authorized fresh audit govern; no CDC/CRC or further Operator acceptance gate is invented here. Historical cc-prompt.md is not treated as a current multi-contributor gate. The source was frozen while reviewed.

## Candidate and source identities

Repository: `/Users/oubiwann/lab/billosys/ai-engineering`. Implementation HEAD during this audit: `7b20ccc3a7019cfad6f238522314ce8ab70e0a35`. Authored Fennel files are working-tree additions, not yet a committed skill release. Exact candidate identity is the 36-file `artifacts/candidate-manifest.json`, SHA-256 `96d19697965eb5f50c3fde8325069960bca3e38e5d3a68f3ed48f18984b8fde9`; all 36 listed SHA-256 values matched current files during the audit. That manifest includes the skill, history, twelve guides, five provenance files, fourteen retained originals, and three packaging/public-library files.

- Website: `253e9463c2d6a306feecb37237beee303f9714c1` at `https://git.sr.ht/~technomancy/fennel-lang.org`.
- Language/source pin: `9af5e47fa7ddea806544d15507412ddc51bd046d`, Fennel release 1.6.1. Original full clone inspected at `/private/tmp/fennel-skill.ScoawT/fennel-lang.org/fennel`; its HEAD equals this pin.
- Filtered documentation tip: `a9acb3b88012ac923ff9b23c5cf37d9ed6b7cb7c`.
- Unsquashed integration: `c6a089ba8f0809d9147ea60d66e3d78f02bd4792`, parents `4e635bb39b2c6151014b316f45f279d3682416d4` and the filtered tip. Its commit message contains both required assistant trailers.
- Rebuilt zip: `target/skills/fennel-guidelines.zip`, SHA-256 `529347ba47778d9bc3afce9f0bf3959e8dbff6010ed539df7ff285fe30b4072d`. Archive timestamps are build-dependent; the source manifest and individual file bytes identify the reviewed content more robustly.
- Skill authority: `metadata.version: "1.0.0"`; sibling history has matching `## Version 1.0.0` entry. This historical audit names the reviewed version and is not a second skill version authority.

## Scope, map and denominators

Authored reading: **14/14 files** (SKILL.md, sibling history and all twelve guides), **56/56 rule bodies**, **112/112 paired Fennel snippets**, all chapter summaries, routes and additional shell/Lua prose fragments. Strengths: 20 MUST, 27 SHOULD, 3 CONSIDER, 6 AVOID. Every rule's cited Fennel section body and necessary surrounding context was read, rather than checking headings alone. Rule-level map follows below.

Requested upstream reading: **6/6 complete documents, 4,192 lines**: style.md 1–612, values.md 1–150, setup.md 1–241, tutorial.md 1–797, reference.md 1–1920 and macros.md 1–472. These were read in bounded chunks. An early combined read was truncated; subsequent bounded reads covered the entire authored set and six documents, so truncation is not counted as reading.

Supplemental reading: all lua-primer.md, security.md, README.md, rationale.md and LICENSE; from-clojure.md 1–205; api.md 1–295 and 403–605; changelog.md 1–100. **Unread semantic scope:** from-clojure.md 206–512; api.md 296–402 and 606–755; changelog.md 101–723. None of those unread sections supplies a rule's cited claim. All fourteen retained files, including these unread portions, were nevertheless checked byte-for-byte against the pin and through the historical import verifier. Compiler/test code was inspected only for the native-closing finding, not comprehensively audited.

Provenance: all five support files inspected; all 749 commit-map rows exercised against actual Git trees and metadata. Packaging: Fennel changes in Makefile, README.md and docs/skill-library.md inspected; actual rebuilt zip extracted logically and checked, rather than trusting build output alone. Scope excludes unrelated LFE/design/protocol work and any repository-wide language or modernization audit. The aggregate package gate necessarily rebuilt generated bundles, but no unrelated source was changed by this audit.

## Findings

### FEN-001 — Medium — Explain the native closing protocol before enabling it

- **Location:** `knowledge/fennel/guides/07-errors-and-resources.md:103`, `:113–127`; companion runtime advice at `knowledge/fennel/guides/10-lua-interop-and-distribution.md:76–79`.
- **Scale/category:** logical unit; correctness and resource API contract.
- **What's wrong:** ER-04 describes handles exposing `:close`, demonstrates a plain table with that method, then presents `--to-be-closed` as a runtime-target choice without saying it changes the required closing protocol. On Lua 5.5, that same custom handle is not native-closable. Standard file handles work; a general custom `:close` method is insufficient.
- **Failure evidence:** the exact ER-04 GOOD snippet passes in the default mode. Compiling it with `fennel --globals '' --to-be-closed --compile` succeeds, but running the emitted Lua fails the final `state.closed?` assertion. A minimal unprotected specimen reveals the underlying error: `variable 'x' got a non-closable value`. Emitted code contains `local x <close> = a`, with no adaptation of `a.close`. A custom handle given a metatable `__close` passes the native-mode positive test.
- **Upstream corroboration:** the pinned Fennel compiler's `src/fennel/compiler.fnl:879–885,895–897` switches from the macro to native marked bindings; pinned `test/core.fnl:378–386` tests native custom handles using `__close`. The [Lua manual, to-be-closed variables](https://www.lua.org/manual/5.4/manual.html#3.3.8) specifies the metamethod protocol. Retained reference.md:848–865 says native closing does the same thing but omits this distinction: this is an inherited upstream oversimplification, now an actionable omission in the derived teaching. Leave retained reference bytes unchanged.
- **Fix:** qualify the fake-handle example as the default protected-cleanup mode. State that native closing requires Lua 5.4+ **and** the `__close` protocol (or actual native file handles), and link the companion LI-03 warning. Add a native-mode positive `__close` witness and a discriminating `:close`-only rejection check. Medium because enabling a documented build option breaks realistic custom resources even on the stated supported VM; the default example is correct.

Minimal independent reproducer:

```fennel
(let [handle {:close (fn [_self] nil)}]
  (with-open [resource handle] :done))
```

```sh
fennel --globals '' --to-be-closed --compile repro.fnl > repro.lua
lua repro.lua
# variable 'resource' got a non-closable value
```

The passing native counterpart uses `(setmetatable {} {:__close (fn [_self _error] nil)})` as the handle.

### FEN-002 — Medium — Restore the actual general upstream copyright attribution

- **Location:** `knowledge/fennel/guides/00-sources-and-license.md:58–59`; `knowledge/fennel/sources/README.md:95–96`.
- **Scale/category:** package/provenance boundary; attribution accuracy.
- **What's wrong:** both authored provenance accounts say the general MIT material is copyright Phil Hagelberg and contributors. The retained upstream README's general notice instead names **2016–2025 Calvin Rose and contributors**. LICENSE contains the general MIT text without a named copyright holder, so it cannot corroborate the substituted name.
- **Evidence:** `knowledge/fennel/sources/md/README.md:120–121`, verified byte-identical to the pin, states the general author/year notice. Its later lines describe separately attributed files. The derived style attribution to Taylor R. Campbell and Phil Hagelberg at guide00:52–54 correctly matches style.md:596–608; that separate notice should stay.
- **Why it matters:** the shipped source/license guide is the installed consumer's attribution record because source files are excluded from the zip. Misidentifying the upstream general notice compromises the requested source/license provenance even though the correct original remains in the repository. This is an introduced error, not an instruction to repair upstream sources.
- **Fix:** quote or accurately paraphrase the general Calvin Rose and contributors notice with its years and a pinned README link in both authored locations. Keep the actual style.md-specific notice separately attributed, preserve individual-file notices, and rebuild the package. This is a provenance finding, not a legal compliance guarantee.

### FEN-003 — Low — Use chapter names in the guide map

- **Location:** `knowledge/fennel/guides/00-sources-and-license.md:67–77`.
- **Scale/category:** file/wayfinding; clarity and coherence.
- **What's wrong:** every guide's link label and Topic cell repeats that chapter's final rule title, rather than describing the chapter. For example, “Keep recursion in a real tail position” routes to the full Functions and Control Flow chapter, and “Use guards with coherent bindings” routes to Pattern Matching. Links resolve, but the index makes the skill appear much narrower than it is.
- **Why it matters:** a reader choosing what to load from this map cannot discover multiple returns, fn/lambda or general matching from those labels. SKILL.md's separate task routes are accurate, so this is local rather than a broken package.
- **Fix:** replace the eleven map labels with the actual chapter titles and make Topic a short scope description; retain the correct file targets and counts. No upstream semantic change is implicated.

## Full rule/source review map

All source paths in this table are relative to `knowledge/fennel/sources/md/` at the pin above. Numbers are the rule's linked start lines; the actual section bodies and relevant surrounding material were read. “Clean” means no actionable mismatch observed in this defined rule, not proof against every possible input. Every row's two snippets was independently re-executed through the copied author checker; additional prose boundaries are discussed below.

| Rule | Cited source bodies | Review result / distinguishing check |
|---|---|---|
| ID-01 | values:35 Transparency; tutorial:529 strict globals | Clean: lexical dependencies and visible `_G` escape; host allowlists remain contextual. |
| ID-02 | tutorial:86 locals/variables; from-clojure:154 Tables | Clean: immutable binding versus mutable table/aliases; copy example explicitly shallow. |
| ID-03 | tutorial:307 Conditionals; style:393 Specific Forms | Clean: `if` preserves false; effect-oriented `when` is a style default. |
| ID-04 | reference:927 if; style:455 emptiness | Clean: nil/false truth, `next` for actual keys, length caveat. |
| ID-05 | reference:1053 operators; tutorial:552 Gotchas | Clean: special forms are not runtime function values; negative fails for that reason. |
| ST-01 | style:20 parentheses through indentation/line layout | Clean: spaces, alignment, closing-delimiter exceptions and roughly 80 columns remain SHOULD. |
| ST-02 | style:234 Names and punctuation | Clean: predicates, destructive intent, conversion names and Lua export exception. |
| ST-03 | style:382 colon strings; reference:92 string syntax | Clean: notation indicates role without inventing a keyword type. |
| ST-04 | style:397 arrows; reference:1339 threading | Clean: subject-change judgment, first/last insertion, maybe-thread single-value restriction. |
| ST-05 | style:314 comments/docstrings; api:556 metadata | Clean: purpose/contracts, REPL use, default omission and allocation costs. |
| DT-01 | tutorial:192 sequential tables; reference:1087 length | Clean: one-based dense sequences, nil holes, removal shift; sparse maps allowed. |
| DT-02 | tutorial:405 absence; reference:927 truth | Clean: false-preserving defaults and nil field/key semantics. |
| DT-03 | lua-primer:63 Iteration | Clean: `pairs` ordering not guaranteed; deterministic key sorting is explicit. |
| DT-04 | reference:378 destructuring; style:407 field access | Clean: field groups, static/dynamic access and lack of shape validation. |
| DT-05 | reference:1146 comprehensions/accumulation | Clean: nil omission versus false, key/value emission, `&into` mutation. |
| DT-06 | tutorial:552 Gotchas; lua-primer:137 table module | Clean: identity with equality-metamethod qualification, length versus key count. |
| FN-01 | reference:111 fn/lambda through metadata context | Clean: missing/extra args, non-nil required bindings, false accepted, compiler option caveat. |
| FN-02 | reference:885 pick-values; style:417 multi-value hazard | Clean: final/non-final value expansion; table.insert's second calling shape. |
| FN-03 | tutorial:484 varargs; reference:1731 compiler environment | Clean: `...` scope and explicit count; runtime unpack fallback distinguished from macro helpers. |
| FN-04 | reference:962 each/for/while | Clean: inclusive ranges, iterator roles, pre-body `&until`, nil loop result. |
| FN-05 | reference:1408 tail! | Clean in shown ordinary recursion: non-tail negative diagnostic and large positive input. |
| PM-01 | reference:653 pinning; reference:690 match | Clean: case fresh binding versus match implicit pin; explicit pin syntax/context correct. |
| PM-02 | reference:470 case binding patterns | Clean: ordinary non-nil, false accepted, `?` and ignored names include nil. |
| PM-03 | reference:570 table patterns/guards | Clean: partial table shapes and non-table rejection; dense-size caveat avoids sparse-length validation. |
| PM-04 | reference:596 guards/disjunctions | Clean: shared guard bindings; negative diagnostic specifically names absent b. |
| MD-01 | style:470 Modules | Clean: small export table, file-level locals/grouped imports, contextual API restrictions. |
| MD-02 | style:507 module effects; api:148 require | Clean: quiet loading, cache versus lifecycle; examples labelled as factory demonstrations. |
| MD-03 | tutorial:632 relative require through non-init modules | Clean: module name vararg, not filesystem cwd; init/non-init and include constraints explained. |
| MD-04 | style:510 reloading; api:148 cache/reload | Clean: copied function versus same-table field replacement; whole-table replacement explicitly excluded. |
| MD-05 | style:249 Lua names; from-clojure:16 Runtime | Clean: underscore export alias without forcing internal naming; Lua calling contract acknowledged. |
| ER-01 | style:539 errors; tutorial:415 errors | Clean: nil/error values, false success and nil-success discriminator caveats. |
| ER-02 | tutorial:442 protected calls; reference:734 case-try | Clean: pcall success versus operation success; assert nil/false and catch scope accurately explained. |
| ER-03 | reference:734 case-try | Clean: staged value failure, no-catch propagation, unmatched catch nil, no implied exception handling. |
| ER-04 | reference:848 with-open; lua-primer:102 I/O | **FEN-001:** default-mode example correct; native `__close` requirement missing. |
| ER-05 | api:403 view serialization; tutorial:552 Gotchas | Clean: development view, unreadable placeholders, explicit compiler-library dependency. |
| MC-01 | style:557 Macros; macros:75 Details | Clean: spell expansion first, use functions when notation adds no value. |
| MC-02 | reference:1664 Macro gotchas | Clean: once-only evaluation unless repetition intended; changing values/effect count discriminate. |
| MC-03 | macros:179 quoting; macros:250 identifiers/gensym | Clean: gensym safety, quoted-template reliance and explicit exposed names; diagnostic checked. |
| MC-04 | macros:392 macro modules; reference:1510 import-macros | Clean: distinct phases, runtime helpers unavailable, module functions exported then imported as macros. |
| MC-05 | macros:366 module functions in expansions | Clean: hygienic emitted require rather than assumed caller alias; undeclared alias negative checked. |
| MC-06 | macros:231 macrodebug; :340 AST quirks; :431 assert-compile | Clean: diagnostic context, symbol nil, last-position splicing and nested do; extra AST/splice specimens pass. |
| TL-01 | setup:106 AOT; lua-primer:137 unpack | Clean: separate compiler/VM axes and pinning recommendation; older hosts not claimed tested. |
| TL-02 | api:234 compile; tutorial:529 strict globals | Clean: bare CLI/API compile permissive; explicit allowlists enforce checking. |
| TL-03 | reference:1664 repeated evaluation; setup:106 AOT | Clean: boundary/effect tests; compile and emitted-runtime checks kept distinct. |
| TL-04 | style:17 fnlfmt; official fnlfmt usage | Clean: check versus fix, separate semantic proof, retained bytes left unchanged. Tool page is a live supplemental link. |
| LI-01 | reference:1286 methods | Clean: receiver passed explicitly; defining dotted function name inserts no self. |
| LI-02 | tutorial:135 numbers/strings; lua-primer:192 missing APIs | Clean: bytes/codepoints/graphemes distinguished, Lua patterns not regex, utf8 host requirement. |
| LI-03 | reference:1053 operators; :848 native cleanup | Numeric/bitwise qualifications clean; add native protocol cross-reference per **FEN-001**. |
| LI-04 | setup:69 embedding/AOT; api:148 searchers; reference:1427 include | Clean: library versus executable, loader versus AOT, dynamic require fallback and emitted dependencies. |
| LI-05 | reference:1780 sandboxing; api:11 env/compilerEnv; security:29 history | Clean: runtime env example not advertised safe; compilation/macros retain authority risks. |
| AP-01 | from-clojure:154 Tables | Clean: alias mutation, string notation and compile-time operations route back to core. |
| AP-02 | reference:927 if | Clean: zero and empty string truth; explicit emptiness rather than size/presence conflation. |
| AP-03 | reference:885 pick-values; tutorial:484 varargs | Clean: nil cardinality and variadic/error boundaries; does not equate value failure with raised errors. |
| AP-04 | reference:570 table patterns | Clean: extra map fields still match; actual-key guard and implicit pin regression check. |
| AP-05 | reference:1664 Macro gotchas | Clean: effectful macro input and collision/multi-body advice; paired square example discriminates repetition. |
| AP-06 | setup:69 embedding/AOT; api:234 compile | Clean: emitted consumer with intended dependencies; no claim launcher success proves distribution. |

## Commands, results and what they prove

Commands were run from the implementation checkout unless noted. Local executable identities: `/opt/homebrew/bin/fennel` reports `Fennel 1.6.1 on PUC Lua 5.5`; `fnlfmt --version` reports `0.3.2`; `lua -v` reports `Lua 5.5.0`. No formatter installation was needed. `date +%Y.%m.%d` returned `2026.10.17`; `make help` was run before Make validation.

1. **All authored example pairs.** Copied `artifacts/check-examples.py` to `/private/tmp/fennel-final-audit/` and ran `python3 /private/tmp/fennel-final-audit/check-examples.py` without `--format`. This avoids changing source or overwriting the author's evidence. Result: **112/112 passed, 0 failed**. There are 104 strict-compiled executable specimens, each run both through Fennel and emitted Lua (208 runtime invocations), plus 8 compile-negatives. Formatting checked 103 specimens; the intentionally ugly ST-01 BAD and eight negatives are deliberately excluded from that formatting denominator. Its success means those complete examples behave as asserted on this VM; prose, alternate compiler modes, general input domains and host compatibility require separate review.

   Each compile-negative failed for its stated cause, not a parser accident:

   | Specimen | Exit | Discriminating diagnostic |
   |---|---|---|
   | ID-05 BAD | 1 | `tried to reference a special form without calling it` |
   | FN-05 BAD | 1 | `Must be in tail position` |
   | PM-04 BAD | 1 | `unknown identifier: b` |
   | MC-03 BAD | 1 | `macro tried to bind value without gensym` |
   | MC-04 BAD | 1 | `unknown identifier: helper` |
   | MC-05 BAD | 1 | `unknown identifier: numeric` |
   | MC-06 BAD | 1 | `attempt to index a number value (local 'forms')` during macro execution |
   | TL-02 BAD | 1 | `unknown identifier: misspelled-processor` under explicit checking |

2. **Integration checker.** Read its implementation, then copied and ran `check-integration.py` from the scratch directory. **9/9 expected outcomes passed:** runtime module/macro consumer, Lua embedding host, checked bundled AOT compile, clean Lua artifact with `package.path` and `package.cpath` emptied, strict-global rejection, unchecked bare compile, actual module-directory relocation, relocated bundled compile, and clean relocated artifact. The strict-global test expects exit 1; bare compilation is only an emission counterexample, not a runnable success. The checker tests one small consumer, not every dependency shape or VM.

3. **Independent boundary program.** Authored `/private/tmp/fennel-final-audit/boundaries.fnl`, containing 29 runtime assertions and three compiler AST assertions. Executed with `fennel`, strict-compiled it, then executed emitted Lua: both final runs print `boundaries-ok`. Checks include lambda false/extra/nil behavior; final versus non-final return expansion and explicit pick-values cardinality; nil-accepting/ignored/repeated/pinned patterns; partial shapes; catch/no-catch value failures and raised-error propagation; default with-open cleanup and nil-containing result count; AST nil as a symbol; nested final unquote splicing both side effects; and default-versus-explicit API global checks. A separate macrodebug specimen prints its expansion and `macrodebug-ok` without executing the expansion's deliberately raising body.

   **Retained failed/invalid attempts:** the first boundary specimen incorrectly asserted the sparse table `[1 nil 3]` had length 3. It failed in Fennel and emitted Lua, in both compile modes attempted. That was the reviewer's invalid test assumption, consistent with the skill's correct undefined-boundary warning; the specimen was changed to assert the actual stored fields. After correction, default mode passed while native mode failed for the non-closable custom handle, which led to FEN-001. No failure is counted as a passing native-mode result.

4. **Native closing differential.** Exact ER-04 GOOD snippet: default execution exits 0; strict native compile exits 0; native emitted Lua exits 1 because the custom `:close`-only handle is rejected and `state.closed?` remains false. An unprotected minimal specimen exposes `variable 'x' got a non-closable value`; a separate `__close` metatable witness compiles natively and prints `native-protocol-ok`. These distinguish the missing protocol requirement from a syntax/VM-version problem. Fennel compiler/test source and the official Lua manual corroborate the result.

5. **Realistic small implementation exercise.** In `/private/tmp/fennel-final-audit/app/`, used the skill to write `vendor/settings/init.fnl`: parse boolean `key=value` assignments into a fresh table, preserve false, return nil/message on malformed or duplicate options, and serialize deterministically by sorted keys. A consumer asserts false/true values, deterministic text, error returns for invalid boolean/duplicate/malformed input, and fresh result identity. Formatter check, Fennel execution, strict `--require-as-include` compilation and emitted Lua with both loader paths emptied pass (`settings-ok`). No application files entered the repository. The first consumer loop mistakenly bound the `ipairs` index as text; this harness error was noticed, corrected to `[_ text ...]`, and the final consumer and formatter checks rerun. The earlier apparent negative-input success is not relied upon. This exercise supports practical usability for a small module, not broad application coverage.

6. **Import verifier rerun.** `python3 knowledge/fennel/sources/verify-import.py /private/tmp/fennel-skill.ScoawT/fennel-lang.org/fennel .` exits 0: `PASS: 749 commits, 679 selected-path non-merge changes, 7493 historical blobs, 14 current files`. It compares full retained trees, author/committer identities and ISO timestamps, messages, selected non-merge change coverage, current bytes and SHA-256 manifests. It checks filtered-tip ancestry of current HEAD. Its scope does not establish correct Fennel prose, authenticity of rewritten signatures, or original graph topology by itself.

7. **Independent Git relationship checks.** Direct `git show` verified the integration's two parents and trailers. Website README, .gitmodules, Makefile HTML list/`%.html: fennel/%.md` rule and exact gitlink independently establish the six requested pages' real source chain. A separate Python graph check loaded original and filtered `git rev-list --topo-order --reverse --parents` graphs, computed each mapped commit's set of retained ancestors, mapped rewritten IDs back to originals, and compared all 749 sets: all equal. This verifies every retained-commit ancestry relationship, beyond the import verifier's tree/metadata checks. Separate `git log --follow --format= --name-only <pin> -- <file>` checks matched all fourteen retained-path records, including api.md's README.md predecessor. SHA-1 blob identity plus direct current-byte and SHA-256 comparison establish preservation of the selected material; this does not preserve upstream cryptographic signatures on rewritten commits.

8. **Mandatory package gates.** `make check-skills` exits 0. `make check-package-paths` exits 0 after freshly rebuilding all managed zips: **25 source skills, 25 packages, 0 version errors; 25 zips, 402 Markdown files, 0 hard path failures; 596 warnings at 594 unique locations and 3 explicit exceptions**. Warning categories: repo-only/provenance 170, parser false positive 154, bundled-reference 124, sibling-skill-reference 97, example-project path 28, source-clone-reference 23. These aggregate warnings are recorded, not silently turned into a clean repository-wide result. The isolated command `./scripts/check-package-paths --exceptions assets/packaging/path-exceptions.tsv --show-warnings target/skills/fennel-guidelines.zip` returns **14 Markdown files, 0 failures, 0 warnings, 0 exceptions**, 110 external URLs skipped. No exception file was changed.

9. **Independent archive/routing checks.** Python ZipFile inspection found exactly 14 files: entrypoint, one history and twelve guides; no sources directory or hidden dependency. All 79 local Markdown links resolve within the archive. Every chapter's rule heading ID/title sequence exactly matches its summary table: 56/56. All packaged guides and history match candidate bytes. Makefile contains Fennel in package names/install inventory, ALL_SKILL_FILES, PHONY/help, concrete `pack_skill` target, `skills`/`all` aggregate and source-version prerequisites. Public README and skill-library inventory include it. No new source-link exception was needed. `git diff --check -- knowledge/fennel Makefile README.md docs/skill-library.md` exits 0.

Scratch logs/JSON are convenient rerun evidence rather than permanent deliverables. The commands, denominators, important diagnostics, exact identities and verdicts are recorded here so the durable report does not rely on those temporary files surviving.

## Concrete clean checks and coherence observations

- Checked all lexical/table examples and core summaries for Clojure-style persistence assumptions: none; aliasing and shallow copy policy are explicit.
- Checked all optional-value/error examples for loss of false and conflation with nil: no unexplained loss; ER-02 accurately distinguishes pcall status from nil/error values.
- Checked every compile-negative for causal diagnostics: all eight fail as labelled, with no unrelated parser failure.
- Checked matching prose against complete case/match/guard bodies: fresh bindings, implicit/explicit pins, nil acceptance, repeated bindings and partial table shapes are correctly distinguished.
- Checked reload advice for the common whole-table replacement trap: MD-04 explicitly limits its same-table demonstration and warns older table references also become stale.
- Checked macro prose and execution for repeated evaluation, capture, phase confusion, dependency capture, nil AST slots and splicing: no mismatch found in the reviewed default mode. Macrodebug is correctly described as compile-time inspection.
- Checked emitted distribution with loader paths removed and relocated modules: no accidental runtime compiler/source dependency in the tested bundled artifacts.
- Checked licensing/package boundaries: style authors, original style notice, adaptation statement, CC-BY-NC-SA metadata and installed attribution guide are present. FEN-002 concerns the separate general source author notice; no legal sufficiency claim is made.
- Checked versions/owned-tree package inventory: one owning entrypoint authority and one sibling history; source upstream language/changelog versions remain subject matter, not competing skill versions.
- Checked all package-local routes and rule summaries: no broken links or ID mismatches. FEN-003 concerns misleading text, which path validation cannot detect.

The teaching set consistently separates MUST semantic claims from contextual SHOULD style preferences and recommendations. It labels synthetic module factories and host fragments, and explains what BAD examples demonstrate. Deliberate repetition in the anti-pattern chapter provides a useful review index. The scope is a Fennel authoring aid; it appropriately avoids inventing Neovim/LÖVE/TIC-80 API contracts or promising untested LuaJIT support.

Retained upstream errors/oversimplifications are not automatically faults introduced by the skill. For example, tutorial.md's assert description mentions nil but omits false, while the derived ER-02 correctly includes both. The native-closing omission is inherited from reference.md but needs correction in the authored guide because its custom-handle example makes the distinction operational. Preserve all retained upstream bytes and record corrections only in derived guidance/provenance.

## Remaining uncertainty and completion handoff

The full **defined 56-rule set** received body-level source review, example execution and summary/routing inspection. This is exhaustive coverage of that defined set, not exhaustive correctness of Fennel, Lua or all possible uses. Some supplemental document sections remain unread as enumerated above. External pinned URLs were checked as citations against retained local source bodies; the package checker skips external URLs and this audit did not prove every remote fragment renders at SourceHut. The live [fnlfmt usage page](https://git.sr.ht/~technomancy/fnlfmt) corroborates check/fix/source-install commands but is not part of the pinned Fennel source snapshot. The installed CLI itself corroborates the modes.

Runtime checks exercised Fennel 1.6.1, fnlfmt 0.3.2 and PUC Lua 5.5.0. Lua 5.1–5.4, LuaJIT, Fengari, actual embedded hosts, failing close methods and every multi-resource acquisition failure path were not comprehensively executed. Compiler sandbox strength was not penetration-tested; the skill correctly disclaims it as a security boundary. Source import verification establishes selected-document fidelity and retained ancestry, not an upstream signature or release-security audit.

Primary-context handoff: fix FEN-001, FEN-002 and FEN-003; preserve the pinned originals; add the native cleanup differential; re-exercise changed guidance and regenerate/check the package; record each disposition in closing-report.md and finish the single-contributor ledgers once evidence supports their criteria. No source correction or completion decision is made by this reviewer.

## Correction verification — 2026-10-17 12:04 CDT — current audit verdict

Reviewer: the same fresh `fennel_final_audit` context. This appended section supersedes the original requirement to make FEN-001–003 corrections; the original findings, frozen-candidate identities, failure evidence and coverage map above remain unchanged as the historical audit record. **Current verdict: all three findings are resolved in the corrected candidate. No remaining actionable finding was identified in this scoped correction review. The corrected deliverable meets the audited source-preservation, teaching, attribution and package requirements, within the explicit coverage limits above.** This reviewer did not edit source or close ledgers.

### Correction identity and actual change boundary

`artifacts/corrected-candidate-manifest.json` has SHA-256 `a5c94aa94950b27fcebe2dc2407c03cdfe6f7735988b32401233cfa00372910e`. I compared both candidate manifests, verified every corrected file against its recorded hash, and inspected the complete differences in the four changed files. To establish full original-to-current diffs despite the candidate being uncommitted, I reconstructed the previously read original text in scratch files and verified each entire reconstructed file against its original candidate SHA-256 before computing the diff. This confirms the diff boundary rather than relying on the author's list of edits.

Exactly four of the 36 candidate files changed:

| File | Corrected SHA-256 |
|---|---|
| guides/00-sources-and-license.md | `cef13308813817952c1368aafd4d1036f725bfe51da6023960fb181117ef03f4` |
| guides/07-errors-and-resources.md | `273e845b3c72761dc0a22cb6d0fc834b3a7ba4ab67f3a7c1b5efc5df6efd0e55` |
| guides/10-lua-interop-and-distribution.md | `4c0b499b89a4af08c8984a35150e06717f46502aeb23d387664fcef0a55cf90c` |
| sources/README.md | `6686b62ecb1e305b3bef9bdbf3ce020be1a88d667db9d3839611a852079dfc80` |

Paths in this table are relative to `knowledge/fennel/`. The other **32/36 candidate files are unchanged**, including all fourteen retained source originals, the commit map/verifier/manifests, Makefile, public inventory files, entrypoint and sibling history. Only ER-04 and LI-03 rule prose changed; **54/56 rule bodies** retain the exact earlier evidence. All **112/112 code blocks** have the same specimen IDs and SHA-256 values as the initial independently executed examples. The initial source/history audit therefore remains applicable; repeating the entire import and semantic audit was unnecessary.

### Findings dispositions

- **FEN-001 resolved.** ER-04:103 now makes cleanup mode part of the resource contract. ER-04:125–130 explicitly distinguishes protected `:close` from native `__close`, qualifies nil/false, identifies real file handles and limits its fake-handle example to default mode. ER-04:132 adds the pinned upstream native-closing test already inspected in the initial audit. LI-03:76–81 now states the native-protocol condition and routes to the resource chapter. These changes address the reproduced failure without altering retained reference.md or claiming a `:close`-only handle works natively.
- **FEN-002 resolved.** Guide00:58–63 now names 2016–2025 Calvin Rose and contributors and links the pinned README license section. Sources/README:95–102 makes the same correction and explicitly says LICENSE supplies the terms without naming a holder. I compared these statements with the retained README:120–121 and unchanged LICENSE. Style-specific Campbell/Hagelberg attribution and CC-BY-NC-SA adaptation terms remain separately intact.
- **FEN-003 resolved.** Guide00:69–79 now uses each actual chapter's title, accurate pattern count and a meaningful topic description. I programmatically compared all eleven labels against the target chapter headings and counted their rule headings; all eleven match. The scope descriptions were also read for meaning, not merely checked for different strings.

### Independently re-exercised evidence

Copied the current runners into `/private/tmp/fennel-final-audit/corrections/` before executing them, preserving the author's evidence files. `check-examples.py` again returned **112/112 passed, 0 failed**, including all eight causal compile-negative diagnostic checks. Comparison against the first independent run confirms every example's code identity is unchanged.

Read the updated `check-integration.py` rather than treating its new count as proof. Its four additional checks actually select native mode, exercise a metatable `__close` handler after a raised body error, assert the original error and cleanup/error-argument flags, compile strictly and execute emitted Lua, and require a `non-closable` diagnostic from a `:close`-only handle. The independent rerun returned **13/13 expected outcomes**. The native positive launcher and emitted Lua runs both print `native-cleanup-ok`; the close-only rejection exits 1 with `variable 'resource' got a non-closable value`.

I also wrote and ran a separate native-mode specimen beyond the author's runner:

```fennel
(local file (assert (io.tmpfile)))
(with-open [absent nil disabled false resource file]
  (assert (= :file (io.type resource)))
  (assert (= nil absent))
  (assert (= false disabled)))
(assert (= "closed file" (io.type file)))
(print :native-values-ok)
```

`fennel --to-be-closed native-values.fnl` and strict native compilation followed by `lua native-values.lua` both print `native-values-ok` and exit 0. This independently exercises the correction's nil/false and real-file claims on the tested VM; it does not broaden the host-version coverage.

Both mandatory gates were rerun independently on the corrected source: `make check-skills` exits 0; `make check-package-paths` exits 0 with **25 source skills/25 packages, 0 version errors, 25 zips/402 Markdown files, 0 hard path failures**, the same 596 warnings/594 unique locations and three exceptions. The author's completed `artifacts/package-checks-final.log` was inspected and agrees with those final results. External URL count rises to 796 across the aggregate because the correction adds two primary-source citations. No exception file changed.

The isolated Fennel package path check returns **0 failures, 0 warnings, 0 exceptions**, 14 Markdown files and 112 skipped external URLs. Direct archive inspection after the independent rebuild confirms **all 14 files equal corrected source bytes**, no sources directory, and **80/80 working local links** (the added resource-chapter cross-link accounts for the increase from 79). The resulting archive SHA-256 is `ccf647effde82c3db7931f3069e457fd3e959940b74867bc075cf0c88e8d5d52`; as noted above, archive timestamps affect the container hash. The corrected source manifest is the stable content identity.

The primary context preserved five original independent specimen sources under `artifacts/audit-specimens/` (boundaries, native protocol, macrodebug, settings module and its consumer). I verified all five are byte-identical to the final scratch sources used for the initial audit and read their rerun README. Those durable copies improve reconstruction without changing the candidate or turning audit programs into shipped skill dependencies. `git diff --check` remains clean for the scoped candidate paths.

The original remaining-uncertainty section still applies: this follow-up does not claim universal correctness, all-host compatibility, legal assurance, external-link availability or comprehensive closing-failure/coroutine behavior. It resolves the three concrete findings with source checks, discriminating runtime evidence and verified package content. The primary context can now record these dispositions and complete its existing single-contributor completion records.
