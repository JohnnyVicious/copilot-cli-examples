# Templates

This directory contains minimal runnable starter templates for each supported language and version. These templates provide a consistent entrypoint and I/O contract to help you get started quickly.

## Purpose

Each template demonstrates:
- Language-specific entrypoint (main function/method)
- Basic input/output operations
- Comments explaining how to run and build
- Minimal dependencies (standard library only)

## Available Templates

### Python (3.11+)
- **File:** [`python/starter.py`](python/starter.py)
- **Run:** `python3 starter.py`
- **Description:** Simple Python script with stdin/stdout I/O

### Go (latest stable)
- **File:** [`go/starter.go`](go/starter.go)
- **Run:** `go run starter.go`
- **Build:** `go build starter.go`
- **Description:** Go program with buffered input reader

### Rust (stable)
- **File:** [`rust/starter.rs`](rust/starter.rs)
- **Run:** `rustc starter.rs && ./starter` or use `cargo run` in a Cargo project
- **Description:** Rust program with error handling for I/O

### PowerShell (Core)
- **File:** [`powershell/starter.ps1`](powershell/starter.ps1)
- **Run:** `pwsh starter.ps1` or `./starter.ps1`
- **Description:** PowerShell script with cmdlet-based I/O

### Java 21
- **File:** [`java21/Starter.java`](java21/Starter.java)
- **Compile:** `javac Starter.java`
- **Run:** `java Starter`
- **Description:** Java class with Scanner for input

### Java 25
- **File:** [`java25/Starter.java`](java25/Starter.java)
- **Compile:** `javac Starter.java`
- **Run:** `java Starter`
- **Description:** Java class with Scanner for input

### C# 12 (.NET 8.0)
- **File:** [`csharp12/Starter.cs`](csharp12/Starter.cs)
- **Run:** `dotnet run` (requires .csproj) or `csc Starter.cs && ./Starter`
- **Description:** C# class with Console I/O

### C# 14 (.NET 10.0)
- **File:** [`csharp14/Starter.cs`](csharp14/Starter.cs)
- **Run:** `dotnet run` (requires .csproj) or `csc Starter.cs && ./Starter`
- **Description:** C# class with Console I/O

## How to Use

1. **Choose your language** - Select a template from the supported languages above
2. **Copy the template** - Use the starter file as a base for your solution
3. **Implement your logic** - Replace the sample code with your implementation
4. **Run and test** - Follow the run/build instructions for your language

## Language Support

For complete details on supported languages, versions, and directory structure, see the [language support documentation](../docs/language-support.md).

## I/O Contract

All templates follow a consistent pattern:

```
1. Read input (from stdin, args, or prompt)
2. Process the input
3. Write output (to stdout)
```

This structure makes it easy to:
- Test implementations with different inputs
- Chain programs together using pipes
- Integrate with automated testing frameworks

## Building on Templates

These templates are intentionally minimal. When solving challenges, you may need to:

- Add command-line argument parsing
- Implement more complex data structures
- Import additional standard library modules
- Handle different input/output formats
- Add error handling and validation

The templates provide a starting point, not a complete solution framework.

## Contributing

When adding a new language or version:

1. Create a new directory under `templates/<language>/`
2. Add a `starter.*` file with appropriate extension
3. Include comments explaining how to run/build
4. Document the I/O pattern in comments
5. Update this README with the new language
6. Update [`language-support.md`](../docs/language-support.md) with cross-links
7. Ensure the template runs without external dependencies
