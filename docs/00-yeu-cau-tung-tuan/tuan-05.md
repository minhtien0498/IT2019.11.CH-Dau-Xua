# Tuần 5: Kiến trúc thông tin và thiết kế điều hướng

- Ngày ghi trên slide: 12/10/2026.
- Hạn nộp tệp, định dạng nộp và trọng số: slide không nêu.
- Nguồn: `slide/05 - Information Architecture and Navigation Design.pdf`, đặc biệt trang 62 (hoạt động thực hành).

## Yêu cầu thực hành ghi trên slide

1. **Paper prototyping (low-fidelity):** Dựa trên các sơ đồ HTA, phác thảo ý tưởng thiết kế ứng dụng di động đầu tiên trên giấy. Slide nói có mẫu để in trên Moodle.
2. **Digital wireframes (medium-fidelity):** Dựa trên bản phác thảo giấy, dùng Figma thiết kế wireframe số của ứng dụng di động. Tập trung vào cấu trúc và điều hướng, chưa cần chi tiết thị giác.

Slide cũng giảng về bản đồ điều hướng/sitemap, các mức độ trung thực của prototype và các kiểu điều hướng. Sitemap là tài liệu phù hợp để giải thích kiến trúc thông tin, nhưng không được liệt kê thành một đầu ra thực hành riêng ở trang 62. Slide không yêu cầu mockup high-fidelity trong hoạt động tuần này.

## Đối chiếu bài làm hiện có (17/10/2026)

| Thành phần | Minh chứng trong workspace | Đánh giá |
|---|---|---|
| HTA làm căn cứ | Chín HTA trong `../02-report/diagrams/drawio/` và hình tại `../02-report/figures/hta/` | Đã có. |
| Sitemap | `../04-design/flowchart/Dau_Xua_App_Sitemap.drawio`, `.svg`, `.png` | Đã có bản phân cấp sáu nhánh; đã đưa vào báo cáo `ver_BaiTap5`. |
| Phác thảo low-fi | Ba tờ SVG/PNG trong `../04-design/low-fidelity/` cho luồng miễn phí, trợ năng và premium; [file Figma phác thảo số](https://www.figma.com/design/Hswz66mX3mCWBZLek8EF2o) | Đã đưa bản phác thảo số vào báo cáo `ver_BaiTap5` và nhập ba tờ SVG vào Figma. Đây chưa phải bản vẽ tay trên giấy như slide yêu cầu; các tờ cũng chưa có mũi tên nối từng bước. |
| Wireframe số medium-fi bằng Figma | Chưa thấy file hoặc liên kết Figma trong workspace | Chưa có minh chứng. Prototype React hiện có không thay cho bộ wireframe dựa trên bản phác thảo giấy. |

## Việc cần hoàn tất cho hoạt động thực hành

1. Vẽ tay hoặc vẽ trực tiếp trên mẫu giấy các màn hình đại diện cho luồng miễn phí, trợ năng và premium; chụp/quét rõ, đánh số và ghi đường chuyển màn hình theo HTA. Ba tờ low-fi số hiện có có thể dùng làm bố cục tham khảo, nhưng cần ghi đúng nguồn gốc của chúng.
2. Từ bản phác thảo đã chọn, tạo các frame wireframe mobile trong Figma, nối luồng chính và nhánh thay thế cho camera/AR không khả dụng. Lưu liên kết Figma hoặc file xuất cùng ảnh minh chứng vào workspace.
3. Khi trình bày kiến trúc thông tin, dùng sitemap trong Mục 2.5 của báo cáo `ver_BaiTap5` để giải thích nhóm nội dung và vị trí điều hướng. Bản báo cáo này đã đồng bộ Markdown, DOCX và bản nộp PDF riêng.
