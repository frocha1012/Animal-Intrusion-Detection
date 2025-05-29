import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import torch

# Load model
model = torch.hub.load('yolov5', 'custom', path='yolov5/best.pt', source='local')
model.conf = 0.25

# App window
root = tk.Tk()
root.title("Animal Intrusion Detection")
root.geometry("1100x600")
root.configure(bg="#f0f0f0")

img1_path = ""
img2_path = ""

def detect_and_display(image_path, result_box, image_label):
    img = Image.open(image_path).resize((400, 250))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    results = model(image_path)
    labels = results.pandas().xyxy[0]

    result_box.delete(0, tk.END)
    if len(labels) == 0:
        result_box.insert(tk.END, "Nenhum animal detectado.")
    else:
        for _, row in labels.iterrows():
            result_box.insert(tk.END, f"{row['name']} ({row['confidence']:.2f})")

def upload_image1():
    global img1_path
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if path:
        img1_path = path
        detect_and_display(img1_path, result_box1, img1_label)

def upload_image2():
    global img2_path
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if path:
        img2_path = path
        detect_and_display(img2_path, result_box2, img2_label)

# Main frame for side-by-side layout
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(pady=20)

# Left section
left_frame = tk.Frame(main_frame, bg="white", padx=10, pady=10)
left_frame.grid(row=0, column=0, padx=20)

btn1 = Button(left_frame, text="Upload Image 1", command=upload_image1, font=("Arial", 10, "bold"))
btn1.pack()
img1_label = Label(left_frame, bg="white")
img1_label.pack(pady=(10, 5))
result_box1 = tk.Listbox(left_frame, height=8, width=50, font=("Courier", 10))
result_box1.pack()

# Right section
right_frame = tk.Frame(main_frame, bg="white", padx=10, pady=10)
right_frame.grid(row=0, column=1, padx=20)

btn2 = Button(right_frame, text="Upload Image 2", command=upload_image2, font=("Arial", 10, "bold"))
btn2.pack()
img2_label = Label(right_frame, bg="white")
img2_label.pack(pady=(10, 5))
result_box2 = tk.Listbox(right_frame, height=8, width=50, font=("Courier", 10))
result_box2.pack()

root.mainloop()
