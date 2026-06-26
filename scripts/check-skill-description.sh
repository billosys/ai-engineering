#!/usr/bin/env sh
# check-skill-description.sh — fail the build when a skill's frontmatter
# `description:` exceeds the platform limit.
#
# The skill loader rejects (or silently truncates) a description longer than
# 1024 characters, so the longest valid description is 1023 chars. Catch it
# here, at build time, instead of discovering it when the skill fails to load.
#
# Usage: check-skill-description.sh <skill-file> [<skill-file> ...]
# Exit:  0 if every description is within the limit; non-zero otherwise.
#
# Handles both an inline scalar (`description: text`) and a YAML block scalar
# (`description: |` followed by indented lines), the two forms used across the
# skills in this repo.
set -eu

MAX=1023

if [ "$#" -lt 1 ]; then
	echo "usage: $0 <skill-file> [<skill-file> ...]" >&2
	exit 2
fi

status=0

for file in "$@"; do
	if [ ! -f "$file" ]; then
		echo "ERROR: $file: no such file" >&2
		status=1
		continue
	fi

	# Label messages with the skill's name as well as its path: many files are
	# just "SKILL.md", so the path alone does not say which skill is failing.
	name=$(sed -n 's/^name:[[:space:]]*//p' "$file" | head -1)
	if [ -n "$name" ]; then
		label="$file ($name)"
	else
		label="$file"
	fi

	len=$(awk '
		# Frontmatter must open on line 1 with a bare "---".
		NR == 1 && $0 !~ /^---[[:space:]]*$/ { print "NOFM"; exit }
		NR == 1 { next }

		# Once the closing "---" is seen, ignore the rest of the file.
		fmend { next }
		/^---[[:space:]]*$/ { fmend = 1; next }

		# Block-scalar body: blank line, then any indented line (dedent 2).
		inblock && /^[[:space:]]*$/ { d = d "\n"; next }
		inblock && /^[[:space:]]/   { line = $0; sub(/^  /, "", line); d = d line "\n"; next }
		# A dedented line ends the block; fall through to re-classify it.
		inblock { inblock = 0 }

		# description: |   (or >)  — block scalar follows on indented lines.
		/^description:[[:space:]]*[|>]/ { inblock = 1; have = 1; next }
		# description: text          — inline scalar on this line.
		/^description:/ { line = $0; sub(/^description:[[:space:]]*/, "", line); d = line; have = 1; next }

		END {
			if (bad)   { print "NOFM";   exit }
			if (!have) { print "NODESC"; exit }
			print length(d)
		}
	' "$file")

	case "$len" in
		NOFM)
			echo "ERROR: $file: no YAML frontmatter (file must start with '---')" >&2
			status=1
			continue
			;;
		NODESC)
			echo "ERROR: $label: frontmatter has no 'description:' field" >&2
			status=1
			continue
			;;
	esac

	if [ "$len" -gt "$MAX" ]; then
		echo "ERROR: $label: description is $len chars (max $MAX)" >&2
		status=1
	fi
done

exit "$status"
