#!/usr/bin/env bash
# count-patterns.sh — count graded patterns / lint rules per knowledge domain,
# and verify the counts claimed in the top-level README.md.
#
# Usage:
#   scripts/count-patterns.sh            # print the count table
#   scripts/count-patterns.sh --verify   # also diff against README claims;
#                                        #   exit 1 on any drift (CI-friendly)
#
# Counting conventions (the same ones the guides are authored to):
#   * Pattern guides:  headings like `## ID-01:`, `### CA-12:`, `## CG-B-03:`
#     — level 2-4 headings bearing an ALL-CAPS, possibly multi-segment ID
#     ending in a number.
#   * Linter guides (biome, deno): level-3 headings that are a single
#     bare rule token, e.g. `### noConstAssign`, `### no-extra-boolean-cast`.
#
# Files named README.md, MERGE_REPORT.md, and CHECKPOINT.md inside guides/
# are bookkeeping, not patterns, and are excluded.

set -euo pipefail
cd "$(dirname "$0")/.."

PATTERN_RE='^#{2,4} [A-Z]{2,}(-[A-Z]+)*-[0-9]+'
RULE_RE='^### [a-zA-Z][a-zA-Z0-9-]*$'

count_patterns() {
    find "knowledge/$1/guides" -name '*.md' \
        ! -name 'README.md' ! -name 'MERGE_REPORT.md' ! -name 'CHECKPOINT.md' \
        -exec cat {} + | grep -cE "$PATTERN_RE" || true
}

count_rules() {
    cat "$1"/*.md | grep -cE "$RULE_RE" || true
}

# readme_claim <row-match> <nth-claim>
# Pull the Nth claimed count out of the README table row whose link text
# matches <row-match>. Only numbers immediately followed by "patterns" or
# "rules" count as claims (so "Go 1.22+" is not a claim). Prints nothing if
# the row or claim is absent.
readme_claim() {
    grep -E "^\| \[$1\]" README.md \
        | grep -oE '[0-9]+ (graded patterns|lint rules|patterns|rules)' \
        | grep -oE '^[0-9]+' \
        | sed -n "${2}p" || true
}

fail=0
printf '%-22s %8s %8s   %s\n' "domain" "counted" "claimed" "status"
printf '%-22s %8s %8s   %s\n' "------" "-------" "-------" "------"

report() {
    local label="$1" counted="$2" claimed="$3"
    local status
    if [ -z "$claimed" ]; then
        status="(not claimed in README)"
        claimed="—"
    elif [ "$counted" = "$claimed" ]; then
        status="OK"
    else
        status="DRIFT"
        fail=1
    fi
    printf '%-22s %8s %8s   %s\n' "$label" "$counted" "$claimed" "$status"
}

verify=${1:-}

# --- pattern-guide domains -------------------------------------------------
report "rust"     "$(count_patterns rust)"    "$(readme_claim 'Rust' 1)"
report "erlang"   "$(count_patterns erlang)"  "$(readme_claim 'Erlang / OTP' 1)"
report "go"       "$(count_patterns go)"      "$(readme_claim 'Go' 1)"
report "js"       "$(count_patterns js)"      "$(readme_claim 'JavaScript / Deno' 1)"
report "cobalt"   "$(count_patterns cobalt)"  "$(readme_claim 'Cobalt' 1)"

# --- linter-rule domains ---------------------------------------------------
report "biome (js-linter)"  "$(count_rules knowledge/biome/guides/js-linter)"  "$(readme_claim 'Biome' 1)"
report "biome (web-linter)" "$(count_rules knowledge/biome/guides/web-linter)" "$(readme_claim 'Biome' 2)"
report "deno lint"          "$(count_rules knowledge/deno/guides)"             "$(readme_claim 'Deno lint' 1)"

# design and tailwindcss carry no numbered-pattern claims; nothing to count.

if [ "$verify" = "--verify" ] && [ "$fail" -ne 0 ]; then
    echo
    echo "DRIFT detected: a README claim no longer matches the counted guides." >&2
    echo "Fix the README (or the guides' headings) before shipping." >&2
    exit 1
fi
