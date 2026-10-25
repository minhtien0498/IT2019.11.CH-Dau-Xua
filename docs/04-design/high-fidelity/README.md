# Dấu Xưa – mockup mức cao trên Figma

Bộ này gồm **22 màn hình và trạng thái mobile 390 × 844 px** cho toàn bộ 14 trang của prototype, hai hộp thoại quét/mua và các nhánh quan trọng của luồng miễn phí, Premium, trợ năng.

- `01-` đến `22-*.svg`: từng màn hình/trạng thái vector đã nhập vào Figma; chữ, hình khối và minh họa là các phần tử SVG.
- Các PNG cùng tên: bản xem trước từng màn hình.
- `Dau_Xua_High_Fidelity_Board.svg/.png`: bảng tổng quan sáu màn hình đầu.
- `Dau_Xua_Full_Mockup_Board.png`: bảng tổng quan đủ 22 màn hình/trạng thái.
- `scripts/generate_week6_mockup.py` tạo sáu màn hình đầu; `scripts/generate_week6_full_mockup.py` tạo thêm 16 màn hình/trạng thái và bản PNG tổng quan. Ảnh trống đồng được lấy từ `app/public/images/bronze-drums.jpg`; các hiện vật khác dùng minh họa vector vì ảnh mẫu trong app không khớp nội dung.

## File Figma

**Dấu Xưa · Mockup mức cao · Bài tập 6:** https://www.figma.com/design/fYqJNkIZOrHHubt2pVu7Y5

22 màn hình/trạng thái 390 × 844 px đã được nhập và xếp theo luồng tham quan miễn phí, Premium, sau đó đến Đã lưu/Cá nhân trên cùng trang. Mỗi màn hình là một frame riêng; chữ và hình vector là các lớp có thể chỉnh sửa trong Figma. Đã kiểm tra ảnh xuất của màn hình Khám phá và Xác nhận mua, dấu tiếng Việt và số lớp của cả 22 frame. PNG trong thư mục này là bản xem trước được xuất từ nguồn SVG.

Các màn hình 07–17 bổ sung Chào mừng, Chọn địa điểm, Quét mã, Gợi ý tiếp theo, Danh sách tour, Xác nhận mua, Tiến trình, Điểm Premium, Hoàn thành, Đã lưu và Cá nhân. Các frame 18–22 thể hiện nhập mã lỗi, Đã lưu rỗng, không có quyền camera, bản chép lời, dòng thời gian/nguồn. File Figma đã có 113 vùng bấm trong suốt để chuyển giữa các frame cho luồng miễn phí, Premium, trợ năng và thanh điều hướng dưới. Màn hình Chào mừng là điểm bắt đầu prototype chính. Các điều khiển trong cùng màn hình như phát âm thanh, bộ lọc và công tắc thiết lập vẫn là minh họa; hai trạng thái camera không có quyền và Đã lưu rỗng chưa có đường vào từ luồng chính. Kiểm tra cấu trúc cho thấy mọi liên kết đều trỏ tới frame tồn tại; chưa kiểm tra thao tác thực tế trong chế độ Present vì Figma MCP đã chạm giới hạn lượt gọi của gói Starter.

Nội dung lịch sử và giao dịch là minh họa, chưa được xác minh. Wireframe Figma mức trung bình vẫn cần hoàn tất trong một file riêng trước khi chốt luồng.
