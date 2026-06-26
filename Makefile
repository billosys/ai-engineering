# Makefile — packaging targets for the ai-engineering repo.
#
# Two kinds of skill bundle:
#   * collab-framework — the top-level collaboration-framework skill
#   * per-domain        — one target per knowledge/ domain (rust, go, …)
#
# Every zip is named after the `name:` declared in the skill's frontmatter
# and wraps its contents in a <name>/ directory, so the archive is never a
# "tarbomb" and the name on disk matches the name the loader sees.

BUILD := build
INSTALL_DIR ?= $(HOME)/.agents/skills

# Build-time guard: every skill bundle runs its SKILL.md through this before
# packaging, so a description over the loader's limit fails the build instead
# of failing silently at load time. Single source of truth for the check.
CHECK_SKILL := ./scripts/check-skill-description.sh
INSTALL_ZIPS := \
	collaboration-framework.zip \
	rust-guidelines.zip go-guidelines.zip javascript-deno-guidelines.zip \
	erlang-guidelines.zip cobalt-guidelines.zip visual-design-system.zip \
	tailwindcss.zip deno-js-linter.zip biome-js-linter.zip biome-linter.zip
INSTALL_SKILLS := $(INSTALL_ZIPS:.zip=)

.PHONY: all skills install uninstall clean help check-skills \
	collab-framework collab-framework-clean \
	rust go js erlang cobalt design tailwindcss deno biome

# Every SKILL.md (and the two biome/deno variants) packaged by this Makefile.
ALL_SKILL_FILES := \
	SKILL.md \
	knowledge/rust/SKILL.md \
	knowledge/go/SKILL.md \
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
	@echo "  make collab-framework   -> collaboration-framework.zip (SKILL.md + its 9 docs)"
	@echo "  make rust               -> rust-guidelines.zip"
	@echo "  make go                 -> go-guidelines.zip"
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
	@echo "  make install            -> build all zips and install them into $(INSTALL_DIR)"
	@echo "  make uninstall          -> remove installed skills from $(INSTALL_DIR)"
	@echo "  make clean              -> remove build/ and all *.zip"

# ---------------------------------------------------------------------------
# collaboration-framework: top-level SKILL.md plus exactly the nine documents it
# pulls in, in their docs/ and templates/ layout so the relative links resolve.
# Nothing else.
# ---------------------------------------------------------------------------

CF_NAME  := collaboration-framework
CF_ZIP   := $(CF_NAME).zip
CF_STAGE := $(BUILD)/$(CF_NAME)

# Explicit (not a docs/ glob) on purpose: the bundle is the skill and its six
# dependencies, and nothing else.
CF_FILES := \
	SKILL.md \
	docs/AI-CONSTITUTION-SUPPLEMENT.md \
	docs/AI-ENGINEERING-METHODOLOGY.md \
	docs/PROJECT-MANAGEMENT.md \
	docs/CODE-AUDIT.md \
	docs/CLAUDE-CODE-COVERAGE.md \
	docs/SUBAGENT-DELEGATION-POLICY.md \
	docs/CONTRIBUTION-STYLE.md \
	templates/LEDGER-DISCIPLINE.md \
	templates/CONTRIBUTION-TICKET.md

## collab-framework: build collaboration-framework.zip (SKILL.md + its 9 files)
collab-framework: collab-framework-clean
	@$(CHECK_SKILL) SKILL.md
	@echo ">> staging $(CF_NAME) bundle"
	@mkdir -p "$(CF_STAGE)"
	@for f in $(CF_FILES); do \
		if [ ! -f "$$f" ]; then \
			echo "ERROR: missing required file: $$f" >&2; exit 1; \
		fi; \
		mkdir -p "$(CF_STAGE)/$$(dirname "$$f")"; \
		cp "$$f" "$(CF_STAGE)/$$f"; \
	done
	@find "$(CF_STAGE)" -name '.DS_Store' -delete
	@echo ">> writing $(CF_ZIP)"
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
	cp "$$src" "$$stage/"; \
	cp -R "$$dir/guides" "$$stage/guides"; \
	find "$$stage" -name '.DS_Store' -delete; \
	echo ">> writing $$name.zip"; \
	rm -f "$$name.zip"; \
	( cd "$(BUILD)" && zip -r -q -X "../$$name.zip" "$$name" ); \
	echo ">> contents:"; \
	unzip -l "$$name.zip"; \
	rm -rf "$(BUILD)"; \
	echo ">> done: $$name.zip"
endef

rust:
	$(call pack_skill,rust,SKILL.md)

go:
	$(call pack_skill,go,SKILL.md)

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
skills: rust go js erlang cobalt design tailwindcss deno biome

## all: build every per-domain zip plus the collaboration-framework zip
all: skills collab-framework

## check-skills: validate the description length of every SKILL.md
check-skills:
	@$(CHECK_SKILL) $(ALL_SKILL_FILES)
	@echo ">> all skill descriptions within limit"

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

## clean: remove the staging dir and every generated zip
clean:
	@rm -rf "$(BUILD)"
	@rm -f $(INSTALL_ZIPS)
	@echo ">> cleaned build/ and all skill zips"
