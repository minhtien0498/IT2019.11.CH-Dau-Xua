#!/usr/bin/env python3
"""Generate editable SVG mockup screens for import into Figma."""
from pathlib import Path
from base64 import b64encode
from html import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/04-design/high-fidelity'
OUT.mkdir(parents=True, exist_ok=True)
IMG = ROOT / 'app/public/images'
W, H = 390, 844
C = {'bg':'#F7F2E8','paper':'#FFFDF8','red':'#7A2E2E','dark':'#542020','gold':'#C7923E',
     'ink':'#1F2933','muted':'#59636E','line':'#D8D0C3','green':'#2F6B4F','blush':'#F1E2DB'}
photos = {name: 'data:image/jpeg;base64,' + b64encode((IMG / name).read_bytes()).decode()
          for name in ('antique-camera.jpg','bronze-drums.jpg','heritage-gate.jpg','old-letter.jpg')}

class SVG:
    def __init__(self, title):
        self.title = title
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="390" height="844" viewBox="0 0 390 844" role="img" aria-label="{escape(title)}">',
            '<defs><clipPath id="screen"><rect width="390" height="844" rx="28"/></clipPath></defs>',
            '<g clip-path="url(#screen)">', self.rect(0,0,390,844,C['bg']),
            self.text(26,31,'9:41',13,bold=True),
            self.text(329,31,'●  ▰',12,bold=True),
            self.line(0,48,390,48,C['line'])]
    def rect(self,x,y,w,h,fill,r=0,stroke=None,sw=1):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"' + (f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '') + '/>'
    def text(self,x,y,s,size=16,color=None,bold=False,serif=False,anchor=None,spacing=None):
        attrs=f' x="{x}" y="{y}" fill="{color or C["ink"]}" font-family="{ "Noto Serif, Georgia, serif" if serif else "Noto Sans, Arial, sans-serif"}" font-size="{size}" font-weight="{700 if bold else 400}"'
        if anchor: attrs+=f' text-anchor="{anchor}"'
        if spacing: attrs+=f' letter-spacing="{spacing}"'
        return f'<text{attrs}>{escape(s)}</text>'
    def line(self,x1,y1,x2,y2,color=None,sw=1):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color or C["line"]}" stroke-width="{sw}"/>'
    def circle(self,x,y,r,fill,stroke=None,sw=1):
        return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"' + (f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '') + '/>'
    def photo(self,name,x,y,w,h,r=8):
        clip=f'clip_{len(self.parts)}'
        self.parts.append(f'<defs><clipPath id="{clip}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath></defs>')
        self.parts.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{photos[name]}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip})"/>')
    def art(self,kind,x,y,w,h,r=8):
        """Simple editable illustration for sample objects without verified photos."""
        bg = {'camera':'#3E3032','letter':'#D9C5A7','gate':'#657875'}[kind]
        self.parts.append(self.rect(x,y,w,h,bg,r))
        cx,cy=x+w/2,y+h/2
        if kind=='camera':
            bw,bh=min(w*.58,150),min(h*.42,88)
            self.parts.extend([self.rect(cx-bw/2,cy-bh/2,bw,bh,'#A8896B',6),
                self.rect(cx-bw*.37,cy-bh*.66,bw*.31,bh*.18,'#A8896B',3),
                self.circle(cx,cy,bh*.36,'#2B282B','#E3CBA5',3),
                self.circle(cx,cy,bh*.23,'#58666B','#E3CBA5',2),
                self.circle(cx,cy,bh*.12,'#1F2933'),
                self.circle(cx+bw*.35,cy-bh*.3,3,'#F5E7D0')])
        elif kind=='letter':
            bw,bh=min(w*.62,165),min(h*.61,125)
            self.parts.extend([self.rect(cx-bw/2,cy-bh/2,bw,bh,'#FAF1DD',3),
                f'<path d="M {cx-bw/2} {cy-bh/2} L {cx} {cy+bh*.1} L {cx+bw/2} {cy-bh/2}" fill="none" stroke="#B69A78" stroke-width="2"/>',
                self.circle(cx,cy+bh*.11,9,C['red']),
                self.line(cx-bw*.28,cy+bh*.31,cx+bw*.28,cy+bh*.31,'#C4AE8D',2)])
        else:
            bw,bh=min(w*.67,184),min(h*.54,118)
            self.parts.extend([self.rect(cx-bw/2,cy-bh*.1,bw,bh*.64,'#E6D1B0',2),
                f'<path d="M {cx-bw*.6} {cy-bh*.13} L {cx} {cy-bh*.67} L {cx+bw*.6} {cy-bh*.13} Z" fill="#672E2F"/>',
                self.rect(cx-bw*.23,cy+bh*.08,bw*.46,bh*.46,'#573132',3),
                self.line(cx,cy+bh*.08,cx,cy+bh*.53,'#D2AC7D',2)])
    def add(self,*items): self.parts.extend(items)
    def top(self,title,back=False):
        if back: self.add(self.text(22,82,'‹',31,C['red']),self.text(54,79,title,17,bold=True,serif=True))
        else: self.add(self.text(22,81,title,19,bold=True,serif=True),self.text(350,80,'⋯',24,C['red'],anchor='middle'))
    def button(self,y,label,primary=True,x=22,w=346):
        self.add(self.rect(x,y,w,50,C['red'] if primary else C['paper'],8,C['red'] if not primary else None),
                 self.text(x+w/2,y+32,label,15,C['paper'] if primary else C['red'],True,anchor='middle'))
    def nav(self,active):
        self.add(self.rect(0,772,390,72,C['paper']),self.line(0,772,390,772))
        for i,(icon,label) in enumerate([('⌂','Khám phá'),('◎','Tour'),('♡','Đã lưu'),('◌','Cá nhân')]):
            x=49+i*97
            color=C['red'] if label==active else C['muted']
            self.add(self.text(x,806,icon,24,color,anchor='middle'),self.text(x,827,label,11,color,label==active,anchor='middle'))
    def save(self,name):
        self.parts.append('</g></svg>')
        (OUT/name).write_text('\n'.join(self.parts),encoding='utf-8')

# 01 Explore: editorial hero, place and main wayfinding.
s=SVG('01 Khám phá tại bảo tàng')
s.add(s.text(22,77,'DẤU XƯA',13,C['red'],True,spacing='2'),s.text(22,113,'Mỗi hiện vật,',27,bold=True,serif=True),s.text(22,145,'một câu chuyện.',27,bold=True,serif=True),
      s.rect(22,162,346,51,C['paper'],8,C['line']),s.text(38,183,'ĐỊA ĐIỂM ĐÃ CHỌN',10,C['muted'],True,spacing='1'),s.text(38,202,'Bảo tàng Dấu Xưa  ⌄',15,bold=True))
s.photo('bronze-drums.jpg',22,231,346,214,8)
s.add(s.rect(22,397,346,48,C['dark'],8),s.text(38,428,'Khám phá di sản quanh bạn',16,C['paper'],True,serif=True),
      s.text(22,479,'BẮT ĐẦU THAM QUAN',11,C['red'],True,spacing='1.5'))
s.button(492,'▣   Quét mã hiện vật')
s.button(554,'Chọn hiện vật từ danh sách',False)
s.add(s.text(22,645,'CÂU CHUYỆN HÔM NAY',11,C['red'],True,spacing='1.2'),s.rect(22,660,346,96,C['paper'],8,C['line']))
s.photo('bronze-drums.jpg',30,668,86,80,5)
s.add(s.text(128,688,'DẤU ẤN ĐÔNG SƠN',10,C['muted'],True),s.text(128,713,'Âm vang trống đồng',16,bold=True,serif=True),s.text(128,736,'04:10 · Nghe miễn phí',12,C['muted']))
s.nav('Khám phá');s.save('01-kham-pha.svg')

# 02 List: searchable object list and camera alternative.
s=SVG('02 Danh sách hiện vật')
s.top('Hiện vật tại địa điểm',True)
s.add(s.text(22,117,'Bảo tàng Dấu Xưa',13,C['muted']),s.rect(22,137,346,49,C['paper'],8,C['line']),s.text(38,168,'⌕  Tìm tên hoặc mã hiện vật',14,C['muted']),
      s.rect(22,201,110,35,C['red'],18),s.text(77,224,'Tất cả  4',12,C['paper'],True,anchor='middle'),
      s.rect(141,201,96,35,C['paper'],18,C['line']),s.text(189,224,'Gần tôi',12,C['muted'],anchor='middle'),
      s.rect(246,201,122,35,C['paper'],18,C['line']),s.text(307,224,'Nghe miễn phí',12,C['muted'],anchor='middle'),
      s.text(22,273,'4 câu chuyện để khám phá',19,bold=True,serif=True))
items=[('antique-camera.jpg','Chiếc máy ảnh của','người phóng viên','03:00 · Cách 20 m'),('bronze-drums.jpg','Âm vang trống đồng','','04:10 · Cách 45 m'),('old-letter.jpg','Lá thư chưa kịp gửi','','02:45 · Cách 80 m'),('heritage-gate.jpg','Cánh cổng của thời gian','','05:05 · Cách 120 m')]
for i,(photo,a,b,meta) in enumerate(items):
    y=292+i*111
    s.add(s.rect(22,y,346,101,C['paper'],8,C['line']))
    if photo=='bronze-drums.jpg': s.photo(photo,30,y+8,87,85,5)
    else: s.art({'antique-camera.jpg':'camera','old-letter.jpg':'letter','heritage-gate.jpg':'gate'}[photo],30,y+8,87,85,5)
    s.add(s.text(129,y+30,a,15,bold=True,serif=True))
    if b: s.add(s.text(129,y+49,b,15,bold=True,serif=True))
    s.add(s.text(129,y+74,meta,11,C['muted']),s.text(348,y+59,'›',26,C['red'],anchor='middle'))
s.add(s.rect(22,749,346,14,C['bg']),s.text(22,759,'Không dùng camera? Chọn trực tiếp một hiện vật.',11,C['muted']))
s.nav('Khám phá');s.save('02-danh-sach-hien-vat.svg')

# 03 Player: image, audio focus, transcript and source.
s=SVG('03 Trình phát câu chuyện')
s.top('Câu chuyện',True)
s.art('camera',22,103,346,268,8)
s.add(s.rect(22,103,346,31,C['dark'],8),s.text(37,124,'PHÒNG KÝ ỨC  ·  03:00',11,C['paper'],True,spacing='0.8'),
      s.text(22,409,'Chiếc máy ảnh của',23,bold=True,serif=True),s.text(22,438,'người phóng viên',23,bold=True,serif=True),
      s.text(22,463,'Một bức ảnh, nhiều lớp ký ức.',13,C['muted']),
      s.line(22,496,368,496,C['line'],4),s.line(22,496,150,496,C['red'],4),s.circle(150,496,6,C['red']),
      s.text(22,518,'01:05',11,C['muted']),s.text(368,518,'03:00',11,C['muted'],anchor='end'),
      s.text(85,582,'↺ 15',16,C['red'],True,anchor='middle'),s.circle(195,566,35,C['red']),
      s.text(195,579,'Ⅱ',27,C['paper'],True,anchor='middle'),s.text(305,582,'15 ↻',16,C['red'],True,anchor='middle'),
      s.rect(22,620,346,55,C['paper'],8,C['line']),s.text(37,642,'MÔ TẢ HIỆN VẬT',10,C['red'],True,spacing='1'),
      s.text(37,660,'Máy ảnh kim loại, ống kính tròn, dây da sẫm.',12,C['ink']),
      s.text(22,712,'Câu chuyện',13,C['red'],True),s.text(145,712,'Bản chép lời',13,C['muted']),s.text(285,712,'Nguồn',13,C['muted']),
      s.line(22,724,117,724,C['red'],2))
s.nav('Khám phá');s.save('03-trinh-phat.svg')

# 04 Premium preview, explicit price and free distinction.
s=SVG('04 Tour Premium')
s.top('Tour tham quan',True)
s.art('letter',22,103,346,194,8)
s.add(s.rect(36,115,105,27,C['dark'],4),s.text(88,134,'PREMIUM',10,C['paper'],True,anchor='middle',spacing='1'),
      s.text(22,331,'Những nhân chứng',25,bold=True,serif=True),s.text(22,362,'thầm lặng',25,bold=True,serif=True),
      s.text(22,389,'60 phút   ·   6 điểm dừng   ·   Đi bộ nhẹ',13,C['muted']),
      s.text(22,425,'Một tuyến kể chuyện kết nối những hiện vật nhỏ',13),s.text(22,445,'với các bước ngoặt lớn của lịch sử.',13),
      s.rect(22,470,346,108,C['paper'],8,C['line']),s.text(38,493,'BẠN NHẬN ĐƯỢC',10,C['red'],True,spacing='1'),
      s.text(38,519,'✓  Tuyến nghe 6 điểm được biên tập',13),s.text(38,544,'✓  Ảnh tái dựng và nội dung mở rộng',13),
      s.rect(22,590,346,67,C['blush'],8),s.text(38,615,'Nội dung cơ bản vẫn miễn phí',14,C['dark'],True),
      s.text(38,638,'Bạn có thể nghe từng câu chuyện riêng.',12,C['muted']),
      s.text(22,693,'49.000đ',24,C['red'],True,serif=True),s.text(368,691,'Giá một lần',12,C['muted'],anchor='end'))
s.button(706,'Xem trước và tiếp tục')
s.nav('Tour');s.save('04-tour-premium.svg')

# 05 AR fallback: error recovery instead of a dead end.
s=SVG('05 Phương án khi AR không dùng được')
s.top('Điểm 1 · Tour Premium',True)
s.art('gate',22,105,346,205,8)
s.add(s.text(22,349,'Cánh cổng của thời gian',23,bold=True,serif=True),s.text(22,374,'Kiến trúc và ký ức  ·  12 phút',12,C['muted']),
      s.rect(22,400,346,164,C['paper'],8,C['line']),s.circle(49,429,15,C['blush']),s.text(49,435,'!',18,C['red'],True,anchor='middle'),
      s.text(75,434,'AR không khả dụng',16,C['dark'],True),
      s.text(38,467,'Thiết bị này chưa mở được tái dựng AR.',13),
      s.text(38,488,'Bạn vẫn có thể khám phá điểm dừng bằng',13),
      s.text(38,509,'ảnh, âm thanh và phần chữ.',13),
      s.text(22,603,'CHỌN CÁCH TIẾP TỤC',11,C['red'],True,spacing='1'),
      s.rect(22,619,346,62,C['paper'],8,C['line']),s.text(38,645,'▧   Xem ảnh tái dựng',15,bold=True),s.text(38,666,'Có chú thích và mốc thời gian',11,C['muted']),
      s.rect(22,692,346,62,C['paper'],8,C['line']),s.text(38,718,'♫   Nghe câu chuyện và đọc tóm tắt',14,bold=True),s.text(38,738,'Điều khiển âm thanh luôn sẵn có',11,C['muted']))
s.nav('Tour');s.save('05-ar-thay-the.svg')

# 06 Accessible settings and explicit labels.
s=SVG('06 Cài đặt trợ năng')
s.top('Trợ năng',True)
s.add(s.rect(22,104,346,90,C['dark'],8),s.text(38,133,'Trải nghiệm theo cách của bạn',17,C['paper'],True,serif=True),
      s.text(38,157,'Âm thanh, chữ và điều khiển rõ ràng',12,C['paper']),s.text(38,177,'trong suốt chuyến tham quan.',12,C['paper']),
      s.text(22,229,'ÂM THANH VÀ PHẢN HỒI',11,C['red'],True,spacing='1'))
rows=[('Mô tả hiện vật bằng chữ','Hiện mô tả trước câu chuyện','ON'),('Tín hiệu rung','Tùy chọn minh họa trong bản mẫu','OFF'),('Tăng tương phản','Làm đậm chữ và đường viền','ON'),('Giảm chuyển động','Tắt các hiệu ứng không cần thiết','OFF')]
ys=[246,328,472,554]
for (title,sub,state),y in zip(rows,ys):
    s.add(s.rect(22,y,346,72,C['paper'],8,C['line']),s.text(38,y+27,title,14,bold=True),s.text(38,y+50,sub,11,C['muted']),
          s.rect(313,y+22,41,26,C['green'] if state=='ON' else C['line'],13),s.circle(340 if state=='ON' else 326,y+35,9,C['paper']))
s.add(s.text(22,455,'HIỂN THỊ',11,C['red'],True,spacing='1'),s.rect(22,636,346,85,C['paper'],8,C['line']),
      s.text(38,666,'Cỡ chữ',14,bold=True),s.text(38,689,'Áp dụng cho nội dung và nút bấm',11,C['muted']),
      s.rect(260,652,94,45,C['bg'],5,C['line']),s.text(277,682,'−',21,C['red'],anchor='middle'),s.text(307,680,'110%',12,C['ink'],True,anchor='middle'),s.text(339,682,'+',19,C['red'],anchor='middle'),
      s.text(22,747,'Không thiết lập nào làm mất nội dung.',11,C['muted']))
s.nav('Cá nhân');s.save('06-tro-nang.svg')

# A single board for quick review; import individual SVGs for editable screen groups.
names=['01-kham-pha.svg','02-danh-sach-hien-vat.svg','03-trinh-phat.svg','04-tour-premium.svg','05-ar-thay-the.svg','06-tro-nang.svg']
board=['<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="2560" height="1090" viewBox="0 0 2560 1090">',
       '<rect width="2560" height="1090" fill="#E8E3DC"/>',
       '<text x="54" y="69" font-family="Noto Serif, Georgia, serif" font-size="30" font-weight="700" fill="#542020">Dấu Xưa · Bộ mockup mức cao</text>',
       '<text x="54" y="102" font-family="Noto Sans, Arial, sans-serif" font-size="16" fill="#59636E">6 màn hình chính · khung 390 × 844 px · bản nguồn SVG để nhập Figma</text>']
for i,name in enumerate(names):
    encoded=b64encode((OUT/name).read_bytes()).decode()
    x=54+i*416
    board.append(f'<image x="{x}" y="160" width="390" height="844" href="data:image/svg+xml;base64,{encoded}"/>')
    board.append(f'<text x="{x}" y="1030" font-family="Noto Sans, Arial, sans-serif" font-size="15" font-weight="600" fill="#542020">{escape(name.removesuffix(".svg"))}</text>')
board.append('</svg>')
(OUT/'Dau_Xua_High_Fidelity_Board.svg').write_text('\n'.join(board),encoding='utf-8')
print('Generated 6 screens and 1 board in',OUT)
