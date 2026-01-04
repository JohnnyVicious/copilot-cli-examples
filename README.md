# GitHub Copilot CLI Examples

A streamlined proof-of-concept showing how to use GitHub Copilot CLI with curated coding challenges and accompanying documentation, especially for teams on GitHub Copilot Business who do not have Codex CLI access. See the [CLI Coding Tools Comparison](docs/cli-coding-tools-comparison.md) for a full breakdown; the quick summary below highlights the most important differences.

## 🧭 Quick CLI Comparison

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Release / Source** | GA, closed | GA, open source (Rust) | Public Preview, closed |
| **Models** | Claude Sonnet/Opus/Haiku | GPT-5.2-Codex family | Multi-vendor (Claude, GPT, Gemini) |
| **Context** | Instant auto-compaction + manual | Native compaction + manual | Auto-compaction at 95% + manual |
| **GitHub Integration** | Via `gh`/MCP | Native GitHub support | Deep native GitHub (Issues/PRs) |
| **MCP** | Client + server | Client-only | Client + GitHub MCP server |
| **Subagents / Delegation** | Background tasks | Cloud agent delegation | Built-in subagents + `/delegate` |
| **Best Fit** | Strong MCP ecosystem, local-first | Cloud agent + Windows support | GitHub-first teams, multi-model |

## 🎯 Purpose

- Demonstrate Copilot CLI workflows end to end
- Provide ready-to-use challenges for practicing algorithmic problem solving with solution templates (see [language support](docs/language-support.md) for versions)
- Offer guidance on setup and best practices when working with Copilot
- Show how Copilot CLI alone can deliver productive, high-quality results without Codex CLI access

## 📂 Repository Structure

```
copilot-cli-examples/
├── challenges/
│   ├── easy/
│   ├── medium/
│   └── hard/
├── results/
│   ├── <language>/
│   └── ...
├── tests/
│   ├── <language>/
│   └── ...
├── templates/
│   ├── <language>/
│   └── ...
├── .claude/
│   └── skills/
├── docs/
│   ├── BEST_PRACTICES.md
│   └── GETTING_STARTED.md
└── README.md
```

See [docs/language-support.md](docs/language-support.md) for the current languages and versions.

Copilot instructions: if both `AGENTS.md` and `.github/copilot-instructions.md` exist, treat `AGENTS.md` as the source of truth for this Copilot CLI-focused repository.

## 🚀 Quick Start

1. **Read**: `docs/GETTING_STARTED.md` for workflow guidance
2. **Practice**: Open any file in `challenges/` and work through the prompts with Copilot using the language template you prefer (see [language support](docs/language-support.md))
3. **Save**: Store solutions under `results/<language>/` and keep language-specific tests under `tests/<language>/`

## 📖 What's Included

- **Challenges**: Algorithmic problems across easy, medium, and hard categories with prompts, constraints, hints, and solution templates for the languages listed in [language support](docs/language-support.md).
- **Results**: Language-separated folders under `results/` for storing completed solutions and artifacts.
- **Tests**: Language-separated folders under `tests/` for storing unit/integration tests and fixtures.
- **Documentation**:
  - `docs/GETTING_STARTED.md` — onboarding and Copilot CLI tips
  - `docs/BEST_PRACTICES.md` — conventions, testing strategies, and security notes
- **Skills** (`.claude/skills/`): Reusable instructions and skills for Copilot workflows, complementing the challenge documentation.

## 🤖 Using Copilot CLI Here

- Open a challenge markdown file and ask Copilot to explain the problem, outline approaches, or draft test cases.
- Iterate on your solution while requesting refactors, complexity analysis, or alternative strategies.
- Use the best practices doc as a checklist for prompting and review.

## 🛠️ Development

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
- [Awesome GitHub Copilot](https://github.com/github/awesome-copilot) — community-curated custom agents, prompts, instructions, and skills to enhance Copilot.
- [Superpowers](https://github.com/obra/superpowers) — composable skills and instructions powering subagent-driven development workflows.

## 📄 License

See [LICENSE](LICENSE) for details.
