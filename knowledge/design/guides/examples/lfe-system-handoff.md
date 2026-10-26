# LFE semantic mode migration handoff

This worked handoff records the bounded change from the LFE design-practice
source before and after Slice06. It is an example of carrying an owned
semantic change between maintainers; it is not a full copy of the LFE site,
an export format, or authorization to publish or deploy the site.

Use [Migrate a Semantic Design System Between Owners](../system-migration.md)
for the general recipe and [Semantic system evolution](../system-evolution.md)
for the preceding owner, mode and consumer analysis. The accepted mode study is
recorded as a small rendered-value witness in that method; it is not a complete
site package. For a concise text route, see [Using the skill: supplied identity](../using-the-skill.md#supplied-identity).

For this handoff, local CC authors the D3 implementation and root performs
independent review. The adopting LFE maintainer owns any future rollout and
consumer decisions. The Operator retains authority over external integration,
publication and deployment; no human maintainer or live rollout is appointed
by this example.

## Ownership and resolved contract

The LFE site owns its CSS tokens and its mode values. The ordinary link and
general focus roles are public names consumed by the site; this migration
keeps both names. The new `--lfe-interactive-accent` semantic-intent token is
owned by the ordinary interactive system and has an opaque sRGB color value in
each mode. The established link and focus roles alias that token within their
own mode scopes. The code component keeps its separate link and focus roles.
Equal gold values do not make those roles interchangeable.

| Scope and role | Before: declaration and resolved value | After: declaration and resolved value | Owner, consumer, and migration decision |
|---|---|---|---|
| Light `--lfe-link` | `#705406` → `#705406` | `var(--lfe-interactive-accent)` → `#624900` | LFE ordinary links, including the inline “bread and butter” homepage link; keep the established role name and bind it to the local accent. |
| Light `--lfe-focus` | `#705406` → `#705406` | `var(--lfe-interactive-accent)` → `#624900` | LFE general `:focus-visible` outline; keep the established role name and bind it to the same local accent. |
| Light `--lfe-interactive-accent` | absent | `#624900` → opaque sRGB `#624900` | New semantic-intent token owned by the ordinary interactive system; the existing link and focus roles alias it locally in light mode. |
| Dark `--lfe-link` | `#e9ca66` → `#e9ca66` | `var(--lfe-interactive-accent)` → `#f0d477` | LFE ordinary links, including the inline homepage link; local dark-scope resolution keeps mode propagation explicit. |
| Dark `--lfe-focus` | `#e9ca66` → `#e9ca66` | `var(--lfe-interactive-accent)` → `#f0d477` | LFE general `:focus-visible` outline; local dark-scope resolution keeps mode propagation explicit. |
| Dark `--lfe-interactive-accent` | absent | `#f0d477` → opaque sRGB `#f0d477` | Same semantic-intent token with its own dark-scope value; the existing roles alias it locally. |
| Both modes: `--lfe-code-link`, `--lfe-code-focus` | explicit `#e9ca66` | explicit `#e9ca66` | Code component owner; the Simple Types/code-description link and keyboard outline retain their existing value on `#1e293b`. This is an intentional exception, not a missed replacement. |

Only the ordinary link/focus roles and their new mode-scoped semantic-intent
token changed. Link hover remains `#533e04` light and `#f6d977` dark; visited
remains `#694c77` light and `#d6b4e6` dark. Action fills and their text remain
`#e2ba35`/`#282311` light and `#e4bf4b`/`#252014` dark, with hover fills
`#f0cb53` light and `#f6d977` dark. Assets, fonts, content and URLs are
unchanged. These are boundaries of this migration, not a claim that every
rendering state or asset was revalidated in S07.

The before and after columns show declarations and resolved values. The CSS
projection below includes only the declarations changed by the migration and
the existing utility mappings that continue to expose the public roles. It is
not a complete token inventory: it omits the rest of the cascade, generated
selectors, assets, other rendering conditions, component behavior and site
content. The source keeps the established names; no role is renamed, retired
or deprecated.

### CSS implementation projection

Before (the pinned pre-migration source):

```css
:root {
  --lfe-link: #705406;
  --lfe-focus: #705406;
  --lfe-code-link: #e9ca66;
  --lfe-code-focus: #e9ca66;
}

.dark {
  --lfe-link: #e9ca66;
  --lfe-focus: #e9ca66;
  --lfe-code-link: #e9ca66;
  --lfe-code-focus: #e9ca66;
}

@theme inline {
  --color-lfe-link: var(--lfe-link);
  --color-lfe-focus: var(--lfe-focus);
}
```

After (the accepted source):

```css
:root {
  --lfe-interactive-accent: #624900;
  --lfe-link: var(--lfe-interactive-accent);
  --lfe-focus: var(--lfe-interactive-accent);
  --lfe-code-link: #e9ca66;
  --lfe-code-focus: #e9ca66;
}

.dark {
  --lfe-interactive-accent: #f0d477;
  --lfe-link: var(--lfe-interactive-accent);
  --lfe-focus: var(--lfe-interactive-accent);
  --lfe-code-link: #e9ca66;
  --lfe-code-focus: #e9ca66;
}

@theme inline {
  --color-lfe-link: var(--lfe-link);
  --color-lfe-focus: var(--lfe-focus);
}
```

`@theme inline` is shown because it is the existing Tailwind mapping for the
two ordinary public roles; it remains unchanged. This projection is semantic
Markdown plus a CSS subset. It does not claim DTCG compatibility, conversion,
or a lossless round trip between token formats.

## Adoption, review and rollback

For a future change, the LFE site owner first checks the source modes and actual
rendered consumers, then names the role, alias, owner, scope and component
exceptions. Keep changes to the smallest owned role set. Rebuild with the
site's existing tooling, inspect the relevant native mode and keyboard states,
and review the source and generated result together before integrating the
task branch. A local task-branch integration is not main-branch integration,
public publication, or deployment authorization.

The accepted Slice06 evidence found that ordinary inline links and general
native focus resolve to `rgb(98, 73, 0)` in light mode and
`rgb(240, 212, 119)` in dark mode. The Simple Types code-tab focus outline
remains `rgb(233, 202, 102)` and is the native code-component focus witness.
The code-description link selector was source-inspected; the accepted
four-panel comparison also observed the unchanged code-link value on its
stated panel content. Do not read that as a separate native Simple Types link
interaction. The native checks used keyboard interaction, including
return-to-comparison focus on `#top`; the preserved English `dir="rtl"` check
at 390px was a layout diagnostic, not a language or script test. These are
retained Slice06 observations, not a new browser run.
They do not establish assistive-technology behavior, forced-colour behavior,
native zoom, other browser engines, participant research or conformance.

The source pins are W3 before `dea8dde5eaa93a2c5d707c27840b7d6123931cf4`
and accepted after `63a2a5bd37871f7c99ce6139c5d2bf526984bca5` on
`tailwind/site.css`. The pinned before-source SHA-256 is
`ff92b05cfbaa144f06cc8a244745e39c076555c564e966479bd0a3b8fc2ce3bc`; the
after-source SHA-256 is
`f387d6b69cb15592429e0a6b044f3241fddce20d9a31f69bbbe3c99d646e7ae7`; its
generated `src/css/site.css` SHA-256 is
`d50b8aa7b759fd92abbb9d18f03f56d8634599b62dee44c99d8e1a41da8e74cf`.
These hashes identify retained Slice06 inputs; S07 did not rebuild or modify
W3.

Rollback is a narrow source edit: restore the prior `--lfe-link` and
`--lfe-focus` values in each affected mode, and remove the new alias only after
checking that no later accepted change uses it. Preserve the code-specific
values and unrelated declarations, then run the existing build and review the
result. A historical baseline is evidence for that earlier state, not
permission to overwrite later work. Do not use broad literal replacement,
`git reset` or `git clean` as a migration procedure. An in-memory reversal used
to compare representations is only a check; it does not execute rollback.

The separate library-visit form remains a fictional example; this change does
not alter its recovery behavior or establish a service policy. If a real
service later retires a saved-draft reader, its service owner must first
communicate and disposition existing drafts through a recovery/clear route or
an agreed migration, expiry or disposal path. A global gold replacement would
erase the code-component exception; removing a real draft reader can strand
saved work even when a replacement form still submits. Both choices violate
the ownership and handoff boundary.

The migration adds no converter or tool-specific schema. A semantic table and
CSS projection can communicate these roles and values, but cannot preserve
every cascade relationship, generated selector, asset, mode, interaction or
implementation-specific detail. A receiving team must compare the projection
to its own source and rebuild with its own existing tools before adopting it.
