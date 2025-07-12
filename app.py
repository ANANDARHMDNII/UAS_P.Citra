import streamlit as st
from ultralytics import YOLO
import tempfile
import os
from PIL import Image
import numpy as np

# Load model YOLOv8 pre-trained (COCO dataset)
model = YOLO("yolov8n.pt")

st.set_page_config(page_title="YOLOv12 Object Detection", layout="centered")
st.title("🔍 YOLOv12 (YOLOv8) Object Detection WebApp")
st.markdown("Upload gambar untuk mendeteksi objek seperti **botol**, **orang**, **laptop**, dll.")

uploaded_file = st.file_uploader("📤 Upload Gambar", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Simpan gambar yang diupload ke file sementara
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        image_path = temp_file.name

    try:
        # Jalankan deteksi
        results = model(image_path)

        # Tampilkan hasil deteksi
        for result in results:
            res_img = result.plot()  # numpy array
            st.image(res_img, caption="📸 Hasil Deteksi", use_column_width=True)

            # Tampilkan label objek yang terdeteksi
            detected_classes = set([model.names[int(cls)] for cls in result.boxes.cls])
            st.success(f"✅ Objek terdeteksi: {', '.join(detected_classes)}")

    except Exception as e:
        st.error(f"Terjadi error saat memproses gambar: {e}")

    # Hapus file sementara
    os.remove(image_path)
