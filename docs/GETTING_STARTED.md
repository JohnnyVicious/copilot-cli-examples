# GitHub Copilot CLI Examples - Getting Started

## Overview
This repository pairs GitHub Copilot CLI with a curated set of coding challenges and reference docs. Use it to practice algorithms, refine prompting habits, and keep your environment consistent.

## What's Inside
- **challenges/** — Nine challenges split across easy, medium, and hard, each with solution templates for Python 3.11+, Go, Rust, and PowerShell Core.
- **results/** — Language-separated folders (`results/<language>/`) for storing completed solutions and artifacts.
- **tests/** — Language-separated folders (`tests/<language>/`) for storing test code and fixtures.
- **docs/** — This guide plus BEST_PRACTICES for prompting, testing, and security.
- **.claude/skills/** — Built-in skills to boost Copilot CLI workflows.

## Quick Start
1. Open `docs/GETTING_STARTED.md` — you are here.
2. Open `challenges/<difficulty>/*.md` — read the prompt, constraints, hints, and pick your language template (Python 3.11+, Go, Rust, or PowerShell Core).
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

## Contributing
- Place new challenges under `challenges/<difficulty>/` with clear statements, examples, and hints.
- Update documentation when adding or modifying content.
