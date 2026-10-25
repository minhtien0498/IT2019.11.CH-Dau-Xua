---
title: "DẤU XƯA"
subtitle: "Báo cáo Thiết kế trải nghiệm người dùng"
author: "Học viên: Tô Huỳnh Minh Tiến"
date: "Tháng 10 năm 2026"
lang: vi-VN
---

# 1. Giới thiệu

## 1.1. Ý tưởng dự án

Dấu Xưa là ứng dụng di động dành cho khách tham quan bảo tàng, di tích lịch sử và di sản văn hóa. Tại điểm tham quan, người dùng quét mã QR hoặc chọn hiện vật từ danh sách để nghe câu chuyện ngắn, xem ảnh tư liệu và tìm nội dung liên quan. Ứng dụng có thể phát tín hiệu rung tại một số đoạn của câu chuyện.

Khách tham quan không phải lúc nào cũng dễ nắm được câu chuyện phía sau hiện vật. Bảng thuyết minh có thể dài, nhiều mốc thời gian hoặc phụ thuộc vào hình ảnh. Người có ít thời gian khó chọn điểm xem trước; trẻ em dễ mất tập trung; người khiếm thị có thể phải nhờ người đi cùng đọc và mô tả. Dấu Xưa dùng lời kể bằng âm thanh làm hình thức chính, kèm ảnh tư liệu, tín hiệu rung, bản chép lời và mô tả âm thanh.

Dự án tập trung vào việc sử dụng điện thoại tại điểm tham quan. Bản đồ và chỉ đường là chức năng hỗ trợ. Phạm vi ứng dụng không gồm đặt vé, khách sạn, nhà hàng, mạng xã hội hay nội dung lịch sử do AI tự tạo. Nội dung lịch sử cần được biên tập và ghi nguồn trước khi đưa vào sản phẩm.

## 1.2. Người dùng mục tiêu

Ba nhóm người dùng được xem xét trong báo cáo:

Nhóm 1: Sinh viên và người trẻ đi tham quan cùng bạn bè. Họ quen dùng điện thoại thông minh, thích nội dung ngắn, trực quan và muốn nắm nhanh những điểm đáng nhớ mà vẫn theo kịp nhóm.

Nhóm 2: Phụ huynh đi cùng gia đình, có ít thời gian và cần lộ trình rõ ràng, phù hợp với nhiều độ tuổi.

Nhóm 3: Người khiếm thị sử dụng VoiceOver hoặc TalkBack. Họ cần tìm, mở và điều khiển nội dung mà không phụ thuộc vào hình ảnh. Phần mô tả hiện vật nên xuất hiện trước câu chuyện chính.

Chân dung người dùng trong báo cáo không đại diện cho mọi trải nghiệm của người khiếm thị. W3C khuyến nghị mời người khuyết tật tham gia trong quá trình thiết kế, bên cạnh việc xây dựng chân dung, kịch bản và quy trình tác vụ. Các giả định ở đây cần được kiểm chứng qua phỏng vấn và thử nghiệm với người dùng thật.

## 1.3. Chức năng của ứng dụng

Trong phiên bản miễn phí, người dùng chọn địa điểm rồi mở hiện vật bằng mã QR hoặc danh sách. Trình phát cung cấp lời kể, hình ảnh, mô tả âm thanh, bản chép lời và nguồn tham khảo. Người dùng có thể phát, tạm dừng, tua, tắt rung và xem gợi ý điểm tiếp theo.

Các chức năng dự kiến khác gồm tuyến tham quan 30, 60 hoặc 90 phút, tuyến theo chủ đề, dòng thời gian ngắn, lưu và xem lại nội dung, cùng tùy chọn ngôn ngữ. Phiên bản miễn phí cũng cần hỗ trợ trình đọc màn hình, tăng cỡ chữ, tăng độ tương phản, giảm chuyển động và tránh dùng màu sắc làm dấu hiệu duy nhất.

Premium Historical Tour là tính năng trả phí chính, gồm các tuyến tham quan đã biên tập để kết nối câu chuyện ở nhiều điểm. Gói có thể bổ sung âm thanh không gian, nội dung ngoại tuyến hoặc AR. Trước khi mua, người dùng được nghe thử và xem giá, phạm vi nội dung. Nếu thiết bị không hỗ trợ AR, tuyến tham quan vẫn có ảnh tái dựng, âm thanh và bản chép lời. Thông tin lịch sử cơ bản, mô tả âm thanh và các chức năng tiếp cận vẫn miễn phí.

## 1.4. Phân tích đối thủ

Báo cáo tham khảo Smartify và Bloomberg Connects, hai ứng dụng cung cấp nội dung văn hóa trên thiết bị di động. Cách tổ chức trải nghiệm và phạm vi nội dung của chúng khác với hướng thiết kế Dấu Xưa.

![Smartify, màn hình 1](figures/competitor-apps/smartify-screen-1.png){ width=22% } ![Smartify, màn hình 2](figures/competitor-apps/smartify-screen-2.png){ width=22% } ![Smartify, màn hình 3](figures/competitor-apps/smartify-screen-3.png){ width=22% } ![Smartify, màn hình 4](figures/competitor-apps/smartify-screen-4.png){ width=22% }

Hình 1. Một số màn hình giới thiệu của Smartify. Nguồn ảnh: Apple App Store.

![Bloomberg Connects, màn hình 1](figures/competitor-apps/bloomberg-connects-screen-1.jpg){ width=22% } ![Bloomberg Connects, màn hình 2](figures/competitor-apps/bloomberg-connects-screen-2.jpg){ width=22% } ![Bloomberg Connects, màn hình 3](figures/competitor-apps/bloomberg-connects-screen-3.jpg){ width=22% } ![Bloomberg Connects, màn hình 4](figures/competitor-apps/bloomberg-connects-screen-4.jpg){ width=22% }

Hình 2. Một số màn hình giới thiệu của Bloomberg Connects. Nguồn ảnh: Apple App Store.

| Tiêu chí | Smartify | Bloomberg Connects | Hàm ý cho Dấu Xưa |
|---|---|---|---|
| Giá trị chính | Khám phá bảo tàng hoặc phòng trưng bày, nhận diện tác phẩm và nghe thuyết minh. | Cung cấp hướng dẫn tham quan miễn phí do các tổ chức văn hóa biên soạn. | Giúp người dùng mở nội dung tại chỗ nhanh, đồng thời kết nối các điểm thành một câu chuyện rõ ràng. |
| Điểm mạnh có thể học hỏi | Khả năng nhận diện hiện vật và thuyết minh bằng âm thanh giúp giảm thao tác tìm kiếm. | Hỗ trợ VoiceOver, phụ đề, bản chép lời, phóng to hình ảnh và điều chỉnh cỡ chữ. | Xem khả năng tiếp cận là yêu cầu cốt lõi; luôn có cách mở nội dung thay cho máy ảnh và có bản chép lời cho âm thanh. |
| Khoảng trống mà Dấu Xưa tập trung | Nội dung nghiêng về nghệ thuật và phụ thuộc vào các đối tác đã tham gia; ứng dụng không thể nhận diện mọi hiện vật. | Nội dung của mỗi hướng dẫn phụ thuộc vào từng tổ chức; ứng dụng không tập trung vào kể chuyện bằng rung hoặc tuyến tái dựng trả phí. | Tập trung vào lịch sử và di sản Việt Nam, kể chuyện ngay tại địa điểm, dùng rung có chọn lọc và luôn có phương án thay thế AR. |

Theo công bố của Smartify, ứng dụng hỗ trợ nhận diện tác phẩm hoặc hiện vật, tìm địa điểm và phát thuyết minh. Khả năng nhận diện phụ thuộc vào quan hệ đối tác và bản quyền. Bloomberg Connects công bố các hỗ trợ như VoiceOver, phụ đề, bản chép lời, phóng to ảnh và điều chỉnh cỡ chữ. Bảng trên đối chiếu thông tin do hai sản phẩm công bố, chưa dựa trên kiểm thử trực tiếp với người dùng.

Dấu Xưa tập trung vào các câu chuyện ngắn tại di sản Việt Nam thay vì mở rộng số lượng bộ sưu tập. Nội dung cơ bản được mở miễn phí; gói trả phí dự kiến có tuyến chuyên sâu, âm thanh không gian, nội dung ngoại tuyến và AR tùy chọn. Giá trị của hướng thiết kế này cần được kiểm chứng với người dùng.

# 2. Thiết kế trải nghiệm người dùng

Thiết kế lấy người dùng làm trung tâm (UCD) xem xét nhu cầu và bối cảnh sử dụng qua nhiều vòng. Theo nội dung môn học, quy trình gồm tìm hiểu người dùng, xác định yêu cầu, đề xuất giải pháp, đánh giá và điều chỉnh.

Mục 2.1–2.2 trình bày chân dung và kịch bản để xác định mục tiêu, bối cảnh và khó khăn của người dùng. Mục 2.3 phân loại yêu cầu theo MoSCoW; Mục 2.4 mô tả các nhiệm vụ bằng HTA. Các nội dung này dựa trên giả định ban đầu và cần kiểm chứng với người dùng thật.

## 2.1. Chân dung người dùng

Ba chân dung dưới đây mô tả bối cảnh, mục tiêu và rào cản của các nhóm người dùng đã chọn. Chân dung 3 là người khiếm thị, theo yêu cầu của bài tập. Đây là các chân dung giả định, chưa được xác thực qua nghiên cứu người dùng.

### Chân dung 1: Minh, sinh viên

| Thuộc tính | Mô tả |
|---|---|
| Tuổi, nghề nghiệp, nơi sống | 21 tuổi; sinh viên năm ba; sống tại TP.HCM. |
| Tính cách | Tò mò, cởi mở, thích khám phá và chia sẻ trải nghiệm với bạn bè. |
| Thiết bị và thói quen | Dùng điện thoại thông minh thường xuyên; quen Google Maps, TikTok và Instagram; thường xem nội dung ngắn thay vì đọc bài dài. |
| Bối cảnh | Tham quan cùng bạn, thời gian dừng ở mỗi điểm ngắn và không muốn nhìn màn hình liên tục. |
| Động lực | Muốn hiểu nhanh câu chuyện đáng nhớ nhất của địa điểm. |
| Mục tiêu | Mở đúng nội dung ngay tại hiện vật; nghe một câu chuyện trong 2–3 phút; biết điểm nào nên xem tiếp. |
| Rào cản / thất vọng | Bảng thuyết minh dài, nhiều tên và mốc thời gian; khó hình dung sự kiện chỉ từ chữ và ảnh tĩnh. |
| Nhu cầu từ Dấu Xưa | Mã QR hoặc danh sách hiện vật; câu chuyện ngắn; lời kể bằng âm thanh; ảnh tư liệu; rung có chọn lọc; gợi ý điểm tiếp theo. |

### Chân dung 2: Hương, phụ huynh tham quan cùng gia đình

| Thuộc tính | Mô tả |
|---|---|
| Tuổi, nghề nghiệp, nơi sống | 36 tuổi; nhân viên văn phòng; sống tại TP.HCM. |
| Tính cách | Có kế hoạch, thực tế; thích hoạt động vừa giải trí vừa giúp con học thêm. |
| Thiết bị và thói quen | Lên kế hoạch bằng điện thoại, đọc đánh giá và xem trước thời lượng tham quan. |
| Bối cảnh | Đi cùng chồng và con; chỉ có 45–90 phút tại một địa điểm. |
| Động lực | Muốn cả gia đình hiểu được những câu chuyện chính trong thời gian tham quan có hạn. |
| Mục tiêu | Chọn lộ trình phù hợp với thời gian, giữ được sự chú ý của trẻ và cân nhắc mua nội dung chuyên sâu khi lợi ích được trình bày rõ. |
| Rào cản / thất vọng | Không biết nên đi tuyến nào; trẻ dễ chán nếu chỉ đọc; nội dung tại chỗ đôi khi quá học thuật. |
| Nhu cầu từ Dấu Xưa | Tuyến tham quan theo thời lượng; ngôn ngữ dễ hiểu; xem trước nội dung trả phí; thanh toán ngắn gọn; phần tóm tắt sau chuyến tham quan. |

### Chân dung 3: Nam, người khiếm thị

| Thuộc tính | Mô tả |
|---|---|
| Tuổi, nghề nghiệp, nơi sống | 29 tuổi; nhân viên văn phòng; sống tại TP.HCM; khiếm thị nặng. |
| Tính cách | Độc lập, kiên nhẫn; thích lịch sử, chương trình âm thanh và các sản phẩm có khả năng tiếp cận tốt. |
| Thiết bị và thói quen | Dùng iPhone hoặc Android với VoiceOver/TalkBack; thường dùng tai nghe. |
| Bối cảnh | Tham quan cùng bạn hoặc tự trải nghiệm một phần nội dung trong không gian đông người. |
| Động lực | Muốn chủ động khám phá bảo tàng và giảm việc phải nhờ người khác đọc hoặc mô tả. |
| Mục tiêu | Biết mình đang nghe về hiện vật nào; nghe mô tả hình dáng trước câu chuyện; điều khiển toàn bộ luồng bằng trình đọc màn hình. |
| Rào cản / thất vọng | Thông tin chủ yếu là chữ và hình; khó biết hiện vật nào ở gần; mã QR và máy ảnh có thể khó tự thao tác. |
| Nhu cầu từ Dấu Xưa | Danh sách thay cho mã QR; mô tả âm thanh; nhãn rõ cho trình đọc màn hình; nút lớn; tín hiệu rung đơn giản và có thể tắt. |

## 2.2. Kịch bản người dùng

Ba kịch bản đặt các chân dung vào tình huống tham quan cụ thể để xác định thao tác và trở ngại cần xử lý. Kịch bản 3 mô tả tính năng trả phí theo yêu cầu của bài tập.

### Kịch bản 1: Minh khám phá nhanh một hiện vật

Minh đến một di tích lịch sử cùng nhóm bạn. Sau khi chụp ảnh, Minh muốn biết sự kiện từng diễn ra tại đây nhưng không muốn đọc bảng thông tin dài. Minh mở Dấu Xưa, chọn địa điểm và quét mã QR bên cạnh hiện vật. Nếu máy ảnh không hoạt động, Minh nhập mã hoặc chọn hiện vật từ danh sách. Câu chuyện kéo dài khoảng 2–3 phút, có lời kể, ảnh tư liệu và một vài tín hiệu rung ở đoạn quan trọng. Kết thúc câu chuyện, ứng dụng gợi ý hai điểm gần đó.

Minh cần mở đúng câu chuyện và nắm ý chính trong thời gian ngắn.

Luồng mở hiện vật cần nhanh và không buộc Minh nhìn màn hình liên tục. Trình phát cần các thao tác phát, tạm dừng, tua, bỏ qua và xem nguồn. Tín hiệu rung chỉ xuất hiện khi cần; người dùng luôn có cách mở hiện vật mà không dùng máy ảnh.

### Kịch bản 2: Nam tham quan bằng trình đọc màn hình

Nam đến bảo tàng và bật chế độ hỗ trợ tiếp cận. Anh dùng VoiceOver hoặc TalkBack để duyệt danh sách hiện vật gần đó thay cho máy ảnh. Sau khi chọn hiện vật, Nam nghe tên, mô tả hình dáng và bối cảnh trước câu chuyện. Tín hiệu rung báo khi nội dung chuyển phần và có thể tắt. Nghe xong, anh chuyển tiêu điểm đến gợi ý tiếp theo mà không cần dựa vào hình ảnh hoặc màu sắc.

Nam muốn tự nhận biết và khám phá hiện vật bằng công nghệ hỗ trợ.

Luồng chính cần dùng được với trình đọc màn hình: nút có tên rõ, tiêu điểm theo thứ tự hợp lý và phần mô tả hiện vật tách khỏi câu chuyện. Màu sắc, âm thanh hoặc rung không được là dấu hiệu duy nhất cho một thông tin.

### Kịch bản 3: Hương mua và sử dụng Premium Historical Tour

Hương có một giờ tham quan cùng gia đình và chọn tuyến 60 phút. Ứng dụng giới thiệu Premium Historical Tour “Những nhân chứng thầm lặng” với sáu điểm dừng. Hương xem lộ trình, nội dung, giá và nghe thử trước khi mua. Sau khi thanh toán, gia đình đi theo tuyến đã biên tập. Tại mỗi điểm, ứng dụng phát câu chuyện dài hơn và gợi ý âm thanh không gian hoặc AR. Nếu thiết bị không dùng được AR, gia đình tiếp tục bằng ảnh tái dựng, âm thanh và bản chép lời. Cuối chuyến đi, ứng dụng tóm tắt các mốc chính và lưu những điểm đã xem.

Hương cần một tuyến chuyên sâu vừa trong một giờ và phù hợp để cả gia đình theo dõi.

Trang giới thiệu cần nêu rõ nội dung và giá trước bước mua. Quy trình thanh toán, bắt đầu tuyến cần ngắn gọn và hiển thị tiến độ rõ. AR là lựa chọn bổ sung, có phương án thay thế; thông tin lịch sử cơ bản vẫn miễn phí.

## 2.3. Yêu cầu người dùng

Các yêu cầu dưới đây được rút ra từ mục tiêu và khó khăn trong ba kịch bản. MoSCoW chia chúng thành bốn nhóm: Must Have (bắt buộc), Should Have (nên có), Could Have (có thể bổ sung) và Won’t Have (chưa thực hiện trong phạm vi hiện tại).

### Bắt buộc phải có (Must Have)

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| M1 | Người dùng có thể chọn đúng bảo tàng hoặc di tích đang tham quan. | Kịch bản 1, 2 |
| M2 | Người dùng có thể mở hiện vật bằng mã QR, nhập mã hoặc chọn từ danh sách; máy ảnh không phải là cách duy nhất. | Kịch bản 1, 2 |
| M3 | Mỗi hiện vật có một câu chuyện ngắn, kết hợp lời kể bằng âm thanh và hình ảnh. | Kịch bản 1 |
| M4 | Trình phát câu chuyện có chức năng phát, tạm dừng, tua, bỏ qua và hiển thị tiến độ. | Kịch bản 1, 2 |
| M5 | Hình ảnh quan trọng có mô tả bằng chữ; hiện vật có phần mô tả âm thanh tách khỏi câu chuyện chính. | Kịch bản 2 |
| M6 | Luồng chính và các nút điều khiển tương thích với VoiceOver/TalkBack; thông tin không chỉ được thể hiện bằng màu sắc, hình ảnh, âm thanh hoặc rung. | Kịch bản 2 |
| M7 | Người dùng có thể tắt tín hiệu rung; ứng dụng chỉ rung ở những mốc nội dung có ý nghĩa. | Kịch bản 1, 2 |
| M8 | Nội dung lịch sử hiển thị nguồn tham khảo hoặc ghi chú biên tập. | Kịch bản 1 |

### Nên có (Should Have)

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| SH1 | Tuyến tham quan theo thời lượng 30, 60 hoặc 90 phút. | Kịch bản 3 |
| SH2 | Tuyến tham quan theo chủ đề và gợi ý điểm tiếp theo. | Kịch bản 1, 3 |
| SH3 | Lưu nội dung yêu thích, xem lại và xem dòng thời gian ngắn. | Kịch bản 1, 3 |
| SH4 | Hỗ trợ đa ngôn ngữ. | Nhóm khách tham quan |
| SH5 | Premium Historical Tour cho phép xem trước nội dung, hiển thị rõ giá và phạm vi của gói, có quy trình thanh toán ngắn gọn và phần tóm tắt sau khi hoàn thành. | Kịch bản 3 |

### Có thể có (Could Have)

| Mã | Yêu cầu | Nguồn |
|---|---|---|
| C1 | Câu hỏi ngắn từ 1–3 câu, chế độ trẻ em và huy hiệu hoàn thành chuyến tham quan. | Chân dung 2 |
| C2 | Tái dựng bằng AR tại một số điểm trả phí, luôn kèm ảnh, âm thanh và bản chép lời thay thế. | Kịch bản 3 |
| C3 | Âm thanh không gian và gói nội dung ngoại tuyến cho tuyến tham quan trả phí. | Kịch bản 3 |
| C4 | Chia sẻ câu chuyện hoặc địa điểm. | Chân dung 1 |

### Chưa thực hiện trong phạm vi hiện tại (Won’t Have)

| Mã | Yêu cầu | Lý do |
|---|---|---|
| W1 | Mạng xã hội hoặc trò chuyện trực tuyến. | Không phục vụ mục tiêu khám phá tại chỗ. |
| W2 | Đặt khách sạn, nhà hàng, chuyến bay hoặc vé du lịch. | Làm sản phẩm thành ứng dụng du lịch tổng hợp. |
| W3 | Trải nghiệm bắt buộc dùng kính thực tế ảo. | Không phù hợp với phạm vi ứng dụng trên điện thoại. |
| W4 | AI tự sinh hoặc người dùng tự đăng nội dung lịch sử. | Rủi ro sai lệch và khó kiểm soát độ tin cậy. |

Khả năng tiếp cận và thông tin lịch sử cơ bản thuộc nhóm bắt buộc và được cung cấp miễn phí. Gói tham quan trả phí thuộc nhóm nên có. AR, âm thanh không gian và nội dung ngoại tuyến thuộc nhóm có thể bổ sung; người dùng vẫn cần hoàn thành tuyến khi thiết bị không hỗ trợ các chức năng này.

## 2.4. Phân tích nhiệm vụ theo thứ bậc (HTA)

HTA chia mục tiêu thành các nhiệm vụ và nhiệm vụ con để kiểm tra trình tự thao tác, nhánh thay thế và bước rườm rà. Theo yêu cầu đánh giá tiến độ, mỗi chức năng bắt buộc có một sơ đồ riêng; bài tập trên lớp cũng yêu cầu mô tả tương tác với chức năng miễn phí và trả phí. Do đó, HTA 1–8 tương ứng M1–M8; HTA 9 mô tả Premium Historical Tour. Sơ đồ thể hiện đầy đủ các bước và kế hoạch thao tác. Phần chữ ghi những nhánh quyết định và giới hạn triển khai cần lưu ý.

### HTA 1: Chọn đúng địa điểm đang tham quan cho M1

Người dùng xác định địa điểm qua vị trí mô phỏng, tìm tên hoặc chọn từ danh sách, sau đó kiểm tra tên trước khi xác nhận. Nếu chọn sai, họ quay lại bước chọn địa điểm.

![Sơ đồ 3. HTA cho M1: chọn đúng địa điểm](figures/hta/hta-m1-select-location.png){ width=95% }

Hình 3. HTA cho M1: chọn đúng địa điểm

### HTA 2: Mở đúng nội dung của một hiện vật cho M2

Quét QR, nhập mã và chọn từ danh sách đều dẫn đến cùng nội dung hiện vật. Khi mã không hợp lệ hoặc camera không dùng được, người dùng chuyển sang cách mở khác.

![Sơ đồ 4. HTA cho M2: mở đúng hiện vật](figures/hta/hta-m2-open-exhibit.png){ width=95% }

Hình 4. HTA cho M2: mở đúng hiện vật

### HTA 3: Nghe câu chuyện ngắn có âm thanh và hình ảnh cho M3

Thiết kế kết hợp lời kể với hình ảnh và có bản chép lời để thay thế âm thanh. Bản mẫu mới có tóm tắt bằng chữ, chưa có bản chép lời khớp tệp đọc.

![Sơ đồ 5. HTA cho M3: nghe câu chuyện ngắn](figures/hta/hta-m3-short-story.png){ width=95% }

Hình 5. HTA cho M3: nghe câu chuyện ngắn

### HTA 4: Điều khiển trình phát câu chuyện cho M4

Người dùng có thể phát, tạm dừng, tua và theo dõi tiến độ mà không rời câu chuyện. Các thao tác điều khiển có thể lặp lại.

![Sơ đồ 6. HTA cho M4: điều khiển trình phát câu chuyện](figures/hta/hta-m4-player-controls.png){ width=95% }

Hình 6. HTA cho M4: điều khiển trình phát câu chuyện

### HTA 5: Truy cập mô tả của hiện vật và hình ảnh cho M5

Thiết kế cho phép tiếp cận mô tả hình dáng bằng âm thanh hoặc chữ. Bản mẫu đã có mô tả bằng chữ nhưng chưa có bản thu riêng.

![Sơ đồ 7. HTA cho M5: truy cập mô tả](figures/hta/hta-m5-audio-description.png){ width=95% }

Hình 7. HTA cho M5: truy cập mô tả

### HTA 6: Hoàn thành luồng chính bằng trình đọc màn hình cho M6

Luồng chính cần có nhãn điều khiển và thứ tự tiêu điểm phù hợp với VoiceOver hoặc TalkBack. Đây là yêu cầu thiết kế, chưa được kiểm thử thực tế với trình đọc màn hình.

![Sơ đồ 8. HTA cho M6: hoàn thành luồng bằng trình đọc màn hình](figures/hta/hta-m6-screen-reader.png){ width=95% }

Hình 8. HTA cho M6: hoàn thành luồng bằng trình đọc màn hình

### HTA 7: Thiết lập và sử dụng tín hiệu rung cho M7

Người dùng có thể bật hoặc tắt rung mà không ảnh hưởng đến việc nghe. Bản mẫu mới có công tắc minh họa; rung theo mốc nội dung chưa được triển khai.

![Sơ đồ 9. HTA cho M7: thiết lập tín hiệu rung](figures/hta/hta-m7-haptics.png){ width=95% }

Hình 9. HTA cho M7: thiết lập tín hiệu rung

### HTA 8: Kiểm tra nguồn của nội dung lịch sử cho M8

Từ câu chuyện, người dùng mở mục Nguồn để xem trích dẫn hoặc ghi chú biên tập rồi quay lại. Bản mẫu chỉ ghi nội dung là minh họa; nguồn lịch sử thật chưa được bổ sung.

![Sơ đồ 10. HTA cho M8: kiểm tra nguồn](figures/hta/hta-m8-sources.png){ width=95% }

Hình 10. HTA cho M8: kiểm tra nguồn

### HTA 9: Mua và trải nghiệm Premium Historical Tour

Người dùng xem giá, nghe thử rồi mua tour và tham quan các điểm trong tuyến. AR, âm thanh không gian và rung là tùy chọn; nội dung thay thế cần giúp họ tiếp tục tuyến. Bản mẫu chỉ có một điểm tương tác và bước mua mô phỏng.

![Sơ đồ 11. HTA cho Premium Historical Tour](figures/hta/hta-premium.png){ width=95% }

Hình 11. HTA cho Premium Historical Tour

HTA 9 dựa trên Kịch bản 3 và yêu cầu SH5. Người dùng cần hoàn thành được tuyến trả phí dù không sử dụng AR, rung hoặc âm thanh không gian.

## 2.5. Kiến trúc thông tin và phác thảo độ trung thực thấp

### 2.5.1. Sitemap và điều hướng

Sitemap nhóm nội dung thành sáu khu vực: Khởi động, Khám phá, Tour, Đã lưu, Cá nhân và Trợ năng. Khám phá chứa luồng mở hiện vật và nghe câu chuyện; Tour chứa các tuyến miễn phí và trả phí. Đã lưu giúp tìm lại nội dung; thiết lập Trợ năng có hiệu lực xuyên suốt ứng dụng. Cấu trúc này nối các nhiệm vụ trong HTA ở Mục 2.4 thành các điểm vào cụ thể.

![Sitemap phân cấp sáu khu vực của ứng dụng Dấu Xưa](figures/week5-ia/01-sitemap.png){ width=98% }

Hình 12. Sitemap tổng quan của Dấu Xưa, đối chiếu với cấu trúc bản thử nghiệm.

Thanh điều hướng dưới của màn hình chính dẫn tới Khám phá, Tour, Đã lưu và Cá nhân. Người dùng chọn ngôn ngữ, địa điểm khi khởi động; thiết lập trợ năng được mở từ điểm vào phù hợp. Trong Khám phá, quét QR, nhập mã và chọn từ danh sách đều mở cùng một trình phát. Nhờ vậy, khi camera không dùng được, người dùng vẫn tiếp tục bằng mã hoặc danh sách.

### 2.5.2. Bản phác thảo số low-fi dựa trên HTA

Ba tờ dưới đây là **phác thảo số độ trung thực thấp** dựa trên HTA ở Mục 2.4, được tạo trước buổi thực hành tuần 5. Chúng dùng để xem xét bố cục và điều hướng, chưa thay thế phác thảo giấy hoặc wireframe medium-fi bằng Figma. Số trên màn hình chỉ trình tự chính; nhánh thay thế được ghi ở màn hình liên quan.

![Phác thảo số low-fi cho luồng miễn phí](figures/week5-ia/02-lowfi-mien-phi.png){ width=96% }

Hình 13. Luồng miễn phí: chọn địa điểm, mở hiện vật bằng mã hoặc danh sách, nghe câu chuyện và xem gợi ý tiếp theo (HTA 1–5, 8).

Trong luồng miễn phí, người dùng mở hiện vật từ Khám phá và có thể chuyển sang danh sách ngay tại màn hình quét mã. Trình phát hiển thị mô tả hiện vật, điều khiển nghe và lối xem nguồn trên cùng màn hình.

![Phác thảo số low-fi cho trợ năng và tình huống camera không dùng được](figures/week5-ia/03-lowfi-tro-nang.png){ width=96% }

Hình 14. Các trạng thái trợ năng: thiết lập độc lập, danh sách đơn giản, lối tiếp tục khi camera lỗi và trình phát có mô tả (HTA 2, 5–7).

Bản phác thảo trợ năng làm rõ nhãn chữ, thứ tự đọc và thao tác sau thông báo lỗi. Khi camera không hoạt động, người dùng nhập mã hoặc chọn từ danh sách. Mô tả hiện vật và bản chép lời có thể đọc mà không cần phát âm thanh.

![Phác thảo số low-fi cho luồng Premium Historical Tour](figures/week5-ia/04-lowfi-premium.png){ width=96% }

Hình 15. Luồng trả phí: xem trước giá và nội dung, xác nhận mua, theo dõi tiến trình, dùng phương án thay thế AR và hoàn thành tour (HTA 9).

Luồng trả phí hiển thị giá và phần nghe thử trước khi xác nhận mua. Nếu không dùng được AR tại một điểm, người dùng tiếp tục bằng ảnh tái dựng, âm thanh và bản chép lời. Các phác thảo số mới thể hiện cấu trúc và chữ trên màn hình. Theo slide, vẫn cần phác thảo giấy từ HTA và wireframe số trong Figma; báo cáo chưa có minh chứng cho hai đầu ra này.

## 2.6. Rà soát và điều chỉnh giao diện theo nguyên tắc khả dụng

Các màn hình của bản thử nghiệm được rà theo 10 nguyên tắc khả dụng của Nielsen để tìm vấn đề trong luồng thao tác và phản hồi giao diện. Đây là đánh giá trên bản thiết kế, chưa phải kiểm thử với người dùng. Bảng đối chiếu đầy đủ nằm trong `USABILITY_HEURISTICS_REVIEW.md`; bảng dưới đây chọn các thay đổi liên quan trực tiếp đến ba kịch bản ở Mục 2.2.

| Tình huống | Điều chỉnh trên bản thử nghiệm | Nguyên tắc liên quan |
|---|---|---|
| Minh cần tìm hiện vật khi không quét được mã | Có lối nhập mã và danh sách hiện vật; danh sách đơn giản ẩn ảnh nhưng giữ tên và thời lượng; bộ lọc thông báo số kết quả. | Linh hoạt, nhận biết thay vì ghi nhớ, phục hồi lỗi. |
| Nam dùng bàn phím hoặc trình đọc màn hình | Thêm liên kết đi thẳng đến nội dung, nhãn điều khiển, thứ tự tab bằng phím mũi tên; hộp thoại giữ và khôi phục tiêu điểm. | Nhất quán, quyền kiểm soát, ngăn ngừa lỗi. |
| Người dùng nghe câu chuyện và cần biết trạng thái | Trình phát hiện trạng thái phát, thời gian và tốc độ; có mô tả hiện vật, phần tóm tắt bằng chữ và trạng thái nguồn nội dung. | Hiển thị trạng thái, thông tin dễ nhận biết, trợ giúp tại chỗ. |
| Hương cân nhắc tour trả phí | Giá và phần nghe thử xuất hiện trước bước xác nhận; thao tác mô phỏng mua có trạng thái đang xử lý; AR có lối tiếp tục bằng nội dung thay thế. | Phù hợp với thế giới thực, ngăn ngừa lỗi, tự do lựa chọn. |

![Trình phát câu chuyện và mô tả hiện vật](figures/week4-heuristics/03-trinh-phat-cau-chuyen.png){ width=42% } ![Thông báo mã hiện vật không hợp lệ](figures/week4-heuristics/04-phuc-hoi-loi-ma-hien-vat.png){ width=42% }

Hình 16. Minh chứng từ lần rà soát tuần 4: phản hồi trong trình phát và lối phục hồi khi mã hiện vật không hợp lệ.

Minh có thêm cách mở câu chuyện, Hương thấy giá trước khi mua, còn Nam có lối thao tác không phụ thuộc camera. Những thay đổi này mới được kiểm tra thủ công trên bản thử nghiệm. Cần thử với người dùng đại diện, đặc biệt là người dùng VoiceOver/TalkBack, trước khi kết luận về khả năng sử dụng và tiếp cận trong thực tế.

Bản thử nghiệm 0.5.1 dùng bốn câu chuyện mẫu chung cho các địa điểm. Vị trí, QR, thanh toán, tải ngoại tuyến, AR và rung đều được mô phỏng. Tour trả phí chỉ có một điểm tương tác; màn hình cuối không xác nhận việc hoàn thành cả sáu điểm. Mô tả hiện vật mới có chữ, chưa có bản thu riêng, bản chép lời khớp tệp đọc hay mốc thời gian đã kiểm chứng. Cần xử lý các giới hạn này trước khi đánh giá sản phẩm hoàn chỉnh; yêu cầu thiết kế ở Mục 2.3 vẫn giữ nguyên.

# Tài liệu tham khảo

Apple App Store (2026a), *Smartify: Arts and Culture*. Truy cập ngày 19/09/2026 tại <https://apps.apple.com/gb/app/smartify-arts-and-culture/id1102736524>.

Apple App Store (2026b), *Connects: Arts+Culture*. Truy cập ngày 19/09/2026 tại <https://apps.apple.com/us/app/connects-arts-culture/id1476456847>.

Bloomberg Connects (2026), *Bloomberg Connects*. Truy cập ngày 12/09/2026 tại <https://www.bloombergconnects.org/>.

Nielsen, Jakob (1994, rà soát năm 2024), *10 Usability Heuristics for User Interface Design*. Nielsen Norman Group. Truy cập ngày 03/10/2026 tại <https://www.nngroup.com/articles/ten-usability-heuristics/>.

Smartify (2026), *Smartify: Arts and Culture*. Truy cập ngày 12/09/2026 tại <https://play.google.com/store/apps/details?id=com.mobgen.smartify>.

Vi Chi Thanh (2026a), *Week 2: Introduction to User-Centred Design Methods*. Tài liệu môn học, University of Information Technology và Birmingham City University.

Vi Chi Thanh (2026b), *Week 3: Introduction to Accessibility and Inclusive Design*. Tài liệu môn học, University of Information Technology và Birmingham City University.

W3C Web Accessibility Initiative (2024a), *How People with Disabilities Use the Web*. Truy cập ngày 12/09/2026 tại <https://www.w3.org/WAI/people-use-web/>.

W3C Web Accessibility Initiative (2024b), *Involving Users in Web Projects for Better, Easier Accessibility*. Truy cập ngày 12/09/2026 tại <https://www.w3.org/WAI/planning/involving-users/>.
