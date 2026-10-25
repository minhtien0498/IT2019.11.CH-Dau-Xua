#!/usr/bin/env python3
"""Xuất PDF khổ A4 từ DOCX bằng Quick Look và Chrome trên macOS."""

from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path


CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
A4_PRINT_STYLE = """
<style id="dau-xua-print-style">
@page {
    size: A4;
    margin: 0 0 10mm;
    @bottom-center {
        content: counter(page);
        font-family: "Times New Roman", serif;
        font-size: 10pt;
    }
}
tr, table, img { break-inside: avoid; }
p:has(+ table) { break-after: avoid; }
p:has(a[name="tài-liệu-tham-khảo"]) { break-before: page; }
</style>
"""


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def export_pdf(source: Path, destination: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"Không tìm thấy file nguồn: {source}")
    if not CHROME.is_file():
        raise FileNotFoundError(f"Không tìm thấy Google Chrome: {CHROME}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="dau-xua-pdf-") as temp_name:
        temp_dir = Path(temp_name)
        run(["qlmanage", "-p", "-o", str(temp_dir), str(source.resolve())])

        preview_files = list(temp_dir.rglob("Preview.html"))
        if len(preview_files) != 1:
            raise RuntimeError("Quick Look không tạo được một file Preview.html duy nhất")

        preview = preview_files[0]
        html = preview.read_text(encoding="utf-8")
        if "</head>" not in html:
            raise RuntimeError("Không tìm thấy phần head trong bản xem trước")
        preview.write_text(
            html.replace("</head>", f"{A4_PRINT_STYLE}</head>", 1),
            encoding="utf-8",
        )

        run(
            [
                str(CHROME),
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={destination.resolve()}",
                preview.as_uri(),
            ]
        )

    if not destination.is_file() or destination.stat().st_size == 0:
        raise RuntimeError("File PDF không được tạo thành công")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="File DOCX nguồn")
    parser.add_argument("destination", type=Path, help="File PDF đầu ra")
    args = parser.parse_args()
    export_pdf(args.source, args.destination)
    print(f"Đã tạo: {args.destination}")


if __name__ == "__main__":
    main()
