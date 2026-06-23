import tkinter as tk
from tkinter import filedialog
from PIL import Image
import tensorflow as tf
import numpy as np

# ==========================================
# THE ULTIMATE BUG FIX: Monkey-Patching
# ==========================================
# Save a reference to TensorFlow's original Dense initialization function
original_dense_init = tf.keras.layers.Dense.__init__

# Create our own version of the initialization function
def patched_dense_init(self, *args, **kwargs):
    # Catch and destroy the rogue Keras 3 variable before it crashes
    kwargs.pop('quantization_config', None)
    # Pass everything else back to the original TensorFlow function
    original_dense_init(self, *args, **kwargs)

# Force TensorFlow to use our patched function instead of its own!
tf.keras.layers.Dense.__init__ = patched_dense_init
# ==========================================

# Now we can load the model completely normally!
model = tf.keras.models.load_model("brain_tumor_model_final.keras")

def predict_image():
    # Open File Dialog
    file_path = filedialog.askopenfilename()
    
    # Safety check: Stop if no file is selected
    if not file_path:
        return

    # Process the Image
    img = Image.open(file_path)
    img = img.resize((224, 224))
    img = np.array(img)
    
    # Convert grayscale to RGB if necessary
    if len(img.shape) == 2:
        img = np.stack((img,)*3, axis=-1)

    # Preprocess specifically for MobileNetV2
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    # Predict
    pred = model.predict(img)[0][0]

    # Update the UI
    if pred > 0.5:
        result.config(text=f"Tumor Detected ({pred:.2f})", fg="red")
    else:
        result.config(text=f"No Tumor ({1-pred:.2f})", fg="green")


# --- Desktop App UI Setup ---
root = tk.Tk()
root.title("Brain Tumor Detector")
root.geometry("300x150") 

button = tk.Button(
    root,
    text="Upload MRI",
    command=predict_image,
    font=("Arial", 12)
)
button.pack(pady=20)

result = tk.Label(
    root,
    text="Awaiting image...",
    font=("Arial", 14, "bold")
)
result.pack()

root.mainloop()
