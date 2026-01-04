.PHONY: help lint-docs markdownlint spellcheck linkcheck

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

lint-docs: markdownlint spellcheck linkcheck ## Run all documentation linting checks

markdownlint: ## Run markdownlint on docs and challenges
	@command -v markdownlint-cli2 >/dev/null 2>&1 || { echo "markdownlint-cli2 not found. Install with: npm install -g markdownlint-cli2"; exit 1; }
	markdownlint-cli2 "docs/**/*.md" "challenges/**/*.md" "*.md"

spellcheck: ## Run cspell spellcheck on docs and challenges
	@command -v cspell >/dev/null 2>&1 || { echo "cspell not found. Install with: npm install -g cspell"; exit 1; }
	cspell --no-progress --show-suggestions "docs/**/*.md" "challenges/**/*.md" "*.md"

linkcheck: ## Run lychee linkcheck on docs and challenges
	@command -v lychee >/dev/null 2>&1 || { echo "lychee not found. Install with: cargo install lychee"; exit 1; }
	lychee --verbose --no-progress \
		--exclude-path results \
		--exclude-path tests \
		--exclude-path templates \
		--exclude-path .github \
		--max-retries 3 \
		--timeout 10 \
		"docs/**/*.md" "challenges/**/*.md" "*.md"
