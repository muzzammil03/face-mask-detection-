import streamlit as st
import numpy as np
import cv2
import requests
from tensorflow.keras.models import load_model

# load model
model = load_model("mask_detector.keras")

st.set_page_config(page_title="Mask Detection", layout="centered")

st.title("😷 Face Mask Detection App")

# ---------------- FUNCTIONS ----------------

def preprocess(img):
    img = cv2.resize(img, (128,128))
    img = img / 255.0
    img = np.reshape(img, (1,128,128,3))
    return img

def predict(img):
    img = preprocess(img)
    pred = model.predict(img)
    return "😷 With Mask" if pred <= 0.5 else "❌ Without Mask"

# ---------------- SESSION STATE ----------------

if "image" not in st.session_state:
    st.session_state.image = None

def reset():
    st.session_state.image = None

# ---------------- UI ----------------

st.button("🔄 Reset", on_click=reset)

uploaded_file = st.file_uploader("📂 Upload Image", type=["jpg", "png", "jpeg"])
url = st.text_input("🌐 Or paste image URL")

img = None

# Upload image
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

# URL image
elif url:
    try:
        response = requests.get(url)
        file_bytes = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
    except:
        st.error("Invalid URL")

# Show image
if img is not None:
    st.session_state.image = img
    st.image(img, channels="BGR", caption="Selected Image")

# 🔥 EXECUTE BUTTON
if st.button("🚀 Run Prediction"):
    if st.session_state.image is not None:
        result = predict(st.session_state.image)
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please upload or provide an image first!")