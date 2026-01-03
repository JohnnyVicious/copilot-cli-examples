# AGENTS Contributor Guide Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create `AGENTS.md` as a concise 200-400 word contributor guide titled "Repository Guidelines".

**Architecture:** Single Markdown document at repo root with clear sections covering structure, commands, style, testing, commit/PR expectations, and security/agent tips tailored to this repo.

**Tech Stack:** Markdown, Git.

### Task 1: Confirm repo context

**Files:**
- Read: `README.md`, `challenges/README.md` (if present), `docs/GETTING_STARTED.md`, `docs/BEST_PRACTICES.md`, `docs/cli-coding-tools-comparison.md`

**Step 1: Review current docs for expectations and terminology**

Run: `ls challenges` and skim key docs above to ensure guidance matches existing patterns. Expected: identify difficulty folders and doc tone.

### Task 2: Draft AGENTS.md outline

**Files:**
- Create: `AGENTS.md`

**Step 1: Write headings and bullets**

Include sections for project structure, build/test/dev commands, coding style/naming, testing guidelines, commit/PR rules, and security/config/agent tips. Keep wording concise and repo-specific.

### Task 3: Fill content with repo specifics

**Files:**
- Modify: `AGENTS.md`

**Step 1: Add structure details**

Describe `challenges/<difficulty>`, `docs/`, and any skill references; include examples (e.g., `rg term challenges/medium`).

**Step 2: Add command guidance**

List key commands (e.g., `rg --files`, `wc -w AGENTS.md` for word count) and note no build/tests expected unless contributors add them.

**Step 3: Add style, testing, and commit/PR conventions**

Mirror observed commit prefixes (e.g., `docs:`) and markdown style expectations. Note PR requirements (summary, linked issues, screenshots when UI content).

**Step 4: Add security/agent tips**

Mention avoiding secrets in prompts/docs, and point to Copilot CLI usage guidance.

### Task 4: Self-check

**Files:**
- Read: `AGENTS.md`

**Step 1: Verify length and clarity**

Run: `wc -w AGENTS.md` to confirm 200-400 words. Re-read for tone and section coverage. Expected: word count within range and sections clear.
