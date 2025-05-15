# Chatbot Tư Vấn Sách

## Giới thiệu

Chatbot Tư Vấn Sách là một ứng dụng web đơn giản, giúp khách hàng tìm kiếm và nhận gợi ý các quyển sách phù hợp dựa trên nhu cầu của họ. Ứng dụng sử dụng mô hình embedding `mxbai-embed-large` từ Ollama để tìm kiếm sách dựa trên ngữ nghĩa và kết nối với cơ sở dữ liệu MariaDB để truy xuất thông tin sách.

### Tính năng chính

- **Tìm kiếm ngữ nghĩa**: Người dùng nhập truy vấn (ví dụ: "sách khoa học viễn tưởng") và chatbot trả về danh sách sách phù hợp.
- **Giao diện thân thiện**: Giao diện web đơn giản, dễ sử dụng.
- **Tích hợp database**: Kết nối với cơ sở dữ liệu MariaDB để lấy thông tin sách từ các bảng `books`, `categories`, và `publishers`.

## Yêu cầu hệ thống

- **Python**: 3.10 trở lên
- **MariaDB**: Phiên bản 10.5 trở lên
- **Ollama**: Đã cài đặt và pull mô hình `mxbai-embed-large`
- **Hệ điều hành**: Windows, macOS, hoặc Linux
- **Trình duyệt web**: Chrome, Firefox, hoặc bất kỳ trình duyệt hiện đại nào

## Cách khởi động và sử dụng Bookstore Chatbot

### Bước 1: Cài đặt Ollama

1. Tải và cài đặt Ollama từ [trang chính thức](https://ollama.com/).
2. Pull mô hình `mxbai-embed-large`:
   ```bash
   ollama pull mxbai-embed-large
   ```

### Bước 2: Cài đặt môi trường Python

1. Clone hoặc giải nén dự án vào một thư mục (ví dụ: `bookstore_chatbot`).
2. Tạo môi trường ảo:
   ```bash
   python -m venv venv
   venv\Scripts\activate         # Windows
   # hoặc
   source venv/bin/activate      # macOS/Linux
   ```
3. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```

### Cấu trúc thư mục

```
bookstore_chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── embedding.py
│   ├── models.py
│   └── routes.py
├── static/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── requirements.txt
└── README.md
```

## Chạy ứng dụng

1. **Khởi động Ollama**:

   ```bash
   ollama serve
   ```
2. **Chạy server FastAPI**:

   ```bash
   cd bookstore_chatbot
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
3. **Truy cập giao diện**:
   Mở trình duyệt và truy cập:

   ```
   http://localhost:8000/static/index.html
   ```

## Sử dụng chatbot

1. Truy cập giao diện web tại `http://localhost:8000/static/index.html`.
2. Nhập truy vấn vào ô nhập liệu, ví dụ:
   - "Sách khoa học viễn tưởng"
   - "Sách về thám tử"
   - "Sách dành cho trẻ em"
3. Nhấn nút "Gửi" hoặc phím Enter để nhận gợi ý sách.
4. Chatbot sẽ hiển thị danh sách sách phù hợp, bao gồm:
   - Tiêu đề
   - Tác giả
   - Giá
   - Danh mục
   - Mô tả

## Cách hoạt động

1. **Truy xuất dữ liệu**: Backend lấy thông tin sách từ cơ sở dữ liệu `satancra_bookService` (bảng `books`, `categories`, `publishers`).
2. **Tạo embedding**: Mô hình `mxbai-embed-large` chuyển truy vấn người dùng và mô tả sách thành vector embedding.
3. **Tìm kiếm ngữ nghĩa**: Sử dụng cosine similarity để so sánh embedding và tìm sách phù hợp nhất.
4. **Hiển thị kết quả**: Frontend hiển thị danh sách sách gợi ý trong giao diện chatbot.

## Khắc phục sự cố

- **Lỗi kết nối database**:
  - Kiểm tra username, password, và tên database trong `app/database.py`.
  - Đảm bảo MariaDB đang chạy.
- **Ollama không phản hồi**:
  - Chạy lệnh `ollama serve` trước khi khởi động ứng dụng.
  - Kiểm tra mô hình `mxbai-embed-large` đã được pull bằng lệnh `ollama list`.
- **API trả về lỗi**:
  - Kiểm tra log server FastAPI bằng cách chạy `uvicorn` với tùy chọn `--log-level debug`.
- **Giao diện không tải**:
  - Đảm bảo truy cập đúng URL: `http://localhost:8000/static/index.html`.
  - Kiểm tra file `static/index.html` tồn tại.

## Giới hạn

- Chỉ hỗ trợ tìm kiếm dựa trên mô tả sách.
- Không có xác thực người dùng hoặc tính năng cá nhân hóa.
- Giao diện đơn giản, chưa hỗ trợ hình ảnh sách hoặc các tính năng nâng cao như giỏ hàng.

## Giấy phép

Dự án được phát hành dưới [MIT License](LICENSE).

---
