# Makefile — packaging targets for the ai-engineering repo.
#
# Two kinds of skill bundle:
#   * collab-framework — the top-level collaboration-framework skill
#   * per-domain        — one target per knowledge/ domain (rust, go, …)
#
# Skill zips are written under $(ZIP_OUTPUT_DIR), named after the `name:`
# declared in the skill's frontmatter, and wrap their contents in a <name>/
# directory, so the archive is never a "tarbomb" and the name on disk matches
# the name the loader sees. CCDP is a separate protocol package with its own
# `ccdp.zip` target and validator.

BUILD := build
ZIP_OUTPUT_DIR := target/skills
INSTALL_DIR ?= $(HOME)/.agents/skills
PACKAGE_PATH_EXCEPTIONS := assets/packaging/path-exceptions.tsv

# Build-time guard: every skill bundle runs its SKILL.md through this before
# packaging, so a description over the loader's limit fails the build instead
# of failing silently at load time. Single source of truth for the check.
CHECK_SKILL := ./scripts/check-skill-description.sh
SKILL_ZIP_NAMES := \
	collaboration-framework.zip \
	rust-guidelines.zip go-guidelines.zip cpp-guidelines.zip javascript-deno-guidelines.zip \
	erlang-guidelines.zip cobalt-guidelines.zip visual-design-system.zip \
	tailwindcss.zip deno-js-linter.zip biome-js-linter.zip biome-linter.zip
INSTALL_ZIPS := $(addprefix $(ZIP_OUTPUT_DIR)/,$(SKILL_ZIP_NAMES))
INSTALL_SKILLS := $(SKILL_ZIP_NAMES:.zip=)
CCDP_NAME := ccdp
CCDP_ZIP := $(ZIP_OUTPUT_DIR)/$(CCDP_NAME).zip
CCDP_STAGE := $(BUILD)/$(CCDP_NAME)

.PHONY: all skills install uninstall clean help check-skills check-package-paths \
	ccdp ccdp-package ccdp-package-clean check-ccdp-package \
	collab-framework collab-framework-clean \
	rust go cpp js erlang cobalt design tailwindcss deno biome

# Every SKILL.md (and the two biome/deno variants) packaged by this Makefile.
ALL_SKILL_FILES := \
	knowledge/collaboration-framework/SKILL.md \
	knowledge/agent-coordination/SKILL.md \
	knowledge/code-auditing/SKILL.md \
	knowledge/contribution-style/SKILL.md \
	knowledge/engineering-methods/SKILL.md \
	knowledge/project-management/SKILL.md \
	knowledge/testing/SKILL.md \
	knowledge/work-verification/SKILL.md \
	knowledge/rust/SKILL.md \
	knowledge/go/SKILL.md \
	knowledge/cpp/SKILL.md \
	knowledge/js/SKILL.md \
	knowledge/erlang/SKILL.md \
	knowledge/cobalt/SKILL.md \
	knowledge/design/SKILL.md \
	knowledge/tailwindcss/SKILL.md \
	knowledge/deno/SKILL-js-linter.md \
	knowledge/biome/SKILL-js-linter.md \
	knowledge/biome/SKILL-web-linter.md

## help: list the available targets
help:
	@echo "Packaging targets:"
	@echo "  make collab-framework   -> $(CF_ZIP) (collaboration framework SKILL.md + framework docs)"
	@echo "  make rust               -> rust-guidelines.zip"
	@echo "  make go                 -> go-guidelines.zip"
	@echo "  make cpp                -> cpp-guidelines.zip"
	@echo "  make js                 -> javascript-deno-guidelines.zip"
	@echo "  make erlang             -> erlang-guidelines.zip"
	@echo "  make cobalt             -> cobalt-guidelines.zip"
	@echo "  make design             -> visual-design-system.zip"
	@echo "  make tailwindcss        -> tailwindcss.zip"
	@echo "  make deno               -> deno-js-linter.zip"
	@echo "  make biome              -> biome-js-linter.zip AND biome-linter.zip"
	@echo "  make skills             -> all per-domain zips"
	@echo "  make all                -> skills + collab-framework"
	@echo "  make check-skills       -> validate every SKILL.md description length"
	@echo "  make ccdp               -> assemble the CCDP protocol document"
	@echo "  make ccdp-package       -> build $(CCDP_ZIP) (protocol package)"
	@echo "  make check-ccdp-package -> validate $(CCDP_ZIP) zipped and unzipped"
	@echo "  make install            -> build all zips and install them into $(INSTALL_DIR)"
	@echo "  make uninstall          -> remove installed skills from $(INSTALL_DIR)"
	@echo "  make clean              -> remove build/ and generated zips in $(ZIP_OUTPUT_DIR)"
	@echo "  make check-package-paths -> validate Markdown paths inside generated zips"

# ---------------------------------------------------------------------------
# collaboration-framework: moved source SKILL.md plus the documents it pulls in,
# staged as package-root SKILL.md with package-local links.
# Nothing else.
# ---------------------------------------------------------------------------

CF_NAME  := collaboration-framework
CF_ZIP   := $(ZIP_OUTPUT_DIR)/$(CF_NAME).zip
CF_STAGE := $(BUILD)/$(CF_NAME)

# Explicit (not a docs/ glob) on purpose: the bundle is the skill and its
# dependencies, and nothing else.
CF_FILES := \
	knowledge/agent-coordination/SKILL.md \
	knowledge/agent-coordination/version-history.md \
	knowledge/code-auditing/SKILL.md \
	knowledge/code-auditing/version-history.md \
	knowledge/contribution-style/SKILL.md \
	knowledge/contribution-style/version-history.md \
	knowledge/engineering-methods/SKILL.md \
	knowledge/project-management/SKILL.md \
	knowledge/testing/SKILL.md \
	knowledge/testing/version-history.md \
	knowledge/work-verification/SKILL.md \
	knowledge/work-verification/version-history.md \
	knowledge/collaboration-framework/guides/01-posture-and-ethics.md \
	knowledge/collaboration-framework/guides/02-structural-pulls.md \
	knowledge/collaboration-framework/guides/03-collaborative-rights.md \
	knowledge/collaboration-framework/guides/04-component-route-table.md \
	knowledge/collaboration-framework/version-history.md \
	knowledge/engineering-methods/guides/01-engineering-methodology.md \
	knowledge/engineering-methods/guides/02-knowledge-substrate.md \
	knowledge/engineering-methods/guides/03-process-rigour.md \
	knowledge/engineering-methods/guides/04-operational-routing.md \
	knowledge/engineering-methods/guides/05-component-boundary-analysis.md \
	knowledge/engineering-methods/guides/06-source-package-release-gates.md \
	knowledge/engineering-methods/version-history.md \
	knowledge/project-management/guides/PROJECT-MANAGEMENT.md \
	knowledge/project-management/guides/01-scales-of-work.md \
	knowledge/project-management/guides/02-canonical-planning-worktree.md \
	knowledge/project-management/guides/03-planning-top-down.md \
	knowledge/project-management/guides/04-closing-slices.md \
	knowledge/project-management/guides/05-closing-arcs.md \
	knowledge/project-management/guides/06-confirmation-protocol.md \
	knowledge/project-management/guides/07-anti-patterns.md \
	knowledge/project-management/guides/08-maintenance.md \
	knowledge/project-management/examples/01-worked-example-odm.md \
	knowledge/project-management/version-history.md \
	knowledge/work-verification/guides/01-ledger-discipline.md \
	knowledge/work-verification/guides/02-evidence-strength.md \
	knowledge/work-verification/guides/03-row-closure.md \
	knowledge/work-verification/guides/04-silent-drop-checks.md \
	knowledge/work-verification/guides/05-independent-verification.md \
	knowledge/code-auditing/guides/CODE-AUDIT.md \
	knowledge/testing/guides/01-testing-discipline.md \
	knowledge/testing/guides/02-coverage-hardening.md \
	knowledge/testing/guides/03-validation-gates.md \
	knowledge/agent-coordination/guides/SUBAGENT-DELEGATION-POLICY.md \
	knowledge/contribution-style/guides/CONTRIBUTION-STYLE.md \
	knowledge/work-verification/templates/LEDGER-DISCIPLINE.md \
	knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md

## collab-framework: build collaboration-framework.zip (package-root SKILL.md + framework files)
collab-framework: collab-framework-clean
	@$(CHECK_SKILL) knowledge/collaboration-framework/SKILL.md
	@echo ">> staging $(CF_NAME) bundle"
	@mkdir -p "$(CF_STAGE)"
	@./scripts/stage-skill-entrypoint knowledge/collaboration-framework/SKILL.md "$(CF_STAGE)/SKILL.md"
	@for f in $(CF_FILES); do \
		if [ ! -f "$$f" ]; then \
			echo "ERROR: missing required file: $$f" >&2; exit 1; \
		fi; \
		mkdir -p "$(CF_STAGE)/$$(dirname "$$f")"; \
		./scripts/stage-skill-entrypoint "$$f" "$(CF_STAGE)/$$f"; \
	done
	@find "$(CF_STAGE)" -name '.DS_Store' -delete
	@echo ">> writing $(CF_ZIP)"
	@mkdir -p "$(ZIP_OUTPUT_DIR)"
	@rm -f "$(CF_ZIP)"
	@cd "$(BUILD)" && zip -r -q -X "../$(CF_ZIP)" "$(CF_NAME)"
	@echo ">> contents:"
	@unzip -l "$(CF_ZIP)"
	@rm -rf "$(BUILD)"
	@echo ">> done: $(CF_ZIP)"

## collab-framework-clean: remove the staging dir (leaves the zip in place)
collab-framework-clean:
	@rm -rf "$(CF_STAGE)"

# ---------------------------------------------------------------------------
# Per-domain skill bundles.
#
# pack_skill packages one skill file plus its sibling guides/ dir into a zip
# named after the skill's frontmatter `name:`.
#   $(1) = domain subdir under knowledge/   (e.g. go)
#   $(2) = skill file within that subdir    (e.g. SKILL.md)
# The contents are wrapped in <name>/ and contain exactly:
#   <name>/<skill-file>   and   <name>/guides/**
# ---------------------------------------------------------------------------

KNOWLEDGE := knowledge

define pack_skill
	@dir="$(KNOWLEDGE)/$(1)"; src="$$dir/$(2)"; \
	if [ ! -f "$$src" ]; then echo "ERROR: missing skill file: $$src" >&2; exit 1; fi; \
	if [ ! -d "$$dir/guides" ]; then echo "ERROR: missing guides dir: $$dir/guides" >&2; exit 1; fi; \
	$(CHECK_SKILL) "$$src"; \
	name=$$(sed -n 's/^name:[[:space:]]*//p' "$$src" | head -1); \
	if [ -z "$$name" ]; then echo "ERROR: no 'name:' in $$src frontmatter" >&2; exit 1; fi; \
	stage="$(BUILD)/$$name"; \
	echo ">> staging $$name bundle ($$src + $$dir/guides)"; \
	rm -rf "$$stage"; mkdir -p "$$stage"; \
	./scripts/stage-skill-entrypoint "$$src" "$$stage/$$(basename "$$src")"; \
	cp -R "$$dir/guides" "$$stage/guides"; \
	find "$$stage" -name '.DS_Store' -delete; \
	zip_path="$(ZIP_OUTPUT_DIR)/$$name.zip"; \
	echo ">> writing $$zip_path"; \
	mkdir -p "$(ZIP_OUTPUT_DIR)"; \
	rm -f "$$zip_path"; \
	( cd "$(BUILD)" && zip -r -q -X "../$$zip_path" "$$name" ); \
	echo ">> contents:"; \
	unzip -l "$$zip_path"; \
	rm -rf "$(BUILD)"; \
	echo ">> done: $$zip_path"
endef

rust:
	$(call pack_skill,rust,SKILL.md)

go:
	$(call pack_skill,go,SKILL.md)

cpp:
	$(call pack_skill,cpp,SKILL.md)

js:
	$(call pack_skill,js,SKILL.md)

erlang:
	$(call pack_skill,erlang,SKILL.md)

cobalt:
	$(call pack_skill,cobalt,SKILL.md)

design:
	$(call pack_skill,design,SKILL.md)

tailwindcss:
	$(call pack_skill,tailwindcss,SKILL.md)

deno:
	$(call pack_skill,deno,SKILL-js-linter.md)

# biome ships two distinct skills (js-linter and web-linter), each with its own
# frontmatter name; build both zips.
biome:
	$(call pack_skill,biome,SKILL-js-linter.md)
	$(call pack_skill,biome,SKILL-web-linter.md)

# ---------------------------------------------------------------------------
# Aggregates
# ---------------------------------------------------------------------------

## skills: build every per-domain zip
skills: rust go cpp js erlang cobalt design tailwindcss deno biome

## all: build every per-domain zip plus the collaboration-framework zip
all: skills collab-framework

## check-skills: validate the description length of every SKILL.md
check-skills:
	@$(CHECK_SKILL) $(ALL_SKILL_FILES)
	@echo ">> all skill descriptions within limit"

## check-package-paths: build all zips and validate package-context Markdown paths
check-package-paths: all
	@./scripts/check-package-paths --exceptions "$(PACKAGE_PATH_EXCEPTIONS)" $(INSTALL_ZIPS)

$(INSTALL_DIR):
	@mkdir -p "$@"

## install: uninstall old copies, build all zips, and install them into $(INSTALL_DIR)
install: $(INSTALL_DIR) uninstall all
	@echo ">> installing skill zips into $(INSTALL_DIR)"
	@for zip in $(INSTALL_ZIPS); do \
		if [ ! -f "$$zip" ]; then \
			echo "ERROR: missing zip: $$zip" >&2; exit 1; \
		fi; \
		unzip -o -q "$$zip" -d "$(INSTALL_DIR)"; \
	done
	@echo ">> installed skills into $(INSTALL_DIR)"

## uninstall: remove installed skills from $(INSTALL_DIR)
uninstall:
	@echo ">> uninstalling skills from $(INSTALL_DIR)"
	@for skill in $(INSTALL_SKILLS); do \
		rm -rf "$(INSTALL_DIR)/$$skill"; \
	done
	@echo ">> uninstalled skills from $(INSTALL_DIR)"

## clean: remove the staging dir and generated zips
clean:
	@rm -rf "$(BUILD)" "$(ZIP_OUTPUT_DIR)"
	@rmdir target 2>/dev/null || true
	@echo ">> cleaned build/ and generated zips in $(ZIP_OUTPUT_DIR)"

ccdp:
	@cd protocols/ccdp && make

ccdp-package-clean:
	@rm -rf "$(CCDP_STAGE)"

ccdp-package: ccdp-package-clean
	@echo ">> checking CCDP assembled spec freshness"
	@tmp=$$(mktemp /private/tmp/ccdp-package-freshness.XXXXXX); \
	$(MAKE) -C protocols/ccdp ccdp-rfc OUTPUT="$$tmp"; \
	if ! cmp -s "protocols/ccdp/composite-cognition-dispatch-protocol.md" "$$tmp"; then \
		echo "ERROR: protocols/ccdp/composite-cognition-dispatch-protocol.md is stale" >&2; \
		echo "Run 'make -C protocols/ccdp ccdp-rfc' and commit the generated refresh." >&2; \
		rm -f "$$tmp"; \
		exit 1; \
	fi; \
	rm -f "$$tmp"
	@echo ">> staging $(CCDP_NAME) package"
	@mkdir -p "$(CCDP_STAGE)"
	@cp protocols/ccdp/composite-cognition-dispatch-protocol.md "$(CCDP_STAGE)/"
	@cp -R protocols/ccdp/src "$(CCDP_STAGE)/src"
	@cp -R protocols/ccdp/json "$(CCDP_STAGE)/json"
	@cp -R protocols/ccdp/visual-guide "$(CCDP_STAGE)/visual-guide"
	@cp -R protocols/ccdp/templates "$(CCDP_STAGE)/templates"
	@mkdir -p "$(CCDP_STAGE)/tools/ccdp-assembler"
	@cp protocols/ccdp/tools/ccdp-assembler/Cargo.toml "$(CCDP_STAGE)/tools/ccdp-assembler/"
	@cp protocols/ccdp/tools/ccdp-assembler/Cargo.lock "$(CCDP_STAGE)/tools/ccdp-assembler/"
	@cp -R protocols/ccdp/tools/ccdp-assembler/src "$(CCDP_STAGE)/tools/ccdp-assembler/src"
	@cp protocols/ccdp/Makefile "$(CCDP_STAGE)/Makefile"
	@cp protocols/ccdp/README.md "$(CCDP_STAGE)/README.md"
	@find "$(CCDP_STAGE)" -name '.DS_Store' -delete
	@echo ">> writing $(CCDP_ZIP)"
	@mkdir -p "$(ZIP_OUTPUT_DIR)"
	@rm -f "$(CCDP_ZIP)"
	@cd "$(BUILD)" && zip -r -q -X "../$(CCDP_ZIP)" "$(CCDP_NAME)"
	@echo ">> contents:"
	@unzip -l "$(CCDP_ZIP)"
	@rm -rf "$(CCDP_STAGE)"
	@rmdir "$(BUILD)" 2>/dev/null || true
	@echo ">> done: $(CCDP_ZIP)"

check-ccdp-package: ccdp-package
	@./scripts/check-ccdp-package "$(CCDP_ZIP)"
