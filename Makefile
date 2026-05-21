# Makefile — packaging targets for the ai-engineering repo.

# The collaboration-framework skill: the top-level SKILL.md plus exactly the
# six documents it pulls in, in their docs/ and templates/ layout so the
# relative links inside SKILL.md resolve. Nothing else.

SKILL_NAME    := collaboration-framework
SKILL_ZIP     := $(SKILL_NAME).zip
SKILL_STAGE   := build/$(SKILL_NAME)

# The files the skill bundles, as repo-relative paths. Keeping this list
# explicit (rather than globbing docs/) is the point: the bundle is the skill
# and its six dependencies, and nothing else.
SKILL_FILES := \
	SKILL.md \
	docs/AI-CONSTITUTION-SUPPLEMENT.md \
	docs/AI-ENGINEERING-METHODOLOGY.md \
	docs/CODE-AUDIT.md \
	docs/CLAUDE-CODE-COVERAGE.md \
	docs/SUBAGENT-DELEGATION-POLICY.md \
	templates/LEDGER_DISCIPLINE.md

.PHONY: collab-framework collab-framework-clean

## collab-framework: build collaboration-framework.zip (SKILL.md + its 6 files)
collab-framework: collab-framework-clean
	@echo ">> staging $(SKILL_NAME) bundle"
	@mkdir -p "$(SKILL_STAGE)"
	@for f in $(SKILL_FILES); do \
		if [ ! -f "$$f" ]; then \
			echo "ERROR: missing required file: $$f" >&2; exit 1; \
		fi; \
		mkdir -p "$(SKILL_STAGE)/$$(dirname "$$f")"; \
		cp "$$f" "$(SKILL_STAGE)/$$f"; \
	done
	@echo ">> writing $(SKILL_ZIP)"
	@rm -f "$(SKILL_ZIP)"
	@cd build && zip -r -q -X "../$(SKILL_ZIP)" "$(SKILL_NAME)"
	@echo ">> contents:"
	@unzip -l "$(SKILL_ZIP)"
	@rm -rf build
	@echo ">> done: $(SKILL_ZIP)"

## collab-framework-clean: remove the staging dir (leaves the zip in place)
collab-framework-clean:
	@rm -rf "$(SKILL_STAGE)"
