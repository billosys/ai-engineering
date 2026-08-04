# Makefile — CCDP RFC assembly.
#
# Builds the ccdp-assembler tool and runs it over the chapter sources in
# src/ to produce composite-cognition-dispatch-protocol.md.

.PHONY: ccdp-rfc ccdp-rfc-strict clean

ASSEMBLER := tools/ccdp-assembler/target/release/ccdp-assembler
TEMPLATE := templates/draft-rfcxml-general-template-standard-00.xml-edited.md
OUTPUT := composite-cognition-dispatch-protocol.md

## ccdp-rfc: assemble the chapters into the RFC document, with validation
ccdp-rfc: $(ASSEMBLER)
	$< --validate --src-dir src --template $(TEMPLATE) --output $(OUTPUT)

## ccdp-rfc-strict: same as ccdp-rfc, but fail the build on any validation warning
ccdp-rfc-strict: $(ASSEMBLER)
	$< --validate --strict --src-dir src --template $(TEMPLATE) --output $(OUTPUT)

$(ASSEMBLER): tools/ccdp-assembler/src/*.rs tools/ccdp-assembler/Cargo.toml
	cd tools/ccdp-assembler && cargo build --release

## clean: remove the assembled document and build artifacts
clean:
	rm -f $(OUTPUT)
	cd tools/ccdp-assembler && cargo clean
