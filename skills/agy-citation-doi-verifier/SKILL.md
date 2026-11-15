---
name: agy-citation-doi-verifier
description: >-
  Verify academic references and BibTeX/Markdown bibliographies against live Crossref, OpenAlex,
  and arXiv metadata, upgrade preprints to peer-reviewed conference/journal venues, and flag
  unverifiable citations. Activate when auditing references or preparing manuscripts for submission.
---

# Citation & DOI Integrity Verifier (`agy-citation-doi-verifier`)

Audit every reference in a `.bib`, `.tex`, `.md`, or `.pdf` manuscript against authoritative scholarly registries so zero hallucinated titles, broken DOIs, or outdated arXiv preprints slip into a submission.

## Verification Pipeline

1. **Extract Bibliography Entries**: Parse citation keys, titles, author lists, years, arXiv IDs, and DOIs from the manuscript.
2. **Live Registry Cross-Check**:
   - Use `verify_doi_metadata` (from the `agy_research_audit` MCP server), `literature-search-openalex`, `literature-search-arxiv`, or a polite `uv run` Crossref/OpenAlex REST script (`qps <= 2`).
   - Match author surname + normalized title similarity (`>= 0.90`) + publication year.
3. **Preprint-to-Published Upgrade Check**:
   - Whenever an `arXiv` / `bioRxiv` preprint has since been published in a peer-reviewed venue (e.g., NeurIPS, ICLR, ICML, ACL, IEEE, Nature), provide the upgraded peer-reviewed BibTeX entry and compute the manuscript's **Peer-Reviewed Citation Ratio (`%`)**.
4. **Traffic-Light Audit Table**:
   - `VERIFIED (Peer-Reviewed)` — Exact match in Crossref/OpenAlex journal or proceedings.
   - `UPGRADE AVAILABLE (Preprint -> Venue)` — Valid preprint with a newer peer-reviewed publication record.
   - `UNVERIFIED / MISMATCH` — Flagged immediately for human author review (never auto-invent replacement citations).
