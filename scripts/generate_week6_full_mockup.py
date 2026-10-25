#!/usr/bin/env python3
"""Extend the week 6 editable SVG mockups to cover every app route and key state."""
from PIL import Image, ImageDraw, ImageFont

from generate_week6_mockup import SVG, C, OUT


def label(s, y, title):
    s.add(s.text(22, y, title, 11, C['red'], True, spacing='1.2'))


def card(s, y, h, title, subtitle='', fill=None):
    s.add(s.rect(22, y, 346, h, fill or C['paper'], 8, C['line']),
          s.text(38, y + 27, title, 15, C['ink'], True))
    if subtitle:
        s.add(s.text(38, y + 49, subtitle, 12, C['muted']))


def bottom_note(s, text):
    s.add(s.text(22, 756, text, 11, C['muted']))


names = []


def save(s, filename):
    s.save(filename)
    names.append(filename)


# Welcome
s = SVG('07 Chào mừng')
s.photo('bronze-drums.jpg', 0, 48, 390, 238, 0)
s.add(s.rect(0, 242, 390, 44, C['dark']), s.text(22, 270, 'DẤU XƯA  ·  CHẠM VÀO LỊCH SỬ', 12, C['paper'], True, spacing='1'))
s.add(s.text(22, 337, 'Mỗi hiện vật', 29, bold=True, serif=True), s.text(22, 374, 'giữ một tiếng nói.', 29, bold=True, serif=True))
s.add(s.text(22, 407, 'Nghe những câu chuyện di sản theo cách', 14), s.text(22, 428, 'phù hợp với bạn, tại bảo tàng hoặc từ xa.', 14))
label(s, 471, 'NGÔN NGỮ TRẢI NGHIỆM')
card(s, 487, 47, '✓  Tiếng Việt')
card(s, 543, 47, '    English')
card(s, 605, 65, 'Hỗ trợ tiếp cận', 'Mô tả hiện vật bằng chữ và chữ lớn')
s.add(s.rect(313, 625, 41, 26, C['green'], 13), s.circle(340, 638, 9, C['paper']))
s.button(688, 'Bắt đầu khám phá')
s.add(s.text(195, 763, 'Thiết lập trợ năng', 14, C['red'], True, anchor='middle'),
      s.text(195, 815, 'Không cần đăng ký để nghe miễn phí', 11, C['muted'], anchor='middle'))
save(s, '07-chao-mung.svg')

# Place selection
s = SVG('08 Chọn địa điểm')
s.top('Chọn địa điểm', True)
label(s, 113, 'BƯỚC 1')
s.add(s.text(22, 150, 'Bạn đang tham quan', 23, bold=True, serif=True), s.text(22, 181, 'ở đâu?', 23, bold=True, serif=True),
      s.text(22, 211, 'Chọn đúng nơi để xem nội dung phù hợp.', 13, C['muted']))
card(s, 233, 80, '⌖  Dùng vị trí hiện tại', 'Quyền vị trí được mô phỏng trong bản mẫu')
s.add(s.text(195, 347, 'hoặc tìm theo tên', 12, C['muted'], anchor='middle'))
card(s, 365, 54, '⌕  Nhập tên bảo tàng hoặc di tích')
label(s, 453, 'ĐỊA ĐIỂM GỢI Ý')
card(s, 470, 82, '◉  Bảo tàng Dấu Xưa', '4 câu chuyện · Cách 0,2 km', C['blush'])
card(s, 565, 82, '○  Di tích Cổng Thành', '3 câu chuyện · Cách 1,4 km')
s.button(685, 'Xác nhận địa điểm')
bottom_note(s, 'Địa điểm và khoảng cách là dữ liệu minh họa.')
save(s, '08-chon-dia-diem.svg')

# Scanner
s = SVG('09 Quét mã hiện vật')
s.add(s.rect(0, 48, 390, 724, '#26252A'), s.text(22, 83, '×', 31, C['paper']),
      s.text(195, 81, 'Quét mã hiện vật', 18, C['paper'], True, serif=True, anchor='middle'),
      s.text(352, 81, '☼', 25, C['paper'], anchor='middle'))
s.add(s.rect(42, 174, 306, 306, '#4F4A47', 12), s.rect(75, 207, 240, 240, 'none', 12, C['paper'], 3),
      s.line(89, 327, 301, 327, C['gold'], 3), s.text(195, 521, 'Đặt mã QR vào giữa khung', 16, C['paper'], True, anchor='middle'),
      s.text(195, 548, 'Camera đang được mô phỏng', 12, '#DDD4CB', anchor='middle'))
s.add(s.rect(0, 591, 390, 253, C['paper']), s.text(22, 626, 'CÁCH MỞ CÂU CHUYỆN', 11, C['red'], True))
card(s, 642, 50, '▣  Mô phỏng quét thành công')
card(s, 701, 50, '⌨  Nhập mã bằng tay')
s.add(s.text(195, 813, 'Chọn hiện vật từ danh sách', 14, C['red'], True, anchor='middle'))
save(s, '09-quet-ma.svg')

# Suggestions
s = SVG('10 Gợi ý điểm tiếp theo')
s.top('Điểm tiếp theo', True)
s.add(s.circle(195, 145, 35, C['green']), s.text(195, 158, '✓', 31, C['paper'], True, anchor='middle'))
label(s, 218, 'CÂU CHUYỆN ĐÃ HOÀN THÀNH')
s.add(s.text(22, 257, 'Bạn muốn đi đâu', 24, bold=True, serif=True), s.text(22, 287, 'tiếp?', 24, bold=True, serif=True),
      s.text(22, 315, 'Ba gợi ý liên quan tới câu chuyện vừa nghe.', 13, C['muted']))
for i, (title, reason, meta, kind) in enumerate([
    ('Âm vang trống đồng', 'Cùng chủ đề ký ức', '04:10 · Cách 45 m', 'drum'),
    ('Lá thư chưa kịp gửi', 'Ở gần bạn', '02:45 · Cách 80 m', 'letter'),
    ('Cánh cổng thời gian', 'Nối tiếp dòng thời gian', '05:05 · Cách 120 m', 'gate'),
]):
    y = 349 + i * 115
    s.add(s.rect(22, y, 346, 103, C['paper'], 8, C['line']), s.text(36, y + 23, f'0{i+1}', 11, C['red'], True))
    if kind == 'drum': s.photo('bronze-drums.jpg', 61, y + 9, 82, 85, 5)
    else: s.art(kind, 61, y + 9, 82, 85, 5)
    s.add(s.text(154, y + 24, reason, 10, C['muted']), s.text(154, y + 50, title, 13, bold=True),
          s.text(154, y + 78, meta, 11, C['muted']))
s.button(705, 'Kết thúc khám phá', False)
s.nav('Khám phá'); save(s, '10-goi-y-tiep-theo.svg')

# Tour list
s = SVG('11 Danh sách tour')
s.top('Tour tham quan')
label(s, 117, 'LỘ TRÌNH ĐƯỢC BIÊN TẬP')
s.add(s.text(22, 154, 'Chọn một cách', 24, bold=True, serif=True), s.text(22, 185, 'khám phá', 24, bold=True, serif=True),
      s.text(22, 213, 'Có bao nhiêu thời gian cho chuyến đi?', 13, C['muted']))
for i, (n, x) in enumerate([(30, 22), (60, 141), (90, 260)]):
    s.add(s.rect(x, 235, 108, 68, C['red'] if n == 60 else C['paper'], 8, None if n == 60 else C['line']),
          s.text(x + 54, 264, str(n), 21, C['paper'] if n == 60 else C['ink'], True, anchor='middle'),
          s.text(x + 54, 286, 'phút', 11, C['paper'] if n == 60 else C['muted'], anchor='middle'))
s.art('letter', 22, 324, 346, 155, 8)
s.add(s.rect(35, 338, 91, 25, C['dark'], 5), s.text(80, 355, 'TRẢ PHÍ', 10, C['paper'], True, anchor='middle'))
card(s, 479, 215, 'Những nhân chứng thầm lặng')
s.add(s.text(38, 535, '6 điểm dừng · đi bộ nhẹ', 12, C['muted']),
      s.text(38, 559, 'Một tuyến kết nối những câu chuyện', 13), s.text(38, 578, 'ít được biết đến trong bảo tàng.', 13),
      s.text(38, 607, '60 phút', 12, C['muted']), s.text(352, 607, '49.000đ', 15, C['red'], True, anchor='end'))
s.button(628, 'Xem tour trả phí', True, 38, 314)
s.add(s.text(22, 733, 'Mô tả hiện vật và chuyện ngắn vẫn miễn phí.', 11, C['muted']))
s.nav('Tour'); save(s, '11-danh-sach-tour.svg')

# Purchase sheet as full mobile state
s = SVG('12 Xác nhận mua tour')
s.top('Chi tiết tour', True)
s.add(s.rect(0, 96, 390, 676, '#4A3B39'), s.rect(0, 160, 390, 684, C['paper'], 22),
      s.rect(170, 172, 50, 5, C['line'], 3))
label(s, 212, 'XÁC NHẬN MUA')
s.add(s.text(22, 247, 'Những nhân chứng', 22, bold=True, serif=True), s.text(22, 275, 'thầm lặng', 22, bold=True, serif=True))
card(s, 299, 79, 'Premium Historical Tour', '60 phút · 6 điểm · Dùng trọn đời')
s.add(s.text(352, 352, '49.000đ', 13, C['red'], True, anchor='end'))
label(s, 416, 'PHƯƠNG THỨC THANH TOÁN')
card(s, 431, 70, '◉  Thẻ thanh toán', 'Visa ·•••• 2406', C['blush'])
card(s, 511, 70, '○  Ví điện tử', 'Tài khoản mô phỏng')
s.add(s.line(22, 607, 368, 607), s.text(22, 637, 'Tổng thanh toán', 14),
      s.text(368, 637, '49.000đ', 20, C['red'], True, serif=True, anchor='end'))
s.button(667, 'Thanh toán và bắt đầu')
s.add(s.text(195, 751, 'Giao dịch mô phỏng · Không trừ tiền thật', 11, C['muted'], anchor='middle'))
save(s, '12-xac-nhan-mua.svg')

# Tour progress
s = SVG('13 Tiến trình tour')
s.top('Hành trình của bạn', True)
s.add(s.rect(22, 104, 346, 259, C['dark'], 9), s.text(38, 131, 'TOUR TRẢ PHÍ · BẢN MẪU', 10, C['paper'], True),
      s.text(38, 169, 'Những nhân chứng', 22, C['paper'], True, serif=True),
      s.text(38, 197, 'thầm lặng', 22, C['paper'], True, serif=True),
      s.circle(195, 265, 43, C['paper']), s.text(195, 263, '1 / 6', 20, C['red'], True, anchor='middle'),
      s.text(195, 283, 'điểm', 11, C['muted'], anchor='middle'),
      s.text(195, 341, 'Đang xem điểm mẫu đầu tiên', 12, C['paper'], anchor='middle'))
card(s, 378, 72, '⇩  Mô phỏng tải ngoại tuyến', 'Chưa lưu tệp khi mất mạng')
label(s, 490, 'LỘ TRÌNH 6 ĐIỂM')
for i, title in enumerate(['Chiếc máy ảnh của người phóng viên', 'Âm vang trống đồng', 'Lá thư chưa kịp gửi']):
    y = 506 + i * 64
    card(s, y, 58, f'{i+1}   {title}')
s.add(s.text(22, 718, 'Ba điểm khác đang ở trạng thái minh họa.', 11, C['muted']))
s.button(706, 'Mở điểm mẫu')
s.nav('Tour'); save(s, '13-tien-trinh-tour.svg')

# Premium stop normal
s = SVG('14 Điểm dừng Premium')
s.top('Điểm 1 · Tour Premium', True)
s.art('camera', 22, 103, 346, 191, 8)
s.add(s.rect(35, 116, 86, 25, C['dark'], 5), s.text(78, 133, 'ĐIỂM 1 / 6', 10, C['paper'], True, anchor='middle'))
label(s, 328, 'NHỮNG NHÂN CHỨNG THẦM LẶNG')
s.add(s.text(22, 361, 'Chiếc máy ảnh của', 21, bold=True, serif=True),
      s.text(22, 389, 'người phóng viên', 21, bold=True, serif=True),
      s.text(22, 418, 'Một bức ảnh, nhiều lớp ký ức.', 13, C['muted']))
card(s, 438, 95, '♫  Không gian của một khoảnh khắc', 'Bản đọc minh họa · âm thanh không gian')
card(s, 545, 58, 'Âm thanh không gian                        BẬT')
card(s, 612, 58, 'Tín hiệu rung (mô phỏng)                   TẮT')
s.button(684, 'Mở tái dựng AR', False)
s.add(s.text(195, 759, 'Hoàn thành điểm mẫu', 13, C['red'], True, anchor='middle'))
s.nav('Tour'); save(s, '14-diem-premium.svg')

# Completion
s = SVG('15 Hoàn thành tour mẫu')
s.add(s.rect(0, 48, 390, 296, C['dark']), s.circle(195, 116, 36, C['gold']),
      s.text(195, 127, '★', 29, C['paper'], True, anchor='middle'),
      s.text(195, 181, 'KẾT THÚC PHẦN MINH HỌA', 11, C['paper'], True, anchor='middle'),
      s.text(195, 221, 'Bạn đã xem', 26, C['paper'], True, True, anchor='middle'),
      s.text(195, 256, 'điểm mẫu đầu tiên.', 23, C['paper'], True, True, anchor='middle'),
      s.text(195, 300, '1/6 điểm của tuyến được minh họa', 12, C['paper'], anchor='middle'))
card(s, 366, 90, '1/6   Đã xem điểm mẫu', 'Những nhân chứng thầm lặng')
label(s, 497, 'ĐIỂM VỪA KHÁM PHÁ')
card(s, 512, 75, '✓   Chiếc máy ảnh của người phóng viên', 'Điểm 1 · dữ liệu minh họa')
s.add(s.text(22, 622, '“Ký ức có thêm một người gìn giữ', 15, C['dark'], True, True),
      s.text(22, 645, 'khi một câu chuyện được lắng nghe.”', 15, C['dark'], True, True))
s.button(672, 'Xem lại câu chuyện')
s.add(s.text(195, 759, 'Mô phỏng lưu tour  ·  Về trang chủ', 12, C['red'], True, anchor='middle'))
s.nav('Tour'); save(s, '15-hoan-thanh.svg')

# Saved list
s = SVG('16 Đã lưu')
s.top('Đã lưu')
label(s, 121, 'BỘ SƯU TẬP CỦA BẠN')
s.add(s.text(22, 156, 'Những điều muốn', 24, bold=True, serif=True),
      s.text(22, 187, 'nghe lại', 24, bold=True, serif=True),
      s.text(22, 217, 'Câu chuyện mẫu đã lưu trong phiên này.', 13, C['muted']))
card(s, 250, 116, 'Chiếc máy ảnh của người phóng viên', '03:00 · Phòng Ký ức')
s.art('camera', 30, 258, 90, 100, 5)
s.add(s.text(129, 285, 'PHÒNG KÝ ỨC', 10, C['red'], True),
      s.text(129, 314, 'Một khoảnh khắc', 13, C['ink'], True), s.text(129, 334, 'được giữ lại', 13, C['ink'], True))
card(s, 382, 90, 'Đã lưu để nghe lại', 'Nhấn một câu chuyện để mở trình phát.')
s.nav('Đã lưu'); save(s, '16-da-luu.svg')

# Profile
s = SVG('17 Cá nhân')
s.top('Cá nhân')
s.add(s.rect(22, 103, 346, 150, C['dark'], 8), s.circle(67, 148, 25, C['paper']),
      s.text(67, 156, '◯', 24, C['red'], anchor='middle'),
      s.text(105, 129, 'KHÁCH THAM QUAN', 10, C['paper'], True),
      s.text(105, 159, 'Trải nghiệm của bạn', 18, C['paper'], True, True),
      s.text(38, 221, 'Dùng miễn phí, không cần tài khoản.', 12, C['paper']))
label(s, 291, 'TÙY CHỈNH')
card(s, 307, 78, '◌  Cài đặt trợ năng', 'Mô tả hiện vật, cỡ chữ, chuyển động')
card(s, 397, 78, '文  Ngôn ngữ', 'Tiếng Việt')
card(s, 487, 78, '◇  Nội dung đã mua', '1 tour mua mô phỏng')
card(s, 577, 78, 'ⓘ  Về Dấu Xưa', 'Bản thử nghiệm 0.5.1 · dữ liệu mẫu')
bottom_note(s, 'Dữ liệu minh họa chỉ lưu trong phiên hiện tại.')
s.nav('Cá nhân'); save(s, '17-ca-nhan.svg')

# Manual code error
s = SVG('18 Nhập mã thủ công · lỗi')
s.top('Nhập mã hiện vật', True)
s.add(s.circle(195, 171, 43, C['blush']), s.text(195, 184, '▣', 34, C['red'], anchor='middle'),
      s.text(22, 274, 'Nhập mã hiện vật', 24, bold=True, serif=True),
      s.text(22, 307, 'Mã nằm bên dưới QR cạnh hiện vật.', 13, C['muted']))
label(s, 349, 'MÃ HIỆN VẬT')
s.add(s.rect(22, 366, 346, 55, C['paper'], 8, '#B42318', 2), s.text(38, 402, 'DX-99', 16),
      s.text(22, 451, '⚠  Không tìm thấy mã này. Hãy thử DX-01.', 12, '#B42318'))
s.button(485, 'Mở câu chuyện')
s.button(548, 'Quay lại camera', False)
s.add(s.text(195, 650, 'Chọn hiện vật từ danh sách', 14, C['red'], True, anchor='middle'))
save(s, '18-nhap-ma-loi.svg')

# Saved empty
s = SVG('19 Đã lưu · rỗng')
s.top('Đã lưu')
s.add(s.circle(195, 297, 53, C['blush']), s.text(195, 312, '♡', 45, C['red'], anchor='middle'),
      s.text(195, 399, 'Chưa có câu chuyện', 22, C['ink'], True, True, anchor='middle'),
      s.text(195, 430, 'đã lưu', 22, C['ink'], True, True, anchor='middle'),
      s.text(195, 468, 'Nhấn Lưu tại một câu chuyện để', 13, C['muted'], anchor='middle'),
      s.text(195, 488, 'tìm lại ở đây.', 13, C['muted'], anchor='middle'))
s.button(551, 'Khám phá hiện vật')
s.nav('Đã lưu'); save(s, '19-da-luu-rong.svg')

# Camera denied fallback
s = SVG('20 Không có quyền camera')
s.top('Quét mã hiện vật', True)
s.add(s.circle(195, 245, 58, C['blush']), s.text(195, 262, '▣', 51, C['red'], anchor='middle'),
      s.text(195, 354, 'Chưa thể dùng camera', 22, C['ink'], True, True, anchor='middle'),
      s.text(195, 392, 'Bạn vẫn mở được câu chuyện mà không', 13, C['muted'], anchor='middle'),
      s.text(195, 413, 'cần quét mã QR.', 13, C['muted'], anchor='middle'))
s.button(477, 'Chọn hiện vật từ danh sách')
s.button(540, 'Nhập mã bằng tay', False)
bottom_note(s, 'Có thể bật quyền camera trong cài đặt thiết bị.')
save(s, '20-camera-khong-co-quyen.svg')

# Story transcript state
s = SVG('21 Bản chép lời câu chuyện')
s.top('Câu chuyện', True)
s.add(s.text(22, 126, 'Chiếc máy ảnh của', 22, bold=True, serif=True),
      s.text(22, 155, 'người phóng viên', 22, bold=True, serif=True))
card(s, 178, 80, 'Ⅱ   Đang phát bản đọc minh họa', '01:05 / 03:00 · Tốc độ 1×')
s.add(s.text(22, 300, 'Câu chuyện', 13, C['muted']), s.text(146, 300, 'Bản chép lời', 13, C['red'], True),
      s.text(293, 300, 'Nguồn', 13, C['muted']), s.line(135, 311, 241, 311, C['red'], 2))
label(s, 358, 'BẢN CHÉP LỜI · DỮ LIỆU MINH HỌA')
card(s, 377, 270, 'Một khoảnh khắc được giữ lại')
for y, line in enumerate(['Chiếc máy ảnh cũ đã đi qua nhiều nơi.',
                          'Người phóng viên dùng nó để ghi lại',
                          'những giây phút mà người khác dễ bỏ',
                          'qua. Trong từng tấm ảnh, ta nhìn thấy',
                          'không chỉ sự kiện mà còn cả con người',
                          'đã có mặt ở đó.'], start=0):
    s.add(s.text(38, 434 + y * 28, line, 14))
s.add(s.text(38, 621, 'Nội dung cần đối chiếu với nguồn bảo tàng.', 11, C['muted']))
s.button(680, 'Câu chuyện tiếp theo')
s.nav('Khám phá'); save(s, '21-ban-chep-loi.svg')

# Story source and timeline state
s = SVG('22 Dòng thời gian và nguồn')
s.top('Câu chuyện', True)
s.add(s.text(22, 126, 'Chiếc máy ảnh của', 22, bold=True, serif=True),
      s.text(22, 155, 'người phóng viên', 22, bold=True, serif=True))
label(s, 210, 'DÒNG THỜI GIAN')
for i, (year, text_) in enumerate([('1940', 'Máy ảnh được sử dụng'), ('1954', 'Những tấm ảnh được lưu giữ'), ('Hôm nay', 'Câu chuyện được kể lại')]):
    y = 229 + i * 90
    s.add(s.circle(37, y + 13, 7, C['gold']), s.text(59, y + 15, year, 12, C['red'], True),
          s.text(59, y + 41, text_, 14))
    if i < 2: s.add(s.line(37, y + 21, 37, y + 91, C['line'], 2))
label(s, 519, 'NGUỒN VÀ GHI CHÚ')
card(s, 536, 121, 'Nguồn tư liệu minh họa', 'Chưa xác minh với đơn vị lưu trữ')
s.add(s.text(38, 612, 'Cần bổ sung nguồn chính thức, chú thích ảnh', 11, C['muted']),
      s.text(38, 631, 'và bản ghi âm trước khi phát hành.', 11, C['muted']))
s.button(691, 'Câu chuyện tiếp theo')
s.nav('Khám phá'); save(s, '22-dong-thoi-gian-nguon.svg')


# Export new screens to PNG for review and submission; originals remain untouched.
import subprocess
for name in names:
    source = OUT / name
    target = source.with_suffix('.png')
    subprocess.run(['sips', '-s', 'format', 'png', str(source), '--out', str(target)],
                   check=True, stdout=subprocess.DEVNULL)

# A review sheet with all routes and state variants.
flow_order = [
    '07-chao-mung', '08-chon-dia-diem', '01-kham-pha', '09-quet-ma',
    '18-nhap-ma-loi', '20-camera-khong-co-quyen', '02-danh-sach-hien-vat',
    '03-trinh-phat', '21-ban-chep-loi', '22-dong-thoi-gian-nguon',
    '10-goi-y-tiep-theo', '11-danh-sach-tour', '04-tour-premium',
    '12-xac-nhan-mua', '13-tien-trinh-tour', '14-diem-premium',
    '05-ar-thay-the', '15-hoan-thanh', '16-da-luu', '19-da-luu-rong',
    '17-ca-nhan', '06-tro-nang',
]
all_names = [name + '.png' for name in flow_order]
cols = 4
pad, gap, title_h, caption_h = 42, 25, 102, 50
rows = (len(all_names) + cols - 1) // cols
board_w = pad * 2 + cols * 390 + (cols - 1) * gap
board_h = title_h + rows * (844 + caption_h + gap) + pad
board = Image.new('RGB', (board_w, board_h), '#E8E3DC')
draw = ImageDraw.Draw(board)
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 22)
font_small = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 15)
draw.text((pad, 25), 'Dau Xua · Full mobile mockup', fill='#542020', font=font)
draw.text((pad, 59), f'{len(all_names)} screens and states · 390 × 844 px', fill='#59636E', font=font_small)
for i, name in enumerate(all_names):
    x = pad + (i % cols) * (390 + gap)
    y = title_h + (i // cols) * (844 + caption_h + gap)
    with Image.open(OUT / name) as img:
        board.paste(img.convert('RGB'), (x, y))
    draw.text((x, y + 858), name.removesuffix('.png'), fill='#542020', font=font_small)
board.save(OUT / 'Dau_Xua_Full_Mockup_Board.png')
print(f'Generated {len(names)} new screens; board has {len(all_names)} screens/states in {OUT}')
