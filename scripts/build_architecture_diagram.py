"""Generate Original 5-Pillar Architecture Diagram for Antigravity Research Engineering Kit.

# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib>=3.8.0",
# ]
# ///
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(r"f:\Antigravity\kaggle\My-antigravity-research-skills\assets\agy_research_kit_architecture.png")
OUT.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    fig, ax = plt.subplots(figsize=(12.4, 4.8), dpi=260)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 12.4)
    ax.set_ylim(0, 4.8)
    ax.axis("off")

    ax.text(
        6.2, 4.48,
        "Google Antigravity Research Engineering Kit (agy-research-kit)",
        ha="center", va="center", fontsize=13.5, fontweight="bold", color="#0F172A"
    )
    ax.text(
        6.2, 4.14,
        "8 Progressive-Disclosure Skills  ·  Stdio Statistical & DOI MCP Server  ·  PostToolUse Safety Hooks  ·  Interactive HTML5 Paper Studio",
        ha="center", va="center", fontsize=9.0, color="#475569"
    )

    # Top Plugin Primitives Bar
    prims = [
        (0.30, "#EFF6FF", "#1D4ED8", "plugin.json + rules/AGENTS.md", "Always-On Metric Provenance\n& Visual Montage QA Gate"),
        (3.32, "#F0FDF4", "#15803D", "mcp_config.json (Stdio MCP)", "verify_wilson_ci · fisher_exact\nleaderboard_noise · crossref_doi"),
        (6.34, "#FEF3C7", "#B45309", "hooks.json (Lifecycle Guard)", "PostToolUse Guard Blocking\nStdlib Shadowing (numbers.py)"),
        (9.36, "#FDF2F8", "#BE185D", "PEP 723 uv Micro-Runtimes", "Headless Chrome PDF · PyMuPDF\nimageio-ffmpeg 1080p MP4"),
    ]
    for x0, bg, bd, title, sub in prims:
        ax.add_patch(FancyBboxPatch((x0, 3.06), 2.74, 0.84, boxstyle="round,pad=0.04,rounding_size=0.09",
                                    facecolor=bg, edgecolor=bd, linewidth=1.4))
        ax.text(x0 + 1.37, 3.69, title, ha="center", va="center", fontsize=7.8, fontweight="bold", color=bd)
        ax.text(x0 + 1.37, 3.30, sub, ha="center", va="center", fontsize=6.8, color="#1E293B")

    # 8 Original Skills (2x4 Grid)
    skills = [
        ("agy-interactive-paper-studio", "Live HTML5/Canvas Slider\nSimulator (GitHub Pages)", "#ECFEFF", "#0E7490"),
        ("agy-ablation-stat-auditor", "Wilson CI, McNemar, Fisher\n& Leaderboard Power Bounds", "#F0FDF4", "#15803D"),
        ("agy-citation-doi-verifier", "Live Crossref + OpenAlex\nDOI & Venue Upgrade Gate", "#FEFCE8", "#A16207"),
        ("agy-figure-forensics", "300-DPI Vector Callouts &\nVisual Anatomy Dossier PDF", "#EFF6FF", "#1D4ED8"),
        ("agy-math-sandbox", "Color Operator Blocks +\nNumPy/SciPy Monte Carlo PDF", "#F5F3FF", "#6D28D9"),
        ("agy-trajectory-cinematics", "16:9 1080p Telemetry Sweep\nMP4 + Voice-Over Cues", "#FFF7ED", "#C2410C"),
        ("agy-graphic-story", "Pure-Code Vector SVG\nTechnical Graphic-Novel PDF", "#FDF2F8", "#BE185D"),
        ("agy-frontier-gap-radar", "Multi-Agent Capability Matrix\n& Q1 Research Blueprints", "#F8FAFC", "#334155"),
    ]

    for idx, (name, desc, bg, bd) in enumerate(skills):
        r, c = divmod(idx, 4)
        x0 = 0.30 + c * 3.02
        y0 = 1.72 - r * 1.24
        ax.add_patch(FancyBboxPatch((x0, y0), 2.74, 1.04, boxstyle="round,pad=0.04,rounding_size=0.09",
                                    facecolor=bg, edgecolor=bd, linewidth=1.35))
        ax.text(x0 + 1.37, y0 + 0.78, name, ha="center", va="center", fontsize=7.6, fontweight="bold", color=bd)
        ax.text(x0 + 1.37, y0 + 0.34, desc, ha="center", va="center", fontsize=7.3, color="#1E293B")

    ax.text(
        6.2, 0.18,
        "Author: Robina Mirbahar (Google Developer Expert in AI & Cloud)  ·  github.com/RobinaMirbahar/My-antigravity-research-skills",
        ha="center", va="center", fontsize=8.2, color="#475569", fontweight="bold"
    )

    fig.savefig(OUT, dpi=260, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Saved:", OUT)


if __name__ == "__main__":
    main()
