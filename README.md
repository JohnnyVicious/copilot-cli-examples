# GitHub Copilot CLI Examples

A streamlined proof-of-concept showing how to use GitHub Copilot CLI with curated coding challenges and accompanying documentation, especially for teams on GitHub Copilot Business who do not have Codex CLI access.

## 🎯 Purpose

- Demonstrate Copilot CLI workflows end to end
- Provide ready-to-use challenges for practicing algorithmic problem solving
- Offer guidance on setup and best practices when working with Copilot
- Show how Copilot CLI alone can deliver productive, high-quality results without Codex CLI access

## 📂 Repository Structure

```
copilot-cli-examples/
├── challenges/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── docs/
│   ├── BEST_PRACTICES.md
│   └── GETTING_STARTED.md
├── setup.py
├── validate.py
└── README.md
```

## 🚀 Quick Start

1. **Setup**: `python setup.py` (checks Python version and repository layout)
2. **Validate**: `python validate.py` (verifies challenges and documentation exist)
3. **Read**: `docs/GETTING_STARTED.md` for workflow guidance
4. **Practice**: Open any file in `challenges/` and work through the prompts with Copilot

## 📖 What's Included

- **Challenges**: Nine algorithmic problems across easy, medium, and hard categories with prompts, constraints, and hints.
- **Documentation**:
  - `docs/GETTING_STARTED.md` — onboarding and Copilot CLI tips
  - `docs/BEST_PRACTICES.md` — conventions, testing strategies, and security notes
- **Utilities**:
  - `setup.py` — environment/version checks
  - `validate.py` — quick integrity verification for docs and challenge files

## 🤖 Using Copilot CLI Here

- Open a challenge markdown file and ask Copilot to explain the problem, outline approaches, or draft test cases.
- Iterate on your solution while requesting refactors, complexity analysis, or alternative strategies.
- Use the best practices doc as a checklist for prompting and review.
- For built-in skills (brainstorming, parallel dispatching, subagent-driven development, worktrees, writing skills, and requesting code review) see `.claude/skills/`; the code review skill uses agent_type `code-reviewer` with the template at `requesting-code-review/code-reviewer.md`.

## 🛠️ Development

- Run `python validate.py` before sharing changes to ensure required files remain in place.
- Keep new challenge files under `challenges/<difficulty>/` with clear statements, examples, and hints.
- Update documentation when adding or modifying challenge content.

## 🤝 Contributing

Suggestions and contributions are welcome:
- Add new challenges or refine existing ones
- Improve documentation and walkthroughs
- Expand validation to cover new content types

## 📚 Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot CLI](https://github.com/github/copilot-cli)

## 📄 License

See [LICENSE](LICENSE) for details.
