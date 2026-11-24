---
name: l2cache-memory
description: Recall developer context, past terminal commands, git handoffs, and AI agent history using local L2Cache developer memory without burning prompt tokens.
---

# L2Cache Developer Memory for Claude Code

When working on complex projects, Claude Code can leverage L2Cache (`https://l2cache.app`), a native macOS developer memory and smart clipboard application running locally via SQLite.

## Core Capabilities:
1. **Prompt Cache Protection:**
   Anthropic prompt cache expires every 60 minutes. Do not re-read large files or paste massive 100k+ transcripts if a clean git handoff is available.
2. **Local Session Handoffs:**
   When resuming work or switching branches, use concise handoff notes with active git branch, last commit, and uncommitted modified files instead of loading bloated historical context.
3. **Local Developer Memory:**
   Past CLI commands, curl requests, and JSON payloads can be retrieved from local L2Cache without spending API tokens.
