# Challenge File Schema

This document defines the required structure for challenge markdown files in the `challenges/` directory.

## Purpose

Maintain consistent formatting across all challenges to:

- Provide a uniform experience for contributors and users
- Enable automated tooling and template extraction
- Ensure all essential information is present

## Required Sections

Each challenge file **MUST** include the following H2 sections in this order:

### 1. Problem Description

Brief overview of the coding challenge, including:

- What the function/solution should accomplish
- Key inputs and outputs
- Any important context or definitions

### 2. Examples

At least one concrete example showing:

- Input values
- Expected output
- Optional explanation of the logic

Format examples in code blocks for clarity.

### 3. Constraints

Technical constraints and boundaries, such as:

- Input size limits
- Value ranges
- Assumptions about data
- Uniqueness guarantees

### 4. Solution Templates

Starter code in supported languages (see [language-support](../docs/language-support.md)).

**Section title MUST be:** `Solution Templates (see [language-support](../../docs/language-support.md))`

Include templates for:

- Python
- Go
- Rust
- PowerShell

Each template should:

- Include a TODO comment where implementation goes
- Provide basic test cases or usage examples
- Follow language-specific best practices

### 5. Hints

Helpful tips without giving away the solution:

- Suggest data structures to consider
- Mention relevant algorithms or patterns
- Highlight key insights
- Include time/space complexity goals

### 6. Solution Approach

Detailed explanation of one or more solution strategies:

- Step-by-step algorithm description
- Time and space complexity analysis
- Key concepts and techniques used
- Trade-offs between different approaches

**Note:** This section may be titled either:

- `Solution Approach` (singular) for single approach
- `Solution Approaches` (plural) for multiple approaches
- `Solution Approach - [Technique]` (with specific technique name, e.g., "Solution Approach - BFS")

All variations are acceptable and will pass validation.

## Optional Sections

The following H2 sections are optional but recommended where relevant:

- **Key Concepts**: List of important topics (algorithms, data structures, patterns)
- **Edge Cases to Consider**: Specific edge cases to handle
- **Common Pitfalls**: Mistakes to avoid
- **Follow-up Questions**: Extension or variation problems

## Validation

The script `scripts/lint-challenges.sh` validates that all required sections are present.

Run validation locally:

```bash
make lint-challenges
```

Or directly:

```bash
bash scripts/lint-challenges.sh
```

## Example Structure

```markdown
# Challenge Title

## Problem Description
[Description here]

## Examples
[Examples here]

## Constraints
[Constraints here]

## Solution Templates (see [language-support](../../docs/language-support.md))
[Code templates here]

## Hints
[Hints here]

## Solution Approach
[Approach explanation here]

## Key Concepts (optional)
[Concepts here]
```
