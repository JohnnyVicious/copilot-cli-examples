# GitHub Copilot CLI Examples - Getting Started

## Overview
This repository pairs GitHub Copilot CLI with a curated set of coding challenges and reference docs. Use it to practice algorithms, refine prompting habits, and keep your environment consistent.

## What's Inside
- **challenges/** — Nine challenges split across easy, medium, and hard.
- **docs/** — This guide plus BEST_PRACTICES for prompting, testing, and security.
- **setup.py** — Checks Python version and verifies the repo layout.
- **validate.py** — Ensures required docs and challenge files exist.

## Quick Start
1. `python setup.py` — confirm your Python version and folder layout.
2. `python validate.py` — verify the repository is intact.
3. Open `challenges/<difficulty>/*.md` — read the prompt, constraints, and hints.
4. Iterate with Copilot CLI — ask for approach outlines, edge cases, and test ideas.

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
- Keep validation passing by running `python validate.py`.
