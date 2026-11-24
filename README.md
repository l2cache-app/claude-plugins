# L2Cache Plugins for Claude Code

Official developer productivity plugins and prompt-caching tools for [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code), built by [L2Cache](https://l2cache.app).

---

## Available Plugins

### ⚡ `l2cache` — Developer Memory & Cache Guard
A live prompt-cache watchdog, quota countdown statusline, and native developer memory for Claude Code.

* **Live Cache Watchdog:** Monitors prompt cache TTL (60m) in real-time. Alerts you if your session has gone cold before sending a turn.
* **Dual Quota Statusline:** Displays exact rolling 5-hour quota and weekly usage percentages permanently at the bottom of your terminal.
* **Smart Memory Skill:** Guides Claude Code to leverage local git handoffs (~75 tokens) instead of re-reading raw files (150k+ tokens).

---

## Quick Install in Claude Code

Inside any active Claude Code terminal, run:

```bash
# 1. Add the Amvotech marketplace
/plugin marketplace add amvotech/claude-plugins

# 2. Install the L2Cache plugin
/plugin install l2cache
```

---

## Native Status Line Setup

To display the live L2Cache prompt cache monitor and quota meter at the bottom of Claude Code:

1. In Claude Code, run `/statusline`.
2. Select **Custom Command**.
3. Point to the statusline script:
   ```bash
   ~/.claude/plugins/l2cache/scripts/statusline.sh
   ```

You will see real-time updates on every turn:
```text
⚡ Sonnet 3.7  🟢 Cache: Warm (42m left)  ⏱️ 5h: 18%  📅 7d: 32%  | L2Cache
```

When idle for over 60 minutes, the statusline automatically switches to:
```text
⚡ Sonnet 3.7  🔴 Cache: EXPIRED (Cold)   ⏱️ 5h: 45%  📅 7d: 32%  | L2Cache
```

---

## Companion Tools

* **[cold-resume-guard](https://github.com/amvotech/claude-cold-resume-guard):** External CLI guard preventing cold 175k-token session launches before Claude starts (`brew install amvotech/tap/cold-resume-guard`).
* **[L2Cache for Mac](https://l2cache.app):** Native macOS developer memory, smart clipboard, and AI coding session history.

---

## License

MIT © [Amvotech](https://amvo.store)
