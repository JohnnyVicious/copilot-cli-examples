# Language Support

This repository centralizes supported languages, versions, and where to place templates, tests, and solutions.

| Language | Version / Notes | Tests | Results | Templates |
| --- | --- | --- | --- | --- |
| Python | 3.11+ | `tests/python/` | `results/python/` | `templates/python/` |
| Go | latest stable | `tests/go/` | `results/go/` | `templates/go/` |
| Rust | stable | `tests/rust/` | `results/rust/` | `templates/rust/` |
| PowerShell | Core | `tests/powershell/` | `results/powershell/` | `templates/powershell/` |
| Java | 21 | `tests/java21/` | `results/java21/` | `templates/java21/` |
| Java | 25 | `tests/java25/` | `results/java25/` | `templates/java25/` |
| C# | 12 (.NET 8.0) | `tests/csharp12/` | `results/csharp12/` | `templates/csharp12/` |
| C# | 14 (.NET 10.0) | `tests/csharp14/` | `results/csharp14/` | `templates/csharp14/` |

## Usage

- Challenges reference this document for supported languages and template locations; add new templates under the matching `templates/<language>/` folder.
- Keep tests and solution artifacts in the corresponding `tests/<language>/` and `results/<language>/` directories.
- When adding a new language or version, update this table and create aligned `tests/`, `results/`, and `templates/` subfolders.
- See [Running Solutions](GETTING_STARTED.md#running-solutions) in the Getting Started guide for copy-pastable run and test commands.
