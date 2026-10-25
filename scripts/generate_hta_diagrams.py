#!/usr/bin/env python3
"""Generate the HTA SVG and PNG assets used by the Dấu Xưa report."""

from __future__ import annotations

import html
import subprocess
from pathlib import Path


ASSET_DIR = Path(__file__).resolve().parents[1] / "docs" / "02-report" / "figures" / "hta"


DIAGRAMS = [
    {
        "slug": "hta-m1-select-location",
        "goal": ["0. Chọn đúng địa điểm", "đang tham quan"],
        "steps": [
            ["1. Mở", "Dấu Xưa"],
            ["2. Tìm", "địa điểm"],
            ["3. Kiểm tra tên", "và địa chỉ"],
            ["4. Xác nhận", "địa điểm"],
            ["5. Xem danh sách", "hiện vật"],
        ],
        "anchor": 2,
        "children": [
            ["2.1 Dùng vị trí", "hiện tại"],
            ["2.2 Tìm kiếm", "theo tên"],
            ["2.3 Chọn từ", "danh sách"],
        ],
        "plan": "Plan 0: 1 → 2 (chọn 2.1, 2.2 hoặc 2.3) → 3 → 4 → 5; sai địa điểm thì quay lại 2.",
    },
    {
        "slug": "hta-m2-open-exhibit",
        "goal": ["0. Mở đúng nội dung", "của một hiện vật"],
        "steps": [
            ["1. Chọn cách", "mở hiện vật"],
            ["2. Cung cấp", "mã hiện vật"],
            ["3. Ứng dụng", "kiểm tra mã"],
            ["4. Kiểm tra tên", "hiện vật"],
            ["5. Mở", "câu chuyện"],
        ],
        "anchor": 1,
        "children": [
            ["1.1 Quét", "mã QR"],
            ["1.2 Nhập mã", "bằng tay"],
            ["1.3 Chọn từ", "danh sách"],
        ],
        "plan": "Plan 0: 1 (chọn 1.1, 1.2 hoặc 1.3) → 2 → 3 → 4 → 5; không khớp thì quay lại 1.",
    },
    {
        "slug": "hta-m3-short-story",
        "goal": ["0. Nghe câu chuyện ngắn", "có âm thanh và hình ảnh"],
        "steps": [
            ["1. Mở", "hiện vật"],
            ["2. Xem phần", "giới thiệu"],
            ["3. Bắt đầu", "câu chuyện"],
            ["4. Trải nghiệm", "nội dung"],
            ["5. Kết thúc", "câu chuyện"],
        ],
        "anchor": 4,
        "children": [
            ["4.1 Nghe", "lời kể"],
            ["4.2 Xem ảnh", "tư liệu"],
            ["4.3 Đọc bản chép lời", "nếu cần"],
        ],
        "plan": "Plan 0: 1 → 2 → 3 → 4; thực hiện 4.1 và 4.2, dùng 4.3 khi cần → 5.",
    },
    {
        "slug": "hta-m4-player-controls",
        "goal": ["0. Điều khiển", "trình phát câu chuyện"],
        "steps": [
            ["1. Mở", "trình phát"],
            ["2. Phát hoặc", "tạm dừng"],
            ["3. Điều chỉnh", "vị trí nghe"],
            ["4. Theo dõi", "tiến độ"],
            ["5. Bỏ qua hoặc", "kết thúc"],
        ],
        "anchor": 3,
        "children": [
            ["3.1 Tua", "lùi"],
            ["3.2 Tua", "tới"],
            ["3.3 Kéo thanh", "tiến độ"],
        ],
        "plan": "Plan 0: 1 → lặp 2–4 theo nhu cầu → 5; tại 3 chọn 3.1, 3.2 hoặc 3.3.",
    },
    {
        "slug": "hta-m5-audio-description",
        "goal": ["0. Truy cập mô tả", "của hiện vật và hình ảnh"],
        "steps": [
            ["1. Mở", "hiện vật"],
            ["2. Tìm mục", "mô tả"],
            ["3. Chọn dạng", "mô tả"],
            ["4. Nghe hoặc", "đọc mô tả"],
            ["5. Tiếp tục", "câu chuyện"],
        ],
        "anchor": 3,
        "children": [
            ["3.1 Mô tả", "âm thanh"],
            ["3.2 Mô tả chữ", "cho hình ảnh"],
        ],
        "plan": "Plan 0: 1 → 2 → 3 (chọn 3.1 hoặc 3.2) → 4 → 5; có thể dùng cả hai dạng.",
    },
    {
        "slug": "hta-m6-screen-reader",
        "goal": ["0. Hoàn thành luồng chính", "bằng trình đọc màn hình"],
        "steps": [
            ["1. Bật VoiceOver", "hoặc TalkBack"],
            ["2. Chọn", "địa điểm"],
            ["3. Chọn", "hiện vật"],
            ["4. Mở", "câu chuyện"],
            ["5. Điều khiển", "phát"],
            ["6. Chọn nội dung", "tiếp theo"],
        ],
        "anchor": 3,
        "children": [
            ["3.1 Duyệt", "danh sách"],
            ["3.2 Nhập", "mã hiện vật"],
        ],
        "plan": "Plan 0: 1 → 2 → 3 (chọn 3.1 hoặc 3.2) → 4 → 5 → 6; dùng nhãn và tiêu điểm ở mọi bước.",
    },
    {
        "slug": "hta-m7-haptics",
        "goal": ["0. Thiết lập và sử dụng", "tín hiệu rung"],
        "steps": [
            ["1. Mở cài đặt", "trợ năng"],
            ["2. Tìm mục", "Tín hiệu rung"],
            ["3. Chọn", "trạng thái"],
            ["4. Phát", "câu chuyện"],
            ["5. Nhận rung tại", "mốc ý nghĩa"],
            ["6. Thay đổi lại", "nếu cần"],
        ],
        "anchor": 3,
        "children": [
            ["3.1 Bật", "tín hiệu rung"],
            ["3.2 Tắt", "tín hiệu rung"],
        ],
        "plan": "Plan 0: 1 → 2 → 3 (chọn 3.1 hoặc 3.2) → 4; nếu bật thì 5; có thể thực hiện 6 bất cứ lúc nào.",
    },
    {
        "slug": "hta-m8-sources",
        "goal": ["0. Kiểm tra nguồn", "của nội dung lịch sử"],
        "steps": [
            ["1. Mở", "câu chuyện"],
            ["2. Chọn", "Nguồn"],
            ["3. Xem thông tin", "biên tập"],
            ["4. Mở chi tiết", "hoặc liên kết"],
            ["5. Quay lại", "câu chuyện"],
        ],
        "anchor": 3,
        "children": [
            ["3.1 Xem", "trích dẫn"],
            ["3.2 Xem ghi chú", "biên tập"],
        ],
        "plan": "Plan 0: 1 → 2 → 3; chọn 3.1 hoặc 3.2, thực hiện 4 nếu cần → 5.",
    },
]


def text_lines(css_class: str, x: float, center_y: float, lines: list[str], line_height: int = 24) -> str:
    start_y = center_y - (len(lines) - 1) * line_height / 2
    parts = []
    for index, line in enumerate(lines):
        y = start_y + index * line_height
        parts.append(f'<text class="{css_class}" x="{x:.1f}" y="{y:.1f}">{html.escape(line)}</text>')
    return "".join(parts)


def render_svg(item: dict[str, object]) -> str:
    width, height = 1400, 650
    steps = item["steps"]
    children = item["children"]
    count = len(steps)
    margin, gap = 35, 22
    box_width = (width - 2 * margin - gap * (count - 1)) / count
    centers = [margin + box_width / 2 + i * (box_width + gap) for i in range(count)]
    anchor_x = centers[int(item["anchor"]) - 1]
    child_width, child_gap = 250, 30
    children_span = len(children) * child_width + (len(children) - 1) * child_gap
    first_child_x = max(25, min(width - children_span - 25, anchor_x - children_span / 2))
    child_centers = [first_child_x + child_width / 2 + i * (child_width + child_gap) for i in range(len(children))]

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs><style>",
        ".box{fill:#f8fafc;stroke:#334155;stroke-width:2}.goal{fill:#e0f2fe;stroke:#0369a1;stroke-width:3}.sub{fill:#f0fdf4;stroke:#15803d;stroke-width:2}.line{stroke:#64748b;stroke-width:2;fill:none}.title{font:700 25px Arial,sans-serif;fill:#0f172a;text-anchor:middle}.text{font:20px Arial,sans-serif;fill:#0f172a;text-anchor:middle}.small{font:18px Arial,sans-serif;fill:#334155;text-anchor:middle}.plan{font:18px Arial,sans-serif;fill:#0f172a;text-anchor:middle}",
        "</style></defs>",
        '<rect class="goal" x="450" y="25" width="500" height="82" rx="14"/>',
        text_lines("title", 700, 66, item["goal"], 28),
        '<path class="line" d="M700 107 V155"/>',
        f'<path class="line" d="M{centers[0]:.1f} 155 H{centers[-1]:.1f}"/>',
    ]
    for center, lines in zip(centers, steps):
        out.append(f'<path class="line" d="M{center:.1f} 155 V190"/>')
        out.append(f'<rect class="box" x="{center - box_width / 2:.1f}" y="190" width="{box_width:.1f}" height="78" rx="12"/>')
        out.append(text_lines("text", center, 229, lines, 24))

    branch_y = 350
    out.append(f'<path class="line" d="M{anchor_x:.1f} 268 V{branch_y}"/>')
    out.append(f'<path class="line" d="M{child_centers[0]:.1f} {branch_y} H{child_centers[-1]:.1f}"/>')
    for center, lines in zip(child_centers, children):
        out.append(f'<path class="line" d="M{center:.1f} {branch_y} V385"/>')
        out.append(f'<rect class="sub" x="{center - child_width / 2:.1f}" y="385" width="{child_width}" height="76" rx="11"/>')
        out.append(text_lines("small", center, 423, lines, 23))

    out.append(text_lines("plan", 700, 565, [item["plan"]], 22))
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main() -> None:
    for item in DIAGRAMS:
        svg_path = ASSET_DIR / f'{item["slug"]}.svg'
        png_path = ASSET_DIR / f'{item["slug"]}.png'
        svg_path.write_text(render_svg(item), encoding="utf-8")
        subprocess.run(
            ["sips", "-s", "format", "png", str(svg_path), "--out", str(png_path)],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        print(f"Generated {svg_path.name} and {png_path.name}")


if __name__ == "__main__":
    main()
