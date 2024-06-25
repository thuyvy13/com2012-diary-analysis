
---

# Xử lý và Phân Tích Dữ Liệu từ Tệp Excel với Python và Tkinter

Dự án này cung cấp các công cụ để xử lý và phân tích dữ liệu từ tệp Excel, phục vụ cho các yêu cầu cụ thể như suy luận thông tin ca học, chuẩn hóa dữ liệu giảng viên, suy luận thông tin nội dung/chủ đề buổi học, và thống kê số phản hồi theo từng lớp, giảng viên, ngày.

## Các Yêu Cầu Chức Năng

### Y1.1 - Suy luận thông tin ca học từ giờ ghi nhật ký và thời điểm trong ca

- **Mô tả:** Sử dụng thời gian ghi nhật ký để suy luận thông tin về ca học của sinh viên.
- **Chức năng:** Đọc tệp Excel chứa thông tin thời gian và áp dụng hàm suy luận để xác định ca học của từng bản ghi.
- **Giao diện người dùng (UI):** Cho phép người dùng chọn tệp Excel và hiển thị kết quả trong một cửa sổ mới.

### Y1.2 - Chuẩn hóa dữ liệu giảng viên và dữ liệu giảng viên chính xác

- **Mô tả:** Chuẩn hóa dữ liệu về mã giảng viên và hiển thị thông tin chính xác của giảng viên.
- **Chức năng:** Đọc dữ liệu từ tệp Excel, ánh xạ mã giảng viên với tên giảng viên từ một bảng dữ liệu khác.
- **Giao diện người dùng (UI):** Cho phép người dùng chọn tệp Excel và hiển thị kết quả sau khi chuẩn hóa.

### Y1.3 - Suy luận thông tin nội dung/chủ đề buổi học

- **Mô tả:** Dựa trên mô tả bài học, suy luận thông tin về chủ đề của buổi học.
- **Chức năng:** Áp dụng các từ khóa để suy luận chủ đề bài học từ mô tả.
- **Giao diện người dùng (UI):** Cho phép người dùng chọn tệp Excel và hiển thị thông tin chủ đề buổi học.

### Y2.1 - Thống kê số phản hồi theo từng lớp và theo từng giảng viên

- **Mô tả:** Thống kê và trực quan hóa số lượng phản hồi theo lớp học và giảng viên.
- **Chức năng:** Đọc dữ liệu từ tệp Excel và biểu đồ hóa số lượng phản hồi theo lớp và theo giảng viên.
- **Giao diện người dùng (UI):** Cho phép người dùng chọn tệp Excel và hiển thị biểu đồ.

### Y2.2 - Thống kê số phản hồi theo từng ngày của từng lớp

- **Mô tả:** Thống kê và trực quan hóa số lượng phản hồi theo ngày cho từng lớp học.
- **Chức năng:** Đọc dữ liệu từ tệp Excel và biểu đồ hóa số lượng phản hồi theo ngày cho từng lớp.
- **Giao diện người dùng (UI):** Cho phép người dùng chọn tệp Excel và hiển thị biểu đồ.

## Hướng Dẫn Sử Dụng

1. **Cài Đặt Môi Trường:**
   - Cài đặt Python và các thư viện cần thiết: `pandas`, `matplotlib`, `seaborn`, `tkinter`, `tabulate`.

2. **Khởi Chạy Ứng Dụng:**
   - Mở terminal và di chuyển vào thư mục dự án.
   - Chạy mỗi mã nguồn Python tương ứng với từng yêu cầu (vd: Y1.1, Y1.2, ...) để mở giao diện người dùng.
   - Chọn tệp Excel chứa dữ liệu cần xử lý.

3. **Xem Kết Quả:**
   - Kết quả sẽ được hiển thị trên giao diện người dùng với bảng dữ liệu và/hoặc biểu đồ thống kê.


