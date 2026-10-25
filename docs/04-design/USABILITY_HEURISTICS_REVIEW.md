# Rà soát usability heuristics cho Dấu Xưa

Ngày rà soát: 03/10/2026  
Phạm vi: prototype React 0.5.0, hai luồng miễn phí và trả phí  
Khung đánh giá: 10 usability heuristics của Nielsen

Tài liệu này là phần chuẩn bị cho buổi kiểm tra tiến độ tuần 4. Mỗi nguyên tắc được nối với quyết định thiết kế có thể chỉ ra trực tiếp trên giao diện, thay vì chỉ nêu định nghĩa.

## Bảng đối chiếu 10 heuristic

| Heuristic | Cách áp dụng trong Dấu Xưa | Lý do phù hợp với người dùng | Minh chứng trên prototype |
|---|---|---|---|
| 1. Hiển thị trạng thái hệ thống | Hiện địa điểm đã chọn, số kết quả, trạng thái phát/tạm dừng, thời gian đã nghe và còn lại, tiến độ tour, trạng thái tải ngoại tuyến, trạng thái thanh toán và thông báo sau thao tác. | Khách tham quan thường vừa di chuyển vừa nghe; phản hồi tức thời giúp họ biết ứng dụng đã nhận thao tác và đang ở đâu trong hành trình. | Trang Khám phá, trình phát, Hành trình của bạn, thông báo ngắn. |
| 2. Phù hợp với thế giới thực | Dùng từ quen thuộc như “hiện vật”, “điểm dừng”, “câu chuyện”, “bản chép lời”; tour biểu diễn theo tuyến và thời lượng; trình phát dùng biểu tượng phát, tạm dừng, tua 15 giây. | Ngôn ngữ bảo tàng và mô hình hành trình dễ hiểu hơn thuật ngữ kỹ thuật, giảm thời gian học giao diện. | Khám phá, Trình phát câu chuyện, Tour. |
| 3. Quyền kiểm soát và tự do của người dùng | Có nút quay lại, đóng hộp thoại, tiếp tục bản miễn phí, kết thúc khám phá, tắt âm thanh không gian/rung; hộp thoại đóng bằng Escape và trả focus về nơi mở; thao tác lưu có “Hoàn tác”. | Người dùng có thể mở nhầm câu chuyện, tour hoặc mã quét và cần thoát nhanh mà không mất ngữ cảnh. | Header, hộp thoại quét QR, xác nhận mua, toast lưu/bỏ lưu. |
| 4. Nhất quán và theo chuẩn | Nút chính/phụ, thanh đầu trang, điều hướng dưới, thẻ câu chuyện và icon được dùng nhất quán; trạng thái chọn có cả hình thức và thuộc tính truy cập; tab hỗ trợ phím mũi tên, Home và End. | Quy luật lặp lại giúp cả người mới và người dùng trình đọc màn hình dự đoán được cách thao tác. | Toàn ứng dụng, đặc biệt trang Hiện vật và các tab câu chuyện. |
| 5. Ngăn ngừa lỗi | Mã hiện vật rỗng không thể gửi; mua tour hiển thị tên, giá, nội dung và nhãn giao dịch mô phỏng trước khi xác nhận; trong lúc xử lý, lựa chọn thanh toán và nút đóng bị khóa để tránh gửi lặp. | Ngăn lỗi trước khi xảy ra an toàn hơn yêu cầu người dùng tự khôi phục, nhất là với thao tác thanh toán. | Nhập mã DX-01 và bottom sheet xác nhận mua. |
| 6. Nhận biết thay vì ghi nhớ | Địa điểm hiện tại, bộ lọc đang chọn, nội dung đang nghe, nhãn tour miễn phí/trả phí và các điều khiển luôn hiển thị; danh sách đơn giản cho phép bỏ ảnh nhưng vẫn giữ tên, khu vực, thời lượng và khoảng cách. | Người dùng không phải nhớ mã, vị trí trước đó hoặc ý nghĩa của màu sắc trong lúc tham quan. | Chọn địa điểm, Hiện vật, Story Player, Tour. |
| 7. Linh hoạt và hiệu quả sử dụng | Có ba cách mở hiện vật: quét QR, nhập mã, chọn danh sách; có tìm kiếm/lọc, thay đổi tốc độ nghe, đổi cỡ chữ, tương phản và giảm chuyển động; người dùng bàn phím có skip link và điều hướng tab chuẩn. | Hỗ trợ nhiều mức kinh nghiệm, điều kiện thiết bị và nhu cầu tiếp cận mà không tạo luồng riêng biệt. | Quét mã, Hiện vật, Trợ năng, Story Player. |
| 8. Thiết kế thẩm mỹ và tối giản | Mỗi màn hình ưu tiên một hành động chính, dùng phân cấp chữ và khoảng trắng; trang Khám phá nhấn một câu chuyện nổi bật thay vì dàn đều nhiều thẻ; thông tin chi tiết được chia theo tab. | Giảm cạnh tranh thị giác trong không gian bảo tàng vốn đã nhiều kích thích, đồng thời giữ trọng tâm ở nội dung di sản. | Chào mừng, Khám phá, Story Player. |
| 9. Nhận biết, chẩn đoán và phục hồi lỗi | Lỗi mã hiện vật nêu nguyên nhân và cung cấp mã thử; khi AR không dùng được, giao diện giải thích tình trạng và đưa ảnh, âm thanh, bản chép lời thay thế; lỗi audio hiển thị bằng chữ. | Thông báo cụ thể giúp người dùng tự tiếp tục thay vì bị chặn bởi camera, AR hoặc âm thanh. | Quét mã, điểm premium, trạng thái trình phát. |
| 10. Trợ giúp và tài liệu | Hướng dẫn ngắn xuất hiện đúng ngữ cảnh: vị trí mã QR, dữ liệu minh họa, nội dung miễn phí, chức năng của cài đặt trợ năng và lựa chọn thay thế AR. | Hỗ trợ tại chỗ giảm nhu cầu rời hành trình để đọc tài liệu dài. | Chào mừng, scanner, Trợ năng, Premium Preview và AR fallback. |

## Các cải tiến đã thực hiện sau khi nhìn lại giao diện

1. Biến “Danh sách đơn giản” từ một nút trang trí thành chế độ thực sự ẩn hình ảnh, đồng thời đổi nhãn thành “Hiện hình ảnh” để người dùng biết cách quay lại.
2. Bổ sung `aria-pressed` cho bộ lọc và chế độ danh sách, thông báo số kết quả bằng vùng live, đồng thời dịch nhãn bộ lọc khi đổi sang tiếng Anh.
3. Chuẩn hóa tab theo mô hình ARIA: liên kết tab–panel, chỉ một tab nằm trong thứ tự focus và hỗ trợ phím mũi tên, Home, End.
4. Giữ focus trong hộp thoại quét/mua, cho phép đóng bằng Escape và trả focus về phần tử đã mở hộp thoại.
5. Ngăn gửi mã hiện vật rỗng, nối thông báo lỗi với ô nhập và cho phép Enter để gửi khi đã có mã.
6. Khi thanh toán đang xử lý, đánh dấu trạng thái bận và khóa các điều khiển có thể làm lặp hoặc gián đoạn thao tác.
7. Thêm “Hoàn tác” sau thao tác lưu hoặc bỏ lưu câu chuyện.
8. Thêm liên kết “Bỏ qua đến nội dung chính” và cập nhật tiêu đề trang theo màn hình để hỗ trợ bàn phím và trình đọc màn hình.

## Điểm cần kiểm chứng với người dùng

- Chưa thể khẳng định các thay đổi làm tăng khả dụng nếu chưa thử với người dùng đại diện cho ba persona.
- Cần kiểm tra thực tế bằng VoiceOver/TalkBack, đặc biệt focus trong hộp thoại, thứ tự đọc tab và thông báo live.
- Cần quan sát liệu “Quét mã hiện vật” có nổi bật quá mức so với lối chọn từ danh sách đối với người không muốn cấp quyền camera.
- Cần đo khả năng đọc chữ và thao tác ngoài trời hoặc trong phòng trưng bày thiếu sáng; chế độ tương phản cao hiện mới là giả thuyết thiết kế.

## Kịch bản trình bày ngắn với giảng viên

1. Giới thiệu ba persona và nhu cầu khác nhau, nhấn mạnh persona khiếm thị.
2. Đi qua ba scenario và chỉ ra yêu cầu MoSCoW tương ứng.
3. Mở một HTA miễn phí và HTA tour trả phí để giải thích quan hệ giữa mục tiêu, bước thao tác và nhánh thay thế.
4. Dùng bảng trên để chọn ba ví dụ mạnh: trạng thái trình phát, ba lối mở hiện vật và phục hồi khi AR không khả dụng.
5. Kết thúc bằng những điểm chưa kiểm chứng, nêu kế hoạch usability testing thay vì tuyên bố giao diện đã tối ưu.
