# Kế hoạch chuẩn bị Mục 2.5–2.7: Dấu Xưa

Trạng thái: chuẩn bị trước, chưa phải yêu cầu nộp chính thức của tuần 3.

Tài liệu này tách khỏi báo cáo và bản nộp đã chốt đến Mục 2.4. Khi giảng viên công bố yêu cầu, phạm vi và hạn nộp, chỉ đưa những đầu ra phù hợp vào `docs/02-report/`, đồng bộ Word rồi mới cập nhật bản nộp.

## 1. Căn cứ và giới hạn

- Slide tuần 2 yêu cầu ba chân dung người dùng, ba kịch bản, danh sách MoSCoW và HTA cho các tính năng bắt buộc; các phần này đã hoàn thành cho mốc 19/09/2026.
- Slide tuần 3 trình bày khả năng tiếp cận, thiết kế bao trùm, bảy nguyên tắc thiết kế phổ quát và WCAG 2.2. Hoạt động trên slide vẫn là hoàn thiện các đầu ra tuần trước; slide chưa quy định báo cáo Mục 2.5–2.7 hay hạn nộp mới.
- Bài mẫu tiếp tục từ Mục 2.4 bằng: 2.5 phác thảo giấy, 2.6 wireframe số, 2.7 mockup độ trung thực cao; sau đó mới đến Mục 3 về kiểm thử khả dụng.

Vì vậy, hướng chuẩn bị là tạo artefact thiết kế có thể kiểm chứng, không viết trước kết quả phỏng vấn, kiểm thử hay đánh giá mà chưa thực hiện.

## 2. Cách nối tiếp báo cáo

| Mục dự kiến | Đầu ra cần chuẩn bị | Dựa vào nội dung đã có |
|---|---|---|
| 2.5. Phác thảo giấy | Ảnh chụp hoặc bản quét các khung vẽ tay, có số màn hình và chú thích quyết định thiết kế | Persona, kịch bản, MoSCoW, chín HTA; các nguyên tắc thiết kế phổ quát trong slide tuần 3 |
| 2.6. Wireframe số | Khung xám mobile-first, có liên kết luồng và chú thích trạng thái | Các bản phác thảo đã chọn ở Mục 2.5; kiến trúc thông tin trong design brief |
| 2.7. Mockup độ trung thực cao | Màn hình hoàn chỉnh, thành phần tái sử dụng và prototype có thể thao tác | Wireframe đã duyệt; app React hiện có là minh chứng tương tác, không thay thế file thiết kế nguồn |

Khung di động 390 × 844 px vẫn là khung chính vì yêu cầu bài tập gốc nói về ứng dụng di động. Bản web đáp ứng hiện có chỉ là cách trình diễn bổ sung trên màn hình lớn, không làm mất tính mobile-first của artefact báo cáo.

## 3. Mục 2.5: Phác thảo giấy

### 3.1. Bộ màn hình cần phác thảo

Không cần phác thảo lại mọi biến thể. Cần có đủ màn hình để người đọc lần theo hai luồng và thấy các quyết định quan trọng.

| Nhóm | Màn hình dự kiến | Liên hệ HTA / yêu cầu |
|---|---|---|
| Luồng miễn phí | Chào mừng, chọn địa điểm, khám phá, quét mã và lối chọn từ danh sách, danh sách hiện vật, trình phát câu chuyện, gợi ý tiếp theo | M1–M5, M8 |
| Luồng tiếp cận | Danh sách đơn giản, trình phát có mô tả hiện vật, cài đặt trợ năng, trạng thái máy ảnh hoặc mã QR không dùng được | M2, M5–M7 |
| Luồng trả phí | Danh sách tour, xem trước tour, xác nhận mua, tiến trình tour, điểm có AR và phương án thay thế, tổng kết | SH1, SH5, C2 |

Mỗi bản phác thảo ghi số màn hình, mũi tên điều hướng, tên nút chính và một ghi chú ngắn về quyết định thiết kế. Chỉ dùng ảnh chụp hoặc bản quét phác thảo thật; không giả lập chữ viết tay bằng hình tạo tự động.

### 3.2. Những quyết định cần giải thích trong báo cáo

- Nút “Quét mã hiện vật” nổi bật, nhưng luôn có lối “Chọn hiện vật từ danh sách” để không phụ thuộc camera.
- Trình phát là trung tâm; vùng chạm phát/tạm dừng, tua lùi và tua tới đủ lớn để thao tác khi đang di chuyển.
- Mô tả hiện vật, bản chép lời và nguồn xuất hiện bằng chữ; âm thanh, rung và màu sắc không là cách truyền đạt duy nhất.
- Người dùng chọn thời lượng tour trước khi quyết định mua; giá, nội dung bao gồm và phần luôn miễn phí được đặt cạnh nhau.
- AR chỉ là lựa chọn bổ sung, có ảnh tái dựng, âm thanh và bản chép lời thay thế.

Các giải thích này lần lượt gắn với: sử dụng công bằng, linh hoạt trong sử dụng, đơn giản và dễ hiểu, thông tin có thể cảm nhận, khả năng chịu lỗi, ít tốn sức và đủ kích thước/khoảng không thao tác.

### 3.3. Tiêu chí hoàn thành Mục 2.5

- Hai luồng đi từ đầu đến cuối mà không cần suy đoán bước tiếp theo.
- Mỗi màn hình có ít nhất một hành động chính rõ ràng.
- Các nhánh lỗi hoặc thay thế quan trọng được vẽ: camera/mã QR không dùng được và AR không khả dụng.
- Bản phác thảo được đánh số, chụp rõ và ghép thành các hình có chú thích, thay vì chèn ảnh rời không có ngữ cảnh.

## 4. Mục 2.6: Wireframe số

### 4.1. Phạm vi wireframe

Tạo trên Figma hoặc Draw.io với nền trung tính, ưu tiên cấu trúc và luồng hơn màu sắc. Có thể bắt đầu bằng 13 màn hình đã xác định trong `DESIGN_BRIEF_DAU_XUA.md`, sau đó thêm ba trạng thái cần thiết:

1. Không cấp quyền camera hoặc mã không hợp lệ.
2. Danh sách rỗng hoặc không có kết quả tìm kiếm.
3. AR không khả dụng.

Tất cả frame dùng lưới 4 cột, spacing 8 px, vùng chạm tối thiểu 44 × 44 px và thứ tự focus dự kiến. Cần ghi chú vị trí chuyển trang của hai luồng, không chỉ đặt các frame cạnh nhau.

### 4.2. Thành phần dùng lại

- Thanh đầu trang, điều hướng dưới, nút chính/phụ/chữ/icon.
- Thẻ hiện vật, thẻ tour, thẻ trạng thái lỗi/rỗng/ngoại tuyến.
- Trình phát đầy đủ và trình phát thu gọn.
- Hàng cài đặt trợ năng, công tắc, bộ lọc, lựa chọn đơn, hộp thoại và thông báo ngắn.

Tên layer và component dùng tiếng Anh để dễ quản lý file thiết kế; nội dung hiện cho người dùng ưu tiên tiếng Việt. Bản tiếng Anh chỉ cần ở biến thể ngôn ngữ của mockup, không cần nhân đôi toàn bộ file wireframe.

### 4.3. Tiêu chí hoàn thành Mục 2.6

- Có nguồn file chỉnh sửa được và liên kết hoặc đường dẫn rõ ràng trong workspace.
- Luồng miễn phí và trả phí có thể lần theo bằng liên kết prototype hoặc sơ đồ flow.
- Các thành phần lặp lại là component/variant, không vẽ lại thủ công mỗi lần.
- Text scale lớn không che CTA và modal không làm mất focus.

## 5. Mục 2.7: Mockup độ trung thực cao

App React `app/` hiện là bản mockup tương tác để tham chiếu. Khi làm bộ mockup chính thức, cần xuất các màn hình có cùng nội dung và luồng với wireframe, thay vì chụp ngẫu nhiên từ app.

| Cụm mockup | Minh chứng tương tác hiện có | Cần chuẩn bị thêm cho báo cáo |
|---|---|---|
| Luồng miễn phí | Chọn địa điểm, quét mã mô phỏng, danh sách, trình phát, nguồn, gợi ý tiếp theo | Ảnh màn hình có đánh số, chú thích luồng và trạng thái không có camera |
| Tiếp cận | Cỡ chữ, tương phản, giảm chuyển động, mô tả âm thanh, bản chép lời, nhãn điều khiển | Annotation thứ tự focus, nội dung đọc bởi VoiceOver/TalkBack và không dùng màu là tín hiệu duy nhất |
| Luồng trả phí | Xem trước, nghe thử, thanh toán mô phỏng, tiến trình, AR thay thế, tổng kết | Ảnh màn hình xác nhận lỗi/thành công và mô tả điều gì vẫn miễn phí |
| Đa ngôn ngữ | Chuyển Việt/Anh, nội dung chính và audio minh họa theo ngôn ngữ | Một cặp màn hình đối chiếu và lưu ý dùng bản thu chính thức trước khi phát hành |

Phần viết cho Mục 2.7 cần giải thích ngắn gọn: cấu trúc điều hướng, thành phần tương tác thật, typography, bảng màu và cách các lựa chọn đó giải quyết nhu cầu từ persona. Không nên biến phần này thành mô tả CSS hoặc liệt kê mọi chi tiết kỹ thuật.

## 6. Thứ tự thực hiện trước khi có đề mới

1. Vẽ và chụp bộ phác thảo cho luồng miễn phí, tiếp cận và trả phí.
2. Số hóa các bản đã chọn thành wireframe; chốt danh sách component và trạng thái.
3. Đồng bộ mockup với wireframe, chuẩn bị bộ ảnh có chú thích và link prototype.
4. Chuẩn bị kịch bản kiểm thử khả dụng cho Mục 3, nhưng chỉ tuyển người tham gia và ghi kết quả khi đã có phạm vi được duyệt.

## 7. Những việc không làm trước

- Không ghi kết quả usability testing, điểm SUS, tỷ lệ hoàn thành hoặc lời trích dẫn người tham gia khi chưa có dữ liệu thật.
- Không tự đặt hạn nộp hoặc khẳng định Mục 2.5–2.7 là yêu cầu chính thức của tuần 3.
- Không thay đổi bản chốt tại `docs/06-luu-tru/2026-09-19-han-nop-muc-2.4/`.
- Không thay thế tài liệu lịch sử có nguồn bằng nội dung minh họa trong bản nộp cuối.
