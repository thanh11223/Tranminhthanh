Mô tả đề tài: Ứng dụng web dự đoán loài hoa Iris

1. Mục tiêu
Xây dựng một ứng dụng web đơn giản cho phép người dùng nhập từ 0 đến 4 tham số (chiều dài/rộng đài hoa, chiều dài/rộng cánh hoa) và hệ thống sẽ dự đoán loài hoa Iris (Setosa, Versicolor, hoặc Virginica).

2. Công nghệ sử dụng

Frontend: HTML + CSS + JavaScript

Giao diện nhập liệu với các ô số.

Nút “Dự đoán” gửi dữ liệu dạng JSON đến backend qua API.

Hiển thị kết quả loài hoa và xác suất dự đoán bằng progress bar.

Backend: Python Flask

Cung cấp API /predict nhận dữ liệu từ người dùng.

Trả về kết quả dự đoán (tên loài + xác suất từng lớp).

Machine Learning: scikit-learn

Mô hình K-Nearest Neighbors (k=3) huấn luyện trên tập dữ liệu Iris (Fisher, 1936).

Kết hợp với SimpleImputer(strategy='mean') để xử lý trường hợp người dùng không nhập đủ tham số.

Mô hình đã huấn luyện được lưu trong file model.pkl.

3. Cấu trúc hệ thống

iris_app/
 ├── app.py            # Flask backend, API và xử lý request
 ├── train_model.py    # Script huấn luyện KNN và lưu model.pkl
 ├── model.pkl         # Mô hình ML đã huấn luyện
 ├── templates/
 │    └── index.html   # Giao diện web chính
 ├── static/
 │    └── style.css    # CSS mở rộng (tùy chọn)
 ├── requirements.txt  # Danh sách thư viện cần cài
 └── README.md         # Tài liệu hướng dẫn


4. Cách sử dụng

Cài môi trường Python và thư viện:

pip install -r requirements.txt


(Tùy chọn) Huấn luyện lại mô hình:

python train_model.py


Chạy ứng dụng Flask:

python app.py


Mở trình duyệt tại http://127.0.0.1:5000 để sử dụng.

5. Điểm nổi bật

Cho phép nhập thiếu thông tin (0–4 tham số).

Giao diện trực quan, có sẵn ví dụ cho từng loài hoa.

API có thể dùng độc lập để tích hợp vào hệ thống khác.

Kết quả dự đoán kèm theo xác suất cho từng loài.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ea5fbcc8-80b2-4bde-815c-94800cf9fda8" />
