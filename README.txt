# 🔍 YOLO12 Detection App

Aplikasi web interaktif berbasis [Streamlit](https://streamlit.io) untuk **deteksi objek** menggunakan model YOLOv8 Nano.  

Upload gambar untuk mengenali objek seperti **orang**, **mobil**, **botol**, **laptop**, dll. Cocok untuk belajar computer vision secara praktis!

---

## 🚀 Fitur Utama
✅ Upload gambar (JPG/PNG) dari perangkat  
✅ Deteksi objek dengan kotak pembatas (*bounding box*)  
✅ Menampilkan label objek terdeteksi beserta skor kepercayaan  
✅ Ringan & cepat dengan YOLOv8 Nano  
✅ Antarmuka web Streamlit yang sederhana & mudah digunakan

---

## 🗂️ Struktur Proyek

yolo12-detection-app/
├── app.py
├── requirements.txt
├── yolov8n.pt
├── sample_images/
│ └── image1.jpg
└── screenshots/
├── Screenshot_Install_Packages.png
├── Screenshot_Run_App.png
├── Screenshot_Hasil_Laptop.png
├── Screenshot_Hasil_Person_Car.png
└── Screenshot_Hasil_Jalan.png

---

## ⚙️ Cara Instalasi

1️⃣ Clone repository (atau unduh ZIP):  
```bash
git clone https://github.com/username/yolo12-detection-app.git
cd yolo12-detection-app
2️⃣ Install dependensi:
```
pip install -r requirements.txt
```
✅ Atau manual:
```
pip install streamlit ultralytics opencv-python pillow
```
▶️ Cara Menjalankan
```
streamlit run app.py
```
✅ App akan berjalan di:

Local URL: http://localhost:8501

Buka di browser → Upload gambar → Lihat hasil deteksi.

📸 Contoh Proses dan Hasil Deteksi

1️⃣ Proses Instalasi
Perintah:
```
pip install streamlit ultralytics opencv-python pillow
```
Penjelasan:
Mengunduh & memasang semua library yang dibutuhkan untuk menjalankan app.

📷 Contoh Terminal:

2️⃣ Menjalankan Aplikasi
Perintah:
```
streamlit run app.py
```
Penjelasan:

Streamlit akan memberi URL lokal dan network.

App siap diakses via browser.

📷 Contoh Terminal:

3️⃣ Hasil Deteksi Objek
Aplikasi menampilkan gambar dengan bounding box, label objek, dan confidence score.

✅ Upload gambar → Model YOLOv8 mendeteksi objek → Tampilkan hasil di browser.

💻 Contoh Hasil 1: Deteksi Laptop
Label: laptop dengan confidence 0.86

Bounding box jelas menyoroti objek utama
📷 Tampilan di browser:

🚗👤 Contoh Hasil 2: Deteksi Orang dan Mobil
Label terdeteksi: person, car

Cocok untuk foto aktivitas luar ruangan
📷 Tampilan di browser:

🛣️ Contoh Hasil 3: Deteksi di Jalan Raya
Multiple objek terdeteksi: car, bus, person

Menunjukkan kemampuan model mendeteksi banyak objek sekaligus di lingkungan kompleks
📷 Tampilan di browser:

🧩 Cuplikan Kode Utama (app.py)
```python

import streamlit as st
from ultralytics import YOLO
import tempfile
import os

# Load model YOLOv8 Nano
model = YOLO("yolov8n.pt")

st.title("🔍 YOLOv12 (YOLOv8) Object Detection WebApp")
uploaded_file = st.file_uploader("📤 Upload Gambar", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        image_path = temp_file.name

    results = model(image_path)

    for result in results:
        res_img = result.plot()
        st.image(res_img, caption="📸 Hasil Deteksi", use_column_width=True)

        detected_classes = set([model.names[int(cls)] for cls in result.boxes.cls])
        st.success(f"✅ Objek terdeteksi: {', '.join(detected_classes)}")

    os.remove(image_path)
```
📦 Requirements
Isi file requirements.txt:
```
ultralytics
streamlit
opencv-python
pillow
```
✅ Instal semua sekaligus:
```
pip install -r requirements.txt
```
---

## ✅ Penutup

Aplikasi **YOLO12 Detection App** ini dibuat sebagai contoh penerapan **YOLOv8** dalam aplikasi web berbasis **Streamlit**.  
Dengan antarmuka yang sederhana dan intuitif, siapa pun dapat dengan mudah mencoba mendeteksi objek pada gambar hanya dengan beberapa klik.

Proyek ini cocok untuk:
- Mahasiswa atau pelajar yang ingin belajar **Computer Vision**
- Pengembang yang ingin membuat prototipe aplikasi deteksi objek
- Siapa saja yang tertarik dengan **AI / Machine Learning** berbasis gambar

Silakan gunakan, pelajari, dan kembangkan aplikasi ini sesuai kebutuhan.  
Semoga proyek ini bermanfaat dan bisa menjadi inspirasi untuk membuat aplikasi yang lebih kompleks dan berguna di masa depan!

---

## 🙏 Ucapan Terima Kasih

Terima kasih telah menggunakan atau membaca dokumentasi **YOLOv8 Detection App** ini.  
Jika ada saran, pertanyaan, atau kontribusi, jangan ragu untuk menghubungi atau membuat *issue* di repositori.

✨ Selamat mencoba, semoga sukses, dan semoga hari Anda menyenangkan!

---
