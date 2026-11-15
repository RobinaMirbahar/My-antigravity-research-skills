---
name: agy-figure-forensics
description: >-
  Dissect research paper architectures and empirical plots into an annotated A4 Visual Anatomy PDF
  with numbered vector callouts, regime shading, "Visual Anatomy" decode steps, and "Engineering Takeaway" cards.
  Activate when asked to break down, annotate, or explain a paper's figures.
---

# Figure Forensics & Visual Anatomy (`agy-figure-forensics`)

Turn dense research figures, multi-panel ablations, and architecture diagrams into a crystal-clear A4 **Visual Anatomy Dossier PDF**. Every figure receives numbered callout badges (`1`, `2`, `3`...), shaded failure/gain regimes, a structured **Visual Anatomy** decode card, and an **Engineering Takeaway** summary.

## Execution Workflow

1. **Map the Narrative Arc (`ARCHITECTURE -> MECHANISM -> EMPIRICAL GAIN`)**:
   - Identify how each figure advances the paper's central thesis and extract every exact number quoted in the text.
2. **Vector Extraction or High-DPI Badge Overlay (`uv run`)**:
   - Extract vector paths via PyMuPDF (`pymupdf`) or overlay crisp circular badges on 300-DPI source PNGs via `matplotlib` (`bbox_inches="tight"`), keeping badges in clean margins away from tick labels.
3. **Render Cross-Platform A4 PDF + Montage QA**:
   - Compile via `uv run scripts/agy_pdf_tools.py render --html Anatomy.html --pdf <Paper>_Figure_Anatomy_v1.pdf`.
   - Inspect the generated PyMuPDF montage PNG with `read_file` to guarantee zero overlapping badges or split cards before delivering.
