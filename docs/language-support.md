# Language Support

This repository centralizes supported languages, versions, and where to place templates, tests, and solutions.

## Supported Languages

| Language | Version / Notes | Starter Template | Tests | Results | Templates |
| --- | --- | --- | --- | --- | --- |
| Python | 3.11+ | [starter.py](../templates/python/starter.py) | `tests/python/` | `results/python/` | `templates/python/` |
| Go | latest stable | [starter.go](../templates/go/starter.go) | `tests/go/` | `results/go/` | `templates/go/` |
| Rust | stable | [starter.rs](../templates/rust/starter.rs) | `tests/rust/` | `results/rust/` | `templates/rust/` |
| PowerShell | Core | [starter.ps1](../templates/powershell/starter.ps1) | `tests/powershell/` | `results/powershell/` | `templates/powershell/` |
| Java | 21 | [Starter.java](../templates/java21/Starter.java) | `tests/java21/` | `results/java21/` | `templates/java21/` |
| Java | 25 | [Starter.java](../templates/java25/Starter.java) | `tests/java25/` | `results/java25/` | `templates/java25/` |
| C# | 12 (.NET 8.0) | [Starter.cs](../templates/csharp12/Starter.cs) | `tests/csharp12/` | `results/csharp12/` | `templates/csharp12/` |
| C# | 14 (.NET 10.0) | [Starter.cs](../templates/csharp14/Starter.cs) | `tests/csharp14/` | `results/csharp14/` | `templates/csharp14/` |

## Starter Templates

Each language has a minimal runnable starter template that demonstrates:
- How to run/build the code
- Basic input/output operations
- Standard entrypoint structure

For detailed information about using these templates, see the [templates README](../templates/README.md).

## Usage

- Challenges reference this document for supported languages and template locations; add new templates under the matching `templates/<language>/` folder.
- Keep tests and solution artifacts in the corresponding `tests/<language>/` and `results/<language>/` directories.
- When adding a new language or version, update this table and create aligned `tests/`, `results/`, and `templates/` subfolders.
- See [Running Solutions](GETTING_STARTED.md#running-solutions) in the Getting Started guide for copy-pastable run and test commands.
