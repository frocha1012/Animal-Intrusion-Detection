
# 🐄 Animal Intrusion Detection (YOLOv5)

This project uses a YOLOv5 model to detect **wild and domestic animals** in images or live video.  
It is based on the [Animal-Intrusion-Detection repo](https://github.com/SaiSwarup27/Animal-Intrusion-Detection), and expands it with:

- ✅ A web app built with Flask (styled with Bootstrap)
- ✅ A simple Python desktop GUI (Tkinter)
- ✅ A camera-based detection script (original from repo)

---

## 🧠 Overview of Tools

| Mode          | File       | Description                                                                 |
|---------------|------------|-----------------------------------------------------------------------------|
| 🧪 Web App     | `main.py`  | Upload 2 images, see detections and bounding boxes in browser               |
| 🖥 Desktop GUI | `app.py`   | Simple windowed app with image upload and label display                     |
| 🎥 Camera Mode | `camera.py`| Original webcam detection using YOLOv5                                      |

Model used: `yolov5/best.pt` (included in the repo)

---

## 🌐 Web App (Flask)

### 📦 Dependencies

```bash
pip install flask torch torchvision pillow opencv-python
```

### ▶️ How to Run

```bash
python main.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

### 🖼 Features
- Upload 2 images at once
- Automatically saves and displays **bounding boxes**
- Shows labels + confidence
- Responsive layout via Bootstrap
- Annotated images saved inside `static/uploads/`

---

## 🖥 Desktop GUI (Tkinter)

### 📦 Dependencies

```bash
pip install torch torchvision pillow opencv-python
```

### ▶️ How to Run

```bash
python app.py
```

- Upload Image 1 and Image 2
- See side-by-side image previews
- Detected animal names and confidence appear in listboxes

> This version works well, but is visually basic (uses native widgets only).

---

## 🎥 Camera Detection

### ▶️ How to Run

```bash
python camera.py
```

- Starts your webcam and runs live YOLOv5 detection
- Bounding boxes and labels appear in real-time
- Great for use in farms, barns, zoos, etc.

---

## 🔧 Code Modifications from Original Repo

### ✅ 1. Web Interface + Image Saving

**New files added:**
- `main.py` — Flask web server
- `templates/index.html` — HTML form for uploading 2 images
- `static/uploads/` — Stores both uploaded and annotated images

**Code added in `main.py`:**
```python
results.save(save_dir=UPLOAD_FOLDER)
```
→ This saves the image with bounding boxes drawn by YOLOv5.

---

### ✅ 2. Desktop App Added

**New file:**
- `app.py` — Built with `tkinter`, lets you select 2 images and shows detected labels per image.

---

### ✅ 3. 🔥 OpenCV Bounding Box Crash Fixed

If you saw this error in YOLO:
```
cv2.error: img marked as output argument, but provided NumPy array marked as readonly
```

It’s caused by YOLO trying to draw on a read-only NumPy array.

✅ **Fix made inside: `yolov5/utils/plots.py`**
- Find `class Annotator` and replace:
```python
self.im = im
```
- With this:
```python
self.im = im.copy()  # Fixes readonly OpenCV error
```

---

### ✅ 4. `common.py` involvement

**File affected during image save:**
- `yolov5/models/common.py` is used internally by `results.save()` and `DetectMultiBackend`.

No edits were made here, but it’s **executed during image annotation**.

---

## 📁 Folder Structure

```
animal-intrusion-detection/
├── app.py                 ← Desktop GUI app
├── main.py                ← Flask Web App
├── camera.py              ← Webcam live detection
├── yolov5/
│   ├── best.pt            ← Trained model
│   ├── utils/plots.py     ← MODIFIED (OpenCV fix)
│   └── models/common.py   ← Used by YOLO saving pipeline
├── static/uploads/        ← Web upload + output images
├── templates/index.html   ← Web form UI
```

---

## 🙏 Credits

- **YOLOv5 by Ultralytics** – https://github.com/ultralytics/yolov5  
- **Original Repo** – https://github.com/SaiSwarup27/Animal-Intrusion-Detection  
- **Fork & Enhancements** – [frocha1012](https://github.com/frocha1012)

---

## ✅ Status

All 3 modes are fully working:

- Web: ✔ Annotates images, shows labels, works on any browser
- Desktop: ✔ Functional, minimal
- Camera: ✔ Live detection with bounding boxes

Ready to test, fork, or deploy.
