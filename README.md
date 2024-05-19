# Sản phẩm : Web thương mại điện tử

## Thành viên nhóm:
**- 22022597 Trịnh Đắc Phú - Nhóm trưởng**
- 22022517 Bùi Tiến Sâm
- 22022521 Nguyễn Văn Mạnh
- 22022654 Triệu Vũ Hoàn

## Công cụ sử dụng Django

## Link
- Video demo: [video](https://drive.google.com/file/d/10ZV4tXUm88zy8SAAzgruWQo2whQbslzL/view?usp=sharing)
- Báo cáo: [báo cáo](https://drive.google.com/file/d/1oRyHPW_hGnAgQ1IaFqH2DBp2Pbvus4_6/view?usp=sharing)

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
Tất cả các nội dung người dùng thấy đều được lấy từ cơ sở dữ liệu, và chỉ có quản trị viên mới có quyền tải lên nội dung. Trang web cũng cung cấp hệ thống đánh giá, cho phép người dùng đưa ra ý kiến và xếp hạng sản phẩm từ 1 đến 5. Quản trị viên có thể thêm sản phẩm mới để hiển thị cho người dùng khác. Hệ thống được thiết kế thân thiện với thiết bị di động và tối ưu hóa cho công cụ tìm kiếm để đảm bảo hiệu suất tốt hơn.

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
