---
name: agy-interactive-paper-studio
description: >-
  Build a standalone, zero-backend interactive HTML5/Canvas/SVG Paper Explorer Studio (index.html)
  for any research paper so readers can drag live sliders over equations, thresholds, and benchmark
  regimes in real time. Activate when asked for an interactive paper demo, web simulator, or GitHub Pages companion.
---

# Interactive Paper Studio (`agy-interactive-paper-studio`)

Transform any technical research paper into a single-file, zero-dependency interactive web studio (`index.html`) ready for GitHub Pages or inline Antigravity Generative UI preview. Instead of static screenshots, readers manipulate live sliders (e.g., sampling temperature $\tau$, context window size, signal-to-noise ratio, or threshold cutoffs) and watch equations, phase boundaries, and trajectory state machines respond instantaneously at 60 FPS.

## Architecture Blueprint

1. **Top Executive Header**: Paper title, author badges, one-sentence core discovery, and quick-jump tabs (*Live Simulator*, *Architecture Anatomy*, *Ablation Matrix*, *Reproducibility*).
2. **Left Control Deck (`32%` width)**:
   - 3–5 range sliders bound to the paper's true governing parameters (initialized to the paper's exact nominal baseline and optimal operating points).
   - Preset scenario buttons (e.g., *"Unpruned Greedy Baseline"* vs. *"Calibrated + LoopBreaker Optimal"*).
3. **Right Dual-Canvas Telemetry Viewport (`68%` width)**:
   - Live HTML5 `<canvas>` or responsive `<svg>` curves recomputed directly from the paper's exact closed-form equations in vanilla ES6 JavaScript.
   - Live KPI metric cards showing instant delta vs. baseline (green gain badges / rose cliff alerts).
4. **Verbatim Grounding Banner**: Footer table comparing simulated readout at preset points against the exact published paper tables.

## Execution Steps

1. Extract the paper's core equations, threshold detectors, and headline benchmark rows.
2. Verify formulas in Python first (`uv run`) so JavaScript math matches 1:1 to at least 4 decimal places.
3. Author a clean, responsive light-mode `index.html` (CSS Grid, crisp sans-serif + monospace metric pills, zero external CDN breakage offline).
4. Open or screenshot-verify via headless browser / subagent to confirm responsive alignment before delivering `file:///.../index.html`.
