import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import cv2
import os
import sys

# =====================================================
# TensorFlow Keras Fix
# =====================================================
original_dense_init = tf.keras.layers.Dense.__init__

def patched_dense_init(self, *args, **kwargs):
    kwargs.pop('quantization_config', None)
    original_dense_init(self, *args, **kwargs)

tf.keras.layers.Dense.__init__ = patched_dense_init

# =====================================================
# Load Model
# =====================================================

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS   # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

MODEL_PATH = resource_path("brain_tumor_model_final.keras")

print("Loading model from:", MODEL_PATH)

model = tf.keras.models.load_model(MODEL_PATH)

# =====================================================
# GUI Setup
# =====================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Brain Tumor Detection System")
app.geometry("1200x700")

# =====================================================
# Functions
# =====================================================

def display_image(img, label):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(img)
    img = img.resize((300, 300))

    photo = ImageTk.PhotoImage(img)

    label.configure(image=photo, text="")
    label.image = photo


def create_heatmap(img):

    # Placeholder heatmap
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    overlay = cv2.addWeighted(
        img,
        0.6,
        heatmap,
        0.4,
        0
    )

    return heatmap, overlay


def predict_image():

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if not file_path:
        return

    original = cv2.imread(file_path)

    if original is None:
        return

    display_image(original, original_label)

    # ==============================
    # Model preprocessing
    # ==============================
    img = cv2.resize(original, (224, 224))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)

    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)[0][0]

    # ==============================
    # Heatmap
    # ==============================
    heatmap, overlay = create_heatmap(original)

    display_image(heatmap, heatmap_label)

    display_image(overlay, overlay_label)

    confidence = pred * 100

    progress.set(confidence / 100)

    if pred > 0.5:

        result_label.configure(
            text=f"TUMOR DETECTED ({confidence:.2f}%)",
            text_color="red"
        )

    else:

        result_label.configure(
            text=f"NO TUMOR ({100-confidence:.2f}%)",
            text_color="green"
        )

    status_label.configure(
        text=f"Loaded: {os.path.basename(file_path)}"
    )


def clear_all():

    for lbl in [original_label, heatmap_label, overlay_label]:
        lbl.configure(image=None, text="No Image")

    result_label.configure(
        text="Awaiting MRI Scan...",
        text_color="white"
    )

    progress.set(0)

    status_label.configure(text="Ready")


# =====================================================
# Title
# =====================================================
title = ctk.CTkLabel(
    app,
    text="Brain Tumor Detection System",
    font=("Arial", 28, "bold")
)

title.pack(pady=10)

# =====================================================
# Image Frame
# =====================================================
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=10)

original_label = ctk.CTkLabel(
    frame,
    text="Original MRI",
    width=300,
    height=300
)

original_label.grid(row=0, column=0, padx=20, pady=20)

heatmap_label = ctk.CTkLabel(
    frame,
    text="Heatmap",
    width=300,
    height=300
)

heatmap_label.grid(row=0, column=1, padx=20)

overlay_label = ctk.CTkLabel(
    frame,
    text="Overlay",
    width=300,
    height=300
)

overlay_label.grid(row=0, column=2, padx=20)

# =====================================================
# Prediction
# =====================================================
result_label = ctk.CTkLabel(
    app,
    text="Awaiting MRI Scan...",
    font=("Arial", 24, "bold")
)

result_label.pack(pady=10)

progress = ctk.CTkProgressBar(app, width=500)
progress.pack(pady=10)
progress.set(0)

# =====================================================
# Buttons
# =====================================================
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

upload_btn = ctk.CTkButton(
    button_frame,
    text="Upload MRI",
    command=predict_image
)

upload_btn.grid(row=0, column=0, padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="Clear",
    command=clear_all
)

clear_btn.grid(row=0, column=1, padx=10)

exit_btn = ctk.CTkButton(
    button_frame,
    text="Exit",
    command=app.destroy
)

exit_btn.grid(row=0, column=2, padx=10)

# =====================================================
# Status Bar
# =====================================================
status_label = ctk.CTkLabel(
    app,
    text="Ready"
)

status_label.pack(side="bottom", pady=5)

app.mainloop()
