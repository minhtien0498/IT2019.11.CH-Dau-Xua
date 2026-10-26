#!/usr/bin/env python3
"""Xuất PDF từ tài liệu đang mở trong Microsoft Word trên macOS."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
import time
import uuid
from pathlib import Path


WORD_CONTAINER = Path.home() / "Library/Containers/com.microsoft.Word/Data/Documents"
DOCUMENT_PATH_SCRIPT = r'''
on run argv
    tell application "Microsoft Word"
        if exists document (item 1 of argv) then
            set documentPath to full name of document (item 1 of argv)
            return POSIX path of (documentPath as alias)
        end if
    end tell
    return ""
end run
'''
EXPORT_SCRIPT = r'''
on run argv
    set pdfPath to (POSIX file (item 2 of argv)) as text
    tell application "Microsoft Word"
        with timeout of 180 seconds
            save as document (item 1 of argv) file name pdfPath file format format PDF
        end timeout
    end tell
end run
'''


def word_script(script: str, *args: str) -> str:
    result = subprocess.run(
        ["osascript", "-", *args],
        input=script,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def ensure_document_open(source: Path) -> None:
    for attempt in range(16):
        opened = word_script(DOCUMENT_PATH_SCRIPT, source.name)
        if opened:
            if not os.path.samefile(opened, source):
                raise RuntimeError(
                    f"Word đang mở tài liệu khác cùng tên: {opened}. "
                    "Hãy đóng tài liệu đó rồi chạy lại."
                )
            return
        if attempt == 0:
            subprocess.run(["open", "-a", "Microsoft Word", str(source)], check=True)
        time.sleep(1)
    raise RuntimeError(f"Word chưa mở được tài liệu: {source}. Hãy mở file trong Word rồi chạy lại.")


def export_pdf(source: Path, destination: Path) -> None:
    source = source.resolve(strict=True)
    destination = destination.resolve()
    if source.suffix.lower() != ".docx":
        raise ValueError("File nguồn phải là DOCX")
    if not WORD_CONTAINER.is_dir():
        raise FileNotFoundError("Không tìm thấy Microsoft Word hoặc thư mục dữ liệu của ứng dụng")

    ensure_document_open(source)
    word_pdf = WORD_CONTAINER / f"codex-word-export-{uuid.uuid4().hex}.pdf"
    try:
        word_script(EXPORT_SCRIPT, source.name, str(word_pdf))
        if not word_pdf.is_file() or word_pdf.stat().st_size < 1000:
            raise RuntimeError("Microsoft Word không tạo được PDF")
        with word_pdf.open("rb") as pdf_file:
            if pdf_file.read(4) != b"%PDF":
                raise RuntimeError("File Word xuất ra không phải PDF hợp lệ")

        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            prefix=".word-export-", suffix=".pdf", dir=destination.parent, delete=False
        ) as staging_file:
            staging = Path(staging_file.name)
        try:
            shutil.copy2(word_pdf, staging)
            staging.replace(destination)
        finally:
            staging.unlink(missing_ok=True)
    finally:
        word_pdf.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="File DOCX nguồn")
    parser.add_argument("destination", type=Path, help="File PDF đầu ra")
    args = parser.parse_args()
    export_pdf(args.source, args.destination)
    print(f"Đã xuất từ Microsoft Word: {args.destination}")


if __name__ == "__main__":
    main()
