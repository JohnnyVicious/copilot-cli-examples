# Results Directory

Store solved challenge outputs here, organized by language/version.

## Structure

Results are organized with **one folder per language** at the top level. See [language-support.md](../docs/language-support.md) for the complete list of supported languages and their corresponding directory names.

```
results/
├── python/           # Python 3.11+ solutions
├── go/              # Go latest stable solutions
├── rust/            # Rust stable solutions
├── java21/          # Java 21 solutions
├── java25/          # Java 25 solutions
├── csharp12/        # C# 12 (.NET 8.0) solutions
├── csharp14/        # C# 14 (.NET 10.0) solutions
└── powershell/      # PowerShell Core solutions
```

## What to Include

Each language folder should contain:

- **Source code files** — Your implemented solution with appropriate file extensions (`.py`, `.go`, `.rs`, `.java`, `.cs`, `.ps1`)
- **Output files** (optional) — Sample program outputs, results, or data files generated during execution
- **Notes** (optional) — Markdown files documenting approaches, complexity analysis, or implementation decisions

## File Naming Conventions

Use descriptive names that reflect the challenge or problem:

- `two_sum.py`, `two_sum.go`, `two_sum.rs` — Challenge solutions
- `binary_search_tree.java`, `linked_list.cs` — Data structure implementations
- `challenge_name_output.txt` — Sample execution outputs
- `notes_challenge_name.md` — Implementation notes (optional)

**Example illustrative layout** (not runnable, for reference only):

```
results/python/
├── two_sum.py
├── reverse_string.py
└── notes_two_sum.md

results/go/
├── two_sum.go
└── binary_search.go

results/rust/
├── two_sum.rs
└── two_sum_output.txt
```

## What to Exclude

Keep the following out of version control (use `.gitignore`):

- Compiled binaries and executables
- Build artifacts (`target/`, `bin/`, `obj/`, `__pycache__/`)
- Package dependencies (`node_modules/`, `vendor/`)
- IDE-specific files

## Guidelines

- **Language-specific**: Each language folder is independent; organize files according to that language's conventions
- **Keep it clean**: Only commit source code and documentation, not generated artifacts
- **Self-contained**: Each solution file should be complete and runnable independently when possible
- **Reference only**: Examples in this README are illustrative to show structure—they are not actual runnable code

For test code and fixtures, use the corresponding language folder in [`tests/`](../tests/README.md).

See [language-support.md](../docs/language-support.md) for language versions and toolchain details.
