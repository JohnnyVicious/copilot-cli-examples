# Known Issues

Issues identified during code review (2026-01-02).

## High

*No open issues.*

---

## Medium

### Broken deep-dive anchor links in quick-reference

**Location:** `docs/rust-lessons/quick-reference.md` (lines 229, 257, 283, 307, 369, 398, 523, 552)

**Description:** Multiple deep-dive links point to anchors that don't exist:
- `performance-deep-dive.md#loop-optimizations` → should be `#1-performance-critical-loop-optimizations`
- `performance-deep-dive.md#zero-copy` → should be `#2-when-not-to-use-zero-copy-abstractions`
- `file-io-deep-dive.md#atomic-writes` → should be `#1-atomic-file-writes`
- `file-io-deep-dive.md#parent-directories` → should be `#2-parent-directories-for-file-writes`
- `file-io-deep-dive.md#testing` → should be `#4-testing-file-io`
- `type-safety-deep-dive.md#constants` → should be `#2-using-constants-for-validation`
- `common-footguns.md#borrow-checker` → should be `#3-borrow-checker-with-hashset`
- `common-footguns.md#toctou-races` → should be `#4-fixing-toctou-races`

**Fix:** Update links to match actual numbered heading anchors.

---

### Overly permissive default flags in github-copilot skill

**Location:** `.claude/skills/github-copilot/SKILL.md:37-48`

**Description:** Default invocation recommends `--allow-all-paths --allow-all-tools` for every copilot call, granting unnecessary filesystem/tool access for simple second-opinion queries.

**Fix:** Default to least privilege (omit flags unless required) and document when elevated access is needed.

---

## Low

### Lesson count mismatch

**Location:** `docs/rust-lessons/index.md:21-22` vs `docs/rust-lessons/quick-reference.md:12`

**Description:** Index claims quick reference has 20 lessons, but quick-reference lists 21.

**Fix:** Reconcile the counts or remove hard-coded numbers.
