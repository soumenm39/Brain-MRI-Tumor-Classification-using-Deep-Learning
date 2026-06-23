# Brain-MRI-Tumor-Classification-using-Deep-Learning

Brain MRI tumor detection and classification using Convolutional Neural Networks (CNNs) and TensorFlow.

## Overview

This project implements a Deep Learning-based Brain MRI Tumor Classification system using TensorFlow and Convolutional Neural Networks (CNNs). The application analyzes MRI brain scans and predicts whether a tumor is present. The system is designed with a user-friendly graphical interface for easy image upload, visualization, and prediction.

The project supports GPU acceleration using NVIDIA CUDA and TensorFlow, enabling efficient model training and inference.

---

## Features

* Brain MRI image classification
* Deep Convolutional Neural Network (CNN)
* GPU-accelerated training and inference
* Interactive graphical user interface (GUI)
* MRI image visualization
* Prediction confidence scores
* Model saving and loading
* Windows executable deployment using PyInstaller
* TensorFlow Lite conversion support (future deployment)
* Grad-CAM explainability support (planned)

---

## Dataset

The model was trained on publicly available Brain MRI datasets containing:

* Tumor MRI images
* Non-Tumor MRI images

Images were resized and normalized before training.

---

## Model Architecture

The CNN architecture consists of:

* Convolutional Layers
* ReLU Activation
* Max Pooling Layers
* Fully Connected Dense Layers
* Dropout Regularization
* Softmax Output Layer

The architecture was optimized for classification performance while maintaining computational efficiency.

---

## Technologies Used

### Programming Language

* Python 3.10

### Deep Learning

* TensorFlow 2.10.1
* Keras

### Computer Vision

* OpenCV
* NumPy

### Visualization

* Matplotlib

### GUI

* CustomTkinter

### Deployment

* PyInstaller

---

## GPU Configuration

The project was developed and tested using:

* NVIDIA GeForce RTX 4060 Laptop GPU
* CUDA 11.2
* cuDNN 8.1
* TensorFlow 2.10.1

GPU memory growth is enabled to prevent unnecessary memory allocation.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Brain-MRI-Tumor-Classification.git
cd Brain-MRI-Tumor-Classification
```

Create and activate a virtual environment:

```bash
conda create -n BrainMRI python=3.10
conda activate BrainMRI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Launch the GUI:

```bash
python app.py
```

---

## Training the Model

To train the model:

```bash
python train_model.py
```

The trained model will be saved as:

```text
brain_tumor_model_final.keras
```

---

## Project Structure

```text
Brain-MRI-Tumor-Classification/
│
├── dataset/
│   ├── tumor/
│   └── no_tumor/
│
├── models/
│   └── brain_tumor_model_final.keras
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── gui.png
    └── prediction.png
```

---

## Results

The CNN model achieved high classification performance on the validation dataset.

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1 Score

Performance may vary depending on dataset composition and preprocessing.

---

## Future Improvements

* Tumor localization and segmentation
* Grad-CAM explainability visualization
* Multi-class tumor classification
* TensorFlow Lite deployment
* Mobile application support
* Real-time clinical decision support tools

---

## Disclaimer

This project is intended for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis.

---

## Author

**Soumen Mondal**

## Acknowledgments

The graphical user interface (GUI) and portions of the application development were created with the assistance of OpenAI's ChatGPT through interactive coding discussions, debugging support, design suggestions, and code refinement. The final implementation, integration, testing, and customization were performed by the author.

#Credit: TinyML - Tiny Machine Learning at UPenn

Research Fellow (Physics)
Saha Institute of Nuclear Physics (SINP)
Homi Bhabha National Institute (HBNI)

Interests:

* Deep Learning
* Medical Image Analysis
* TinyML
* Embedded AI
* Robotics and Intelligent Systems
