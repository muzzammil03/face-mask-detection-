# 😷 Face Mask Detection using CNN

A deep learning project that detects whether a person is **wearing a face mask or not** from an image. A Convolutional Neural Network (CNN) built from scratch with TensorFlow/Keras does the classification, and a **Streamlit** web app lets you test it by uploading an image or pasting an image URL.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-5C3EE8?logo=opencv&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)

---

## 📌 Problem Statement

Wearing a face mask is an important safety measure in public places. Checking this manually is slow and unreliable, so this project builds an automatic image classifier with two classes:

- ✅ **With Mask**
- ❌ **Without Mask**

---

## ✨ Features

- 🧠 CNN classifier built from scratch with multiple convolutional blocks
- 📉 Overfitting control using hyperparameter tuning and callbacks
- 📊 Training, validation and test performance comparison
- 🖼️ Predict from an **uploaded image** (jpg, png, jpeg)
- 🌐 Predict from an **image URL**
- 🔄 Reset button to clear the selected image
- 🚀 Simple and clean Streamlit interface

---

## 🗂️ Dataset

The dataset is split into three folders, each with two sub-folders:

```
dataset/
├── train/
│   ├── with_mask/
│   └── without_mask/
├── validation/
│   ├── with_mask/
│   └── without_mask/
└── test/
    ├── with_mask/
    └── without_mask/
```

---

## 🔬 Project Workflow

1. **Data loading and EDA**
   - Plot sample images with and without a mask
   - Prepare labels from the loaded data
2. **Model building and training**
   - CNN classifier from scratch with multiple CNN blocks
   - Hyperparameter tuning to improve performance and reduce overfitting
   - Callbacks used during training
   - Plot training and validation metrics
3. **Evaluation and testing**
   - Compare training, validation and test scores
   - Save and reload the trained model
   - Build a prediction function and test it on random images

The complete workflow is in [`CNN.ipynb`](CNN.ipynb) and [`main.ipynb`](main.ipynb).

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Deep learning | TensorFlow / Keras |
| Image processing | OpenCV |
| Numerical computing | NumPy |
| Web app | Streamlit |
| Notebook | Jupyter |

---

## 📁 Project Structure

```
face-mask-detection-/
├── CNN.ipynb           # CNN model building, training and evaluation
├── main.ipynb          # Notebook for model testing
├── main.py             # Streamlit web app
├── instructions.txt    # Problem statement and task details
└── README.md
```

> The trained model `mask_detector.keras` is not stored in this repository because of GitHub's file size limit. See the download link below.

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/muzzammil03/face-mask-detection-.git
cd face-mask-detection-
```

**2. Install dependencies**

```bash
pip install streamlit tensorflow opencv-python numpy requests
```

**3. Download the trained model**

Download `mask_detector.keras` from the Google Drive link below and place it in the **project root folder** (next to `main.py`):

👉 [Download model from Google Drive](https://drive.google.com/drive/folders/1HJXK4yZZI3XT_z1FeEhPLihPLsHx1qBo?usp=drive_link)

---

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

The app opens at `http://localhost:8501`.

1. Upload an image **or** paste an image URL
2. Click **🚀 Run Prediction**
3. The result shows **😷 With Mask** or **❌ Without Mask**
4. Use **🔄 Reset** to clear and try another image

---

## 🧠 How the Prediction Works

1. The image is read with OpenCV.
2. It is resized to **128 × 128** pixels and normalised (pixel values divided by 255).
3. The CNN outputs a probability score.
4. A score of **0.5 or below → With Mask**, above 0.5 → Without Mask.

---

## 📸 Screenshots

- [Screenshot 1](https://drive.google.com/file/d/10VMXaNPREa_Yt5zFp4GHWd4lkGskke40/view?usp=drive_link)
- [Screenshot 2](https://drive.google.com/file/d/1Zcy4svtQAvf2KzcwuOoKT7a3Kcmf3F86/view?usp=drive_link)
- [Screenshot 3](https://drive.google.com/file/d/1GjPTnJzODav83EJZ5NsnE1hM1Cs3NdbT/view?usp=drive_link)

---

## 📊 Results

> Add your final scores here from `CNN.ipynb`.

| Dataset | Accuracy | Loss |
|---|---|---|
| Train | – | – |
| Validation | – | – |
| Test | – | – |

---

## 🔭 Future Improvements

- Real-time detection using a webcam
- Detect multiple faces in one image (face detection plus classification)
- Add a third class for incorrectly worn masks
- Try transfer learning (MobileNetV2) for higher accuracy
- Deploy on Streamlit Community Cloud

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👤 Author

**Muzzammil**
GitHub: [@muzzammil03](https://github.com/muzzammil03)

---

⭐ If you found this project useful, please give it a star!
