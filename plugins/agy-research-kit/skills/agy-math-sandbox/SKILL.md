---
name: agy-math-sandbox
description: >-
  Decompose research paper equations, theorems, and bounds into color-coded operator blocks,
  run deterministic Python/NumPy/SciPy numerical sandboxes and Monte Carlo checks, and compile
  an A4 Mathematical Verification Guide PDF. Activate when asked to explain or verify a paper's math.
---

# Mathematical Operator Sandbox & Verifier (`agy-math-sandbox`)

Demystify and computationally verify every equation, proposition, lemma, and control law in a technical paper. Combines color-coded operator pills, plain-English intuition, step-by-step proofs, deterministic `uv run` numerical evaluations, and 300-DPI sensitivity plots in a single A4 PDF.

## Execution Workflow

1. **Operator Dependency Graph**: Trace how structural definitions feed bounds, detectors/estimators, and empirical metrics.
2. **Deterministic Python Sandbox (`verify_math.py`, never `numbers.py`)**:
   - Run `uv run verify_math.py` (`numpy`, `scipy`) at the paper's nominal parameters (`seed=42`) to evaluate every formula numerically and verify closed-form claims via simulation, saving results to `eq_verified_numbers.json`.
3. **Sensitivity & Regime Plots (`matplotlib`)**: Plot how each key formula responds across its critical parameter sweep, marking both the failure regime and calibrated operating point.
4. **A4 PDF Render & Visual QA**: Render via `agy_pdf_tools.py`, inspect the PyMuPDF page montage with `read_file` to ensure zero colliding callout pills, and deliver both the PDF and `eq_verified_numbers.json`.
