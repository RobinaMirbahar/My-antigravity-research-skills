"""Zero-dependency Stdio Model Context Protocol (MCP) Server for Antigravity Research Kit.

# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "scipy>=1.12.0",
#   "numpy>=1.26.0",
# ]
# ///

Exposes deterministic statistical & bibliographic audit tools to Google Antigravity:
1. `verify_wilson_ci` — Exact 95% Wilson score confidence interval for benchmark proportions (k/n).
2. `verify_fisher_exact` — Two-sided Fisher's Exact p-value and odds ratio for 2x2 ablation tables.
3. `leaderboard_noise_floor` — Standard error, 95% CI width, and minimum detectable lift on N-task benchmarks.
4. `verify_doi_metadata` — Live Crossref REST lookup to verify a DOI exists and return peer-reviewed venue metadata.
"""

from __future__ import annotations

import json
import math
import sys
import urllib.parse
import urllib.request
from scipy import stats


TOOLS = [
    {
        "name": "verify_wilson_ci",
        "description": "Compute exact Wilson score confidence interval for k successes out of n benchmark tasks.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "successes": {"type": "integer", "description": "Number of solved/passed tasks (k)"},
                "total": {"type": "integer", "description": "Total number of tasks (n)"},
                "confidence": {"type": "number", "default": 0.95},
            },
            "required": ["successes", "total"],
        },
    },
    {
        "name": "verify_fisher_exact",
        "description": "Compute exact two-sided Fisher's Exact p-value comparing Method A (k1/n1) vs Baseline B (k2/n2).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "k_method": {"type": "integer"},
                "n_method": {"type": "integer"},
                "k_baseline": {"type": "integer"},
                "n_baseline": {"type": "integer"},
            },
            "required": ["k_method", "n_method", "k_baseline", "n_baseline"],
        },
    },
    {
        "name": "leaderboard_noise_floor",
        "description": "Calculate standard error and minimum statistically significant gain (80% power) on an N-task benchmark.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "num_tasks": {"type": "integer", "description": "Number of benchmark instances"},
                "baseline_rate": {"type": "number", "default": 0.25, "description": "Baseline accuracy in [0, 1]"},
            },
            "required": ["num_tasks"],
        },
    },
    {
        "name": "verify_doi_metadata",
        "description": "Verify a scholarly DOI against the public Crossref API and return title, authors, year, and container venue.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "doi": {"type": "string", "description": "DOI string (e.g. '10.1145/3340531.3412757')"},
            },
            "required": ["doi"],
        },
    },
]


def call_tool(name: str, args: dict) -> dict:
    if name == "verify_wilson_ci":
        k, n = int(args["successes"]), int(args["total"])
        conf = float(args.get("confidence", 0.95))
        z = float(stats.norm.ppf(1.0 - (1.0 - conf) / 2.0))
        p = k / n
        denom = 1.0 + z**2 / n
        center = (p + z**2 / (2.0 * n)) / denom
        half = (z * math.sqrt((p * (1.0 - p) + z**2 / (4.0 * n)) / n)) / denom
        return {
            "rate_pct": round(p * 100.0, 2),
            "wilson_low_pct": round((center - half) * 100.0, 2),
            "wilson_high_pct": round((center + half) * 100.0, 2),
            "formatted": f"{p*100:.1f}% (95% Wilson CI [{(center-half)*100:.1f}%, {(center+half)*100:.1f}%])",
        }
    if name == "verify_fisher_exact":
        k1, n1 = int(args["k_method"]), int(args["n_method"])
        k2, n2 = int(args["k_baseline"]), int(args["n_baseline"])
        odds, p_val = stats.fisher_exact([[k1, n1 - k1], [k2, n2 - k2]], alternative="two-sided")
        return {
            "method_rate_pct": round(k1 / n1 * 100.0, 2),
            "baseline_rate_pct": round(k2 / n2 * 100.0, 2),
            "odds_ratio": float(odds) if not math.isinf(odds) else "inf",
            "p_value": float(p_val),
            "significant_at_0_01": bool(p_val < 0.01),
        }
    if name == "leaderboard_noise_floor":
        n = int(args["num_tasks"])
        p = float(args.get("baseline_rate", 0.25))
        se = math.sqrt(p * (1.0 - p) / n)
        ci_half = 1.96 * se
        mde_80 = 2.80 * se
        return {
            "num_tasks": n,
            "std_error_pct": round(se * 100.0, 2),
            "ci_95_half_width_pct": round(ci_half * 100.0, 2),
            "min_detectable_lift_80pct_power_pts": round(mde_80 * 100.0, 2),
        }
    if name == "verify_doi_metadata":
        doi = args["doi"].strip().removeprefix("https://doi.org/")
        url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
        req = urllib.request.Request(url, headers={"User-Agent": "AntigravityResearchKit/1.0 (mailto:research@example.org)"})
        try:
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode("utf-8"))["message"]
            return {
                "verified": True,
                "doi": doi,
                "title": (data.get("title") or [""])[0],
                "venue": (data.get("container-title") or [""])[0],
                "type": data.get("type", ""),
                "year": data.get("issued", {}).get("date-parts", [[None]])[0][0],
            }
        except Exception as exc:
            return {"verified": False, "doi": doi, "error": str(exc)}
    raise ValueError(f"Unknown tool: {name}")


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        msg = json.loads(line)
        mid = msg.get("id")
        method = msg.get("method")
        if method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": mid,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "agy-research-audit-mcp", "version": "1.0.0"},
                },
            }
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        elif method == "tools/list":
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}}) + "\n")
            sys.stdout.flush()
        elif method == "tools/call":
            params = msg.get("params", {})
            out = call_tool(params["name"], params.get("arguments", {}))
            resp = {
                "jsonrpc": "2.0",
                "id": mid,
                "result": {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]},
            }
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
