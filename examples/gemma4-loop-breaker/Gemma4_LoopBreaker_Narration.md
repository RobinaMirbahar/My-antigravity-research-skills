# Gemma 4 LoopBreakerEngine — Explainer Video Narration Guide

| Time | On-Screen Milestone | Narration (Plain English) |
| :--- | :--- | :--- |
| `0:00 - 0:01` | Turn 1–4 Setup | A quantized 4-bit Gemma 4 31B agent starts cleanly when calibrated at T=1.0 with a 6-relation AST parser. |
| `0:01 - 0:03` | The 14.3k Compaction Cliff | Without pruning, failed pytest tracebacks push KV tokens above 14,336, starving the bug spec of attention. |
| `0:03 - 0:04` | G-CCR Sawtooth Reset | LoopBreakerEngine detects repeated errors or low action entropy, prunes noisy turns, and injects a 150-token Negative Constraint Ledger. |
| `0:04 - 0:06` | Headline Benchmark Gains | Active KV drops by 70.8%, end-to-end resolution doubles from 11.6% to 24.0%, and Trap-25 recovery jumps from 16% to 96%! |
