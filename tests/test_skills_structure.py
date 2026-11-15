"""Validate all 8 agy-* SKILL.md manifests, agy-research-kit plugin, MCP server tools, and artifacts.

# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pyyaml>=6.0.1",
#   "scipy>=1.12.0",
#   "numpy>=1.26.0",
# ]
# ///
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "plugins" / "agy-research-kit" / "mcp"))
import research_audit_mcp as mcp_srv  # noqa: E402

EXPECTED_SKILLS = [
    "agy-interactive-paper-studio",
    "agy-ablation-stat-auditor",
    "agy-citation-doi-verifier",
    "agy-figure-forensics",
    "agy-math-sandbox",
    "agy-trajectory-cinematics",
    "agy-graphic-story",
    "agy-frontier-gap-radar",
]


def main() -> int:
    for sname in EXPECTED_SKILLS:
        sfile = ROOT / "skills" / sname / "SKILL.md"
        assert sfile.exists(), f"Missing {sfile}"
        raw = sfile.read_text(encoding="utf-8")
        assert raw.startswith("---\n"), f"{sfile} must start with YAML frontmatter"
        parts = raw.split("---\n", 2)
        meta = yaml.safe_load(parts[1])
        assert meta.get("name") == sname, f"Frontmatter name mismatch in {sfile}: {meta}"
        assert len(meta.get("description", "")) >= 40, f"Description too short in {sfile}"

    # Verify plugin manifest, MCP config, and hooks.json
    plug_dir = ROOT / "plugins" / "agy-research-kit"
    assert json.loads((plug_dir / "plugin.json").read_text(encoding="utf-8"))["name"] == "agy-research-kit"
    assert "agy_research_audit" in json.loads((plug_dir / "mcp_config.json").read_text(encoding="utf-8"))["mcpServers"]
    assert "PostToolUse" in json.loads((plug_dir / "hooks.json").read_text(encoding="utf-8"))["hooks"]

    # Verify MCP statistical tools directly
    ci = mcp_srv.call_tool("verify_wilson_ci", {"successes": 51, "total": 129})
    assert ci["rate_pct"] == 39.53 and 31.4 <= ci["wilson_low_pct"] <= 31.6
    fe = mcp_srv.call_tool("verify_fisher_exact", {"k_method": 24, "n_method": 25, "k_baseline": 4, "n_baseline": 25})
    assert fe["significant_at_0_01"] is True and fe["p_value"] < 1e-7

    # Verify interactive HTML5 studio & showcase files
    assert (ROOT / "docs" / "index.html").exists()
    assert (ROOT / "assets" / "agy_research_kit_architecture.png").exists()

    print("ALL 8 ORIGINAL AGY SKILLS + STDIO MCP SERVER + HOOKS + INTERACTIVE HTML5 STUDIO VERIFIED!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
