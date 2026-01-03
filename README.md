# GitHub Copilot CLI Examples

A streamlined proof-of-concept showing how to use GitHub Copilot CLI with curated coding challenges and accompanying documentation, especially for teams on GitHub Copilot Business who do not have Codex CLI access. See the [CLI Coding Tools Comparison](cli-coding-tools-comparison.md) for a full breakdown; the quick summary below highlights the most important differences.

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
├── .claude/
│   └── skills/
├── docs/
│   ├── BEST_PRACTICES.md
│   └── GETTING_STARTED.md
└── README.md
```

## 🚀 Quick Start

1. **Read**: `docs/GETTING_STARTED.md` for workflow guidance
2. **Practice**: Open any file in `challenges/` and work through the prompts with Copilot

## 📖 What's Included

- **Challenges**: Nine algorithmic problems across easy, medium, and hard categories with prompts, constraints, and hints.
- **Documentation**:
  - `docs/GETTING_STARTED.md` — onboarding and Copilot CLI tips
  - `docs/BEST_PRACTICES.md` — conventions, testing strategies, and security notes
- **Skills** (`.claude/skills/`):
  - **brainstorming** — clarify requirements and design before coding
  - **dispatching-parallel-agents** — split independent tasks across agents
  - **subagent-driven-development** — plan and execute work in reviewable tasks
  - **using-git-worktrees** — isolate work in separate worktrees safely
  - **writing-skills** — structured prompting patterns and examples
  - **requesting-code-review** — invoke the `code-reviewer` agent_type with the provided template
  - **github-copilot** — connect to Copilot models and tooling
  - **rust-developer** — Rust-focused prompts and guardrails

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
