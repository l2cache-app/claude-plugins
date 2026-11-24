#!/usr/bin/env python3
"""
L2Cache Statusline for Claude Code
Reads Claude Code session state via stdin, computes prompt cache TTL & rate limits,
and renders a clean, real-time status bar.
"""
import sys
import os
import json
import time
import glob

def get_status():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            return "⚡ L2Cache Active"
        data = json.loads(raw_input)
    except Exception:
        return "⚡ L2Cache Active"

    # Extract Rate Limits
    rate_limits = data.get("rate_limits", {})
    five_hour_pct = rate_limits.get("five_hour", {}).get("used_percentage")
    seven_day_pct = rate_limits.get("seven_day", {}).get("used_percentage")
    
    # Model display
    model_name = data.get("model", {}).get("display_name", "Claude")

    # Context tokens
    ctx = data.get("context_window", {})
    tokens = ctx.get("total_input_tokens", 0)

    # Check project cache age
    cwd = data.get("workspace", {}).get("current_dir", os.getcwd())
    project_slug = cwd.replace("/", "-")
    project_dir = os.path.expanduser(f"~/.claude/projects/{project_slug}")
    
    cache_badge = "🟢 Cache: Warm"
    if os.path.isdir(project_dir):
        files = glob.glob(os.path.join(project_dir, "*.jsonl"))
        if files:
            latest_file = max(files, key=os.path.getmtime)
            mtime = os.path.getmtime(latest_file)
            idle_seconds = time.time() - mtime
            idle_minutes = int(idle_seconds // 60)
            
            if idle_seconds > 3600:
                cache_badge = "\033[1;31m🔴 Cache: EXPIRED (Cold)\033[0m"
            else:
                remaining_m = 60 - idle_minutes
                cache_badge = f"\033[1;32m🟢 Cache: Warm ({remaining_m}m left)\033[0m"

    # Format output components
    parts = [f"\033[1;35m⚡ {model_name}\033[0m", cache_badge]
    
    if five_hour_pct is not None:
        p5 = round(float(five_hour_pct))
        color = "\033[1;31m" if p5 > 80 else ("\033[1;33m" if p5 > 50 else "\033[1;32m")
        parts.append(f"⏱️ 5h: {color}{p5}%\033[0m")
        
    if seven_day_pct is not None:
        p7 = round(float(seven_day_pct))
        color = "\033[1;31m" if p7 > 80 else ("\033[1;33m" if p7 > 50 else "\033[1;34m")
        parts.append(f"📅 7d: {color}{p7}%\033[0m")

    parts.append("\033[90m| L2Cache\033[0m")
    return "  ".join(parts)

if __name__ == "__main__":
    print(get_status())
