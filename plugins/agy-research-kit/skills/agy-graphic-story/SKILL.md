---
name: agy-graphic-story
description: >-
  Transform a technical research paper into a pure-code A4 vector SVG Graphic-Novel Story PDF
  with custom characters, architectural blackboards, decision gates, and benchmark scoreboards.
  Activate when asked for a comic, graphic story, or visual storytelling summary of a paper.
---

# Technical Graphic-Novel Studio (`agy-graphic-story`)

Turn complex systems, AI, or scientific papers into an engaging A4 **Vector SVG Graphic-Novel PDF** rendered purely from Python + SVG/HTML via headless Chrome/Edge and PyMuPDF—zero external image-generation APIs and 100% faithful to the paper's exact benchmark numbers.

## Execution Workflow

1. **Cast Technical Archetypes**: Map the paper's system/agent (`robot`), failure bottleneck (`monster`), researcher narrator (`scientist`), rigid baseline (`sergeant`), adaptive method (`explorer`), and threshold detector (`gatekeeper`) using `scripts/story_svg_engine.py`.
2. **Embed Real Data Charts & Scoreboards**: Pair character dialogue with SVG blackboards, bar charts, decision diamonds, and verbatim HTML benchmark tables.
3. **2-Up Montage Visual QA**: Render via `uv run` and inspect every 2-up PNG preview sheet (`read_file`) to verify speech bubbles never occlude character faces, bars, or table rows before delivering the final PDF.
