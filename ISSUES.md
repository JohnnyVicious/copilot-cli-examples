# Known Issues

Issues identified during code review (2026-01-02).

## High

*No open issues.*

---

## Medium

*No open issues.*

---

## Low

### Lesson count mismatch

**Location:** `docs/rust-lessons/index.md:21-22` vs `docs/rust-lessons/quick-reference.md:12`

**Description:** Index claims quick reference has 20 lessons, but quick-reference lists 21.

**Fix:** Reconcile the counts or remove hard-coded numbers.
