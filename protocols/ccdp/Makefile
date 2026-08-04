# Makefile — CCDP RFC assembly.
#
# Builds the ccdp-assembler tool and runs it over the chapter sources in
# src/ to produce composite-cognition-dispatch-protocol.md. Defaults to
# GitHub-Flavored Markdown, the spec's primary home; the kramdown-rfc
# targets below are for feeding the doc to `kramdown-rfc` to produce RFC
# XML/HTML.

.PHONY: ccdp-rfc ccdp-rfc-strict ccdp-rfc-kramdown ccdp-rfc-kramdown-strict clean

ASSEMBLER := tools/ccdp-assembler/target/release/ccdp-assembler
TEMPLATE := templates/draft-rfcxml-general-template-standard-00.xml-edited.md
OUTPUT := composite-cognition-dispatch-protocol.md

## ccdp-rfc: assemble the chapters into GFM, with validation
ccdp-rfc: $(ASSEMBLER)
	$< --validate --src-dir src --output $(OUTPUT)

## ccdp-rfc-strict: same as ccdp-rfc, but fail the build on any validation warning
ccdp-rfc-strict: $(ASSEMBLER)
	$< --validate --strict --src-dir src --output $(OUTPUT)

## ccdp-rfc-kramdown: assemble the chapters into kramdown-rfc-flavored markdown
ccdp-rfc-kramdown: $(ASSEMBLER)
	$< --validate --format kramdown-rfc --src-dir src --template $(TEMPLATE) --output $(OUTPUT)

## ccdp-rfc-kramdown-strict: same as ccdp-rfc-kramdown, but fail the build on any validation warning
ccdp-rfc-kramdown-strict: $(ASSEMBLER)
	$< --validate --strict --format kramdown-rfc --src-dir src --template $(TEMPLATE) --output $(OUTPUT)

$(ASSEMBLER): tools/ccdp-assembler/src/*.rs tools/ccdp-assembler/Cargo.toml
	cd tools/ccdp-assembler && cargo build --release

## clean: remove the assembled document and build artifacts
clean:
	rm -f $(OUTPUT)
	cd tools/ccdp-assembler && cargo clean
