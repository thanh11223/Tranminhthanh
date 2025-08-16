# Iris Web App (Flask + scikit-learn, nhập 0–4 tham số → xuất loài hoa)

Ứng dụng web đơn giản dự đoán loài Iris (Setosa/Versicolor/Virginica).
Frontend: HTML/JS. Backend: Flask (Python) + scikit-learn (KNN). Hỗ trợ **thiếu tham số** (0–4) nhờ `SimpleImputer` (điền trung bình).

## Cách chạy (Windows/macOS/Linux)
```bash
# 1) Tạo môi trường ảo (khuyến nghị)
python -m venv .venv
# Kích hoạt:
#   Windows: .venv\Scripts\activate
#   macOS/Linux: source .venv/bin/activate

# 2) Cài thư viện
pip install -r requirements.txt

# 3) (Tuỳ chọn) Huấn luyện lại mô hình
python train_model.py

# 4) Chạy backend Flask
python app.py
```
Mặc định ứng dụng lắng nghe tại `http://127.0.0.1:5000`.

## API
- `POST /predict` — body JSON:
```json
{
  "sepal_len": 5.1,
  "sepal_wid": 3.5,
  "petal_len": 1.4,
  "petal_wid": 0.2
}
```
Các trường có thể để `null` hoặc bỏ hẳn.

Phản hồi:
```json
{
  "species": "Iris setosa",
  "probabilities": {
    "Iris setosa": 0.98,
    "Iris versicolor": 0.02,
    "Iris virginica": 0.00
  }
}
```

## Ghi chú
- Mô hình: `KNeighborsClassifier(n_neighbors=3)` nằm trong pipeline cùng `SimpleImputer(strategy='mean')`.
- Nếu muốn đổi `k`, chỉnh trong `train_model.py`, chạy lại script để sinh `model.pkl` mới.
