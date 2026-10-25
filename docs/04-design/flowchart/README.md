# Flow chart tổng quan ứng dụng Dấu Xưa

Thư mục này chứa sơ đồ luồng tổng quan bám theo prototype React 0.5.0.

## Tệp

- `Dau_Xua_App_Flow.drawio`: luồng thao tác tổng quan dạng rút gọn, có thể chỉnh sửa trong Draw.io.
- `Dau_Xua_App_Flow.svg` và `.png`: bản xem nhanh của luồng tổng quan.
- `Dau_Xua_App_Sitemap.drawio`: sitemap phân cấp các khu vực và màn hình của ứng dụng.
- `Dau_Xua_App_Sitemap.svg` và `.png`: bản xem nhanh của sitemap.

## Phạm vi sơ đồ

Flow chart rút gọn gồm ba dải:

1. Khởi động và vào trang Khám phá.
2. Khám phá miễn phí và Story Player.
3. Tour miễn phí hoặc tour trả phí.

Sitemap thể hiện sáu nhánh cấp cao: Khởi động, Khám phá, Tour, Đã lưu, Cá nhân và Trợ năng. Các đường nối dùng trục chung và chạm trực tiếp cạnh khối; không dùng đường quay lại hoặc đường giao cắt.

Cả hai sơ đồ chỉ dùng màu đỏ nâu cho màn hình hoặc nhánh chính, còn lại dùng trắng, xám và nền kem để dễ in và trình bày.

Sơ đồ này mô tả điều hướng cấp ứng dụng, không thay thế chín HTA nhiệm vụ trong `docs/02-report/diagrams/drawio/`.
