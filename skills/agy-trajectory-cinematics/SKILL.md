---
name: agy-trajectory-cinematics
description: >-
  Render a 16:9 (1920x1080) animated telemetry & parameter-sweep explainer video (.mp4) with a
  synchronized live system state monitor, 2x2 real-time data plots, PEP 723 generator script,
  and timestamped voice-over script. Activate when asked for an animated video explainer of a paper.
---

# Trajectory & Telemetry Cinematics (`agy-trajectory-cinematics`)

Produce a broadcast-clean **1920x1080 H.264 `.mp4` dashboard animation** (plus its reproducible PEP 723 script and timestamped narration `.md`) showing a research paper's system state and 2x2 quantitative curves evolving live across turns, time, or a swept parameter.

## Execution Workflow

1. **Zero-Install Portable Encoding (`imageio[ffmpeg]`)**: Declare `imageio[ffmpeg]`, `matplotlib`, `numpy`, and `pillow` in PEP 723 inline metadata so `uv run` encodes universal `yuv420p` H.264 `.mp4` videos on Windows, macOS, and Linux without requiring a separate system `ffmpeg` setup. Set `macro_block_size=1` or dimensions divisible by 16 (`1920x1088` or `1920x1080` with `macro_block_size=1`) for crisp native resolution.
2. **4-Milestone Visual Preview Gate**: Render 3–4 milestone PNG frames first and inspect them with `read_file` to verify clean `gridspec` margins, non-overlapping legends, and readable bottom milestone banners before encoding the full video.
3. **Deliver `.mp4` + Reproducible `.py` + Narration `.md`**.
