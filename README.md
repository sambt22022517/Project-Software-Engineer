# Sản phẩm : Web thương mại điện tử The Middles

### Thành viên nhóm:
- 22022517 Bùi Tiến Sâm
- 22022521 Nguyễn Văn Mạnh
- 22022597 Trịnh Đắc Phú
- 22022654 Triệu Vũ Hoàn

### Công cụ sử dụng Django

### Trước khi làm việc
- Tải những thư viện cần thiết bằng `pip install -r requirements.txt`
- Học thêm về Django nếu chưa biết cách sử dụng [tại đây](https://www.w3schools.com/django/index.php).

## Cấu trúc sắp xếp file
```
The_Middle\
|---all_static_files\
|---global_static_files\
|---The_Middle\
    |---__init__.py
    |---asgi.py
    |---setting.py
    |---urls.py
    |---wsgi.py
|---manage.py
```

## Cách chạy thử
**Lưu ý rằng phải thực hiện công việc trong phần Trước khi làm việc.**
- Mở cmd tại folder chứa file `manage.py`.
- Copy `python manage.py runserver` vào cmd và Enter.
  Kết quả sẽ kiểu như này:
```
Performing system checks...

System check identified no issues (0 silenced).
April 06, 2024 - 14:13:07
Django version 5.0.3, using settings 'The_Middles.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Cách chạy thử demo Trang chủ và Danh mục sản phẩm
  + Nhập đường link http://127.0.0.1:8000/ để trải nghiệm chức năng trang chủ.
  + Nhập đường link http://127.0.0.1:8000/danh-muc-san-pham/tat-ca để trải nghiệm chức năng danh mục sản phẩm với tất cả danh mục.
  + Nhập đường link http://127.0.0.1:8000/danh-muc-san-pham/name để trải nghiệm chức năng danh mục sản phẩm với danh mục name.
    Trong đó, name = {dien-tu, sach, mon-an, ve-phim, meo, quan-ao}
  + Sử dụng các đường link trực tiếp trên trang web để chuyển từ trang này sang trang khác cũng được.

## Cách chạy thử demo sign-up-in
  + Nhập đường link http://127.0.0.1:8000/login để trải nghiệm chức năng đăng nhập.
  + Nhập đường link http://127.0.0.1:8000/register để trải nghiệm chức năng đăng ký.
  + Sử dụng các đường link trực tiếp trên trang web để chuyển từ trang này sang trang khác cũng được.
