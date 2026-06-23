# 🧠 Brain MRI Tumor Detection System

A deep learning-based Brain MRI Tumor Detection application developed using **TensorFlow**, **Keras**, **MobileNetV2**, and **CustomTkinter**. The system provides an intuitive desktop interface for detecting the presence of brain tumors from MRI images while offering visual feedback through confidence scores and image overlays.

---

## 📌 Project Overview

Brain tumors are among the most critical neurological disorders requiring early diagnosis and treatment. This project demonstrates the application of deep learning techniques to assist in the classification of MRI scans into **Tumor** and **No Tumor** categories.

The application includes:

* A trained TensorFlow/Keras classification model
* Simple desktop GUI for rapid testing
* Advanced GUI with image visualization
* Confidence score display
* Heatmap and overlay visualization
* Standalone executable support

---

## 🚀 Features

✅ Brain MRI image classification

✅ Deep learning-based tumor detection

✅ MobileNetV2 preprocessing pipeline

✅ Simple Tkinter GUI

✅ Advanced CustomTkinter GUI

✅ Confidence score visualization

✅ Heatmap and overlay generation

✅ PyInstaller executable support

✅ User-friendly desktop interface

---

# 📷 Application Screenshots

## Main Interface

> Insert screenshot here

<img width="2414" height="1468" alt="image" src="https://github.com/user-attachments/assets/aa6a18b6-06d3-4d0c-9728-c178b0e55735" />

---

## Tumor Detection Example
<img width="2414" height="1472" alt="image" src="https://github.com/user-attachments/assets/a5a869e9-c0db-4e3f-93b9-193195f57fbf" />

---

## No Tumor Example

<img width="2408" height="1470" alt="image" src="https://github.com/user-attachments/assets/51b62674-c6a1-4bc9-8a1b-51910ae3ab61" />

---

## Basics GUI

<img width="818" height="780" alt="image" src="https://github.com/user-attachments/assets/afbe2956-8e62-46dd-b567-0bbbd9810bc7" />

<img width="702" height="610" alt="image" src="https://github.com/user-attachments/assets/e827b9c0-cda7-4af0-b2f1-584346c91e13" />

---

# 🏗 Project Structure

```text
Brain-MRI-Tumor-Detection/
│
├── brain_tumor_model_final.keras
│
├── Python_GUI_Trial.py
│
├── app.py
│
├── screenshots/
│   ├── main_gui.png
│   ├── prediction.png
│   ├── tumor_detected.png
│   ├── no_tumor.png
│   └── heatmap_overlay.png
│
├── requirements.txt
│
└── README.md
```

---

# 🧠 Deep Learning Model

### Framework

* TensorFlow 2.21
* Keras 3.12

### Input

* MRI Brain Scan
* Input Size: 224 × 224 × 3

### Preprocessing

* MobileNetV2 preprocessing

### Output

Binary Classification:

* Tumor
* No Tumor

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Brain-MRI-Tumor-Detection.git

cd Brain-MRI-Tumor-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

## Basic GUI

```bash
python Python_GUI_Trial.py
```

A lightweight interface for quickly testing MRI images.

---

## Advanced GUI

```bash
python app.py
```

Features:

* MRI image preview
* Confidence score
* Heatmap visualization
* Overlay display
* Modern user interface

---

# 📦 Building a Standalone Executable

Using PyInstaller:

```bash
pyinstaller --onefile --windowed app.py
```

The executable will be generated inside:

```text
dist/
```

---

# 📊 Example Workflow

1. Launch the application.
2. Upload an MRI scan.
3. The image is automatically preprocessed.
4. The trained neural network performs inference.
5. The prediction result is displayed.
6. Confidence score and visualization outputs are generated.

---

# 🔬 Applications

* Medical Image Analysis
* Healthcare AI
* Deep Learning Education
* Computer Vision Demonstrations
* Research and Academic Projects

---

# ⚠ Disclaimer

This software is intended for educational, research, and demonstration purposes only.

It is **not a medical device** and should not be used as a substitute for professional medical diagnosis or clinical decision-making.

---

# 👨‍💻 Author

**Soumen Mondal**

Research Scholar
Saha Institute of Nuclear Physics (SINP)
Homi Bhabha National Institute (HBNI), India

LinkedIn:
https://www.linkedin.com/in/soumen-mondal-4b9465b2

---

# 🙏 Acknowledgements

* TensorFlow & Keras Development Team
* OpenCV Development Team
* CustomTkinter Project
* Python Open-Source Community
* OpenAI ChatGPT for assistance in GUI development, debugging, packaging, and software integration during the project workflow.

---

# ⭐ If you find this project useful

Please consider starring the repository and sharing feedback.
