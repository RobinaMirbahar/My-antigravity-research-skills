# Antigravity Research Engineering Kit — Grounding, Statistical & Visual QA Rules

Whenever working on scientific papers, ML ablation benchmarks, mathematical derivations, or visual research explainers in this workspace:

1. **Statistical & Metric Provenance**: Every sample size (`N`), confidence interval, p-value, and benchmark percentage must trace directly to repository data or source text. When `agy_research_audit` MCP tools (`verify_wilson_ci`, `verify_fisher_exact`, `leaderboard_noise_floor`) are available, verify confidence intervals and p-values deterministically rather than estimating mentally.
2. **PEP 723 Isolated Micro-Environments (`uv run`)**: Run all numerical audits, plots, headless Chromium PDF builds, and `imageio-ffmpeg` video renders using `uv run` with inline `# /// script` dependencies. Never create scripts named `numbers.py` or `statistics.py` that shadow standard library modules.
3. **Interactive-First & Visual Montage Inspection**: Prefer interactive HTML5/Canvas parameter sandboxes (`agy-interactive-paper-studio`) alongside print-ready A4 PDFs, and always inspect PyMuPDF page montages (`read_file`) to confirm zero overlapping callouts before delivery.
