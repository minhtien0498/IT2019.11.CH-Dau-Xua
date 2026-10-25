# Design Brief – Dấu Xưa

Tài liệu này dùng để giao việc cho Google Stitch, Figma AI hoặc UI/UX designer. Thiết kế cần bám theo persona, scenario, MoSCoW và HTA trong tài liệu HCI của dự án.

## 1. Tổng quan sản phẩm

Dấu Xưa là ứng dụng di động hỗ trợ người dùng khám phá bảo tàng, di tích lịch sử và di sản văn hóa ngay tại địa điểm thật. Thay vì chỉ đọc bảng thông tin dài, người dùng có thể nghe câu chuyện ngắn, xem ảnh tư liệu “xưa và nay”, nhận rung ở các mốc quan trọng và tiếp tục đến hiện vật liên quan.

Giá trị cốt lõi:

- Giúp lịch sử dễ hiểu và dễ nhớ bằng storytelling.
- Cho phép người dùng vừa di chuyển vừa nghe, không phải nhìn màn hình liên tục.
- Hỗ trợ người khiếm thị bằng audio description, screen reader và haptic cue.
- Cung cấp tour theo thời lượng để người dùng biết nên xem gì trong thời gian có hạn.

Không thiết kế Dấu Xưa thành mạng xã hội, ứng dụng đặt vé/khách sạn hoặc một bản sao của Google Maps.

## 2. Người dùng mục tiêu

### Minh – sinh viên, 21 tuổi

Muốn biết nhanh câu chuyện đáng nhớ phía sau địa điểm. Minh quen với nội dung ngắn, sử dụng smartphone thường xuyên và không thích đọc các đoạn thuyết minh dài.

### Hương – phụ huynh, 36 tuổi

Đi cùng gia đình và chỉ có 45–90 phút tham quan. Hương cần một tuyến có định hướng, nội dung dễ hiểu cho trẻ và có thể trả phí cho trải nghiệm chuyên sâu.

### Nam – người khiếm thị, 29 tuổi

Sử dụng VoiceOver hoặc TalkBack và thường đeo tai nghe. Nam cần điều khiển toàn bộ chức năng chính bằng screen reader, nghe mô tả hiện vật trước khi nghe câu chuyện và không phải phụ thuộc vào hình ảnh.

## 3. Mục tiêu thiết kế

1. Người dùng mở đúng câu chuyện của hiện vật trong tối đa ba thao tác sau khi vào địa điểm.
2. Audio là trải nghiệm trung tâm; màn hình hỗ trợ cho việc nghe thay vì cạnh tranh sự chú ý.
3. Luồng chính phải rõ ràng ngay cả khi người dùng đang đi bộ, nơi đông người hoặc ánh sáng không ổn định.
4. Accessibility là chức năng cốt lõi và miễn phí, không nằm sau paywall.
5. Premium phải thể hiện chiều sâu của trải nghiệm, không khóa thông tin lịch sử cơ bản.
6. Giao diện gợi cảm giác lịch sử và tin cậy nhưng vẫn hiện đại, không cũ kỹ hoặc nặng tính trang trí.

## 4. Nền tảng và khung thiết kế

- Nền tảng: mobile app cho iOS và Android.
- Kích thước frame tham chiếu: 390 × 844 px.
- Bố cục: mobile-first, dùng lưới 4 cột và hệ spacing 8 px.
- Vùng chạm tối thiểu: 44 × 44 px.
- Điều hướng dưới cùng: Khám phá, Tour, Đã lưu, Cá nhân.
- Hành động quét QR phải dễ thấy trên màn hình Khám phá nhưng không che nội dung.
- Nội dung phải co giãn tốt khi người dùng tăng cỡ chữ.

## 5. Hướng mỹ thuật

Từ khóa cảm xúc: trầm ấm, giàu chiều sâu, đáng tin cậy, gần gũi, tôn trọng lịch sử, hiện đại vừa đủ.

Tránh:

- Phong cách game hóa quá mạnh hoặc dùng quá nhiều badge.
- Nền giấy cũ, texture nặng, viền cổ điển rườm rà.
- Dùng đỏ/vàng quá bão hòa trên diện tích lớn.
- Màn hình dày đặc chữ hoặc có quá nhiều lựa chọn cùng cấp.
- Hiệu ứng chuyển động liên tục khi người dùng đang nghe audio.

### Bảng màu đề xuất

| Token | Màu | Mục đích |
|---|---|---|
| Background | `#F7F2E8` | Nền sáng ấm, gợi chất liệu lưu trữ lịch sử. |
| Surface | `#FFFDF8` | Card, sheet và vùng nội dung. |
| Primary | `#7A2E2E` | CTA chính, trạng thái đang phát, điểm nhấn thương hiệu. |
| Primary dark | `#542020` | Trạng thái nhấn và chữ trên nền sáng. |
| Accent | `#C7923E` | Mốc timeline và chi tiết premium; không dùng cho chữ nhỏ trên nền sáng. |
| Text primary | `#1F2933` | Nội dung chính. |
| Text secondary | `#59636E` | Metadata và mô tả phụ. |
| Divider | `#D8D0C3` | Đường phân cách nhẹ. |
| Success | `#2F6B4F` | Trạng thái hoàn thành hoặc đã tải. |
| Error | `#B42318` | Lỗi quét, thanh toán hoặc kết nối. |

Mọi cặp màu chữ/nền phải đạt độ tương phản dễ đọc. Không dùng màu sắc làm dấu hiệu duy nhất cho trạng thái.

### Typography

- Tiêu đề: Noto Serif hoặc một serif hỗ trợ đầy đủ tiếng Việt.
- Nội dung và điều khiển: Inter hoặc Noto Sans.
- Body mặc định: 16 px, line-height khoảng 24 px.
- Nhãn nút: tối thiểu 15–16 px, ưu tiên câu ngắn và động từ rõ ràng.
- Hạn chế viết toàn bộ chữ in hoa; giữ nguyên các acronym phổ biến như QR, AR.

### Hình ảnh và icon

- Ảnh lịch sử dùng tỷ lệ 4:3 hoặc 16:9, có chú thích, năm và nguồn.
- Chế độ “xưa và nay” có thanh kéo so sánh hoặc hai ảnh đặt cạnh nhau.
- Icon dạng outline, nét rõ, luôn đi kèm text label ở các hành động quan trọng.
- Premium dùng điểm nhấn màu vàng đồng vừa phải; không dùng biểu tượng vương miện lớn.

## 6. Kiến trúc thông tin

```text
Khám phá
├── Địa điểm hiện tại
├── Quét QR
├── Danh sách hiện vật gần đây
└── Story Player
    ├── Audio storytelling
    ├── Audio description
    ├── Ảnh xưa và nay
    ├── Timeline
    ├── Transcript
    └── Nguồn tham khảo

Tour
├── Tour theo thời lượng
├── Tour theo chủ đề
└── Premium Historical Tour
    ├── Preview
    ├── Thanh toán
    ├── Tiến trình tour
    ├── AR / phương án thay thế
    └── Tổng kết

Đã lưu
└── Câu chuyện và địa điểm yêu thích

Cá nhân
├── Ngôn ngữ
├── Nội dung đã mua
└── Cài đặt trợ năng
```

## 7. Danh sách màn hình cần thiết kế

### P0 – Luồng cốt lõi cần có trong prototype

#### 01. Welcome và thiết lập ban đầu

- Logo Dấu Xưa và câu giới thiệu ngắn.
- Chọn ngôn ngữ.
- Cho phép bật “Chế độ hỗ trợ tiếp cận”.
- Hai CTA: “Bắt đầu khám phá” và “Thiết lập trợ năng”.
- Không yêu cầu đăng ký tài khoản trước khi dùng nội dung miễn phí.

#### 02. Chọn địa điểm và khám phá tại địa điểm

- Trạng thái đầu cho phép dùng vị trí hiện tại hoặc tìm bảo tàng, di tích theo tên.
- Người dùng xác nhận địa điểm trước khi xem nội dung; sau đó vẫn có thể đổi địa điểm.
- Tên địa điểm hiện tại và trạng thái “Bạn đang ở đây”.
- CTA chính “Quét mã hiện vật”.
- Card “Tiếp tục nghe” nếu có nội dung đang phát.
- Danh sách 3–5 hiện vật/câu chuyện nổi bật.
- Lối vào tour 30, 60 hoặc 90 phút.

#### 03. Quét QR

- Camera view với khung quét lớn.
- Hướng dẫn ngắn bằng chữ và âm thanh.
- Nút bật đèn, nhập mã và đóng.
- Phương án thay thế rõ ràng: “Chọn hiện vật từ danh sách”.
- Trạng thái quét thành công, mã không hợp lệ và không có quyền camera.

#### 04. Danh sách hiện vật

- Tìm kiếm và bộ lọc theo khu vực/chủ đề.
- Mỗi item có ảnh, tên, thời lượng nghe và khoảng cách tương đối nếu có dữ liệu.
- Có chế độ danh sách đơn giản, thân thiện với screen reader.

#### 05. Chi tiết câu chuyện / Story Player

- Tên hiện vật, ảnh chính, thời lượng và nguồn.
- Audio description xuất hiện trước storytelling khi chế độ trợ năng được bật.
- Player lớn: tua lại 15 giây, phát/tạm dừng, tua tới 15 giây, tốc độ phát.
- Progress bar có thời gian đã nghe/còn lại.
- Tab hoặc section: Câu chuyện, Xưa và nay, Timeline, Transcript, Nguồn.
- Haptic cue chỉ xuất hiện tại mốc có ý nghĩa và có nút tắt.
- CTA cuối: “Câu chuyện tiếp theo”.

#### 06. Gợi ý điểm tiếp theo

- Hai hoặc ba gợi ý có quan hệ rõ với câu chuyện vừa nghe.
- Hiển thị thời lượng và lý do được gợi ý.
- CTA “Mở câu chuyện” và “Kết thúc khám phá”.

#### 07. Cài đặt trợ năng

- Screen reader compatibility status.
- Bật/tắt audio description.
- Bật/tắt haptic cue.
- Cỡ chữ, tăng tương phản, giảm chuyển động.
- Luôn có mô tả bằng text; toggle không phụ thuộc vào màu.

### P1 – Luồng Premium Historical Tour

#### 08. Danh sách tour

- Bộ chọn thời lượng: 30, 60, 90 phút.
- Tour miễn phí và premium được phân biệt rõ bằng label, không chỉ bằng màu.
- Mỗi card có số điểm, thời lượng, chủ đề, mức độ đi bộ và giá.

#### 09. Premium Tour Preview

- Hero image, tên tour và một đoạn giới thiệu ngắn.
- Tuyến gồm bao nhiêu điểm, thời lượng và nội dung bao gồm.
- Preview miễn phí của một đoạn audio hoặc một điểm trong tour.
- Giải thích giá trị: nội dung dài hơn, tuyến được biên tập, AR, spatial audio, offline.
- Ghi rõ audio description và thông tin cơ bản vẫn miễn phí.
- CTA “Mua tour” và CTA phụ “Tiếp tục bản miễn phí”.

#### 10. Xác nhận mua tour

- Tóm tắt tour, giá và phương thức thanh toán.
- Không thêm phí ẩn hoặc ép subscription.
- CTA “Thanh toán và bắt đầu”.
- Trạng thái đang xử lý, thành công và thất bại.

#### 11. Tiến trình Premium Tour

- Hiển thị điểm hiện tại, tổng số điểm và thời gian còn lại.
- Danh sách tuyến đơn giản; bản đồ chỉ là phần hỗ trợ.
- CTA “Bắt đầu điểm này”.
- Nút tải offline và trạng thái tải.

#### 12. Trải nghiệm tại một điểm premium

- Story Player vẫn là trung tâm.
- CTA tùy chọn “Mở tái dựng AR”.
- Nếu AR không khả dụng, cung cấp ảnh tái dựng, audio và transcript thay thế.
- Spatial audio và haptic đều có thể tắt độc lập.

#### 13. Hoàn thành tour

- Tóm tắt các mốc chính và danh sách điểm đã xem.
- Tiến độ hoàn thành rõ bằng text và biểu tượng.
- CTA “Xem lại câu chuyện”, “Lưu tour” và “Về trang chủ”.
- Không bắt buộc chia sẻ lên mạng xã hội.

## 8. Component cần tạo trong Figma

- App bar: default, back, title dài.
- Bottom navigation: default và selected.
- Primary, secondary, text và icon button; có disabled/loading state.
- Story card: compact, featured, completed và locked premium.
- Tour card: free/premium, downloaded và in-progress.
- Audio player: mini player và full player.
- Progress indicator cho story và tour.
- QR scanner overlay.
- Timeline item.
- Historical image card có caption và source.
- Accessibility setting row.
- Toggle, checkbox, radio, segmented control và filter chip.
- Bottom sheet, confirmation dialog, toast và error banner.
- Empty, loading, offline, permission denied và AR unavailable state.

Tạo component variants và dùng Auto Layout. Tên layer/component bằng tiếng Anh nhất quán; nội dung hiển thị trong prototype bằng tiếng Việt.

## 9. Quy tắc accessibility

- Mọi nút icon phải có accessible name và text label khi hành động không hiển nhiên.
- Thứ tự focus phải đi theo trình tự đọc và không bị kẹt trong modal/player.
- Không truyền đạt trạng thái chỉ bằng màu, rung hoặc âm thanh.
- Có transcript cho audio và caption/mô tả cho hình ảnh quan trọng.
- Ảnh lịch sử phải có mô tả ngắn; audio description mô tả hiện vật trước khi kể chuyện.
- Nút điều khiển audio có vùng chạm lớn và khoảng cách đủ để tránh bấm nhầm.
- Hỗ trợ tăng cỡ chữ mà không cắt nội dung hoặc che CTA.
- Cho phép tắt haptic, spatial audio và animation.
- Tránh tự động phát âm thanh khi người dùng chưa chủ động bắt đầu.
- Luồng mua và nội dung premium vẫn phải sử dụng được bằng screen reader.

## 10. Nội dung mẫu cho mockup

Đây là dữ liệu minh họa giao diện, không phải nội dung lịch sử đã được kiểm chứng.

| Trường | Nội dung mẫu |
|---|---|
| Địa điểm | Bảo tàng Dấu Xưa |
| Hiện vật | Chiếc máy ảnh của người phóng viên |
| Story title | Một khoảnh khắc được giữ lại |
| Thời lượng | 03:20 phút |
| Mô tả ngắn | Câu chuyện về cách một bức ảnh trở thành ký ức chung của nhiều thế hệ. |
| Audio description | Một máy ảnh thân kim loại màu đen, ống kính tròn nhô ra phía trước, dây đeo bằng da đã sẫm màu theo thời gian. |
| Nguồn | Nội dung minh họa – cần thay bằng nguồn bảo tàng trước khi sử dụng thật. |
| Tour premium | Những nhân chứng thầm lặng |
| Giá minh họa | 49.000đ / tour |

## 11. Hai luồng prototype bắt buộc

### Luồng miễn phí

```text
Khám phá tại địa điểm
→ Quét QR hoặc chọn từ danh sách
→ Mở Story Player
→ Nghe audio / xem ảnh / đọc nguồn
→ Chọn câu chuyện tiếp theo
```

### Luồng premium

```text
Danh sách tour
→ Premium Tour Preview
→ Xác nhận mua
→ Chọn tuyến/thời lượng
→ Trải nghiệm từng điểm
→ Lặp đến hết tour
→ Xem tổng kết
```

Prototype phải có một nhánh “AR không khả dụng” và một cách tiếp tục trải nghiệm mà không cần camera.

## 12. Đầu ra mong muốn từ designer hoặc công cụ AI

- Sitemap hoặc user-flow ngắn gọn.
- 13 màn hình mobile ở trên, ưu tiên P0 trước P1.
- Bộ design tokens và component variants.
- Prototype click-through cho luồng miễn phí và premium.
- Trạng thái lỗi/empty/loading quan trọng.
- Ghi chú accessibility cho Story Player, QR scanner và luồng thanh toán.
- Không tự bổ sung chức năng đặt vé, chat, mạng xã hội hoặc AI sinh nội dung lịch sử.

## 13. Prompt dùng trực tiếp cho Google Stitch / Figma AI

```text
Design a mobile app called “Dấu Xưa” for an HCI user-centred design project. The app helps visitors explore museums and historical sites through short audio stories, archival images, subtle haptic cues, and accessible audio descriptions.

Create a warm, trustworthy, contemporary visual direction inspired by historical archives without looking old-fashioned. Use a warm ivory background (#F7F2E8), off-white surfaces (#FFFDF8), deep heritage red as the primary color (#7A2E2E), restrained bronze accents (#C7923E), and dark slate text (#1F2933). Use Noto Serif for headings and Inter or Noto Sans for body text. All visible UI copy should be in Vietnamese.

Design for a 390 × 844 px mobile frame with an 8 px spacing system, large touch targets, clear hierarchy, Auto Layout, reusable components, and accessible contrast. The bottom navigation contains: Khám phá, Tour, Đã lưu, Cá nhân. Audio is the core interaction, so the player controls must be large and easy to operate while walking.

Primary users are: a 21-year-old student who prefers short content, a parent with only 45–90 minutes for a family visit, and a blind user who uses VoiceOver or TalkBack. Do not rely only on color, images, sound, or haptics to communicate status. Include transcripts, image descriptions, scalable text, screen-reader-friendly labels, reduced-motion support, and an option to disable haptics.

Create these screens:
1. Welcome and accessibility setup.
2. Location selection and current museum home, with current-location and name-search options.
3. QR scanner with “select from list” fallback.
4. Nearby exhibit list.
5. Full Story Player with audio description, archival image, transcript, timeline, and sources.
6. Related next-story suggestions.
7. Accessibility settings.
8. Tour list with 30/60/90-minute filters.
9. Premium Historical Tour preview with a free sample.
10. Purchase confirmation and payment states.
11. Premium tour progress.
12. Premium story point with optional AR and a non-AR fallback.
13. Tour completion summary.

Create two clickable flows: a free exhibit-story flow and a Premium Historical Tour purchase-and-completion flow. Premium adds depth through curated routes, longer stories, AR, spatial audio, and offline access, but basic historical information, audio description, and accessibility must remain free. Do not add social networking, hotel booking, flight booking, or AI-generated historical content.
```

## 14. Checklist bàn giao thiết kế

- [ ] Tất cả màn hình P0 đã được thiết kế.
- [ ] Tất cả màn hình P1 đã được thiết kế.
- [ ] Hai prototype flow có thể thao tác từ đầu đến cuối.
- [ ] Có trạng thái loading, empty, error, offline và permission denied.
- [ ] Có phương án thay thế khi QR, camera hoặc AR không hoạt động.
- [ ] Component sử dụng Auto Layout và có variants phù hợp.
- [ ] Nội dung tiếng Việt không bị tràn khi tăng cỡ chữ.
- [ ] Màu sắc, icon, haptic và audio không phải cách duy nhất truyền đạt thông tin.
- [ ] Story Player và luồng premium có annotation dành cho screen reader.
- [ ] Nội dung lịch sử minh họa được ghi rõ và chưa bị hiểu nhầm là dữ liệu thật.
