"""Cross-platform HTML-to-PDF and PyMuPDF page-montage renderer for Antigravity Research Skills.

# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pymupdf>=1.24.0",
#   "pillow>=10.0.0",
# ]
# ///

Renders any self-contained HTML/SVG/KaTeX document into a crisp, print-faithful A4 PDF
using headless Google Chrome or Microsoft Edge (zero TeX Live / Playwright binary setup required),
and generates visual inspection montages via PyMuPDF (`fitz`) + Pillow so the agent can verify
zero overlapping callouts, orphan headings, or clipped tables before delivering to the user.
"""

from __future__ import annotations

import argparse
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys

import fitz  # PyMuPDF
from PIL import Image, ImageDraw


BROWSER_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "google-chrome",
    "chromium",
    "chromium-browser",
    "microsoft-edge",
    "msedge",
]


def find_browser() -> str:
    env_bin = os.environ.get("AGY_PDF_BROWSER")
    if env_bin and (Path(env_bin).exists() or shutil.which(env_bin)):
        return env_bin
    for cand in BROWSER_CANDIDATES:
        if Path(cand).exists():
            return cand
        resolved = shutil.which(cand)
        if resolved:
            return resolved
    raise RuntimeError(
        "No Chromium-based browser (Chrome/Edge/Chromium) found for headless HTML-to-PDF rendering. "
        "Set AGY_PDF_BROWSER to your browser binary path."
    )


def html_to_pdf(html_path: Path, pdf_path: Path, wait_ms: int = 1800) -> Path:
    html_path = html_path.resolve()
    pdf_path = pdf_path.resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    browser = find_browser()
    file_url = html_path.as_uri()

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--virtual-time-budget={wait_ms}",
        f"--print-to-pdf={pdf_path}",
        file_url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        raise RuntimeError(
            f"Headless browser failed to produce PDF ({proc.returncode}):\n"
            f"STDOUT: {proc.stdout}\nSTDERR: {proc.stderr}"
        )
    return pdf_path


def pdf_to_montage(
    pdf_path: Path,
    out_dir: Path,
    dpi: int = 110,
    cols: int = 3,
) -> list[Path]:
    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    page_imgs: list[Image.Image] = []
    for idx, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=(180, 190, 205), width=2)
        page_file = out_dir / f"page_{idx + 1:02d}.png"
        img.save(page_file)
        page_imgs.append(img)
    doc.close()

    if not page_imgs:
        return []

    w, h = page_imgs[0].size
    pad = 16
    rows = math.ceil(len(page_imgs) / cols)
    canvas = Image.new(
        "RGB",
        (cols * w + (cols + 1) * pad, rows * h + (rows + 1) * pad),
        (241, 245, 249),
    )
    for idx, im in enumerate(page_imgs):
        r, c = divmod(idx, cols)
        canvas.paste(im, (pad + c * (w + pad), pad + r * (h + pad)))

    montage_path = out_dir / f"{pdf_path.stem}_montage.png"
    canvas.save(montage_path)
    return [montage_path]


def main() -> int:
    parser = argparse.ArgumentParser(description="Render HTML to A4 PDF and build PyMuPDF QA montage.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_render = sub.add_parser("render", help="Convert HTML to PDF and emit QA montage")
    p_render.add_argument("--html", type=Path, required=True, help="Input HTML file")
    p_render.add_argument("--pdf", type=Path, required=True, help="Output PDF file")
    p_render.add_argument("--montage-dir", type=Path, default=None, help="Directory for PNG previews")
    p_render.add_argument("--dpi", type=int, default=110)
    p_render.add_argument("--cols", type=int, default=3)

    p_mont = sub.add_parser("montage", help="Build QA montage from an existing PDF")
    p_mont.add_argument("--pdf", type=Path, required=True, help="Input PDF file")
    p_mont.add_argument("--out-dir", type=Path, required=True, help="Output directory for PNG pages & montage")
    p_mont.add_argument("--dpi", type=int, default=110)
    p_mont.add_argument("--cols", type=int, default=3)

    args = parser.parse_args()
    if args.cmd == "render":
        pdf = html_to_pdf(args.html, args.pdf)
        mdir = args.montage_dir or (args.pdf.parent / f"{args.pdf.stem}_preview")
        sheets = pdf_to_montage(pdf, mdir, dpi=args.dpi, cols=args.cols)
        print(f"OK PDF: {pdf} ({pdf.stat().st_size:,} bytes) | Montage: {[str(s) for s in sheets]}")
    elif args.cmd == "montage":
        sheets = pdf_to_montage(args.pdf, args.out_dir, dpi=args.dpi, cols=args.cols)
        print(f"OK Montage: {[str(s) for s in sheets]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
