# Sản phẩm : Web thương mại điện tử

## Thành viên nhóm:
- **22022597 Trịnh Đắc Phú - Nhóm trưởng**
- 22022517 Bùi Tiến Sâm
- 22022521 Nguyễn Văn Mạnh
- 22022654 Triệu Vũ Hoàn

## Công cụ sử dụng Django

## Link
- Video demo: [Phần 1](https://drive.google.com/file/d/1HDooPjt8iCo6ZdVC9eA3jIbN_5o3R6fV/view?usp=sharing) [Phần 2](https://drive.google.com/file/d/1hJeo3sig7DEvD2bspNlO4P2POcBdXMlg/view?usp=sharing) [Phần 3](https://drive.google.com/file/d/17NL22CTj1X04YfedATqcF2Vr0PCI_E9i/view?usp=sharing)
- Báo cáo: [báo cáo](https://drive.google.com/file/d/1uF8iMtrrwVpRUBa8nELy43tSiHoDsaRZ/view?usp=sharing)

## Persona
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chị Nguyễn Phương Lan, 28 tuổi, là giáo viên dạy toán của một trường THCS tại địa bàn huyện Ninh Giang, Hải Dương. Chị đã có chồng và hai con nhỏ học tiểu học. Cả nhà hiện đang sinh sống tại xã Hưng Long, huyện Ninh Giang, tỉnh Hải Dương.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chị Lan tốt nghiệp bằng giỏi của trường Đại học Sư phạm Hà Nội, khoa Vật lý kỹ thuật năm 22 tuổi. Sau quá trình thực tập, chị được phân công công tác tại quê và trở thành giáo viên chính thức của trường.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chị Lan là người có tâm huyết với nghề, luôn mong muốn các em học sinh có được tiết học bổ ích thay vì chỉ học lý thuyết khô khan. Chị đã đề xuất với nhà trường về việc bổ sung trang thiết bị cho phòng thực hành vật lý, và được nhà trường bàn giao cho công việc đó cùng kinh phí thực hiện.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tuy nhiên, vì lịch dạy dày đặc cùng với việc có con nhỏ, chị Lan không có đủ thời gian để đi “rong ruổi” tìm kiếm những nơi có bán trang thiết bị thực hành vật lý. Vậy nên, chị đã sử dụng The Middles, trang web thương mại điện tử nổi tiếng, để thực hiện mục tiêu, nhờ vậy mà tiết kiệm được thời gian.

## Scenarios
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chị Lan, sau khi lập ra danh sách những vật cần mua, đã sử dụng The Middles để thực hiện công việc. Nhưng, khi mua về, chị nhận ra mình đã bỏ sót những vật nhỏ nhặt liên quan, như là quả cầu sắt nhưng không có móc treo, hay lực kế mà không có quả cân,... Sau đó chị Lan đã lại lần nữa tìm và mua hàng.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sau lần quên đồ vừa rồi, chị đã phải suy nghĩ kỹ lưỡng hơn, đồng thời chị nghĩ rằng nếu web có thể có chức năng gợi ý những thứ liên quan đến những thứ chị đã xem thì có lẽ chị sẽ đỡ tốn công hơn nhiều.

## Mục tiêu chính
- Thiết kế, phát triển và kiểm tra một ứng dụng web thương mại điện tử đầy đủ tính năng để xem, mua, đánh giá và đánh giá các sản phẩm khác nhau.
- Xây dựng hệ thống gợi ý để đề xuất các sản phẩm khác nhau phục vụ cho từng người dùng.
- Triển khai mô hình MVT (Model, View, Template) cho nền tảng ứng dụng web.

## Ứng dụng Web
Hệ thống này được thiết kế với giao diện web có thể mở rộng và bao gồm nhiều tính năng như:
- Đăng ký và xác thực tài khoản người dùng.
- Tìm kiếm và duyệt sản phẩm.
- Xem chi tiết sản phẩm.
- Quản lý danh mục và danh mục phụ.
- Thanh tìm kiếm.
- Đánh giá và xếp hạng sản phẩm bởi người dùng.
- Mua hàng và thanh toán.
- Đề xuất sản phẩm theo sở thích của người dùng.
- Trang hồ sơ lưu thông tin, ảnh đại diện người dùng.

## Yêu cầu
### Yêu cầu chức năng
#### Giao diện/ Trải nghiệm người dùng (UI/UX):
- Trang web có thiết kế hấp dẫn, dễ điều hướng và tải trang nhanh chóng, sử dụng màu sắc, phông chữ và hình ảnh phù hợp sẽ thu hút người dùng.
- Với phần lớn người dùng truy cập từ thiết bị di động, trang web phải thân thiện với di động và tương thích với nhiều kích thước màn hình khác nhau.
- Hệ thống cần có tính năng tìm kiếm và lọc sản phẩm theo các danh mục để giúp người dùng dễ dàng tìm thấy sản phẩm mong muốn.
- Ngoài ra, chức năng đánh giá và nhận xét sản phẩm giúp người bán hiểu rõ hơn về nhu cầu và mong đợi của khách hàng.
- Trang web cũng phải cung cấp tính năng giỏ hàng và thanh toán cho người dùng đã đăng nhập, tạo điều kiện thuận lợi cho quá trình mua sắm.
#### Hệ thống đề xuất cá nhân:
Hệ thống cần có tính năng đề xuất sản phẩm động và cá nhân hóa dựa trên sở thích, lịch sử hoạt động và đánh giá của từng người dùng. Các sản phẩm mà người dùng đã đánh giá trước đó sẽ không xuất hiện trong các đề xuất mới, giúp tối ưu hóa trải nghiệm mua sắm.
#### Quản lý thông tin:
Chỉ có quản trị viên (admin) mới có quyền truy cập và đăng nhập vào bảng điều khiển quản trị của hệ thống. Quản trị viên sẽ chịu trách nhiệm tải lên và quản lý sản phẩm, đơn hàng, đảm bảo thông tin luôn được cập nhật và chính xác.
### Yêu cầu phi chức năng:
#### Tốc độ:
Tốc độ tải trang có thể bị ảnh hưởng bởi nhiều yếu tố như ảnh có độ phân giải cao chưa được tối ưu hóa, quy trình đặt hàng phức tạp, hoặc code chưa được tối ưu tốt. Cần khắc phục các vấn đề này để đảm bảo tốc độ tải trang nhanh và mượt mà.
#### Bảo mật và riêng tư:
- Hệ thống phải được bảo vệ khỏi các lỗ hổng bảo mật để đảm bảo dữ liệu nhạy cảm của người dùng không bị rò rỉ.
- Xác thực người dùng phải được bảo vệ nghiêm ngặt và mã hóa phức tạp để ngăn chặn các cuộc tấn công.
- Quyền riêng tư của người dùng cần được tôn trọng, và các chính sách, điều khoản và điều kiện phải có thể được cập nhật từ phía quản trị viên.
#### Khả năng mở rộng:
- Hệ thống cần có khả năng mở rộng để hỗ trợ số lượng lớn người dùng và sản phẩm thuộc nhiều danh mục khác nhau.
- Các thao tác điều chỉnh về sản phẩm, danh mục, đơn hàng, và các yếu tố khác phải được thực hiện dễ dàng qua bảng điều khiển của quản trị viên.
### Yêu cầu về tính sử dụng:
#### Dễ sử dụng:
Hệ thống phải dễ sử dụng và thân thiện với người dùng. Chức năng và điều hướng phải đơn giản và rõ ràng.
#### Hài lòng và dễ nhớ:
Thiết kế của hệ thống phải dễ nhìn và dễ nhớ, tạo cảm giác hài lòng cho người dùng.
#### Đồ họa:
Đồ họa chất lượng cao sẽ nâng cao trải nghiệm người dùng. Code phải được tối ưu hóa để đảm bảo chất lượng hiển thị ổn định trên mọi thiết bị phần cứng.

## Cách sử dụng
1. Tải repo trên về máy.
2. Thực hiện `pip install -r requirements.txt`.
3. Chuyển vị trí đến thư mục `webdjango/` chứa file `manage.py`.
4. Chạy lệnh `python manage.py runserver`.
5. Truy cập vào đường link [http://127.0.0.1:8000/shop/index/](http://127.0.0.1:8000/shop/index/) để trải nghiệm.
