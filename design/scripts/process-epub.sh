#!/usr/bin/env bash

SOURCE_FILE=$1
OUTPUT_DIR=$2
mkdir -p "$OUTPUT_DIR"

pandoc \
    "$SOURCE_FILE" \
    --data-dir="$OUTPUT_DIR" \
    --extract-media="$OUTPUT_DIR/media" \
    -o "$OUTPUT_DIR/book.md" \


# Example Usage
: <<'EXAMPLES'

scripts/process-epub.sh \
  /Users/oubiwann/Dropbox/Apps/General Books/Music/[2023] Hutchinson - Music Theory for the 21st-Century Classroom (August 2023).epub \
  sources-md/21st-century-classroom/

EXAMPLES
