# Tests Directory

Organize challenge test code and fixtures by language/version.

## Structure

Tests are organized with **one folder per language** at the top level. See [language-support.md](../docs/language-support.md) for the complete list of supported languages and their corresponding directory names.

```
tests/
├── python/           # Python 3.11+ tests
├── go/              # Go latest stable tests
├── rust/            # Rust stable tests
├── java21/          # Java 21 tests
├── java25/          # Java 25 tests
├── csharp12/        # C# 12 (.NET 8.0) tests
├── csharp14/        # C# 14 (.NET 10.0) tests
└── powershell/      # PowerShell Core tests
```

## What to Include

Each language folder should contain:

- **Test files** — Unit tests, integration tests following language-specific conventions
- **Test fixtures** — Sample input files, expected output files, or test data
- **Test helpers** — Shared utilities, mocks, or test setup code

## File Naming Conventions

Follow language-specific testing conventions:

- **Python**: `test_*.py` or `*_test.py` (e.g., `test_two_sum.py`)
- **Go**: `*_test.go` (e.g., `two_sum_test.go`)
- **Rust**: `tests/*.rs` or inline `#[cfg(test)]` modules
- **Java**: `*Test.java` (e.g., `TwoSumTest.java`)
- **C#**: `*Tests.cs` (e.g., `TwoSumTests.cs`)
- **PowerShell**: `*.Tests.ps1` (e.g., `TwoSum.Tests.ps1`)

**Example illustrative layout** (not runnable, for reference only):

```
tests/python/
├── test_two_sum.py
├── test_reverse_string.py
├── fixtures/
│   └── sample_input.txt
└── helpers.py

tests/go/
├── two_sum_test.go
└── benchmark_test.go

tests/rust/
└── integration_test.rs
```

## Running Tests

Test commands vary by language. Refer to the table in [language-support.md](../docs/language-support.md) for language versions and setup details. Common patterns:

| Language | Typical Command | Notes |
| --- | --- | --- |
| Python | `pytest` or `python -m pytest` | Requires pytest package |
| Go | `go test ./...` | Built-in test runner |
| Rust | `cargo test` | Built-in test runner |
| Java | `mvn test` or `gradle test` | Requires build tool setup |
| C# | `dotnet test` | Requires .NET SDK |
| PowerShell | `Invoke-Pester` | Requires Pester module |

**Note**: These commands are illustrative examples. Actual test execution depends on your project structure, dependencies, and build configuration. See [language-support.md](../docs/language-support.md) for language-specific details.

## What to Exclude

Keep the following out of version control (use `.gitignore`):

- Test coverage reports and output files
- Compiled test binaries
- Test cache directories (`.pytest_cache/`, `__pycache__/`)
- IDE test runner configurations

## Guidelines

- **Language conventions**: Follow each language's testing best practices and naming patterns
- **Test isolation**: Tests should be independent and not rely on execution order
- **Fixtures over mocks**: Prefer real data fixtures when practical
- **Clear assertions**: Use descriptive test names and assertion messages
- **Reference only**: Examples in this README are illustrative to show structure—they are not actual runnable tests

For solution code and outputs, use the corresponding language folder in [`results/`](../results/README.md).

See [language-support.md](../docs/language-support.md) for language versions, toolchain details, and testing framework recommendations.
