# Hướng dẫn chạy app Dấu Xưa

## Thông tin nhanh

- Thư mục ứng dụng: `app/`
- Phiên bản hiện tại: `0.3.0`
- Công nghệ: React + Vite
- Node.js yêu cầu: phiên bản 20 trở lên
- Port mặc định: `4173`
- URL trên máy: <http://localhost:4173>
- Dữ liệu: mock cục bộ, chưa dùng backend hoặc API

## Chạy lần đầu

Từ thư mục gốc của workspace:

```bash
cd app
npm install
npm run dev
```

Sau khi terminal hiển thị `ready`, mở <http://localhost:4173>.

## Chạy những lần sau

```bash
cd app
npm run dev
```

Giữ terminal đang chạy trong lúc sử dụng app. Nhấn `Ctrl+C` trong terminal đó để dừng.

## Kiểm tra bản production

```bash
cd app
npm run build
npm run preview
```

Lệnh `npm run build` tạo đầu ra trong `app/dist/`. Lệnh preview cũng dùng port `4173`, vì vậy cần dừng dev server trước khi chạy preview.

## Kiểm tra port

Kiểm tra tiến trình đang nghe trên port `4173`:

```bash
lsof -nP -iTCP:4173 -sTCP:LISTEN
```

Dừng tiến trình đang nghe trên đúng port của app:

```bash
lsof -tiTCP:4173 -sTCP:LISTEN | xargs kill
```

Nếu port chưa được sử dụng, lệnh có thể không in gì. Không nên dừng toàn bộ port trên máy vì có thể làm tắt dịch vụ hệ thống hoặc ứng dụng khác.

## Dùng port khác

Ví dụ chạy tạm trên port `4174`:

```bash
cd app
npm run dev -- --port 4174
```

Khi đó mở <http://localhost:4174>.

## Lưu ý về bản thử nghiệm

Bản thử nghiệm 0.5.1 là web app đáp ứng cho điện thoại, máy tính bảng và màn hình lớn. Có bốn câu chuyện mẫu và các tệp giọng đọc tiếng Việt, tiếng Anh lưu cục bộ. Người dùng có thể phát, tạm dừng, tua và đổi tốc độ ở màn hình câu chuyện; khi chuyển ngôn ngữ ở trang mở đầu, thanh tiêu đề hoặc trang Cá nhân, nội dung chính và giọng đọc sẽ cùng chuyển. Phần nghe thử của tour trả phí cũng phát đúng ngôn ngữ đã chọn. Vị trí, camera, quét mã QR, AR, thanh toán, tải ngoại tuyến và rung vẫn là mô phỏng; tour trả phí chỉ có một điểm tương tác mẫu. Mô tả hiện vật hiện bằng chữ; bản chép lời khớp âm thanh và kiểm thử VoiceOver/TalkBack chưa hoàn thành. Khóa API Stitch trong `.venv` chỉ phục vụ kết nối công cụ thiết kế, không được ứng dụng đưa ra trình duyệt và không cần thiết để chạy bản thử nghiệm.
