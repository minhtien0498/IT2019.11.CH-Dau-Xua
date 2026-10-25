# Nguồn Draw.io cho các sơ đồ HTA

Thư mục này chứa nguồn có thể chỉnh sửa của chín sơ đồ HTA trong báo cáo. Các khối, nhãn và đường nối đều là phần tử Draw.io, không phải ảnh được nhúng vào trang vẽ.

## File tổng hợp

- `HTA_Dau_Xua.drawio`: gồm chín trang, tương ứng với HTA 1–9 trong báo cáo.

## Đối chiếu với hình trong báo cáo

| Hình | Nguồn Draw.io | Ảnh dùng trong báo cáo |
|---|---|---|
| Hình 3: M1 | `hta-m1-select-location.drawio` | `../../figures/hta/hta-m1-select-location.png` |
| Hình 4: M2 | `hta-m2-open-exhibit.drawio` | `../../figures/hta/hta-m2-open-exhibit.png` |
| Hình 5: M3 | `hta-m3-short-story.drawio` | `../../figures/hta/hta-m3-short-story.png` |
| Hình 6: M4 | `hta-m4-player-controls.drawio` | `../../figures/hta/hta-m4-player-controls.png` |
| Hình 7: M5 | `hta-m5-audio-description.drawio` | `../../figures/hta/hta-m5-audio-description.png` |
| Hình 8: M6 | `hta-m6-screen-reader.drawio` | `../../figures/hta/hta-m6-screen-reader.png` |
| Hình 9: M7 | `hta-m7-haptics.drawio` | `../../figures/hta/hta-m7-haptics.png` |
| Hình 10: M8 | `hta-m8-sources.drawio` | `../../figures/hta/hta-m8-sources.png` |
| Hình 11: Premium Historical Tour | `hta-premium.drawio` | `../../figures/hta/hta-premium.png` |

## Cách mở và xuất ảnh

1. Mở <https://app.diagrams.net/> hoặc ứng dụng Draw.io trên máy.
2. Trong menu **File**, chọn **Open From**, rồi chọn **Device** và mở file `.drawio` cần chỉnh.
3. Sau khi chỉnh, vào menu **File**, chọn **Export as**, rồi chọn **PNG**.
4. Xuất với nền trong suốt và thay đúng file PNG tương ứng trong `../../figures/hta/`.
5. Tạo lại hai bản Word và kiểm tra hình trước khi cập nhật file trong `docs/03-submission/`.

Chạy `python3 scripts/generate_hta_drawio.py` từ thư mục gốc để tạo lại toàn bộ nguồn Draw.io. Lưu ý: thao tác này ghi đè các chỉnh sửa thủ công trong những file `.drawio` hiện có.
