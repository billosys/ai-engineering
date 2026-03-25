#!/usr/bin/env python3
"""
Build the biome-js-linter skill from extracted rules JSON.

Filters to pure JS/ECMAScript rules only — no React/JSX, Next.js, Vue, Qwik,
Node.js, CSS, GraphQL, or HTML-specific rules. Then re-organizes into
categories that make sense for pure JS development.
"""

import json
import re
from pathlib import Path


# Rules to exclude by name pattern (framework/runtime/non-JS specific)
EXCLUDE_PATTERNS = [
    # React / JSX
    r"(?i)jsx",
    r"(?i)react",
    r"(?i)children",  # useChildrenProp etc.
    r"(?i)dangerously",  # noDangerouslySetInnerHtml
    r"(?i)fragment",  # useFragmentSyntax
    r"(?i)hook",  # React hooks rules
    # Next.js
    r"(?i)next",
    r"(?i)img.?element",  # noImgElement (Next.js specific)
    r"(?i)head.?element",  # noHeadElement (Next.js)
    r"(?i)document",  # noDocumentImportInPage etc.
    r"(?i)polyfill",  # noUnwantedPolyfillio
    # Vue
    r"(?i)vue",
    # Qwik
    r"(?i)qwik",
    # Svelte
    r"(?i)svelte",
    # CSS specific
    r"(?i)css",
    r"(?i)specificity",
    r"(?i)font",
    r"(?i)color(?!less)",  # CSS color rules but not "colorless"
    r"(?i)important.?style",
    r"(?i)shorthand.?property",  # CSS shorthand
    # GraphQL
    r"(?i)graphql",
    # HTML / DOM specific (not JS language)
    r"(?i)aria",
    r"(?i)a11y",
    r"(?i)tabindex",
    r"(?i)alt.?text",
    r"(?i)blank.?target",
    r"(?i)semantic.?element",
    r"(?i)redundant.?role",
    r"(?i)label.?without",
    r"(?i)header.?scope",
    r"(?i)interactive",
    r"(?i)autofocus",
    r"(?i)focusable",
    r"(?i)anchor",  # HTML anchor rules
    r"(?i)iframe",
    r"(?i)media",  # media elements
    r"(?i)distracting",  # noDistractingElements
    r"(?i)svg",
    r"(?i)unknown.?attribute",  # HTML attributes
    r"(?i)access.?key",  # noAccessKey (HTML)
    r"(?i)image.?size",  # useImageSize (HTML img)
    r"(?i)script.?url",  # noScriptUrl (HTML)
    r"(?i)unique.?element",  # useUniqueElementIds (HTML)
    r"(?i)autocomplete",  # useValidAutocomplete (HTML)
    r"(?i)inline.?style",  # noInlineStyles (HTML/JSX)
    r"(?i)leaked.?render",  # noLeakedRender (JSX)
    r"(?i)element.?id",  # HTML element IDs
]

# Specific rule names to exclude (caught individually)
EXCLUDE_NAMES = {
    # DOM / Browser API specific (not language-level)
    "noDocumentCookie",
    "noDocumentImportInPage",
    "noAlert",
    "noConsole",  # debatable but it's a browser/node API, not language
    "noGlobalEval",  # keeping this — eval is language-level
    # Node.js specific
    "noCommonJs",  # CJS is Node-specific
    "noNodejsModules",
    "noProcessEnv",
    # CSS
    "noImportantStyles",
    "noDuplicateProperties",
    "noDescendingSpecificity",
    "noUnknownAtRules",
    "noMissingGenericFamilyKeyword",
    "noDuplicateFontNames",
    "noInvalidPositionAtImportRule",
    "noUnknownFunction",
    "noUnknownMediaFeatureName",
    "noUnknownProperty",
    "noUnknownPseudoClass",
    "noUnknownPseudoElement",
    "noUnknownUnit",
    "noValueAtRule",
    "useConsistentCurlyBraces",
    "useGenericFontNames",
    "useShorthandAssign",
    # React-specific but not caught by patterns
    "useHookAtTopLevel",
    "useExhaustiveDependencies",
    "noChildrenProp",
    "noRenderReturnValue",
    "noStringRefs",
    "noUnusedState",
    "noVoidElementsWithChildren",
    "noDirectMutationState",
    "noFindDOMNode",
    "useButtonType",
    "useKeyWithClickEvents",
    "useKeyWithMouseEvents",
    "useValidAnchor",
    "useValidAriaProps",
    "useValidAriaRole",
    "useValidAriaValues",
    "useAriaActivedescendant",
    "useAriaPropsForRole",
    "useAriaPropsSupportedByRole",
    "useIframeTitle",
    "useMediaCaption",
    "useValidLang",
    "noSvgWithoutTitle",
    "noNoninteractiveElementToInteractiveRole",
    "noNoninteractiveTabindex",
    "noInteractiveElementToNoninteractiveRole",
    "noAutofocus",
    "noHeaderScope",
    "noBlankTarget",
    # JSX/HTML-specific that slipped through name patterns
    "noCommentText",
    "noDuplicateAtImportRules",
    "noDuplicateAttributes",
    "noDuplicatedSpreadProps",
    "noImplicitBoolean",
    "noJsxLiterals",
    "noNestedComponentDefinitions",
    "noNextAsyncClientComponent",
    "noReactForwardRef",
    "noReactPropAssignments",
    "noReactSpecificProps",
    "noRedundantAlt",
    "noRestrictedElements",
    "noSolidDestructuredProps",
    "noStaticElementInteractions",
    "noSuspiciousSemicolonInJsx",
    "useImageSize",
    "useQwikClasslist",
    "useReactFunctionComponents",
    "useSelfClosingElements",
    "useValidAnchor",
    "useFocusableInteractive",
    "noBeforeInteractiveScriptOutsideDocument",
    # TypeScript-only type system rules (keeping TS syntax rules that apply to JS too)
    "noExplicitAny",
    "noInferrableTypes",
    "useEnumInitializers",
    "noConfusingVoidType",
    "noVoidTypeReturn",
    "noMisleadingInstantiator",
    "useConsistentMemberAccessibility",
    "noEmptyInterface",
    "useInterfaceDeclaration",  # TS-specific
    "noExtraNonNullAssertion",
    "noNonNullAssertion",
    "useAsConstAssertion",
    "useExplicitType",  # TS-specific
    "noTypeOnlyImportAttributes",  # TS-specific
    "noUnnecessaryTypeAssertion",  # TS-specific
    "noNamespace",  # TS-specific
    "useConsistentTypeExports",  # TS-specific
    "useImportType",  # TS-specific
    "useExportType",  # TS-specific
}

# Also exclude if description mentions these
EXCLUDE_DESC_PATTERNS = [
    r"(?i)\breact\b",
    r"(?i)\bjsx\b",
    r"(?i)\btsx\b",
    r"(?i)next\.js",
    r"(?i)\bvue\b",
    r"(?i)\bcss\b",
    r"(?i)\bgraphql\b",
]


def is_pure_js(rule: dict) -> bool:
    """Return True if the rule is pure JS/ECMAScript (no frameworks, no TS types)."""
    name = rule["name"]
    desc = rule.get("description", "")

    # Check explicit exclusion list
    if name in EXCLUDE_NAMES:
        return False

    # Check name patterns
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, name):
            return False

    # Check description patterns
    for pat in EXCLUDE_DESC_PATTERNS:
        if re.search(pat, desc):
            return False

    # Exclude a11y category entirely
    if rule.get("category") == "a11y":
        return False

    return True


# Re-organize into JS-focused categories
JS_CATEGORIES = {
    "bugs": {
        "title": "Bugs & Correctness",
        "description": "Rules that catch real bugs — wrong assignments, unreachable code, broken control flow, incorrect operations.",
        "source_categories": ["correctness"],
    },
    "pitfalls": {
        "title": "Pitfalls & Suspicious Patterns",
        "description": "Patterns that are likely wrong or unintended — potential typos, dubious comparisons, misused operators, debug leftovers.",
        "source_categories": ["suspicious"],
    },
    "style": {
        "title": "Style & Idioms",
        "description": "Code style consistency — naming, syntax preferences, modern idioms, cleaner expressions.",
        "source_categories": ["style"],
    },
    "simplification": {
        "title": "Simplification",
        "description": "Rules that flag unnecessarily complex code — redundant wrappers, verbose patterns, over-engineering.",
        "source_categories": ["complexity"],
    },
    "performance": {
        "title": "Performance",
        "description": "Rules that catch performance anti-patterns — O(n^2) patterns, blocking operations, unnecessary allocations.",
        "source_categories": ["performance"],
    },
    "security": {
        "title": "Security",
        "description": "Rules that prevent security vulnerabilities — eval(), hardcoded secrets.",
        "source_categories": ["security"],
    },
    "experimental": {
        "title": "Experimental",
        "description": "Rules under evaluation (Biome nursery). Not recommended by default — enable individually if useful.",
        "source_categories": ["nursery"],
    },
}


def format_code_block(code: str) -> str:
    """Format a code block as JS."""
    if not code:
        return ""
    return f"```js\n{code}\n```"


def build_reference(title: str, description: str, rules: list[dict]) -> str:
    """Build a reference markdown file."""
    recommended = [r for r in rules if r["recommended"]]
    optional = [r for r in rules if not r["recommended"]]

    lines = [
        f"# {title}",
        "",
        description,
        "",
        f"**{len(recommended)} recommended** | **{len(optional)} optional**",
        "",
    ]

    def write_rule(rule: dict) -> list[str]:
        out = []
        out.append(f"### {rule['name']}")
        out.append("")
        if rule["description"]:
            out.append(rule["description"])
            out.append("")
        if rule["invalid"]:
            out.append("**Don't:**")
            out.append(format_code_block(rule["invalid"]))
            out.append("")
        if rule["valid"]:
            out.append("**Do:**")
            out.append(format_code_block(rule["valid"]))
            out.append("")
        out.append("---")
        out.append("")
        return out

    if recommended:
        lines.append("## Recommended Rules")
        lines.append("")
        for rule in recommended:
            lines.extend(write_rule(rule))

    if optional:
        lines.append("## Optional Rules")
        lines.append("")
        for rule in optional:
            lines.extend(write_rule(rule))

    return "\n".join(lines)


def main():
    with open("sources-md/biome/extracted-rules.json") as f:
        data = json.load(f)

    # Flatten all rules
    all_rules = []
    for cat_rules in data["categories"].values():
        all_rules.extend(cat_rules)

    # Filter to pure JS
    js_rules = [r for r in all_rules if is_pure_js(r)]

    print(f"Total extracted: {len(all_rules)}")
    print(f"Pure JS rules: {len(js_rules)}")
    print()

    out_dir = Path("skills/biome-js-linter/references")
    out_dir.mkdir(parents=True, exist_ok=True)

    total_rules = 0
    for cat_key, cat_info in JS_CATEGORIES.items():
        # Gather rules from source categories
        cat_rules = [
            r for r in js_rules
            if r["category"] in cat_info["source_categories"]
        ]
        if not cat_rules:
            continue

        content = build_reference(
            cat_info["title"],
            cat_info["description"],
            cat_rules,
        )
        out_file = out_dir / f"{cat_key}.md"
        with open(out_file, "w") as f:
            f.write(content)

        rec = sum(1 for r in cat_rules if r["recommended"])
        print(f"  {cat_key}: {len(cat_rules)} rules ({rec} recommended)")
        total_rules += len(cat_rules)

    print(f"\nTotal JS rules written: {total_rules}")


if __name__ == "__main__":
    main()
