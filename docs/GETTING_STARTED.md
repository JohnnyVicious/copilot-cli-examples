# GitHub Copilot CLI Examples - Getting Started

## Overview
This repository pairs GitHub Copilot CLI with a curated set of coding challenges and reference docs. Use it to practice algorithms, refine prompting habits, and keep your environment consistent.

## What's Inside
- **challenges/** — Nine challenges split across easy, medium, and hard, each with solution templates for the languages listed in [language-support](language-support.md).
- **results/** — Language-separated folders (`results/<language>/`) for storing completed solutions and artifacts.
- **tests/** — Language-separated folders (`tests/<language>/`) for storing test code and fixtures.
- **docs/** — This guide plus BEST_PRACTICES for prompting, testing, and security.
- **.claude/skills/** — Built-in skills to boost Copilot CLI workflows.

## Quick Start
1. Open `docs/GETTING_STARTED.md` — you are here.
2. Open `challenges/<difficulty>/*.md` — read the prompt, constraints, hints, and pick your language template (see [language-support](language-support.md) for options).
3. Iterate with Copilot CLI — ask for approach outlines, edge cases, and test ideas in your chosen language.
4. Save your solution under `results/<language>/` and keep any tests under `tests/<language>/`.

## Working Through a Challenge
1. Read the problem statement and examples.
2. Ask Copilot to summarize requirements or propose multiple strategies.
3. Draft a solution; request Copilot to generate tests and complexity analysis.
4. Refine until it passes your tests and matches the constraints.

## Copilot Prompting Tips
- Be specific about language, data structures, and constraints.
- Request step-by-step reasoning or alternative approaches.
- Ask for targeted help (e.g., “generate edge cases for sliding window solution”).
- Use the guidance in `docs/BEST_PRACTICES.md` as a checklist.

## Running Solutions

Use these commands to run and test your solutions. See [language-support](language-support.md) for version details and directory structure.

| Language | Run Command | Test Command |
| --- | --- | --- |
| Python | `python templates/python/main.py` | `python -m pytest tests/python/` |
| Go | `go run templates/go/main.go` | `go test ./tests/go/...` |
| Rust | `cargo run --manifest-path templates/rust/Cargo.toml` | `cargo test --manifest-path templates/rust/Cargo.toml` |
| PowerShell | `pwsh templates/powershell/main.ps1` | `pwsh -Command "Invoke-Pester tests/powershell/"` |
| Java 21 | `java templates/java21/Main.java` | `java -cp .:junit-platform-console-standalone.jar org.junit.platform.console.ConsoleLauncher --scan-classpath --classpath tests/java21` |
| Java 25 | `java templates/java25/Main.java` | `java -cp .:junit-platform-console-standalone.jar org.junit.platform.console.ConsoleLauncher --scan-classpath --classpath tests/java25` |
| C# 12 | `dotnet run --project templates/csharp12` | `dotnet test tests/csharp12` |
| C# 14 | `dotnet run --project templates/csharp14` | `dotnet test tests/csharp14` |

**Notes:**
- Commands assume you're in the repository root.
- For Java, download [JUnit Console Standalone](https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/) JAR if running tests directly.
- Adjust file names (e.g., `main.py`, `Main.java`) to match your solution file name.

## Contributing
- Place new challenges under `challenges/<difficulty>/` with clear statements, examples, and hints.
- Update documentation when adding or modifying content.
