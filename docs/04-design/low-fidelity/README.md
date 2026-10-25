# Phác thảo low-fi cho Mục 2.5

Thư mục này chứa ba tờ phác thảo low-fidelity số, chuẩn bị cho Mục 2.5 theo cấu trúc bài mẫu. Chúng ghi lại cấu trúc màn hình, hành động chính, nhánh thay thế và quyết định về khả năng tiếp cận; không phải mockup độ trung thực cao.

| Tệp | Nội dung |
|---|---|
| `phac-thao-lowfi-luong-mien-phi.svg` và `.png` | Chào mừng, chọn địa điểm, khám phá, quét mã, danh sách, trình phát và gợi ý tiếp theo. |
| `phac-thao-lowfi-tro-nang.svg` và `.png` | Cài đặt trợ năng, danh sách đơn giản, camera không dùng được và trình phát có mô tả hiện vật. |
| `phac-thao-lowfi-luong-premium.svg` và `.png` | Chọn tour, xem trước, xác nhận mua, tiến trình, AR không khả dụng và tổng kết. |

Nguồn tạo: `scripts/generate_lowfi_prototypes.py`. Chạy từ thư mục gốc:

```bash
python3 scripts/generate_lowfi_prototypes.py
```

SVG là nguồn vector có thể chỉnh sửa hoặc nhập vào Draw.io/Figma. Nếu giảng viên yêu cầu đúng nghĩa paper prototype, dùng các tờ này làm bố cục tham khảo để vẽ lại trên giấy hoặc tablet, sau đó chụp hay quét bản vẽ. Không trình bày các hình này là bản vẽ tay.

Các số lượng câu chuyện và trạng thái hoàn thành trong phác thảo là ý tưởng thiết kế ban đầu. Prototype 0.5.1 chỉ có bốn câu chuyện mẫu dùng chung và một điểm tour trả phí có thể thao tác; không xem các màn hình phác thảo là minh chứng chức năng đã triển khai.
