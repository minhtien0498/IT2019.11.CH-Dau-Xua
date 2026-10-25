# Dấu Xưa: HCI User-Centred Design

Dấu Xưa là ý tưởng ứng dụng hỗ trợ tham quan bảo tàng, di tích lịch sử và di sản văn hóa bằng kể chuyện, hình ảnh, âm thanh và rung. Trải nghiệm được thiết kế theo hướng mobile-first, sử dụng tại địa điểm thật và có khả năng tiếp cận cho người khiếm thị.

Mã nguồn và tài liệu dự án: [IT2019.11.CH-Dau-Xua](https://github.com/minhtien0498/IT2019.11.CH-Dau-Xua). Repo không chứa slide, bài mẫu môn học, bản lưu trữ sau hạn nộp, file môi trường cục bộ hoặc thư mục build.

## Tài liệu

Cấu trúc chính của workspace:

```text
.
├── app/                    # Mã nguồn bản mẫu React/Vite
├── docs/
│   ├── 00-yeu-cau-tung-tuan/ # Yêu cầu, hạn nộp và đầu ra từng tuần
│   ├── 01-course-materials/
│   │   ├── lectures/       # Slide môn học
│   │   └── sample-report/  # Báo cáo mẫu do giảng viên cung cấp
│   ├── 02-report/           # Nguồn Markdown, Word và tài nguyên báo cáo
│   │   ├── figures/
│   │   │   ├── competitor-apps/ # Ảnh giao diện ứng dụng tham khảo
│   │   │   └── hta/             # Ảnh PNG/SVG của 9 HTA
│   │   └── diagrams/drawio/       # Nguồn Draw.io chỉnh sửa được
│   ├── 03-submission/       # Bản DOCX/PDF và gói tài nguyên để nộp
│   ├── 04-design/           # Bản mô tả thiết kế giao diện
│   ├── 05-guides/           # Hướng dẫn cài đặt và chạy
│   └── 06-luu-tru/          # Bản chốt tại các hạn nộp
├── scripts/                # Script tạo sơ đồ và định dạng Word
├── README.md
└── CHECKLIST.md
```

Các file quan trọng:

- `docs/00-yeu-cau-tung-tuan/`: yêu cầu, hạn nộp và đầu ra cần hoàn thành của từng tuần.
- `docs/01-course-materials/lectures/`: slide và yêu cầu bài thực hành.
- `docs/01-course-materials/sample-report/CMP6214-UXD-ThuHaNgo-24104128-report.pdf`: bài mẫu do giảng viên cung cấp.
- `docs/02-report/Dau_Xua_HCI_User_Centred_Design_Expanded.md`: nguồn nội dung có thể chỉnh sửa.
- `docs/02-report/Dau_Xua_HCI_User_Centred_Design_Expanded.docx`: bản Word được đồng bộ từ nguồn Markdown.
- `docs/02-report/Dau_Xua_HCI_User_Centred_Design_Expanded_ver_BaiTap4.md` và `.docx`: bản báo cáo riêng cho Bài tập 4; giữ nguyên tiêu đề báo cáo gốc, có bảng lịch sử thay đổi và phụ lục rà soát heuristic cùng ảnh giao diện.
- `docs/02-report/Dau_Xua_HCI_User_Centred_Design_Expanded_ver_BaiTap5.md` và `.docx`: bản báo cáo tích lũy hiện hành, có Mục 2.5 về sitemap và phác thảo số low-fi, Mục 2.6 về rà soát giao diện; phác thảo giấy và wireframe Figma còn thiếu.
- `docs/02-report/Dau_Xua_Final_Report.md` và `.docx`: bản báo cáo cuối kỳ rút gọn từ `ver_BaiTap5`, giữ các đề mục cũ và thêm Mục 2.7 về liên kết xem thiết kế, mã nguồn; nhúng hình HTA, phác thảo và tám màn hình mockup đã nhập vào Figma.
- `docs/02-report/diagrams/drawio/HTA_Dau_Xua.drawio`: file Draw.io tổng hợp chín trang HTA; thư mục này cũng có chín file nguồn riêng.
- `docs/03-submission/2026-UIT-MSc-Tô Huỳnh Minh Tiến.docx` và `.pdf`: hai bản cuối để nộp.
- `docs/03-submission/2026-UIT-MSc-Tô Huỳnh Minh Tiến_ver_BaiTap4.docx` và `.pdf`: bản nộp riêng cho Bài tập 4; không ghi đè bản nộp ngày 19/09/2026.
- `docs/03-submission/2026-UIT-MSc-Tô Huỳnh Minh Tiến_ver_BaiTap5.docx` và `.pdf`: bản xuất của báo cáo tích lũy hiện hành; chưa được xem là hoàn tất hai đầu ra thực hành tuần 5.
- `docs/03-submission/finalreport_ToHuynhMinhTien_250201095.docx` và `.pdf`: bản báo cáo cuối kỳ theo mẫu tên `finalreport_tên_mssv`, đã điền MSSV 250201095.
- `docs/03-submission/Dau_Xua_Design_BaiTap5/`: thư mục tài nguyên thiết kế để tải lên Google Drive, gồm sơ đồ Draw.io/SVG, PNG xuất và ảnh giao diện minh chứng. Báo cáo DOCX/PDF Bài tập 5 nằm riêng ở cấp `docs/03-submission/`.
- `docs/04-design/DESIGN_BRIEF_DAU_XUA.md`: bản mô tả giao diện dành cho công cụ thiết kế hoặc người thiết kế.
- `docs/04-design/flowchart/`: flow chart rút gọn và sitemap tổng quan ở các định dạng Draw.io, SVG và PNG, bám theo prototype 0.5.0.
- `docs/04-design/high-fidelity/`: nguồn SVG, PNG xem trước, bảng tổng quan và liên kết [file Figma mockup mức cao](https://www.figma.com/design/fYqJNkIZOrHHubt2pVu7Y5) gồm 22 màn hình/trạng thái có lớp chữ/vector chỉnh sửa được và các vùng bấm chuyển màn hình trong prototype.
- `docs/04-design/low-fidelity/`: ba bản phác thảo số low-fi SVG/PNG; đã nhập vào [file Figma phác thảo số riêng](https://www.figma.com/design/Hswz66mX3mCWBZLek8EF2o) để chỉnh sửa, chưa phải wireframe medium-fi.
- `docs/04-design/USABILITY_HEURISTICS_REVIEW.md`: bảng đối chiếu 10 usability heuristics, lý do áp dụng và kịch bản trình bày tuần 4.
- `docs/04-design/KE_HOACH_MUC_2_5_DEN_2_7.md`: kế hoạch chuẩn bị phác thảo giấy, wireframe và mockup theo cấu trúc bài mẫu; chưa phải yêu cầu nộp chính thức.
- `docs/05-guides/START_APP.md`: hướng dẫn cài đặt, chạy, tạo bản dựng và dừng ứng dụng.
- `docs/06-luu-tru/`: các bản chốt không chỉnh sửa sau mỗi hạn nộp.
- `scripts/generate_hta_diagrams.py`: tạo lại các sơ đồ HTA trong `docs/02-report/figures/hta/`.
- `scripts/generate_hta_drawio.py`: tạo lại file Draw.io tổng hợp và chín file nguồn riêng trong `docs/02-report/diagrams/drawio/`.
- `scripts/format_report_docx.py`: áp dụng định dạng bảng và chú thích hình cho bản Word.
- `scripts/export_submission_pdf.py`: xuất bản PDF khổ A4 từ file Word nộp bài trên macOS.
- `docs/00-yeu-cau-tung-tuan/tuan-06.md`: yêu cầu thực hành của slide tuần 6 và đối chiếu hiện trạng.
- `docs/00-yeu-cau-tung-tuan/bao-cao-cuoi-ky.md`: ghi nhận yêu cầu báo cáo cuối kỳ, cách nộp và bài thi theo thông tin người học cung cấp ngày 24/10/2026; bản rút gọn và tên file nộp đã hoàn tất.
- `scripts/generate_week6_mockup.py` và `scripts/generate_week6_full_mockup.py`: tạo bộ mockup SVG/PNG mức cao và bảng tổng quan đủ 22 frame.
- `CHECKLIST.md`: trạng thái công việc và các bước tiếp theo.

## Phạm vi hiện tại

Báo cáo cuối kỳ `Dau_Xua_Final_Report` được rút gọn từ `ver_BaiTap5`, giữ các mục cũ và danh mục tham khảo, đồng thời đưa tám màn hình mockup Figma vào Mục 2.6. Mục 2.7 có liên kết đến hai file Figma và kho mã nguồn. Các bản báo cáo và bản nộp trước được giữ để tra cứu lịch sử; không sửa bản chốt trong `docs/06-luu-tru/`. Bản thử nghiệm React 0.5.1 có bốn câu chuyện mẫu, các luồng mở hiện vật, trình phát và một điểm tour trả phí để minh họa. Vị trí, QR, thanh toán, tải ngoại tuyến, AR và rung được mô phỏng; mô tả hiện vật có chữ nhưng chưa có bản thu riêng hoặc bản chép lời khớp âm thanh. Chưa kiểm thử với VoiceOver/TalkBack. Theo slide tuần 5, vẫn cần bản phác thảo giấy và wireframe số trong Figma.

Mốc từ phần mở đầu đến hết Mục 2.4 có hạn nộp ngày 19/09/2026 và đã được lưu tại `docs/06-luu-tru/2026-09-19-han-nop-muc-2.4/`. Từ ngày 20/09/2026, các thay đổi mới tiếp tục thực hiện trên bản làm việc; không ghi đè bản đã lưu.

## Xuất bản PDF để nộp

Trên macOS có cài Google Chrome, chạy lệnh sau từ thư mục gốc:

```bash
python3 scripts/export_submission_pdf.py \
  "docs/03-submission/finalreport_ToHuynhMinhTien_250201095.docx" \
  "docs/03-submission/finalreport_ToHuynhMinhTien_250201095.pdf"
```

Script xuất PDF khổ A4, giữ hình và bảng, đồng thời thêm số trang ở giữa chân trang. PDF dùng Quick Look và Chrome để kết xuất nên số trang có thể khác khi mở DOCX trực tiếp trong Microsoft Word; hãy đánh giá bố cục bản Word bằng Word.

## Chạy prototype

Yêu cầu Node.js 20 trở lên. Từ thư mục workspace:

```bash
cd app
npm install
npm run dev
```

Mở URL Vite hiển thị trong terminal. Dùng `npm run build` để kiểm tra bản dùng thử. Bản thử nghiệm có tệp giọng đọc tiếng Việt và tiếng Anh lưu cục bộ; khi đổi ngôn ngữ, màn hình chính và tệp đọc của các hiện vật đổi cùng nhau. Vị trí, camera, mã QR, AR, thanh toán và tải ngoại tuyến vẫn là mô phỏng; ứng dụng chưa gọi API hoặc máy chủ. Nội dung, ảnh và giọng đọc đều là dữ liệu minh họa, cần được thay bằng tư liệu có nguồn và bản thu chính thức trước khi dùng thật.

Port mặc định là `4173`. Xem hướng dẫn đầy đủ và cách dừng ứng dụng trong `docs/05-guides/START_APP.md`.

## Quy ước làm việc

Khi bắt đầu phiên mới, đọc `README.md`, `CHECKLIST.md` và yêu cầu của tuần đang làm trước khi chỉnh sửa. Sau khi hoàn thành một hạng mục, cập nhật trạng thái trong `CHECKLIST.md`; chỉ cập nhật README khi phạm vi, cấu trúc tài liệu hoặc cách sử dụng thay đổi. Nội dung trong `docs/02-report/` phải được giữ đồng bộ và bản cuối trong `docs/03-submission/` chỉ được cập nhật sau khi đã kiểm tra. Sau mỗi hạn nộp, tạo một thư mục mốc mới trong `docs/06-luu-tru/` và không chỉnh sửa bản đã lưu.

Kết nối Google Stitch MCP dùng biến `STITCH_API_KEY` trong file `.venv` cục bộ. File này bị loại khỏi Git và không được đưa khóa API vào tài liệu hoặc commit.

Quy trình này còn được hỗ trợ bởi skill Codex `project-readme-checklist` tại `~/.codex/skills/project-readme-checklist`. File `AGENTS.md` bảo đảm quy ước vẫn được áp dụng khi mở một phiên mới trong workspace này.
