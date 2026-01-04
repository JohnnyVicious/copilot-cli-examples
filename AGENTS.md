# Repository Guidelines

Purpose: Copilot CLI-focused challenge and documentation set for practicing workflows without Codex CLI.

## Project Structure & Module Organization
- Challenges grouped in `challenges/easy|medium|hard`; each file includes prompt, constraints, hints, and templates.
- `docs/` contains onboarding (`GETTING_STARTED.md`), prompting/testing guidance (`BEST_PRACTICES.md`), and CLI comparison notes.
- Skills for Copilot workflows live under `.claude/skills/`; this guide complements those instructions.

## Build, Test, and Development Commands
- No build pipeline here; work directly with Markdown challenges and docs.
- Search quickly: `rg term challenges/medium` or list files with `rg --files`.
- Word count check for docs: `wc -w AGENTS.md`.
- Run `make lint-docs` to check markdown formatting, spelling, and links (requires markdownlint-cli2, cspell, and lychee).
- Run `make help` for available development commands.

## Coding Style & Naming Conventions
- Markdown: sentence-case headings, concise bullets, and fenced code blocks with language tags.
- Challenge files follow the existing format (problem, examples, constraints, template, hints, approach, complexity).
- Use descriptive names in code snippets to aid Copilot suggestions; keep indentation consistent with language defaults.

## Testing Guidelines
- Repository has no automated test suite; run sample snippets within challenge files or your language REPL.
- If adding executable code or scripts, include inline assertions/examples and document how to run them.
- Keep example inputs/outputs accurate and minimal.

## Commit & Pull Request Guidelines
- Follow observed prefixes (`docs:`, `chore:`) and keep messages imperative and scoped.
- Write PR titles that include the prefix plus a concise scope (e.g., `docs: clarify language support`).
- Complete the pre-merge checklist in the [PR template](.github/pull_request_template.md) before finalizing your pull request.
- In PR descriptions, include:
  - **Summary**: 2–4 bullets describing the specific changes (what/where/why), noting docs-only when applicable.
  - **Testing**: Exact commands run, or `not run (reason)`.
  - **Context/Links**: Issue/PR references or motivation if no issue.
  - **Before/After**: Screenshots or brief text diffs for UX/docs/format changes.
  - **Risks/Rollout**: Breaking changes, follow-ups, or flags if relevant.
- Update documentation when adding or modifying challenges.
- When committing with Codex, add `Co-authored-by: ChatGPT (Codex CLI) <chatgpt@codex.cli>` so agent use is visible.

## Security, Configuration, and Agent Notes
- Do not include secrets, tokens, or proprietary problem statements in prompts or docs.
- When using Copilot CLI, provide clear context but scrub sensitive data; prefer local files over pasted payloads.
- Keep new files in the established directories; avoid creating new top-level folders without discussion.
