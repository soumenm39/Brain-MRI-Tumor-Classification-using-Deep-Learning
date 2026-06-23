# Brain MRI Tumor Detection System

A deep learning-based Brain MRI Tumor Detection application developed using TensorFlow and MobileNetV2. The project provides both a simple desktop GUI and an advanced visualization interface for detecting the presence of brain tumors from MRI images.

## Features

* Brain tumor classification from MRI scans
* TensorFlow / Keras deep learning model
* MobileNetV2-based image preprocessing pipeline
* Simple Tkinter GUI for quick testing
* Advanced CustomTkinter GUI
* Confidence score visualization
* Heatmap and overlay visualization
* Standalone executable support using PyInstaller

## Project Structure

```text
Brain-MRI-Tumor-Detection/
│
├── models/
│   └── brain_tumor_model_final.keras
│
├── gui/
│   ├── Python_GUI_Trial.py
│   └── app.py
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

```bash
git clone https://github.com/yourusername/Brain-MRI-Tumor-Detection.git

cd Brain-MRI-Tumor-Detection

pip install -r requirements.txt
```

## Run Simple GUI

```bash
python Python_GUI_Trial.py
```

## Run Advanced GUI

```bash
python app.py
```

## Build Standalone Executable

```bash
pyinstaller --onefile --windowed app.py
```

## Model Information

* Framework: TensorFlow / Keras
* Model Format: `.keras`
* Input Size: 224 × 224 × 3
* Preprocessing: MobileNetV2 preprocessing
* Output: Binary Classification (Tumor / No Tumor)

## Disclaimer

This project is intended for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis.

## Acknowledgements

* TensorFlow & Keras Team
* OpenCV Team
* CustomTkinter Project
* ChatGPT (OpenAI) for assistance with GUI development, debugging, packaging, and software integration during the project workflow.
