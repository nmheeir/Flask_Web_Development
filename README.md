# Flasky

---

## Các tính năng chính

- Đăng ký, đăng nhập, xác thực email, đổi mật khẩu, đổi email
- Quản lý hồ sơ cá nhân, avatar (Gravatar)
- Đăng bài viết, chỉnh sửa, xóa bài viết
- Bình luận, chỉnh sửa bình luận
- Theo dõi người dùng, xem feed bài viết của người theo dõi
- Phân quyền: User, Moderator, Administrator
- Quản trị user: tìm kiếm, lọc theo role, phân trang, chỉnh sửa, xóa user
- Log hoạt động đăng nhập/đăng xuất của người dùng
- API RESTful cho bài viết, user, comment (chuẩn hóa JSON)
- Giao diện responsive với Flask-Bootstrap
- Hỗ trợ gửi email (xác thực, thông báo lỗi)
- Tạo dữ liệu mẫu bằng Faker
- Đầy đủ migration với Flask-Migrate
- Unit test cho model, API, client

---

## Cài đặt (Local Development Setup)

### 1. Clone repository & tạo môi trường ảo

```bash
git clone <repo-url>
cd Flask_Web_Development
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
```

### 2. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 3. Thiết lập biến môi trường (tùy chọn)

Tạo file `.env` hoặc export biến môi trường:
```bash
export FLASK_APP=flasky.py
export FLASK_CONFIG=development
export SECRET_KEY=your_secret_key
export MAIL_USERNAME=your_email@gmail.com
export MAIL_PASSWORD=your_app_password
export FLASKY_ADMIN=your_email@gmail.com
```

### 4. Khởi tạo database & migrate

```bash
flask db upgrade
```

### 5. Tạo dữ liệu mẫu (tùy chọn)

```bash
flask forge
```

### 6. Chạy ứng dụng

```bash
flask run
```
Truy cập: http://localhost:5000

---

## Sơ đồ thư mục

```
Heir_Flask_Web_Development/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── email.py
│   ├── fake.py
│   ├── exceptions.py
│   ├── decorators.py
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── manage.html
│   │   ├── user_logs.html
│   │   ├── ... (các template khác)
│   ├── main/
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── errors.py
│   ├── api/
│   │   ├── posts.py
│   │   ├── users.py
│   │   ├── comments.py
│   │   ├── authentication.py
│   │   ├── ... (các file API khác)
│   ├── auth/
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── __init__.py
│
├── migrations/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   ├── alembic.ini
│
├── tests/
│   ├── test_api.py
│   ├── test_client.py
│   ├── test_user_model.py
│   ├── test_basics.py
│
├── flasky.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Một số lệnh CLI hữu ích

- **Chạy test:**  
  `flask test`
- **Sinh dữ liệu mẫu:**  
  `flask forge`
- **Chạy profiler:**  
  `flask profile`
