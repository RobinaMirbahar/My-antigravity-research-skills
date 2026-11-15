---
name: agy-frontier-gap-radar
description: >-
  Orchestrate multi-angle scholarly retrieval (OpenAlex, arXiv, Europe PMC, Crossref) to produce
  an A4 Frontier Gap Radar & Q1 Research Blueprint PDF featuring thematic synthesis, capability
  coverage heatmaps, evidence-backed blind spots, and novelty-checked research designs.
---

# Frontier Gap Radar & Q1 Blueprint (`agy-frontier-gap-radar`)

Synthesize 18–25 recent papers on any scientific or engineering topic into a structured A4 **Frontier Gap Radar & Research Blueprint PDF**. Designed to leverage Google Antigravity's parallel agent workflows (`run_workflow` / subagents) and scholarly search tools (`literature-search-openalex`, `literature-search-arxiv`, `literature-search-europepmc`, `search_web`).

## Execution Workflow

1. **Parallel Multi-Angle Retrieval & Deduplication**: Query 5–6 orthogonal sub-facets (theory, algorithms, systems constraints, benchmarks, deployment failure modes). Upgrade arXiv preprints to peer-reviewed venues whenever published and tag remaining preprints explicitly.
2. **Capability Matrix & Blind-Spot Extraction**: Build an `N Papers x 7 Capability Dimensions` matrix; dimensions with `<= 2` studies define empirical blind spots (`G1..G7`) backed by exact paper IDs and metrics.
3. **Novelty-Checked Q1 Blueprints**: Formulate concrete follow-up research architectures (`B1..B6`), run targeted novelty queries against prior art, plot a 300-DPI **Capability Heatmap + Impact-vs-Compute Radar**, and compile into a visually inspected A4 PDF via `agy_pdf_tools.py`.
