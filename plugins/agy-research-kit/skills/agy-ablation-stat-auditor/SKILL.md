---
name: agy-ablation-stat-auditor
description: >-
  Audit ML and systems research benchmarks for statistical rigor: recompute Wilson 95% score CIs,
  Fisher's Exact and McNemar paired p-values, leaderboard noise floors, and multi-seed power bounds.
  Activate when auditing paper tables, checking ablation significance, or writing benchmark sections.
---

# Ablation & Statistical Auditor (`agy-ablation-stat-auditor`)

Perform forensic statistical verification on machine learning, agentic coding, and scientific benchmark tables. Prevents over-interpreting noisy small-sample leaderboard draws and equips papers with exact non-asymptotic confidence intervals and paired hypothesis tests.

## What This Skill Audits

1. **Exact Wilson 95% Score Intervals (`k / n`)**: Replaces flawed normal approximations ($p \pm 1.96\sqrt{p(1-p)/n}$) that break near `0%`, `100%`, or small `N` (`N < 150`).
2. **Paired vs. Unpaired Hypothesis Tests**:
   - **McNemar's Exact Test** when comparing two models/configs on the *same* `N` task instances (`b` wins vs. `c` losses).
   - **Two-Sided Fisher's Exact Test** for independent contingency tables (e.g., controlled fault-injection suites).
   - **Wilcoxon Signed-Rank Test** for skewed resource metrics (KV-cache tokens, latency, VRAM, wall-clock seconds).
3. **Leaderboard Noise Floor & Winner's Curse Analysis**:
   - Computes standard error $\text{SE} = \sqrt{p(1-p)/N}$ and minimum detectable lift at 80% statistical power ($\Delta_{80\%} \approx 2.80 \times \text{SE}$), explaining why small single-seed leaderboards (`N = 50..60`) mask genuine 3–5 point engineering improvements.

## Execution Workflow

1. Call the bundled `agy_research_audit` MCP tools (`verify_wilson_ci`, `verify_fisher_exact`, `leaderboard_noise_floor`) when loaded, or run a PEP 723 script via `uv run --with scipy --with numpy audit_stats.py`.
2. Output a structured **Statistical Audit Report** (`Claim | Paper Value | Exact Recomputed CI / p-value | Power Verdict`) plus publication-ready Markdown/LaTeX table rows.
