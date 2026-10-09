# Proposed portable design contract

Status: Slice01 proposal for CDC/Operator review. This document specifies
intended behavior and downstream source treatment; it does not edit or repair
the installed skill. The approved scope and the proposed teaching language are
kept separate.

## 1. Binding decisions and intended behavior

The Project10 Operator decisions recorded in
`project10-design-foundations/project-plan.md#recorded-operator-decisions`
bind this work:

- Remove Cowboys & Beans (C&B) identity and project-specific material from the
  live skill and package. Do not retain an opt-in C&B profile or case study;
  Git history is the historical source if needed.
- Treat the original C&B coupling as a bug. Removing it requires no
  compatibility bridge, legacy behavior or migration obligation. This does not
  waive version/history requirements or pre-classify unrelated changes.
- Review all 233 baseline cards semantically, with the five dimensions in the
  Project10 full-corpus contract. Anything short of the agreed corpus review is
  a project defect, not an alternate acceptance scope.
- Use `knowledge/design/sources/md/` for Markdown source holdings and preserve
  provenance and originals. Do not infer a bulk source move or conversion.
- Preserve the existing skill's compositional ethos: relationships, content,
  proportion, expressive coherence, fluid web constraints and skilled judgment.

Generic tasks must begin with the user/project's supplied identity, assets and
constraints when available. When identity is absent, the method must not
silently supply C&B values or a new default house style. The installable skill
and the card/source corpus are separate populations: packaging remains the
direct live skill payload, while corpus provenance/review remains project
evidence. The inventory in this slice is not semantic card review.

## 2. Reusable method and adopting-project inputs

A project profile is a short prose/table contract used to explain the relevant
context before styling choices. It is not a serialized schema, required
questionnaire, mandatory intake form, tool, or universal preset. Ask only
questions whose answers could change a consequential decision. Unknown values
stay marked unknown or are offered as explicit, reversible proposals with
reasons and assumptions.

| Profile input | Purpose | Behavior when absent or unknown |
|---|---|---|
| Audience, tasks and content | Establish who is doing what, with which information and actions; distinguish reading, finding, comparing, editing and submitting work. | Ask a consequential question if the task/meaning would change; otherwise state the provisional task/content assumption and continue. Never invent user research. |
| Content and reading conditions | Identify length, hierarchy, language, sequence, density, reference needs and the environment in which content is read. | Preserve known content; state which content/context is assumed. Avoid choosing a layout from a generic page template alone. |
| Existing identity and assets | Preserve supplied name, logo, semantic tokens, typefaces, imagery, components and accepted brand rules. | Do not infer inherited identity from this skill or an example. If none is supplied, label any suggested palette/type direction as a proposal. |
| Platforms, viewports and input modes | Establish web/native/print scope, viewport/container constraints, pointer/touch/keyboard/assistive input and supported environments. | Ask only when platform changes implementation/behavior; otherwise name the assumed target. A breakpoint or media query is allowed when content or behavior requires it. |
| Language, script and direction | Check script coverage, shaping, line breaking, writing direction, localization and text expansion. | Preserve the supplied language; mark untested scripts/directions. Do not claim multilingual support from Latin examples. |
| Accessibility and user preferences | Record applicable standards/targets and preferences such as text enlargement, reduced motion, forced colors, contrast, zoom and focus. | Treat unknown preferences as reasons to keep ordinary browser/user controls available and avoid inaccessible interaction assumptions; do not claim conformance without actual checks. |
| Typography, colour, spacing and token constraints | Record required assets, supported axes, role hierarchy, existing token architecture, contrast pairs, content measure, and fixed or fluid values. | Reuse supplied tokens/assets where they fit. If absent, develop context-specific candidates and test complete pairs and rendered use; do not impose named fonts, colours or a token-layer count. |
| Density, themes and modes | Describe compact/comfortable or other useful density, light/dark/high-contrast modes and the contexts that need them. | Do not infer one density or theme. Propose alternatives only when they serve an identified task or environment. |
| Fixed decisions | Mark requirements that are already decided, owned elsewhere or constrained by policy/implementation. | Do not reopen or silently alter fixed choices; explain a conflict and refer it to its owner. |
| Unknowns and evidence | Keep observations, source evidence, assumptions, preferences and unresolved items distinct, with affected decisions and next checks. | Preserve the unknown and identify its consequence/owner. Lack of evidence does not prove a claim false or true. |

This contract allows a short brief rather than a heavyweight intake. The
profile is a way to make context visible, not a prerequisite to every small
edit. A user-chosen brown, typeface or ratio remains a legitimate project
choice when appropriate; portability removes inherited defaults, not those
values.

## 3. Seven-principle disposition proposals

Candidate wording below follows the seven proposals in the Project09 synthesis,
with the scope corrections required by DES-001–009. Every proposed formulation
remains pending CDC/Operator adoption. “Retain” means preserve the underlying
useful intent, not preserve the current absolute wording.

| Current principle and primary witnesses | Proposed disposition | Candidate portable formulation and claim boundary |
|---|---|---|
| **I. Multiply, Never Add.** `guides/design.md`, “Multiply, Never Add” and “The Deeper Structure”; `guides/layout.md`, “Scale by Ratio, Never by Addition”; `guides/type.md`, “The Mathematics Behind the Scale”. DES-002/003/004. Brown's local `sources/md/posts/more-meaningful-typography.md:310–314` explicitly allows a departure from a scale. | Correct/replace the universal rule. | **Make relationships intentional and legible.** Ratios and arithmetic progressions are mathematical constructions; which one serves a task is a design decision. Scales can suggest coherent values, but fluid interpolation between two geometric scales is not generally geometric at intermediate widths (DES-003), and a scale does not prove perceptual equality or accessibility. Keep generated examples tied to one declared configuration and test endpoints/interior values (DES-004). |
| **II. Perception Is the Only Coordinate System That Matters.** `guides/design.md`, Principle II; `guides/colour.md`, palette rationale; `guides/layout.md`, Utopia and viewport-unit passages; `guides/foundations-of-design.md`, Oklab explanation. DES-002/005/007. | Correct/replace the absolute. | **Evaluate perception in context, across people and conditions.** Choose units/spaces for their stated purpose and test the resulting presentation. OKLCH is a useful approximately perceptual model, not an exact brightness, contrast or harmony oracle. `vi` describes an inline viewport axis; it does not itself guarantee text enlargement. Encoded sRGB linearization and Oklab's nonlinear step prevent the full conversion from being one matrix multiply. Separate measured outcomes, empirical findings and heuristics. |
| **III. Name the Role, Not the Value.** `guides/design.md`, Principle III; `guides/colour.md`, “Semantic Tokens” and “Design Rationale”; `guides/foundations-of-design.md`, “Notation Conventions Converge on Three-Tier Token Architecture”. DES-008. | Retain the useful distinction; correct the universality claim. | **Name design roles and separate them from particular values.** Semantic names can clarify purpose and mappings. Primitive → semantic → optional component aliases are a useful architecture with tradeoffs, not a mandatory three-layer law. DTCG defines a token interchange format, not universal layer count or role meanings; explain differences between source systems and validate actual exports. |
| **IV. Constraint Liberates; Freedom Paralyses.** `guides/design.md`, Principle IV; `guides/layout.md`, “Encode Axioms, Not Artefacts”; `guides/foundations-of-design.md`, developer-mistake prescriptions. DES-002/009. | Correct/replace the universal quantifier. | **Choose constraints that support the task and leave room for judgment.** Constraints can make decisions legible and repeatable. They should be scoped, explained and revised when content, users, platforms or evidence call for it. A finite token set or axiom cannot guarantee good composition; it may need an explicit exception or a different system. |
| **V. Unity Is Not Uniformity.** `guides/design.md`, Principle V; `guides/type.md`, “Same Instruments, Different Music”; `guides/layout.md`, “Design Systems, Not Pages”. DES-001/002/009. | Retain; replace C&B's shared skeleton/values with supplied project identity. | **Preserve coherence while allowing contextual expression.** A project may share selected roles, principles or components while varying values and forms by context. Existing identity has priority; do not require common ratios, palettes, fonts, domains or visual grammar. Distinctiveness must still serve task, content and orientation. |
| **VI. Proximity Carries Meaning; Uniformity Erases It.** `guides/design.md`, Principle VI and absolute spacing rule; `guides/foundations-of-design.md`, “Gestalt Principles Have Computational Formalisations”. DES-002. | Correct the empirical absolutism; retain as a heuristic. | **Use spacing and other grouping cues to communicate structure.** Proximity can signal grouping and should be considered with color, shape, labels, borders, sequence and accessibility. Do not claim it precedes every cue in all cases or require a strict universal intra/inter-group inequality. Evaluate the relation in the actual composition and preserve readable separation. |
| **VII. Design the Invariants, Not the Instances.** `guides/design.md`, Principle VII; `guides/layout.md`, “Encode Axioms” and “Unify Type, Space, and Grid”; `guides/foundations-of-design.md`, token and scale passages. DES-002/003/008/009. | Retain a scoped, testable invariant concept; replace “the system is the design.” | **Define useful invariants, then test the resulting instances.** State what a rule guarantees, for which content, users and environments, and how exceptions are handled. Systems support design judgment; they do not make all combinations correct or remove the need to inspect instances. Treat mathematical identities as identities, measured/empirical claims as scoped evidence, contextual heuristics as heuristics, project conventions as project choices, and analogies as analogies. |

Do not replace one universal preset with another. Preserve sound relationships,
content-led composition, intrinsic layout, optical adjustment and expressive
craft. Remove claims that scientific authority, token naming, or mathematical
regularity automatically yields beautiful, correct or accessible results.

## 4. Eight-file change map

This map covers the eight live files counted by the baseline: entrypoint,
sibling history and six guides. Exact source witnesses were scanned and read in
their surrounding sections; the file/line anchors below are locators for later
source work, not claims of changes made here.

| Live file and current source locations | Required removal/correction and preservation | Portable replacement behavior | Observable later check |
|---|---|---|---|
| `knowledge/design/SKILL.md`: description/stance; guide tables and routes; seven-principle summary; primitive, palette, type, fluid and zero-breakpoint summaries; workflow/checklists. | Remove the C&B promise, brown/three-domain palette, three-font assignments, mandatory perfect-fourth/default scale, “every layout from these primitives,” zero-media-query rule, universal 60ch and cognitive/scientific guarantees. Fix guide links that currently use bare `design.md` etc. Keep the fast task routes, helpful vocabulary and compositional ethos. | Entry point first reads a short brief/profile, preserves supplied identity, routes to relevant guidance and distinguishes a proposal from a requirement. Examples are illustrative and correctly linked. | Fresh generic literary-page task introduces no C&B names, palette or fonts; existing supplied tokens/typeface survive. Route checks resolve from packaged entrypoint. |
| `knowledge/design/version-history.md`: sole sibling change record, currently one history entry. | Preserve one history authority and past Git history. Do not add a C&B profile/case study or reproduce C&B-specific live content in history; describe future changes at a neutral project-scope level. Keep version matching the entrypoint metadata under repository version rules. | Explain the portable correction and meaningful changes without encoding a second profile or duplicate version authority. | Check metadata/history agreement and scan the packaged tree for removed project-specific prescription and competing history/version declarations. |
| `knowledge/design/guides/design.md`: hero/provenance; “Convergence Thesis”; seven principles; deeper structure; tools/technology and coda. | Remove brand-specific governance and deterministic claims that perception/science/algebra compel one style; correct current global statements about geometric scales, proximity, token layers, system universality and matrix conversions. Keep relationships, systems-thinking, meaningful constraints and expressive coherence as useful ideas with limits. | Seven scoped principles accompany examples, counterexamples, claim category/source, applicable context and exceptions. | Each principle has a bounded proposition/witness; a legitimate optical correction and a non-geometric need are allowed; no analogy is labeled proof. |
| `knowledge/design/guides/colour.md`: Brand Brown, warm neutrals, three sites and per-site accents; role mappings and site demos; OKLCH and DTCG rationale. | Remove C&B palette/tokens/domains/site prose and specific hex/OKLCH values as defaults. Correct equal-lightness, three-layer and contrast implications. Preserve the role-based approach, contrast as an evaluated property, palette construction ideas and complete-pair requirement. | Start from provided color roles and identity; propose values only from context. Evaluate actual foreground/background/state combinations, gamut/compositing and contrast; do not treat a color-space value or token role as sufficient proof. | Supplied semantic tokens remain. Chosen palette has explicit complete pair/state checks; no C&B default or blanket ban on independently chosen brown/other hues. |
| `knowledge/design/guides/type.md`: “Three Voices”; named fonts and axes; perfect-fourth scale and fluid examples; three site demos; recommendations and breakpoint/math claims. | Remove Fraunces/Literata/IBM Plex assignments, C&B name/domain samples, fixed ratio/default fonts and unsupported uniform interpolation/legibility claims. Preserve role hierarchy, scale as optional aid, variable-axis explanation where verified, optical adjustment and actual-reading-context considerations. | Choose type by script coverage, reading/task context, hierarchy, available assets/axes, fallbacks and user settings. State configuration, test actual values including negative/interior/endpoints, allow reasoned optical adjustment, and keep functional text readable. | User-supplied typeface and tokens remain; browser font failure and large text do not break sample; generated configuration matches all declared inputs and tested widths. |
| `knowledge/design/guides/layout.md`: C&B identity; all seven precepts; Utopia endpoint configuration; 13 primitives; “no media queries” tests; global measure/axioms; `vi` accessibility claim. | Remove C&B endpoints/ratios as defaults, guarantees that intermediate fluid scales remain geometric, no-breakpoint prohibition, universal 60ch and “axioms produce correct unseen contexts”. Correct text-enlargement claim. Preserve intrinsic layout, composable primitives, content-driven sizing and fluid interpolation as tools. | Start intrinsically, then add container/viewport breakpoints or semantic behavior when task/content/user settings require them. Scope reading measures to prose; name what CSS guarantees and test actual combinations. | Case with dense layout needing a breakpoint and optical adjustment passes; text resize/reflow is checked separately; examples do not rely on a ban on media queries. |
| `knowledge/design/guides/foundations-of-design.md`: research/taxonomy universality; competency question and source breadth; math/Weber/Gestalt claims; cross-domain “rigorous” labels; three-tier/DTCG and responsive-token conventions; source-acquisition table. | Remove unsupported claims of universal curricular/research consensus, source completeness, population-wide truth, one mandatory architecture, and universal scale behavior. Correct the Oklab nonlinear pipeline and label analogies as analogy unless equivalence is established. Preserve useful technical/history material only with exact scope, source, date/edition and current verification. | Present a scoped source register and claim/source boundary; distinguish mathematical identity, empirical evidence, contextual heuristic, project convention and analogy. Name unavailable originals and do not substitute card metadata for them. | Every retained consequential claim has inspectable support and scope; package dates/technical claims refreshed in later source work; no 55-CQ or “30+ sources” promise without reconciled inventory. |
| `knowledge/design/guides/breaking-the-layout-monoculture.md`: CHI homogenization statistic and causal story; CSS support assertions; seven strategies including animation, hover/clip-path and horizontal scroll; site/model examples and references. | Correct the measured interval/metric and do not claim general causal loss of comprehension from banner-blindness work. Remove universally pro-distinctiveness or “breakpoint-free” claims. Preserve editorial variety, wayfinding, spatial zoning and composition examples as optional context-led patterns. | Choose familiar/repeated patterns where they aid recognition and comparison; departures answer a content/task need. Any hover, scroll, transition or lateral interaction retains visible alternatives, keyboard access, reduced-motion behavior, focus and reading order. Check support by target platform. | Five task scenarios keep familiar controls when useful, permit justified adaptation, and reject hover-only/motion-dependent information; browser support is checked for the named target. |

Removing brand words alone is insufficient. The C&B choices also shape the
scale values, semantic token mappings, named font roles, examples, zero-query
tests, site-specific axes and task routes. Generic copy with brown aliases or
the same three-site/three-font/1.333 assumptions would still impose that
identity. The change must remove the coupling in behavior and in the
instructional defaults while retaining useful transferable craft.

## 5. Finding ownership proposal

One primary Project10 arc is assigned per finding for allocation; cross-arc
dependencies are explicit. “Verification” below is later work, not Slice01
completion or a claim that the audit finding is closed.

| Finding | Primary owner; cross-reference | Required downstream outcome | Verification and outstanding input |
|---|---|---|---|
| DES-001 | Arc01 contract; Arc04/05 | Remove the C&B default and preserve existing supplied identity. | Generic and existing-brand fresh-context tasks; inspect entire live payload/package. C&B scope is settled by Operator; wording/profile remains proposed. |
| DES-002 | Arc02 theory; Arc03 accessibility/layout; Arc04/05 | Scope scientific/perceptual claims; allow contextual judgment. | Claim-level source review and counterexamples across the 233-card population and guides. Source availability and claim register required. |
| DES-003 | Arc02 theory | Correct the claim that interpolating two geometric endpoint scales remains geometric. | Reproduce declared intermediate values/ratios for each retained example. Exact example/configuration is pending CDC/Operator choice. |
| DES-004 | Arc02 theory; Arc04 examples | Use one declared configuration and consistent generated values. | Recompute endpoints, negative steps, interior widths, rounding and root-size changes. Example parameters remain proposal. |
| DES-005 | Arc03 accessibility/typesetting; Arc02/05 | Remove `vi`-as-accessibility guarantee; preserve user preferences and test text enlargement separately from reflow. | Actual text-size and reflow specimens at named environments. No browser/AT test was run in this slice. |
| DES-006 | Arc03 accessibility; Arc04/05 | Establish keyboard, focus, semantics, reading-order, motion and complete color-pair floor. | Inspect retained interactive examples against the floor and maintained patterns. Specify runtime/environment and actual token pairs. |
| DES-007 | Arc02 theory/evidence | Correct full sRGB-to-Oklab nonlinear pipeline and scope OKLCH claims. | Check linearization, cube-root and matrices against identified technical source; verify card claims. Original Oklab source is cited in audit; card source claims still need full review. |
| DES-008 | Arc02 theory; Arc04 package | Treat token layers as contextual architecture rather than a universal DTCG rule. | Compare exact source-system generations and validate any actual exported format. Pin current source docs before release. |
| DES-009 | Arc02 layout; Arc03/05 | Use intrinsic layout first while allowing content/behavior/user-preference breakpoints and scoped measure. | Dense-interface case needs and justifies a breakpoint; check content change and target contexts. |
| DES-010 | Arc04 guides/package | Repair package routes, converted markup, examples and declared dependencies. | Build and inspect isolated package; resolve every shipped link/snippet. `make design` and package gates belong to later authorized source work. |
| DES-011 | Arc03 typography; Arc04/05 | Provide transferable type selection/typesetting, axis verification, fallback/loading, script coverage and readable functional examples. | Named fonts/axes and fallback specimen plus large text/missing font checks; broader multilingual scope remains Project11 unless Project10's accepted floor requires it. |
| DES-012 | Arc02 evidence; Arc04/05 | Scope CHI observation and remove unsupported broad causal interpretation. | Obtain/inspect full paper before claims stronger than abstract; compare repeated-layout use by task. Audit records failed PDF retrieval; resolve later. |
| DES-013 | Arc02 evidence; Arc04 package | Add source/claim traceability, accurate source/readiness states and limited installed promise. | Reconcile each source/claim/CQ and population; identify missing Arnheim/Cleland/Tschichold originals and other source snapshots. Slice02 owns acquisition/readiness planning. |
| DES-014 | Arc04 workflow; Project11 capability extension | Add a bounded brief/context route before visual styling and state the 1.5 promise. | Follow fresh brief through question/assumption, relevant guidance, choice and review. Connected research/prototype practice remains Project11. |
| DES-015 | Arc02 full corpus; coordinate Project08 | Review all cards and correct cross-domain errors only with claim-level evidence; keep unavailable originals unresolved. | Complete five-dimension review for every card, track revisions/claims/source spans, preserve Project08 boundaries. Current targeted audit is not a verdict. |
| DES-016 | Arc02 full corpus | Repair literal escapes where normal prose is damaged without blindly decoding legitimate code examples. | Compare before/after text for all affected posts, preserving meaning/provenance; manifest baseline remains denominator. |

## 6. Worked contract cases

These are analytic checks that distinguish the proposed contract from the
existing defaults. They are not model-performance trials.

| Input | Expected decision behavior | Contract clauses exercised |
|---|---|---|
| Generic literary page with no supplied identity | Ask only if a missing audience/task/content answer changes hierarchy or behavior. Otherwise state provisional roles/type/color choices as proposals. Never introduce C&B names, brown palette, Fraunces/Literata/Plex, three sites or their axes. | Binding behavior; audience/tasks, content, identity, unknowns; principle V. |
| Existing interface with supplied semantic tokens and typeface | Preserve the names, mappings and typeface where they serve the task. Explain a correction only when a concrete task/accessibility/technical issue supports it; do not rebrand or replace the user's system to fit a token-layer ideal. | Identity/assets; fixed choices; principle III and V. |
| User independently selects brown and Fraunces | Keep the choices when suitable. Evaluate the actual palette pairs and the typeface's script/reading/fallback fit. Portability means no inherited C&B defaults, not a prohibition on brown or Fraunces. | Identity/assets; typography/colour constraints; principle V. |
| Dense interface needs a breakpoint and optical adjustment | Permit a breakpoint when the content/behavior becomes unclear or unusable at a measured container state. Permit a documented optical departure after applying a scale. Verify the content and interaction at both sides of the threshold. | Platforms/viewports; principle I and IV; layout map; DES-003/009/011. |
| Source/card conflict or unavailable original | Keep both assertions and their provenance, state which comparison could not be performed, distinguish prepared text from original and source support from truth, and name the affected cards plus owner/next evidence. Do not promote a preferred assertion or count quarantined cards as completed review. | Unknowns/evidence; full-corpus decision; source-readiness; DES-013/015; reconciliation boundaries. |

## 7. Unresolved decisions and handoff

Settled: population is 233 cards; C&B-specific live/package behavior is to be
removed, its history is Git-only, no compatibility bridge is required, and
Markdown sources use `sources/md/`. These are not reopening questions.

Proposed, pending CDC/Operator: exact revised principle wording; which small
example configuration is adopted; how much brief/profile guidance belongs in
the 1.5 entrypoint versus an optional route; the final source/claim-register
representation; exact card-to-source locators; and the boundaries of any
retained technical example. This slice's contract table does not settle them.

Slice02 must turn the actual source gaps into acquisition/preparation needs and
a claim-level five-dimension review procedure. It must pin source identity and
edition/snapshot, preserve original/prepared locator relationships, record
which card claims are blocked by each missing source, and define complete
coverage accounting for all 233 cards and repeated guide claims. Missing
sources do not allow reduction of the review population.

Slice03 must compose the accepted portable contract and Slice02 method, resolve
proposed wording/configuration through CDC/Operator, assign every card and
relevant guide claim to Arc02 execution groups without dropped IDs, and preserve
an explicit proposal/decision record. Neither slice silently changes schemas,
rewrites source material or performs the live-skill implementation; those need
their own authorized work.
