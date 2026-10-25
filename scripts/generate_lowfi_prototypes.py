#!/usr/bin/env python3
"""Generate low-fidelity mobile prototype sheets for the Dấu Xưa design preparation.

These are intentionally monochrome digital sketches. They document content hierarchy,
primary actions and fallback states; they are not high-fidelity UI mockups.
"""

from __future__ import annotations

import html
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "04-design" / "low-fidelity"
WIDTH, HEIGHT = 1600, 1400
PHONE_W, PHONE_H = 270, 520
TOP_Y, BOTTOM_Y = 145, 770
X4 = [125, 500, 875, 1250]
X3 = [310, 665, 1020]


def esc(value: str) -> str:
    return html.escape(value)


def rect(x: float, y: float, w: float, h: float, cls: str = "box", radius: int = 8) -> str:
    return f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}"/>'


def line(x1: float, y1: float, x2: float, y2: float, cls: str = "line") -> str:
    return f'<path class="{cls}" d="M{x1} {y1} L{x2} {y2}"/>'


def text(x: float, y: float, value: str, cls: str = "text", anchor: str = "start") -> str:
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{esc(value)}</text>'


def multiline(x: float, y: float, lines: list[str], cls: str = "text", line_height: int = 16, anchor: str = "start") -> str:
    return "".join(text(x, y + i * line_height, value, cls, anchor) for i, value in enumerate(lines))


def phone(x: float, y: float, number: str, title: str, subtitle: str = "") -> list[str]:
    return [
        rect(x, y, PHONE_W, PHONE_H, "phone", 18),
        rect(x + 105, y + 8, 60, 5, "ink", 3),
        text(x + 14, y - 20, number, "screen-number"),
        text(x + 45, y - 20, title, "screen-title"),
        text(x + PHONE_W / 2, y + 35, "DẤU XƯA", "appbar", "middle"),
        line(x + 14, y + 49, x + PHONE_W - 14, y + 49, "soft-line"),
        text(x + 16, y + PHONE_H + 20, subtitle, "caption", "start") if subtitle else "",
    ]


def button(x: float, y: float, w: float, label: str, primary: bool = False) -> str:
    cls = "sketch-button-primary" if primary else "sketch-button"
    return rect(x, y, w, 30, cls, 6) + text(x + w / 2, y + 20, label, "button-text", "middle")


def nav(x: float, y: float, active: str = "Khám phá") -> str:
    labels = ["Khám phá", "Tour", "Đã lưu", "Cá nhân"]
    items = [rect(x + 12, y + PHONE_H - 49, PHONE_W - 24, 36, "nav", 7)]
    for index, label in enumerate(labels):
        cx = x + 40 + index * 63
        dot_class = "ink-dot" if label == active else "dot"
        items.append(f'<circle class="{dot_class}" cx="{cx}" cy="{y + PHONE_H - 35}" r="4"/>')
        items.append(text(cx, y + PHONE_H - 19, label, "nav-text", "middle"))
    return "".join(items)


def card(x: float, y: float, w: float, title: str, meta: str = "", image: bool = False) -> str:
    parts = [rect(x, y, w, 54, "box", 7)]
    tx = x + 10
    if image:
        parts.append(rect(x + 8, y + 8, 38, 38, "image", 5))
        tx = x + 55
    parts.append(text(tx, y + 22, title, "strong"))
    if meta:
        parts.append(text(tx, y + 40, meta, "muted"))
    return "".join(parts)


def tiny_note(x: float, y: float, lines: list[str]) -> str:
    return rect(x, y, 230, 52, "note", 8) + multiline(x + 10, y + 20, lines, "note-text", 15)


def arrow(x1: float, y1: float, x2: float, y2: float) -> str:
    return (
        f'<path class="arrow" d="M{x1} {y1} C{(x1 + x2) / 2} {y1}, {(x1 + x2) / 2} {y2}, {x2} {y2}"/>'
        f'<path class="arrow-head" d="M{x2 - 8} {y2 - 5} L{x2} {y2} L{x2 - 8} {y2 + 5}"/>'
    )


def welcome(x: float, y: float) -> str:
    p = phone(x, y, "01", "Chào mừng", "Bắt đầu luồng miễn phí")
    p += [rect(x + 16, y + 68, PHONE_W - 32, 105, "image", 8)]
    p += [multiline(x + 18, y + 205, ["Mỗi hiện vật", "giữ một tiếng nói."], "heading", 23)]
    p += [text(x + 18, y + 260, "Chọn ngôn ngữ", "muted")]
    p += [button(x + 18, y + 274, 110, "Tiếng Việt"), button(x + 142, y + 274, 110, "English")]
    p += [button(x + 18, y + 326, PHONE_W - 36, "Bắt đầu khám phá", True)]
    p += [text(x + 18, y + 384, "• Thiết lập trợ năng", "muted"), text(x + 18, y + 408, "• Không cần tài khoản", "muted")]
    return "".join(p)


def location(x: float, y: float) -> str:
    p = phone(x, y, "02", "Chọn địa điểm", "M1: xác nhận bối cảnh")
    p += [multiline(x + 18, y + 82, ["Bạn đang tham quan", "ở đâu?"], "heading", 20)]
    p += [button(x + 18, y + 145, PHONE_W - 36, "Dùng vị trí hiện tại")]
    p += [rect(x + 18, y + 190, PHONE_W - 36, 30, "input", 6), text(x + 30, y + 210, "Tìm tên địa điểm", "muted")]
    p += [card(x + 18, y + 236, PHONE_W - 36, "Bảo tàng Dấu Xưa", "12 câu chuyện · gần bạn")]
    p += [card(x + 18, y + 300, PHONE_W - 36, "Di tích Thành Nội", "8 câu chuyện")]
    p += [button(x + 18, y + 405, PHONE_W - 36, "Xác nhận địa điểm", True)]
    return "".join(p)


def explore(x: float, y: float) -> str:
    p = phone(x, y, "03", "Khám phá", "CTA quét mã luôn có lối thay thế")
    p += [text(x + 18, y + 84, "Bảo tàng Dấu Xưa", "heading"), text(x + 18, y + 108, "12 câu chuyện ở quanh bạn", "muted")]
    p += [button(x + 18, y + 130, PHONE_W - 36, "Quét mã hiện vật", True)]
    p += [text(x + 18, y + 190, "Tiếp tục nghe", "strong"), card(x + 18, y + 204, PHONE_W - 36, "Chiếc máy ảnh", "01:12 còn lại", True)]
    p += [text(x + 18, y + 280, "Câu chuyện nổi bật", "strong"), card(x + 18, y + 294, PHONE_W - 36, "Âm vang trống đồng", "04:10", True)]
    p += [nav(x, y)]
    return "".join(p)


def scan(x: float, y: float) -> str:
    p = phone(x, y, "04", "Quét mã", "M2: camera không là cách duy nhất")
    p += [rect(x + 33, y + 88, PHONE_W - 66, 175, "dark", 6)]
    p += [rect(x + 75, y + 120, 120, 120, "scan", 0)]
    p += [text(x + PHONE_W / 2, y + 286, "Đặt mã QR vào giữa khung", "muted", "middle")]
    p += [button(x + 18, y + 315, PHONE_W - 36, "Nhập mã bằng tay")]
    p += [button(x + 18, y + 355, PHONE_W - 36, "Chọn hiện vật từ danh sách")]
    p += [tiny_note(x + 18, y + 410, ["Không có quyền camera?", "Người dùng vẫn tiếp tục được."])]
    return "".join(p)


def objects(x: float, y: float) -> str:
    p = phone(x, y, "05", "Danh sách hiện vật", "Tìm kiếm, lọc, danh sách đơn giản")
    p += [rect(x + 18, y + 76, PHONE_W - 36, 30, "input", 6), text(x + 30, y + 96, "Tìm hiện vật", "muted")]
    p += [button(x + 18, y + 118, 75, "Tất cả"), button(x + 101, y + 118, 80, "Ký ức"), button(x + 189, y + 118, 63, "Lọc")]
    p += [card(x + 18, y + 170, PHONE_W - 36, "Chiếc máy ảnh", "03:00 · Phòng Ký ức", True)]
    p += [card(x + 18, y + 236, PHONE_W - 36, "Âm vang trống đồng", "04:10 · Khởi nguyên", True)]
    p += [card(x + 18, y + 302, PHONE_W - 36, "Lá thư chưa kịp gửi", "02:45 · Nhân chứng", True)]
    p += [tiny_note(x + 18, y + 390, ["Có chế độ danh sách đơn giản", "cho trình đọc màn hình."])]
    return "".join(p)


def player(x: float, y: float) -> str:
    p = phone(x, y, "06", "Trình phát", "M3–M5: audio là trung tâm")
    p += [rect(x + 18, y + 75, PHONE_W - 36, 105, "image", 8)]
    p += [text(x + 18, y + 208, "Chiếc máy ảnh của người phóng viên", "strong")]
    p += [rect(x + 18, y + 224, PHONE_W - 36, 55, "note", 7)]
    p += [text(x + 28, y + 245, "Mô tả hiện vật", "strong"), text(x + 28, y + 264, "Có thể nghe hoặc đọc trước câu chuyện", "muted")]
    p += [rect(x + 18, y + 296, PHONE_W - 36, 98, "box", 8)]
    p += [line(x + 32, y + 318, x + PHONE_W - 32, y + 318, "soft-line")]
    p += [text(x + PHONE_W / 2, y + 358, "◀ 15     ▶     15 ▶", "player", "middle")]
    p += [text(x + PHONE_W / 2, y + 380, "0:00                         -3:00", "muted", "middle")]
    p += [button(x + 18, y + 412, 72, "Câu chuyện"), button(x + 98, y + 412, 66, "Timeline"), button(x + 172, y + 412, 80, "Nguồn")]
    return "".join(p)


def suggestions(x: float, y: float) -> str:
    p = phone(x, y, "07", "Gợi ý tiếp theo", "Kết thúc hoặc tiếp tục rõ ràng")
    p += [text(x + PHONE_W / 2, y + 88, "✓", "completion", "middle")]
    p += [multiline(x + 18, y + 125, ["Bạn muốn đi", "đâu tiếp?"], "heading", 21)]
    p += [card(x + 18, y + 186, PHONE_W - 36, "Âm vang trống đồng", "Cùng chủ đề ký ức", True)]
    p += [card(x + 18, y + 252, PHONE_W - 36, "Lá thư chưa kịp gửi", "Ở gần bạn", True)]
    p += [button(x + 18, y + 350, PHONE_W - 36, "Kết thúc khám phá")]
    p += [nav(x, y)]
    return "".join(p)


def accessibility_settings(x: float, y: float) -> str:
    p = phone(x, y, "A1", "Cài đặt trợ năng", "M5–M7: lựa chọn độc lập")
    p += [multiline(x + 18, y + 84, ["Trải nghiệm theo", "cách của bạn"], "heading", 20)]
    for idx, (label, detail) in enumerate([
        ("Mô tả bằng âm thanh", "Bật"),
        ("Tín hiệu rung", "Tắt"),
        ("Tăng tương phản", "Bật"),
        ("Giảm chuyển động", "Tắt"),
    ]):
        yy = y + 152 + idx * 60
        p += [rect(x + 18, yy, PHONE_W - 36, 48, "box", 7), text(x + 29, yy + 21, label, "strong"), text(x + 29, yy + 38, detail, "muted"), rect(x + 218, yy + 13, 24, 16, "toggle-on" if detail == "Bật" else "toggle-off", 8)]
    p += [tiny_note(x + 18, y + 410, ["Không chỉ dùng màu, âm thanh", "hoặc rung để báo trạng thái."])]
    return "".join(p)


def simple_list(x: float, y: float) -> str:
    p = phone(x, y, "A2", "Danh sách đơn giản", "M6: thứ tự đọc và nhãn rõ")
    p += [text(x + 18, y + 82, "Hiện vật quanh bạn", "heading")]
    p += [text(x + 18, y + 110, "3 kết quả", "muted")]
    for idx, title in enumerate(["Chiếc máy ảnh", "Âm vang trống đồng", "Lá thư chưa kịp gửi"]):
        yy = y + 140 + idx * 68
        p += [rect(x + 18, yy, PHONE_W - 36, 55, "box", 7), text(x + 30, yy + 22, f"{idx + 1}. {title}", "strong"), text(x + 30, yy + 40, "Nút mở câu chuyện", "muted")]
    p += [tiny_note(x + 18, y + 370, ["Focus đọc theo thứ tự:", "tiêu đề → mô tả → mở."])]
    return "".join(p)


def camera_error(x: float, y: float) -> str:
    p = phone(x, y, "A3", "Camera không dùng được", "Khả năng chịu lỗi")
    p += [text(x + PHONE_W / 2, y + 145, "!", "error-mark", "middle")]
    p += [multiline(x + 18, y + 190, ["Không thể dùng", "camera trên thiết bị này"], "heading", 20)]
    p += [text(x + 18, y + 252, "Bạn vẫn có thể mở câu chuyện", "muted")]
    p += [button(x + 18, y + 286, PHONE_W - 36, "Nhập mã bằng tay")]
    p += [button(x + 18, y + 328, PHONE_W - 36, "Chọn từ danh sách", True)]
    p += [tiny_note(x + 18, y + 400, ["Thông báo bằng chữ và icon;", "không chỉ bằng màu đỏ."])]
    return "".join(p)


def accessible_player(x: float, y: float) -> str:
    p = phone(x, y, "A4", "Player có mô tả", "Thông tin có thể cảm nhận")
    p += [text(x + 18, y + 85, "Chiếc máy ảnh", "heading")]
    p += [rect(x + 18, y + 120, PHONE_W - 36, 76, "note", 7)]
    p += [text(x + 28, y + 145, "Mô tả hiện vật", "strong")]
    p += [multiline(x + 28, y + 164, ["Máy ảnh thân kim loại,", "ống kính tròn, dây da."], "muted", 15)]
    p += [rect(x + 18, y + 218, PHONE_W - 36, 115, "box", 8)]
    p += [text(x + PHONE_W / 2, y + 263, "Lùi 15   Phát   Tới 15", "player", "middle")]
    p += [text(x + PHONE_W / 2, y + 294, "Tiến độ 0:00 / 3:00", "muted", "middle")]
    p += [button(x + 18, y + 365, PHONE_W - 36, "Đọc bản chép lời")]
    p += [tiny_note(x + 18, y + 410, ["Nhãn điều khiển đủ nghĩa", "cho VoiceOver/TalkBack."])]
    return "".join(p)


def tours(x: float, y: float) -> str:
    p = phone(x, y, "P1", "Danh sách tour", "SH1: chọn theo thời lượng")
    p += [text(x + 18, y + 84, "Chọn một cách khám phá", "heading")]
    p += [button(x + 18, y + 125, 68, "30 phút"), button(x + 101, y + 125, 68, "60 phút", True), button(x + 184, y + 125, 68, "90 phút")]
    p += [card(x + 18, y + 185, PHONE_W - 36, "Những nhân chứng", "6 điểm · 60 phút · 49.000đ", True)]
    p += [text(x + 28, y + 252, "TRẢ PHÍ", "tag")]
    p += [card(x + 18, y + 285, PHONE_W - 36, "Lần đầu gặp Dấu Xưa", "4 điểm · miễn phí", True)]
    p += [nav(x, y, "Tour")]
    return "".join(p)


def premium_preview(x: float, y: float) -> str:
    p = phone(x, y, "P2", "Xem trước tour", "Giá trị và phần miễn phí rõ ràng")
    p += [rect(x + 18, y + 76, PHONE_W - 36, 100, "image", 8)]
    p += [text(x + 18, y + 205, "Những nhân chứng thầm lặng", "strong")]
    p += [text(x + 18, y + 228, "60 phút · 6 điểm · 49.000đ", "muted")]
    p += [rect(x + 18, y + 250, PHONE_W - 36, 65, "note", 7)]
    p += [text(x + 30, y + 276, "▶ Nghe thử đoạn mở đầu", "strong")]
    p += [text(x + 30, y + 297, "Nội dung cơ bản vẫn miễn phí", "muted")]
    p += [button(x + 18, y + 340, PHONE_W - 36, "Mua tour", True)]
    p += [button(x + 18, y + 380, PHONE_W - 36, "Tiếp tục bản miễn phí")]
    return "".join(p)


def purchase(x: float, y: float) -> str:
    p = phone(x, y, "P3", "Xác nhận mua", "Không phí ẩn, trạng thái rõ")
    p += [text(x + 18, y + 84, "Tóm tắt đơn hàng", "heading")]
    p += [card(x + 18, y + 120, PHONE_W - 36, "Premium Historical Tour", "60 phút · dùng trọn đời")]
    p += [text(x + 18, y + 205, "Phương thức thanh toán", "strong")]
    p += [rect(x + 18, y + 220, PHONE_W - 36, 46, "selected", 7), text(x + 30, y + 248, "◉  Thẻ thanh toán", "strong")]
    p += [rect(x + 18, y + 276, PHONE_W - 36, 46, "box", 7), text(x + 30, y + 304, "○  Ví điện tử", "strong")]
    p += [text(x + 18, y + 355, "Tổng: 49.000đ", "heading")]
    p += [button(x + 18, y + 390, PHONE_W - 36, "Thanh toán và bắt đầu", True)]
    return "".join(p)


def tour_progress(x: float, y: float) -> str:
    p = phone(x, y, "P4", "Tiến trình tour", "Một tuyến đơn giản, điểm hiện tại rõ")
    p += [text(x + 18, y + 84, "Điểm 1 / 6", "heading")]
    p += [rect(x + 18, y + 110, PHONE_W - 36, 8, "progress", 4), rect(x + 18, y + 110, 42, 8, "ink", 4)]
    p += [text(x + 18, y + 145, "Khoảng 52 phút còn lại", "muted")]
    for idx, title in enumerate(["1  Chiếc máy ảnh", "2  Bức ảnh phòng tối", "3  Lá thư chưa gửi"]):
        yy = y + 178 + idx * 62
        p += [rect(x + 18, yy, PHONE_W - 36, 48, "selected" if idx == 0 else "box", 7), text(x + 30, yy + 28, title, "strong")]
    p += [button(x + 18, y + 390, PHONE_W - 36, "Bắt đầu điểm này", True)]
    return "".join(p)


def ar_fallback(x: float, y: float) -> str:
    p = phone(x, y, "P5", "AR không khả dụng", "C2: có phương án thay thế")
    p += [rect(x + 18, y + 78, PHONE_W - 36, 104, "image", 8)]
    p += [text(x + PHONE_W / 2, y + 230, "!", "error-mark", "middle")]
    p += [multiline(x + 18, y + 264, ["Không thể mở AR", "trên thiết bị này"], "heading", 20)]
    p += [text(x + 18, y + 323, "Bạn vẫn có thể tiếp tục bằng:", "muted")]
    p += [text(x + 30, y + 350, "• Ảnh tái dựng", "strong"), text(x + 30, y + 374, "• Âm thanh và bản chép lời", "strong")]
    p += [button(x + 18, y + 408, PHONE_W - 36, "Xem ảnh tái dựng", True)]
    return "".join(p)


def completion(x: float, y: float) -> str:
    p = phone(x, y, "P6", "Hoàn thành tour", "Tổng kết, không ép chia sẻ")
    p += [text(x + PHONE_W / 2, y + 128, "✓", "completion", "middle")]
    p += [multiline(x + PHONE_W / 2, y + 175, ["Bạn đã lắng nghe", "sáu tiếng nói."], "heading", 21, "middle")]
    p += [rect(x + 18, y + 242, PHONE_W - 36, 68, "note", 7)]
    p += [text(x + 30, y + 270, "6/6 điểm đã hoàn thành", "strong"), text(x + 30, y + 291, "Những nhân chứng thầm lặng", "muted")]
    p += [button(x + 18, y + 340, PHONE_W - 36, "Xem lại câu chuyện")]
    p += [button(x + 18, y + 380, PHONE_W - 36, "Về trang chủ", True)]
    return "".join(p)


def stylesheet() -> str:
    return """
    <style>
      .sheet{fill:#faf9f6}.phone{fill:#fff;stroke:#202124;stroke-width:2.2}.box{fill:#fff;stroke:#4a4a4a;stroke-width:1.4}.image{fill:#e5e5e5;stroke:#4a4a4a;stroke-width:1.4}.input{fill:#fafafa;stroke:#4a4a4a;stroke-width:1.4}.sketch-button{fill:#fff;stroke:#202124;stroke-width:1.6}.sketch-button-primary{fill:#dedede;stroke:#202124;stroke-width:2.2}.nav{fill:#f2f2f2;stroke:#777;stroke-width:1}.note{fill:#f6f6f6;stroke:#555;stroke-width:1.2}.dark{fill:#4a4a4a;stroke:#202124;stroke-width:1.4}.scan{fill:none;stroke:#fff;stroke-width:2.5}.selected{fill:#efefef;stroke:#202124;stroke-width:2}.toggle-on{fill:#202124;stroke:#202124;stroke-width:1}.toggle-off{fill:#fff;stroke:#202124;stroke-width:1}.progress{fill:#ddd;stroke:#777;stroke-width:1}.ink{fill:#202124}.line{stroke:#202124;stroke-width:1.4;fill:none}.soft-line{stroke:#a3a3a3;stroke-width:1.2;fill:none}.arrow{stroke:#555;stroke-width:2;fill:none;stroke-dasharray:7 6}.arrow-head{stroke:#555;stroke-width:2;fill:none}.dot{fill:#aaa}.ink-dot{fill:#202124}.appbar{font:700 11px Arial,sans-serif;letter-spacing:1.1px;fill:#202124}.screen-number{font:700 18px Arial,sans-serif;fill:#202124}.screen-title{font:700 16px Arial,sans-serif;fill:#202124}.heading{font:700 17px Arial,sans-serif;fill:#202124}.strong{font:700 12px Arial,sans-serif;fill:#202124}.text{font:12px Arial,sans-serif;fill:#202124}.muted{font:11px Arial,sans-serif;fill:#666}.button-text{font:700 11px Arial,sans-serif;fill:#202124}.caption{font:italic 11px Arial,sans-serif;fill:#555}.note-text{font:11px Arial,sans-serif;fill:#303030}.nav-text{font:8px Arial,sans-serif;fill:#404040}.player{font:700 14px Arial,sans-serif;fill:#202124}.completion{font:700 48px Arial,sans-serif;fill:#202124}.error-mark{font:700 42px Arial,sans-serif;fill:#202124}.tag{font:700 9px Arial,sans-serif;fill:#202124;letter-spacing:1px}
      .sheet-title{font:700 28px Arial,sans-serif;fill:#202124}.sheet-subtitle{font:14px Arial,sans-serif;fill:#606060}.legend{fill:#f0f0ee;stroke:#666;stroke-width:1}.legend-head{font:700 12px Arial,sans-serif;fill:#202124}.legend-text{font:11px Arial,sans-serif;fill:#303030}
    </style>
    """


def render(title: str, subtitle: str, screens: list[tuple[int, int, str]], notes: list[str]) -> str:
    body = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">', stylesheet(), rect(0, 0, WIDTH, HEIGHT, "sheet", 0)]
    body += [text(80, 58, title, "sheet-title"), text(80, 86, subtitle, "sheet-subtitle")]
    for x, y, screen in screens:
        body.append(screen)
    body += [rect(80, 1280, WIDTH - 160, 72, "legend", 10), text(102, 1310, "Ghi chú thiết kế:", "legend-head")]
    for idx, note in enumerate(notes):
        body.append(text(255 + idx * 400, 1310, f"• {note}", "legend-text"))
    body.append('</svg>')
    return "\n".join(body)


def write_sheet(slug: str, title: str, subtitle: str, screens: list[tuple[int, int, str]], notes: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    svg_path = OUT / f"{slug}.svg"
    png_path = OUT / f"{slug}.png"
    svg_path.write_text(render(title, subtitle, screens, notes), encoding="utf-8")
    subprocess.run(["sips", "-s", "format", "png", str(svg_path), "--out", str(png_path)], check=True, stdout=subprocess.DEVNULL)
    print(f"Generated {svg_path.relative_to(ROOT)} and {png_path.relative_to(ROOT)}")


def main() -> None:
    write_sheet(
        "phac-thao-lowfi-luong-mien-phi",
        "Phác thảo low-fi 01 — Luồng miễn phí",
        "Chuẩn bị cho Mục 2.5. Mobile-first · minh họa cấu trúc, không phải mockup hoàn chỉnh.",
        [
            (X4[0], TOP_Y, welcome(X4[0], TOP_Y)), (X4[1], TOP_Y, location(X4[1], TOP_Y)),
            (X4[2], TOP_Y, explore(X4[2], TOP_Y)), (X4[3], TOP_Y, scan(X4[3], TOP_Y)),
            (X3[0], BOTTOM_Y, objects(X3[0], BOTTOM_Y)), (X3[1], BOTTOM_Y, player(X3[1], BOTTOM_Y)),
            (X3[2], BOTTOM_Y, suggestions(X3[2], BOTTOM_Y)),
        ],
        ["Mã QR có lối thay thế bằng danh sách", "Audio và mô tả hiện vật là trọng tâm", "Người dùng có thể kết thúc hoặc tiếp tục"],
    )
    write_sheet(
        "phac-thao-lowfi-tro-nang",
        "Phác thảo low-fi 02 — Luồng trợ năng và phương án thay thế",
        "Chuẩn bị cho Mục 2.5. Mỗi trạng thái có chữ, nhãn và hành động rõ ràng.",
        [
            (X4[0], TOP_Y, accessibility_settings(X4[0], TOP_Y)), (X4[1], TOP_Y, simple_list(X4[1], TOP_Y)),
            (X4[2], TOP_Y, camera_error(X4[2], TOP_Y)), (X4[3], TOP_Y, accessible_player(X4[3], TOP_Y)),
        ],
        ["Không chỉ dùng màu sắc, âm thanh hoặc rung", "Có thứ tự đọc dự kiến cho trình đọc màn hình", "Camera lỗi vẫn mở được nội dung"],
    )
    write_sheet(
        "phac-thao-lowfi-luong-premium",
        "Phác thảo low-fi 03 — Luồng Premium Historical Tour",
        "Chuẩn bị cho Mục 2.5. Giá trị gói, thanh toán và phương án AR thay thế được thể hiện trước.",
        [
            (X3[0], TOP_Y, tours(X3[0], TOP_Y)), (X3[1], TOP_Y, premium_preview(X3[1], TOP_Y)),
            (X3[2], TOP_Y, purchase(X3[2], TOP_Y)), (X3[0], BOTTOM_Y, tour_progress(X3[0], BOTTOM_Y)),
            (X3[1], BOTTOM_Y, ar_fallback(X3[1], BOTTOM_Y)), (X3[2], BOTTOM_Y, completion(X3[2], BOTTOM_Y)),
        ],
        ["Nội dung cơ bản và trợ năng luôn miễn phí", "Không ép đăng ký định kỳ hoặc phí ẩn", "AR là tùy chọn, có cách tiếp tục khác"],
    )


if __name__ == "__main__":
    main()
