#!/usr/bin/env sh
# Retain the repository's 1023-character packaging policy. Codex's aggregate
# catalog budget is separate; use skill-descriptions live to observe truncation.
set -eu
exec sh "$(dirname -- "$0")/skill-descriptions" audit --max-chars 1023 "$@"
