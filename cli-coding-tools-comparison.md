# CLI Coding Tools Comparison: Claude Code vs OpenAI Codex CLI vs GitHub Copilot CLI

*Last updated: January 3, 2026*

This comparison covers the three major AI-powered CLI coding agents based on their latest release notes and documentation.

## Overview

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Developer** | Anthropic | OpenAI | GitHub/Microsoft |
| **Release Status** | GA — latest v2.0.74 | Stable v0.77.0 (0.78.0-alpha pre-releases) | Public Preview — latest v0.0.374 |
| **Open Source** | ❌ No (closed source) | ✅ Yes (Apache-2.0) | ❌ No (closed source) |
| **Default Model** | Claude Sonnet 4 / Opus 4.5 | GPT-5.x-Codex (configurable) | Claude Sonnet 4.5 |
| **Primary Language** | TypeScript/Node.js | Rust | TypeScript/Node.js |
| **GitHub Releases** | [anthropics/claude-code](https://github.com/anthropics/claude-code/releases) | [openai/codex](https://github.com/openai/codex/releases) | [github/copilot-cli](https://github.com/github/copilot-cli/releases) |

> **Note on source availability:** Only OpenAI Codex CLI publishes its full source code (Rust). Claude Code and GitHub Copilot CLI repos contain releases, changelogs, and documentation only - not the actual source code.

## Context Management

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Auto Context Compaction** | ✅ Yes (instant as of v2.0.64) | ✅ Yes (native compaction) | ✅ Yes (at 95% limit, v0.0.374) |
| **Manual Compaction** | ✅ `/compact` command | ✅ `codex resume` | ✅ `/compact` command (v0.0.374) |
| **Context Preservation Instructions** | ✅ Custom preservation prompts | ✅ Automatic summarization | ⚠️ Automatic only |
| **Context Visualization** | ✅ `/context` command | ✅ Token usage display | ✅ `/context` command |
| **Context Meter** | ✅ Visual indicator | ✅ Warning at limit | ✅ Warning at ≤20% |
| **MCP Context Optimization** | ✅ Disable unused servers | ✅ Configurable limits | ⚠️ Basic support |

## Session Management

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Session Resume** | ✅ `/resume` command | ✅ `codex resume` | ✅ `--resume` flag |
| **Continue Last Session** | ✅ `--continue` flag | ✅ `--continue` flag | ✅ `--continue` flag |
| **Session Naming/Renaming** | ✅ `/rename` command | ✅ Supported | ⚠️ Limited |
| **Session Search** | ✅ Search past sessions | ⚠️ Basic | ❌ Feature requested |
| **Session Stats** | ✅ `/stats` command | ✅ Usage tracking | ✅ `/usage` command |
| **Session Forking** | ✅ `--fork-session` | ❌ Not available | ❌ Not available |
| **Session Export** | ✅ `/export` command | ⚠️ Basic | ✅ `/share` command |

## Web & Network Features

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Built-in Web Search** | ❌ Via MCP servers | ✅ Native web search | ❌ Via MCP servers |
| **Web Fetch** | ✅ URL fetching | ✅ Native support | ✅ Built-in `web_fetch` (v0.0.374) |
| **Network Access Control** | ✅ Domain allowlists | ✅ Sandbox + allowlist | ✅ URL permission controls |
| **Image URL Fetching** | ✅ Supported | ✅ Supported | ✅ Supported |

## MCP (Model Context Protocol) Support

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **MCP Client** | ✅ Full support | ✅ Full support | ✅ Full support |
| **MCP Server** | ✅ Acts as server too | ⚠️ Client only | ⚠️ Client only |
| **HTTP Transport** | ✅ Recommended | ✅ Supported | ✅ Supported |
| **SSE Transport** | ⚠️ Deprecated | ✅ Supported | ⚠️ Limited |
| **stdio Transport** | ✅ Supported | ✅ Supported | ✅ Supported |
| **OAuth for MCP** | ✅ Supported | ✅ Supported | ✅ Supported |
| **Built-in MCP Servers** | ❌ Install separately | ❌ Install separately | ✅ GitHub MCP included |
| **MCP Debug Mode** | ✅ `--mcp-debug` flag | ⚠️ Limited | ⚠️ Limited |

## Agent & Automation Features

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Async Subagents** | ✅ Background tasks (Ctrl-b) | ❌ Not available | ✅ Built-in subagents (v0.0.374) |
| **Agent Skills** | ✅ Skill folders | ✅ `$skill-name` syntax | ✅ Agent Skills support |
| **Custom Agents** | ✅ `.claude/agents/` | ⚠️ Via skills | ✅ Custom agent profiles |
| **Hooks System** | ✅ 7+ hook types | ⚠️ Limited | ⚠️ Limited |
| **Headless/Programmatic Mode** | ✅ `-p` flag | ✅ Supported | ✅ `-p` flag |
| **CI/CD Integration** | ✅ GitHub Actions | ✅ GitHub Actions | ✅ Native GitHub integration |
| **Cloud Agent Delegation** | ❌ Local only | ✅ Codex cloud | ✅ `/delegate` command |

## Git & GitHub Integration

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Git Operations** | ✅ Via `gh` CLI | ✅ Native | ✅ Native (best-in-class) |
| **GitHub Issues** | ✅ Via MCP/CLI | ✅ Via GitHub integration | ✅ Native support |
| **Pull Request Creation** | ✅ Supported | ✅ Supported | ✅ Native + delegation |
| **Code Review** | ⚠️ Manual | ✅ Codex Code Review | ✅ Automated PR reviews |
| **Branch Management** | ✅ Supported | ✅ Supported | ✅ Native support |

## Code Intelligence & Tools

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **LSP Integration** | ✅ Go-to-definition, references | ⚠️ Basic | ⚠️ Basic |
| **Code Search (ripgrep)** | ✅ Bundled | ✅ Native fuzzy search | ✅ Bundled ripgrep |
| **File Editing** | ✅ Multi-tool support | ✅ Native | ✅ Native |
| **Undo Support** | ✅ Supported | ✅ `/undo` command | ⚠️ Limited |
| **Diff Preview** | ✅ Visual diffs | ✅ Visual diffs | ✅ Visual diffs |

## Input & UI Features

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Image Input** | ✅ Paste/drag-drop | ✅ Paste/drag-drop | ✅ `@` mention + paste |
| **Multi-line Input** | ✅ Shift+Enter | ✅ Supported | ✅ Kitty protocol |
| **Vim Bindings** | ✅ `/vim` command | ❌ Not available | ❌ Not available |
| **Thinking Mode** | ✅ 'think'/'ultrathink' | ✅ Reasoning effort levels | ⚠️ Model-dependent |
| **Prompt Suggestions** | ✅ Tab to accept | ⚠️ Limited | ⚠️ Limited |
| **Syntax Highlighting** | ✅ Configurable | ✅ Supported | ✅ Supported |
| **IME Support (CJK)** | ✅ Full support | ⚠️ Basic | ⚠️ Basic |

## Model Support

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Model Switching** | ✅ `/model` command | ✅ `/model` command | ✅ `/model` command |
| **Default Model** | Claude Sonnet 4 | GPT-5.2-Codex | Claude Sonnet 4.5 |
| **Available Models** | Claude family (Opus, Sonnet, Haiku) | GPT-5.x-Codex variants | Multi-vendor (Claude Sonnet 4.5, Claude Sonnet 4, GPT-5, etc.) |
| **Third-party Models** | ✅ Via Bedrock/Vertex | ⚠️ OpenAI only | ✅ Claude, GPT, Gemini |
| **Custom Model Config** | ✅ config.toml | ✅ config.toml | ✅ Settings / COPILOT_MODEL env |
| **Reasoning Effort** | ✅ Thinking modes | ✅ low/medium/high/xhigh | ⚠️ Model-dependent |

## Custom Instructions & Memory

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Project Instructions** | ✅ CLAUDE.md / .claude/rules/ | ✅ AGENTS.md / codex.md | ✅ AGENTS.md / copilot-instructions.md |
| **Custom Slash Commands** | ✅ .claude/commands/ | ✅ Skills system | ✅ Custom commands |
| **Memory Persistence** | ✅ Project memory files | ⚠️ Via instructions | ⚠️ Via instructions |
| **Agent Skills** | ✅ `.claude/skills/` | ✅ `$skill-name` syntax | ✅ `.github/skills/` (recommended) or `.claude/skills/` |

> **Note:** GitHub Copilot CLI supports skills in both `.github/skills/` (recommended for new skills) and `.claude/skills/` (legacy/backward compatibility). This enables cross-tool skill portability with Claude Code.

## Platform Support

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **macOS** | ✅ Full support | ✅ Full support | ✅ Full support |
| **Linux** | ✅ Full support (incl. Alpine) | ✅ Full support | ✅ Full support |
| **Windows** | ✅ Native + WSL | ✅ Native (improved in 5.2) | ✅ WSL only |
| **IDE Extension** | ✅ VS Code extension | ✅ VS Code/Cursor extension | ⚠️ Planned |

## Pricing & Access

| Feature | Claude Code | OpenAI Codex CLI | GitHub Copilot CLI |
|---------|-------------|------------------|-------------------|
| **Pricing Model** | API usage / Max plan flat rate | ChatGPT subscription / API | Copilot subscription |
| **Free Tier** | ❌ No | ⚠️ Limited credits | ❌ No |
| **Plans** | API pay-as-you-go, Max ($200/mo) | Plus ($20), Pro ($200) | Pro ($10), Pro+ ($39), Business, Enterprise |
| **Rate Limits** | Per-minute token limits | Premium request quotas | Premium request quotas |

## Latest Notable Features (Dec 2025)

### Claude Code (v2.0.74 / v2.0.73)
- Added LSP tool for go-to-definition, references, and hover docs (v2.0.74)
- `/terminal-setup` support for Kitty, Alacritty, Zed, Warp; ctrl+t toggle for syntax highlighting; theme picker improvements
- Search filtering in plugin discover; clickable image links; session forking with custom session IDs
- Fixes across skills allowed-tools handling, Opus 4.5 tip display, input history, and keyboard shortcut labeling

### OpenAI Codex CLI (v0.77.0 with 0.78.0-alpha series)
- TUI scroll normalization and new `tui.scroll_*` config settings
- `allowed_sandbox_modes` in `requirements.toml` to constrain sandbox modes
- MCP OAuth login no longer needs `rmcp_client` feature flag; improved fuzzy file search; updated bundled model metadata
- Ongoing 0.78.0-alpha pre-releases (rust-v0.78.0-alpha.2–10) focus on performance and interoperability

### GitHub Copilot CLI (v0.0.374 - Jan 2, 2026)
- **Auto-compaction at 95% token limit and `/compact` command** ⭐ NEW
- **Built-in subagents** for exploring and managing tasks ⭐ NEW
- **Built-in `web_fetch` tool** for fetching web content ⭐ NEW
- Model picker improvements with settings link for unavailable models; MCP server type help text corrections
- Tab completion for path arguments in `/cwd` and `/add-dir` (v0.0.373)
- `/context` command for token usage visualization and `--resume` for remote sessions (v0.0.372)
- URL permission controls for web-accessing commands (v0.0.372)

## Summary Recommendations

| Use Case | Recommended Tool |
|----------|------------------|
| **Best Context Management** | Claude Code (instant compaction, manual control with preservation) |
| **Best GitHub Integration** | GitHub Copilot CLI (native GitHub context, Issues, PRs) |
| **Best Cloud Agent** | OpenAI Codex CLI (cloud execution, code review) |
| **Best for Windows** | OpenAI Codex CLI (native support improved) |
| **Best MCP Ecosystem** | Claude Code (server + client, largest ecosystem) |
| **Best Multi-Model Support** | GitHub Copilot CLI (Claude, GPT, Gemini) |
| **Best for Teams/Enterprise** | GitHub Copilot CLI (governance, policies) |
| **Best Local-First** | Claude Code (no cloud dependency) |
| **Best Value** | GitHub Copilot CLI (included with Copilot sub) |
| **Most Feature-Complete** | All three are now highly capable - choice depends on ecosystem preference |

> **Note (Jan 2026):** GitHub Copilot CLI v0.0.374 significantly closed the feature gap by adding auto-compaction, subagents, and web_fetch - making all three tools competitive on core features.

---

*Note: Features and capabilities change rapidly. Always check official documentation for the most current information.*

**Sources:**
- [Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [OpenAI Codex Changelog](https://developers.openai.com/codex/changelog/)
- [GitHub Copilot CLI Releases](https://github.com/github/copilot-cli/releases)
